from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_chromepolicy() -> Import:
    chromepolicy = HTTPRuntime("https://chromepolicy.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromepolicy_1_ErrorResponse",
        "Proto2EnumValueDescriptorProtoIn": "_chromepolicy_2_Proto2EnumValueDescriptorProtoIn",
        "Proto2EnumValueDescriptorProtoOut": "_chromepolicy_3_Proto2EnumValueDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn": "_chromepolicy_4_GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut": "_chromepolicy_5_GoogleChromePolicyVersionsV1RemoveCertificateErrorDetailsOut",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn": "_chromepolicy_6_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut": "_chromepolicy_7_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateRequestIn": "_chromepolicy_8_GoogleChromePolicyVersionsV1RemoveCertificateRequestIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateRequestOut": "_chromepolicy_9_GoogleChromePolicyVersionsV1RemoveCertificateRequestOut",
        "GoogleChromePolicyVersionsV1CertificateReferenceIn": "_chromepolicy_10_GoogleChromePolicyVersionsV1CertificateReferenceIn",
        "GoogleChromePolicyVersionsV1CertificateReferenceOut": "_chromepolicy_11_GoogleChromePolicyVersionsV1CertificateReferenceOut",
        "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn": "_chromepolicy_12_GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn",
        "GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut": "_chromepolicy_13_GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut",
        "GoogleChromePolicyVersionsV1DefineNetworkResponseIn": "_chromepolicy_14_GoogleChromePolicyVersionsV1DefineNetworkResponseIn",
        "GoogleChromePolicyVersionsV1DefineNetworkResponseOut": "_chromepolicy_15_GoogleChromePolicyVersionsV1DefineNetworkResponseOut",
        "GoogleChromePolicyVersionsV1DefineNetworkRequestIn": "_chromepolicy_16_GoogleChromePolicyVersionsV1DefineNetworkRequestIn",
        "GoogleChromePolicyVersionsV1DefineNetworkRequestOut": "_chromepolicy_17_GoogleChromePolicyVersionsV1DefineNetworkRequestOut",
        "GoogleChromePolicyVersionsV1RemoveNetworkResponseIn": "_chromepolicy_18_GoogleChromePolicyVersionsV1RemoveNetworkResponseIn",
        "GoogleChromePolicyVersionsV1RemoveNetworkResponseOut": "_chromepolicy_19_GoogleChromePolicyVersionsV1RemoveNetworkResponseOut",
        "GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn": "_chromepolicy_20_GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn",
        "GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut": "_chromepolicy_21_GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut",
        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn": "_chromepolicy_22_GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut": "_chromepolicy_23_GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut",
        "GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn": "_chromepolicy_24_GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut": "_chromepolicy_25_GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1PolicyValueIn": "_chromepolicy_26_GoogleChromePolicyVersionsV1PolicyValueIn",
        "GoogleChromePolicyVersionsV1PolicyValueOut": "_chromepolicy_27_GoogleChromePolicyVersionsV1PolicyValueOut",
        "GoogleChromePolicyVersionsV1ResolveResponseIn": "_chromepolicy_28_GoogleChromePolicyVersionsV1ResolveResponseIn",
        "GoogleChromePolicyVersionsV1ResolveResponseOut": "_chromepolicy_29_GoogleChromePolicyVersionsV1ResolveResponseOut",
        "GoogleChromePolicyVersionsV1ResolvedPolicyIn": "_chromepolicy_30_GoogleChromePolicyVersionsV1ResolvedPolicyIn",
        "GoogleChromePolicyVersionsV1ResolvedPolicyOut": "_chromepolicy_31_GoogleChromePolicyVersionsV1ResolvedPolicyOut",
        "GoogleChromePolicyVersionsV1ResolveRequestIn": "_chromepolicy_32_GoogleChromePolicyVersionsV1ResolveRequestIn",
        "GoogleChromePolicyVersionsV1ResolveRequestOut": "_chromepolicy_33_GoogleChromePolicyVersionsV1ResolveRequestOut",
        "Proto2OneofDescriptorProtoIn": "_chromepolicy_34_Proto2OneofDescriptorProtoIn",
        "Proto2OneofDescriptorProtoOut": "_chromepolicy_35_Proto2OneofDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn": "_chromepolicy_36_GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn",
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut": "_chromepolicy_37_GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut",
        "GoogleChromePolicyVersionsV1NumericRangeConstraintIn": "_chromepolicy_38_GoogleChromePolicyVersionsV1NumericRangeConstraintIn",
        "GoogleChromePolicyVersionsV1NumericRangeConstraintOut": "_chromepolicy_39_GoogleChromePolicyVersionsV1NumericRangeConstraintOut",
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn": "_chromepolicy_40_GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut": "_chromepolicy_41_GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn": "_chromepolicy_42_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestIn",
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut": "_chromepolicy_43_GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequestOut",
        "Proto2DescriptorProtoIn": "_chromepolicy_44_Proto2DescriptorProtoIn",
        "Proto2DescriptorProtoOut": "_chromepolicy_45_Proto2DescriptorProtoOut",
        "GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn": "_chromepolicy_46_GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn",
        "GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut": "_chromepolicy_47_GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut",
        "GoogleProtobufEmptyIn": "_chromepolicy_48_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_chromepolicy_49_GoogleProtobufEmptyOut",
        "GoogleChromePolicyVersionsV1PolicySchemaIn": "_chromepolicy_50_GoogleChromePolicyVersionsV1PolicySchemaIn",
        "GoogleChromePolicyVersionsV1PolicySchemaOut": "_chromepolicy_51_GoogleChromePolicyVersionsV1PolicySchemaOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn": "_chromepolicy_52_GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut": "_chromepolicy_53_GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut",
        "Proto2FieldDescriptorProtoIn": "_chromepolicy_54_Proto2FieldDescriptorProtoIn",
        "Proto2FieldDescriptorProtoOut": "_chromepolicy_55_Proto2FieldDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn": "_chromepolicy_56_GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut": "_chromepolicy_57_GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut",
        "GoogleChromePolicyVersionsV1DefineCertificateResponseIn": "_chromepolicy_58_GoogleChromePolicyVersionsV1DefineCertificateResponseIn",
        "GoogleChromePolicyVersionsV1DefineCertificateResponseOut": "_chromepolicy_59_GoogleChromePolicyVersionsV1DefineCertificateResponseOut",
        "GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn": "_chromepolicy_60_GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn",
        "GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut": "_chromepolicy_61_GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut",
        "GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn": "_chromepolicy_62_GoogleChromePolicyVersionsV1AdditionalTargetKeyNameIn",
        "GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut": "_chromepolicy_63_GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut",
        "GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn": "_chromepolicy_64_GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut": "_chromepolicy_65_GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1RemoveCertificateResponseIn": "_chromepolicy_66_GoogleChromePolicyVersionsV1RemoveCertificateResponseIn",
        "GoogleChromePolicyVersionsV1RemoveCertificateResponseOut": "_chromepolicy_67_GoogleChromePolicyVersionsV1RemoveCertificateResponseOut",
        "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn": "_chromepolicy_68_GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn",
        "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut": "_chromepolicy_69_GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestOut",
        "GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn": "_chromepolicy_70_GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestIn",
        "GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut": "_chromepolicy_71_GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequestOut",
        "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn": "_chromepolicy_72_GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn",
        "GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut": "_chromepolicy_73_GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut",
        "GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn": "_chromepolicy_74_GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsIn",
        "GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut": "_chromepolicy_75_GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut",
        "ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn": "_chromepolicy_76_ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn",
        "ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut": "_chromepolicy_77_ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut",
        "GoogleChromePolicyVersionsV1PolicyTargetKeyIn": "_chromepolicy_78_GoogleChromePolicyVersionsV1PolicyTargetKeyIn",
        "GoogleChromePolicyVersionsV1PolicyTargetKeyOut": "_chromepolicy_79_GoogleChromePolicyVersionsV1PolicyTargetKeyOut",
        "GoogleChromePolicyVersionsV1NetworkSettingIn": "_chromepolicy_80_GoogleChromePolicyVersionsV1NetworkSettingIn",
        "GoogleChromePolicyVersionsV1NetworkSettingOut": "_chromepolicy_81_GoogleChromePolicyVersionsV1NetworkSettingOut",
        "GoogleTypeDateIn": "_chromepolicy_82_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_chromepolicy_83_GoogleTypeDateOut",
        "GoogleChromePolicyVersionsV1RemoveNetworkRequestIn": "_chromepolicy_84_GoogleChromePolicyVersionsV1RemoveNetworkRequestIn",
        "GoogleChromePolicyVersionsV1RemoveNetworkRequestOut": "_chromepolicy_85_GoogleChromePolicyVersionsV1RemoveNetworkRequestOut",
        "Proto2EnumDescriptorProtoIn": "_chromepolicy_86_Proto2EnumDescriptorProtoIn",
        "Proto2EnumDescriptorProtoOut": "_chromepolicy_87_Proto2EnumDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn": "_chromepolicy_88_GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn",
        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut": "_chromepolicy_89_GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorIn": "_chromepolicy_90_GoogleChromePolicyVersionsV1PolicyModificationErrorIn",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorOut": "_chromepolicy_91_GoogleChromePolicyVersionsV1PolicyModificationErrorOut",
        "GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn": "_chromepolicy_92_GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn",
        "GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut": "_chromepolicy_93_GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut",
        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn": "_chromepolicy_94_GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn",
        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut": "_chromepolicy_95_GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut",
        "GoogleChromePolicyVersionsV1FieldConstraintsIn": "_chromepolicy_96_GoogleChromePolicyVersionsV1FieldConstraintsIn",
        "GoogleChromePolicyVersionsV1FieldConstraintsOut": "_chromepolicy_97_GoogleChromePolicyVersionsV1FieldConstraintsOut",
        "Proto2FileDescriptorProtoIn": "_chromepolicy_98_Proto2FileDescriptorProtoIn",
        "Proto2FileDescriptorProtoOut": "_chromepolicy_99_Proto2FileDescriptorProtoOut",
        "GoogleChromePolicyVersionsV1DefineCertificateRequestIn": "_chromepolicy_100_GoogleChromePolicyVersionsV1DefineCertificateRequestIn",
        "GoogleChromePolicyVersionsV1DefineCertificateRequestOut": "_chromepolicy_101_GoogleChromePolicyVersionsV1DefineCertificateRequestOut",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn": "_chromepolicy_102_GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsIn",
        "GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut": "_chromepolicy_103_GoogleChromePolicyVersionsV1PolicyModificationErrorDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseIn"])
    types[
        "GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut"
    ] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyNamespace": t.string().optional(),
            "groupIds": t.array(t.string()).optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponseOut"]
    )
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
    types["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DeleteGroupPolicyRequestOut"])
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
    types["GoogleChromePolicyVersionsV1RemoveNetworkResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkResponseIn"])
    types["GoogleChromePolicyVersionsV1RemoveNetworkResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveNetworkResponseOut"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn"] = t.struct(
        {"downloadUri": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileResponseIn"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut"] = t.struct(
        {
            "downloadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileResponseOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"] = t.struct(
        {
            "noticeValue": t.string().optional(),
            "field": t.string().optional(),
            "acknowledgementRequired": t.boolean().optional(),
            "noticeMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"])
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
    types["GoogleChromePolicyVersionsV1ResolvedPolicyIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1ResolvedPolicyIn"])
    types["GoogleChromePolicyVersionsV1ResolvedPolicyOut"] = t.struct(
        {
            "targetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "value": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueOut"]
            ).optional(),
            "sourceKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "addedSourceKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolvedPolicyOut"])
    types["GoogleChromePolicyVersionsV1ResolveRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "policySchemaFilter": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveRequestIn"])
    types["GoogleChromePolicyVersionsV1ResolveRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "policySchemaFilter": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ResolveRequestOut"])
    types["Proto2OneofDescriptorProtoIn"] = t.struct({"name": t.string()}).named(
        renames["Proto2OneofDescriptorProtoIn"]
    )
    types["Proto2OneofDescriptorProtoOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["Proto2OneofDescriptorProtoOut"])
    types[
        "GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestIn"
    ] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
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
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "policyNamespace": t.string().optional(),
            "groupIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequestOut"]
    )
    types["GoogleChromePolicyVersionsV1NumericRangeConstraintIn"] = t.struct(
        {"minimum": t.string().optional(), "maximum": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1NumericRangeConstraintIn"])
    types["GoogleChromePolicyVersionsV1NumericRangeConstraintOut"] = t.struct(
        {
            "minimum": t.string().optional(),
            "maximum": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1NumericRangeConstraintOut"])
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
    types["Proto2DescriptorProtoIn"] = t.struct(
        {
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoIn"])),
            "oneofDecl": t.array(t.proxy(renames["Proto2OneofDescriptorProtoIn"])),
            "name": t.string(),
            "field": t.array(t.proxy(renames["Proto2FieldDescriptorProtoIn"])),
            "nestedType": t.array(t.proxy(renames["Proto2DescriptorProtoIn"])),
        }
    ).named(renames["Proto2DescriptorProtoIn"])
    types["Proto2DescriptorProtoOut"] = t.struct(
        {
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoOut"])),
            "oneofDecl": t.array(t.proxy(renames["Proto2OneofDescriptorProtoOut"])),
            "name": t.string(),
            "field": t.array(t.proxy(renames["Proto2FieldDescriptorProtoOut"])),
            "nestedType": t.array(t.proxy(renames["Proto2DescriptorProtoOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2DescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policySchemas": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1PolicySchemaIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseIn"])
    types["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policySchemas": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1PolicySchemaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaIn"] = t.struct(
        {
            "name": t.string().optional(),
            "definition": t.proxy(renames["Proto2FileDescriptorProtoIn"]).optional(),
            "categoryTitle": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaOut"] = t.struct(
        {
            "additionalTargetKeyNames": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1AdditionalTargetKeyNameOut"]
                )
            ).optional(),
            "fieldDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"
                    ]
                )
            ).optional(),
            "name": t.string().optional(),
            "supportUri": t.string().optional(),
            "policyDescription": t.string().optional(),
            "schemaName": t.string().optional(),
            "validTargetResources": t.array(t.string()).optional(),
            "policyApiLifecycle": t.proxy(
                renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"]
            ).optional(),
            "accessRestrictions": t.array(t.string()).optional(),
            "definition": t.proxy(renames["Proto2FileDescriptorProtoOut"]).optional(),
            "notices": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaNoticeDescriptionOut"
                    ]
                )
            ).optional(),
            "categoryTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaOut"])
    types[
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionIn"]
    )
    types[
        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"
    ] = t.struct(
        {
            "value": t.string().optional(),
            "fieldDependencies": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"
                    ]
                )
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"]
    )
    types["Proto2FieldDescriptorProtoIn"] = t.struct(
        {
            "name": t.string(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string(),
            "typeName": t.string().optional(),
            "jsonName": t.string().optional(),
            "proto3Optional": t.boolean().optional(),
            "number": t.integer(),
        }
    ).named(renames["Proto2FieldDescriptorProtoIn"])
    types["Proto2FieldDescriptorProtoOut"] = t.struct(
        {
            "name": t.string(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string(),
            "typeName": t.string().optional(),
            "jsonName": t.string().optional(),
            "proto3Optional": t.boolean().optional(),
            "number": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2FieldDescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn"] = t.struct(
        {"description": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"] = t.struct(
        {
            "nestedFieldDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"
                    ]
                )
            ).optional(),
            "fieldConstraints": t.proxy(
                renames["GoogleChromePolicyVersionsV1FieldConstraintsOut"]
            ).optional(),
            "requiredItems": t.array(
                t.proxy(
                    renames["GoogleChromePolicyVersionsV1PolicySchemaRequiredItemsOut"]
                )
            ).optional(),
            "fieldDescription": t.string().optional(),
            "knownValueDescriptions": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescriptionOut"
                    ]
                )
            ).optional(),
            "inputConstraint": t.string().optional(),
            "field": t.string().optional(),
            "name": t.string().optional(),
            "fieldDependencies": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"
                    ]
                )
            ).optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDescriptionOut"])
    types["GoogleChromePolicyVersionsV1DefineCertificateResponseIn"] = t.struct(
        {
            "targetResource": t.string().optional(),
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseIn"])
    types["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"] = t.struct(
        {
            "targetResource": t.string().optional(),
            "networkId": t.string().optional(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"])
    types["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn"] = t.struct(
        {
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueIn"]
            ).optional(),
            "updateMask": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut"] = t.struct(
        {
            "policyValue": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyValueOut"]
            ).optional(),
            "updateMask": t.string(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequestOut"])
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
    types["GoogleChromePolicyVersionsV1RemoveCertificateResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseIn"])
    types["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromePolicyVersionsV1RemoveCertificateResponseOut"])
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
    types["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
            ),
        }
    ).named(renames["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestIn"])
    types["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut"] = t.struct(
        {
            "policySchema": t.string().optional(),
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequestOut"])
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
    types["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn"] = t.struct(
        {
            "description": t.string().optional(),
            "deprecatedInFavorOf": t.array(t.string()).optional(),
            "endSupport": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "policyApiLifecycleStage": t.string().optional(),
        }
    ).named(renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleIn"])
    types["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"] = t.struct(
        {
            "description": t.string().optional(),
            "deprecatedInFavorOf": t.array(t.string()).optional(),
            "endSupport": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "policyApiLifecycleStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycleOut"])
    types["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"] = t.struct(
        {
            "targetResource": t.string().optional(),
            "additionalTargetKeys": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"])
    types["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"] = t.struct(
        {
            "targetResource": t.string().optional(),
            "additionalTargetKeys": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"])
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
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn"] = t.struct(
        {
            "sourceFieldValue": t.string().optional(),
            "sourceField": t.string().optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesIn"])
    types["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"] = t.struct(
        {
            "sourceFieldValue": t.string().optional(),
            "sourceField": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicySchemaFieldDependenciesOut"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorIn"])
    types["GoogleChromePolicyVersionsV1PolicyModificationErrorOut"] = t.struct(
        {
            "policyTargetKey": t.proxy(
                renames["GoogleChromePolicyVersionsV1PolicyTargetKeyOut"]
            ).optional(),
            "fieldErrors": t.array(
                t.proxy(
                    renames[
                        "GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"
                    ]
                )
            ).optional(),
            "errors": t.array(t.string()).optional(),
            "policySchema": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationErrorOut"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn"] = t.struct(
        {"policyField": t.string()}
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileRequestIn"])
    types["GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut"] = t.struct(
        {
            "policyField": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1UploadPolicyFileRequestOut"])
    types["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorIn"])
    types["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"] = t.struct(
        {
            "field": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1PolicyModificationFieldErrorOut"])
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
    types["Proto2FileDescriptorProtoIn"] = t.struct(
        {
            "package": t.string().optional(),
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoIn"])),
            "name": t.string().optional(),
            "messageType": t.array(
                t.proxy(renames["Proto2DescriptorProtoIn"])
            ).optional(),
            "syntax": t.string().optional(),
        }
    ).named(renames["Proto2FileDescriptorProtoIn"])
    types["Proto2FileDescriptorProtoOut"] = t.struct(
        {
            "package": t.string().optional(),
            "enumType": t.array(t.proxy(renames["Proto2EnumDescriptorProtoOut"])),
            "name": t.string().optional(),
            "messageType": t.array(
                t.proxy(renames["Proto2DescriptorProtoOut"])
            ).optional(),
            "syntax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Proto2FileDescriptorProtoOut"])
    types["GoogleChromePolicyVersionsV1DefineCertificateRequestIn"] = t.struct(
        {
            "certificate": t.string(),
            "ceritificateName": t.string().optional(),
            "targetResource": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateRequestIn"])
    types["GoogleChromePolicyVersionsV1DefineCertificateRequestOut"] = t.struct(
        {
            "certificate": t.string(),
            "ceritificateName": t.string().optional(),
            "targetResource": t.string(),
            "settings": t.array(
                t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromePolicyVersionsV1DefineCertificateRequestOut"])
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

    functions = {}
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
    functions["customersPolicySchemasGet"] = chromepolicy.get(
        "v1/{parent}/policySchemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1ListPolicySchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesResolve"] = chromepolicy.post(
        "v1/{customer}/policies:resolve",
        t.struct(
            {
                "customer": t.string().optional(),
                "pageToken": t.string().optional(),
                "policySchemaFilter": t.string(),
                "policyTargetKey": t.proxy(
                    renames["GoogleChromePolicyVersionsV1PolicyTargetKeyIn"]
                ),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1ResolveResponseOut"]),
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
    functions["customersPoliciesGroupsBatchDelete"] = chromepolicy.post(
        "v1/{customer}/policies/groups:batchModify",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"
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
        "v1/{customer}/policies/groups:batchModify",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"
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
        "v1/{customer}/policies/groups:batchModify",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"
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
        "v1/{customer}/policies/groups:batchModify",
        t.struct(
            {
                "customer": t.string().optional(),
                "requests": t.array(
                    t.proxy(
                        renames[
                            "GoogleChromePolicyVersionsV1ModifyGroupPolicyRequestIn"
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
    functions["customersPoliciesNetworksRemoveCertificate"] = chromepolicy.post(
        "v1/{customer}/policies/networks:defineCertificate",
        t.struct(
            {
                "customer": t.string(),
                "certificate": t.string(),
                "ceritificateName": t.string().optional(),
                "targetResource": t.string(),
                "settings": t.array(
                    t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksRemoveNetwork"] = chromepolicy.post(
        "v1/{customer}/policies/networks:defineCertificate",
        t.struct(
            {
                "customer": t.string(),
                "certificate": t.string(),
                "ceritificateName": t.string().optional(),
                "targetResource": t.string(),
                "settings": t.array(
                    t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksDefineNetwork"] = chromepolicy.post(
        "v1/{customer}/policies/networks:defineCertificate",
        t.struct(
            {
                "customer": t.string(),
                "certificate": t.string(),
                "ceritificateName": t.string().optional(),
                "targetResource": t.string(),
                "settings": t.array(
                    t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPoliciesNetworksDefineCertificate"] = chromepolicy.post(
        "v1/{customer}/policies/networks:defineCertificate",
        t.struct(
            {
                "customer": t.string(),
                "certificate": t.string(),
                "ceritificateName": t.string().optional(),
                "targetResource": t.string(),
                "settings": t.array(
                    t.proxy(renames["GoogleChromePolicyVersionsV1NetworkSettingIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromePolicyVersionsV1DefineCertificateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chromepolicy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
