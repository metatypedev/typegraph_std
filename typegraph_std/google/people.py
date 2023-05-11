from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_people() -> Import:
    people = HTTPRuntime("https://people.googleapis.com/")

    renames = {
        "ErrorResponse": "_people_1_ErrorResponse",
        "SipAddressIn": "_people_2_SipAddressIn",
        "SipAddressOut": "_people_3_SipAddressOut",
        "ExternalIdIn": "_people_4_ExternalIdIn",
        "ExternalIdOut": "_people_5_ExternalIdOut",
        "ListDirectoryPeopleResponseIn": "_people_6_ListDirectoryPeopleResponseIn",
        "ListDirectoryPeopleResponseOut": "_people_7_ListDirectoryPeopleResponseOut",
        "DomainMembershipIn": "_people_8_DomainMembershipIn",
        "DomainMembershipOut": "_people_9_DomainMembershipOut",
        "ResidenceIn": "_people_10_ResidenceIn",
        "ResidenceOut": "_people_11_ResidenceOut",
        "RelationshipStatusIn": "_people_12_RelationshipStatusIn",
        "RelationshipStatusOut": "_people_13_RelationshipStatusOut",
        "RelationIn": "_people_14_RelationIn",
        "RelationOut": "_people_15_RelationOut",
        "BraggingRightsIn": "_people_16_BraggingRightsIn",
        "BraggingRightsOut": "_people_17_BraggingRightsOut",
        "ModifyContactGroupMembersRequestIn": "_people_18_ModifyContactGroupMembersRequestIn",
        "ModifyContactGroupMembersRequestOut": "_people_19_ModifyContactGroupMembersRequestOut",
        "AddressIn": "_people_20_AddressIn",
        "AddressOut": "_people_21_AddressOut",
        "ContactToCreateIn": "_people_22_ContactToCreateIn",
        "ContactToCreateOut": "_people_23_ContactToCreateOut",
        "LocationIn": "_people_24_LocationIn",
        "LocationOut": "_people_25_LocationOut",
        "EmptyIn": "_people_26_EmptyIn",
        "EmptyOut": "_people_27_EmptyOut",
        "CalendarUrlIn": "_people_28_CalendarUrlIn",
        "CalendarUrlOut": "_people_29_CalendarUrlOut",
        "OrganizationIn": "_people_30_OrganizationIn",
        "OrganizationOut": "_people_31_OrganizationOut",
        "UrlIn": "_people_32_UrlIn",
        "UrlOut": "_people_33_UrlOut",
        "ContactGroupIn": "_people_34_ContactGroupIn",
        "ContactGroupOut": "_people_35_ContactGroupOut",
        "BatchUpdateContactsRequestIn": "_people_36_BatchUpdateContactsRequestIn",
        "BatchUpdateContactsRequestOut": "_people_37_BatchUpdateContactsRequestOut",
        "ContactGroupResponseIn": "_people_38_ContactGroupResponseIn",
        "ContactGroupResponseOut": "_people_39_ContactGroupResponseOut",
        "EmailAddressIn": "_people_40_EmailAddressIn",
        "EmailAddressOut": "_people_41_EmailAddressOut",
        "PhoneNumberIn": "_people_42_PhoneNumberIn",
        "PhoneNumberOut": "_people_43_PhoneNumberOut",
        "ImClientIn": "_people_44_ImClientIn",
        "ImClientOut": "_people_45_ImClientOut",
        "MiscKeywordIn": "_people_46_MiscKeywordIn",
        "MiscKeywordOut": "_people_47_MiscKeywordOut",
        "SourceIn": "_people_48_SourceIn",
        "SourceOut": "_people_49_SourceOut",
        "BatchCreateContactsRequestIn": "_people_50_BatchCreateContactsRequestIn",
        "BatchCreateContactsRequestOut": "_people_51_BatchCreateContactsRequestOut",
        "BatchDeleteContactsRequestIn": "_people_52_BatchDeleteContactsRequestIn",
        "BatchDeleteContactsRequestOut": "_people_53_BatchDeleteContactsRequestOut",
        "PersonMetadataIn": "_people_54_PersonMetadataIn",
        "PersonMetadataOut": "_people_55_PersonMetadataOut",
        "BiographyIn": "_people_56_BiographyIn",
        "BiographyOut": "_people_57_BiographyOut",
        "ContactGroupMembershipIn": "_people_58_ContactGroupMembershipIn",
        "ContactGroupMembershipOut": "_people_59_ContactGroupMembershipOut",
        "NameIn": "_people_60_NameIn",
        "NameOut": "_people_61_NameOut",
        "UpdateContactPhotoRequestIn": "_people_62_UpdateContactPhotoRequestIn",
        "UpdateContactPhotoRequestOut": "_people_63_UpdateContactPhotoRequestOut",
        "FileAsIn": "_people_64_FileAsIn",
        "FileAsOut": "_people_65_FileAsOut",
        "DateIn": "_people_66_DateIn",
        "DateOut": "_people_67_DateOut",
        "MembershipIn": "_people_68_MembershipIn",
        "MembershipOut": "_people_69_MembershipOut",
        "SkillIn": "_people_70_SkillIn",
        "SkillOut": "_people_71_SkillOut",
        "BatchGetContactGroupsResponseIn": "_people_72_BatchGetContactGroupsResponseIn",
        "BatchGetContactGroupsResponseOut": "_people_73_BatchGetContactGroupsResponseOut",
        "UpdateContactPhotoResponseIn": "_people_74_UpdateContactPhotoResponseIn",
        "UpdateContactPhotoResponseOut": "_people_75_UpdateContactPhotoResponseOut",
        "ModifyContactGroupMembersResponseIn": "_people_76_ModifyContactGroupMembersResponseIn",
        "ModifyContactGroupMembersResponseOut": "_people_77_ModifyContactGroupMembersResponseOut",
        "GroupClientDataIn": "_people_78_GroupClientDataIn",
        "GroupClientDataOut": "_people_79_GroupClientDataOut",
        "CopyOtherContactToMyContactsGroupRequestIn": "_people_80_CopyOtherContactToMyContactsGroupRequestIn",
        "CopyOtherContactToMyContactsGroupRequestOut": "_people_81_CopyOtherContactToMyContactsGroupRequestOut",
        "GenderIn": "_people_82_GenderIn",
        "GenderOut": "_people_83_GenderOut",
        "BirthdayIn": "_people_84_BirthdayIn",
        "BirthdayOut": "_people_85_BirthdayOut",
        "SearchDirectoryPeopleResponseIn": "_people_86_SearchDirectoryPeopleResponseIn",
        "SearchDirectoryPeopleResponseOut": "_people_87_SearchDirectoryPeopleResponseOut",
        "CreateContactGroupRequestIn": "_people_88_CreateContactGroupRequestIn",
        "CreateContactGroupRequestOut": "_people_89_CreateContactGroupRequestOut",
        "InterestIn": "_people_90_InterestIn",
        "InterestOut": "_people_91_InterestOut",
        "DeleteContactPhotoResponseIn": "_people_92_DeleteContactPhotoResponseIn",
        "DeleteContactPhotoResponseOut": "_people_93_DeleteContactPhotoResponseOut",
        "PhotoIn": "_people_94_PhotoIn",
        "PhotoOut": "_people_95_PhotoOut",
        "BatchUpdateContactsResponseIn": "_people_96_BatchUpdateContactsResponseIn",
        "BatchUpdateContactsResponseOut": "_people_97_BatchUpdateContactsResponseOut",
        "PersonIn": "_people_98_PersonIn",
        "PersonOut": "_people_99_PersonOut",
        "GetPeopleResponseIn": "_people_100_GetPeopleResponseIn",
        "GetPeopleResponseOut": "_people_101_GetPeopleResponseOut",
        "ListConnectionsResponseIn": "_people_102_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_people_103_ListConnectionsResponseOut",
        "TaglineIn": "_people_104_TaglineIn",
        "TaglineOut": "_people_105_TaglineOut",
        "ProfileMetadataIn": "_people_106_ProfileMetadataIn",
        "ProfileMetadataOut": "_people_107_ProfileMetadataOut",
        "SearchResultIn": "_people_108_SearchResultIn",
        "SearchResultOut": "_people_109_SearchResultOut",
        "ClientDataIn": "_people_110_ClientDataIn",
        "ClientDataOut": "_people_111_ClientDataOut",
        "UpdateContactGroupRequestIn": "_people_112_UpdateContactGroupRequestIn",
        "UpdateContactGroupRequestOut": "_people_113_UpdateContactGroupRequestOut",
        "NicknameIn": "_people_114_NicknameIn",
        "NicknameOut": "_people_115_NicknameOut",
        "StatusIn": "_people_116_StatusIn",
        "StatusOut": "_people_117_StatusOut",
        "ContactGroupMetadataIn": "_people_118_ContactGroupMetadataIn",
        "ContactGroupMetadataOut": "_people_119_ContactGroupMetadataOut",
        "LocaleIn": "_people_120_LocaleIn",
        "LocaleOut": "_people_121_LocaleOut",
        "CoverPhotoIn": "_people_122_CoverPhotoIn",
        "CoverPhotoOut": "_people_123_CoverPhotoOut",
        "UserDefinedIn": "_people_124_UserDefinedIn",
        "UserDefinedOut": "_people_125_UserDefinedOut",
        "FieldMetadataIn": "_people_126_FieldMetadataIn",
        "FieldMetadataOut": "_people_127_FieldMetadataOut",
        "BatchCreateContactsResponseIn": "_people_128_BatchCreateContactsResponseIn",
        "BatchCreateContactsResponseOut": "_people_129_BatchCreateContactsResponseOut",
        "SearchResponseIn": "_people_130_SearchResponseIn",
        "SearchResponseOut": "_people_131_SearchResponseOut",
        "PersonResponseIn": "_people_132_PersonResponseIn",
        "PersonResponseOut": "_people_133_PersonResponseOut",
        "AgeRangeTypeIn": "_people_134_AgeRangeTypeIn",
        "AgeRangeTypeOut": "_people_135_AgeRangeTypeOut",
        "ListContactGroupsResponseIn": "_people_136_ListContactGroupsResponseIn",
        "ListContactGroupsResponseOut": "_people_137_ListContactGroupsResponseOut",
        "OccupationIn": "_people_138_OccupationIn",
        "OccupationOut": "_people_139_OccupationOut",
        "EventIn": "_people_140_EventIn",
        "EventOut": "_people_141_EventOut",
        "RelationshipInterestIn": "_people_142_RelationshipInterestIn",
        "RelationshipInterestOut": "_people_143_RelationshipInterestOut",
        "ListOtherContactsResponseIn": "_people_144_ListOtherContactsResponseIn",
        "ListOtherContactsResponseOut": "_people_145_ListOtherContactsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SipAddressIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["SipAddressIn"])
    types["SipAddressOut"] = t.struct(
        {
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SipAddressOut"])
    types["ExternalIdIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ExternalIdIn"])
    types["ExternalIdOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalIdOut"])
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
    types["DomainMembershipIn"] = t.struct(
        {"inViewerDomain": t.boolean().optional()}
    ).named(renames["DomainMembershipIn"])
    types["DomainMembershipOut"] = t.struct(
        {
            "inViewerDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMembershipOut"])
    types["ResidenceIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "current": t.boolean().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["ResidenceIn"])
    types["ResidenceOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "current": t.boolean().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResidenceOut"])
    types["RelationshipStatusIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["RelationshipStatusIn"])
    types["RelationshipStatusOut"] = t.struct(
        {
            "formattedValue": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipStatusOut"])
    types["RelationIn"] = t.struct(
        {
            "type": t.string().optional(),
            "person": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "type": t.string().optional(),
            "person": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
    types["BraggingRightsIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["BraggingRightsIn"])
    types["BraggingRightsOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BraggingRightsOut"])
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
    types["AddressIn"] = t.struct(
        {
            "region": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "country": t.string().optional(),
            "type": t.string().optional(),
            "streetAddress": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "postalCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "formattedValue": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "region": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "country": t.string().optional(),
            "type": t.string().optional(),
            "streetAddress": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "postalCode": t.string().optional(),
            "countryCode": t.string().optional(),
            "poBox": t.string().optional(),
            "city": t.string().optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["ContactToCreateIn"] = t.struct(
        {"contactPerson": t.proxy(renames["PersonIn"])}
    ).named(renames["ContactToCreateIn"])
    types["ContactToCreateOut"] = t.struct(
        {
            "contactPerson": t.proxy(renames["PersonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactToCreateOut"])
    types["LocationIn"] = t.struct(
        {
            "value": t.string().optional(),
            "floor": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "buildingId": t.string().optional(),
            "deskCode": t.string().optional(),
            "floorSection": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "value": t.string().optional(),
            "floor": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "buildingId": t.string().optional(),
            "deskCode": t.string().optional(),
            "floorSection": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["OrganizationIn"] = t.struct(
        {
            "location": t.string().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "current": t.boolean().optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "name": t.string().optional(),
            "symbol": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "domain": t.string().optional(),
            "department": t.string().optional(),
            "jobDescription": t.string().optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "title": t.string().optional(),
            "costCenter": t.string().optional(),
            "phoneticName": t.string().optional(),
        }
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "location": t.string().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "current": t.boolean().optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "name": t.string().optional(),
            "symbol": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "domain": t.string().optional(),
            "department": t.string().optional(),
            "jobDescription": t.string().optional(),
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "formattedType": t.string().optional(),
            "title": t.string().optional(),
            "costCenter": t.string().optional(),
            "phoneticName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["UrlIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["UrlIn"])
    types["UrlOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlOut"])
    types["ContactGroupIn"] = t.struct(
        {
            "clientData": t.array(t.proxy(renames["GroupClientDataIn"])).optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ContactGroupIn"])
    types["ContactGroupOut"] = t.struct(
        {
            "clientData": t.array(t.proxy(renames["GroupClientDataOut"])).optional(),
            "groupType": t.string().optional(),
            "memberResourceNames": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["ContactGroupMetadataOut"]).optional(),
            "resourceName": t.string().optional(),
            "memberCount": t.integer().optional(),
            "formattedName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupOut"])
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
    types["ContactGroupResponseIn"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupIn"]).optional(),
            "requestedResourceName": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ContactGroupResponseIn"])
    types["ContactGroupResponseOut"] = t.struct(
        {
            "contactGroup": t.proxy(renames["ContactGroupOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupResponseOut"])
    types["EmailAddressIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
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
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "canonicalForm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["ImClientIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "username": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["ImClientIn"])
    types["ImClientOut"] = t.struct(
        {
            "formattedProtocol": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "username": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImClientOut"])
    types["MiscKeywordIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["MiscKeywordIn"])
    types["MiscKeywordOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "type": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MiscKeywordOut"])
    types["SourceIn"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "profileMetadata": t.proxy(renames["ProfileMetadataOut"]).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["BatchCreateContactsRequestIn"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "readMask": t.string(),
            "contacts": t.array(t.proxy(renames["ContactToCreateIn"])),
        }
    ).named(renames["BatchCreateContactsRequestIn"])
    types["BatchCreateContactsRequestOut"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "readMask": t.string(),
            "contacts": t.array(t.proxy(renames["ContactToCreateOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsRequestOut"])
    types["BatchDeleteContactsRequestIn"] = t.struct(
        {"resourceNames": t.array(t.string())}
    ).named(renames["BatchDeleteContactsRequestIn"])
    types["BatchDeleteContactsRequestOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteContactsRequestOut"])
    types["PersonMetadataIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["SourceIn"])).optional()}
    ).named(renames["PersonMetadataIn"])
    types["PersonMetadataOut"] = t.struct(
        {
            "deleted": t.boolean().optional(),
            "objectType": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "previousResourceNames": t.array(t.string()).optional(),
            "linkedPeopleResourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonMetadataOut"])
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
    types["NameIn"] = t.struct(
        {
            "honorificPrefix": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "middleName": t.string().optional(),
            "phoneticHonorificPrefix": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "honorificPrefix": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "givenName": t.string().optional(),
            "familyName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "phoneticFullName": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "displayName": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "displayNameLastFirst": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "middleName": t.string().optional(),
            "phoneticHonorificPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
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
    types["FileAsIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["FileAsIn"])
    types["FileAsOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileAsOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
            "domainMembership": t.proxy(renames["DomainMembershipOut"]).optional(),
            "contactGroupMembership": t.proxy(
                renames["ContactGroupMembershipOut"]
            ).optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
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
    types["UpdateContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["UpdateContactPhotoResponseIn"])
    types["UpdateContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoResponseOut"])
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
    types["CopyOtherContactToMyContactsGroupRequestIn"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "copyMask": t.string(),
            "readMask": t.string().optional(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestIn"])
    types["CopyOtherContactToMyContactsGroupRequestOut"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "copyMask": t.string(),
            "readMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestOut"])
    types["GenderIn"] = t.struct(
        {
            "value": t.string().optional(),
            "addressMeAs": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["GenderIn"])
    types["GenderOut"] = t.struct(
        {
            "value": t.string().optional(),
            "formattedValue": t.string().optional(),
            "addressMeAs": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderOut"])
    types["BirthdayIn"] = t.struct(
        {
            "text": t.string().optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["BirthdayIn"])
    types["BirthdayOut"] = t.struct(
        {
            "text": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BirthdayOut"])
    types["SearchDirectoryPeopleResponseIn"] = t.struct(
        {
            "people": t.array(t.proxy(renames["PersonIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseIn"])
    types["SearchDirectoryPeopleResponseOut"] = t.struct(
        {
            "people": t.array(t.proxy(renames["PersonOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDirectoryPeopleResponseOut"])
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
    types["DeleteContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["DeleteContactPhotoResponseIn"])
    types["DeleteContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteContactPhotoResponseOut"])
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
    types["BatchUpdateContactsResponseIn"] = t.struct(
        {"updateResult": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BatchUpdateContactsResponseIn"])
    types["BatchUpdateContactsResponseOut"] = t.struct(
        {
            "updateResult": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsResponseOut"])
    types["PersonIn"] = t.struct(
        {
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "etag": t.string().optional(),
            "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
            "names": t.array(t.proxy(renames["NameIn"])).optional(),
            "resourceName": t.string().optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
            "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsIn"])).optional(),
            "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
            "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
            "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "etag": t.string().optional(),
            "occupations": t.array(t.proxy(renames["OccupationOut"])).optional(),
            "ageRanges": t.array(t.proxy(renames["AgeRangeTypeOut"])).optional(),
            "relationshipStatuses": t.array(
                t.proxy(renames["RelationshipStatusOut"])
            ).optional(),
            "names": t.array(t.proxy(renames["NameOut"])).optional(),
            "resourceName": t.string().optional(),
            "coverPhotos": t.array(t.proxy(renames["CoverPhotoOut"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordOut"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedOut"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "genders": t.array(t.proxy(renames["GenderOut"])).optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "ageRange": t.string().optional(),
            "biographies": t.array(t.proxy(renames["BiographyOut"])).optional(),
            "taglines": t.array(t.proxy(renames["TaglineOut"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "relationshipInterests": t.array(
                t.proxy(renames["RelationshipInterestOut"])
            ).optional(),
            "residences": t.array(t.proxy(renames["ResidenceOut"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressOut"])).optional(),
            "fileAses": t.array(t.proxy(renames["FileAsOut"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameOut"])).optional(),
            "skills": t.array(t.proxy(renames["SkillOut"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlOut"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "metadata": t.proxy(renames["PersonMetadataOut"]).optional(),
            "addresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsOut"])).optional(),
            "relations": t.array(t.proxy(renames["RelationOut"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientOut"])).optional(),
            "urls": t.array(t.proxy(renames["UrlOut"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataOut"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdOut"])).optional(),
            "interests": t.array(t.proxy(renames["InterestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
    types["GetPeopleResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["GetPeopleResponseIn"])
    types["GetPeopleResponseOut"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPeopleResponseOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonIn"])).optional(),
            "totalPeople": t.integer().optional(),
        }
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonOut"])).optional(),
            "totalPeople": t.integer().optional(),
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
    types["SearchResultIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["SearchResultIn"])
    types["SearchResultOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResultOut"])
    types["ClientDataIn"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["ClientDataIn"])
    types["ClientDataOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientDataOut"])
    types["UpdateContactGroupRequestIn"] = t.struct(
        {
            "updateGroupFields": t.string().optional(),
            "readGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupIn"]),
        }
    ).named(renames["UpdateContactGroupRequestIn"])
    types["UpdateContactGroupRequestOut"] = t.struct(
        {
            "updateGroupFields": t.string().optional(),
            "readGroupFields": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactGroupRequestOut"])
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
    types["LocaleIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["LocaleIn"])
    types["LocaleOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocaleOut"])
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
    types["UserDefinedIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["UserDefinedIn"])
    types["UserDefinedOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserDefinedOut"])
    types["FieldMetadataIn"] = t.struct(
        {
            "sourcePrimary": t.boolean().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "sourcePrimary": t.boolean().optional(),
            "primary": t.boolean().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "verified": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["BatchCreateContactsResponseIn"] = t.struct(
        {"createdPeople": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["BatchCreateContactsResponseIn"])
    types["BatchCreateContactsResponseOut"] = t.struct(
        {
            "createdPeople": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsResponseOut"])
    types["SearchResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["SearchResultIn"])).optional()}
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
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
    types["ListContactGroupsResponseIn"] = t.struct(
        {
            "contactGroups": t.array(t.proxy(renames["ContactGroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["ListContactGroupsResponseIn"])
    types["ListContactGroupsResponseOut"] = t.struct(
        {
            "contactGroups": t.array(t.proxy(renames["ContactGroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactGroupsResponseOut"])
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
    types["EventIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "date": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "date": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["RelationshipInterestIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["RelationshipInterestIn"])
    types["RelationshipInterestOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipInterestOut"])
    types["ListOtherContactsResponseIn"] = t.struct(
        {
            "otherContacts": t.array(t.proxy(renames["PersonIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOtherContactsResponseIn"])
    types["ListOtherContactsResponseOut"] = t.struct(
        {
            "otherContacts": t.array(t.proxy(renames["PersonOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOtherContactsResponseOut"])

    functions = {}
    functions["otherContactsList"] = people.post(
        "v1/{resourceName}:copyOtherContactToMyContactsGroup",
        t.struct(
            {
                "resourceName": t.string(),
                "sources": t.array(t.string()).optional(),
                "copyMask": t.string(),
                "readMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsSearch"] = people.post(
        "v1/{resourceName}:copyOtherContactToMyContactsGroup",
        t.struct(
            {
                "resourceName": t.string(),
                "sources": t.array(t.string()).optional(),
                "copyMask": t.string(),
                "readMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsCopyOtherContactToMyContactsGroup"] = people.post(
        "v1/{resourceName}:copyOtherContactToMyContactsGroup",
        t.struct(
            {
                "resourceName": t.string(),
                "sources": t.array(t.string()).optional(),
                "copyMask": t.string(),
                "readMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContactPhoto"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchDeleteContacts"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchDirectoryPeople"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchUpdateContacts"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleCreateContact"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchCreateContacts"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleListDirectoryPeople"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGet"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchContacts"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGetBatchGet"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContactPhoto"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContact"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContact"] = people.patch(
        "v1/{resourceName}:updateContact",
        t.struct(
            {
                "personFields": t.string().optional(),
                "updatePersonFields": t.string(),
                "sources": t.string().optional(),
                "resourceName": t.string().optional(),
                "events": t.array(t.proxy(renames["EventIn"])).optional(),
                "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
                "etag": t.string().optional(),
                "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
                "names": t.array(t.proxy(renames["NameIn"])).optional(),
                "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
                "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
                "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
                "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
                "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
                "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
                "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
                "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
                "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
                "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
                "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
                "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
                "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
                "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
                "emailAddresses": t.array(
                    t.proxy(renames["EmailAddressIn"])
                ).optional(),
                "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
                "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
                "braggingRights": t.array(
                    t.proxy(renames["BraggingRightsIn"])
                ).optional(),
                "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
                "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
                "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
                "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
                "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
                "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleConnectionsList"] = people.get(
        "v1/{resourceName}/connections",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "sources": t.string().optional(),
                "syncToken": t.string().optional(),
                "requestSyncToken": t.boolean().optional(),
                "resourceName": t.string(),
                "pageToken": t.string().optional(),
                "personFields": t.string(),
                "requestMask.includeField": t.string(),
                "sortOrder": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsDelete"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsList"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsGet"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsUpdate"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsCreate"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["contactGroupsBatchGet"] = people.get(
        "v1/contactGroups:batchGet",
        t.struct(
            {
                "groupFields": t.string().optional(),
                "maxMembers": t.integer().optional(),
                "resourceNames": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetContactGroupsResponseOut"]),
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

    return Import(importer="people", renames=renames, types=types, functions=functions)
