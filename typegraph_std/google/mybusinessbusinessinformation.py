from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessbusinessinformation() -> Import:
    mybusinessbusinessinformation = HTTPRuntime(
        "https://mybusinessbusinessinformation.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinessinformation_1_ErrorResponse",
        "LocationIn": "_mybusinessbusinessinformation_2_LocationIn",
        "LocationOut": "_mybusinessbusinessinformation_3_LocationOut",
        "DateIn": "_mybusinessbusinessinformation_4_DateIn",
        "DateOut": "_mybusinessbusinessinformation_5_DateOut",
        "AttributeMetadataIn": "_mybusinessbusinessinformation_6_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusinessbusinessinformation_7_AttributeMetadataOut",
        "OpenInfoIn": "_mybusinessbusinessinformation_8_OpenInfoIn",
        "OpenInfoOut": "_mybusinessbusinessinformation_9_OpenInfoOut",
        "SearchGoogleLocationsResponseIn": "_mybusinessbusinessinformation_10_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusinessbusinessinformation_11_SearchGoogleLocationsResponseOut",
        "SpecialHourPeriodIn": "_mybusinessbusinessinformation_12_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusinessbusinessinformation_13_SpecialHourPeriodOut",
        "PhoneNumbersIn": "_mybusinessbusinessinformation_14_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusinessbusinessinformation_15_PhoneNumbersOut",
        "ChainUriIn": "_mybusinessbusinessinformation_16_ChainUriIn",
        "ChainUriOut": "_mybusinessbusinessinformation_17_ChainUriOut",
        "TimePeriodIn": "_mybusinessbusinessinformation_18_TimePeriodIn",
        "TimePeriodOut": "_mybusinessbusinessinformation_19_TimePeriodOut",
        "StructuredServiceItemIn": "_mybusinessbusinessinformation_20_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusinessbusinessinformation_21_StructuredServiceItemOut",
        "ChainNameIn": "_mybusinessbusinessinformation_22_ChainNameIn",
        "ChainNameOut": "_mybusinessbusinessinformation_23_ChainNameOut",
        "RelationshipDataIn": "_mybusinessbusinessinformation_24_RelationshipDataIn",
        "RelationshipDataOut": "_mybusinessbusinessinformation_25_RelationshipDataOut",
        "ServiceItemIn": "_mybusinessbusinessinformation_26_ServiceItemIn",
        "ServiceItemOut": "_mybusinessbusinessinformation_27_ServiceItemOut",
        "MoreHoursIn": "_mybusinessbusinessinformation_28_MoreHoursIn",
        "MoreHoursOut": "_mybusinessbusinessinformation_29_MoreHoursOut",
        "ClearLocationAssociationRequestIn": "_mybusinessbusinessinformation_30_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusinessbusinessinformation_31_ClearLocationAssociationRequestOut",
        "SpecialHoursIn": "_mybusinessbusinessinformation_32_SpecialHoursIn",
        "SpecialHoursOut": "_mybusinessbusinessinformation_33_SpecialHoursOut",
        "SearchChainsResponseIn": "_mybusinessbusinessinformation_34_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusinessbusinessinformation_35_SearchChainsResponseOut",
        "RepeatedEnumAttributeValueIn": "_mybusinessbusinessinformation_36_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusinessbusinessinformation_37_RepeatedEnumAttributeValueOut",
        "ServiceAreaBusinessIn": "_mybusinessbusinessinformation_38_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusinessbusinessinformation_39_ServiceAreaBusinessOut",
        "ProfileIn": "_mybusinessbusinessinformation_40_ProfileIn",
        "ProfileOut": "_mybusinessbusinessinformation_41_ProfileOut",
        "AssociateLocationRequestIn": "_mybusinessbusinessinformation_42_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusinessbusinessinformation_43_AssociateLocationRequestOut",
        "FreeFormServiceItemIn": "_mybusinessbusinessinformation_44_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusinessbusinessinformation_45_FreeFormServiceItemOut",
        "GoogleLocationIn": "_mybusinessbusinessinformation_46_GoogleLocationIn",
        "GoogleLocationOut": "_mybusinessbusinessinformation_47_GoogleLocationOut",
        "EmptyIn": "_mybusinessbusinessinformation_48_EmptyIn",
        "EmptyOut": "_mybusinessbusinessinformation_49_EmptyOut",
        "CategoryIn": "_mybusinessbusinessinformation_50_CategoryIn",
        "CategoryOut": "_mybusinessbusinessinformation_51_CategoryOut",
        "ServiceTypeIn": "_mybusinessbusinessinformation_52_ServiceTypeIn",
        "ServiceTypeOut": "_mybusinessbusinessinformation_53_ServiceTypeOut",
        "MoneyIn": "_mybusinessbusinessinformation_54_MoneyIn",
        "MoneyOut": "_mybusinessbusinessinformation_55_MoneyOut",
        "PlacesIn": "_mybusinessbusinessinformation_56_PlacesIn",
        "PlacesOut": "_mybusinessbusinessinformation_57_PlacesOut",
        "CategoriesIn": "_mybusinessbusinessinformation_58_CategoriesIn",
        "CategoriesOut": "_mybusinessbusinessinformation_59_CategoriesOut",
        "BatchGetCategoriesResponseIn": "_mybusinessbusinessinformation_60_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusinessbusinessinformation_61_BatchGetCategoriesResponseOut",
        "AttributeValueMetadataIn": "_mybusinessbusinessinformation_62_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusinessbusinessinformation_63_AttributeValueMetadataOut",
        "TimeOfDayIn": "_mybusinessbusinessinformation_64_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinessbusinessinformation_65_TimeOfDayOut",
        "ListCategoriesResponseIn": "_mybusinessbusinessinformation_66_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusinessbusinessinformation_67_ListCategoriesResponseOut",
        "GoogleUpdatedLocationIn": "_mybusinessbusinessinformation_68_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusinessbusinessinformation_69_GoogleUpdatedLocationOut",
        "AttributesIn": "_mybusinessbusinessinformation_70_AttributesIn",
        "AttributesOut": "_mybusinessbusinessinformation_71_AttributesOut",
        "SearchGoogleLocationsRequestIn": "_mybusinessbusinessinformation_72_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusinessbusinessinformation_73_SearchGoogleLocationsRequestOut",
        "AdWordsLocationExtensionsIn": "_mybusinessbusinessinformation_74_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusinessbusinessinformation_75_AdWordsLocationExtensionsOut",
        "RelevantLocationIn": "_mybusinessbusinessinformation_76_RelevantLocationIn",
        "RelevantLocationOut": "_mybusinessbusinessinformation_77_RelevantLocationOut",
        "MoreHoursTypeIn": "_mybusinessbusinessinformation_78_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusinessbusinessinformation_79_MoreHoursTypeOut",
        "ChainIn": "_mybusinessbusinessinformation_80_ChainIn",
        "ChainOut": "_mybusinessbusinessinformation_81_ChainOut",
        "LabelIn": "_mybusinessbusinessinformation_82_LabelIn",
        "LabelOut": "_mybusinessbusinessinformation_83_LabelOut",
        "LatLngIn": "_mybusinessbusinessinformation_84_LatLngIn",
        "LatLngOut": "_mybusinessbusinessinformation_85_LatLngOut",
        "BusinessHoursIn": "_mybusinessbusinessinformation_86_BusinessHoursIn",
        "BusinessHoursOut": "_mybusinessbusinessinformation_87_BusinessHoursOut",
        "ListAttributeMetadataResponseIn": "_mybusinessbusinessinformation_88_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusinessbusinessinformation_89_ListAttributeMetadataResponseOut",
        "UriAttributeValueIn": "_mybusinessbusinessinformation_90_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusinessbusinessinformation_91_UriAttributeValueOut",
        "PlaceInfoIn": "_mybusinessbusinessinformation_92_PlaceInfoIn",
        "PlaceInfoOut": "_mybusinessbusinessinformation_93_PlaceInfoOut",
        "PostalAddressIn": "_mybusinessbusinessinformation_94_PostalAddressIn",
        "PostalAddressOut": "_mybusinessbusinessinformation_95_PostalAddressOut",
        "AttributeIn": "_mybusinessbusinessinformation_96_AttributeIn",
        "AttributeOut": "_mybusinessbusinessinformation_97_AttributeOut",
        "MetadataIn": "_mybusinessbusinessinformation_98_MetadataIn",
        "MetadataOut": "_mybusinessbusinessinformation_99_MetadataOut",
        "ListLocationsResponseIn": "_mybusinessbusinessinformation_100_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusinessbusinessinformation_101_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LocationIn"] = t.struct(
        {
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "labels": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "websiteUri": t.string().optional(),
            "title": t.string(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "name": t.string().optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "storeCode": t.string().optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "labels": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "languageCode": t.string().optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "websiteUri": t.string().optional(),
            "title": t.string(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "name": t.string().optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "storeCode": t.string().optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["AttributeMetadataIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "displayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "displayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
    types["OpenInfoIn"] = t.struct(
        {"openingDate": t.proxy(renames["DateIn"]).optional(), "status": t.string()}
    ).named(renames["OpenInfoIn"])
    types["OpenInfoOut"] = t.struct(
        {
            "canReopen": t.boolean().optional(),
            "openingDate": t.proxy(renames["DateOut"]).optional(),
            "status": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenInfoOut"])
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
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
    types["PhoneNumbersIn"] = t.struct(
        {"additionalPhones": t.array(t.string()).optional(), "primaryPhone": t.string()}
    ).named(renames["PhoneNumbersIn"])
    types["PhoneNumbersOut"] = t.struct(
        {
            "additionalPhones": t.array(t.string()).optional(),
            "primaryPhone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhoneNumbersOut"])
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
    types["TimePeriodIn"] = t.struct(
        {
            "openTime": t.proxy(renames["TimeOfDayIn"]),
            "openDay": t.string(),
            "closeDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "openDay": t.string(),
            "closeDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["StructuredServiceItemIn"] = t.struct(
        {"serviceTypeId": t.string(), "description": t.string().optional()}
    ).named(renames["StructuredServiceItemIn"])
    types["StructuredServiceItemOut"] = t.struct(
        {
            "serviceTypeId": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructuredServiceItemOut"])
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
    types["ServiceItemIn"] = t.struct(
        {
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemIn"]
            ).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "freeFormServiceItem": t.proxy(renames["FreeFormServiceItemIn"]).optional(),
        }
    ).named(renames["ServiceItemIn"])
    types["ServiceItemOut"] = t.struct(
        {
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemOut"]
            ).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "freeFormServiceItem": t.proxy(
                renames["FreeFormServiceItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceItemOut"])
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
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])
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
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
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
    types["GoogleLocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "requestAdminRightsUri": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "requestAdminRightsUri": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CategoryIn"] = t.struct({"name": t.string()}).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "serviceTypes": t.array(t.proxy(renames["ServiceTypeOut"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "moreHoursTypes": t.array(t.proxy(renames["MoreHoursTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
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
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
    types["AttributeValueMetadataIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AttributeValueMetadataIn"])
    types["AttributeValueMetadataOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeValueMetadataOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["GoogleUpdatedLocationIn"] = t.struct(
        {
            "diffMask": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "pendingMask": t.string().optional(),
        }
    ).named(renames["GoogleUpdatedLocationIn"])
    types["GoogleUpdatedLocationOut"] = t.struct(
        {
            "diffMask": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "pendingMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationOut"])
    types["AttributesIn"] = t.struct(
        {
            "name": t.string(),
            "attributes": t.array(t.proxy(renames["AttributeIn"])).optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "name": t.string(),
            "attributes": t.array(t.proxy(renames["AttributeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["SearchGoogleLocationsRequestIn"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestIn"])
    types["SearchGoogleLocationsRequestOut"] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestOut"])
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
    types["RelevantLocationIn"] = t.struct(
        {"placeId": t.string(), "relationType": t.string()}
    ).named(renames["RelevantLocationIn"])
    types["RelevantLocationOut"] = t.struct(
        {
            "placeId": t.string(),
            "relationType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelevantLocationOut"])
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
    types["ChainIn"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
            "locationCount": t.integer().optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "locationCount": t.integer().optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
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
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
    types["ListAttributeMetadataResponseIn"] = t.struct(
        {
            "attributeMetadata": t.array(
                t.proxy(renames["AttributeMetadataIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAttributeMetadataResponseIn"])
    types["ListAttributeMetadataResponseOut"] = t.struct(
        {
            "attributeMetadata": t.array(
                t.proxy(renames["AttributeMetadataOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttributeMetadataResponseOut"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["PlaceInfoIn"] = t.struct(
        {"placeId": t.string(), "placeName": t.string()}
    ).named(renames["PlaceInfoIn"])
    types["PlaceInfoOut"] = t.struct(
        {
            "placeId": t.string(),
            "placeName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceInfoOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "revision": t.integer().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "revision": t.integer().optional(),
            "administrativeArea": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "languageCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
            "name": t.string(),
            "valueType": t.string().optional(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "canOperateHealthData": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "newReviewUri": t.string().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "placeId": t.string().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "duplicateLocation": t.string().optional(),
            "canDelete": t.boolean().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])

    functions = {}
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
    functions["googleLocationsSearch"] = mybusinessbusinessinformation.post(
        "v1/googleLocations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "location": t.proxy(renames["LocationIn"]).optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGoogleLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["attributesList"] = mybusinessbusinessinformation.get(
        "v1/attributes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "regionCode": t.string().optional(),
                "showAll": t.boolean().optional(),
                "categoryName": t.string().optional(),
                "pageToken": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAssociate"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "locationsClearLocationAssociation"
    ] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetAttributes"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetGoogleUpdated"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPatch"] = mybusinessbusinessinformation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "labels": t.array(t.string()).optional(),
                "languageCode": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "websiteUri": t.string().optional(),
                "title": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
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
    functions["accountsLocationsCreate"] = mybusinessbusinessinformation.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesList"] = mybusinessbusinessinformation.get(
        "v1/categories:batchGet",
        t.struct(
            {
                "regionCode": t.string().optional(),
                "view": t.string(),
                "names": t.string(),
                "languageCode": t.string(),
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
                "regionCode": t.string().optional(),
                "view": t.string(),
                "names": t.string(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessbusinessinformation",
        renames=renames,
        types=types,
        functions=functions,
    )
