from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinessbusinessinformation() -> Import:
    mybusinessbusinessinformation = HTTPRuntime(
        "https://mybusinessbusinessinformation.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinessinformation_1_ErrorResponse",
        "OpenInfoIn": "_mybusinessbusinessinformation_2_OpenInfoIn",
        "OpenInfoOut": "_mybusinessbusinessinformation_3_OpenInfoOut",
        "GoogleLocationIn": "_mybusinessbusinessinformation_4_GoogleLocationIn",
        "GoogleLocationOut": "_mybusinessbusinessinformation_5_GoogleLocationOut",
        "SearchChainsResponseIn": "_mybusinessbusinessinformation_6_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusinessbusinessinformation_7_SearchChainsResponseOut",
        "AssociateLocationRequestIn": "_mybusinessbusinessinformation_8_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusinessbusinessinformation_9_AssociateLocationRequestOut",
        "PlacesIn": "_mybusinessbusinessinformation_10_PlacesIn",
        "PlacesOut": "_mybusinessbusinessinformation_11_PlacesOut",
        "RepeatedEnumAttributeValueIn": "_mybusinessbusinessinformation_12_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusinessbusinessinformation_13_RepeatedEnumAttributeValueOut",
        "MetadataIn": "_mybusinessbusinessinformation_14_MetadataIn",
        "MetadataOut": "_mybusinessbusinessinformation_15_MetadataOut",
        "AttributeMetadataIn": "_mybusinessbusinessinformation_16_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusinessbusinessinformation_17_AttributeMetadataOut",
        "ListLocationsResponseIn": "_mybusinessbusinessinformation_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusinessbusinessinformation_19_ListLocationsResponseOut",
        "TimePeriodIn": "_mybusinessbusinessinformation_20_TimePeriodIn",
        "TimePeriodOut": "_mybusinessbusinessinformation_21_TimePeriodOut",
        "SearchGoogleLocationsRequestIn": "_mybusinessbusinessinformation_22_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusinessbusinessinformation_23_SearchGoogleLocationsRequestOut",
        "UriAttributeValueIn": "_mybusinessbusinessinformation_24_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusinessbusinessinformation_25_UriAttributeValueOut",
        "AttributesIn": "_mybusinessbusinessinformation_26_AttributesIn",
        "AttributesOut": "_mybusinessbusinessinformation_27_AttributesOut",
        "ClearLocationAssociationRequestIn": "_mybusinessbusinessinformation_28_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusinessbusinessinformation_29_ClearLocationAssociationRequestOut",
        "ListAttributeMetadataResponseIn": "_mybusinessbusinessinformation_30_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusinessbusinessinformation_31_ListAttributeMetadataResponseOut",
        "RelationshipDataIn": "_mybusinessbusinessinformation_32_RelationshipDataIn",
        "RelationshipDataOut": "_mybusinessbusinessinformation_33_RelationshipDataOut",
        "MoneyIn": "_mybusinessbusinessinformation_34_MoneyIn",
        "MoneyOut": "_mybusinessbusinessinformation_35_MoneyOut",
        "ChainUriIn": "_mybusinessbusinessinformation_36_ChainUriIn",
        "ChainUriOut": "_mybusinessbusinessinformation_37_ChainUriOut",
        "ChainIn": "_mybusinessbusinessinformation_38_ChainIn",
        "ChainOut": "_mybusinessbusinessinformation_39_ChainOut",
        "BatchGetCategoriesResponseIn": "_mybusinessbusinessinformation_40_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusinessbusinessinformation_41_BatchGetCategoriesResponseOut",
        "SpecialHourPeriodIn": "_mybusinessbusinessinformation_42_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusinessbusinessinformation_43_SpecialHourPeriodOut",
        "LocationIn": "_mybusinessbusinessinformation_44_LocationIn",
        "LocationOut": "_mybusinessbusinessinformation_45_LocationOut",
        "MoreHoursTypeIn": "_mybusinessbusinessinformation_46_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusinessbusinessinformation_47_MoreHoursTypeOut",
        "SpecialHoursIn": "_mybusinessbusinessinformation_48_SpecialHoursIn",
        "SpecialHoursOut": "_mybusinessbusinessinformation_49_SpecialHoursOut",
        "FreeFormServiceItemIn": "_mybusinessbusinessinformation_50_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusinessbusinessinformation_51_FreeFormServiceItemOut",
        "ChainNameIn": "_mybusinessbusinessinformation_52_ChainNameIn",
        "ChainNameOut": "_mybusinessbusinessinformation_53_ChainNameOut",
        "ServiceTypeIn": "_mybusinessbusinessinformation_54_ServiceTypeIn",
        "ServiceTypeOut": "_mybusinessbusinessinformation_55_ServiceTypeOut",
        "LatLngIn": "_mybusinessbusinessinformation_56_LatLngIn",
        "LatLngOut": "_mybusinessbusinessinformation_57_LatLngOut",
        "ProfileIn": "_mybusinessbusinessinformation_58_ProfileIn",
        "ProfileOut": "_mybusinessbusinessinformation_59_ProfileOut",
        "ServiceItemIn": "_mybusinessbusinessinformation_60_ServiceItemIn",
        "ServiceItemOut": "_mybusinessbusinessinformation_61_ServiceItemOut",
        "ServiceAreaBusinessIn": "_mybusinessbusinessinformation_62_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusinessbusinessinformation_63_ServiceAreaBusinessOut",
        "PhoneNumbersIn": "_mybusinessbusinessinformation_64_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusinessbusinessinformation_65_PhoneNumbersOut",
        "AttributeIn": "_mybusinessbusinessinformation_66_AttributeIn",
        "AttributeOut": "_mybusinessbusinessinformation_67_AttributeOut",
        "EmptyIn": "_mybusinessbusinessinformation_68_EmptyIn",
        "EmptyOut": "_mybusinessbusinessinformation_69_EmptyOut",
        "ListCategoriesResponseIn": "_mybusinessbusinessinformation_70_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusinessbusinessinformation_71_ListCategoriesResponseOut",
        "AttributeValueMetadataIn": "_mybusinessbusinessinformation_72_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusinessbusinessinformation_73_AttributeValueMetadataOut",
        "AdWordsLocationExtensionsIn": "_mybusinessbusinessinformation_74_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusinessbusinessinformation_75_AdWordsLocationExtensionsOut",
        "LabelIn": "_mybusinessbusinessinformation_76_LabelIn",
        "LabelOut": "_mybusinessbusinessinformation_77_LabelOut",
        "MoreHoursIn": "_mybusinessbusinessinformation_78_MoreHoursIn",
        "MoreHoursOut": "_mybusinessbusinessinformation_79_MoreHoursOut",
        "CategoriesIn": "_mybusinessbusinessinformation_80_CategoriesIn",
        "CategoriesOut": "_mybusinessbusinessinformation_81_CategoriesOut",
        "TimeOfDayIn": "_mybusinessbusinessinformation_82_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinessbusinessinformation_83_TimeOfDayOut",
        "DateIn": "_mybusinessbusinessinformation_84_DateIn",
        "DateOut": "_mybusinessbusinessinformation_85_DateOut",
        "PostalAddressIn": "_mybusinessbusinessinformation_86_PostalAddressIn",
        "PostalAddressOut": "_mybusinessbusinessinformation_87_PostalAddressOut",
        "SearchGoogleLocationsResponseIn": "_mybusinessbusinessinformation_88_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusinessbusinessinformation_89_SearchGoogleLocationsResponseOut",
        "StructuredServiceItemIn": "_mybusinessbusinessinformation_90_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusinessbusinessinformation_91_StructuredServiceItemOut",
        "CategoryIn": "_mybusinessbusinessinformation_92_CategoryIn",
        "CategoryOut": "_mybusinessbusinessinformation_93_CategoryOut",
        "BusinessHoursIn": "_mybusinessbusinessinformation_94_BusinessHoursIn",
        "BusinessHoursOut": "_mybusinessbusinessinformation_95_BusinessHoursOut",
        "GoogleUpdatedLocationIn": "_mybusinessbusinessinformation_96_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusinessbusinessinformation_97_GoogleUpdatedLocationOut",
        "PlaceInfoIn": "_mybusinessbusinessinformation_98_PlaceInfoIn",
        "PlaceInfoOut": "_mybusinessbusinessinformation_99_PlaceInfoOut",
        "RelevantLocationIn": "_mybusinessbusinessinformation_100_RelevantLocationIn",
        "RelevantLocationOut": "_mybusinessbusinessinformation_101_RelevantLocationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OpenInfoIn"] = t.struct(
        {"openingDate": t.proxy(renames["DateIn"]).optional(), "status": t.string()}
    ).named(renames["OpenInfoIn"])
    types["OpenInfoOut"] = t.struct(
        {
            "openingDate": t.proxy(renames["DateOut"]).optional(),
            "canReopen": t.boolean().optional(),
            "status": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenInfoOut"])
    types["GoogleLocationIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "name": t.string().optional(),
            "requestAdminRightsUri": t.string().optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "name": t.string().optional(),
            "requestAdminRightsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
    types["RepeatedEnumAttributeValueIn"] = t.struct(
        {
            "unsetValues": t.array(t.string()).optional(),
            "setValues": t.array(t.string()).optional(),
        }
    ).named(renames["RepeatedEnumAttributeValueIn"])
    types["RepeatedEnumAttributeValueOut"] = t.struct(
        {
            "unsetValues": t.array(t.string()).optional(),
            "setValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatedEnumAttributeValueOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "duplicateLocation": t.string().optional(),
            "canDelete": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "placeId": t.string().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["AttributeMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "deprecated": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "repeatable": t.boolean().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "deprecated": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
            "parent": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["TimePeriodIn"] = t.struct(
        {
            "openDay": t.string(),
            "closeDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "openDay": t.string(),
            "closeDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["SearchGoogleLocationsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestIn"])
    types["SearchGoogleLocationsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "query": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestOut"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["AttributesIn"] = t.struct(
        {
            "attributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
            "name": t.string(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "attributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
    types["ListAttributeMetadataResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attributeMetadata": t.array(
                t.proxy(renames["AttributeMetadataIn"])
            ).optional(),
        }
    ).named(renames["ListAttributeMetadataResponseIn"])
    types["ListAttributeMetadataResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attributeMetadata": t.array(
                t.proxy(renames["AttributeMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttributeMetadataResponseOut"])
    types["RelationshipDataIn"] = t.struct(
        {
            "parentChain": t.string().optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationIn"])
            ).optional(),
            "parentLocation": t.proxy(renames["RelevantLocationIn"]).optional(),
        }
    ).named(renames["RelationshipDataIn"])
    types["RelationshipDataOut"] = t.struct(
        {
            "parentChain": t.string().optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationOut"])
            ).optional(),
            "parentLocation": t.proxy(renames["RelevantLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDataOut"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
    types["ChainIn"] = t.struct(
        {
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "locationCount": t.integer().optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "locationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "closed": t.boolean().optional(),
            "startDate": t.proxy(renames["DateIn"]),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "closed": t.boolean().optional(),
            "startDate": t.proxy(renames["DateOut"]),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
    types["LocationIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "title": t.string(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "websiteUri": t.string().optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "name": t.string().optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "labels": t.array(t.string()).optional(),
            "storeCode": t.string().optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "title": t.string(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "websiteUri": t.string().optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "name": t.string().optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "labels": t.array(t.string()).optional(),
            "storeCode": t.string().optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["MoreHoursTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoreHoursTypeIn"]
    )
    types["MoreHoursTypeOut"] = t.struct(
        {
            "localizedDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "hoursTypeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursTypeOut"])
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
    types["FreeFormServiceItemIn"] = t.struct(
        {"label": t.proxy(renames["LabelIn"]), "category": t.string()}
    ).named(renames["FreeFormServiceItemIn"])
    types["FreeFormServiceItemOut"] = t.struct(
        {
            "label": t.proxy(renames["LabelOut"]),
            "category": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeFormServiceItemOut"])
    types["ChainNameIn"] = t.struct(
        {"languageCode": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["ChainNameIn"])
    types["ChainNameOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainNameOut"])
    types["ServiceTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ServiceTypeIn"]
    )
    types["ServiceTypeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "serviceTypeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceTypeOut"])
    types["LatLngIn"] = t.struct(
        {"latitude": t.number().optional(), "longitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["ServiceItemIn"] = t.struct(
        {
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemIn"]
            ).optional(),
            "freeFormServiceItem": t.proxy(renames["FreeFormServiceItemIn"]).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["ServiceItemIn"])
    types["ServiceItemOut"] = t.struct(
        {
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemOut"]
            ).optional(),
            "freeFormServiceItem": t.proxy(
                renames["FreeFormServiceItemOut"]
            ).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceItemOut"])
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "places": t.proxy(renames["PlacesIn"]).optional(),
            "businessType": t.string(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "businessType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
    types["PhoneNumbersIn"] = t.struct(
        {"primaryPhone": t.string(), "additionalPhones": t.array(t.string()).optional()}
    ).named(renames["PhoneNumbersIn"])
    types["PhoneNumbersOut"] = t.struct(
        {
            "primaryPhone": t.string(),
            "additionalPhones": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumbersOut"])
    types["AttributeIn"] = t.struct(
        {
            "uriValues": t.array(t.proxy(renames["UriAttributeValueIn"])).optional(),
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueIn"]
            ).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "valueType": t.string().optional(),
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListCategoriesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
        }
    ).named(renames["ListCategoriesResponseIn"])
    types["ListCategoriesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCategoriesResponseOut"])
    types["AttributeValueMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AttributeValueMetadataIn"])
    types["AttributeValueMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeValueMetadataOut"])
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
    types["LabelIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "displayName": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["MoreHoursIn"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodIn"])),
            "hoursTypeId": t.string(),
        }
    ).named(renames["MoreHoursIn"])
    types["MoreHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "hoursTypeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursOut"])
    types["CategoriesIn"] = t.struct(
        {
            "primaryCategory": t.proxy(renames["CategoryIn"]),
            "additionalCategories": t.array(t.proxy(renames["CategoryIn"])).optional(),
        }
    ).named(renames["CategoriesIn"])
    types["CategoriesOut"] = t.struct(
        {
            "primaryCategory": t.proxy(renames["CategoryOut"]),
            "additionalCategories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoriesOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "locality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "locality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["SearchGoogleLocationsResponseIn"] = t.struct(
        {"googleLocations": t.array(t.proxy(renames["GoogleLocationIn"])).optional()}
    ).named(renames["SearchGoogleLocationsResponseIn"])
    types["SearchGoogleLocationsResponseOut"] = t.struct(
        {
            "googleLocations": t.array(
                t.proxy(renames["GoogleLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsResponseOut"])
    types["StructuredServiceItemIn"] = t.struct(
        {"description": t.string().optional(), "serviceTypeId": t.string()}
    ).named(renames["StructuredServiceItemIn"])
    types["StructuredServiceItemOut"] = t.struct(
        {
            "description": t.string().optional(),
            "serviceTypeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredServiceItemOut"])
    types["CategoryIn"] = t.struct({"name": t.string()}).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "moreHoursTypes": t.array(t.proxy(renames["MoreHoursTypeOut"])).optional(),
            "name": t.string(),
            "serviceTypes": t.array(t.proxy(renames["ServiceTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
    types["GoogleUpdatedLocationIn"] = t.struct(
        {
            "diffMask": t.string().optional(),
            "pendingMask": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationIn"])
    types["GoogleUpdatedLocationOut"] = t.struct(
        {
            "diffMask": t.string().optional(),
            "pendingMask": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationOut"])
    types["PlaceInfoIn"] = t.struct(
        {"placeName": t.string(), "placeId": t.string()}
    ).named(renames["PlaceInfoIn"])
    types["PlaceInfoOut"] = t.struct(
        {
            "placeName": t.string(),
            "placeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceInfoOut"])
    types["RelevantLocationIn"] = t.struct(
        {"relationType": t.string(), "placeId": t.string()}
    ).named(renames["RelevantLocationIn"])
    types["RelevantLocationOut"] = t.struct(
        {
            "relationType": t.string(),
            "placeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelevantLocationOut"])

    functions = {}
    functions["attributesList"] = mybusinessbusinessinformation.get(
        "v1/attributes",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "regionCode": t.string().optional(),
                "categoryName": t.string().optional(),
                "showAll": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsCreate"] = mybusinessbusinessinformation.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsList"] = mybusinessbusinessinformation.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetAttributes"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPatch"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAssociate"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetGoogleUpdated"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsClearLocationAssociation"] = mybusinessbusinessinformation.post(
        "v1/{name}:clearLocationAssociation",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "locationsAttributesGetGoogleUpdated"
    ] = mybusinessbusinessinformation.get(
        "v1/{name}:getGoogleUpdated",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesList"] = mybusinessbusinessinformation.get(
        "v1/categories:batchGet",
        t.struct(
            {
                "languageCode": t.string(),
                "view": t.string(),
                "names": t.string(),
                "regionCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesBatchGet"] = mybusinessbusinessinformation.get(
        "v1/categories:batchGet",
        t.struct(
            {
                "languageCode": t.string(),
                "view": t.string(),
                "names": t.string(),
                "regionCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleLocationsSearch"] = mybusinessbusinessinformation.post(
        "v1/googleLocations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "location": t.proxy(renames["LocationIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGoogleLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["chainsSearch"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["chainsGet"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessbusinessinformation",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
