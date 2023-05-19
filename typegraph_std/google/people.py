from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_people() -> Import:
    people = HTTPRuntime("https://people.googleapis.com/")

    renames = {
        "ErrorResponse": "_people_1_ErrorResponse",
        "DomainMembershipIn": "_people_2_DomainMembershipIn",
        "DomainMembershipOut": "_people_3_DomainMembershipOut",
        "SipAddressIn": "_people_4_SipAddressIn",
        "SipAddressOut": "_people_5_SipAddressOut",
        "BatchUpdateContactsResponseIn": "_people_6_BatchUpdateContactsResponseIn",
        "BatchUpdateContactsResponseOut": "_people_7_BatchUpdateContactsResponseOut",
        "RelationshipInterestIn": "_people_8_RelationshipInterestIn",
        "RelationshipInterestOut": "_people_9_RelationshipInterestOut",
        "SearchDirectoryPeopleResponseIn": "_people_10_SearchDirectoryPeopleResponseIn",
        "SearchDirectoryPeopleResponseOut": "_people_11_SearchDirectoryPeopleResponseOut",
        "FileAsIn": "_people_12_FileAsIn",
        "FileAsOut": "_people_13_FileAsOut",
        "BirthdayIn": "_people_14_BirthdayIn",
        "BirthdayOut": "_people_15_BirthdayOut",
        "ContactGroupResponseIn": "_people_16_ContactGroupResponseIn",
        "ContactGroupResponseOut": "_people_17_ContactGroupResponseOut",
        "ModifyContactGroupMembersResponseIn": "_people_18_ModifyContactGroupMembersResponseIn",
        "ModifyContactGroupMembersResponseOut": "_people_19_ModifyContactGroupMembersResponseOut",
        "GroupClientDataIn": "_people_20_GroupClientDataIn",
        "GroupClientDataOut": "_people_21_GroupClientDataOut",
        "UpdateContactPhotoRequestIn": "_people_22_UpdateContactPhotoRequestIn",
        "UpdateContactPhotoRequestOut": "_people_23_UpdateContactPhotoRequestOut",
        "UpdateContactPhotoResponseIn": "_people_24_UpdateContactPhotoResponseIn",
        "UpdateContactPhotoResponseOut": "_people_25_UpdateContactPhotoResponseOut",
        "MembershipIn": "_people_26_MembershipIn",
        "MembershipOut": "_people_27_MembershipOut",
        "ExternalIdIn": "_people_28_ExternalIdIn",
        "ExternalIdOut": "_people_29_ExternalIdOut",
        "RelationIn": "_people_30_RelationIn",
        "RelationOut": "_people_31_RelationOut",
        "PhoneNumberIn": "_people_32_PhoneNumberIn",
        "PhoneNumberOut": "_people_33_PhoneNumberOut",
        "ListOtherContactsResponseIn": "_people_34_ListOtherContactsResponseIn",
        "ListOtherContactsResponseOut": "_people_35_ListOtherContactsResponseOut",
        "MiscKeywordIn": "_people_36_MiscKeywordIn",
        "MiscKeywordOut": "_people_37_MiscKeywordOut",
        "StatusIn": "_people_38_StatusIn",
        "StatusOut": "_people_39_StatusOut",
        "ContactToCreateIn": "_people_40_ContactToCreateIn",
        "ContactToCreateOut": "_people_41_ContactToCreateOut",
        "ContactGroupMetadataIn": "_people_42_ContactGroupMetadataIn",
        "ContactGroupMetadataOut": "_people_43_ContactGroupMetadataOut",
        "OccupationIn": "_people_44_OccupationIn",
        "OccupationOut": "_people_45_OccupationOut",
        "BatchCreateContactsResponseIn": "_people_46_BatchCreateContactsResponseIn",
        "BatchCreateContactsResponseOut": "_people_47_BatchCreateContactsResponseOut",
        "SourceIn": "_people_48_SourceIn",
        "SourceOut": "_people_49_SourceOut",
        "BatchGetContactGroupsResponseIn": "_people_50_BatchGetContactGroupsResponseIn",
        "BatchGetContactGroupsResponseOut": "_people_51_BatchGetContactGroupsResponseOut",
        "ClientDataIn": "_people_52_ClientDataIn",
        "ClientDataOut": "_people_53_ClientDataOut",
        "InterestIn": "_people_54_InterestIn",
        "InterestOut": "_people_55_InterestOut",
        "SkillIn": "_people_56_SkillIn",
        "SkillOut": "_people_57_SkillOut",
        "DeleteContactPhotoResponseIn": "_people_58_DeleteContactPhotoResponseIn",
        "DeleteContactPhotoResponseOut": "_people_59_DeleteContactPhotoResponseOut",
        "ResidenceIn": "_people_60_ResidenceIn",
        "ResidenceOut": "_people_61_ResidenceOut",
        "LocaleIn": "_people_62_LocaleIn",
        "LocaleOut": "_people_63_LocaleOut",
        "CalendarUrlIn": "_people_64_CalendarUrlIn",
        "CalendarUrlOut": "_people_65_CalendarUrlOut",
        "PhotoIn": "_people_66_PhotoIn",
        "PhotoOut": "_people_67_PhotoOut",
        "BiographyIn": "_people_68_BiographyIn",
        "BiographyOut": "_people_69_BiographyOut",
        "ContactGroupIn": "_people_70_ContactGroupIn",
        "ContactGroupOut": "_people_71_ContactGroupOut",
        "UrlIn": "_people_72_UrlIn",
        "UrlOut": "_people_73_UrlOut",
        "SearchResponseIn": "_people_74_SearchResponseIn",
        "SearchResponseOut": "_people_75_SearchResponseOut",
        "NameIn": "_people_76_NameIn",
        "NameOut": "_people_77_NameOut",
        "AgeRangeTypeIn": "_people_78_AgeRangeTypeIn",
        "AgeRangeTypeOut": "_people_79_AgeRangeTypeOut",
        "ProfileMetadataIn": "_people_80_ProfileMetadataIn",
        "ProfileMetadataOut": "_people_81_ProfileMetadataOut",
        "PersonMetadataIn": "_people_82_PersonMetadataIn",
        "PersonMetadataOut": "_people_83_PersonMetadataOut",
        "ContactGroupMembershipIn": "_people_84_ContactGroupMembershipIn",
        "ContactGroupMembershipOut": "_people_85_ContactGroupMembershipOut",
        "LocationIn": "_people_86_LocationIn",
        "LocationOut": "_people_87_LocationOut",
        "BatchUpdateContactsRequestIn": "_people_88_BatchUpdateContactsRequestIn",
        "BatchUpdateContactsRequestOut": "_people_89_BatchUpdateContactsRequestOut",
        "GenderIn": "_people_90_GenderIn",
        "GenderOut": "_people_91_GenderOut",
        "FieldMetadataIn": "_people_92_FieldMetadataIn",
        "FieldMetadataOut": "_people_93_FieldMetadataOut",
        "EventIn": "_people_94_EventIn",
        "EventOut": "_people_95_EventOut",
        "NicknameIn": "_people_96_NicknameIn",
        "NicknameOut": "_people_97_NicknameOut",
        "PersonIn": "_people_98_PersonIn",
        "PersonOut": "_people_99_PersonOut",
        "BraggingRightsIn": "_people_100_BraggingRightsIn",
        "BraggingRightsOut": "_people_101_BraggingRightsOut",
        "BatchDeleteContactsRequestIn": "_people_102_BatchDeleteContactsRequestIn",
        "BatchDeleteContactsRequestOut": "_people_103_BatchDeleteContactsRequestOut",
        "EmailAddressIn": "_people_104_EmailAddressIn",
        "EmailAddressOut": "_people_105_EmailAddressOut",
        "ListContactGroupsResponseIn": "_people_106_ListContactGroupsResponseIn",
        "ListContactGroupsResponseOut": "_people_107_ListContactGroupsResponseOut",
        "CoverPhotoIn": "_people_108_CoverPhotoIn",
        "CoverPhotoOut": "_people_109_CoverPhotoOut",
        "EmptyIn": "_people_110_EmptyIn",
        "EmptyOut": "_people_111_EmptyOut",
        "ModifyContactGroupMembersRequestIn": "_people_112_ModifyContactGroupMembersRequestIn",
        "ModifyContactGroupMembersRequestOut": "_people_113_ModifyContactGroupMembersRequestOut",
        "GetPeopleResponseIn": "_people_114_GetPeopleResponseIn",
        "GetPeopleResponseOut": "_people_115_GetPeopleResponseOut",
        "AddressIn": "_people_116_AddressIn",
        "AddressOut": "_people_117_AddressOut",
        "CopyOtherContactToMyContactsGroupRequestIn": "_people_118_CopyOtherContactToMyContactsGroupRequestIn",
        "CopyOtherContactToMyContactsGroupRequestOut": "_people_119_CopyOtherContactToMyContactsGroupRequestOut",
        "DateIn": "_people_120_DateIn",
        "DateOut": "_people_121_DateOut",
        "OrganizationIn": "_people_122_OrganizationIn",
        "OrganizationOut": "_people_123_OrganizationOut",
        "BatchCreateContactsRequestIn": "_people_124_BatchCreateContactsRequestIn",
        "BatchCreateContactsRequestOut": "_people_125_BatchCreateContactsRequestOut",
        "UpdateContactGroupRequestIn": "_people_126_UpdateContactGroupRequestIn",
        "UpdateContactGroupRequestOut": "_people_127_UpdateContactGroupRequestOut",
        "ListConnectionsResponseIn": "_people_128_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_people_129_ListConnectionsResponseOut",
        "TaglineIn": "_people_130_TaglineIn",
        "TaglineOut": "_people_131_TaglineOut",
        "ListDirectoryPeopleResponseIn": "_people_132_ListDirectoryPeopleResponseIn",
        "ListDirectoryPeopleResponseOut": "_people_133_ListDirectoryPeopleResponseOut",
        "ImClientIn": "_people_134_ImClientIn",
        "ImClientOut": "_people_135_ImClientOut",
        "UserDefinedIn": "_people_136_UserDefinedIn",
        "UserDefinedOut": "_people_137_UserDefinedOut",
        "PersonResponseIn": "_people_138_PersonResponseIn",
        "PersonResponseOut": "_people_139_PersonResponseOut",
        "SearchResultIn": "_people_140_SearchResultIn",
        "SearchResultOut": "_people_141_SearchResultOut",
        "CreateContactGroupRequestIn": "_people_142_CreateContactGroupRequestIn",
        "CreateContactGroupRequestOut": "_people_143_CreateContactGroupRequestOut",
        "RelationshipStatusIn": "_people_144_RelationshipStatusIn",
        "RelationshipStatusOut": "_people_145_RelationshipStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DomainMembershipIn"] = t.struct(
        {"inViewerDomain": t.boolean().optional()}
    ).named(renames["DomainMembershipIn"])
    types["DomainMembershipOut"] = t.struct(
        {
            "inViewerDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMembershipOut"])
    types["SipAddressIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SipAddressIn"])
    types["SipAddressOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SipAddressOut"])
    types["BatchUpdateContactsResponseIn"] = t.struct(
        {"updateResult": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BatchUpdateContactsResponseIn"])
    types["BatchUpdateContactsResponseOut"] = t.struct(
        {
            "updateResult": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsResponseOut"])
    types["RelationshipInterestIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["RelationshipInterestIn"])
    types["RelationshipInterestOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipInterestOut"])
    types["SearchDirectoryPeopleResponseIn"] = t.struct(
        {
            "people": t.array(t.proxy(renames["PersonIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseIn"])
    types["SearchDirectoryPeopleResponseOut"] = t.struct(
        {
            "people": t.array(t.proxy(renames["PersonOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseOut"])
    types["FileAsIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["FileAsIn"])
    types["FileAsOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileAsOut"])
    types["BirthdayIn"] = t.struct(
        {
            "text": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["BirthdayIn"])
    types["BirthdayOut"] = t.struct(
        {
            "text": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BirthdayOut"])
    types["ContactGroupResponseIn"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "requestedResourceName": t.string().optional(),
        }
    ).named(renames["ContactGroupResponseIn"])
    types["ContactGroupResponseOut"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupResponseOut"])
    types["ModifyContactGroupMembersResponseIn"] = t.struct(
        {
            "canNotRemoveLastContactGroupResourceNames": t.array(t.string()).optional(),
            "notFoundResourceNames": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyContactGroupMembersResponseIn"])
    types["ModifyContactGroupMembersResponseOut"] = t.struct(
        {
            "canNotRemoveLastContactGroupResourceNames": t.array(t.string()).optional(),
            "notFoundResourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyContactGroupMembersResponseOut"])
    types["GroupClientDataIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GroupClientDataIn"])
    types["GroupClientDataOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupClientDataOut"])
    types["UpdateContactPhotoRequestIn"] = t.struct(
        {
            "photoBytes": t.string(),
            "sources": t.array(t.string()).optional(),
            "personFields": t.string().optional(),
        }
    ).named(renames["UpdateContactPhotoRequestIn"])
    types["UpdateContactPhotoRequestOut"] = t.struct(
        {
            "photoBytes": t.string(),
            "sources": t.array(t.string()).optional(),
            "personFields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoRequestOut"])
    types["UpdateContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["UpdateContactPhotoResponseIn"])
    types["UpdateContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoResponseOut"])
    types["MembershipIn"] = t.struct(
        {
            "contactGroupMembership": t.proxy(
                renames["ContactGroupMembershipIn"]
            ).optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "contactGroupMembership": t.proxy(
                renames["ContactGroupMembershipOut"]
            ).optional(),
            "domainMembership": t.proxy(renames["DomainMembershipOut"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["ExternalIdIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ExternalIdIn"])
    types["ExternalIdOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalIdOut"])
    types["RelationIn"] = t.struct(
        {
            "person": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "person": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
    types["PhoneNumberIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PhoneNumberIn"])
    types["PhoneNumberOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "canonicalForm": t.string().optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["ListOtherContactsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "otherContacts": t.array(t.proxy(renames["PersonIn"])).optional(),
            "nextSyncToken": t.string().optional(),
        }
    ).named(renames["ListOtherContactsResponseIn"])
    types["ListOtherContactsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "otherContacts": t.array(t.proxy(renames["PersonOut"])).optional(),
            "nextSyncToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOtherContactsResponseOut"])
    types["MiscKeywordIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MiscKeywordIn"])
    types["MiscKeywordOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "formattedType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MiscKeywordOut"])
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
    types["ContactToCreateIn"] = t.struct(
        {"contactPerson": t.proxy(renames["PersonIn"])}
    ).named(renames["ContactToCreateIn"])
    types["ContactToCreateOut"] = t.struct(
        {
            "contactPerson": t.proxy(renames["PersonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactToCreateOut"])
    types["ContactGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ContactGroupMetadataIn"]
    )
    types["ContactGroupMetadataOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupMetadataOut"])
    types["OccupationIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["OccupationIn"])
    types["OccupationOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccupationOut"])
    types["BatchCreateContactsResponseIn"] = t.struct(
        {"createdPeople": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["BatchCreateContactsResponseIn"])
    types["BatchCreateContactsResponseOut"] = t.struct(
        {
            "createdPeople": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsResponseOut"])
    types["SourceIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "profileMetadata": t.proxy(renames["ProfileMetadataOut"]).optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["BatchGetContactGroupsResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["ContactGroupResponseIn"])).optional()}
    ).named(renames["BatchGetContactGroupsResponseIn"])
    types["BatchGetContactGroupsResponseOut"] = t.struct(
        {
            "responses": t.array(
                t.proxy(renames["ContactGroupResponseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetContactGroupsResponseOut"])
    types["ClientDataIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ClientDataIn"])
    types["ClientDataOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientDataOut"])
    types["InterestIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["InterestIn"])
    types["InterestOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterestOut"])
    types["SkillIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["SkillIn"])
    types["SkillOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkillOut"])
    types["DeleteContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["DeleteContactPhotoResponseIn"])
    types["DeleteContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContactPhotoResponseOut"])
    types["ResidenceIn"] = t.struct(
        {
            "value": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["ResidenceIn"])
    types["ResidenceOut"] = t.struct(
        {
            "value": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResidenceOut"])
    types["LocaleIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["LocaleIn"])
    types["LocaleOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocaleOut"])
    types["CalendarUrlIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["CalendarUrlIn"])
    types["CalendarUrlOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "url": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarUrlOut"])
    types["PhotoIn"] = t.struct(
        {
            "url": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "default": t.boolean().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "default": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["BiographyIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["BiographyIn"])
    types["BiographyOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiographyOut"])
    types["ContactGroupIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "resourceName": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ContactGroupIn"])
    types["ContactGroupOut"] = t.struct(
        {
            "memberCount": t.integer().optional(),
            "metadata": t.proxy(renames["ContactGroupMetadataOut"]).optional(),
            "etag": t.string().optional(),
            "resourceName": t.string().optional(),
            "memberResourceNames": t.array(t.string()).optional(),
            "formattedName": t.string().optional(),
            "groupType": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupOut"])
    types["UrlIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["UrlIn"])
    types["UrlOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlOut"])
    types["SearchResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["SearchResultIn"])).optional()}
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["NameIn"] = t.struct(
        {
            "middleName": t.string().optional(),
            "honorificPrefix": t.string().optional(),
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "givenName": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "unstructuredName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "familyName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "middleName": t.string().optional(),
            "honorificPrefix": t.string().optional(),
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "givenName": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "unstructuredName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "displayName": t.string().optional(),
            "familyName": t.string().optional(),
            "displayNameLastFirst": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["AgeRangeTypeIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "ageRange": t.string().optional(),
        }
    ).named(renames["AgeRangeTypeIn"])
    types["AgeRangeTypeOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "ageRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTypeOut"])
    types["ProfileMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProfileMetadataIn"]
    )
    types["ProfileMetadataOut"] = t.struct(
        {
            "objectType": t.string().optional(),
            "userTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileMetadataOut"])
    types["PersonMetadataIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["SourceIn"])).optional()}
    ).named(renames["PersonMetadataIn"])
    types["PersonMetadataOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "objectType": t.string().optional(),
            "linkedPeopleResourceNames": t.array(t.string()).optional(),
            "previousResourceNames": t.array(t.string()).optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonMetadataOut"])
    types["ContactGroupMembershipIn"] = t.struct(
        {"contactGroupResourceName": t.string().optional()}
    ).named(renames["ContactGroupMembershipIn"])
    types["ContactGroupMembershipOut"] = t.struct(
        {
            "contactGroupId": t.string().optional(),
            "contactGroupResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupMembershipOut"])
    types["LocationIn"] = t.struct(
        {
            "current": t.boolean().optional(),
            "buildingId": t.string().optional(),
            "floorSection": t.string().optional(),
            "floor": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "deskCode": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "current": t.boolean().optional(),
            "buildingId": t.string().optional(),
            "floorSection": t.string().optional(),
            "floor": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "deskCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BatchUpdateContactsRequestIn"] = t.struct(
        {
            "readMask": t.string(),
            "updateMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "contacts": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["BatchUpdateContactsRequestIn"])
    types["BatchUpdateContactsRequestOut"] = t.struct(
        {
            "readMask": t.string(),
            "updateMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "contacts": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsRequestOut"])
    types["GenderIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "addressMeAs": t.string().optional(),
        }
    ).named(renames["GenderIn"])
    types["GenderOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "addressMeAs": t.string().optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderOut"])
    types["FieldMetadataIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "sourcePrimary": t.boolean().optional(),
        }
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "verified": t.boolean().optional(),
            "primary": t.boolean().optional(),
            "sourcePrimary": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["EventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["NicknameIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["NicknameIn"])
    types["NicknameOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NicknameOut"])
    types["PersonIn"] = t.struct(
        {
            "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "etag": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
            "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
            "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsIn"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
            "resourceName": t.string().optional(),
            "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
            "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
            "names": t.array(t.proxy(renames["NameIn"])).optional(),
            "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "sipAddresses": t.array(t.proxy(renames["SipAddressOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "etag": t.string().optional(),
            "metadata": t.proxy(renames["PersonMetadataOut"]).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientOut"])).optional(),
            "ageRanges": t.array(t.proxy(renames["AgeRangeTypeOut"])).optional(),
            "coverPhotos": t.array(t.proxy(renames["CoverPhotoOut"])).optional(),
            "urls": t.array(t.proxy(renames["UrlOut"])).optional(),
            "relationshipInterests": t.array(
                t.proxy(renames["RelationshipInterestOut"])
            ).optional(),
            "addresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "genders": t.array(t.proxy(renames["GenderOut"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayOut"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsOut"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedOut"])).optional(),
            "interests": t.array(t.proxy(renames["InterestOut"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdOut"])).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationOut"])).optional(),
            "ageRange": t.string().optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlOut"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataOut"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsOut"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordOut"])).optional(),
            "taglines": t.array(t.proxy(renames["TaglineOut"])).optional(),
            "relationshipStatuses": t.array(
                t.proxy(renames["RelationshipStatusOut"])
            ).optional(),
            "residences": t.array(t.proxy(renames["ResidenceOut"])).optional(),
            "resourceName": t.string().optional(),
            "nicknames": t.array(t.proxy(renames["NicknameOut"])).optional(),
            "skills": t.array(t.proxy(renames["SkillOut"])).optional(),
            "names": t.array(t.proxy(renames["NameOut"])).optional(),
            "relations": t.array(t.proxy(renames["RelationOut"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyOut"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["BraggingRightsIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["BraggingRightsIn"])
    types["BraggingRightsOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BraggingRightsOut"])
    types["BatchDeleteContactsRequestIn"] = t.struct(
        {"resourceNames": t.array(t.string())}
    ).named(renames["BatchDeleteContactsRequestIn"])
    types["BatchDeleteContactsRequestOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteContactsRequestOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
    types["ListContactGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "contactGroups": t.array(t.proxy(renames["ContactGroupIn"])).optional(),
        }
    ).named(renames["ListContactGroupsResponseIn"])
    types["ListContactGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "contactGroups": t.array(t.proxy(renames["ContactGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactGroupsResponseOut"])
    types["CoverPhotoIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "default": t.boolean().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["CoverPhotoIn"])
    types["CoverPhotoOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "default": t.boolean().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CoverPhotoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ModifyContactGroupMembersRequestIn"] = t.struct(
        {
            "resourceNamesToRemove": t.array(t.string()).optional(),
            "resourceNamesToAdd": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyContactGroupMembersRequestIn"])
    types["ModifyContactGroupMembersRequestOut"] = t.struct(
        {
            "resourceNamesToRemove": t.array(t.string()).optional(),
            "resourceNamesToAdd": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyContactGroupMembersRequestOut"])
    types["GetPeopleResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["GetPeopleResponseIn"])
    types["GetPeopleResponseOut"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPeopleResponseOut"])
    types["AddressIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "streetAddress": t.string().optional(),
            "region": t.string().optional(),
            "countryCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "country": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "formattedValue": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "streetAddress": t.string().optional(),
            "region": t.string().optional(),
            "countryCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "formattedType": t.string().optional(),
            "country": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["CopyOtherContactToMyContactsGroupRequestIn"] = t.struct(
        {
            "readMask": t.string().optional(),
            "sources": t.array(t.string()).optional(),
            "copyMask": t.string(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestIn"])
    types["CopyOtherContactToMyContactsGroupRequestOut"] = t.struct(
        {
            "readMask": t.string().optional(),
            "sources": t.array(t.string()).optional(),
            "copyMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["OrganizationIn"] = t.struct(
        {
            "symbol": t.string().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "department": t.string().optional(),
            "costCenter": t.string().optional(),
            "jobDescription": t.string().optional(),
            "domain": t.string().optional(),
            "phoneticName": t.string().optional(),
            "title": t.string().optional(),
            "current": t.boolean().optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
        }
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "symbol": t.string().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "department": t.string().optional(),
            "costCenter": t.string().optional(),
            "jobDescription": t.string().optional(),
            "domain": t.string().optional(),
            "formattedType": t.string().optional(),
            "phoneticName": t.string().optional(),
            "title": t.string().optional(),
            "current": t.boolean().optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["BatchCreateContactsRequestIn"] = t.struct(
        {
            "contacts": t.array(t.proxy(renames["ContactToCreateIn"])),
            "readMask": t.string(),
            "sources": t.array(t.string()).optional(),
        }
    ).named(renames["BatchCreateContactsRequestIn"])
    types["BatchCreateContactsRequestOut"] = t.struct(
        {
            "contacts": t.array(t.proxy(renames["ContactToCreateOut"])),
            "readMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsRequestOut"])
    types["UpdateContactGroupRequestIn"] = t.struct(
        {
            "updateGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupIn"]),
            "readGroupFields": t.string().optional(),
        }
    ).named(renames["UpdateContactGroupRequestIn"])
    types["UpdateContactGroupRequestOut"] = t.struct(
        {
            "updateGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupOut"]),
            "readGroupFields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactGroupRequestOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonIn"])).optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonOut"])).optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
    types["TaglineIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["TaglineIn"])
    types["TaglineOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaglineOut"])
    types["ListDirectoryPeopleResponseIn"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "people": t.array(t.proxy(renames["PersonIn"])).optional(),
        }
    ).named(renames["ListDirectoryPeopleResponseIn"])
    types["ListDirectoryPeopleResponseOut"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "people": t.array(t.proxy(renames["PersonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDirectoryPeopleResponseOut"])
    types["ImClientIn"] = t.struct(
        {
            "type": t.string().optional(),
            "username": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["ImClientIn"])
    types["ImClientOut"] = t.struct(
        {
            "type": t.string().optional(),
            "username": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedProtocol": t.string().optional(),
            "formattedType": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImClientOut"])
    types["UserDefinedIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["UserDefinedIn"])
    types["UserDefinedOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedOut"])
    types["PersonResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "requestedResourceName": t.string().optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
            "httpStatusCode": t.integer().optional(),
        }
    ).named(renames["PersonResponseIn"])
    types["PersonResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "httpStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonResponseOut"])
    types["SearchResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["CreateContactGroupRequestIn"] = t.struct(
        {
            "readGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupIn"]),
        }
    ).named(renames["CreateContactGroupRequestIn"])
    types["CreateContactGroupRequestOut"] = t.struct(
        {
            "readGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateContactGroupRequestOut"])
    types["RelationshipStatusIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["RelationshipStatusIn"])
    types["RelationshipStatusOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipStatusOut"])

    functions = {}
    functions["peopleCreateContact"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchContacts"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContact"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchCreateContacts"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContact"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContactPhoto"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGet"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGetBatchGet"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchDirectoryPeople"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchDeleteContacts"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleListDirectoryPeople"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContactPhoto"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchUpdateContacts"] = people.post(
        "v1/people:batchUpdateContacts",
        t.struct(
            {
                "readMask": t.string(),
                "updateMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "contacts": t.struct({"_": t.string().optional()}),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleConnectionsList"] = people.get(
        "v1/{resourceName}/connections",
        t.struct(
            {
                "personFields": t.string(),
                "requestSyncToken": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "resourceName": t.string(),
                "syncToken": t.string().optional(),
                "requestMask.includeField": t.string(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsGet"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsUpdate"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsList"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsBatchGet"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsCreate"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsDelete"] = people.delete(
        "v1/{resourceName}",
        t.struct(
            {
                "resourceName": t.string(),
                "deleteContacts": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsMembersModify"] = people.post(
        "v1/{resourceName}/members:modify",
        t.struct(
            {
                "resourceName": t.string(),
                "resourceNamesToRemove": t.array(t.string()).optional(),
                "resourceNamesToAdd": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyContactGroupMembersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsCopyOtherContactToMyContactsGroup"] = people.get(
        "v1/otherContacts",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "requestSyncToken": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "sources": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOtherContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsSearch"] = people.get(
        "v1/otherContacts",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "requestSyncToken": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "sources": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOtherContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsList"] = people.get(
        "v1/otherContacts",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "requestSyncToken": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "sources": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOtherContactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="people", renames=renames, types=Box(types), functions=Box(functions)
    )
