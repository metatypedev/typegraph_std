from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_drivelabels() -> Import:
    drivelabels = HTTPRuntime("https://drivelabels.googleapis.com/")

    renames = {
        "ErrorResponse": "_drivelabels_1_ErrorResponse",
        "GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn": "_drivelabels_2_GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn",
        "GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut": "_drivelabels_3_GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut",
        "GoogleAppsDriveLabelsV2FieldPropertiesIn": "_drivelabels_4_GoogleAppsDriveLabelsV2FieldPropertiesIn",
        "GoogleAppsDriveLabelsV2FieldPropertiesOut": "_drivelabels_5_GoogleAppsDriveLabelsV2FieldPropertiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn": "_drivelabels_6_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut": "_drivelabels_7_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn": "_drivelabels_8_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut": "_drivelabels_9_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn": "_drivelabels_10_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut": "_drivelabels_11_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut",
        "GoogleTypeColorIn": "_drivelabels_12_GoogleTypeColorIn",
        "GoogleTypeColorOut": "_drivelabels_13_GoogleTypeColorOut",
        "GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn": "_drivelabels_14_GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut": "_drivelabels_15_GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn": "_drivelabels_16_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut": "_drivelabels_17_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut",
        "GoogleAppsDriveLabelsV2FieldListOptionsIn": "_drivelabels_18_GoogleAppsDriveLabelsV2FieldListOptionsIn",
        "GoogleAppsDriveLabelsV2FieldListOptionsOut": "_drivelabels_19_GoogleAppsDriveLabelsV2FieldListOptionsOut",
        "GoogleAppsDriveLabelsV2BadgeConfigIn": "_drivelabels_20_GoogleAppsDriveLabelsV2BadgeConfigIn",
        "GoogleAppsDriveLabelsV2BadgeConfigOut": "_drivelabels_21_GoogleAppsDriveLabelsV2BadgeConfigOut",
        "GoogleAppsDriveLabelsV2FieldDateOptionsIn": "_drivelabels_22_GoogleAppsDriveLabelsV2FieldDateOptionsIn",
        "GoogleAppsDriveLabelsV2FieldDateOptionsOut": "_drivelabels_23_GoogleAppsDriveLabelsV2FieldDateOptionsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn": "_drivelabels_24_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut": "_drivelabels_25_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn": "_drivelabels_26_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut": "_drivelabels_27_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn": "_drivelabels_28_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut": "_drivelabels_29_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn": "_drivelabels_30_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut": "_drivelabels_31_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut",
        "GoogleAppsDriveLabelsV2FieldDisplayHintsIn": "_drivelabels_32_GoogleAppsDriveLabelsV2FieldDisplayHintsIn",
        "GoogleAppsDriveLabelsV2FieldDisplayHintsOut": "_drivelabels_33_GoogleAppsDriveLabelsV2FieldDisplayHintsOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn": "_drivelabels_34_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut": "_drivelabels_35_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn": "_drivelabels_36_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut": "_drivelabels_37_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2LabelIn": "_drivelabels_38_GoogleAppsDriveLabelsV2LabelIn",
        "GoogleAppsDriveLabelsV2LabelOut": "_drivelabels_39_GoogleAppsDriveLabelsV2LabelOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn": "_drivelabels_40_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut": "_drivelabels_41_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2IntegerLimitsIn": "_drivelabels_42_GoogleAppsDriveLabelsV2IntegerLimitsIn",
        "GoogleAppsDriveLabelsV2IntegerLimitsOut": "_drivelabels_43_GoogleAppsDriveLabelsV2IntegerLimitsOut",
        "GoogleAppsDriveLabelsV2PublishLabelRequestIn": "_drivelabels_44_GoogleAppsDriveLabelsV2PublishLabelRequestIn",
        "GoogleAppsDriveLabelsV2PublishLabelRequestOut": "_drivelabels_45_GoogleAppsDriveLabelsV2PublishLabelRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn": "_drivelabels_46_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut": "_drivelabels_47_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn": "_drivelabels_48_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut": "_drivelabels_49_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut",
        "GoogleAppsDriveLabelsV2LockStatusIn": "_drivelabels_50_GoogleAppsDriveLabelsV2LockStatusIn",
        "GoogleAppsDriveLabelsV2LockStatusOut": "_drivelabels_51_GoogleAppsDriveLabelsV2LockStatusOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn": "_drivelabels_52_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut": "_drivelabels_53_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut",
        "GoogleAppsDriveLabelsV2SelectionLimitsIn": "_drivelabels_54_GoogleAppsDriveLabelsV2SelectionLimitsIn",
        "GoogleAppsDriveLabelsV2SelectionLimitsOut": "_drivelabels_55_GoogleAppsDriveLabelsV2SelectionLimitsOut",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn": "_drivelabels_56_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut": "_drivelabels_57_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut",
        "GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn": "_drivelabels_58_GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut": "_drivelabels_59_GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn": "_drivelabels_60_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut": "_drivelabels_61_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut",
        "GoogleAppsDriveLabelsV2LabelPermissionIn": "_drivelabels_62_GoogleAppsDriveLabelsV2LabelPermissionIn",
        "GoogleAppsDriveLabelsV2LabelPermissionOut": "_drivelabels_63_GoogleAppsDriveLabelsV2LabelPermissionOut",
        "GoogleAppsDriveLabelsV2LabelPropertiesIn": "_drivelabels_64_GoogleAppsDriveLabelsV2LabelPropertiesIn",
        "GoogleAppsDriveLabelsV2LabelPropertiesOut": "_drivelabels_65_GoogleAppsDriveLabelsV2LabelPropertiesOut",
        "GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn": "_drivelabels_66_GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut": "_drivelabels_67_GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn": "_drivelabels_68_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut": "_drivelabels_69_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut",
        "GoogleAppsDriveLabelsV2LifecycleIn": "_drivelabels_70_GoogleAppsDriveLabelsV2LifecycleIn",
        "GoogleAppsDriveLabelsV2LifecycleOut": "_drivelabels_71_GoogleAppsDriveLabelsV2LifecycleOut",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn": "_drivelabels_72_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut": "_drivelabels_73_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut",
        "GoogleAppsDriveLabelsV2UserInfoIn": "_drivelabels_74_GoogleAppsDriveLabelsV2UserInfoIn",
        "GoogleAppsDriveLabelsV2UserInfoOut": "_drivelabels_75_GoogleAppsDriveLabelsV2UserInfoOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn": "_drivelabels_76_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut": "_drivelabels_77_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn": "_drivelabels_78_GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn",
        "GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut": "_drivelabels_79_GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut",
        "GoogleAppsDriveLabelsV2DisableLabelRequestIn": "_drivelabels_80_GoogleAppsDriveLabelsV2DisableLabelRequestIn",
        "GoogleAppsDriveLabelsV2DisableLabelRequestOut": "_drivelabels_81_GoogleAppsDriveLabelsV2DisableLabelRequestOut",
        "GoogleAppsDriveLabelsV2ListLimitsIn": "_drivelabels_82_GoogleAppsDriveLabelsV2ListLimitsIn",
        "GoogleAppsDriveLabelsV2ListLimitsOut": "_drivelabels_83_GoogleAppsDriveLabelsV2ListLimitsOut",
        "GoogleAppsDriveLabelsV2ListLabelLocksResponseIn": "_drivelabels_84_GoogleAppsDriveLabelsV2ListLabelLocksResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelLocksResponseOut": "_drivelabels_85_GoogleAppsDriveLabelsV2ListLabelLocksResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn": "_drivelabels_86_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut": "_drivelabels_87_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut",
        "GoogleAppsDriveLabelsV2ListLabelsResponseIn": "_drivelabels_88_GoogleAppsDriveLabelsV2ListLabelsResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelsResponseOut": "_drivelabels_89_GoogleAppsDriveLabelsV2ListLabelsResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn": "_drivelabels_90_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut": "_drivelabels_91_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut",
        "GoogleAppsDriveLabelsV2FieldUserOptionsIn": "_drivelabels_92_GoogleAppsDriveLabelsV2FieldUserOptionsIn",
        "GoogleAppsDriveLabelsV2FieldUserOptionsOut": "_drivelabels_93_GoogleAppsDriveLabelsV2FieldUserOptionsOut",
        "GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn": "_drivelabels_94_GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn",
        "GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut": "_drivelabels_95_GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut",
        "GoogleAppsDriveLabelsV2FieldIn": "_drivelabels_96_GoogleAppsDriveLabelsV2FieldIn",
        "GoogleAppsDriveLabelsV2FieldOut": "_drivelabels_97_GoogleAppsDriveLabelsV2FieldOut",
        "GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn": "_drivelabels_98_GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn",
        "GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut": "_drivelabels_99_GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn": "_drivelabels_100_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut": "_drivelabels_101_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn": "_drivelabels_102_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut": "_drivelabels_103_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2UserLimitsIn": "_drivelabels_104_GoogleAppsDriveLabelsV2UserLimitsIn",
        "GoogleAppsDriveLabelsV2UserLimitsOut": "_drivelabels_105_GoogleAppsDriveLabelsV2UserLimitsOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsIn": "_drivelabels_106_GoogleAppsDriveLabelsV2FieldSelectionOptionsIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsOut": "_drivelabels_107_GoogleAppsDriveLabelsV2FieldSelectionOptionsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn": "_drivelabels_108_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut": "_drivelabels_109_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut",
        "GoogleTypeDateIn": "_drivelabels_110_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_drivelabels_111_GoogleTypeDateOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn": "_drivelabels_112_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut": "_drivelabels_113_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn": "_drivelabels_114_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut": "_drivelabels_115_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut",
        "GoogleAppsDriveLabelsV2DateLimitsIn": "_drivelabels_116_GoogleAppsDriveLabelsV2DateLimitsIn",
        "GoogleAppsDriveLabelsV2DateLimitsOut": "_drivelabels_117_GoogleAppsDriveLabelsV2DateLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn": "_drivelabels_118_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut": "_drivelabels_119_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut",
        "GoogleAppsDriveLabelsV2FieldTextOptionsIn": "_drivelabels_120_GoogleAppsDriveLabelsV2FieldTextOptionsIn",
        "GoogleAppsDriveLabelsV2FieldTextOptionsOut": "_drivelabels_121_GoogleAppsDriveLabelsV2FieldTextOptionsOut",
        "GoogleAppsDriveLabelsV2UserCapabilitiesIn": "_drivelabels_122_GoogleAppsDriveLabelsV2UserCapabilitiesIn",
        "GoogleAppsDriveLabelsV2UserCapabilitiesOut": "_drivelabels_123_GoogleAppsDriveLabelsV2UserCapabilitiesOut",
        "GoogleAppsDriveLabelsV2EnableLabelRequestIn": "_drivelabels_124_GoogleAppsDriveLabelsV2EnableLabelRequestIn",
        "GoogleAppsDriveLabelsV2EnableLabelRequestOut": "_drivelabels_125_GoogleAppsDriveLabelsV2EnableLabelRequestOut",
        "GoogleAppsDriveLabelsV2FieldLimitsIn": "_drivelabels_126_GoogleAppsDriveLabelsV2FieldLimitsIn",
        "GoogleAppsDriveLabelsV2FieldLimitsOut": "_drivelabels_127_GoogleAppsDriveLabelsV2FieldLimitsOut",
        "GoogleAppsDriveLabelsV2LabelDisplayHintsIn": "_drivelabels_128_GoogleAppsDriveLabelsV2LabelDisplayHintsIn",
        "GoogleAppsDriveLabelsV2LabelDisplayHintsOut": "_drivelabels_129_GoogleAppsDriveLabelsV2LabelDisplayHintsOut",
        "GoogleAppsDriveLabelsV2TextLimitsIn": "_drivelabels_130_GoogleAppsDriveLabelsV2TextLimitsIn",
        "GoogleAppsDriveLabelsV2TextLimitsOut": "_drivelabels_131_GoogleAppsDriveLabelsV2TextLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn": "_drivelabels_132_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut": "_drivelabels_133_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut",
        "GoogleProtobufEmptyIn": "_drivelabels_134_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_drivelabels_135_GoogleProtobufEmptyOut",
        "GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn": "_drivelabels_136_GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut": "_drivelabels_137_GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn": "_drivelabels_138_GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut": "_drivelabels_139_GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2WriteControlIn": "_drivelabels_140_GoogleAppsDriveLabelsV2WriteControlIn",
        "GoogleAppsDriveLabelsV2WriteControlOut": "_drivelabels_141_GoogleAppsDriveLabelsV2WriteControlOut",
        "GoogleAppsDriveLabelsV2FieldLongTextOptionsIn": "_drivelabels_142_GoogleAppsDriveLabelsV2FieldLongTextOptionsIn",
        "GoogleAppsDriveLabelsV2FieldLongTextOptionsOut": "_drivelabels_143_GoogleAppsDriveLabelsV2FieldLongTextOptionsOut",
        "GoogleAppsDriveLabelsV2LabelLockIn": "_drivelabels_144_GoogleAppsDriveLabelsV2LabelLockIn",
        "GoogleAppsDriveLabelsV2LabelLockOut": "_drivelabels_145_GoogleAppsDriveLabelsV2LabelLockOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn": "_drivelabels_146_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut": "_drivelabels_147_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut",
        "GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn": "_drivelabels_148_GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut": "_drivelabels_149_GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut",
        "GoogleAppsDriveLabelsV2FieldIntegerOptionsIn": "_drivelabels_150_GoogleAppsDriveLabelsV2FieldIntegerOptionsIn",
        "GoogleAppsDriveLabelsV2FieldIntegerOptionsOut": "_drivelabels_151_GoogleAppsDriveLabelsV2FieldIntegerOptionsOut",
        "GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn": "_drivelabels_152_GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn",
        "GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut": "_drivelabels_153_GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn": "_drivelabels_154_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut": "_drivelabels_155_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut",
        "GoogleAppsDriveLabelsV2LabelLimitsIn": "_drivelabels_156_GoogleAppsDriveLabelsV2LabelLimitsIn",
        "GoogleAppsDriveLabelsV2LabelLimitsOut": "_drivelabels_157_GoogleAppsDriveLabelsV2LabelLimitsOut",
        "GoogleAppsDriveLabelsV2LongTextLimitsIn": "_drivelabels_158_GoogleAppsDriveLabelsV2LongTextLimitsIn",
        "GoogleAppsDriveLabelsV2LongTextLimitsOut": "_drivelabels_159_GoogleAppsDriveLabelsV2LongTextLimitsOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn": "_drivelabels_160_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut": "_drivelabels_161_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn": "_drivelabels_162_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut": "_drivelabels_163_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut",
        "GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn": "_drivelabels_164_GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn",
        "GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut": "_drivelabels_165_GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn": "_drivelabels_166_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut": "_drivelabels_167_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn": "_drivelabels_168_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut": "_drivelabels_169_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut",
        "GoogleAppsDriveLabelsV2BadgeColorsIn": "_drivelabels_170_GoogleAppsDriveLabelsV2BadgeColorsIn",
        "GoogleAppsDriveLabelsV2BadgeColorsOut": "_drivelabels_171_GoogleAppsDriveLabelsV2BadgeColorsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn": "_drivelabels_172_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut": "_drivelabels_173_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn"] = t.struct(
        {
            "copyMode": t.string(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn"])
    types["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut"] = t.struct(
        {
            "copyMode": t.string(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut"])
    types["GoogleAppsDriveLabelsV2FieldPropertiesIn"] = t.struct(
        {
            "required": t.boolean().optional(),
            "displayName": t.string(),
            "insertBeforeField": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"])
    types["GoogleAppsDriveLabelsV2FieldPropertiesOut"] = t.struct(
        {
            "required": t.boolean().optional(),
            "displayName": t.string(),
            "insertBeforeField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"
    ] = t.struct(
        {
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ),
            "id": t.string(),
            "updateMask": t.string().optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"
    ] = t.struct(
        {
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ),
            "id": t.string(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "choice": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"]
            ),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "choice": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn"
    ] = t.struct(
        {"priority": t.integer().optional(), "id": t.string().optional()}
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut"
    ] = t.struct(
        {
            "priority": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut"]
    )
    types["GoogleTypeColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
        }
    ).named(renames["GoogleTypeColorIn"])
    types["GoogleTypeColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "alpha": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeColorOut"])
    types["GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn"] = t.struct(
        {"canViewPolicy": t.boolean().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"] = t.struct(
        {
            "canViewPolicy": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn"] = t.struct(
        {
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut"] = t.struct(
        {
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut"])
    types["GoogleAppsDriveLabelsV2FieldListOptionsIn"] = t.struct(
        {"maxEntries": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldListOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldListOptionsOut"] = t.struct(
        {
            "maxEntries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldListOptionsOut"])
    types["GoogleAppsDriveLabelsV2BadgeConfigIn"] = t.struct(
        {
            "color": t.proxy(renames["GoogleTypeColorIn"]).optional(),
            "priorityOverride": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BadgeConfigIn"])
    types["GoogleAppsDriveLabelsV2BadgeConfigOut"] = t.struct(
        {
            "color": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "priorityOverride": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BadgeConfigOut"])
    types["GoogleAppsDriveLabelsV2FieldDateOptionsIn"] = t.struct(
        {"dateFormatType": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldDateOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldDateOptionsOut"] = t.struct(
        {
            "dateFormat": t.string().optional(),
            "dateFormatType": t.string().optional(),
            "minValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "maxValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDateOptionsOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn"
    ] = t.struct(
        {
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"]),
            "id": t.string(),
            "updateMask": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut"
    ] = t.struct(
        {
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"]),
            "id": t.string(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"
                ]
            ),
            "updateMask": t.string().optional(),
            "id": t.string(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"
                ]
            ),
            "updateMask": t.string().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2FieldDisplayHintsIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "required": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDisplayHintsIn"])
    types["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "required": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"])
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn"
    ] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "darkBadgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsIn"]
            ).optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "badgePriority": t.string().optional(),
            "badgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"
    ] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "darkBadgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsOut"]
            ).optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "badgePriority": t.string().optional(),
            "badgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn"
    ] = t.struct(
        {
            "id": t.string(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ),
            "fieldId": t.string(),
            "updateMask": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut"
    ] = t.struct(
        {
            "id": t.string(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ),
            "fieldId": t.string(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LabelIn"] = t.struct(
        {
            "fields": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldIn"])
            ).optional(),
            "labelType": t.string(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesIn"]),
            "learnMoreUri": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelIn"])
    types["GoogleAppsDriveLabelsV2LabelOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "appliedCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut"]
            ).optional(),
            "id": t.string().optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "disableTime": t.string().optional(),
            "revisionCreator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "schemaCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"]
            ).optional(),
            "fields": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "labelType": t.string(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesOut"]),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "displayHints": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"]
            ).optional(),
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publishTime": t.string().optional(),
            "appliedLabelPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"]
            ).optional(),
            "learnMoreUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2IntegerLimitsIn"] = t.struct(
        {"minValue": t.string().optional(), "maxValue": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2IntegerLimitsIn"])
    types["GoogleAppsDriveLabelsV2IntegerLimitsOut"] = t.struct(
        {
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2IntegerLimitsOut"])
    types["GoogleAppsDriveLabelsV2PublishLabelRequestIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2PublishLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2PublishLabelRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2PublishLabelRequestOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn"
    ] = t.struct({"fieldId": t.string(), "id": t.string()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn"
    ] = t.struct(
        {
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut"
    ] = t.struct(
        {
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LockStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LockStatusIn"])
    types["GoogleAppsDriveLabelsV2LockStatusOut"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LockStatusOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn"
    ] = t.struct({"id": t.string()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut"
    ] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut"]
    )
    types["GoogleAppsDriveLabelsV2SelectionLimitsIn"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsIn"]
            ).optional(),
            "maxChoices": t.integer().optional(),
            "maxIdLength": t.integer().optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxDeletedChoices": t.integer().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2SelectionLimitsIn"])
    types["GoogleAppsDriveLabelsV2SelectionLimitsOut"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsOut"]
            ).optional(),
            "maxChoices": t.integer().optional(),
            "maxIdLength": t.integer().optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxDeletedChoices": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2SelectionLimitsOut"])
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"]
                )
            ),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn"])
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut"])
    types["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn"] = t.struct(
        {
            "canUpdate": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"] = t.struct(
        {
            "canUpdate": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesIn"]),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LabelPermissionIn"] = t.struct(
        {
            "email": t.string().optional(),
            "person": t.string().optional(),
            "name": t.string().optional(),
            "role": t.string().optional(),
            "audience": t.string().optional(),
            "group": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelPermissionIn"])
    types["GoogleAppsDriveLabelsV2LabelPermissionOut"] = t.struct(
        {
            "email": t.string().optional(),
            "person": t.string().optional(),
            "name": t.string().optional(),
            "role": t.string().optional(),
            "audience": t.string().optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"])
    types["GoogleAppsDriveLabelsV2LabelPropertiesIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelPropertiesIn"])
    types["GoogleAppsDriveLabelsV2LabelPropertiesOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelPropertiesOut"])
    types["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn"] = t.struct(
        {
            "labelPermissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn"])
    types["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"] = t.struct(
        {
            "labelPermissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LifecycleIn"] = t.struct(
        {
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleIn"])
    types["GoogleAppsDriveLabelsV2LifecycleOut"] = t.struct(
        {
            "state": t.string().optional(),
            "hasUnpublishedChanges": t.boolean().optional(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleOut"])
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn"] = t.struct(
        {
            "permissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionIn"])
            )
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn"])
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"])
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut"])
    types["GoogleAppsDriveLabelsV2UserInfoIn"] = t.struct(
        {"person": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2UserInfoIn"])
    types["GoogleAppsDriveLabelsV2UserInfoOut"] = t.struct(
        {
            "person": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserInfoOut"])
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn"
    ] = t.struct(
        {
            "canSelect": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut"
    ] = t.struct(
        {
            "canSelect": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                )
            ),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn"])
    types["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"]
                )
            ),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut"])
    types["GoogleAppsDriveLabelsV2DisableLabelRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
            "updateMask": t.string().optional(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DisableLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2DisableLabelRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "updateMask": t.string().optional(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DisableLabelRequestOut"])
    types["GoogleAppsDriveLabelsV2ListLimitsIn"] = t.struct(
        {"maxEntries": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2ListLimitsIn"])
    types["GoogleAppsDriveLabelsV2ListLimitsOut"] = t.struct(
        {
            "maxEntries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLimitsOut"])
    types["GoogleAppsDriveLabelsV2ListLabelLocksResponseIn"] = t.struct(
        {
            "labelLocks": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelLockIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseIn"])
    types["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"] = t.struct(
        {
            "labelLocks": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelLockOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2ListLabelsResponseIn"] = t.struct(
        {
            "labels": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelsResponseIn"])
    types["GoogleAppsDriveLabelsV2ListLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelsResponseOut"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn"] = t.struct(
        {
            "updatedLabel": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelIn"]
            ).optional(),
            "responses": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn"]
                )
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut"] = t.struct(
        {
            "updatedLabel": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelOut"]
            ).optional(),
            "responses": t.array(
                t.proxy(
                    renames[
                        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut"])
    types["GoogleAppsDriveLabelsV2FieldUserOptionsIn"] = t.struct(
        {
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldUserOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldUserOptionsOut"] = t.struct(
        {
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldUserOptionsOut"])
    types["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn"] = t.struct(
        {"copyMode": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn"])
    types["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"] = t.struct(
        {
            "copyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"])
    types["GoogleAppsDriveLabelsV2FieldIn"] = t.struct(
        {
            "properties": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"]
            ).optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsIn"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsIn"]
            ).optional(),
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsIn"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"]
            ).optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldIn"])
    types["GoogleAppsDriveLabelsV2FieldOut"] = t.struct(
        {
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "properties": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"]
            ).optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsOut"]
            ).optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "updater": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsOut"]
            ).optional(),
            "disableTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "displayHints": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"]
            ).optional(),
            "appliedCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"]
            ).optional(),
            "schemaCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"]
            ).optional(),
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsOut"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"]
            ).optional(),
            "queryKey": t.string().optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldOut"])
    types["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"] = t.struct(
        {"hideInSearch": t.boolean().optional(), "showInApply": t.boolean().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"])
    types["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"] = t.struct(
        {
            "hideInSearch": t.boolean().optional(),
            "showInApply": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn"
    ] = t.struct({"priority": t.integer().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut"
    ] = t.struct(
        {
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2UserLimitsIn"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserLimitsIn"])
    types["GoogleAppsDriveLabelsV2UserLimitsOut"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserLimitsOut"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"] = t.struct(
        {
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsIn"]
            ).optional(),
            "choices": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"] = t.struct(
        {
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsOut"]
            ).optional(),
            "choices": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn"]
                )
            ).optional(),
            "view": t.string().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut"]
                )
            ).optional(),
            "view": t.string().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn"
    ] = t.struct({"priority": t.integer().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut"
    ] = t.struct(
        {
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2DateLimitsIn"] = t.struct(
        {
            "minValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "maxValue": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DateLimitsIn"])
    types["GoogleAppsDriveLabelsV2DateLimitsOut"] = t.struct(
        {
            "minValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "maxValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DateLimitsOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn"
    ] = t.struct({"field": t.proxy(renames["GoogleAppsDriveLabelsV2FieldIn"])}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut"
    ] = t.struct(
        {
            "field": t.proxy(renames["GoogleAppsDriveLabelsV2FieldOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut"]
    )
    types["GoogleAppsDriveLabelsV2FieldTextOptionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldTextOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldTextOptionsOut"] = t.struct(
        {
            "maxLength": t.integer().optional(),
            "minLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldTextOptionsOut"])
    types["GoogleAppsDriveLabelsV2UserCapabilitiesIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2UserCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2UserCapabilitiesOut"] = t.struct(
        {
            "canCreateSharedLabels": t.boolean().optional(),
            "canAdministrateLabels": t.boolean().optional(),
            "name": t.string().optional(),
            "canCreateAdminLabels": t.boolean().optional(),
            "canAccessLabelManager": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2EnableLabelRequestIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2EnableLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2EnableLabelRequestOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2EnableLabelRequestOut"])
    types["GoogleAppsDriveLabelsV2FieldLimitsIn"] = t.struct(
        {
            "maxIdLength": t.integer().optional(),
            "longTextLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2LongTextLimitsIn"]
            ).optional(),
            "userLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserLimitsIn"]
            ).optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
            "selectionLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2SelectionLimitsIn"]
            ).optional(),
            "dateLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2DateLimitsIn"]
            ).optional(),
            "textLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2TextLimitsIn"]
            ).optional(),
            "integerLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2IntegerLimitsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldLimitsIn"])
    types["GoogleAppsDriveLabelsV2FieldLimitsOut"] = t.struct(
        {
            "maxIdLength": t.integer().optional(),
            "longTextLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2LongTextLimitsOut"]
            ).optional(),
            "userLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserLimitsOut"]
            ).optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
            "selectionLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2SelectionLimitsOut"]
            ).optional(),
            "dateLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2DateLimitsOut"]
            ).optional(),
            "textLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2TextLimitsOut"]
            ).optional(),
            "integerLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2IntegerLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldLimitsOut"])
    types["GoogleAppsDriveLabelsV2LabelDisplayHintsIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "priority": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelDisplayHintsIn"])
    types["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "priority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"])
    types["GoogleAppsDriveLabelsV2TextLimitsIn"] = t.struct(
        {"minLength": t.integer().optional(), "maxLength": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2TextLimitsIn"])
    types["GoogleAppsDriveLabelsV2TextLimitsOut"] = t.struct(
        {
            "minLength": t.integer().optional(),
            "maxLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2TextLimitsOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn"
    ] = t.struct({"fieldId": t.string(), "id": t.string()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut"
    ] = t.struct(
        {
            "fieldId": t.string(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut"
        ]
    )
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn"] = t.struct(
        {
            "canWrite": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"] = t.struct(
        {
            "canWrite": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn"] = t.struct(
        {
            "canApply": t.boolean().optional(),
            "canRemove": t.boolean().optional(),
            "canRead": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut"] = t.struct(
        {
            "canApply": t.boolean().optional(),
            "canRemove": t.boolean().optional(),
            "canRead": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2WriteControlIn"])
    types["GoogleAppsDriveLabelsV2WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2WriteControlOut"])
    types["GoogleAppsDriveLabelsV2FieldLongTextOptionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldLongTextOptionsOut"] = t.struct(
        {
            "maxLength": t.integer().optional(),
            "minLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsOut"])
    types["GoogleAppsDriveLabelsV2LabelLockIn"] = t.struct(
        {"choiceId": t.string().optional(), "fieldId": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockIn"])
    types["GoogleAppsDriveLabelsV2LabelLockOut"] = t.struct(
        {
            "choiceId": t.string().optional(),
            "deleteTime": t.string().optional(),
            "fieldId": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "state": t.string().optional(),
            "capabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockOut"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"] = t.struct(
        {
            "id": t.string().optional(),
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "displayHints": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"
                ]
            ).optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publishTime": t.string().optional(),
            "updater": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"
                ]
            ).optional(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "disableTime": t.string().optional(),
            "schemaCapabilities": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut"
                ]
            ).optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "appliedCapabilities": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut"
                ]
            ).optional(),
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"])
    types["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn"] = t.struct(
        {
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"] = t.struct(
        {
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2FieldIntegerOptionsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldIntegerOptionsOut"] = t.struct(
        {
            "minValue": t.string().optional(),
            "maxValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsOut"])
    types["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"] = t.struct(
        {"name": t.string(), "useAdminAccess": t.boolean().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"])
    types["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"] = t.struct(
        {
            "name": t.string(),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn"
    ] = t.struct({"id": t.string()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut"
    ] = t.struct(
        {"id": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut"]
    )
    types["GoogleAppsDriveLabelsV2LabelLimitsIn"] = t.struct(
        {
            "maxTitleLength": t.integer().optional(),
            "maxFields": t.integer().optional(),
            "fieldLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLimitsIn"]
            ).optional(),
            "name": t.string().optional(),
            "maxDraftRevisions": t.integer().optional(),
            "maxDeletedFields": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLimitsIn"])
    types["GoogleAppsDriveLabelsV2LabelLimitsOut"] = t.struct(
        {
            "maxTitleLength": t.integer().optional(),
            "maxFields": t.integer().optional(),
            "fieldLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLimitsOut"]
            ).optional(),
            "name": t.string().optional(),
            "maxDraftRevisions": t.integer().optional(),
            "maxDeletedFields": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLimitsOut"])
    types["GoogleAppsDriveLabelsV2LongTextLimitsIn"] = t.struct(
        {"maxLength": t.integer().optional(), "minLength": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LongTextLimitsIn"])
    types["GoogleAppsDriveLabelsV2LongTextLimitsOut"] = t.struct(
        {
            "maxLength": t.integer().optional(),
            "minLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LongTextLimitsOut"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"] = t.struct(
        {
            "badgeConfig": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeConfigIn"]
            ).optional(),
            "insertBeforeChoice": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"] = t.struct(
        {
            "badgeConfig": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeConfigOut"]
            ).optional(),
            "insertBeforeChoice": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut"]
    )
    types["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"] = t.struct(
        {
            "labelPermission": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelPermissionIn"]
            ),
            "parent": t.string(),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"])
    types["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"] = t.struct(
        {
            "labelPermission": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]
            ),
            "parent": t.string(),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
    ] = t.struct({"fieldId": t.string().optional(), "id": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
    ] = t.struct(
        {
            "fieldId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn"] = t.struct(
        {
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut"] = t.struct(
        {
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut"])
    types["GoogleAppsDriveLabelsV2BadgeColorsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2BadgeColorsIn"])
    types["GoogleAppsDriveLabelsV2BadgeColorsOut"] = t.struct(
        {
            "foregroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "soloColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BadgeColorsOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsIn"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsIn"]
            ).optional(),
            "id": t.string(),
            "longTextOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsIn"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"]
            ).optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsIn"]
            ).optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsOut"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsOut"]
            ).optional(),
            "id": t.string(),
            "longTextOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsOut"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"]
            ).optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsOut"]
            ).optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut"
        ]
    )

    functions = {}
    functions["labelsDelete"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsDelta"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsDisable"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsUpdateLabelCopyMode"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsGet"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsList"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPublish"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsCreate"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsEnable"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsUpdatePermissions"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsLocksList"] = drivelabels.get(
        "v2/{parent}/locks",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsUpdatePermissions"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsLocksList"] = drivelabels.get(
        "v2/{parent}/locks",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsBatchUpdate"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsDelete"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsBatchDelete"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsList"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsCreate"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "email": t.string().optional(),
                "person": t.string().optional(),
                "name": t.string().optional(),
                "role": t.string().optional(),
                "audience": t.string().optional(),
                "group": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsCreate"] = drivelabels.post(
        "v2/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(
                    t.proxy(
                        renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                    )
                ),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsList"] = drivelabels.post(
        "v2/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(
                    t.proxy(
                        renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                    )
                ),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsBatchUpdate"] = drivelabels.post(
        "v2/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(
                    t.proxy(
                        renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                    )
                ),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsDelete"] = drivelabels.post(
        "v2/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(
                    t.proxy(
                        renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                    )
                ),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsBatchDelete"] = drivelabels.post(
        "v2/{parent}/permissions:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "requests": t.array(
                    t.proxy(
                        renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                    )
                ),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetCapabilities"] = drivelabels.get(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2UserCapabilitiesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["limitsGetLabel"] = drivelabels.get(
        "v2/limits/label",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelLimitsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="drivelabels",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
