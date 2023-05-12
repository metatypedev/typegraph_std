from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_people() -> Import:
    people = HTTPRuntime("https://people.googleapis.com/")

    renames = {
        "ErrorResponse": "_people_1_ErrorResponse",
        "NameIn": "_people_2_NameIn",
        "NameOut": "_people_3_NameOut",
        "DomainMembershipIn": "_people_4_DomainMembershipIn",
        "DomainMembershipOut": "_people_5_DomainMembershipOut",
        "ContactGroupResponseIn": "_people_6_ContactGroupResponseIn",
        "ContactGroupResponseOut": "_people_7_ContactGroupResponseOut",
        "SearchResponseIn": "_people_8_SearchResponseIn",
        "SearchResponseOut": "_people_9_SearchResponseOut",
        "ClientDataIn": "_people_10_ClientDataIn",
        "ClientDataOut": "_people_11_ClientDataOut",
        "GenderIn": "_people_12_GenderIn",
        "GenderOut": "_people_13_GenderOut",
        "TaglineIn": "_people_14_TaglineIn",
        "TaglineOut": "_people_15_TaglineOut",
        "BatchCreateContactsRequestIn": "_people_16_BatchCreateContactsRequestIn",
        "BatchCreateContactsRequestOut": "_people_17_BatchCreateContactsRequestOut",
        "PersonMetadataIn": "_people_18_PersonMetadataIn",
        "PersonMetadataOut": "_people_19_PersonMetadataOut",
        "BraggingRightsIn": "_people_20_BraggingRightsIn",
        "BraggingRightsOut": "_people_21_BraggingRightsOut",
        "RelationshipStatusIn": "_people_22_RelationshipStatusIn",
        "RelationshipStatusOut": "_people_23_RelationshipStatusOut",
        "InterestIn": "_people_24_InterestIn",
        "InterestOut": "_people_25_InterestOut",
        "BatchCreateContactsResponseIn": "_people_26_BatchCreateContactsResponseIn",
        "BatchCreateContactsResponseOut": "_people_27_BatchCreateContactsResponseOut",
        "BatchDeleteContactsRequestIn": "_people_28_BatchDeleteContactsRequestIn",
        "BatchDeleteContactsRequestOut": "_people_29_BatchDeleteContactsRequestOut",
        "ListDirectoryPeopleResponseIn": "_people_30_ListDirectoryPeopleResponseIn",
        "ListDirectoryPeopleResponseOut": "_people_31_ListDirectoryPeopleResponseOut",
        "SipAddressIn": "_people_32_SipAddressIn",
        "SipAddressOut": "_people_33_SipAddressOut",
        "ListContactGroupsResponseIn": "_people_34_ListContactGroupsResponseIn",
        "ListContactGroupsResponseOut": "_people_35_ListContactGroupsResponseOut",
        "ContactGroupMetadataIn": "_people_36_ContactGroupMetadataIn",
        "ContactGroupMetadataOut": "_people_37_ContactGroupMetadataOut",
        "LocaleIn": "_people_38_LocaleIn",
        "LocaleOut": "_people_39_LocaleOut",
        "UserDefinedIn": "_people_40_UserDefinedIn",
        "UserDefinedOut": "_people_41_UserDefinedOut",
        "BirthdayIn": "_people_42_BirthdayIn",
        "BirthdayOut": "_people_43_BirthdayOut",
        "PersonResponseIn": "_people_44_PersonResponseIn",
        "PersonResponseOut": "_people_45_PersonResponseOut",
        "OccupationIn": "_people_46_OccupationIn",
        "OccupationOut": "_people_47_OccupationOut",
        "UpdateContactGroupRequestIn": "_people_48_UpdateContactGroupRequestIn",
        "UpdateContactGroupRequestOut": "_people_49_UpdateContactGroupRequestOut",
        "FileAsIn": "_people_50_FileAsIn",
        "FileAsOut": "_people_51_FileAsOut",
        "ContactGroupMembershipIn": "_people_52_ContactGroupMembershipIn",
        "ContactGroupMembershipOut": "_people_53_ContactGroupMembershipOut",
        "ListConnectionsResponseIn": "_people_54_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_people_55_ListConnectionsResponseOut",
        "GroupClientDataIn": "_people_56_GroupClientDataIn",
        "GroupClientDataOut": "_people_57_GroupClientDataOut",
        "FieldMetadataIn": "_people_58_FieldMetadataIn",
        "FieldMetadataOut": "_people_59_FieldMetadataOut",
        "OrganizationIn": "_people_60_OrganizationIn",
        "OrganizationOut": "_people_61_OrganizationOut",
        "EventIn": "_people_62_EventIn",
        "EventOut": "_people_63_EventOut",
        "ProfileMetadataIn": "_people_64_ProfileMetadataIn",
        "ProfileMetadataOut": "_people_65_ProfileMetadataOut",
        "NicknameIn": "_people_66_NicknameIn",
        "NicknameOut": "_people_67_NicknameOut",
        "EmptyIn": "_people_68_EmptyIn",
        "EmptyOut": "_people_69_EmptyOut",
        "BatchUpdateContactsRequestIn": "_people_70_BatchUpdateContactsRequestIn",
        "BatchUpdateContactsRequestOut": "_people_71_BatchUpdateContactsRequestOut",
        "ContactToCreateIn": "_people_72_ContactToCreateIn",
        "ContactToCreateOut": "_people_73_ContactToCreateOut",
        "SearchDirectoryPeopleResponseIn": "_people_74_SearchDirectoryPeopleResponseIn",
        "SearchDirectoryPeopleResponseOut": "_people_75_SearchDirectoryPeopleResponseOut",
        "ExternalIdIn": "_people_76_ExternalIdIn",
        "ExternalIdOut": "_people_77_ExternalIdOut",
        "CoverPhotoIn": "_people_78_CoverPhotoIn",
        "CoverPhotoOut": "_people_79_CoverPhotoOut",
        "EmailAddressIn": "_people_80_EmailAddressIn",
        "EmailAddressOut": "_people_81_EmailAddressOut",
        "SearchResultIn": "_people_82_SearchResultIn",
        "SearchResultOut": "_people_83_SearchResultOut",
        "CreateContactGroupRequestIn": "_people_84_CreateContactGroupRequestIn",
        "CreateContactGroupRequestOut": "_people_85_CreateContactGroupRequestOut",
        "GetPeopleResponseIn": "_people_86_GetPeopleResponseIn",
        "GetPeopleResponseOut": "_people_87_GetPeopleResponseOut",
        "CalendarUrlIn": "_people_88_CalendarUrlIn",
        "CalendarUrlOut": "_people_89_CalendarUrlOut",
        "MembershipIn": "_people_90_MembershipIn",
        "MembershipOut": "_people_91_MembershipOut",
        "UpdateContactPhotoRequestIn": "_people_92_UpdateContactPhotoRequestIn",
        "UpdateContactPhotoRequestOut": "_people_93_UpdateContactPhotoRequestOut",
        "DeleteContactPhotoResponseIn": "_people_94_DeleteContactPhotoResponseIn",
        "DeleteContactPhotoResponseOut": "_people_95_DeleteContactPhotoResponseOut",
        "ResidenceIn": "_people_96_ResidenceIn",
        "ResidenceOut": "_people_97_ResidenceOut",
        "RelationIn": "_people_98_RelationIn",
        "RelationOut": "_people_99_RelationOut",
        "ImClientIn": "_people_100_ImClientIn",
        "ImClientOut": "_people_101_ImClientOut",
        "ModifyContactGroupMembersRequestIn": "_people_102_ModifyContactGroupMembersRequestIn",
        "ModifyContactGroupMembersRequestOut": "_people_103_ModifyContactGroupMembersRequestOut",
        "RelationshipInterestIn": "_people_104_RelationshipInterestIn",
        "RelationshipInterestOut": "_people_105_RelationshipInterestOut",
        "BatchGetContactGroupsResponseIn": "_people_106_BatchGetContactGroupsResponseIn",
        "BatchGetContactGroupsResponseOut": "_people_107_BatchGetContactGroupsResponseOut",
        "DateIn": "_people_108_DateIn",
        "DateOut": "_people_109_DateOut",
        "StatusIn": "_people_110_StatusIn",
        "StatusOut": "_people_111_StatusOut",
        "UpdateContactPhotoResponseIn": "_people_112_UpdateContactPhotoResponseIn",
        "UpdateContactPhotoResponseOut": "_people_113_UpdateContactPhotoResponseOut",
        "AddressIn": "_people_114_AddressIn",
        "AddressOut": "_people_115_AddressOut",
        "PhoneNumberIn": "_people_116_PhoneNumberIn",
        "PhoneNumberOut": "_people_117_PhoneNumberOut",
        "BatchUpdateContactsResponseIn": "_people_118_BatchUpdateContactsResponseIn",
        "BatchUpdateContactsResponseOut": "_people_119_BatchUpdateContactsResponseOut",
        "PhotoIn": "_people_120_PhotoIn",
        "PhotoOut": "_people_121_PhotoOut",
        "PersonIn": "_people_122_PersonIn",
        "PersonOut": "_people_123_PersonOut",
        "BiographyIn": "_people_124_BiographyIn",
        "BiographyOut": "_people_125_BiographyOut",
        "AgeRangeTypeIn": "_people_126_AgeRangeTypeIn",
        "AgeRangeTypeOut": "_people_127_AgeRangeTypeOut",
        "ModifyContactGroupMembersResponseIn": "_people_128_ModifyContactGroupMembersResponseIn",
        "ModifyContactGroupMembersResponseOut": "_people_129_ModifyContactGroupMembersResponseOut",
        "SourceIn": "_people_130_SourceIn",
        "SourceOut": "_people_131_SourceOut",
        "ListOtherContactsResponseIn": "_people_132_ListOtherContactsResponseIn",
        "ListOtherContactsResponseOut": "_people_133_ListOtherContactsResponseOut",
        "MiscKeywordIn": "_people_134_MiscKeywordIn",
        "MiscKeywordOut": "_people_135_MiscKeywordOut",
        "SkillIn": "_people_136_SkillIn",
        "SkillOut": "_people_137_SkillOut",
        "ContactGroupIn": "_people_138_ContactGroupIn",
        "ContactGroupOut": "_people_139_ContactGroupOut",
        "LocationIn": "_people_140_LocationIn",
        "LocationOut": "_people_141_LocationOut",
        "UrlIn": "_people_142_UrlIn",
        "UrlOut": "_people_143_UrlOut",
        "CopyOtherContactToMyContactsGroupRequestIn": "_people_144_CopyOtherContactToMyContactsGroupRequestIn",
        "CopyOtherContactToMyContactsGroupRequestOut": "_people_145_CopyOtherContactToMyContactsGroupRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NameIn"] = t.struct(
        {
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "givenName": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "middleName": t.string().optional(),
            "familyName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "honorificPrefix": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "phoneticFullName": t.string().optional(),
        }
    ).named(renames["NameIn"])
    types["NameOut"] = t.struct(
        {
            "phoneticHonorificPrefix": t.string().optional(),
            "phoneticGivenName": t.string().optional(),
            "phoneticFamilyName": t.string().optional(),
            "givenName": t.string().optional(),
            "unstructuredName": t.string().optional(),
            "phoneticMiddleName": t.string().optional(),
            "displayNameLastFirst": t.string().optional(),
            "phoneticHonorificSuffix": t.string().optional(),
            "middleName": t.string().optional(),
            "familyName": t.string().optional(),
            "honorificSuffix": t.string().optional(),
            "displayName": t.string().optional(),
            "honorificPrefix": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "phoneticFullName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NameOut"])
    types["DomainMembershipIn"] = t.struct(
        {"inViewerDomain": t.boolean().optional()}
    ).named(renames["DomainMembershipIn"])
    types["DomainMembershipOut"] = t.struct(
        {
            "inViewerDomain": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMembershipOut"])
    types["ContactGroupResponseIn"] = t.struct(
        {
            "requestedResourceName": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ContactGroupResponseIn"])
    types["ContactGroupResponseOut"] = t.struct(
        {
            "requestedResourceName": t.string().optional(),
            "contactGroup": t.proxy(renames["ContactGroupOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupResponseOut"])
    types["SearchResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["SearchResultIn"])).optional()}
    ).named(renames["SearchResponseIn"])
    types["SearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["SearchResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchResponseOut"])
    types["ClientDataIn"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "key": t.string().optional(),
        }
    ).named(renames["ClientDataIn"])
    types["ClientDataOut"] = t.struct(
        {
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientDataOut"])
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
            "formattedValue": t.string().optional(),
            "value": t.string().optional(),
            "addressMeAs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenderOut"])
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
    types["BatchCreateContactsRequestIn"] = t.struct(
        {
            "readMask": t.string(),
            "contacts": t.array(t.proxy(renames["ContactToCreateIn"])),
            "sources": t.array(t.string()).optional(),
        }
    ).named(renames["BatchCreateContactsRequestIn"])
    types["BatchCreateContactsRequestOut"] = t.struct(
        {
            "readMask": t.string(),
            "contacts": t.array(t.proxy(renames["ContactToCreateOut"])),
            "sources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsRequestOut"])
    types["PersonMetadataIn"] = t.struct(
        {"sources": t.array(t.proxy(renames["SourceIn"])).optional()}
    ).named(renames["PersonMetadataIn"])
    types["PersonMetadataOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "deleted": t.boolean().optional(),
            "objectType": t.string().optional(),
            "linkedPeopleResourceNames": t.array(t.string()).optional(),
            "previousResourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonMetadataOut"])
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
    types["BatchCreateContactsResponseIn"] = t.struct(
        {"createdPeople": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["BatchCreateContactsResponseIn"])
    types["BatchCreateContactsResponseOut"] = t.struct(
        {
            "createdPeople": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateContactsResponseOut"])
    types["BatchDeleteContactsRequestIn"] = t.struct(
        {"resourceNames": t.array(t.string())}
    ).named(renames["BatchDeleteContactsRequestIn"])
    types["BatchDeleteContactsRequestOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteContactsRequestOut"])
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
    types["SipAddressIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SipAddressIn"])
    types["SipAddressOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SipAddressOut"])
    types["ListContactGroupsResponseIn"] = t.struct(
        {
            "contactGroups": t.array(t.proxy(renames["ContactGroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
        }
    ).named(renames["ListContactGroupsResponseIn"])
    types["ListContactGroupsResponseOut"] = t.struct(
        {
            "contactGroups": t.array(t.proxy(renames["ContactGroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListContactGroupsResponseOut"])
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
    types["PersonResponseIn"] = t.struct(
        {
            "person": t.proxy(renames["PersonIn"]).optional(),
            "httpStatusCode": t.integer().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "requestedResourceName": t.string().optional(),
        }
    ).named(renames["PersonResponseIn"])
    types["PersonResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "httpStatusCode": t.integer().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "requestedResourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonResponseOut"])
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
    types["ListConnectionsResponseIn"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonIn"])).optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "nextSyncToken": t.string().optional(),
            "totalPeople": t.integer().optional(),
            "connections": t.array(t.proxy(renames["PersonOut"])).optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
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
    types["FieldMetadataIn"] = t.struct(
        {
            "sourcePrimary": t.boolean().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["FieldMetadataIn"])
    types["FieldMetadataOut"] = t.struct(
        {
            "sourcePrimary": t.boolean().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "verified": t.boolean().optional(),
            "primary": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldMetadataOut"])
    types["OrganizationIn"] = t.struct(
        {
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "department": t.string().optional(),
            "symbol": t.string().optional(),
            "jobDescription": t.string().optional(),
            "phoneticName": t.string().optional(),
            "title": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "domain": t.string().optional(),
            "costCenter": t.string().optional(),
        }
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "fullTimeEquivalentMillipercent": t.integer().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "department": t.string().optional(),
            "symbol": t.string().optional(),
            "jobDescription": t.string().optional(),
            "phoneticName": t.string().optional(),
            "title": t.string().optional(),
            "formattedType": t.string().optional(),
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "domain": t.string().optional(),
            "costCenter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["EventIn"] = t.struct(
        {
            "date": t.proxy(renames["DateIn"]).optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "date": t.proxy(renames["DateOut"]).optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["ProfileMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ProfileMetadataIn"]
    )
    types["ProfileMetadataOut"] = t.struct(
        {
            "userTypes": t.array(t.string()).optional(),
            "objectType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileMetadataOut"])
    types["NicknameIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["NicknameIn"])
    types["NicknameOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NicknameOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchUpdateContactsRequestIn"] = t.struct(
        {
            "readMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "contacts": t.struct({"_": t.string().optional()}),
            "updateMask": t.string(),
        }
    ).named(renames["BatchUpdateContactsRequestIn"])
    types["BatchUpdateContactsRequestOut"] = t.struct(
        {
            "readMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "contacts": t.struct({"_": t.string().optional()}),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsRequestOut"])
    types["ContactToCreateIn"] = t.struct(
        {"contactPerson": t.proxy(renames["PersonIn"])}
    ).named(renames["ContactToCreateIn"])
    types["ContactToCreateOut"] = t.struct(
        {
            "contactPerson": t.proxy(renames["PersonOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactToCreateOut"])
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
    types["ExternalIdIn"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["ExternalIdIn"])
    types["ExternalIdOut"] = t.struct(
        {
            "value": t.string().optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalIdOut"])
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
    types["EmailAddressIn"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["EmailAddressIn"])
    types["EmailAddressOut"] = t.struct(
        {
            "type": t.string().optional(),
            "value": t.string().optional(),
            "displayName": t.string().optional(),
            "formattedType": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailAddressOut"])
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
    types["GetPeopleResponseIn"] = t.struct(
        {"responses": t.array(t.proxy(renames["PersonResponseIn"])).optional()}
    ).named(renames["GetPeopleResponseIn"])
    types["GetPeopleResponseOut"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["PersonResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPeopleResponseOut"])
    types["CalendarUrlIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "url": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CalendarUrlIn"])
    types["CalendarUrlOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "url": t.string().optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarUrlOut"])
    types["MembershipIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "contactGroupMembership": t.proxy(
                renames["ContactGroupMembershipIn"]
            ).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "domainMembership": t.proxy(renames["DomainMembershipOut"]).optional(),
            "contactGroupMembership": t.proxy(
                renames["ContactGroupMembershipOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["UpdateContactPhotoRequestIn"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "photoBytes": t.string(),
            "personFields": t.string().optional(),
        }
    ).named(renames["UpdateContactPhotoRequestIn"])
    types["UpdateContactPhotoRequestOut"] = t.struct(
        {
            "sources": t.array(t.string()).optional(),
            "photoBytes": t.string(),
            "personFields": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoRequestOut"])
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
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["ResidenceIn"])
    types["ResidenceOut"] = t.struct(
        {
            "current": t.boolean().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResidenceOut"])
    types["RelationIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "type": t.string().optional(),
            "person": t.string().optional(),
        }
    ).named(renames["RelationIn"])
    types["RelationOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "type": t.string().optional(),
            "person": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationOut"])
    types["ImClientIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "type": t.string().optional(),
            "username": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["ImClientIn"])
    types["ImClientOut"] = t.struct(
        {
            "formattedProtocol": t.string().optional(),
            "protocol": t.string().optional(),
            "type": t.string().optional(),
            "username": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImClientOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["UpdateContactPhotoResponseIn"] = t.struct(
        {"person": t.proxy(renames["PersonIn"]).optional()}
    ).named(renames["UpdateContactPhotoResponseIn"])
    types["UpdateContactPhotoResponseOut"] = t.struct(
        {
            "person": t.proxy(renames["PersonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateContactPhotoResponseOut"])
    types["AddressIn"] = t.struct(
        {
            "region": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "city": t.string().optional(),
            "poBox": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "streetAddress": t.string().optional(),
            "type": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "formattedValue": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "formattedType": t.string().optional(),
            "region": t.string().optional(),
            "extendedAddress": t.string().optional(),
            "countryCode": t.string().optional(),
            "city": t.string().optional(),
            "poBox": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "streetAddress": t.string().optional(),
            "type": t.string().optional(),
            "country": t.string().optional(),
            "postalCode": t.string().optional(),
            "formattedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["PhoneNumberIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["PhoneNumberIn"])
    types["PhoneNumberOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "value": t.string().optional(),
            "canonicalForm": t.string().optional(),
            "type": t.string().optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumberOut"])
    types["BatchUpdateContactsResponseIn"] = t.struct(
        {"updateResult": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BatchUpdateContactsResponseIn"])
    types["BatchUpdateContactsResponseOut"] = t.struct(
        {
            "updateResult": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateContactsResponseOut"])
    types["PhotoIn"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "default": t.boolean().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "default": t.boolean().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["PersonIn"] = t.struct(
        {
            "fileAses": t.array(t.proxy(renames["FileAsIn"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlIn"])).optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdIn"])).optional(),
            "names": t.array(t.proxy(renames["NameIn"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayIn"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceIn"])).optional(),
            "skills": t.array(t.proxy(renames["SkillIn"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordIn"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressIn"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientIn"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedIn"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameIn"])).optional(),
            "genders": t.array(t.proxy(renames["GenderIn"])).optional(),
            "events": t.array(t.proxy(renames["EventIn"])).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataIn"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "urls": t.array(t.proxy(renames["UrlIn"])).optional(),
            "resourceName": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "biographies": t.array(t.proxy(renames["BiographyIn"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressIn"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberIn"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleIn"])).optional(),
            "interests": t.array(t.proxy(renames["InterestIn"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsIn"])).optional(),
            "relations": t.array(t.proxy(renames["RelationIn"])).optional(),
            "etag": t.string().optional(),
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationIn"])).optional(),
        }
    ).named(renames["PersonIn"])
    types["PersonOut"] = t.struct(
        {
            "fileAses": t.array(t.proxy(renames["FileAsOut"])).optional(),
            "calendarUrls": t.array(t.proxy(renames["CalendarUrlOut"])).optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "metadata": t.proxy(renames["PersonMetadataOut"]).optional(),
            "externalIds": t.array(t.proxy(renames["ExternalIdOut"])).optional(),
            "names": t.array(t.proxy(renames["NameOut"])).optional(),
            "birthdays": t.array(t.proxy(renames["BirthdayOut"])).optional(),
            "residences": t.array(t.proxy(renames["ResidenceOut"])).optional(),
            "ageRange": t.string().optional(),
            "skills": t.array(t.proxy(renames["SkillOut"])).optional(),
            "miscKeywords": t.array(t.proxy(renames["MiscKeywordOut"])).optional(),
            "ageRanges": t.array(t.proxy(renames["AgeRangeTypeOut"])).optional(),
            "sipAddresses": t.array(t.proxy(renames["SipAddressOut"])).optional(),
            "imClients": t.array(t.proxy(renames["ImClientOut"])).optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "userDefined": t.array(t.proxy(renames["UserDefinedOut"])).optional(),
            "nicknames": t.array(t.proxy(renames["NicknameOut"])).optional(),
            "genders": t.array(t.proxy(renames["GenderOut"])).optional(),
            "events": t.array(t.proxy(renames["EventOut"])).optional(),
            "relationshipStatuses": t.array(
                t.proxy(renames["RelationshipStatusOut"])
            ).optional(),
            "clientData": t.array(t.proxy(renames["ClientDataOut"])).optional(),
            "addresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "urls": t.array(t.proxy(renames["UrlOut"])).optional(),
            "resourceName": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "relationshipInterests": t.array(
                t.proxy(renames["RelationshipInterestOut"])
            ).optional(),
            "biographies": t.array(t.proxy(renames["BiographyOut"])).optional(),
            "emailAddresses": t.array(t.proxy(renames["EmailAddressOut"])).optional(),
            "phoneNumbers": t.array(t.proxy(renames["PhoneNumberOut"])).optional(),
            "taglines": t.array(t.proxy(renames["TaglineOut"])).optional(),
            "locales": t.array(t.proxy(renames["LocaleOut"])).optional(),
            "interests": t.array(t.proxy(renames["InterestOut"])).optional(),
            "braggingRights": t.array(t.proxy(renames["BraggingRightsOut"])).optional(),
            "relations": t.array(t.proxy(renames["RelationOut"])).optional(),
            "etag": t.string().optional(),
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "coverPhotos": t.array(t.proxy(renames["CoverPhotoOut"])).optional(),
            "occupations": t.array(t.proxy(renames["OccupationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonOut"])
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
    types["SourceIn"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "profileMetadata": t.proxy(renames["ProfileMetadataOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ListOtherContactsResponseIn"] = t.struct(
        {
            "otherContacts": t.array(t.proxy(renames["PersonIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
        }
    ).named(renames["ListOtherContactsResponseIn"])
    types["ListOtherContactsResponseOut"] = t.struct(
        {
            "otherContacts": t.array(t.proxy(renames["PersonOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "nextSyncToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOtherContactsResponseOut"])
    types["MiscKeywordIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["MiscKeywordIn"])
    types["MiscKeywordOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MiscKeywordOut"])
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
    types["ContactGroupIn"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataIn"])).optional(),
        }
    ).named(renames["ContactGroupIn"])
    types["ContactGroupOut"] = t.struct(
        {
            "formattedName": t.string().optional(),
            "groupType": t.string().optional(),
            "resourceName": t.string().optional(),
            "name": t.string().optional(),
            "memberCount": t.integer().optional(),
            "memberResourceNames": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["ContactGroupMetadataOut"]).optional(),
            "etag": t.string().optional(),
            "clientData": t.array(t.proxy(renames["GroupClientDataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactGroupOut"])
    types["LocationIn"] = t.struct(
        {
            "buildingId": t.string().optional(),
            "current": t.boolean().optional(),
            "type": t.string().optional(),
            "floorSection": t.string().optional(),
            "floor": t.string().optional(),
            "deskCode": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "buildingId": t.string().optional(),
            "current": t.boolean().optional(),
            "type": t.string().optional(),
            "floorSection": t.string().optional(),
            "floor": t.string().optional(),
            "deskCode": t.string().optional(),
            "value": t.string().optional(),
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
            "metadata": t.proxy(renames["FieldMetadataOut"]).optional(),
            "formattedType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlOut"])
    types["CopyOtherContactToMyContactsGroupRequestIn"] = t.struct(
        {
            "readMask": t.string().optional(),
            "copyMask": t.string(),
            "sources": t.array(t.string()).optional(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestIn"])
    types["CopyOtherContactToMyContactsGroupRequestOut"] = t.struct(
        {
            "readMask": t.string().optional(),
            "copyMask": t.string(),
            "sources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CopyOtherContactToMyContactsGroupRequestOut"])

    functions = {}
    functions["contactGroupsGet"] = people.get(
        "v1/contactGroups",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
                "syncToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "groupFields": t.string().optional(),
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
    functions["peopleCreateContact"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchDeleteContacts"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContact"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleListDirectoryPeople"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchUpdateContacts"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGetBatchGet"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleBatchCreateContacts"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContact"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleGet"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchDirectoryPeople"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleUpdateContactPhoto"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleDeleteContactPhoto"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleSearchContacts"] = people.get(
        "v1/people:searchContacts",
        t.struct(
            {
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["peopleConnectionsList"] = people.get(
        "v1/{resourceName}/connections",
        t.struct(
            {
                "sortOrder": t.string().optional(),
                "personFields": t.string(),
                "resourceName": t.string(),
                "syncToken": t.string().optional(),
                "requestMask.includeField": t.string(),
                "requestSyncToken": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "sources": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListConnectionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["otherContactsList"] = people.post(
        "v1/{resourceName}:copyOtherContactToMyContactsGroup",
        t.struct(
            {
                "resourceName": t.string(),
                "readMask": t.string().optional(),
                "copyMask": t.string(),
                "sources": t.array(t.string()).optional(),
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
                "readMask": t.string().optional(),
                "copyMask": t.string(),
                "sources": t.array(t.string()).optional(),
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
                "readMask": t.string().optional(),
                "copyMask": t.string(),
                "sources": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PersonOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="people", renames=renames, types=Box(types), functions=Box(functions)
    )
