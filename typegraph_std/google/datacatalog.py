from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datacatalog() -> Import:
    datacatalog = HTTPRuntime("https://datacatalog.googleapis.com/")

    renames = {
        "ErrorResponse": "_datacatalog_1_ErrorResponse",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestIn": "_datacatalog_2_GoogleCloudDatacatalogV1ReconcileTagsRequestIn",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestOut": "_datacatalog_3_GoogleCloudDatacatalogV1ReconcileTagsRequestOut",
        "PolicyIn": "_datacatalog_4_PolicyIn",
        "PolicyOut": "_datacatalog_5_PolicyOut",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecIn": "_datacatalog_6_GoogleCloudDatacatalogV1BigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecOut": "_datacatalog_7_GoogleCloudDatacatalogV1BigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseIn": "_datacatalog_8_GoogleCloudDatacatalogV1ListPolicyTagsResponseIn",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseOut": "_datacatalog_9_GoogleCloudDatacatalogV1ListPolicyTagsResponseOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn": "_datacatalog_10_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut": "_datacatalog_11_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut",
        "GoogleCloudDatacatalogV1SearchCatalogResultIn": "_datacatalog_12_GoogleCloudDatacatalogV1SearchCatalogResultIn",
        "GoogleCloudDatacatalogV1SearchCatalogResultOut": "_datacatalog_13_GoogleCloudDatacatalogV1SearchCatalogResultOut",
        "GoogleCloudDatacatalogV1TaxonomyServiceIn": "_datacatalog_14_GoogleCloudDatacatalogV1TaxonomyServiceIn",
        "GoogleCloudDatacatalogV1TaxonomyServiceOut": "_datacatalog_15_GoogleCloudDatacatalogV1TaxonomyServiceOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn": "_datacatalog_16_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut": "_datacatalog_17_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut",
        "GoogleCloudDatacatalogV1PolicyTagIn": "_datacatalog_18_GoogleCloudDatacatalogV1PolicyTagIn",
        "GoogleCloudDatacatalogV1PolicyTagOut": "_datacatalog_19_GoogleCloudDatacatalogV1PolicyTagOut",
        "TestIamPermissionsResponseIn": "_datacatalog_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datacatalog_21_TestIamPermissionsResponseOut",
        "GoogleCloudDatacatalogV1SerializedPolicyTagIn": "_datacatalog_22_GoogleCloudDatacatalogV1SerializedPolicyTagIn",
        "GoogleCloudDatacatalogV1SerializedPolicyTagOut": "_datacatalog_23_GoogleCloudDatacatalogV1SerializedPolicyTagOut",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn": "_datacatalog_24_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut": "_datacatalog_25_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut",
        "GoogleCloudDatacatalogV1UnstarEntryRequestIn": "_datacatalog_26_GoogleCloudDatacatalogV1UnstarEntryRequestIn",
        "GoogleCloudDatacatalogV1UnstarEntryRequestOut": "_datacatalog_27_GoogleCloudDatacatalogV1UnstarEntryRequestOut",
        "GoogleCloudDatacatalogV1TagFieldIn": "_datacatalog_28_GoogleCloudDatacatalogV1TagFieldIn",
        "GoogleCloudDatacatalogV1TagFieldOut": "_datacatalog_29_GoogleCloudDatacatalogV1TagFieldOut",
        "GoogleCloudDatacatalogV1ServiceSpecIn": "_datacatalog_30_GoogleCloudDatacatalogV1ServiceSpecIn",
        "GoogleCloudDatacatalogV1ServiceSpecOut": "_datacatalog_31_GoogleCloudDatacatalogV1ServiceSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn": "_datacatalog_32_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut": "_datacatalog_33_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut",
        "GoogleCloudDatacatalogV1TagTemplateFieldIn": "_datacatalog_34_GoogleCloudDatacatalogV1TagTemplateFieldIn",
        "GoogleCloudDatacatalogV1TagTemplateFieldOut": "_datacatalog_35_GoogleCloudDatacatalogV1TagTemplateFieldOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn": "_datacatalog_36_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut": "_datacatalog_37_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut",
        "GoogleCloudDatacatalogV1ViewSpecIn": "_datacatalog_38_GoogleCloudDatacatalogV1ViewSpecIn",
        "GoogleCloudDatacatalogV1ViewSpecOut": "_datacatalog_39_GoogleCloudDatacatalogV1ViewSpecOut",
        "GoogleCloudDatacatalogV1ImportEntriesRequestIn": "_datacatalog_40_GoogleCloudDatacatalogV1ImportEntriesRequestIn",
        "GoogleCloudDatacatalogV1ImportEntriesRequestOut": "_datacatalog_41_GoogleCloudDatacatalogV1ImportEntriesRequestOut",
        "GoogleCloudDatacatalogV1ColumnSchemaIn": "_datacatalog_42_GoogleCloudDatacatalogV1ColumnSchemaIn",
        "GoogleCloudDatacatalogV1ColumnSchemaOut": "_datacatalog_43_GoogleCloudDatacatalogV1ColumnSchemaOut",
        "GoogleCloudDatacatalogV1EntryIn": "_datacatalog_44_GoogleCloudDatacatalogV1EntryIn",
        "GoogleCloudDatacatalogV1EntryOut": "_datacatalog_45_GoogleCloudDatacatalogV1EntryOut",
        "GoogleCloudDatacatalogV1StarEntryResponseIn": "_datacatalog_46_GoogleCloudDatacatalogV1StarEntryResponseIn",
        "GoogleCloudDatacatalogV1StarEntryResponseOut": "_datacatalog_47_GoogleCloudDatacatalogV1StarEntryResponseOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecIn": "_datacatalog_48_GoogleCloudDatacatalogV1DatabaseTableSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecOut": "_datacatalog_49_GoogleCloudDatacatalogV1DatabaseTableSpecOut",
        "GoogleCloudDatacatalogV1TaggedEntryIn": "_datacatalog_50_GoogleCloudDatacatalogV1TaggedEntryIn",
        "GoogleCloudDatacatalogV1TaggedEntryOut": "_datacatalog_51_GoogleCloudDatacatalogV1TaggedEntryOut",
        "OperationIn": "_datacatalog_52_OperationIn",
        "OperationOut": "_datacatalog_53_OperationOut",
        "GoogleCloudDatacatalogV1SchemaIn": "_datacatalog_54_GoogleCloudDatacatalogV1SchemaIn",
        "GoogleCloudDatacatalogV1SchemaOut": "_datacatalog_55_GoogleCloudDatacatalogV1SchemaOut",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseIn": "_datacatalog_56_GoogleCloudDatacatalogV1ListTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseOut": "_datacatalog_57_GoogleCloudDatacatalogV1ListTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1CrossRegionalSourceIn": "_datacatalog_58_GoogleCloudDatacatalogV1CrossRegionalSourceIn",
        "GoogleCloudDatacatalogV1CrossRegionalSourceOut": "_datacatalog_59_GoogleCloudDatacatalogV1CrossRegionalSourceOut",
        "GoogleCloudDatacatalogV1TagIn": "_datacatalog_60_GoogleCloudDatacatalogV1TagIn",
        "GoogleCloudDatacatalogV1TagOut": "_datacatalog_61_GoogleCloudDatacatalogV1TagOut",
        "GetIamPolicyRequestIn": "_datacatalog_62_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_datacatalog_63_GetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1GcsFileSpecIn": "_datacatalog_64_GoogleCloudDatacatalogV1GcsFileSpecIn",
        "GoogleCloudDatacatalogV1GcsFileSpecOut": "_datacatalog_65_GoogleCloudDatacatalogV1GcsFileSpecOut",
        "GoogleCloudDatacatalogV1EntryGroupIn": "_datacatalog_66_GoogleCloudDatacatalogV1EntryGroupIn",
        "GoogleCloudDatacatalogV1EntryGroupOut": "_datacatalog_67_GoogleCloudDatacatalogV1EntryGroupOut",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseIn": "_datacatalog_68_GoogleCloudDatacatalogV1ListEntryGroupsResponseIn",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseOut": "_datacatalog_69_GoogleCloudDatacatalogV1ListEntryGroupsResponseOut",
        "GoogleCloudDatacatalogV1SystemTimestampsIn": "_datacatalog_70_GoogleCloudDatacatalogV1SystemTimestampsIn",
        "GoogleCloudDatacatalogV1SystemTimestampsOut": "_datacatalog_71_GoogleCloudDatacatalogV1SystemTimestampsOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn": "_datacatalog_72_GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut": "_datacatalog_73_GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut",
        "StatusIn": "_datacatalog_74_StatusIn",
        "StatusOut": "_datacatalog_75_StatusOut",
        "GoogleCloudDatacatalogV1TaxonomyIn": "_datacatalog_76_GoogleCloudDatacatalogV1TaxonomyIn",
        "GoogleCloudDatacatalogV1TaxonomyOut": "_datacatalog_77_GoogleCloudDatacatalogV1TaxonomyOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestIn": "_datacatalog_78_GoogleCloudDatacatalogV1SearchCatalogRequestIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestOut": "_datacatalog_79_GoogleCloudDatacatalogV1SearchCatalogRequestOut",
        "GoogleCloudDatacatalogV1StoragePropertiesIn": "_datacatalog_80_GoogleCloudDatacatalogV1StoragePropertiesIn",
        "GoogleCloudDatacatalogV1StoragePropertiesOut": "_datacatalog_81_GoogleCloudDatacatalogV1StoragePropertiesOut",
        "GoogleCloudDatacatalogV1InlineSourceIn": "_datacatalog_82_GoogleCloudDatacatalogV1InlineSourceIn",
        "GoogleCloudDatacatalogV1InlineSourceOut": "_datacatalog_83_GoogleCloudDatacatalogV1InlineSourceOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn": "_datacatalog_84_GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut": "_datacatalog_85_GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseIn": "_datacatalog_86_GoogleCloudDatacatalogV1ReconcileTagsResponseIn",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseOut": "_datacatalog_87_GoogleCloudDatacatalogV1ReconcileTagsResponseOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn": "_datacatalog_88_GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut": "_datacatalog_89_GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecIn": "_datacatalog_90_GoogleCloudDatacatalogV1DataplexFilesetSpecIn",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecOut": "_datacatalog_91_GoogleCloudDatacatalogV1DataplexFilesetSpecOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn": "_datacatalog_92_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut": "_datacatalog_93_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut",
        "GoogleCloudDatacatalogV1UsageSignalIn": "_datacatalog_94_GoogleCloudDatacatalogV1UsageSignalIn",
        "GoogleCloudDatacatalogV1UsageSignalOut": "_datacatalog_95_GoogleCloudDatacatalogV1UsageSignalOut",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn": "_datacatalog_96_GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut": "_datacatalog_97_GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut",
        "GoogleCloudDatacatalogV1DataSourceIn": "_datacatalog_98_GoogleCloudDatacatalogV1DataSourceIn",
        "GoogleCloudDatacatalogV1DataSourceOut": "_datacatalog_99_GoogleCloudDatacatalogV1DataSourceOut",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataIn": "_datacatalog_100_GoogleCloudDatacatalogV1ImportEntriesMetadataIn",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataOut": "_datacatalog_101_GoogleCloudDatacatalogV1ImportEntriesMetadataOut",
        "GoogleCloudDatacatalogV1ListTagsResponseIn": "_datacatalog_102_GoogleCloudDatacatalogV1ListTagsResponseIn",
        "GoogleCloudDatacatalogV1ListTagsResponseOut": "_datacatalog_103_GoogleCloudDatacatalogV1ListTagsResponseOut",
        "GoogleCloudDatacatalogV1GcsFilesetSpecIn": "_datacatalog_104_GoogleCloudDatacatalogV1GcsFilesetSpecIn",
        "GoogleCloudDatacatalogV1GcsFilesetSpecOut": "_datacatalog_105_GoogleCloudDatacatalogV1GcsFilesetSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn": "_datacatalog_106_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut": "_datacatalog_107_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut",
        "GoogleCloudDatacatalogV1FieldTypeIn": "_datacatalog_108_GoogleCloudDatacatalogV1FieldTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeOut": "_datacatalog_109_GoogleCloudDatacatalogV1FieldTypeOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn": "_datacatalog_110_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut": "_datacatalog_111_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataIn": "_datacatalog_112_GoogleCloudDatacatalogV1ReconcileTagsMetadataIn",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataOut": "_datacatalog_113_GoogleCloudDatacatalogV1ReconcileTagsMetadataOut",
        "GetPolicyOptionsIn": "_datacatalog_114_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_datacatalog_115_GetPolicyOptionsOut",
        "GoogleCloudDatacatalogV1PersonalDetailsIn": "_datacatalog_116_GoogleCloudDatacatalogV1PersonalDetailsIn",
        "GoogleCloudDatacatalogV1PersonalDetailsOut": "_datacatalog_117_GoogleCloudDatacatalogV1PersonalDetailsOut",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecIn": "_datacatalog_118_GoogleCloudDatacatalogV1DataSourceConnectionSpecIn",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecOut": "_datacatalog_119_GoogleCloudDatacatalogV1DataSourceConnectionSpecOut",
        "GoogleCloudDatacatalogV1BigQueryTableSpecIn": "_datacatalog_120_GoogleCloudDatacatalogV1BigQueryTableSpecIn",
        "GoogleCloudDatacatalogV1BigQueryTableSpecOut": "_datacatalog_121_GoogleCloudDatacatalogV1BigQueryTableSpecOut",
        "GoogleCloudDatacatalogV1ListEntriesResponseIn": "_datacatalog_122_GoogleCloudDatacatalogV1ListEntriesResponseIn",
        "GoogleCloudDatacatalogV1ListEntriesResponseOut": "_datacatalog_123_GoogleCloudDatacatalogV1ListEntriesResponseOut",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn": "_datacatalog_124_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut": "_datacatalog_125_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1DumpItemIn": "_datacatalog_126_GoogleCloudDatacatalogV1DumpItemIn",
        "GoogleCloudDatacatalogV1DumpItemOut": "_datacatalog_127_GoogleCloudDatacatalogV1DumpItemOut",
        "GoogleCloudDatacatalogV1CommonUsageStatsIn": "_datacatalog_128_GoogleCloudDatacatalogV1CommonUsageStatsIn",
        "GoogleCloudDatacatalogV1CommonUsageStatsOut": "_datacatalog_129_GoogleCloudDatacatalogV1CommonUsageStatsOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeIn": "_datacatalog_130_GoogleCloudDatacatalogV1FieldTypeEnumTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeOut": "_datacatalog_131_GoogleCloudDatacatalogV1FieldTypeEnumTypeOut",
        "GoogleCloudDatacatalogV1DataplexTableSpecIn": "_datacatalog_132_GoogleCloudDatacatalogV1DataplexTableSpecIn",
        "GoogleCloudDatacatalogV1DataplexTableSpecOut": "_datacatalog_133_GoogleCloudDatacatalogV1DataplexTableSpecOut",
        "GoogleCloudDatacatalogV1DataplexSpecIn": "_datacatalog_134_GoogleCloudDatacatalogV1DataplexSpecIn",
        "GoogleCloudDatacatalogV1DataplexSpecOut": "_datacatalog_135_GoogleCloudDatacatalogV1DataplexSpecOut",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn": "_datacatalog_136_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut": "_datacatalog_137_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut",
        "GoogleCloudDatacatalogV1TagFieldEnumValueIn": "_datacatalog_138_GoogleCloudDatacatalogV1TagFieldEnumValueIn",
        "GoogleCloudDatacatalogV1TagFieldEnumValueOut": "_datacatalog_139_GoogleCloudDatacatalogV1TagFieldEnumValueOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaIn": "_datacatalog_140_GoogleCloudDatacatalogV1PhysicalSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOut": "_datacatalog_141_GoogleCloudDatacatalogV1PhysicalSchemaOut",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentIn": "_datacatalog_142_GoogleCloudDatacatalogV1RoutineSpecArgumentIn",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentOut": "_datacatalog_143_GoogleCloudDatacatalogV1RoutineSpecArgumentOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn": "_datacatalog_144_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut": "_datacatalog_145_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut",
        "SetIamPolicyRequestIn": "_datacatalog_146_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datacatalog_147_SetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1DataplexExternalTableIn": "_datacatalog_148_GoogleCloudDatacatalogV1DataplexExternalTableIn",
        "GoogleCloudDatacatalogV1DataplexExternalTableOut": "_datacatalog_149_GoogleCloudDatacatalogV1DataplexExternalTableOut",
        "GoogleCloudDatacatalogV1RoutineSpecIn": "_datacatalog_150_GoogleCloudDatacatalogV1RoutineSpecIn",
        "GoogleCloudDatacatalogV1RoutineSpecOut": "_datacatalog_151_GoogleCloudDatacatalogV1RoutineSpecOut",
        "GoogleCloudDatacatalogV1UnstarEntryResponseIn": "_datacatalog_152_GoogleCloudDatacatalogV1UnstarEntryResponseIn",
        "GoogleCloudDatacatalogV1UnstarEntryResponseOut": "_datacatalog_153_GoogleCloudDatacatalogV1UnstarEntryResponseOut",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn": "_datacatalog_154_GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut": "_datacatalog_155_GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut",
        "GoogleCloudDatacatalogV1ContactsPersonIn": "_datacatalog_156_GoogleCloudDatacatalogV1ContactsPersonIn",
        "GoogleCloudDatacatalogV1ContactsPersonOut": "_datacatalog_157_GoogleCloudDatacatalogV1ContactsPersonOut",
        "BindingIn": "_datacatalog_158_BindingIn",
        "BindingOut": "_datacatalog_159_BindingOut",
        "TestIamPermissionsRequestIn": "_datacatalog_160_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datacatalog_161_TestIamPermissionsRequestOut",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn": "_datacatalog_162_GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut": "_datacatalog_163_GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut",
        "ListOperationsResponseIn": "_datacatalog_164_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datacatalog_165_ListOperationsResponseOut",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn": "_datacatalog_166_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut": "_datacatalog_167_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut",
        "GoogleCloudDatacatalogV1FilesetSpecIn": "_datacatalog_168_GoogleCloudDatacatalogV1FilesetSpecIn",
        "GoogleCloudDatacatalogV1FilesetSpecOut": "_datacatalog_169_GoogleCloudDatacatalogV1FilesetSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn": "_datacatalog_170_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut": "_datacatalog_171_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut",
        "EmptyIn": "_datacatalog_172_EmptyIn",
        "EmptyOut": "_datacatalog_173_EmptyOut",
        "GoogleCloudDatacatalogV1BusinessContextIn": "_datacatalog_174_GoogleCloudDatacatalogV1BusinessContextIn",
        "GoogleCloudDatacatalogV1BusinessContextOut": "_datacatalog_175_GoogleCloudDatacatalogV1BusinessContextOut",
        "GoogleCloudDatacatalogV1ImportEntriesResponseIn": "_datacatalog_176_GoogleCloudDatacatalogV1ImportEntriesResponseIn",
        "GoogleCloudDatacatalogV1ImportEntriesResponseOut": "_datacatalog_177_GoogleCloudDatacatalogV1ImportEntriesResponseOut",
        "GoogleCloudDatacatalogV1SearchCatalogResponseIn": "_datacatalog_178_GoogleCloudDatacatalogV1SearchCatalogResponseIn",
        "GoogleCloudDatacatalogV1SearchCatalogResponseOut": "_datacatalog_179_GoogleCloudDatacatalogV1SearchCatalogResponseOut",
        "GoogleCloudDatacatalogV1LookerSystemSpecIn": "_datacatalog_180_GoogleCloudDatacatalogV1LookerSystemSpecIn",
        "GoogleCloudDatacatalogV1LookerSystemSpecOut": "_datacatalog_181_GoogleCloudDatacatalogV1LookerSystemSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn": "_datacatalog_182_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut": "_datacatalog_183_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut",
        "GoogleCloudDatacatalogV1UsageStatsIn": "_datacatalog_184_GoogleCloudDatacatalogV1UsageStatsIn",
        "GoogleCloudDatacatalogV1UsageStatsOut": "_datacatalog_185_GoogleCloudDatacatalogV1UsageStatsOut",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecIn": "_datacatalog_186_GoogleCloudDatacatalogV1BigQueryRoutineSpecIn",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecOut": "_datacatalog_187_GoogleCloudDatacatalogV1BigQueryRoutineSpecOut",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn": "_datacatalog_188_GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut": "_datacatalog_189_GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn": "_datacatalog_190_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut": "_datacatalog_191_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut",
        "GoogleCloudDatacatalogV1StarEntryRequestIn": "_datacatalog_192_GoogleCloudDatacatalogV1StarEntryRequestIn",
        "GoogleCloudDatacatalogV1StarEntryRequestOut": "_datacatalog_193_GoogleCloudDatacatalogV1StarEntryRequestOut",
        "GoogleCloudDatacatalogV1SerializedTaxonomyIn": "_datacatalog_194_GoogleCloudDatacatalogV1SerializedTaxonomyIn",
        "GoogleCloudDatacatalogV1SerializedTaxonomyOut": "_datacatalog_195_GoogleCloudDatacatalogV1SerializedTaxonomyOut",
        "ExprIn": "_datacatalog_196_ExprIn",
        "ExprOut": "_datacatalog_197_ExprOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn": "_datacatalog_198_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut": "_datacatalog_199_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut",
        "GoogleCloudDatacatalogV1TableSpecIn": "_datacatalog_200_GoogleCloudDatacatalogV1TableSpecIn",
        "GoogleCloudDatacatalogV1TableSpecOut": "_datacatalog_201_GoogleCloudDatacatalogV1TableSpecOut",
        "GoogleCloudDatacatalogV1TagTemplateIn": "_datacatalog_202_GoogleCloudDatacatalogV1TagTemplateIn",
        "GoogleCloudDatacatalogV1TagTemplateOut": "_datacatalog_203_GoogleCloudDatacatalogV1TagTemplateOut",
        "GoogleCloudDatacatalogV1EntryOverviewIn": "_datacatalog_204_GoogleCloudDatacatalogV1EntryOverviewIn",
        "GoogleCloudDatacatalogV1EntryOverviewOut": "_datacatalog_205_GoogleCloudDatacatalogV1EntryOverviewOut",
        "GoogleCloudDatacatalogV1ContactsIn": "_datacatalog_206_GoogleCloudDatacatalogV1ContactsIn",
        "GoogleCloudDatacatalogV1ContactsOut": "_datacatalog_207_GoogleCloudDatacatalogV1ContactsOut",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn": "_datacatalog_208_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut": "_datacatalog_209_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"] = t.struct(
        {
            "forceDeleteMissing": t.boolean().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "tagTemplate": t.string(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"] = t.struct(
        {
            "forceDeleteMissing": t.boolean().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "tagTemplate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["GoogleCloudDatacatalogV1ListPolicyTagsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListPolicyTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ListPolicyTagsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListPolicyTagsResponseOut"])
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
    types["GoogleCloudDatacatalogV1SearchCatalogResultIn"] = t.struct(
        {
            "fullyQualifiedName": t.string().optional(),
            "searchResultType": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "linkedResource": t.string().optional(),
            "displayName": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "description": t.string().optional(),
            "modifyTime": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResultOut"] = t.struct(
        {
            "fullyQualifiedName": t.string().optional(),
            "searchResultType": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "linkedResource": t.string().optional(),
            "displayName": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "description": t.string().optional(),
            "integratedSystem": t.string().optional(),
            "modifyTime": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
    types["GoogleCloudDatacatalogV1TaxonomyServiceIn"] = t.struct(
        {"name": t.string().optional(), "identity": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyServiceIn"])
    types["GoogleCloudDatacatalogV1TaxonomyServiceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "identity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyServiceOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"])
    types["GoogleCloudDatacatalogV1PolicyTagIn"] = t.struct(
        {
            "displayName": t.string(),
            "parentPolicyTag": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagIn"])
    types["GoogleCloudDatacatalogV1PolicyTagOut"] = t.struct(
        {
            "displayName": t.string(),
            "parentPolicyTag": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "childPolicyTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudDatacatalogV1SerializedPolicyTagIn"] = t.struct(
        {
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "policyTag": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
    types["GoogleCloudDatacatalogV1SerializedPolicyTagOut"] = t.struct(
        {
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "policyTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
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
    types["GoogleCloudDatacatalogV1UnstarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestOut"])
    types["GoogleCloudDatacatalogV1TagFieldIn"] = t.struct(
        {
            "timestampValue": t.string().optional(),
            "richtextValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldIn"])
    types["GoogleCloudDatacatalogV1TagFieldOut"] = t.struct(
        {
            "timestampValue": t.string().optional(),
            "richtextValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "doubleValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "displayName": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"]
            ).optional(),
            "order": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldIn"] = t.struct(
        {
            "isRequired": t.boolean().optional(),
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
            "displayName": t.string().optional(),
            "order": t.integer().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldIn"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldOut"] = t.struct(
        {
            "isRequired": t.boolean().optional(),
            "name": t.string().optional(),
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeOut"]),
            "displayName": t.string().optional(),
            "order": t.integer().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"] = t.struct(
        {"newTagTemplateFieldId": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"] = t.struct(
        {
            "newTagTemplateFieldId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"])
    types["GoogleCloudDatacatalogV1ViewSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecIn"])
    types["GoogleCloudDatacatalogV1ViewSpecOut"] = t.struct(
        {
            "viewQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecOut"])
    types["GoogleCloudDatacatalogV1ImportEntriesRequestIn"] = t.struct(
        {"gcsBucketPath": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesRequestOut"] = t.struct(
        {
            "gcsBucketPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestOut"])
    types["GoogleCloudDatacatalogV1ColumnSchemaIn"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"]
            ).optional(),
            "gcRule": t.string().optional(),
            "column": t.string(),
            "defaultValue": t.string().optional(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
            ).optional(),
            "mode": t.string().optional(),
            "description": t.string().optional(),
            "highestIndexingType": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaOut"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"]
            ).optional(),
            "gcRule": t.string().optional(),
            "column": t.string(),
            "defaultValue": t.string().optional(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
            ).optional(),
            "mode": t.string().optional(),
            "description": t.string().optional(),
            "highestIndexingType": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
    types["GoogleCloudDatacatalogV1EntryIn"] = t.struct(
        {
            "type": t.string().optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "userSpecifiedType": t.string().optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextIn"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
            ).optional(),
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
            ).optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
            ).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaIn"]).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
            ).optional(),
            "description": t.string().optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalIn"]
            ).optional(),
            "userSpecifiedSystem": t.string().optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
            ).optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
            ).optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryIn"])
    types["GoogleCloudDatacatalogV1EntryOut"] = t.struct(
        {
            "type": t.string().optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "userSpecifiedType": t.string().optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextOut"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecOut"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "bigqueryDateShardedSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"]
            ).optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"]
            ).optional(),
            "personalDetails": t.proxy(
                renames["GoogleCloudDatacatalogV1PersonalDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"]
            ).optional(),
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecOut"]
            ).optional(),
            "dataSource": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceOut"]
            ).optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecOut"]
            ).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaOut"]).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecOut"]
            ).optional(),
            "description": t.string().optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalOut"]
            ).optional(),
            "integratedSystem": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecOut"]
            ).optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"]
            ).optional(),
            "bigqueryTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOut"])
    types["GoogleCloudDatacatalogV1StarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1StarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["GoogleCloudDatacatalogV1ListTaxonomiesResponseIn"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTaxonomiesResponseIn"])
    types["GoogleCloudDatacatalogV1ListTaxonomiesResponseOut"] = t.struct(
        {
            "taxonomies": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTaxonomiesResponseOut"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceIn"] = t.struct(
        {"taxonomy": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceIn"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceOut"] = t.struct(
        {"taxonomy": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceOut"])
    types["GoogleCloudDatacatalogV1TagIn"] = t.struct(
        {
            "column": t.string().optional(),
            "name": t.string().optional(),
            "template": t.string(),
            "fields": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagIn"])
    types["GoogleCloudDatacatalogV1TagOut"] = t.struct(
        {
            "column": t.string().optional(),
            "name": t.string().optional(),
            "template": t.string(),
            "templateDisplayName": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1GcsFileSpecIn"] = t.struct(
        {"filePath": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecIn"])
    types["GoogleCloudDatacatalogV1GcsFileSpecOut"] = t.struct(
        {
            "filePath": t.string(),
            "sizeBytes": t.string().optional(),
            "gcsTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecOut"])
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
    types["GoogleCloudDatacatalogV1ListEntryGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entryGroups": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseIn"])
    types["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entryGroups": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"])
    types["GoogleCloudDatacatalogV1SystemTimestampsIn"] = t.struct(
        {"createTime": t.string().optional(), "updateTime": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsIn"])
    types["GoogleCloudDatacatalogV1SystemTimestampsOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"] = t.struct(
        {
            "includeProjectIds": t.array(t.string()).optional(),
            "restrictedLocations": t.array(t.string()).optional(),
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "starredOnly": t.boolean().optional(),
            "includeOrgIds": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"] = t.struct(
        {
            "includeProjectIds": t.array(t.string()).optional(),
            "restrictedLocations": t.array(t.string()).optional(),
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "starredOnly": t.boolean().optional(),
            "includeOrgIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"])
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
    types["GoogleCloudDatacatalogV1TaxonomyIn"] = t.struct(
        {
            "displayName": t.string(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyIn"])
    types["GoogleCloudDatacatalogV1TaxonomyOut"] = t.struct(
        {
            "taxonomyTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "name": t.string().optional(),
            "service": t.proxy(
                renames["GoogleCloudDatacatalogV1TaxonomyServiceOut"]
            ).optional(),
            "displayName": t.string(),
            "policyTagCount": t.integer().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestIn"] = t.struct(
        {
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
            ),
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestOut"] = t.struct(
        {
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"]
            ),
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestOut"])
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
    types["GoogleCloudDatacatalogV1ReconcileTagsResponseIn"] = t.struct(
        {
            "createdTagsCount": t.string().optional(),
            "deletedTagsCount": t.string().optional(),
            "updatedTagsCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsResponseOut"] = t.struct(
        {
            "createdTagsCount": t.string().optional(),
            "deletedTagsCount": t.string().optional(),
            "updatedTagsCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsResponseOut"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn"] = t.struct(
        {
            "crossRegionalSource": t.proxy(
                renames["GoogleCloudDatacatalogV1CrossRegionalSourceIn"]
            ).optional(),
            "inlineSource": t.proxy(
                renames["GoogleCloudDatacatalogV1InlineSourceIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn"])
    types["GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut"] = t.struct(
        {
            "crossRegionalSource": t.proxy(
                renames["GoogleCloudDatacatalogV1CrossRegionalSourceOut"]
            ).optional(),
            "inlineSource": t.proxy(
                renames["GoogleCloudDatacatalogV1InlineSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut"])
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
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"] = t.struct(
        {
            "viewType": t.string().optional(),
            "baseTable": t.string().optional(),
            "sqlQuery": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"] = t.struct(
        {
            "viewType": t.string().optional(),
            "baseTable": t.string().optional(),
            "sqlQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"])
    types["GoogleCloudDatacatalogV1UsageSignalIn"] = t.struct(
        {
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "updateTime": t.string().optional(),
            "favoriteCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalIn"])
    types["GoogleCloudDatacatalogV1UsageSignalOut"] = t.struct(
        {
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "updateTime": t.string().optional(),
            "usageWithinTimeRange": t.struct({"_": t.string().optional()}).optional(),
            "favoriteCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalOut"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"] = t.struct(
        {"contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsIn"])}
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"] = t.struct(
        {
            "contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"])
    types["GoogleCloudDatacatalogV1DataSourceIn"] = t.struct(
        {
            "service": t.string().optional(),
            "resource": t.string().optional(),
            "storageProperties": t.proxy(
                renames["GoogleCloudDatacatalogV1StoragePropertiesIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceIn"])
    types["GoogleCloudDatacatalogV1DataSourceOut"] = t.struct(
        {
            "service": t.string().optional(),
            "resource": t.string().optional(),
            "sourceEntry": t.string().optional(),
            "storageProperties": t.proxy(
                renames["GoogleCloudDatacatalogV1StoragePropertiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataSourceOut"])
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
    types["GoogleCloudDatacatalogV1GcsFilesetSpecIn"] = t.struct(
        {"filePatterns": t.array(t.string())}
    ).named(renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"])
    types["GoogleCloudDatacatalogV1GcsFilesetSpecOut"] = t.struct(
        {
            "sampleGcsFileSpecs": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1GcsFileSpecOut"])
            ).optional(),
            "filePatterns": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1GcsFilesetSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"])
    types["GoogleCloudDatacatalogV1FieldTypeIn"] = t.struct(
        {
            "enumType": t.proxy(
                renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeIn"]
            ).optional(),
            "primitiveType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeIn"])
    types["GoogleCloudDatacatalogV1FieldTypeOut"] = t.struct(
        {
            "enumType": t.proxy(
                renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeOut"]
            ).optional(),
            "primitiveType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GoogleCloudDatacatalogV1PersonalDetailsIn"] = t.struct(
        {"starTime": t.string().optional(), "starred": t.boolean().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PersonalDetailsIn"])
    types["GoogleCloudDatacatalogV1PersonalDetailsOut"] = t.struct(
        {
            "starTime": t.string().optional(),
            "starred": t.boolean().optional(),
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
    types["GoogleCloudDatacatalogV1BigQueryTableSpecIn"] = t.struct(
        {
            "tableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1TableSpecIn"]
            ).optional(),
            "viewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ViewSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryTableSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryTableSpecOut"] = t.struct(
        {
            "tableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1TableSpecOut"]
            ).optional(),
            "viewSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ViewSpecOut"]
            ).optional(),
            "tableSourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"])
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
    types["GoogleCloudDatacatalogV1CommonUsageStatsIn"] = t.struct(
        {"viewCount": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsIn"])
    types["GoogleCloudDatacatalogV1CommonUsageStatsOut"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsOut"])
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
    types["GoogleCloudDatacatalogV1DataplexTableSpecIn"] = t.struct(
        {
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecIn"]
            ).optional(),
            "externalTables": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1DataplexExternalTableIn"])
            ).optional(),
            "userManaged": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexTableSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexTableSpecOut"] = t.struct(
        {
            "dataplexSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataplexSpecOut"]
            ).optional(),
            "externalTables": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1DataplexExternalTableOut"])
            ).optional(),
            "userManaged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexTableSpecOut"])
    types["GoogleCloudDatacatalogV1DataplexSpecIn"] = t.struct(
        {
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"]
            ).optional(),
            "asset": t.string().optional(),
            "compressionFormat": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexSpecOut"] = t.struct(
        {
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"]
            ).optional(),
            "asset": t.string().optional(),
            "compressionFormat": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecOut"])
    types["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"] = t.struct(
        {
            "databaseVersion": t.string().optional(),
            "sqlEngine": t.string().optional(),
            "instanceHost": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"])
    types["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"] = t.struct(
        {
            "databaseVersion": t.string().optional(),
            "sqlEngine": t.string().optional(),
            "instanceHost": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaIn"] = t.struct(
        {
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"]
            ).optional(),
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"]
            ).optional(),
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOut"] = t.struct(
        {
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"]
            ).optional(),
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"]
            ).optional(),
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"] = t.struct(
        {
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"] = t.struct(
        {
            "mode": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1DataplexExternalTableIn"] = t.struct(
        {
            "dataCatalogEntry": t.string().optional(),
            "system": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "googleCloudResource": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableIn"])
    types["GoogleCloudDatacatalogV1DataplexExternalTableOut"] = t.struct(
        {
            "dataCatalogEntry": t.string().optional(),
            "system": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "googleCloudResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecIn"] = t.struct(
        {
            "language": t.string().optional(),
            "returnType": t.string().optional(),
            "definitionBody": t.string().optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
            ).optional(),
            "routineType": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecOut"] = t.struct(
        {
            "language": t.string().optional(),
            "returnType": t.string().optional(),
            "definitionBody": t.string().optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
            ).optional(),
            "routineType": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecOut"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"] = t.struct(
        {"instanceDisplayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"] = t.struct(
        {
            "instanceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"])
    types["GoogleCloudDatacatalogV1ContactsPersonIn"] = t.struct(
        {"designation": t.string().optional(), "email": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ContactsPersonIn"])
    types["GoogleCloudDatacatalogV1ContactsPersonOut"] = t.struct(
        {
            "designation": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ContactsPersonOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"] = t.struct(
        {
            "shardCount": t.string().optional(),
            "latestShardResource": t.string().optional(),
            "dataset": t.string().optional(),
            "tablePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudDatacatalogV1BusinessContextIn"] = t.struct(
        {
            "entryOverview": t.proxy(
                renames["GoogleCloudDatacatalogV1EntryOverviewIn"]
            ).optional(),
            "contacts": t.proxy(
                renames["GoogleCloudDatacatalogV1ContactsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BusinessContextIn"])
    types["GoogleCloudDatacatalogV1BusinessContextOut"] = t.struct(
        {
            "entryOverview": t.proxy(
                renames["GoogleCloudDatacatalogV1EntryOverviewOut"]
            ).optional(),
            "contacts": t.proxy(
                renames["GoogleCloudDatacatalogV1ContactsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BusinessContextOut"])
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
    types["GoogleCloudDatacatalogV1SearchCatalogResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "unreachable": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "unreachable": t.array(t.string()).optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseOut"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecIn"] = t.struct(
        {
            "parentViewDisplayName": t.string().optional(),
            "parentInstanceId": t.string().optional(),
            "parentViewId": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
            "parentModelId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecOut"] = t.struct(
        {
            "parentViewDisplayName": t.string().optional(),
            "parentInstanceId": t.string().optional(),
            "parentViewId": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
            "parentModelId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"])
    types["GoogleCloudDatacatalogV1UsageStatsIn"] = t.struct(
        {
            "totalCancellations": t.number().optional(),
            "totalFailures": t.number().optional(),
            "totalCompletions": t.number().optional(),
            "totalExecutionTimeForCompletionsMillis": t.number().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageStatsIn"])
    types["GoogleCloudDatacatalogV1UsageStatsOut"] = t.struct(
        {
            "totalCancellations": t.number().optional(),
            "totalFailures": t.number().optional(),
            "totalCompletions": t.number().optional(),
            "totalExecutionTimeForCompletionsMillis": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageStatsOut"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"] = t.struct(
        {"importedLibraries": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"] = t.struct(
        {
            "importedLibraries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"])
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
    types[
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn"
    ] = t.struct(
        {
            "linkedResource": t.string().optional(),
            "displayName": t.string().optional(),
            "location": t.string().optional(),
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
            "displayName": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut"
        ]
    )
    types["GoogleCloudDatacatalogV1StarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1StarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestOut"])
    types["GoogleCloudDatacatalogV1SerializedTaxonomyIn"] = t.struct(
        {
            "displayName": t.string(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
            "description": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"])
    types["GoogleCloudDatacatalogV1SerializedTaxonomyOut"] = t.struct(
        {
            "displayName": t.string(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "description": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"])
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
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"] = t.struct(
        {"displayName": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"] = t.struct(
        {
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"])
    types["GoogleCloudDatacatalogV1TableSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TableSpecIn"])
    types["GoogleCloudDatacatalogV1TableSpecOut"] = t.struct(
        {
            "groupedEntry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TableSpecOut"])
    types["GoogleCloudDatacatalogV1TagTemplateIn"] = t.struct(
        {
            "isPubliclyReadable": t.boolean().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateIn"])
    types["GoogleCloudDatacatalogV1TagTemplateOut"] = t.struct(
        {
            "isPubliclyReadable": t.boolean().optional(),
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateOut"])
    types["GoogleCloudDatacatalogV1EntryOverviewIn"] = t.struct(
        {"overview": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewIn"])
    types["GoogleCloudDatacatalogV1EntryOverviewOut"] = t.struct(
        {
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewOut"])
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
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"])

    functions = {}
    functions["projectsLocationsTagTemplatesCreate"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesSetIamPolicy"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesDelete"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesGetIamPolicy"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesPatch"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesGet"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesTestIamPermissions"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesFieldsDelete"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "isRequired": t.boolean().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsRename"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "isRequired": t.boolean().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsCreate"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "isRequired": t.boolean().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsPatch"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "isRequired": t.boolean().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
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
    functions["projectsLocationsOperationsDelete"] = datacatalog.post(
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
    functions["projectsLocationsOperationsList"] = datacatalog.post(
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
    functions["projectsLocationsTaxonomiesCreate"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesExport"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGet"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGetIamPolicy"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesTestIamPermissions"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesDelete"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesImport"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesReplace"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesSetIamPolicy"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesList"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPatch"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "activatedPolicyTypes": t.array(t.string()).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TaxonomyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsDelete"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsSetIamPolicy"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGet"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsList"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsPatch"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsCreate"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTaxonomiesPolicyTagsTestIamPermissions"
    ] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGetIamPolicy"] = datacatalog.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsSetIamPolicy"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGetIamPolicy"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsCreate"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTestIamPermissions"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsPatch"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsDelete"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGet"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsList"] = datacatalog.get(
        "v1/{parent}/entryGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListEntryGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsDelete"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsCreate"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsPatch"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsList"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesTestIamPermissions"
    ] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesUnstar"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryContacts"
    ] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesGetIamPolicy"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesDelete"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesStar"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesCreate"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesGet"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesList"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesImport"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryOverview"
    ] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesPatch"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "type": t.string().optional(),
                "gcsFilesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "userSpecifiedType": t.string().optional(),
                "businessContext": t.proxy(
                    renames["GoogleCloudDatacatalogV1BusinessContextIn"]
                ).optional(),
                "linkedResource": t.string().optional(),
                "filesetSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
                ).optional(),
                "fullyQualifiedName": t.string().optional(),
                "sqlDatabaseSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "cloudBigtableSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
                ).optional(),
                "routineSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
                ).optional(),
                "databaseTableSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
                ).optional(),
                "schema": t.proxy(
                    renames["GoogleCloudDatacatalogV1SchemaIn"]
                ).optional(),
                "serviceSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
                ).optional(),
                "description": t.string().optional(),
                "usageSignal": t.proxy(
                    renames["GoogleCloudDatacatalogV1UsageSignalIn"]
                ).optional(),
                "userSpecifiedSystem": t.string().optional(),
                "dataSourceConnectionSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
                ).optional(),
                "sourceSystemTimestamps": t.proxy(
                    renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
                ).optional(),
                "lookerSystemSpec": t.proxy(
                    renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsDelete"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsCreate"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsPatch"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsReconcile"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesTagsList"] = datacatalog.get(
        "v1/{parent}/tags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesLookup"] = datacatalog.get(
        "v1/entries:lookup",
        t.struct(
            {
                "fullyQualifiedName": t.string().optional(),
                "linkedResource": t.string().optional(),
                "sqlResource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["catalogSearch"] = datacatalog.post(
        "v1/catalog:search",
        t.struct(
            {
                "scope": t.proxy(
                    renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
                ),
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
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
        importer="datacatalog", renames=renames, types=types, functions=functions
    )
