from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_chromepolicy() -> Import:
    chromepolicy = HTTPRuntime("https://chromepolicy.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromepolicy_1_ErrorResponse",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn": "_chromepolicy_2_GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut": "_chromepolicy_3_GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut",
        "GoogleChromePolicyVersionsV1PolicyTargetKeyIn": "_chromepolicy_4_GoogleChromePolicyVersionsV1PolicyTargetKeyIn",
        "GoogleChromePolicyVersionsV1PolicyTargetKeyOut": "_chromepolicy_5_GoogleChromePolicyVersionsV1PolicyTargetKeyOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn": "_chromepolicy_6_GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut": "_chromepolicy_7_GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut",
        "GoogleChromePolicyVersionsV1NetworkSettingIn": "_chromepolicy_8_GoogleChromePolicyVersionsV1NetworkSettingIn",
        "GoogleChromePolicyVersionsV1NetworkSettingOut": "_chromepolicy_9_GoogleChromePolicyVersionsV1NetworkSettingOut",
        "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn": "_chromepolicy_10_GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn",
        "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut": "_chromepolicy_11_GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut",
        "Proto2OneofDescriptorProtoIn": "_chromepolicy_12_Proto2OneofDescriptorProtoIn",
        "Proto2OneofDescriptorProtoOut": "_chromepolicy_13_Proto2OneofDescriptorProtoOut",
        "Proto2EnumDescriptorProtoIn": "_chromepolicy_14_Proto2EnumDescriptorProtoIn",
        "Proto2EnumDescriptorProtoOut": "_chromepolicy_15_Proto2EnumDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn": "_chromepolicy_16_GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn",
        "GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut": "_chromepolicy_17_GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut",
        "Proto2FileDescriptorProtoIn": "_chromepolicy_18_Proto2FileDescriptorProtoIn",
        "Proto2FileDescriptorProtoOut": "_chromepolicy_19_Proto2FileDescriptorProtoOut",
        "Proto2FieldDescriptorProtoIn": "_chromepolicy_20_Proto2FieldDescriptorProtoIn",
        "Proto2FieldDescriptorProtoOut": "_chromepolicy_21_Proto2FieldDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn": "_chromepolicy_22_GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn",
        "GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut": "_chromepolicy_23_GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut",
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn": "_chromepolicy_24_GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn",
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut": "_chromepolicy_25_GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut",
        "GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn": "_chromepolicy_26_GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn",
        "GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut": "_chromepolicy_27_GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut",
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn": "_chromepolicy_28_GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut": "_chromepolicy_29_GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn": "_chromepolicy_30_GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut": "_chromepolicy_31_GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut",
        "GoogleChromePolicyVersionsV1FieldConstraintsIn": "_chromepolicy_32_GoogleChromePolicyVersionsV1FieldConstraintsIn",
        "GoogleChromePolicyVersionsV1FieldConstraintsOut": "_chromepolicy_33_GoogleChromePolicyVersionsV1FieldConstraintsOut",
        "GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn": "_chromepolicy_34_GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut": "_chromepolicy_35_GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1PolicySchemaIn": "_chromepolicy_36_GoogleChromePolicyVersionsV1PolicySchemaIn",
        "GoogleChromePolicyVersionsV1PolicySchemaOut": "_chromepolicy_37_GoogleChromePolicyVersionsV1PolicySchemaOut",
        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn": "_chromepolicy_38_GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut": "_chromepolicy_39_GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorIn": "_chromepolicy_40_GoogleChromePolicyVersionsV1PolicyModificationErrorIn",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorOut": "_chromepolicy_41_GoogleChromePolicyVersionsV1PolicyModificationErrorOut",
        "GoogleChromePolicyVersionsV1CertificateReferenceIn": "_chromepolicy_42_GoogleChromePolicyVersionsV1CertificateReferenceIn",
        "GoogleChromePolicyVersionsV1CertificateReferenceOut": "_chromepolicy_43_GoogleChromePolicyVersionsV1CertificateReferenceOut",
        "GoogleChromePolicyVersionsV1DefineNetworkResponseIn": "_chromepolicy_44_GoogleChromePolicyVersionsV1DefineNetworkResponseIn",
        "GoogleChromePolicyVersionsV1DefineNetworkResponseOut": "_chromepolicy_45_GoogleChromePolicyVersionsV1DefineNetworkResponseOut",
        "GoogleChromePolicyVersionsV1RemoveNetworkResponseIn": "_chromepolicy_46_GoogleChromePolicyVersionsV1RemoveNetworkResponseIn",
        "GoogleChromePolicyVersionsV1RemoveNetworkResponseOut": "_chromepolicy_47_GoogleChromePolicyVersionsV1RemoveNetworkResponseOut",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn": "_chromepolicy_48_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut": "_chromepolicy_49_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut",
        "GoogleChromePolicyVersionsV1DefineCertificateResponseIn": "_chromepolicy_50_GoogleChromePolicyVersionsV1DefineCertificateResponseIn",
        "GoogleChromePolicyVersionsV1DefineCertificateResponseOut": "_chromepolicy_51_GoogleChromePolicyVersionsV1DefineCertificateResponseOut",
        "GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn": "_chromepolicy_52_GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn",
        "GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut": "_chromepolicy_53_GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut",
        "GoogleTypeDateIn": "_chromepolicy_54_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_chromepolicy_55_GoogleTypeDateOut",
        "GoogleChromePolicyVersionsV1ResolveRequestIn": "_chromepolicy_56_GoogleChromePolicyVersionsV1ResolveRequestIn",
        "GoogleChromePolicyVersionsV1ResolveRequestOut": "_chromepolicy_57_GoogleChromePolicyVersionsV1ResolveRequestOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateRequestIn": "_chromepolicy_58_GoogleChromePolicyVersionsV1RemoveCertificateRequestIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateRequestOut": "_chromepolicy_59_GoogleChromePolicyVersionsV1RemoveCertificateRequestOut",
        "GoogleChromePolicyVersionsV1ResolvedPolicyIn": "_chromepolicy_60_GoogleChromePolicyVersionsV1ResolvedPolicyIn",
        "GoogleChromePolicyVersionsV1ResolvedPolicyOut": "_chromepolicy_61_GoogleChromePolicyVersionsV1ResolvedPolicyOut",
        "GoogleChromePolicyVersionsV1DefineCertificateRequestIn": "_chromepolicy_62_GoogleChromePolicyVersionsV1DefineCertificateRequestIn",
        "GoogleChromePolicyVersionsV1DefineCertificateRequestOut": "_chromepolicy_63_GoogleChromePolicyVersionsV1DefineCertificateRequestOut",
        "ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn": "_chromepolicy_64_ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn",
        "ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut": "_chromepolicy_65_ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn": "_chromepolicy_66_GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut": "_chromepolicy_67_GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn": "_chromepolicy_68_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut": "_chromepolicy_69_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn": "_chromepolicy_70_GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut": "_chromepolicy_71_GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut",
        "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn": "_chromepolicy_72_GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn",
        "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut": "_chromepolicy_73_GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut",
        "GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn": "_chromepolicy_74_GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut": "_chromepolicy_75_GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn": "_chromepolicy_76_GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn",
        "GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut": "_chromepolicy_77_GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut",
        "GoogleProtobufEmptyIn": "_chromepolicy_78_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_chromepolicy_79_GoogleProtobufEmptyOut",
        "GoogleChromePolicyVersionsV1DefineNetworkRequestIn": "_chromepolicy_80_GoogleChromePolicyVersionsV1DefineNetworkRequestIn",
        "GoogleChromePolicyVersionsV1DefineNetworkRequestOut": "_chromepolicy_81_GoogleChromePolicyVersionsV1DefineNetworkRequestOut",
        "GoogleChromePolicyVersionsV1NumericRangeConstraintIn": "_chromepolicy_82_GoogleChromePolicyVersionsV1NumericRangeConstraintIn",
        "GoogleChromePolicyVersionsV1NumericRangeConstraintOut": "_chromepolicy_83_GoogleChromePolicyVersionsV1NumericRangeConstraintOut",
        "GoogleChromePolicyVersionsV1RemoveNetworkRequestIn": "_chromepolicy_84_GoogleChromePolicyVersionsV1RemoveNetworkRequestIn",
        "GoogleChromePolicyVersionsV1RemoveNetworkRequestOut": "_chromepolicy_85_GoogleChromePolicyVersionsV1RemoveNetworkRequestOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateResponseIn": "_chromepolicy_86_GoogleChromePolicyVersionsV1RemoveCertificateResponseIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateResponseOut": "_chromepolicy_87_GoogleChromePolicyVersionsV1RemoveCertificateResponseOut",
        "Proto2DescriptorProtoIn": "_chromepolicy_88_Proto2DescriptorProtoIn",
        "Proto2DescriptorProtoOut": "_chromepolicy_89_Proto2DescriptorProtoOut",
        "GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn": "_chromepolicy_90_GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut": "_chromepolicy_91_GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn": "_chromepolicy_92_GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn",
        "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut": "_chromepolicy_93_GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut",
        "GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn": "_chromepolicy_94_GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn",
        "GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut": "_chromepolicy_95_GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut",
        "GoogleChromePolicyVersionsV1PolicyValueIn": "_chromepolicy_96_GoogleChromePolicyVersionsV1PolicyValueIn",
        "GoogleChromePolicyVersionsV1PolicyValueOut": "_chromepolicy_97_GoogleChromePolicyVersionsV1PolicyValueOut",
        "GoogleChromePolicyVersionsV1ResolveResponseIn": "_chromepolicy_98_GoogleChromePolicyVersionsV1ResolveResponseIn",
        "GoogleChromePolicyVersionsV1ResolveResponseOut": "_chromepolicy_99_GoogleChromePolicyVersionsV1ResolveResponseOut",
        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn": "_chromepolicy_100_GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn",
        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut": "_chromepolicy_101_GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut",
        "Proto2EnumValueDescriptorProtoIn": "_chromepolicy_102_Proto2EnumValueDescriptorProtoIn",
        "Proto2EnumValueDescriptorProtoOut": "_chromepolicy_103_Proto2EnumValueDescriptorProtoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut"] = t.struct(
        {
            "modificationErrors": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1PolicyModificationErrorOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut"])
    types["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"] = t.struct(
        {
            "additionalTargetKeys": t.struct({"_": t.string().optional()}).optional(),
            "targetResource": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"])
    types["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"] = t.struct(
        {
            "additionalTargetKeys": t.struct({"_": t.string().optional()}).optional(),
            "targetResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn"] = t.struct(
        {
            "sourceField": t.string().optional(),
            "sourceFieldValue": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"] = t.struct(
        {
            "sourceField": t.string().optional(),
            "sourceFieldValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"])
    types["GoogleChromePolicyVersionsV1NetworkSettingIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "policySchema": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
    types["GoogleChromePolicyVersionsV1NetworkSettingOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "policySchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
    types["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "policySchema": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut"] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "policySchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut"])
    types["Proto2OneofDescriptorProtoIn"] = t.struct({"name": t.string()}).named(
        renames["Proto2OneofDescriptorProtoIn"]
    )
    types["Proto2OneofDescriptorProtoOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["Proto2OneofDescriptorProtoOut"])
    types["Proto2EnumDescriptorProtoIn"] = t.struct(
        {
            "name": t.string(),
            "value": t.array(t.proxy(renames["Proto2EnumValueDescriptorProtoIn"])),
        }
    ).named(renames["Proto2EnumDescriptorProtoIn"])
    types["Proto2EnumDescriptorProtoOut"] = t.struct(
        {
            "name": t.string(),
            "value": t.array(t.proxy(renames["Proto2EnumValueDescriptorProtoOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2EnumDescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn"] = t.struct(
        {"keyDescription": t.string().optional(), "key": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn"])
    types["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut"] = t.struct(
        {
            "keyDescription": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut"])
    types["Proto2FileDescriptorProtoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoIn"])),
            "messageType": t.array(
                t.proxy(renames["Proto2DescriptorProtoIn"])
            ).optional(),
            "package": t.string().optional(),
        }
    ).named(renames["Proto2FileDescriptorProtoIn"])
    types["Proto2FileDescriptorProtoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoOut"])),
            "messageType": t.array(
                t.proxy(renames["Proto2DescriptorProtoOut"])
            ).optional(),
            "package": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2FileDescriptorProtoOut"])
    types["Proto2FieldDescriptorProtoIn"] = t.struct(
        {
            "name": t.string(),
            "jsonName": t.string().optional(),
            "typeName": t.string().optional(),
            "proto3Optional": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer(),
            "defaultValue": t.string().optional(),
            "label": t.string(),
            "type": t.string().optional(),
        }
    ).named(renames["Proto2FieldDescriptorProtoIn"])
    types["Proto2FieldDescriptorProtoOut"] = t.struct(
        {
            "name": t.string(),
            "jsonName": t.string().optional(),
            "typeName": t.string().optional(),
            "proto3Optional": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer(),
            "defaultValue": t.string().optional(),
            "label": t.string(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2FieldDescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn"] = t.struct(
        {
            "policySchemas": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1PolicySchemaIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn"])
    types["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"] = t.struct(
        {
            "policySchemas": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1PolicySchemaOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"])
    types[
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn"
    ] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "policySchema": t.string().optional(),
            "policyNamespace": t.string().optional(),
            "groupIds": t.array(t.string()),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn"]
    )
    types[
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut"
    ] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "policySchema": t.string().optional(),
            "policyNamespace": t.string().optional(),
            "groupIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut"]
    )
    types["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueIn"]
            ).optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueOut"]
            ).optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut"])
    types[
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn"
    ] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"]
                )
            ).optional()
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn"]
    )
    types[
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut"
    ] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut"]
    )
    types["GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut"] = t.struct(
        {
            "certificateReferences": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1CertificateReferenceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut"])
    types["GoogleChromePolicyVersionsV1FieldConstraintsIn"] = t.struct(
        {
            "numericRangeConstraint": t.proxy(
                renames["GoogleChromePolicyVersionsV1NumericRangeConstraintIn"]
            ).optional()
        }
    ).named(renames["GoogleChromePolicyVersionsV1FieldConstraintsIn"])
    types["GoogleChromePolicyVersionsV1FieldConstraintsOut"] = t.struct(
        {
            "numericRangeConstraint": t.proxy(
                renames["GoogleChromePolicyVersionsV1NumericRangeConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1FieldConstraintsOut"])
    types["GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn"])
    types["GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaIn"] = t.struct(
        {
            "definition": t.proxy(renames["Proto2FileDescriptorProtoIn"]).optional(),
            "categoryTitle": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaOut"] = t.struct(
        {
            "definition": t.proxy(renames["Proto2FileDescriptorProtoOut"]).optional(),
            "categoryTitle": t.string().optional(),
            "accessRestrictions": t.array(t.string()).optional(),
            "validTargetResources": t.array(t.string()).optional(),
            "policyDescription": t.string().optional(),
            "notices": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"
                    ]
                )
            ).optional(),
            "name": t.string().optional(),
            "fieldDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"
                    ]
                )
            ).optional(),
            "schemaName": t.string().optional(),
            "policyApiLifecycle": t.proxy(
                renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"]
            ).optional(),
            "additionalTargetKeyNames": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut"]
                )
            ).optional(),
            "supportUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"] = t.struct(
        {
            "noticeMessage": t.string().optional(),
            "field": t.string().optional(),
            "acknowledgementRequired": t.boolean().optional(),
            "noticeValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorIn"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorOut"] = t.struct(
        {
            "fieldErrors": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"
                    ]
                )
            ).optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "errors": t.array(t.string()).optional(),
            "policySchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorOut"])
    types["GoogleChromePolicyVersionsV1CertificateReferenceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1CertificateReferenceIn"])
    types["GoogleChromePolicyVersionsV1CertificateReferenceOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1CertificateReferenceOut"])
    types["GoogleChromePolicyVersionsV1DefineNetworkResponseIn"] = t.struct(
        {
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ).optional(),
            "targetResource": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineNetworkResponseIn"])
    types["GoogleChromePolicyVersionsV1DefineNetworkResponseOut"] = t.struct(
        {
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ).optional(),
            "targetResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineNetworkResponseOut"])
    types["GoogleChromePolicyVersionsV1RemoveNetworkResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkResponseIn"])
    types["GoogleChromePolicyVersionsV1RemoveNetworkResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkResponseOut"])
    types["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn"])
    types[
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut"
    ] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "groupIds": t.array(t.string()).optional(),
            "policySchema": t.string().optional(),
            "policyNamespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut"]
    )
    types["GoogleChromePolicyVersionsV1DefineCertificateResponseIn"] = t.struct(
        {
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ).optional(),
            "targetResource": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseIn"])
    types["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"] = t.struct(
        {
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ).optional(),
            "targetResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn"] = t.struct(
        {
            "requiredFields": t.array(t.string()).optional(),
            "fieldConditions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut"] = t.struct(
        {
            "requiredFields": t.array(t.string()).optional(),
            "fieldConditions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleChromePolicyVersionsV1ResolveRequestIn"] = t.struct(
        {
            "policySchemaFilter": t.string(),
            "pageSize": t.integer().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "pageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveRequestIn"])
    types["GoogleChromePolicyVersionsV1ResolveRequestOut"] = t.struct(
        {
            "policySchemaFilter": t.string(),
            "pageSize": t.integer().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveRequestOut"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateRequestIn"] = t.struct(
        {"targetResource": t.string(), "networkId": t.string()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateRequestIn"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateRequestOut"] = t.struct(
        {
            "targetResource": t.string(),
            "networkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateRequestOut"])
    types["GoogleChromePolicyVersionsV1ResolvedPolicyIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1ResolvedPolicyIn"])
    types["GoogleChromePolicyVersionsV1ResolvedPolicyOut"] = t.struct(
        {
            "addedSourceKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "targetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "value": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueOut"]
            ).optional(),
            "sourceKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolvedPolicyOut"])
    types["GoogleChromePolicyVersionsV1DefineCertificateRequestIn"] = t.struct(
        {
            "ceritificateName": t.string().optional(),
            "certificate": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ).optional(),
            "targetResource": t.string(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateRequestIn"])
    types["GoogleChromePolicyVersionsV1DefineCertificateRequestOut"] = t.struct(
        {
            "ceritificateName": t.string().optional(),
            "certificate": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ).optional(),
            "targetResource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateRequestOut"])
    types["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn"] = t.struct(
        {
            "deprecatedInFavorOf": t.array(t.string()).optional(),
            "policyApiLifecycleStage": t.string().optional(),
            "endSupport": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn"])
    types["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"] = t.struct(
        {
            "deprecatedInFavorOf": t.array(t.string()).optional(),
            "policyApiLifecycleStage": t.string().optional(),
            "endSupport": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"])
    types[
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn"]
    )
    types[
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"
    ] = t.struct(
        {
            "description": t.string().optional(),
            "value": t.string().optional(),
            "fieldDependencies": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"]
    )
    types["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn"] = t.struct(
        {
            "policyNamespace": t.string().optional(),
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn"])
    types["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut"] = t.struct(
        {
            "policyNamespace": t.string().optional(),
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn"] = t.struct(
        {"description": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"] = t.struct(
        {
            "fieldConstraints": t.proxy(
                renames["GoogleChromePolicyVersionsV1FieldConstraintsOut"]
            ).optional(),
            "knownValueDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"
                    ]
                )
            ).optional(),
            "requiredItems": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut"]
                )
            ).optional(),
            "description": t.string().optional(),
            "nestedFieldDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"
                    ]
                )
            ).optional(),
            "inputConstraint": t.string().optional(),
            "fieldDependencies": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"
                    ]
                )
            ).optional(),
            "name": t.string().optional(),
            "fieldDescription": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"])
    types["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueIn"]
            ).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut"])
    types["GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn"])
    types["GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn"] = t.struct(
        {"downloadUri": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut"] = t.struct(
        {
            "downloadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleChromePolicyVersionsV1DefineNetworkRequestIn"] = t.struct(
        {
            "targetResource": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ),
            "name": t.string(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineNetworkRequestIn"])
    types["GoogleChromePolicyVersionsV1DefineNetworkRequestOut"] = t.struct(
        {
            "targetResource": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineNetworkRequestOut"])
    types["GoogleChromePolicyVersionsV1NumericRangeConstraintIn"] = t.struct(
        {"maximum": t.string().optional(), "minimum": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1NumericRangeConstraintIn"])
    types["GoogleChromePolicyVersionsV1NumericRangeConstraintOut"] = t.struct(
        {
            "maximum": t.string().optional(),
            "minimum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1NumericRangeConstraintOut"])
    types["GoogleChromePolicyVersionsV1RemoveNetworkRequestIn"] = t.struct(
        {"targetResource": t.string(), "networkId": t.string()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkRequestIn"])
    types["GoogleChromePolicyVersionsV1RemoveNetworkRequestOut"] = t.struct(
        {
            "targetResource": t.string(),
            "networkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkRequestOut"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseIn"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"])
    types["Proto2DescriptorProtoIn"] = t.struct(
        {
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoIn"])),
            "field": t.array(t.proxy(renames["Proto2FieldDescriptorProtoIn"])),
            "name": t.string(),
            "oneofDecl": t.array(t.proxy(renames["Proto2OneofDescriptorProtoIn"])),
            "nestedType": t.array(t.proxy(renames["Proto2DescriptorProtoIn"])),
        }
    ).named(renames["Proto2DescriptorProtoIn"])
    types["Proto2DescriptorProtoOut"] = t.struct(
        {
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoOut"])),
            "field": t.array(t.proxy(renames["Proto2FieldDescriptorProtoOut"])),
            "name": t.string(),
            "oneofDecl": t.array(t.proxy(renames["Proto2OneofDescriptorProtoOut"])),
            "nestedType": t.array(t.proxy(renames["Proto2DescriptorProtoOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2DescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn"] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn"]
                )
            ).optional()
        }
    ).named(renames["GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn"])
    types[
        "GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut"
    ] = t.struct(
        {
            "requests": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut"]
    )
    types["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "policySchema": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut"] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "policySchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn"] = t.struct(
        {"policyField": t.string()}
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut"] = t.struct(
        {
            "policyField": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut"])
    types["GoogleChromePolicyVersionsV1PolicyValueIn"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyValueIn"])
    types["GoogleChromePolicyVersionsV1PolicyValueOut"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyValueOut"])
    types["GoogleChromePolicyVersionsV1ResolveResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resolvedPolicies": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1ResolvedPolicyIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveResponseIn"])
    types["GoogleChromePolicyVersionsV1ResolveResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resolvedPolicies": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1ResolvedPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveResponseOut"])
    types["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn"])
    types["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"] = t.struct(
        {
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"])
    types["Proto2EnumValueDescriptorProtoIn"] = t.struct(
        {"number": t.integer(), "name": t.string()}
    ).named(renames["Proto2EnumValueDescriptorProtoIn"])
    types["Proto2EnumValueDescriptorProtoOut"] = t.struct(
        {
            "number": t.integer(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2EnumValueDescriptorProtoOut"])

    functions = {}
    functions["customersPoliciesResolve"] = chromepolicy.post(
        "v1/{customer}/policies:resolve",
        t.struct(
            {
                "customer": t.string().optional(),
                "policySchemaFilter": t.string(),
                "pageSize": t.integer().optional(),
                "policyTargetKey": t.proxy(
                    renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
                ),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1ResolveResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksDefineCertificate"] = chromepolicy.post(
        "v1/{customer}/policies/networks:removeCertificate",
        t.struct(
            {
                "customer": t.string(),
                "targetResource": t.string(),
                "networkId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksDefineNetwork"] = chromepolicy.post(
        "v1/{customer}/policies/networks:removeCertificate",
        t.struct(
            {
                "customer": t.string(),
                "targetResource": t.string(),
                "networkId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksRemoveNetwork"] = chromepolicy.post(
        "v1/{customer}/policies/networks:removeCertificate",
        t.struct(
            {
                "customer": t.string(),
                "targetResource": t.string(),
                "networkId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksRemoveCertificate"] = chromepolicy.post(
        "v1/{customer}/policies/networks:removeCertificate",
        t.struct(
            {
                "customer": t.string(),
                "targetResource": t.string(),
                "networkId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesOrgunitsBatchModify"] = chromepolicy.post(
        "v1/{customer}/policies/orgunits:batchInherit",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesOrgunitsBatchInherit"] = chromepolicy.post(
        "v1/{customer}/policies/orgunits:batchInherit",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesGroupsUpdateGroupPriorityOrdering"] = chromepolicy.post(
        "v1/{customer}/policies/groups:batchDelete",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesGroupsBatchModify"] = chromepolicy.post(
        "v1/{customer}/policies/groups:batchDelete",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesGroupsListGroupPriorityOrdering"] = chromepolicy.post(
        "v1/{customer}/policies/groups:batchDelete",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesGroupsBatchDelete"] = chromepolicy.post(
        "v1/{customer}/policies/groups:batchDelete",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPolicySchemasGet"] = chromepolicy.get(
        "v1/{parent}/policySchemas",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPolicySchemasList"] = chromepolicy.get(
        "v1/{parent}/policySchemas",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = chromepolicy.post(
        "v1/{customer}/policies/files:uploadPolicyFile",
        t.struct(
            {
                "customer": t.string(),
                "policyField": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chromepolicy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
