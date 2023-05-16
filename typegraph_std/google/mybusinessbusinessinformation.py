from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessbusinessinformation() -> Import:
    mybusinessbusinessinformation = HTTPRuntime(
        "https://mybusinessbusinessinformation.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinessinformation_1_ErrorResponse",
        "ListAttributeMetadataResponseIn": "_mybusinessbusinessinformation_2_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusinessbusinessinformation_3_ListAttributeMetadataResponseOut",
        "PlacesIn": "_mybusinessbusinessinformation_4_PlacesIn",
        "PlacesOut": "_mybusinessbusinessinformation_5_PlacesOut",
        "ClearLocationAssociationRequestIn": "_mybusinessbusinessinformation_6_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusinessbusinessinformation_7_ClearLocationAssociationRequestOut",
        "LocationIn": "_mybusinessbusinessinformation_8_LocationIn",
        "LocationOut": "_mybusinessbusinessinformation_9_LocationOut",
        "LatLngIn": "_mybusinessbusinessinformation_10_LatLngIn",
        "LatLngOut": "_mybusinessbusinessinformation_11_LatLngOut",
        "CategoryIn": "_mybusinessbusinessinformation_12_CategoryIn",
        "CategoryOut": "_mybusinessbusinessinformation_13_CategoryOut",
        "PostalAddressIn": "_mybusinessbusinessinformation_14_PostalAddressIn",
        "PostalAddressOut": "_mybusinessbusinessinformation_15_PostalAddressOut",
        "MoreHoursTypeIn": "_mybusinessbusinessinformation_16_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusinessbusinessinformation_17_MoreHoursTypeOut",
        "OpenInfoIn": "_mybusinessbusinessinformation_18_OpenInfoIn",
        "OpenInfoOut": "_mybusinessbusinessinformation_19_OpenInfoOut",
        "ServiceItemIn": "_mybusinessbusinessinformation_20_ServiceItemIn",
        "ServiceItemOut": "_mybusinessbusinessinformation_21_ServiceItemOut",
        "AttributeValueMetadataIn": "_mybusinessbusinessinformation_22_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusinessbusinessinformation_23_AttributeValueMetadataOut",
        "SpecialHoursIn": "_mybusinessbusinessinformation_24_SpecialHoursIn",
        "SpecialHoursOut": "_mybusinessbusinessinformation_25_SpecialHoursOut",
        "SearchGoogleLocationsResponseIn": "_mybusinessbusinessinformation_26_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusinessbusinessinformation_27_SearchGoogleLocationsResponseOut",
        "ProfileIn": "_mybusinessbusinessinformation_28_ProfileIn",
        "ProfileOut": "_mybusinessbusinessinformation_29_ProfileOut",
        "AttributeMetadataIn": "_mybusinessbusinessinformation_30_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusinessbusinessinformation_31_AttributeMetadataOut",
        "RelevantLocationIn": "_mybusinessbusinessinformation_32_RelevantLocationIn",
        "RelevantLocationOut": "_mybusinessbusinessinformation_33_RelevantLocationOut",
        "RepeatedEnumAttributeValueIn": "_mybusinessbusinessinformation_34_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusinessbusinessinformation_35_RepeatedEnumAttributeValueOut",
        "MoneyIn": "_mybusinessbusinessinformation_36_MoneyIn",
        "MoneyOut": "_mybusinessbusinessinformation_37_MoneyOut",
        "BusinessHoursIn": "_mybusinessbusinessinformation_38_BusinessHoursIn",
        "BusinessHoursOut": "_mybusinessbusinessinformation_39_BusinessHoursOut",
        "ChainIn": "_mybusinessbusinessinformation_40_ChainIn",
        "ChainOut": "_mybusinessbusinessinformation_41_ChainOut",
        "DateIn": "_mybusinessbusinessinformation_42_DateIn",
        "DateOut": "_mybusinessbusinessinformation_43_DateOut",
        "ChainUriIn": "_mybusinessbusinessinformation_44_ChainUriIn",
        "ChainUriOut": "_mybusinessbusinessinformation_45_ChainUriOut",
        "ChainNameIn": "_mybusinessbusinessinformation_46_ChainNameIn",
        "ChainNameOut": "_mybusinessbusinessinformation_47_ChainNameOut",
        "ListLocationsResponseIn": "_mybusinessbusinessinformation_48_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusinessbusinessinformation_49_ListLocationsResponseOut",
        "UriAttributeValueIn": "_mybusinessbusinessinformation_50_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusinessbusinessinformation_51_UriAttributeValueOut",
        "AdWordsLocationExtensionsIn": "_mybusinessbusinessinformation_52_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusinessbusinessinformation_53_AdWordsLocationExtensionsOut",
        "ServiceAreaBusinessIn": "_mybusinessbusinessinformation_54_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusinessbusinessinformation_55_ServiceAreaBusinessOut",
        "MoreHoursIn": "_mybusinessbusinessinformation_56_MoreHoursIn",
        "MoreHoursOut": "_mybusinessbusinessinformation_57_MoreHoursOut",
        "AttributeIn": "_mybusinessbusinessinformation_58_AttributeIn",
        "AttributeOut": "_mybusinessbusinessinformation_59_AttributeOut",
        "EmptyIn": "_mybusinessbusinessinformation_60_EmptyIn",
        "EmptyOut": "_mybusinessbusinessinformation_61_EmptyOut",
        "ListCategoriesResponseIn": "_mybusinessbusinessinformation_62_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusinessbusinessinformation_63_ListCategoriesResponseOut",
        "TimeOfDayIn": "_mybusinessbusinessinformation_64_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinessbusinessinformation_65_TimeOfDayOut",
        "TimePeriodIn": "_mybusinessbusinessinformation_66_TimePeriodIn",
        "TimePeriodOut": "_mybusinessbusinessinformation_67_TimePeriodOut",
        "FreeFormServiceItemIn": "_mybusinessbusinessinformation_68_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusinessbusinessinformation_69_FreeFormServiceItemOut",
        "AssociateLocationRequestIn": "_mybusinessbusinessinformation_70_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusinessbusinessinformation_71_AssociateLocationRequestOut",
        "RelationshipDataIn": "_mybusinessbusinessinformation_72_RelationshipDataIn",
        "RelationshipDataOut": "_mybusinessbusinessinformation_73_RelationshipDataOut",
        "StructuredServiceItemIn": "_mybusinessbusinessinformation_74_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusinessbusinessinformation_75_StructuredServiceItemOut",
        "GoogleUpdatedLocationIn": "_mybusinessbusinessinformation_76_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusinessbusinessinformation_77_GoogleUpdatedLocationOut",
        "SearchGoogleLocationsRequestIn": "_mybusinessbusinessinformation_78_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusinessbusinessinformation_79_SearchGoogleLocationsRequestOut",
        "PhoneNumbersIn": "_mybusinessbusinessinformation_80_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusinessbusinessinformation_81_PhoneNumbersOut",
        "PlaceInfoIn": "_mybusinessbusinessinformation_82_PlaceInfoIn",
        "PlaceInfoOut": "_mybusinessbusinessinformation_83_PlaceInfoOut",
        "GoogleLocationIn": "_mybusinessbusinessinformation_84_GoogleLocationIn",
        "GoogleLocationOut": "_mybusinessbusinessinformation_85_GoogleLocationOut",
        "AttributesIn": "_mybusinessbusinessinformation_86_AttributesIn",
        "AttributesOut": "_mybusinessbusinessinformation_87_AttributesOut",
        "MetadataIn": "_mybusinessbusinessinformation_88_MetadataIn",
        "MetadataOut": "_mybusinessbusinessinformation_89_MetadataOut",
        "LabelIn": "_mybusinessbusinessinformation_90_LabelIn",
        "LabelOut": "_mybusinessbusinessinformation_91_LabelOut",
        "BatchGetCategoriesResponseIn": "_mybusinessbusinessinformation_92_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusinessbusinessinformation_93_BatchGetCategoriesResponseOut",
        "ServiceTypeIn": "_mybusinessbusinessinformation_94_ServiceTypeIn",
        "ServiceTypeOut": "_mybusinessbusinessinformation_95_ServiceTypeOut",
        "SpecialHourPeriodIn": "_mybusinessbusinessinformation_96_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusinessbusinessinformation_97_SpecialHourPeriodOut",
        "CategoriesIn": "_mybusinessbusinessinformation_98_CategoriesIn",
        "CategoriesOut": "_mybusinessbusinessinformation_99_CategoriesOut",
        "SearchChainsResponseIn": "_mybusinessbusinessinformation_100_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusinessbusinessinformation_101_SearchChainsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "websiteUri": t.string().optional(),
            "title": t.string(),
            "storeCode": t.string().optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "name": t.string().optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "languageCode": t.string().optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "labels": t.array(t.string()).optional(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "websiteUri": t.string().optional(),
            "title": t.string(),
            "storeCode": t.string().optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "name": t.string().optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "languageCode": t.string().optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "labels": t.array(t.string()).optional(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["CategoryIn"] = t.struct({"name": t.string()}).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "serviceTypes": t.array(t.proxy(renames["ServiceTypeOut"])).optional(),
            "moreHoursTypes": t.array(t.proxy(renames["MoreHoursTypeOut"])).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sortingCode": t.string().optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
            "revision": t.integer().optional(),
            "sortingCode": t.string().optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["MoreHoursTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoreHoursTypeIn"]
    )
    types["MoreHoursTypeOut"] = t.struct(
        {
            "hoursTypeId": t.string().optional(),
            "localizedDisplayName": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursTypeOut"])
    types["OpenInfoIn"] = t.struct(
        {"status": t.string(), "openingDate": t.proxy(renames["DateIn"]).optional()}
    ).named(renames["OpenInfoIn"])
    types["OpenInfoOut"] = t.struct(
        {
            "status": t.string(),
            "canReopen": t.boolean().optional(),
            "openingDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenInfoOut"])
    types["ServiceItemIn"] = t.struct(
        {
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemIn"]
            ).optional(),
            "freeFormServiceItem": t.proxy(renames["FreeFormServiceItemIn"]).optional(),
        }
    ).named(renames["ServiceItemIn"])
    types["ServiceItemOut"] = t.struct(
        {
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemOut"]
            ).optional(),
            "freeFormServiceItem": t.proxy(
                renames["FreeFormServiceItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceItemOut"])
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
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
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
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["AttributeMetadataIn"] = t.struct(
        {
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "deprecated": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "deprecated": t.boolean().optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
    types["ChainIn"] = t.struct(
        {
            "locationCount": t.integer().optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "locationCount": t.integer().optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
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
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
    types["ChainNameIn"] = t.struct(
        {"displayName": t.string().optional(), "languageCode": t.string().optional()}
    ).named(renames["ChainNameIn"])
    types["ChainNameOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainNameOut"])
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
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "places": t.proxy(renames["PlacesIn"]).optional(),
            "regionCode": t.string().optional(),
            "businessType": t.string(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "regionCode": t.string().optional(),
            "businessType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
    types["MoreHoursIn"] = t.struct(
        {
            "hoursTypeId": t.string(),
            "periods": t.array(t.proxy(renames["TimePeriodIn"])),
        }
    ).named(renames["MoreHoursIn"])
    types["MoreHoursOut"] = t.struct(
        {
            "hoursTypeId": t.string(),
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursOut"])
    types["AttributeIn"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueIn"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueIn"])).optional(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "valueType": t.string().optional(),
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListCategoriesResponseIn"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCategoriesResponseIn"])
    types["ListCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCategoriesResponseOut"])
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
    types["TimePeriodIn"] = t.struct(
        {
            "openDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "openDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["FreeFormServiceItemIn"] = t.struct(
        {"category": t.string(), "label": t.proxy(renames["LabelIn"])}
    ).named(renames["FreeFormServiceItemIn"])
    types["FreeFormServiceItemOut"] = t.struct(
        {
            "category": t.string(),
            "label": t.proxy(renames["LabelOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeFormServiceItemOut"])
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
    types["RelationshipDataIn"] = t.struct(
        {
            "parentLocation": t.proxy(renames["RelevantLocationIn"]).optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationIn"])
            ).optional(),
            "parentChain": t.string().optional(),
        }
    ).named(renames["RelationshipDataIn"])
    types["RelationshipDataOut"] = t.struct(
        {
            "parentLocation": t.proxy(renames["RelevantLocationOut"]).optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationOut"])
            ).optional(),
            "parentChain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDataOut"])
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
    types["GoogleLocationIn"] = t.struct(
        {
            "requestAdminRightsUri": t.string().optional(),
            "name": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "requestAdminRightsUri": t.string().optional(),
            "name": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
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
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "canModifyServiceList": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "placeId": t.string().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "duplicateLocation": t.string().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["LabelIn"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "displayName": t.string(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
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
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
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
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])

    functions = {}
    functions["locationsGetGoogleUpdated"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPatch"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsClearLocationAssociation"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetAttributes"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAssociate"] = mybusinessbusinessinformation.post(
        "v1/{name}:associate",
        t.struct(
            {
                "name": t.string(),
                "placeId": t.string().optional(),
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
    functions["attributesList"] = mybusinessbusinessinformation.get(
        "v1/attributes",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "showAll": t.boolean().optional(),
                "parent": t.string().optional(),
                "regionCode": t.string().optional(),
                "categoryName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
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
    functions["accountsLocationsCreate"] = mybusinessbusinessinformation.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["categoriesBatchGet"] = mybusinessbusinessinformation.get(
        "v1/categories",
        t.struct(
            {
                "languageCode": t.string(),
                "filter": t.string().optional(),
                "view": t.string(),
                "pageSize": t.integer().optional(),
                "regionCode": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesList"] = mybusinessbusinessinformation.get(
        "v1/categories",
        t.struct(
            {
                "languageCode": t.string(),
                "filter": t.string().optional(),
                "view": t.string(),
                "pageSize": t.integer().optional(),
                "regionCode": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessbusinessinformation",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
