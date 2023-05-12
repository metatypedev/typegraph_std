from typegraph import t
from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from box import Box


def import_mybusiness() -> Import:
    mybusiness = HTTPRuntime("https://mybusinessbusinessinformation.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusiness_1_ErrorResponse",
        "UriAttributeValueIn": "_mybusiness_2_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusiness_3_UriAttributeValueOut",
        "SpecialHoursIn": "_mybusiness_4_SpecialHoursIn",
        "SpecialHoursOut": "_mybusiness_5_SpecialHoursOut",
        "DateIn": "_mybusiness_6_DateIn",
        "DateOut": "_mybusiness_7_DateOut",
        "PostalAddressIn": "_mybusiness_8_PostalAddressIn",
        "PostalAddressOut": "_mybusiness_9_PostalAddressOut",
        "ChainNameIn": "_mybusiness_10_ChainNameIn",
        "ChainNameOut": "_mybusiness_11_ChainNameOut",
        "RelationshipDataIn": "_mybusiness_12_RelationshipDataIn",
        "RelationshipDataOut": "_mybusiness_13_RelationshipDataOut",
        "BusinessHoursIn": "_mybusiness_14_BusinessHoursIn",
        "BusinessHoursOut": "_mybusiness_15_BusinessHoursOut",
        "SearchChainsResponseIn": "_mybusiness_16_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusiness_17_SearchChainsResponseOut",
        "RepeatedEnumAttributeValueIn": "_mybusiness_18_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusiness_19_RepeatedEnumAttributeValueOut",
        "GoogleLocationIn": "_mybusiness_20_GoogleLocationIn",
        "GoogleLocationOut": "_mybusiness_21_GoogleLocationOut",
        "AttributeValueMetadataIn": "_mybusiness_22_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusiness_23_AttributeValueMetadataOut",
        "BatchGetCategoriesResponseIn": "_mybusiness_24_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusiness_25_BatchGetCategoriesResponseOut",
        "EmptyIn": "_mybusiness_26_EmptyIn",
        "EmptyOut": "_mybusiness_27_EmptyOut",
        "StructuredServiceItemIn": "_mybusiness_28_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusiness_29_StructuredServiceItemOut",
        "ListCategoriesResponseIn": "_mybusiness_30_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusiness_31_ListCategoriesResponseOut",
        "TimePeriodIn": "_mybusiness_32_TimePeriodIn",
        "TimePeriodOut": "_mybusiness_33_TimePeriodOut",
        "AssociateLocationRequestIn": "_mybusiness_34_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusiness_35_AssociateLocationRequestOut",
        "MoreHoursTypeIn": "_mybusiness_36_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusiness_37_MoreHoursTypeOut",
        "ServiceTypeIn": "_mybusiness_38_ServiceTypeIn",
        "ServiceTypeOut": "_mybusiness_39_ServiceTypeOut",
        "AttributeIn": "_mybusiness_40_AttributeIn",
        "AttributeOut": "_mybusiness_41_AttributeOut",
        "LabelIn": "_mybusiness_42_LabelIn",
        "LabelOut": "_mybusiness_43_LabelOut",
        "ServiceItemIn": "_mybusiness_44_ServiceItemIn",
        "ServiceItemOut": "_mybusiness_45_ServiceItemOut",
        "MoneyIn": "_mybusiness_46_MoneyIn",
        "MoneyOut": "_mybusiness_47_MoneyOut",
        "ClearLocationAssociationRequestIn": "_mybusiness_48_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusiness_49_ClearLocationAssociationRequestOut",
        "SearchGoogleLocationsRequestIn": "_mybusiness_50_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusiness_51_SearchGoogleLocationsRequestOut",
        "ServiceAreaBusinessIn": "_mybusiness_52_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusiness_53_ServiceAreaBusinessOut",
        "LatLngIn": "_mybusiness_54_LatLngIn",
        "LatLngOut": "_mybusiness_55_LatLngOut",
        "AdWordsLocationExtensionsIn": "_mybusiness_56_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusiness_57_AdWordsLocationExtensionsOut",
        "FreeFormServiceItemIn": "_mybusiness_58_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusiness_59_FreeFormServiceItemOut",
        "PlaceInfoIn": "_mybusiness_60_PlaceInfoIn",
        "PlaceInfoOut": "_mybusiness_61_PlaceInfoOut",
        "GoogleUpdatedLocationIn": "_mybusiness_62_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusiness_63_GoogleUpdatedLocationOut",
        "AttributeMetadataIn": "_mybusiness_64_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusiness_65_AttributeMetadataOut",
        "SearchGoogleLocationsResponseIn": "_mybusiness_66_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusiness_67_SearchGoogleLocationsResponseOut",
        "LocationIn": "_mybusiness_68_LocationIn",
        "LocationOut": "_mybusiness_69_LocationOut",
        "SpecialHourPeriodIn": "_mybusiness_70_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusiness_71_SpecialHourPeriodOut",
        "MetadataIn": "_mybusiness_72_MetadataIn",
        "MetadataOut": "_mybusiness_73_MetadataOut",
        "PlacesIn": "_mybusiness_74_PlacesIn",
        "PlacesOut": "_mybusiness_75_PlacesOut",
        "TimeOfDayIn": "_mybusiness_76_TimeOfDayIn",
        "TimeOfDayOut": "_mybusiness_77_TimeOfDayOut",
        "CategoryIn": "_mybusiness_78_CategoryIn",
        "CategoryOut": "_mybusiness_79_CategoryOut",
        "OpenInfoIn": "_mybusiness_80_OpenInfoIn",
        "OpenInfoOut": "_mybusiness_81_OpenInfoOut",
        "MoreHoursIn": "_mybusiness_82_MoreHoursIn",
        "MoreHoursOut": "_mybusiness_83_MoreHoursOut",
        "ListAttributeMetadataResponseIn": "_mybusiness_84_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusiness_85_ListAttributeMetadataResponseOut",
        "RelevantLocationIn": "_mybusiness_86_RelevantLocationIn",
        "RelevantLocationOut": "_mybusiness_87_RelevantLocationOut",
        "ChainIn": "_mybusiness_88_ChainIn",
        "ChainOut": "_mybusiness_89_ChainOut",
        "ProfileIn": "_mybusiness_90_ProfileIn",
        "ProfileOut": "_mybusiness_91_ProfileOut",
        "AttributesIn": "_mybusiness_92_AttributesIn",
        "AttributesOut": "_mybusiness_93_AttributesOut",
        "PhoneNumbersIn": "_mybusiness_94_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusiness_95_PhoneNumbersOut",
        "ListLocationsResponseIn": "_mybusiness_96_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusiness_97_ListLocationsResponseOut",
        "ChainUriIn": "_mybusiness_98_ChainUriIn",
        "ChainUriOut": "_mybusiness_99_ChainUriOut",
        "CategoriesIn": "_mybusiness_100_CategoriesIn",
        "CategoriesOut": "_mybusiness_101_CategoriesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
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
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationIn"])
            ).optional(),
            "parentChain": t.string().optional(),
            "parentLocation": t.proxy(renames["RelevantLocationIn"]).optional(),
        }
    ).named(renames["RelationshipDataIn"])
    types["RelationshipDataOut"] = t.struct(
        {
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationOut"])
            ).optional(),
            "parentChain": t.string().optional(),
            "parentLocation": t.proxy(renames["RelevantLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDataOut"])
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
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
            "setValues": t.array(t.string()).optional(),
            "unsetValues": t.array(t.string()).optional(),
        }
    ).named(renames["RepeatedEnumAttributeValueIn"])
    types["RepeatedEnumAttributeValueOut"] = t.struct(
        {
            "setValues": t.array(t.string()).optional(),
            "unsetValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepeatedEnumAttributeValueOut"])
    types["GoogleLocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "requestAdminRightsUri": t.string().optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "requestAdminRightsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
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
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["TimePeriodIn"] = t.struct(
        {
            "closeDay": t.string(),
            "openDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "closeDay": t.string(),
            "openDay": t.string(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
    types["MoreHoursTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoreHoursTypeIn"]
    )
    types["MoreHoursTypeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "localizedDisplayName": t.string().optional(),
            "hoursTypeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursTypeOut"])
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
    types["AttributeIn"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueIn"]
            ).optional(),
            "name": t.string(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueIn"])).optional(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "name": t.string(),
            "valueType": t.string().optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["LabelIn"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["ServiceItemIn"] = t.struct(
        {
            "freeFormServiceItem": t.proxy(renames["FreeFormServiceItemIn"]).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemIn"]
            ).optional(),
        }
    ).named(renames["ServiceItemIn"])
    types["ServiceItemOut"] = t.struct(
        {
            "freeFormServiceItem": t.proxy(
                renames["FreeFormServiceItemOut"]
            ).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceItemOut"])
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
    types["SearchGoogleLocationsRequestIn"] = t.struct(
        {
            "query": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestIn"])
    types["SearchGoogleLocationsRequestOut"] = t.struct(
        {
            "query": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestOut"])
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "businessType": t.string(),
            "places": t.proxy(renames["PlacesIn"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "businessType": t.string(),
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
    types["LatLngIn"] = t.struct(
        {"longitude": t.number().optional(), "latitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
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
    types["AttributeMetadataIn"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "parent": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "parent": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
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
    types["LocationIn"] = t.struct(
        {
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "labels": t.array(t.string()).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "storeCode": t.string().optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "websiteUri": t.string().optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "title": t.string(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "labels": t.array(t.string()).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "languageCode": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "storeCode": t.string().optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "websiteUri": t.string().optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]),
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]),
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "newReviewUri": t.string().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "duplicateLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["ChainIn"] = t.struct(
        {
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
            "locationCount": t.integer().optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "name": t.string(),
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "locationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
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
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
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

    functions = {}
    functions["locationsClearLocationAssociation"] = mybusiness.post(
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
    functions["locationsUpdateAttributes"] = mybusiness.post(
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
    functions["locationsPatch"] = mybusiness.post(
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
    functions["locationsGetAttributes"] = mybusiness.post(
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
    functions["locationsDelete"] = mybusiness.post(
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
    functions["locationsGetGoogleUpdated"] = mybusiness.post(
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
    functions["locationsGet"] = mybusiness.post(
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
    functions["locationsAssociate"] = mybusiness.post(
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
    functions["locationsAttributesGetGoogleUpdated"] = mybusiness.get(
        "v1/{name}:getGoogleUpdated",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AttributesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["attributesList"] = mybusiness.get(
        "v1/attributes",
        t.struct(
            {
                "regionCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "categoryName": t.string().optional(),
                "showAll": t.boolean().optional(),
                "languageCode": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleLocationsSearch"] = mybusiness.post(
        "v1/googleLocations:search",
        t.struct(
            {
                "query": t.string().optional(),
                "location": t.proxy(renames["LocationIn"]).optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGoogleLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["chainsGet"] = mybusiness.get(
        "v1/chains:search",
        t.struct(
            {
                "chainName": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchChainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["chainsSearch"] = mybusiness.get(
        "v1/chains:search",
        t.struct(
            {
                "chainName": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchChainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsList"] = mybusiness.post(
        "v1/{parent}/locations",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "languageCode": t.string().optional(),
                "name": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "storeCode": t.string().optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "title": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsCreate"] = mybusiness.post(
        "v1/{parent}/locations",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "languageCode": t.string().optional(),
                "name": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "storeCode": t.string().optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "title": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesBatchGet"] = mybusiness.get(
        "v1/categories",
        t.struct(
            {
                "languageCode": t.string(),
                "view": t.string(),
                "regionCode": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesList"] = mybusiness.get(
        "v1/categories",
        t.struct(
            {
                "languageCode": t.string(),
                "view": t.string(),
                "regionCode": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusiness",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
