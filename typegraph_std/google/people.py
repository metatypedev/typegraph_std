from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_people():
    people = HTTPRuntime("https://people.googleapis.com/")

    renames = {
        "ErrorResponse": "_people_1_ErrorResponse",
        "SkillIn": "_people_2_SkillIn",
        "SkillOut": "_people_3_SkillOut",
        "ClientDataIn": "_people_4_ClientDataIn",
        "ClientDataOut": "_people_5_ClientDataOut",
        "PersonIn": "_people_6_PersonIn",
        "PersonOut": "_people_7_PersonOut",
        "DeleteContactPhotoResponseIn": "_people_8_DeleteContactPhotoResponseIn",
        "DeleteContactPhotoResponseOut": "_people_9_DeleteContactPhotoResponseOut",
        "ListDirectoryPeopleResponseIn": "_people_10_ListDirectoryPeopleResponseIn",
        "ListDirectoryPeopleResponseOut": "_people_11_ListDirectoryPeopleResponseOut",
        "ContactGroupResponseIn": "_people_12_ContactGroupResponseIn",
        "ContactGroupResponseOut": "_people_13_ContactGroupResponseOut",
        "ProfileMetadataIn": "_people_14_ProfileMetadataIn",
        "ProfileMetadataOut": "_people_15_ProfileMetadataOut",
        "RelationshipStatusIn": "_people_16_RelationshipStatusIn",
        "RelationshipStatusOut": "_people_17_RelationshipStatusOut",
        "ContactGroupMembershipIn": "_people_18_ContactGroupMembershipIn",
        "ContactGroupMembershipOut": "_people_19_ContactGroupMembershipOut",
        "ContactGroupIn": "_people_20_ContactGroupIn",
        "ContactGroupOut": "_people_21_ContactGroupOut",
        "ListConnectionsResponseIn": "_people_22_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_people_23_ListConnectionsResponseOut",
        "PhoneNumberIn": "_people_24_PhoneNumberIn",
        "PhoneNumberOut": "_people_25_PhoneNumberOut",
        "UserDefinedIn": "_people_26_UserDefinedIn",
        "UserDefinedOut": "_people_27_UserDefinedOut",
        "ModifyContactGroupMembersResponseIn": "_people_28_ModifyContactGroupMembersResponseIn",
        "ModifyContactGroupMembersResponseOut": "_people_29_ModifyContactGroupMembersResponseOut",
        "PhotoIn": "_people_30_PhotoIn",
        "PhotoOut": "_people_31_PhotoOut",
        "GetPeopleResponseIn": "_people_32_GetPeopleResponseIn",
        "GetPeopleResponseOut": "_people_33_GetPeopleResponseOut",
        "OccupationIn": "_people_34_OccupationIn",
        "OccupationOut": "_people_35_OccupationOut",
        "EmptyIn": "_people_36_EmptyIn",
        "EmptyOut": "_people_37_EmptyOut",
        "DomainMembershipIn": "_people_38_DomainMembershipIn",
        "DomainMembershipOut": "_people_39_DomainMembershipOut",
        "PersonMetadataIn": "_people_40_PersonMetadataIn",
        "PersonMetadataOut": "_people_41_PersonMetadataOut",
        "BatchGetContactGroupsResponseIn": "_people_42_BatchGetContactGroupsResponseIn",
        "BatchGetContactGroupsResponseOut": "_people_43_BatchGetContactGroupsResponseOut",
        "InterestIn": "_people_44_InterestIn",
        "InterestOut": "_people_45_InterestOut",
        "RelationshipInterestIn": "_people_46_RelationshipInterestIn",
        "RelationshipInterestOut": "_people_47_RelationshipInterestOut",
        "ListContactGroupsResponseIn": "_people_48_ListContactGroupsResponseIn",
        "ListContactGroupsResponseOut": "_people_49_ListContactGroupsResponseOut",
        "SearchResponseIn": "_people_50_SearchResponseIn",
        "SearchResponseOut": "_people_51_SearchResponseOut",
        "ContactGroupMetadataIn": "_people_52_ContactGroupMetadataIn",
        "ContactGroupMetadataOut": "_people_53_ContactGroupMetadataOut",
        "NameIn": "_people_54_NameIn",
        "NameOut": "_people_55_NameOut",
        "BatchCreateContactsRequestIn": "_people_56_BatchCreateContactsRequestIn",
        "BatchCreateContactsRequestOut": "_people_57_BatchCreateContactsRequestOut",
        "FieldMetadataIn": "_people_58_FieldMetadataIn",
        "FieldMetadataOut": "_people_59_FieldMetadataOut",
        "PersonResponseIn": "_people_60_PersonResponseIn",
        "PersonResponseOut": "_people_61_PersonResponseOut",
        "BatchUpdateContactsRequestIn": "_people_62_BatchUpdateContactsRequestIn",
        "BatchUpdateContactsRequestOut": "_people_63_BatchUpdateContactsRequestOut",
        "ResidenceIn": "_people_64_ResidenceIn",
        "ResidenceOut": "_people_65_ResidenceOut",
        "CreateContactGroupRequestIn": "_people_66_CreateContactGroupRequestIn",
        "CreateContactGroupRequestOut": "_people_67_CreateContactGroupRequestOut",
        "BraggingRightsIn": "_people_68_BraggingRightsIn",
        "BraggingRightsOut": "_people_69_BraggingRightsOut",
        "TaglineIn": "_people_70_TaglineIn",
        "TaglineOut": "_people_71_TaglineOut",
        "EventIn": "_people_72_EventIn",
        "EventOut": "_people_73_EventOut",
        "LocationIn": "_people_74_LocationIn",
        "LocationOut": "_people_75_LocationOut",
        "UpdateContactPhotoResponseIn": "_people_76_UpdateContactPhotoResponseIn",
        "UpdateContactPhotoResponseOut": "_people_77_UpdateContactPhotoResponseOut",
        "SipAddressIn": "_people_78_SipAddressIn",
        "SipAddressOut": "_people_79_SipAddressOut",
        "NicknameIn": "_people_80_NicknameIn",
        "NicknameOut": "_people_81_NicknameOut",
        "ImClientIn": "_people_82_ImClientIn",
        "ImClientOut": "_people_83_ImClientOut",
        "SourceIn": "_people_84_SourceIn",
        "SourceOut": "_people_85_SourceOut",
        "CopyOtherContactToMyContactsGroupRequestIn": "_people_86_CopyOtherContactToMyContactsGroupRequestIn",
        "CopyOtherContactToMyContactsGroupRequestOut": "_people_87_CopyOtherContactToMyContactsGroupRequestOut",
        "StatusIn": "_people_88_StatusIn",
        "StatusOut": "_people_89_StatusOut",
        "AgeRangeTypeIn": "_people_90_AgeRangeTypeIn",
        "AgeRangeTypeOut": "_people_91_AgeRangeTypeOut",
        "ListOtherContactsResponseIn": "_people_92_ListOtherContactsResponseIn",
        "ListOtherContactsResponseOut": "_people_93_ListOtherContactsResponseOut",
        "GenderIn": "_people_94_GenderIn",
        "GenderOut": "_people_95_GenderOut",
        "BatchUpdateContactsResponseIn": "_people_96_BatchUpdateContactsResponseIn",
        "BatchUpdateContactsResponseOut": "_people_97_BatchUpdateContactsResponseOut",
        "BatchDeleteContactsRequestIn": "_people_98_BatchDeleteContactsRequestIn",
        "BatchDeleteContactsRequestOut": "_people_99_BatchDeleteContactsRequestOut",
        "UpdateContactGroupRequestIn": "_people_100_UpdateContactGroupRequestIn",
        "UpdateContactGroupRequestOut": "_people_101_UpdateContactGroupRequestOut",
        "BatchCreateContactsResponseIn": "_people_102_BatchCreateContactsResponseIn",
        "BatchCreateContactsResponseOut": "_people_103_BatchCreateContactsResponseOut",
        "MiscKeywordIn": "_people_104_MiscKeywordIn",
        "MiscKeywordOut": "_people_105_MiscKeywordOut",
        "RelationIn": "_people_106_RelationIn",
        "RelationOut": "_people_107_RelationOut",
        "OrganizationIn": "_people_108_OrganizationIn",
        "OrganizationOut": "_people_109_OrganizationOut",
        "DateIn": "_people_110_DateIn",
        "DateOut": "_people_111_DateOut",
        "FileAsIn": "_people_112_FileAsIn",
        "FileAsOut": "_people_113_FileAsOut",
        "CoverPhotoIn": "_people_114_CoverPhotoIn",
        "CoverPhotoOut": "_people_115_CoverPhotoOut",
        "LocaleIn": "_people_116_LocaleIn",
        "LocaleOut": "_people_117_LocaleOut",
        "ModifyContactGroupMembersRequestIn": "_people_118_ModifyContactGroupMembersRequestIn",
        "ModifyContactGroupMembersRequestOut": "_people_119_ModifyContactGroupMembersRequestOut",
        "MembershipIn": "_people_120_MembershipIn",
        "MembershipOut": "_people_121_MembershipOut",
        "SearchDirectoryPeopleResponseIn": "_people_122_SearchDirectoryPeopleResponseIn",
        "SearchDirectoryPeopleResponseOut": "_people_123_SearchDirectoryPeopleResponseOut",
        "CalendarUrlIn": "_people_124_CalendarUrlIn",
        "CalendarUrlOut": "_people_125_CalendarUrlOut",
        "BiographyIn": "_people_126_BiographyIn",
        "BiographyOut": "_people_127_BiographyOut",
        "SearchResultIn": "_people_128_SearchResultIn",
        "SearchResultOut": "_people_129_SearchResultOut",
        "ExternalIdIn": "_people_130_ExternalIdIn",
        "ExternalIdOut": "_people_131_ExternalIdOut",
        "ContactToCreateIn": "_people_132_ContactToCreateIn",
        "ContactToCreateOut": "_people_133_ContactToCreateOut",
        "EmailAddressIn": "_people_134_EmailAddressIn",
        "EmailAddressOut": "_people_135_EmailAddressOut",
        "UrlIn": "_people_136_UrlIn",
        "UrlOut": "_people_137_UrlOut",
        "GroupClientDataIn": "_people_138_GroupClientDataIn",
        "GroupClientDataOut": "_people_139_GroupClientDataOut",
        "UpdateContactPhotoRequestIn": "_people_140_UpdateContactPhotoRequestIn",
        "UpdateContactPhotoRequestOut": "_people_141_UpdateContactPhotoRequestOut",
        "AddressIn": "_people_142_AddressIn",
        "AddressOut": "_people_143_AddressOut",
        "BirthdayIn": "_people_144_BirthdayIn",
        "BirthdayOut": "_people_145_BirthdayOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PersonIn"] = t.struct(
        {
            "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
            "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
            "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
            "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
            "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
            "resourceName": t.string().optional(),
            "etag": t.string().optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsIn"])).optional(),
            "names": t.array(t.proxy(renames["NameIn"])).optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "userDefined": t.array(t.proxy(renames["UserDefinedOut"])).optional(),
            "ageRange": t.string().optional(),
            "relations": t.array(t.proxy(renames["RelationOut"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlOut"])).optional(),
            "metadata": t.proxy(renames["PersonMetadataOut"]).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameOut"])).optional(),
            "coverPhotos": t.array(t.proxy(renames["CoverPhotoOut"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyOut"])).optional(),
            "skills": t.array(t.proxy(renames["SkillOut"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressOut"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceOut"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataOut"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordOut"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdOut"])).optional(),
            "taglines": t.array(t.proxy(renames["TaglineOut"])).optional(),
            "genders": t.array(t.proxy(renames["GenderOut"])).optional(),
            "relationshipInterests": t.array(
                t.proxy(renames["RelationshipInterestOut"])
            ).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayOut"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationOut"])).optional(),
            "urls": t.array(t.proxy(renames["UrlOut"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "relationshipStatuses": t.array(
                t.proxy(renames["RelationshipStatusOut"])
            ).optional(),
            "imClients": t.array(t.proxy(renames["ImClientOut"])).optional(),
            "resourceName": t.string().optional(),
            "etag": t.string().optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsOut"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "names": t.array(t.proxy(renames["NameOut"])).optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsOut"])).optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "interests": t.array(t.proxy(renames["InterestOut"])).optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "ageRanges": t.array(t.proxy(renames["AgeRangeTypeOut"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["DeleteContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["DeleteContactPhotoResponseIn"])
    types["DeleteContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContactPhotoResponseOut"])
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
    types["ContactGroupResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupIn"]).optional(),
            "requestedResourceName": t.string().optional(),
        }
    ).named(renames["ContactGroupResponseIn"])
    types["ContactGroupResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "contactGroup": t.proxy(renames["ContactGroupOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupResponseOut"])
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
    types["RelationshipStatusIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["RelationshipStatusIn"])
    types["RelationshipStatusOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedValue": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipStatusOut"])
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
    types["ContactGroupIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataIn"])).optional(),
            "name": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["ContactGroupIn"])
    types["ContactGroupOut"] = t.struct(
        {
            "groupType": t.string().optional(),
            "formattedName": t.string().optional(),
            "etag": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataOut"])).optional(),
            "name": t.string().optional(),
            "memberResourceNames": t.array(t.string()).optional(),
            "resourceName": t.string().optional(),
            "memberCount": t.integer().optional(),
            "metadata": t.proxy(renames["ContactGroupMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["PersonIn"])).optional(),
            "nextSyncToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["PersonOut"])).optional(),
            "nextSyncToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
    types["PhoneNumberIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["PhoneNumberIn"])
    types["PhoneNumberOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "canonicalForm": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["UserDefinedIn"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["UserDefinedIn"])
    types["UserDefinedOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedOut"])
    types["ModifyContactGroupMembersResponseIn"] = t.struct(
        {
            "notFoundResourceNames": t.array(t.string()).optional(),
            "canNotRemoveLastContactGroupResourceNames": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyContactGroupMembersResponseIn"])
    types["ModifyContactGroupMembersResponseOut"] = t.struct(
        {
            "notFoundResourceNames": t.array(t.string()).optional(),
            "canNotRemoveLastContactGroupResourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyContactGroupMembersResponseOut"])
    types["PhotoIn"] = t.struct(
        {
            "default": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "default": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["GetPeopleResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["GetPeopleResponseIn"])
    types["GetPeopleResponseOut"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPeopleResponseOut"])
    types["OccupationIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["OccupationIn"])
    types["OccupationOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OccupationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DomainMembershipIn"] = t.struct(
        {"inViewerDomain": t.boolean().optional()}
    ).named(renames["DomainMembershipIn"])
    types["DomainMembershipOut"] = t.struct(
        {
            "inViewerDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMembershipOut"])
    types["PersonMetadataIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["SourceIn"])).optional()}
    ).named(renames["PersonMetadataIn"])
    types["PersonMetadataOut"] = t.struct(
        {
            "previousResourceNames": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "linkedPeopleResourceNames": t.array(t.string()).optional(),
            "deleted": t.boolean().optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonMetadataOut"])
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
    types["InterestIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["InterestIn"])
    types["InterestOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InterestOut"])
    types["RelationshipInterestIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["RelationshipInterestIn"])
    types["RelationshipInterestOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedValue": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipInterestOut"])
    types["ListContactGroupsResponseIn"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "contactGroups": t.array(t.proxy(renames["ContactGroupIn"])).optional(),
        }
    ).named(renames["ListContactGroupsResponseIn"])
    types["ListContactGroupsResponseOut"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "contactGroups": t.array(t.proxy(renames["ContactGroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactGroupsResponseOut"])
    types["SearchResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["SearchResultIn"])).optional()}
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["ContactGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ContactGroupMetadataIn"]
    )
    types["ContactGroupMetadataOut"] = t.struct(
        {
            "deleted": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupMetadataOut"])
    types["NameIn"] = t.struct(
        {
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "honorificPrefix": t.string().optional(),
            "middleName": t.string().optional(),
            "givenName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "familyName": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "honorificPrefix": t.string().optional(),
            "middleName": t.string().optional(),
            "givenName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "familyName": t.string().optional(),
            "displayName": t.string().optional(),
            "displayNameLastFirst": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
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
    types["FieldMetadataIn"] = t.struct(
        {
            "sourcePrimary": t.boolean().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "primary": t.boolean().optional(),
            "verified": t.boolean().optional(),
            "sourcePrimary": t.boolean().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["PersonResponseIn"] = t.struct(
        {
            "requestedResourceName": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "httpStatusCode": t.integer().optional(),
            "person": t.proxy(renames["PersonIn"]).optional(),
        }
    ).named(renames["PersonResponseIn"])
    types["PersonResponseOut"] = t.struct(
        {
            "requestedResourceName": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "httpStatusCode": t.integer().optional(),
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonResponseOut"])
    types["BatchUpdateContactsRequestIn"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "updateMask": t.string(),
            "contacts": t.struct({"_": t.string().optional()}),
            "readMask": t.string(),
        }
    ).named(renames["BatchUpdateContactsRequestIn"])
    types["BatchUpdateContactsRequestOut"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "updateMask": t.string(),
            "contacts": t.struct({"_": t.string().optional()}),
            "readMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsRequestOut"])
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
    types["CreateContactGroupRequestIn"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupIn"]),
            "readGroupFields": t.string().optional(),
        }
    ).named(renames["CreateContactGroupRequestIn"])
    types["CreateContactGroupRequestOut"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupOut"]),
            "readGroupFields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateContactGroupRequestOut"])
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
    types["TaglineIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["TaglineIn"])
    types["TaglineOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaglineOut"])
    types["EventIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["LocationIn"] = t.struct(
        {
            "buildingId": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "floorSection": t.string().optional(),
            "current": t.boolean().optional(),
            "floor": t.string().optional(),
            "value": t.string().optional(),
            "deskCode": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "buildingId": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "floorSection": t.string().optional(),
            "current": t.boolean().optional(),
            "floor": t.string().optional(),
            "value": t.string().optional(),
            "deskCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["UpdateContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["UpdateContactPhotoResponseIn"])
    types["UpdateContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoResponseOut"])
    types["SipAddressIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["SipAddressIn"])
    types["SipAddressOut"] = t.struct(
        {
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SipAddressOut"])
    types["NicknameIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["NicknameIn"])
    types["NicknameOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NicknameOut"])
    types["ImClientIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "username": t.string().optional(),
            "type": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["ImClientIn"])
    types["ImClientOut"] = t.struct(
        {
            "formattedProtocol": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "username": t.string().optional(),
            "type": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImClientOut"])
    types["SourceIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "profileMetadata": t.proxy(renames["ProfileMetadataOut"]).optional(),
            "etag": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["AgeRangeTypeIn"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["AgeRangeTypeIn"])
    types["AgeRangeTypeOut"] = t.struct(
        {
            "ageRange": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AgeRangeTypeOut"])
    types["ListOtherContactsResponseIn"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "otherContacts": t.array(t.proxy(renames["PersonIn"])).optional(),
        }
    ).named(renames["ListOtherContactsResponseIn"])
    types["ListOtherContactsResponseOut"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "otherContacts": t.array(t.proxy(renames["PersonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOtherContactsResponseOut"])
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
    types["BatchUpdateContactsResponseIn"] = t.struct(
        {"updateResult": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BatchUpdateContactsResponseIn"])
    types["BatchUpdateContactsResponseOut"] = t.struct(
        {
            "updateResult": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsResponseOut"])
    types["BatchDeleteContactsRequestIn"] = t.struct(
        {"resourceNames": t.array(t.string())}
    ).named(renames["BatchDeleteContactsRequestIn"])
    types["BatchDeleteContactsRequestOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteContactsRequestOut"])
    types["UpdateContactGroupRequestIn"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupIn"]),
            "readGroupFields": t.string().optional(),
            "updateGroupFields": t.string().optional(),
        }
    ).named(renames["UpdateContactGroupRequestIn"])
    types["UpdateContactGroupRequestOut"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupOut"]),
            "readGroupFields": t.string().optional(),
            "updateGroupFields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactGroupRequestOut"])
    types["BatchCreateContactsResponseIn"] = t.struct(
        {"createdPeople": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["BatchCreateContactsResponseIn"])
    types["BatchCreateContactsResponseOut"] = t.struct(
        {
            "createdPeople": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsResponseOut"])
    types["MiscKeywordIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["MiscKeywordIn"])
    types["MiscKeywordOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MiscKeywordOut"])
    types["RelationIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "person": t.string().optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "person": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
    types["OrganizationIn"] = t.struct(
        {
            "department": t.string().optional(),
            "jobDescription": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "costCenter": t.string().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "symbol": t.string().optional(),
            "current": t.boolean().optional(),
            "domain": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "phoneticName": t.string().optional(),
        }
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "department": t.string().optional(),
            "jobDescription": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "costCenter": t.string().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "formattedType": t.string().optional(),
            "symbol": t.string().optional(),
            "current": t.boolean().optional(),
            "domain": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "phoneticName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["CoverPhotoIn"] = t.struct(
        {
            "url": t.string().optional(),
            "default": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["CoverPhotoIn"])
    types["CoverPhotoOut"] = t.struct(
        {
            "url": t.string().optional(),
            "default": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CoverPhotoOut"])
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
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "domainMembership": t.proxy(renames["DomainMembershipOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["SearchDirectoryPeopleResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "people": t.array(t.proxy(renames["PersonIn"])).optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseIn"])
    types["SearchDirectoryPeopleResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "people": t.array(t.proxy(renames["PersonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseOut"])
    types["CalendarUrlIn"] = t.struct(
        {
            "url": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CalendarUrlIn"])
    types["CalendarUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarUrlOut"])
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
    types["SearchResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["ExternalIdIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["ExternalIdIn"])
    types["ExternalIdOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalIdOut"])
    types["ContactToCreateIn"] = t.struct(
        {"contactPerson": t.proxy(renames["PersonIn"])}
    ).named(renames["ContactToCreateIn"])
    types["ContactToCreateOut"] = t.struct(
        {
            "contactPerson": t.proxy(renames["PersonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactToCreateOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
    types["UrlIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["UrlIn"])
    types["UrlOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlOut"])
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
            "personFields": t.string().optional(),
            "sources": t.array(t.string()).optional(),
            "photoBytes": t.string(),
        }
    ).named(renames["UpdateContactPhotoRequestIn"])
    types["UpdateContactPhotoRequestOut"] = t.struct(
        {
            "personFields": t.string().optional(),
            "sources": t.array(t.string()).optional(),
            "photoBytes": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoRequestOut"])
    types["AddressIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "extendedAddress": t.string().optional(),
            "region": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "countryCode": t.string().optional(),
            "formattedValue": t.string().optional(),
            "streetAddress": t.string().optional(),
            "type": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "extendedAddress": t.string().optional(),
            "region": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "countryCode": t.string().optional(),
            "formattedValue": t.string().optional(),
            "streetAddress": t.string().optional(),
            "type": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["BirthdayIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "text": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["BirthdayIn"])
    types["BirthdayOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "text": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BirthdayOut"])

    functions = {}
    functions["contactGroupsGet"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsBatchGet"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsUpdate"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsDelete"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsCreate"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsList"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListContactGroupsResponseOut"]),
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
    functions["peopleDeleteContactPhoto"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchDeleteContacts"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGet"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchDirectoryPeople"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchContacts"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleCreateContact"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContactPhoto"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContact"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchUpdateContacts"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchCreateContacts"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleListDirectoryPeople"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContact"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGetBatchGet"] = people.get(
        "v1/people:batchGet",
        t.struct(
            {
                "requestMask.includeField": t.string(),
                "sources": t.string().optional(),
                "personFields": t.string(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetPeopleResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleConnectionsList"] = people.get(
        "v1/{resourceName}/connections",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "sortOrder": t.string().optional(),
                "requestMask.includeField": t.string(),
                "syncToken": t.string().optional(),
                "requestSyncToken": t.boolean().optional(),
                "resourceName": t.string(),
                "personFields": t.string(),
                "sources": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsList"] = people.get(
        "v1/otherContacts:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsCopyOtherContactToMyContactsGroup"] = people.get(
        "v1/otherContacts:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsSearch"] = people.get(
        "v1/otherContacts:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="people", renames=renames, types=Box(types), functions=Box(functions)
    )
