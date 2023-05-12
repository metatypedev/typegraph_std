from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_drivelabels() -> Import:
    drivelabels = HTTPRuntime("https://drivelabels.googleapis.com/")

    renames = {
        "ErrorResponse": "_drivelabels_1_ErrorResponse",
        "GoogleAppsDriveLabelsV2LabelDisplayHintsIn": "_drivelabels_2_GoogleAppsDriveLabelsV2LabelDisplayHintsIn",
        "GoogleAppsDriveLabelsV2LabelDisplayHintsOut": "_drivelabels_3_GoogleAppsDriveLabelsV2LabelDisplayHintsOut",
        "GoogleAppsDriveLabelsV2FieldIntegerOptionsIn": "_drivelabels_4_GoogleAppsDriveLabelsV2FieldIntegerOptionsIn",
        "GoogleAppsDriveLabelsV2FieldIntegerOptionsOut": "_drivelabels_5_GoogleAppsDriveLabelsV2FieldIntegerOptionsOut",
        "GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn": "_drivelabels_6_GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut": "_drivelabels_7_GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn": "_drivelabels_8_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut": "_drivelabels_9_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn": "_drivelabels_10_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut": "_drivelabels_11_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn": "_drivelabels_12_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut": "_drivelabels_13_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut",
        "GoogleAppsDriveLabelsV2PublishLabelRequestIn": "_drivelabels_14_GoogleAppsDriveLabelsV2PublishLabelRequestIn",
        "GoogleAppsDriveLabelsV2PublishLabelRequestOut": "_drivelabels_15_GoogleAppsDriveLabelsV2PublishLabelRequestOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn": "_drivelabels_16_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut": "_drivelabels_17_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut",
        "GoogleAppsDriveLabelsV2ListLabelsResponseIn": "_drivelabels_18_GoogleAppsDriveLabelsV2ListLabelsResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelsResponseOut": "_drivelabels_19_GoogleAppsDriveLabelsV2ListLabelsResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn": "_drivelabels_20_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut": "_drivelabels_21_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequestOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn": "_drivelabels_22_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut": "_drivelabels_23_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn": "_drivelabels_24_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut": "_drivelabels_25_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn": "_drivelabels_26_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut": "_drivelabels_27_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut",
        "GoogleAppsDriveLabelsV2LabelLimitsIn": "_drivelabels_28_GoogleAppsDriveLabelsV2LabelLimitsIn",
        "GoogleAppsDriveLabelsV2LabelLimitsOut": "_drivelabels_29_GoogleAppsDriveLabelsV2LabelLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn": "_drivelabels_30_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut": "_drivelabels_31_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut",
        "GoogleAppsDriveLabelsV2DisableLabelRequestIn": "_drivelabels_32_GoogleAppsDriveLabelsV2DisableLabelRequestIn",
        "GoogleAppsDriveLabelsV2DisableLabelRequestOut": "_drivelabels_33_GoogleAppsDriveLabelsV2DisableLabelRequestOut",
        "GoogleAppsDriveLabelsV2LabelPermissionIn": "_drivelabels_34_GoogleAppsDriveLabelsV2LabelPermissionIn",
        "GoogleAppsDriveLabelsV2LabelPermissionOut": "_drivelabels_35_GoogleAppsDriveLabelsV2LabelPermissionOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn": "_drivelabels_36_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut": "_drivelabels_37_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut",
        "GoogleAppsDriveLabelsV2UserInfoIn": "_drivelabels_38_GoogleAppsDriveLabelsV2UserInfoIn",
        "GoogleAppsDriveLabelsV2UserInfoOut": "_drivelabels_39_GoogleAppsDriveLabelsV2UserInfoOut",
        "GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn": "_drivelabels_40_GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn",
        "GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut": "_drivelabels_41_GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn": "_drivelabels_42_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseIn",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut": "_drivelabels_43_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponseOut",
        "GoogleAppsDriveLabelsV2ListLimitsIn": "_drivelabels_44_GoogleAppsDriveLabelsV2ListLimitsIn",
        "GoogleAppsDriveLabelsV2ListLimitsOut": "_drivelabels_45_GoogleAppsDriveLabelsV2ListLimitsOut",
        "GoogleTypeDateIn": "_drivelabels_46_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_drivelabels_47_GoogleTypeDateOut",
        "GoogleAppsDriveLabelsV2FieldIn": "_drivelabels_48_GoogleAppsDriveLabelsV2FieldIn",
        "GoogleAppsDriveLabelsV2FieldOut": "_drivelabels_49_GoogleAppsDriveLabelsV2FieldOut",
        "GoogleAppsDriveLabelsV2UserLimitsIn": "_drivelabels_50_GoogleAppsDriveLabelsV2UserLimitsIn",
        "GoogleAppsDriveLabelsV2UserLimitsOut": "_drivelabels_51_GoogleAppsDriveLabelsV2UserLimitsOut",
        "GoogleAppsDriveLabelsV2WriteControlIn": "_drivelabels_52_GoogleAppsDriveLabelsV2WriteControlIn",
        "GoogleAppsDriveLabelsV2WriteControlOut": "_drivelabels_53_GoogleAppsDriveLabelsV2WriteControlOut",
        "GoogleAppsDriveLabelsV2TextLimitsIn": "_drivelabels_54_GoogleAppsDriveLabelsV2TextLimitsIn",
        "GoogleAppsDriveLabelsV2TextLimitsOut": "_drivelabels_55_GoogleAppsDriveLabelsV2TextLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn": "_drivelabels_56_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut": "_drivelabels_57_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseOut",
        "GoogleAppsDriveLabelsV2FieldPropertiesIn": "_drivelabels_58_GoogleAppsDriveLabelsV2FieldPropertiesIn",
        "GoogleAppsDriveLabelsV2FieldPropertiesOut": "_drivelabels_59_GoogleAppsDriveLabelsV2FieldPropertiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn": "_drivelabels_60_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut": "_drivelabels_61_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn": "_drivelabels_62_GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn",
        "GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut": "_drivelabels_63_GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut",
        "GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn": "_drivelabels_64_GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn",
        "GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut": "_drivelabels_65_GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut",
        "GoogleAppsDriveLabelsV2IntegerLimitsIn": "_drivelabels_66_GoogleAppsDriveLabelsV2IntegerLimitsIn",
        "GoogleAppsDriveLabelsV2IntegerLimitsOut": "_drivelabels_67_GoogleAppsDriveLabelsV2IntegerLimitsOut",
        "GoogleAppsDriveLabelsV2FieldUserOptionsIn": "_drivelabels_68_GoogleAppsDriveLabelsV2FieldUserOptionsIn",
        "GoogleAppsDriveLabelsV2FieldUserOptionsOut": "_drivelabels_69_GoogleAppsDriveLabelsV2FieldUserOptionsOut",
        "GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn": "_drivelabels_70_GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn",
        "GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut": "_drivelabels_71_GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn": "_drivelabels_72_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut": "_drivelabels_73_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut",
        "GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn": "_drivelabels_74_GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut": "_drivelabels_75_GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut",
        "GoogleAppsDriveLabelsV2FieldLongTextOptionsIn": "_drivelabels_76_GoogleAppsDriveLabelsV2FieldLongTextOptionsIn",
        "GoogleAppsDriveLabelsV2FieldLongTextOptionsOut": "_drivelabels_77_GoogleAppsDriveLabelsV2FieldLongTextOptionsOut",
        "GoogleAppsDriveLabelsV2LabelIn": "_drivelabels_78_GoogleAppsDriveLabelsV2LabelIn",
        "GoogleAppsDriveLabelsV2LabelOut": "_drivelabels_79_GoogleAppsDriveLabelsV2LabelOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn": "_drivelabels_80_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut": "_drivelabels_81_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2LabelPropertiesIn": "_drivelabels_82_GoogleAppsDriveLabelsV2LabelPropertiesIn",
        "GoogleAppsDriveLabelsV2LabelPropertiesOut": "_drivelabels_83_GoogleAppsDriveLabelsV2LabelPropertiesOut",
        "GoogleAppsDriveLabelsV2FieldDisplayHintsIn": "_drivelabels_84_GoogleAppsDriveLabelsV2FieldDisplayHintsIn",
        "GoogleAppsDriveLabelsV2FieldDisplayHintsOut": "_drivelabels_85_GoogleAppsDriveLabelsV2FieldDisplayHintsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn": "_drivelabels_86_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut": "_drivelabels_87_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn": "_drivelabels_88_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut": "_drivelabels_89_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut",
        "GoogleAppsDriveLabelsV2LabelLockIn": "_drivelabels_90_GoogleAppsDriveLabelsV2LabelLockIn",
        "GoogleAppsDriveLabelsV2LabelLockOut": "_drivelabels_91_GoogleAppsDriveLabelsV2LabelLockOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn": "_drivelabels_92_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut": "_drivelabels_93_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2EnableLabelRequestIn": "_drivelabels_94_GoogleAppsDriveLabelsV2EnableLabelRequestIn",
        "GoogleAppsDriveLabelsV2EnableLabelRequestOut": "_drivelabels_95_GoogleAppsDriveLabelsV2EnableLabelRequestOut",
        "GoogleAppsDriveLabelsV2FieldLimitsIn": "_drivelabels_96_GoogleAppsDriveLabelsV2FieldLimitsIn",
        "GoogleAppsDriveLabelsV2FieldLimitsOut": "_drivelabels_97_GoogleAppsDriveLabelsV2FieldLimitsOut",
        "GoogleAppsDriveLabelsV2ListLabelLocksResponseIn": "_drivelabels_98_GoogleAppsDriveLabelsV2ListLabelLocksResponseIn",
        "GoogleAppsDriveLabelsV2ListLabelLocksResponseOut": "_drivelabels_99_GoogleAppsDriveLabelsV2ListLabelLocksResponseOut",
        "GoogleAppsDriveLabelsV2BadgeConfigIn": "_drivelabels_100_GoogleAppsDriveLabelsV2BadgeConfigIn",
        "GoogleAppsDriveLabelsV2BadgeConfigOut": "_drivelabels_101_GoogleAppsDriveLabelsV2BadgeConfigOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn": "_drivelabels_102_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut": "_drivelabels_103_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut",
        "GoogleAppsDriveLabelsV2FieldDateOptionsIn": "_drivelabels_104_GoogleAppsDriveLabelsV2FieldDateOptionsIn",
        "GoogleAppsDriveLabelsV2FieldDateOptionsOut": "_drivelabels_105_GoogleAppsDriveLabelsV2FieldDateOptionsOut",
        "GoogleAppsDriveLabelsV2LockStatusIn": "_drivelabels_106_GoogleAppsDriveLabelsV2LockStatusIn",
        "GoogleAppsDriveLabelsV2LockStatusOut": "_drivelabels_107_GoogleAppsDriveLabelsV2LockStatusOut",
        "GoogleAppsDriveLabelsV2FieldTextOptionsIn": "_drivelabels_108_GoogleAppsDriveLabelsV2FieldTextOptionsIn",
        "GoogleAppsDriveLabelsV2FieldTextOptionsOut": "_drivelabels_109_GoogleAppsDriveLabelsV2FieldTextOptionsOut",
        "GoogleAppsDriveLabelsV2LifecycleIn": "_drivelabels_110_GoogleAppsDriveLabelsV2LifecycleIn",
        "GoogleAppsDriveLabelsV2LifecycleOut": "_drivelabels_111_GoogleAppsDriveLabelsV2LifecycleOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn": "_drivelabels_112_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut": "_drivelabels_113_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn": "_drivelabels_114_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut": "_drivelabels_115_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn": "_drivelabels_116_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut": "_drivelabels_117_GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn": "_drivelabels_118_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut": "_drivelabels_119_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn": "_drivelabels_120_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut": "_drivelabels_121_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut",
        "GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn": "_drivelabels_122_GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn",
        "GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut": "_drivelabels_123_GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn": "_drivelabels_124_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut": "_drivelabels_125_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2FieldListOptionsIn": "_drivelabels_126_GoogleAppsDriveLabelsV2FieldListOptionsIn",
        "GoogleAppsDriveLabelsV2FieldListOptionsOut": "_drivelabels_127_GoogleAppsDriveLabelsV2FieldListOptionsOut",
        "GoogleAppsDriveLabelsV2DateLimitsIn": "_drivelabels_128_GoogleAppsDriveLabelsV2DateLimitsIn",
        "GoogleAppsDriveLabelsV2DateLimitsOut": "_drivelabels_129_GoogleAppsDriveLabelsV2DateLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn": "_drivelabels_130_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut": "_drivelabels_131_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut",
        "GoogleTypeColorIn": "_drivelabels_132_GoogleTypeColorIn",
        "GoogleTypeColorOut": "_drivelabels_133_GoogleTypeColorOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn": "_drivelabels_134_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut": "_drivelabels_135_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut",
        "GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn": "_drivelabels_136_GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut": "_drivelabels_137_GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn": "_drivelabels_138_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn",
        "GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut": "_drivelabels_139_GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn": "_drivelabels_140_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut": "_drivelabels_141_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut",
        "GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn": "_drivelabels_142_GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut": "_drivelabels_143_GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn": "_drivelabels_144_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut": "_drivelabels_145_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut",
        "GoogleAppsDriveLabelsV2SelectionLimitsIn": "_drivelabels_146_GoogleAppsDriveLabelsV2SelectionLimitsIn",
        "GoogleAppsDriveLabelsV2SelectionLimitsOut": "_drivelabels_147_GoogleAppsDriveLabelsV2SelectionLimitsOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn": "_drivelabels_148_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut": "_drivelabels_149_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn": "_drivelabels_150_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut": "_drivelabels_151_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut",
        "GoogleAppsDriveLabelsV2UserCapabilitiesIn": "_drivelabels_152_GoogleAppsDriveLabelsV2UserCapabilitiesIn",
        "GoogleAppsDriveLabelsV2UserCapabilitiesOut": "_drivelabels_153_GoogleAppsDriveLabelsV2UserCapabilitiesOut",
        "GoogleAppsDriveLabelsV2BadgeColorsIn": "_drivelabels_154_GoogleAppsDriveLabelsV2BadgeColorsIn",
        "GoogleAppsDriveLabelsV2BadgeColorsOut": "_drivelabels_155_GoogleAppsDriveLabelsV2BadgeColorsOut",
        "GoogleAppsDriveLabelsV2LongTextLimitsIn": "_drivelabels_156_GoogleAppsDriveLabelsV2LongTextLimitsIn",
        "GoogleAppsDriveLabelsV2LongTextLimitsOut": "_drivelabels_157_GoogleAppsDriveLabelsV2LongTextLimitsOut",
        "GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn": "_drivelabels_158_GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn",
        "GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut": "_drivelabels_159_GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut",
        "GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn": "_drivelabels_160_GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn",
        "GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut": "_drivelabels_161_GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn": "_drivelabels_162_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut": "_drivelabels_163_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn": "_drivelabels_164_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut": "_drivelabels_165_GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn": "_drivelabels_166_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn",
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut": "_drivelabels_167_GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut",
        "GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn": "_drivelabels_168_GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn",
        "GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut": "_drivelabels_169_GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut",
        "GoogleProtobufEmptyIn": "_drivelabels_170_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_drivelabels_171_GoogleProtobufEmptyOut",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsIn": "_drivelabels_172_GoogleAppsDriveLabelsV2FieldSelectionOptionsIn",
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsOut": "_drivelabels_173_GoogleAppsDriveLabelsV2FieldSelectionOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsDriveLabelsV2LabelDisplayHintsIn"] = t.struct(
        {
            "shownInApply": t.boolean().optional(),
            "priority": t.string().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelDisplayHintsIn"])
    types["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"] = t.struct(
        {
            "shownInApply": t.boolean().optional(),
            "priority": t.string().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"])
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
    types["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn"] = t.struct(
        {
            "canEnable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"] = t.struct(
        {
            "canEnable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"])
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
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
    ] = t.struct({"id": t.string().optional(), "fieldId": t.string().optional()}).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
    ] = t.struct(
        {
            "id": t.string().optional(),
            "fieldId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
        ]
    )
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
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn"
    ] = t.struct(
        {
            "badgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsIn"]
            ).optional(),
            "disabled": t.boolean().optional(),
            "darkBadgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsIn"]
            ).optional(),
            "hiddenInSearch": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "badgePriority": t.string().optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"
    ] = t.struct(
        {
            "badgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsOut"]
            ).optional(),
            "disabled": t.boolean().optional(),
            "darkBadgeColors": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeColorsOut"]
            ).optional(),
            "hiddenInSearch": t.boolean().optional(),
            "shownInApply": t.boolean().optional(),
            "badgePriority": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"]
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
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesIn"
    ] = t.struct(
        {
            "canEnable": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
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
            "canEnable": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canUpdate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut"
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
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"]
    )
    types["GoogleAppsDriveLabelsV2LabelLimitsIn"] = t.struct(
        {
            "maxDeletedFields": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
            "maxFields": t.integer().optional(),
            "maxTitleLength": t.integer().optional(),
            "maxDraftRevisions": t.integer().optional(),
            "name": t.string().optional(),
            "fieldLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLimitsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLimitsIn"])
    types["GoogleAppsDriveLabelsV2LabelLimitsOut"] = t.struct(
        {
            "maxDeletedFields": t.integer().optional(),
            "maxDescriptionLength": t.integer().optional(),
            "maxFields": t.integer().optional(),
            "maxTitleLength": t.integer().optional(),
            "maxDraftRevisions": t.integer().optional(),
            "name": t.string().optional(),
            "fieldLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLimitsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLimitsOut"])
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
    types["GoogleAppsDriveLabelsV2DisableLabelRequestIn"] = t.struct(
        {
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ).optional(),
            "updateMask": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DisableLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2DisableLabelRequestOut"] = t.struct(
        {
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ).optional(),
            "updateMask": t.string().optional(),
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DisableLabelRequestOut"])
    types["GoogleAppsDriveLabelsV2LabelPermissionIn"] = t.struct(
        {
            "person": t.string().optional(),
            "audience": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "group": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelPermissionIn"])
    types["GoogleAppsDriveLabelsV2LabelPermissionOut"] = t.struct(
        {
            "person": t.string().optional(),
            "audience": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "group": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"])
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
    types["GoogleAppsDriveLabelsV2UserInfoIn"] = t.struct(
        {"person": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2UserInfoIn"])
    types["GoogleAppsDriveLabelsV2UserInfoOut"] = t.struct(
        {
            "person": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserInfoOut"])
    types["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"]
                )
            ),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestIn"])
    types["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"]
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequestOut"])
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
    types["GoogleAppsDriveLabelsV2ListLimitsIn"] = t.struct(
        {"maxEntries": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2ListLimitsIn"])
    types["GoogleAppsDriveLabelsV2ListLimitsOut"] = t.struct(
        {
            "maxEntries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLimitsOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleAppsDriveLabelsV2FieldIn"] = t.struct(
        {
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsIn"]
            ).optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsIn"]
            ).optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsIn"]
            ).optional(),
            "properties": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldIn"])
    types["GoogleAppsDriveLabelsV2FieldOut"] = t.struct(
        {
            "schemaCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSchemaCapabilitiesOut"]
            ).optional(),
            "dateOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDateOptionsOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "displayHints": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"]
            ).optional(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "userOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldUserOptionsOut"]
            ).optional(),
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsOut"]
            ).optional(),
            "queryKey": t.string().optional(),
            "appliedCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"]
            ).optional(),
            "properties": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"]
            ).optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "disableTime": t.string().optional(),
            "updater": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "id": t.string().optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"]
            ).optional(),
            "integerOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldIntegerOptionsOut"]
            ).optional(),
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldOut"])
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
    types["GoogleAppsDriveLabelsV2WriteControlIn"] = t.struct(
        {"requiredRevisionId": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2WriteControlIn"])
    types["GoogleAppsDriveLabelsV2WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2WriteControlOut"])
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
    types["GoogleAppsDriveLabelsV2FieldPropertiesIn"] = t.struct(
        {
            "displayName": t.string(),
            "required": t.boolean().optional(),
            "insertBeforeField": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"])
    types["GoogleAppsDriveLabelsV2FieldPropertiesOut"] = t.struct(
        {
            "displayName": t.string(),
            "required": t.boolean().optional(),
            "insertBeforeField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "id": t.string(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ),
            "fieldId": t.string(),
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
            "updateMask": t.string().optional(),
            "id": t.string(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ),
            "fieldId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"] = t.struct(
        {"showInApply": t.boolean().optional(), "hideInSearch": t.boolean().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"])
    types["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"] = t.struct(
        {
            "showInApply": t.boolean().optional(),
            "hideInSearch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"])
    types["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "labelPermission": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelPermissionIn"]
            ),
            "parent": t.string(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"])
    types["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "labelPermission": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]
            ),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"])
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
    types["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "copyMode": t.string(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestIn"])
    types["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "copyMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequestOut"])
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
    types["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "labelPermissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseIn"])
    types["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "labelPermissions": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"])
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
    types["GoogleAppsDriveLabelsV2LabelIn"] = t.struct(
        {
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesIn"]),
            "fields": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldIn"])
            ).optional(),
            "learnMoreUri": t.string().optional(),
            "labelType": t.string(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelIn"])
    types["GoogleAppsDriveLabelsV2LabelOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesOut"]),
            "appliedCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelAppliedCapabilitiesOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "revisionId": t.string().optional(),
            "disableTime": t.string().optional(),
            "fields": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldOut"])
            ).optional(),
            "displayHints": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelDisplayHintsOut"]
            ).optional(),
            "appliedLabelPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"]
            ).optional(),
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "learnMoreUri": t.string().optional(),
            "customer": t.string().optional(),
            "schemaCapabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"]
            ).optional(),
            "labelType": t.string(),
            "revisionCreator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelOut"])
    types[
        "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesIn"
    ] = t.struct(
        {
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
            "canSelect": t.boolean().optional(),
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
            "canSearch": t.boolean().optional(),
            "canRead": t.boolean().optional(),
            "canSelect": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut"
        ]
    )
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
    types["GoogleAppsDriveLabelsV2FieldDisplayHintsIn"] = t.struct(
        {
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "required": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDisplayHintsIn"])
    types["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"] = t.struct(
        {
            "shownInApply": t.boolean().optional(),
            "hiddenInSearch": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "required": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDisplayHintsOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "id": t.string(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2FieldPropertiesIn"]),
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
            "updateMask": t.string().optional(),
            "id": t.string(),
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2FieldPropertiesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut"
        ]
    )
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
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "updater": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "disableTime": t.string().optional(),
            "disabler": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "publishTime": t.string().optional(),
            "lockStatus": t.proxy(
                renames["GoogleAppsDriveLabelsV2LockStatusOut"]
            ).optional(),
            "publisher": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"
                ]
            ).optional(),
            "lifecycle": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleOut"]
            ).optional(),
            "schemaCapabilities": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilitiesOut"
                ]
            ).optional(),
            "appliedCapabilities": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilitiesOut"
                ]
            ).optional(),
            "displayHints": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHintsOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"])
    types["GoogleAppsDriveLabelsV2LabelLockIn"] = t.struct(
        {"choiceId": t.string().optional(), "fieldId": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockIn"])
    types["GoogleAppsDriveLabelsV2LabelLockOut"] = t.struct(
        {
            "capabilities": t.proxy(
                renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"]
            ).optional(),
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserInfoOut"]
            ).optional(),
            "choiceId": t.string().optional(),
            "name": t.string().optional(),
            "fieldId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockOut"])
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
    types["GoogleAppsDriveLabelsV2EnableLabelRequestIn"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2EnableLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2EnableLabelRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2EnableLabelRequestOut"])
    types["GoogleAppsDriveLabelsV2FieldLimitsIn"] = t.struct(
        {
            "maxDisplayNameLength": t.integer().optional(),
            "selectionLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2SelectionLimitsIn"]
            ).optional(),
            "textLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2TextLimitsIn"]
            ).optional(),
            "longTextLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2LongTextLimitsIn"]
            ).optional(),
            "dateLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2DateLimitsIn"]
            ).optional(),
            "userLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserLimitsIn"]
            ).optional(),
            "maxDescriptionLength": t.integer().optional(),
            "integerLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2IntegerLimitsIn"]
            ).optional(),
            "maxIdLength": t.integer().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldLimitsIn"])
    types["GoogleAppsDriveLabelsV2FieldLimitsOut"] = t.struct(
        {
            "maxDisplayNameLength": t.integer().optional(),
            "selectionLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2SelectionLimitsOut"]
            ).optional(),
            "textLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2TextLimitsOut"]
            ).optional(),
            "longTextLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2LongTextLimitsOut"]
            ).optional(),
            "dateLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2DateLimitsOut"]
            ).optional(),
            "userLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2UserLimitsOut"]
            ).optional(),
            "maxDescriptionLength": t.integer().optional(),
            "integerLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2IntegerLimitsOut"]
            ).optional(),
            "maxIdLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldLimitsOut"])
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
    types["GoogleAppsDriveLabelsV2FieldDateOptionsIn"] = t.struct(
        {"dateFormatType": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldDateOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldDateOptionsOut"] = t.struct(
        {
            "minValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "dateFormat": t.string().optional(),
            "dateFormatType": t.string().optional(),
            "maxValue": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldDateOptionsOut"])
    types["GoogleAppsDriveLabelsV2LockStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LockStatusIn"])
    types["GoogleAppsDriveLabelsV2LockStatusOut"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LockStatusOut"])
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
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn"] = t.struct(
        {
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
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestIn"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestIn"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestIn"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestIn"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestIn"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestIn"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestIn"
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
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequestOut"
                ]
            ).optional(),
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequestOut"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequestOut"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequestOut"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequestOut"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequestOut"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequestOut"
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
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"] = t.struct(
        {
            "badgeConfig": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeConfigIn"]
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "insertBeforeChoice": t.string().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"] = t.struct(
        {
            "badgeConfig": t.proxy(
                renames["GoogleAppsDriveLabelsV2BadgeConfigOut"]
            ).optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "insertBeforeChoice": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestIn"
    ] = t.struct(
        {
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesIn"
                ]
            ),
            "fieldId": t.string(),
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
            "properties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2FieldSelectionOptionsChoicePropertiesOut"
                ]
            ),
            "fieldId": t.string(),
            "updateMask": t.string().optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequestOut"
        ]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestIn"
    ] = t.struct(
        {
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesIn"]),
            "updateMask": t.string().optional(),
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
            "properties": t.proxy(renames["GoogleAppsDriveLabelsV2LabelPropertiesOut"]),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn"] = t.struct(
        {"copyMode": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyIn"])
    types["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"] = t.struct(
        {
            "copyMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelAppliedLabelPolicyOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestIn"
    ] = t.struct(
        {
            "choice": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"]
            ),
            "fieldId": t.string(),
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
            "choice": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"]
            ),
            "fieldId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequestOut"
        ]
    )
    types["GoogleAppsDriveLabelsV2FieldListOptionsIn"] = t.struct(
        {"maxEntries": t.integer().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2FieldListOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldListOptionsOut"] = t.struct(
        {
            "maxEntries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldListOptionsOut"])
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
    types["GoogleTypeColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["GoogleTypeColorIn"])
    types["GoogleTypeColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "alpha": t.number().optional(),
            "green": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeColorOut"])
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyIn"]
            ),
            "id": t.string(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestIn"]
    )
    types[
        "GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"
    ] = t.struct(
        {
            "updateMask": t.string().optional(),
            "disabledPolicy": t.proxy(
                renames["GoogleAppsDriveLabelsV2LifecycleDisabledPolicyOut"]
            ),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequestOut"]
    )
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
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestIn"]
                )
            ),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestIn"])
    types["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2UpdateLabelPermissionRequestOut"]
                )
            ),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequestOut"])
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
    types["GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn"] = t.struct(
        {"canViewPolicy": t.boolean().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"] = t.struct(
        {
            "canViewPolicy": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelLockCapabilitiesOut"])
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
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsIn"]
            ).optional(),
            "longTextOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsIn"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"]
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
            "textOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldTextOptionsOut"]
            ).optional(),
            "longTextOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldLongTextOptionsOut"]
            ).optional(),
            "selectionOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"]
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
    types["GoogleAppsDriveLabelsV2SelectionLimitsIn"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsIn"]
            ).optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxIdLength": t.integer().optional(),
            "maxDeletedChoices": t.integer().optional(),
            "maxChoices": t.integer().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2SelectionLimitsIn"])
    types["GoogleAppsDriveLabelsV2SelectionLimitsOut"] = t.struct(
        {
            "listLimits": t.proxy(
                renames["GoogleAppsDriveLabelsV2ListLimitsOut"]
            ).optional(),
            "maxDisplayNameLength": t.integer().optional(),
            "maxIdLength": t.integer().optional(),
            "maxDeletedChoices": t.integer().optional(),
            "maxChoices": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2SelectionLimitsOut"])
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
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn"] = t.struct(
        {
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseIn"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseIn"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseIn"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseIn"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseIn"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseIn"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseIn"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseIn"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseIn"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseIn"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseIn"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut"] = t.struct(
        {
            "createField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponseOut"
                ]
            ).optional(),
            "disableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponseOut"
                ]
            ).optional(),
            "updateLabel": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponseOut"
                ]
            ).optional(),
            "disableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponseOut"
                ]
            ).optional(),
            "createSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponseOut"
                ]
            ).optional(),
            "deleteField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponseOut"
                ]
            ).optional(),
            "updateField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponseOut"
                ]
            ).optional(),
            "enableField": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponseOut"
                ]
            ).optional(),
            "updateFieldType": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponseOut"
                ]
            ).optional(),
            "enableSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponseOut"
                ]
            ).optional(),
            "deleteSelectionChoice": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponseOut"
                ]
            ).optional(),
            "updateSelectionChoiceProperties": t.proxy(
                renames[
                    "GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponseOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponseOut"])
    types["GoogleAppsDriveLabelsV2UserCapabilitiesIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2UserCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2UserCapabilitiesOut"] = t.struct(
        {
            "canAccessLabelManager": t.boolean().optional(),
            "canAdministrateLabels": t.boolean().optional(),
            "canCreateSharedLabels": t.boolean().optional(),
            "canCreateAdminLabels": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2UserCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2BadgeColorsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsDriveLabelsV2BadgeColorsIn"])
    types["GoogleAppsDriveLabelsV2BadgeColorsOut"] = t.struct(
        {
            "soloColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "backgroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "foregroundColor": t.proxy(renames["GoogleTypeColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2BadgeColorsOut"])
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
    types["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn"] = t.struct(
        {
            "canRead": t.boolean().optional(),
            "canWrite": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"] = t.struct(
        {
            "canRead": t.boolean().optional(),
            "canWrite": t.boolean().optional(),
            "canSearch": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldAppliedCapabilitiesOut"])
    types["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"] = t.struct(
        {"useAdminAccess": t.boolean().optional(), "name": t.string()}
    ).named(renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestIn"])
    types["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"] = t.struct(
        {
            "useAdminAccess": t.boolean().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeleteLabelPermissionRequestOut"])
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
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlIn"]
            ).optional(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestIn"]
                )
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestIn"])
    types["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(
                renames["GoogleAppsDriveLabelsV2WriteControlOut"]
            ).optional(),
            "view": t.string().optional(),
            "languageCode": t.string().optional(),
            "requests": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequestOut"]
                )
            ).optional(),
            "useAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestOut"])
    types["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn"] = t.struct(
        {
            "canUpdate": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesIn"])
    types["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"] = t.struct(
        {
            "canUpdate": t.boolean().optional(),
            "canEnable": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canDisable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2LabelSchemaCapabilitiesOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"] = t.struct(
        {
            "choices": t.array(
                t.proxy(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceIn"])
            ).optional(),
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsIn"])
    types["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"] = t.struct(
        {
            "choices": t.array(
                t.proxy(
                    renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceOut"]
                )
            ).optional(),
            "listOptions": t.proxy(
                renames["GoogleAppsDriveLabelsV2FieldListOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsDriveLabelsV2FieldSelectionOptionsOut"])

    functions = {}
    functions["labelsDisable"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPublish"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsCreate"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsDelete"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsUpdatePermissions"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsDelta"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsUpdateLabelCopyMode"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsList"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsGet"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsEnable"] = drivelabels.post(
        "v2/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "writeControl": t.proxy(
                    renames["GoogleAppsDriveLabelsV2WriteControlIn"]
                ).optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsUpdatePermissions"] = drivelabels.patch(
        "v2/{parent}/permissions",
        t.struct(
            {
                "parent": t.string(),
                "useAdminAccess": t.boolean().optional(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsBatchUpdate"] = drivelabels.get(
        "v2/{parent}/permissions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsCreate"] = drivelabels.get(
        "v2/{parent}/permissions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsDelete"] = drivelabels.get(
        "v2/{parent}/permissions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsBatchDelete"] = drivelabels.get(
        "v2/{parent}/permissions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsRevisionsPermissionsList"] = drivelabels.get(
        "v2/{parent}/permissions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "useAdminAccess": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsBatchUpdate"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsDelete"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsBatchDelete"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsList"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2LabelPermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["labelsPermissionsCreate"] = drivelabels.post(
        "v2/{parent}/permissions",
        t.struct(
            {
                "useAdminAccess": t.boolean().optional(),
                "parent": t.string(),
                "person": t.string().optional(),
                "audience": t.string().optional(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "group": t.string().optional(),
                "role": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsDriveLabelsV2ListLabelLocksResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetCapabilities"] = drivelabels.get(
        "v2/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
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
