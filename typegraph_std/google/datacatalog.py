from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datacatalog():
    datacatalog = HTTPRuntime("https://datacatalog.googleapis.com/")

    renames = {
        "ErrorResponse": "_datacatalog_1_ErrorResponse",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecIn": "_datacatalog_2_GoogleCloudDatacatalogV1BigQueryRoutineSpecIn",
        "GoogleCloudDatacatalogV1BigQueryRoutineSpecOut": "_datacatalog_3_GoogleCloudDatacatalogV1BigQueryRoutineSpecOut",
        "GoogleCloudDatacatalogV1RoutineSpecIn": "_datacatalog_4_GoogleCloudDatacatalogV1RoutineSpecIn",
        "GoogleCloudDatacatalogV1RoutineSpecOut": "_datacatalog_5_GoogleCloudDatacatalogV1RoutineSpecOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecIn": "_datacatalog_6_GoogleCloudDatacatalogV1DatabaseTableSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecOut": "_datacatalog_7_GoogleCloudDatacatalogV1DatabaseTableSpecOut",
        "GoogleCloudDatacatalogV1SystemTimestampsIn": "_datacatalog_8_GoogleCloudDatacatalogV1SystemTimestampsIn",
        "GoogleCloudDatacatalogV1SystemTimestampsOut": "_datacatalog_9_GoogleCloudDatacatalogV1SystemTimestampsOut",
        "GoogleCloudDatacatalogV1UnstarEntryRequestIn": "_datacatalog_10_GoogleCloudDatacatalogV1UnstarEntryRequestIn",
        "GoogleCloudDatacatalogV1UnstarEntryRequestOut": "_datacatalog_11_GoogleCloudDatacatalogV1UnstarEntryRequestOut",
        "ExprIn": "_datacatalog_12_ExprIn",
        "ExprOut": "_datacatalog_13_ExprOut",
        "GoogleCloudDatacatalogV1FieldTypeIn": "_datacatalog_14_GoogleCloudDatacatalogV1FieldTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeOut": "_datacatalog_15_GoogleCloudDatacatalogV1FieldTypeOut",
        "GoogleCloudDatacatalogV1TableSpecIn": "_datacatalog_16_GoogleCloudDatacatalogV1TableSpecIn",
        "GoogleCloudDatacatalogV1TableSpecOut": "_datacatalog_17_GoogleCloudDatacatalogV1TableSpecOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeIn": "_datacatalog_18_GoogleCloudDatacatalogV1FieldTypeEnumTypeIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeOut": "_datacatalog_19_GoogleCloudDatacatalogV1FieldTypeEnumTypeOut",
        "BindingIn": "_datacatalog_20_BindingIn",
        "BindingOut": "_datacatalog_21_BindingOut",
        "GoogleCloudDatacatalogV1SerializedTaxonomyIn": "_datacatalog_22_GoogleCloudDatacatalogV1SerializedTaxonomyIn",
        "GoogleCloudDatacatalogV1SerializedTaxonomyOut": "_datacatalog_23_GoogleCloudDatacatalogV1SerializedTaxonomyOut",
        "GoogleCloudDatacatalogV1EntryOverviewIn": "_datacatalog_24_GoogleCloudDatacatalogV1EntryOverviewIn",
        "GoogleCloudDatacatalogV1EntryOverviewOut": "_datacatalog_25_GoogleCloudDatacatalogV1EntryOverviewOut",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn": "_datacatalog_26_GoogleCloudDatacatalogV1BigQueryDateShardedSpecIn",
        "GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut": "_datacatalog_27_GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecIn": "_datacatalog_28_GoogleCloudDatacatalogV1DataSourceConnectionSpecIn",
        "GoogleCloudDatacatalogV1DataSourceConnectionSpecOut": "_datacatalog_29_GoogleCloudDatacatalogV1DataSourceConnectionSpecOut",
        "TestIamPermissionsRequestIn": "_datacatalog_30_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datacatalog_31_TestIamPermissionsRequestOut",
        "GoogleCloudDatacatalogV1InlineSourceIn": "_datacatalog_32_GoogleCloudDatacatalogV1InlineSourceIn",
        "GoogleCloudDatacatalogV1InlineSourceOut": "_datacatalog_33_GoogleCloudDatacatalogV1InlineSourceOut",
        "StatusIn": "_datacatalog_34_StatusIn",
        "StatusOut": "_datacatalog_35_StatusOut",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseIn": "_datacatalog_36_GoogleCloudDatacatalogV1ListEntryGroupsResponseIn",
        "GoogleCloudDatacatalogV1ListEntryGroupsResponseOut": "_datacatalog_37_GoogleCloudDatacatalogV1ListEntryGroupsResponseOut",
        "GoogleCloudDatacatalogV1StarEntryResponseIn": "_datacatalog_38_GoogleCloudDatacatalogV1StarEntryResponseIn",
        "GoogleCloudDatacatalogV1StarEntryResponseOut": "_datacatalog_39_GoogleCloudDatacatalogV1StarEntryResponseOut",
        "GoogleCloudDatacatalogV1UsageStatsIn": "_datacatalog_40_GoogleCloudDatacatalogV1UsageStatsIn",
        "GoogleCloudDatacatalogV1UsageStatsOut": "_datacatalog_41_GoogleCloudDatacatalogV1UsageStatsOut",
        "GoogleCloudDatacatalogV1SchemaIn": "_datacatalog_42_GoogleCloudDatacatalogV1SchemaIn",
        "GoogleCloudDatacatalogV1SchemaOut": "_datacatalog_43_GoogleCloudDatacatalogV1SchemaOut",
        "GoogleCloudDatacatalogV1SerializedPolicyTagIn": "_datacatalog_44_GoogleCloudDatacatalogV1SerializedPolicyTagIn",
        "GoogleCloudDatacatalogV1SerializedPolicyTagOut": "_datacatalog_45_GoogleCloudDatacatalogV1SerializedPolicyTagOut",
        "TestIamPermissionsResponseIn": "_datacatalog_46_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datacatalog_47_TestIamPermissionsResponseOut",
        "GoogleCloudDatacatalogV1CrossRegionalSourceIn": "_datacatalog_48_GoogleCloudDatacatalogV1CrossRegionalSourceIn",
        "GoogleCloudDatacatalogV1CrossRegionalSourceOut": "_datacatalog_49_GoogleCloudDatacatalogV1CrossRegionalSourceOut",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn": "_datacatalog_50_GoogleCloudDatacatalogV1ExportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut": "_datacatalog_51_GoogleCloudDatacatalogV1ExportTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn": "_datacatalog_52_GoogleCloudDatacatalogV1ImportTaxonomiesRequestIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut": "_datacatalog_53_GoogleCloudDatacatalogV1ImportTaxonomiesRequestOut",
        "GoogleCloudDatacatalogV1CommonUsageStatsIn": "_datacatalog_54_GoogleCloudDatacatalogV1CommonUsageStatsIn",
        "GoogleCloudDatacatalogV1CommonUsageStatsOut": "_datacatalog_55_GoogleCloudDatacatalogV1CommonUsageStatsOut",
        "GoogleCloudDatacatalogV1GcsFileSpecIn": "_datacatalog_56_GoogleCloudDatacatalogV1GcsFileSpecIn",
        "GoogleCloudDatacatalogV1GcsFileSpecOut": "_datacatalog_57_GoogleCloudDatacatalogV1GcsFileSpecOut",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn": "_datacatalog_58_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn",
        "GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut": "_datacatalog_59_GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn": "_datacatalog_60_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut": "_datacatalog_61_GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn": "_datacatalog_62_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn",
        "GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut": "_datacatalog_63_GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut",
        "GoogleCloudDatacatalogV1DataplexTableSpecIn": "_datacatalog_64_GoogleCloudDatacatalogV1DataplexTableSpecIn",
        "GoogleCloudDatacatalogV1DataplexTableSpecOut": "_datacatalog_65_GoogleCloudDatacatalogV1DataplexTableSpecOut",
        "GoogleCloudDatacatalogV1StarEntryRequestIn": "_datacatalog_66_GoogleCloudDatacatalogV1StarEntryRequestIn",
        "GoogleCloudDatacatalogV1StarEntryRequestOut": "_datacatalog_67_GoogleCloudDatacatalogV1StarEntryRequestOut",
        "PolicyIn": "_datacatalog_68_PolicyIn",
        "PolicyOut": "_datacatalog_69_PolicyOut",
        "GoogleCloudDatacatalogV1ViewSpecIn": "_datacatalog_70_GoogleCloudDatacatalogV1ViewSpecIn",
        "GoogleCloudDatacatalogV1ViewSpecOut": "_datacatalog_71_GoogleCloudDatacatalogV1ViewSpecOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn": "_datacatalog_72_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut": "_datacatalog_73_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut",
        "GoogleCloudDatacatalogV1ListEntriesResponseIn": "_datacatalog_74_GoogleCloudDatacatalogV1ListEntriesResponseIn",
        "GoogleCloudDatacatalogV1ListEntriesResponseOut": "_datacatalog_75_GoogleCloudDatacatalogV1ListEntriesResponseOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn": "_datacatalog_76_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut": "_datacatalog_77_GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut",
        "GoogleCloudDatacatalogV1TaxonomyIn": "_datacatalog_78_GoogleCloudDatacatalogV1TaxonomyIn",
        "GoogleCloudDatacatalogV1TaxonomyOut": "_datacatalog_79_GoogleCloudDatacatalogV1TaxonomyOut",
        "GoogleCloudDatacatalogV1DataSourceIn": "_datacatalog_80_GoogleCloudDatacatalogV1DataSourceIn",
        "GoogleCloudDatacatalogV1DataSourceOut": "_datacatalog_81_GoogleCloudDatacatalogV1DataSourceOut",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecIn": "_datacatalog_82_GoogleCloudDatacatalogV1DataplexFilesetSpecIn",
        "GoogleCloudDatacatalogV1DataplexFilesetSpecOut": "_datacatalog_83_GoogleCloudDatacatalogV1DataplexFilesetSpecOut",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseIn": "_datacatalog_84_GoogleCloudDatacatalogV1ListTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ListTaxonomiesResponseOut": "_datacatalog_85_GoogleCloudDatacatalogV1ListTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1ImportEntriesResponseIn": "_datacatalog_86_GoogleCloudDatacatalogV1ImportEntriesResponseIn",
        "GoogleCloudDatacatalogV1ImportEntriesResponseOut": "_datacatalog_87_GoogleCloudDatacatalogV1ImportEntriesResponseOut",
        "GoogleCloudDatacatalogV1LookerSystemSpecIn": "_datacatalog_88_GoogleCloudDatacatalogV1LookerSystemSpecIn",
        "GoogleCloudDatacatalogV1LookerSystemSpecOut": "_datacatalog_89_GoogleCloudDatacatalogV1LookerSystemSpecOut",
        "GoogleCloudDatacatalogV1UnstarEntryResponseIn": "_datacatalog_90_GoogleCloudDatacatalogV1UnstarEntryResponseIn",
        "GoogleCloudDatacatalogV1UnstarEntryResponseOut": "_datacatalog_91_GoogleCloudDatacatalogV1UnstarEntryResponseOut",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn": "_datacatalog_92_GoogleCloudDatacatalogV1ImportTaxonomiesResponseIn",
        "GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut": "_datacatalog_93_GoogleCloudDatacatalogV1ImportTaxonomiesResponseOut",
        "GoogleCloudDatacatalogV1ColumnSchemaIn": "_datacatalog_94_GoogleCloudDatacatalogV1ColumnSchemaIn",
        "GoogleCloudDatacatalogV1ColumnSchemaOut": "_datacatalog_95_GoogleCloudDatacatalogV1ColumnSchemaOut",
        "OperationIn": "_datacatalog_96_OperationIn",
        "OperationOut": "_datacatalog_97_OperationOut",
        "GoogleCloudDatacatalogV1TagFieldIn": "_datacatalog_98_GoogleCloudDatacatalogV1TagFieldIn",
        "GoogleCloudDatacatalogV1TagFieldOut": "_datacatalog_99_GoogleCloudDatacatalogV1TagFieldOut",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn": "_datacatalog_100_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn",
        "GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut": "_datacatalog_101_GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut",
        "GoogleCloudDatacatalogV1ContactsIn": "_datacatalog_102_GoogleCloudDatacatalogV1ContactsIn",
        "GoogleCloudDatacatalogV1ContactsOut": "_datacatalog_103_GoogleCloudDatacatalogV1ContactsOut",
        "GoogleCloudDatacatalogV1DataplexSpecIn": "_datacatalog_104_GoogleCloudDatacatalogV1DataplexSpecIn",
        "GoogleCloudDatacatalogV1DataplexSpecOut": "_datacatalog_105_GoogleCloudDatacatalogV1DataplexSpecOut",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn": "_datacatalog_106_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestIn",
        "GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut": "_datacatalog_107_GoogleCloudDatacatalogV1ReplaceTaxonomyRequestOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn": "_datacatalog_108_GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut": "_datacatalog_109_GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut",
        "GoogleCloudDatacatalogV1StoragePropertiesIn": "_datacatalog_110_GoogleCloudDatacatalogV1StoragePropertiesIn",
        "GoogleCloudDatacatalogV1StoragePropertiesOut": "_datacatalog_111_GoogleCloudDatacatalogV1StoragePropertiesOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn": "_datacatalog_112_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut": "_datacatalog_113_GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut",
        "GoogleCloudDatacatalogV1PersonalDetailsIn": "_datacatalog_114_GoogleCloudDatacatalogV1PersonalDetailsIn",
        "GoogleCloudDatacatalogV1PersonalDetailsOut": "_datacatalog_115_GoogleCloudDatacatalogV1PersonalDetailsOut",
        "GoogleCloudDatacatalogV1GcsFilesetSpecIn": "_datacatalog_116_GoogleCloudDatacatalogV1GcsFilesetSpecIn",
        "GoogleCloudDatacatalogV1GcsFilesetSpecOut": "_datacatalog_117_GoogleCloudDatacatalogV1GcsFilesetSpecOut",
        "GoogleCloudDatacatalogV1DataplexExternalTableIn": "_datacatalog_118_GoogleCloudDatacatalogV1DataplexExternalTableIn",
        "GoogleCloudDatacatalogV1DataplexExternalTableOut": "_datacatalog_119_GoogleCloudDatacatalogV1DataplexExternalTableOut",
        "GoogleCloudDatacatalogV1TagFieldEnumValueIn": "_datacatalog_120_GoogleCloudDatacatalogV1TagFieldEnumValueIn",
        "GoogleCloudDatacatalogV1TagFieldEnumValueOut": "_datacatalog_121_GoogleCloudDatacatalogV1TagFieldEnumValueOut",
        "GetPolicyOptionsIn": "_datacatalog_122_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_datacatalog_123_GetPolicyOptionsOut",
        "GoogleCloudDatacatalogV1TagIn": "_datacatalog_124_GoogleCloudDatacatalogV1TagIn",
        "GoogleCloudDatacatalogV1TagOut": "_datacatalog_125_GoogleCloudDatacatalogV1TagOut",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn": "_datacatalog_126_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn",
        "GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut": "_datacatalog_127_GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut",
        "GoogleCloudDatacatalogV1DumpItemIn": "_datacatalog_128_GoogleCloudDatacatalogV1DumpItemIn",
        "GoogleCloudDatacatalogV1DumpItemOut": "_datacatalog_129_GoogleCloudDatacatalogV1DumpItemOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaIn": "_datacatalog_130_GoogleCloudDatacatalogV1PhysicalSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOut": "_datacatalog_131_GoogleCloudDatacatalogV1PhysicalSchemaOut",
        "GoogleCloudDatacatalogV1ListTagsResponseIn": "_datacatalog_132_GoogleCloudDatacatalogV1ListTagsResponseIn",
        "GoogleCloudDatacatalogV1ListTagsResponseOut": "_datacatalog_133_GoogleCloudDatacatalogV1ListTagsResponseOut",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn": "_datacatalog_134_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestIn",
        "GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut": "_datacatalog_135_GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequestOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn": "_datacatalog_136_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut": "_datacatalog_137_GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestIn": "_datacatalog_138_GoogleCloudDatacatalogV1ReconcileTagsRequestIn",
        "GoogleCloudDatacatalogV1ReconcileTagsRequestOut": "_datacatalog_139_GoogleCloudDatacatalogV1ReconcileTagsRequestOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn": "_datacatalog_140_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut": "_datacatalog_141_GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut",
        "GoogleCloudDatacatalogV1EntryIn": "_datacatalog_142_GoogleCloudDatacatalogV1EntryIn",
        "GoogleCloudDatacatalogV1EntryOut": "_datacatalog_143_GoogleCloudDatacatalogV1EntryOut",
        "GoogleCloudDatacatalogV1TaxonomyServiceIn": "_datacatalog_144_GoogleCloudDatacatalogV1TaxonomyServiceIn",
        "GoogleCloudDatacatalogV1TaxonomyServiceOut": "_datacatalog_145_GoogleCloudDatacatalogV1TaxonomyServiceOut",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataIn": "_datacatalog_146_GoogleCloudDatacatalogV1ReconcileTagsMetadataIn",
        "GoogleCloudDatacatalogV1ReconcileTagsMetadataOut": "_datacatalog_147_GoogleCloudDatacatalogV1ReconcileTagsMetadataOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn": "_datacatalog_148_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut": "_datacatalog_149_GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn": "_datacatalog_150_GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut": "_datacatalog_151_GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut",
        "GoogleCloudDatacatalogV1SearchCatalogResultIn": "_datacatalog_152_GoogleCloudDatacatalogV1SearchCatalogResultIn",
        "GoogleCloudDatacatalogV1SearchCatalogResultOut": "_datacatalog_153_GoogleCloudDatacatalogV1SearchCatalogResultOut",
        "GoogleCloudDatacatalogV1ContactsPersonIn": "_datacatalog_154_GoogleCloudDatacatalogV1ContactsPersonIn",
        "GoogleCloudDatacatalogV1ContactsPersonOut": "_datacatalog_155_GoogleCloudDatacatalogV1ContactsPersonOut",
        "GoogleCloudDatacatalogV1ImportEntriesRequestIn": "_datacatalog_156_GoogleCloudDatacatalogV1ImportEntriesRequestIn",
        "GoogleCloudDatacatalogV1ImportEntriesRequestOut": "_datacatalog_157_GoogleCloudDatacatalogV1ImportEntriesRequestOut",
        "GoogleCloudDatacatalogV1BigQueryTableSpecIn": "_datacatalog_158_GoogleCloudDatacatalogV1BigQueryTableSpecIn",
        "GoogleCloudDatacatalogV1BigQueryTableSpecOut": "_datacatalog_159_GoogleCloudDatacatalogV1BigQueryTableSpecOut",
        "SetIamPolicyRequestIn": "_datacatalog_160_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datacatalog_161_SetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn": "_datacatalog_162_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut": "_datacatalog_163_GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1UsageSignalIn": "_datacatalog_164_GoogleCloudDatacatalogV1UsageSignalIn",
        "GoogleCloudDatacatalogV1UsageSignalOut": "_datacatalog_165_GoogleCloudDatacatalogV1UsageSignalOut",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn": "_datacatalog_166_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut": "_datacatalog_167_GoogleCloudDatacatalogV1ModifyEntryOverviewRequestOut",
        "GoogleCloudDatacatalogV1TagTemplateIn": "_datacatalog_168_GoogleCloudDatacatalogV1TagTemplateIn",
        "GoogleCloudDatacatalogV1TagTemplateOut": "_datacatalog_169_GoogleCloudDatacatalogV1TagTemplateOut",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn": "_datacatalog_170_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecIn",
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut": "_datacatalog_171_GoogleCloudDatacatalogV1CloudBigtableInstanceSpecOut",
        "GoogleCloudDatacatalogV1ServiceSpecIn": "_datacatalog_172_GoogleCloudDatacatalogV1ServiceSpecIn",
        "GoogleCloudDatacatalogV1ServiceSpecOut": "_datacatalog_173_GoogleCloudDatacatalogV1ServiceSpecOut",
        "EmptyIn": "_datacatalog_174_EmptyIn",
        "EmptyOut": "_datacatalog_175_EmptyOut",
        "ListOperationsResponseIn": "_datacatalog_176_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datacatalog_177_ListOperationsResponseOut",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecIn": "_datacatalog_178_GoogleCloudDatacatalogV1BigQueryConnectionSpecIn",
        "GoogleCloudDatacatalogV1BigQueryConnectionSpecOut": "_datacatalog_179_GoogleCloudDatacatalogV1BigQueryConnectionSpecOut",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentIn": "_datacatalog_180_GoogleCloudDatacatalogV1RoutineSpecArgumentIn",
        "GoogleCloudDatacatalogV1RoutineSpecArgumentOut": "_datacatalog_181_GoogleCloudDatacatalogV1RoutineSpecArgumentOut",
        "GoogleCloudDatacatalogV1TagTemplateFieldIn": "_datacatalog_182_GoogleCloudDatacatalogV1TagTemplateFieldIn",
        "GoogleCloudDatacatalogV1TagTemplateFieldOut": "_datacatalog_183_GoogleCloudDatacatalogV1TagTemplateFieldOut",
        "GoogleCloudDatacatalogV1EntryGroupIn": "_datacatalog_184_GoogleCloudDatacatalogV1EntryGroupIn",
        "GoogleCloudDatacatalogV1EntryGroupOut": "_datacatalog_185_GoogleCloudDatacatalogV1EntryGroupOut",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn": "_datacatalog_186_GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn",
        "GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut": "_datacatalog_187_GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut",
        "GetIamPolicyRequestIn": "_datacatalog_188_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_datacatalog_189_GetIamPolicyRequestOut",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataIn": "_datacatalog_190_GoogleCloudDatacatalogV1ImportEntriesMetadataIn",
        "GoogleCloudDatacatalogV1ImportEntriesMetadataOut": "_datacatalog_191_GoogleCloudDatacatalogV1ImportEntriesMetadataOut",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseIn": "_datacatalog_192_GoogleCloudDatacatalogV1ReconcileTagsResponseIn",
        "GoogleCloudDatacatalogV1ReconcileTagsResponseOut": "_datacatalog_193_GoogleCloudDatacatalogV1ReconcileTagsResponseOut",
        "GoogleCloudDatacatalogV1SearchCatalogRequestIn": "_datacatalog_194_GoogleCloudDatacatalogV1SearchCatalogRequestIn",
        "GoogleCloudDatacatalogV1SearchCatalogRequestOut": "_datacatalog_195_GoogleCloudDatacatalogV1SearchCatalogRequestOut",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseIn": "_datacatalog_196_GoogleCloudDatacatalogV1ListPolicyTagsResponseIn",
        "GoogleCloudDatacatalogV1ListPolicyTagsResponseOut": "_datacatalog_197_GoogleCloudDatacatalogV1ListPolicyTagsResponseOut",
        "GoogleCloudDatacatalogV1BusinessContextIn": "_datacatalog_198_GoogleCloudDatacatalogV1BusinessContextIn",
        "GoogleCloudDatacatalogV1BusinessContextOut": "_datacatalog_199_GoogleCloudDatacatalogV1BusinessContextOut",
        "GoogleCloudDatacatalogV1TaggedEntryIn": "_datacatalog_200_GoogleCloudDatacatalogV1TaggedEntryIn",
        "GoogleCloudDatacatalogV1TaggedEntryOut": "_datacatalog_201_GoogleCloudDatacatalogV1TaggedEntryOut",
        "GoogleCloudDatacatalogV1PolicyTagIn": "_datacatalog_202_GoogleCloudDatacatalogV1PolicyTagIn",
        "GoogleCloudDatacatalogV1PolicyTagOut": "_datacatalog_203_GoogleCloudDatacatalogV1PolicyTagOut",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn": "_datacatalog_204_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn",
        "GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut": "_datacatalog_205_GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut",
        "GoogleCloudDatacatalogV1FilesetSpecIn": "_datacatalog_206_GoogleCloudDatacatalogV1FilesetSpecIn",
        "GoogleCloudDatacatalogV1FilesetSpecOut": "_datacatalog_207_GoogleCloudDatacatalogV1FilesetSpecOut",
        "GoogleCloudDatacatalogV1SearchCatalogResponseIn": "_datacatalog_208_GoogleCloudDatacatalogV1SearchCatalogResponseIn",
        "GoogleCloudDatacatalogV1SearchCatalogResponseOut": "_datacatalog_209_GoogleCloudDatacatalogV1SearchCatalogResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"] = t.struct(
        {"importedLibraries": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"] = t.struct(
        {
            "importedLibraries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecIn"] = t.struct(
        {
            "definitionBody": t.string().optional(),
            "routineType": t.string().optional(),
            "language": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecIn"]
            ).optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
            ).optional(),
            "returnType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecOut"] = t.struct(
        {
            "definitionBody": t.string().optional(),
            "routineType": t.string().optional(),
            "language": t.string().optional(),
            "bigqueryRoutineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryRoutineSpecOut"]
            ).optional(),
            "routineArguments": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
            ).optional(),
            "returnType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecOut"])
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
    types["GoogleCloudDatacatalogV1SystemTimestampsIn"] = t.struct(
        {"createTime": t.string().optional(), "updateTime": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsIn"])
    types["GoogleCloudDatacatalogV1SystemTimestampsOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SystemTimestampsOut"])
    types["GoogleCloudDatacatalogV1UnstarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["GoogleCloudDatacatalogV1TableSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TableSpecIn"])
    types["GoogleCloudDatacatalogV1TableSpecOut"] = t.struct(
        {
            "groupedEntry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TableSpecOut"])
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
    types["GoogleCloudDatacatalogV1SerializedTaxonomyIn"] = t.struct(
        {
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyIn"])
    types["GoogleCloudDatacatalogV1SerializedTaxonomyOut"] = t.struct(
        {
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "policyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedTaxonomyOut"])
    types["GoogleCloudDatacatalogV1EntryOverviewIn"] = t.struct(
        {"overview": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewIn"])
    types["GoogleCloudDatacatalogV1EntryOverviewOut"] = t.struct(
        {
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOverviewOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["GoogleCloudDatacatalogV1StarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1StarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryResponseOut"])
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
    types["GoogleCloudDatacatalogV1SerializedPolicyTagIn"] = t.struct(
        {
            "displayName": t.string(),
            "policyTag": t.string().optional(),
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagIn"])
    types["GoogleCloudDatacatalogV1SerializedPolicyTagOut"] = t.struct(
        {
            "displayName": t.string(),
            "policyTag": t.string().optional(),
            "childPolicyTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SerializedPolicyTagOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceIn"] = t.struct(
        {"taxonomy": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceIn"])
    types["GoogleCloudDatacatalogV1CrossRegionalSourceOut"] = t.struct(
        {"taxonomy": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1CrossRegionalSourceOut"])
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
    types["GoogleCloudDatacatalogV1CommonUsageStatsIn"] = t.struct(
        {"viewCount": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsIn"])
    types["GoogleCloudDatacatalogV1CommonUsageStatsOut"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CommonUsageStatsOut"])
    types["GoogleCloudDatacatalogV1GcsFileSpecIn"] = t.struct(
        {"filePath": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecIn"])
    types["GoogleCloudDatacatalogV1GcsFileSpecOut"] = t.struct(
        {
            "gcsTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "sizeBytes": t.string().optional(),
            "filePath": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1GcsFileSpecOut"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"] = t.struct(
        {
            "sqlQuery": t.string().optional(),
            "viewType": t.string().optional(),
            "baseTable": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecIn"])
    types["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"] = t.struct(
        {
            "sqlQuery": t.string().optional(),
            "viewType": t.string().optional(),
            "baseTable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpecOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"])
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
    types["GoogleCloudDatacatalogV1StarEntryRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestIn"])
    types["GoogleCloudDatacatalogV1StarEntryRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1StarEntryRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudDatacatalogV1ViewSpecIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecIn"])
    types["GoogleCloudDatacatalogV1ViewSpecOut"] = t.struct(
        {
            "viewQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ViewSpecOut"])
    types[
        "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecIn"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "linkedResource": t.string().optional(),
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
            "location": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "linkedResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpecOut"
        ]
    )
    types["GoogleCloudDatacatalogV1ListEntriesResponseIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntriesResponseIn"])
    types["GoogleCloudDatacatalogV1ListEntriesResponseOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListEntriesResponseOut"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"] = t.struct(
        {"newTagTemplateFieldId": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestIn"])
    types["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"] = t.struct(
        {
            "newTagTemplateFieldId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RenameTagTemplateFieldRequestOut"])
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
            "taxonomyTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "service": t.proxy(
                renames["GoogleCloudDatacatalogV1TaxonomyServiceOut"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "activatedPolicyTypes": t.array(t.string()).optional(),
            "policyTagCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaxonomyOut"])
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
    types["GoogleCloudDatacatalogV1ImportEntriesResponseIn"] = t.struct(
        {
            "deletedEntriesCount": t.string().optional(),
            "upsertedEntriesCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesResponseIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesResponseOut"] = t.struct(
        {
            "deletedEntriesCount": t.string().optional(),
            "upsertedEntriesCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesResponseOut"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecIn"] = t.struct(
        {
            "parentInstanceId": t.string().optional(),
            "parentViewDisplayName": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentViewId": t.string().optional(),
            "parentModelId": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"])
    types["GoogleCloudDatacatalogV1LookerSystemSpecOut"] = t.struct(
        {
            "parentInstanceId": t.string().optional(),
            "parentViewDisplayName": t.string().optional(),
            "parentModelDisplayName": t.string().optional(),
            "parentViewId": t.string().optional(),
            "parentModelId": t.string().optional(),
            "parentInstanceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseIn"])
    types["GoogleCloudDatacatalogV1UnstarEntryResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"])
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
    types["GoogleCloudDatacatalogV1ColumnSchemaIn"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"]
            ).optional(),
            "mode": t.string().optional(),
            "highestIndexingType": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "gcRule": t.string().optional(),
            "column": t.string(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaOut"] = t.struct(
        {
            "ordinalPosition": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "lookerColumnSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"]
            ).optional(),
            "mode": t.string().optional(),
            "highestIndexingType": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "gcRule": t.string().optional(),
            "column": t.string(),
            "subcolumns": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudDatacatalogV1TagFieldIn"] = t.struct(
        {
            "richtextValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldIn"])
    types["GoogleCloudDatacatalogV1TagFieldOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "order": t.integer().optional(),
            "richtextValue": t.string().optional(),
            "doubleValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "timestampValue": t.string().optional(),
            "stringValue": t.string().optional(),
            "enumValue": t.proxy(
                renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldOut"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"] = t.struct(
        {"displayName": t.string()}
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueIn"])
    types["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"] = t.struct(
        {
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValueOut"])
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
    types["GoogleCloudDatacatalogV1DataplexSpecIn"] = t.struct(
        {
            "asset": t.string().optional(),
            "compressionFormat": t.string().optional(),
            "projectId": t.string().optional(),
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecIn"])
    types["GoogleCloudDatacatalogV1DataplexSpecOut"] = t.struct(
        {
            "asset": t.string().optional(),
            "compressionFormat": t.string().optional(),
            "projectId": t.string().optional(),
            "dataFormat": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexSpecOut"])
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
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"] = t.struct(
        {
            "restrictedLocations": t.array(t.string()).optional(),
            "includeOrgIds": t.array(t.string()).optional(),
            "includeProjectIds": t.array(t.string()).optional(),
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "starredOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"] = t.struct(
        {
            "restrictedLocations": t.array(t.string()).optional(),
            "includeOrgIds": t.array(t.string()).optional(),
            "includeProjectIds": t.array(t.string()).optional(),
            "includePublicTagTemplates": t.boolean().optional(),
            "includeGcpPublicDatasets": t.boolean().optional(),
            "starredOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"])
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
    types["GoogleCloudDatacatalogV1DataplexExternalTableIn"] = t.struct(
        {
            "googleCloudResource": t.string().optional(),
            "system": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "dataCatalogEntry": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableIn"])
    types["GoogleCloudDatacatalogV1DataplexExternalTableOut"] = t.struct(
        {
            "googleCloudResource": t.string().optional(),
            "system": t.string().optional(),
            "fullyQualifiedName": t.string().optional(),
            "dataCatalogEntry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1DataplexExternalTableOut"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueIn"] = t.struct(
        {"displayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueIn"])
    types["GoogleCloudDatacatalogV1TagFieldEnumValueOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagFieldEnumValueOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GoogleCloudDatacatalogV1TagIn"] = t.struct(
        {
            "name": t.string().optional(),
            "column": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "template": t.string(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagIn"])
    types["GoogleCloudDatacatalogV1TagOut"] = t.struct(
        {
            "templateDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "column": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "template": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagOut"])
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"] = t.struct(
        {"type": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecIn"])
    types["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpecOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaIn"] = t.struct(
        {
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaIn"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaIn"]
            ).optional(),
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"]
            ).optional(),
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOut"] = t.struct(
        {
            "orc": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"]
            ).optional(),
            "csv": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"]
            ).optional(),
            "parquet": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaParquetSchemaOut"]
            ).optional(),
            "protobuf": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchemaOut"]
            ).optional(),
            "thrift": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"]
            ).optional(),
            "avro": t.proxy(
                renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOut"])
    types["GoogleCloudDatacatalogV1ListTagsResponseIn"] = t.struct(
        {
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTagsResponseIn"])
    types["GoogleCloudDatacatalogV1ListTagsResponseOut"] = t.struct(
        {
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ListTagsResponseOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaCsvSchemaOut"])
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"] = t.struct(
        {
            "tagTemplate": t.string(),
            "forceDeleteMissing": t.boolean().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestIn"])
    types["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"] = t.struct(
        {
            "tagTemplate": t.string(),
            "forceDeleteMissing": t.boolean().optional(),
            "tags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ReconcileTagsRequestOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaAvroSchemaOut"])
    types["GoogleCloudDatacatalogV1EntryIn"] = t.struct(
        {
            "type": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsIn"]
            ).optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecIn"]
            ).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecIn"]
            ).optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecIn"]
            ).optional(),
            "userSpecifiedType": t.string().optional(),
            "displayName": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"]
            ).optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextIn"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaIn"]).optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecIn"]
            ).optional(),
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecIn"]
            ).optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecIn"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecIn"]
            ).optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalIn"]
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryIn"])
    types["GoogleCloudDatacatalogV1EntryOut"] = t.struct(
        {
            "type": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "sourceSystemTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "filesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1FilesetSpecOut"]
            ).optional(),
            "bigqueryDateShardedSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryDateShardedSpecOut"]
            ).optional(),
            "serviceSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1ServiceSpecOut"]
            ).optional(),
            "sqlDatabaseSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1SqlDatabaseSystemSpecOut"]
            ).optional(),
            "userSpecifiedType": t.string().optional(),
            "displayName": t.string().optional(),
            "cloudBigtableSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"]
            ).optional(),
            "businessContext": t.proxy(
                renames["GoogleCloudDatacatalogV1BusinessContextOut"]
            ).optional(),
            "linkedResource": t.string().optional(),
            "personalDetails": t.proxy(
                renames["GoogleCloudDatacatalogV1PersonalDetailsOut"]
            ).optional(),
            "dataSourceConnectionSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceConnectionSpecOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "schema": t.proxy(renames["GoogleCloudDatacatalogV1SchemaOut"]).optional(),
            "name": t.string().optional(),
            "integratedSystem": t.string().optional(),
            "lookerSystemSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1LookerSystemSpecOut"]
            ).optional(),
            "routineSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1RoutineSpecOut"]
            ).optional(),
            "bigqueryTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"]
            ).optional(),
            "gcsFilesetSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1GcsFilesetSpecOut"]
            ).optional(),
            "fullyQualifiedName": t.string().optional(),
            "databaseTableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1DatabaseTableSpecOut"]
            ).optional(),
            "usageSignal": t.proxy(
                renames["GoogleCloudDatacatalogV1UsageSignalOut"]
            ).optional(),
            "description": t.string().optional(),
            "dataSource": t.proxy(
                renames["GoogleCloudDatacatalogV1DataSourceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryOut"])
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
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaThriftSchemaOut"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"] = t.struct(
        {"instanceDisplayName": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecIn"])
    types["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"] = t.struct(
        {
            "instanceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudBigtableSystemSpecOut"])
    types["GoogleCloudDatacatalogV1SearchCatalogResultIn"] = t.struct(
        {
            "fullyQualifiedName": t.string().optional(),
            "modifyTime": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "displayName": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "linkedResource": t.string().optional(),
            "description": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "searchResultType": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResultOut"] = t.struct(
        {
            "fullyQualifiedName": t.string().optional(),
            "modifyTime": t.string().optional(),
            "searchResultSubtype": t.string().optional(),
            "displayName": t.string().optional(),
            "relativeResourceName": t.string().optional(),
            "linkedResource": t.string().optional(),
            "integratedSystem": t.string().optional(),
            "description": t.string().optional(),
            "userSpecifiedSystem": t.string().optional(),
            "searchResultType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
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
    types["GoogleCloudDatacatalogV1ImportEntriesRequestIn"] = t.struct(
        {"gcsBucketPath": t.string().optional(), "jobId": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesRequestOut"] = t.struct(
        {
            "gcsBucketPath": t.string().optional(),
            "jobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesRequestOut"])
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
            "tableSpec": t.proxy(
                renames["GoogleCloudDatacatalogV1TableSpecOut"]
            ).optional(),
            "tableSourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryTableSpecOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"] = t.struct(
        {
            "type": t.string().optional(),
            "database": t.string().optional(),
            "instanceId": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"])
    types["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"] = t.struct(
        {
            "type": t.string().optional(),
            "database": t.string().optional(),
            "instanceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"])
    types["GoogleCloudDatacatalogV1UsageSignalIn"] = t.struct(
        {
            "favoriteCount": t.string().optional(),
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalIn"])
    types["GoogleCloudDatacatalogV1UsageSignalOut"] = t.struct(
        {
            "usageWithinTimeRange": t.struct({"_": t.string().optional()}).optional(),
            "favoriteCount": t.string().optional(),
            "commonUsageWithinTimeRange": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1UsageSignalOut"])
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
    types["GoogleCloudDatacatalogV1TagTemplateIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "isPubliclyReadable": t.boolean().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateIn"])
    types["GoogleCloudDatacatalogV1TagTemplateOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "isPubliclyReadable": t.boolean().optional(),
            "fields": t.struct({"_": t.string().optional()}),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["GoogleCloudDatacatalogV1BigQueryConnectionSpecIn"] = t.struct(
        {
            "hasCredential": t.boolean().optional(),
            "connectionType": t.string().optional(),
            "cloudSql": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecIn"])
    types["GoogleCloudDatacatalogV1BigQueryConnectionSpecOut"] = t.struct(
        {
            "hasCredential": t.boolean().optional(),
            "connectionType": t.string().optional(),
            "cloudSql": t.proxy(
                renames["GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1BigQueryConnectionSpecOut"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"] = t.struct(
        {
            "type": t.string().optional(),
            "mode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentIn"])
    types["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"] = t.struct(
        {
            "type": t.string().optional(),
            "mode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1RoutineSpecArgumentOut"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldIn"] = t.struct(
        {
            "isRequired": t.boolean().optional(),
            "displayName": t.string().optional(),
            "order": t.integer().optional(),
            "description": t.string().optional(),
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldIn"])
    types["GoogleCloudDatacatalogV1TagTemplateFieldOut"] = t.struct(
        {
            "isRequired": t.boolean().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "order": t.integer().optional(),
            "description": t.string().optional(),
            "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"])
    types["GoogleCloudDatacatalogV1EntryGroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryGroupIn"])
    types["GoogleCloudDatacatalogV1EntryGroupOut"] = t.struct(
        {
            "dataCatalogTimestamps": t.proxy(
                renames["GoogleCloudDatacatalogV1SystemTimestampsOut"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1EntryGroupOut"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"] = t.struct(
        {"contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsIn"])}
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestIn"])
    types["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"] = t.struct(
        {
            "contacts": t.proxy(renames["GoogleCloudDatacatalogV1ContactsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ModifyEntryContactsRequestOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["GoogleCloudDatacatalogV1ImportEntriesMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["StatusIn"])).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesMetadataIn"])
    types["GoogleCloudDatacatalogV1ImportEntriesMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errors": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1ImportEntriesMetadataOut"])
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
    types["GoogleCloudDatacatalogV1SearchCatalogRequestIn"] = t.struct(
        {
            "orderBy": t.string().optional(),
            "query": t.string().optional(),
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
            ),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogRequestOut"] = t.struct(
        {
            "orderBy": t.string().optional(),
            "query": t.string().optional(),
            "scope": t.proxy(
                renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeOut"]
            ),
            "pageToken": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogRequestOut"])
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
    types["GoogleCloudDatacatalogV1TaggedEntryIn"] = t.struct(
        {
            "v1Entry": t.proxy(renames["GoogleCloudDatacatalogV1EntryIn"]).optional(),
            "presentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
            "absentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaggedEntryIn"])
    types["GoogleCloudDatacatalogV1TaggedEntryOut"] = t.struct(
        {
            "v1Entry": t.proxy(renames["GoogleCloudDatacatalogV1EntryOut"]).optional(),
            "presentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "absentTags": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1TagOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1TaggedEntryOut"])
    types["GoogleCloudDatacatalogV1PolicyTagIn"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "parentPolicyTag": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagIn"])
    types["GoogleCloudDatacatalogV1PolicyTagOut"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "childPolicyTags": t.array(t.string()).optional(),
            "parentPolicyTag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1PolicyTagOut"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaIn"])
    types["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatacatalogV1PhysicalSchemaOrcSchemaOut"])
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
    types["GoogleCloudDatacatalogV1SearchCatalogResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseIn"])
    types["GoogleCloudDatacatalogV1SearchCatalogResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "results": t.array(
                t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResultOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatacatalogV1SearchCatalogResponseOut"])

    functions = {}
    functions["projectsLocationsOperationsCancel"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGet"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesSetIamPolicy"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesImport"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesExport"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesGetIamPolicy"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesReplace"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesTestIamPermissions"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPatch"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesCreate"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesList"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesDelete"] = datacatalog.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsCreate"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsList"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsPatch"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsSetIamPolicy"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGetIamPolicy"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTaxonomiesPolicyTagsTestIamPermissions"
    ] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsDelete"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTaxonomiesPolicyTagsGet"] = datacatalog.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatacatalogV1PolicyTagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesSetIamPolicy"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesPatch"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesDelete"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesGet"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesTestIamPermissions"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesCreate"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesGetIamPolicy"] = datacatalog.post(
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
    functions["projectsLocationsTagTemplatesFieldsPatch"] = datacatalog.post(
        "v1/{parent}/fields",
        t.struct(
            {
                "tagTemplateFieldId": t.string(),
                "parent": t.string(),
                "isRequired": t.boolean().optional(),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsDelete"] = datacatalog.post(
        "v1/{parent}/fields",
        t.struct(
            {
                "tagTemplateFieldId": t.string(),
                "parent": t.string(),
                "isRequired": t.boolean().optional(),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsRename"] = datacatalog.post(
        "v1/{parent}/fields",
        t.struct(
            {
                "tagTemplateFieldId": t.string(),
                "parent": t.string(),
                "isRequired": t.boolean().optional(),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagTemplateFieldOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTagTemplatesFieldsCreate"] = datacatalog.post(
        "v1/{parent}/fields",
        t.struct(
            {
                "tagTemplateFieldId": t.string(),
                "parent": t.string(),
                "isRequired": t.boolean().optional(),
                "displayName": t.string().optional(),
                "order": t.integer().optional(),
                "description": t.string().optional(),
                "type": t.proxy(renames["GoogleCloudDatacatalogV1FieldTypeIn"]),
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
    functions["projectsLocationsEntryGroupsTestIamPermissions"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGetIamPolicy"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsDelete"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsList"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsCreate"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsGet"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsPatch"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsSetIamPolicy"] = datacatalog.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesImport"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesStar"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesDelete"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesList"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesGetIamPolicy"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryContacts"
    ] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesTestIamPermissions"
    ] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesGet"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEntryGroupsEntriesModifyEntryOverview"
    ] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesPatch"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesCreate"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsEntriesUnstar"] = datacatalog.post(
        "v1/{name}:unstar",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1UnstarEntryResponseOut"]),
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
    functions["projectsLocationsEntryGroupsEntriesTagsReconcile"] = datacatalog.delete(
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
    functions["projectsLocationsEntryGroupsTagsDelete"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "column": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}),
                "template": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsList"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "column": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}),
                "template": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsCreate"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "column": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}),
                "template": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEntryGroupsTagsPatch"] = datacatalog.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "column": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}),
                "template": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1TagOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["catalogSearch"] = datacatalog.post(
        "v1/catalog:search",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "query": t.string().optional(),
                "scope": t.proxy(
                    renames["GoogleCloudDatacatalogV1SearchCatalogRequestScopeIn"]
                ),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatacatalogV1SearchCatalogResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entriesLookup"] = datacatalog.get(
        "v1/entries:lookup",
        t.struct(
            {
                "location": t.string().optional(),
                "project": t.string().optional(),
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

    return Import(
        importer="datacatalog",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
