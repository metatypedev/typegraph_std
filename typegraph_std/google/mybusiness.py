from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph.importers.base.importer import Import
from box import Box


def import_mybusiness() -> Import:
    mybusiness = HTTPRuntime("https://mybusinessbusinessinformation.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusiness_1_ErrorResponse",
        "LabelIn": "_mybusiness_2_LabelIn",
        "LabelOut": "_mybusiness_3_LabelOut",
        "PhoneNumbersIn": "_mybusiness_4_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusiness_5_PhoneNumbersOut",
        "ListLocationsResponseIn": "_mybusiness_6_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusiness_7_ListLocationsResponseOut",
        "MoneyIn": "_mybusiness_8_MoneyIn",
        "MoneyOut": "_mybusiness_9_MoneyOut",
        "MoreHoursTypeIn": "_mybusiness_10_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusiness_11_MoreHoursTypeOut",
        "TimeOfDayIn": "_mybusiness_12_TimeOfDayIn",
        "TimeOfDayOut": "_mybusiness_13_TimeOfDayOut",
        "UriAttributeValueIn": "_mybusiness_14_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusiness_15_UriAttributeValueOut",
        "SpecialHourPeriodIn": "_mybusiness_16_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusiness_17_SpecialHourPeriodOut",
        "PlaceInfoIn": "_mybusiness_18_PlaceInfoIn",
        "PlaceInfoOut": "_mybusiness_19_PlaceInfoOut",
        "ChainNameIn": "_mybusiness_20_ChainNameIn",
        "ChainNameOut": "_mybusiness_21_ChainNameOut",
        "AttributeValueMetadataIn": "_mybusiness_22_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusiness_23_AttributeValueMetadataOut",
        "AttributeIn": "_mybusiness_24_AttributeIn",
        "AttributeOut": "_mybusiness_25_AttributeOut",
        "LocationIn": "_mybusiness_26_LocationIn",
        "LocationOut": "_mybusiness_27_LocationOut",
        "ServiceItemIn": "_mybusiness_28_ServiceItemIn",
        "ServiceItemOut": "_mybusiness_29_ServiceItemOut",
        "SpecialHoursIn": "_mybusiness_30_SpecialHoursIn",
        "SpecialHoursOut": "_mybusiness_31_SpecialHoursOut",
        "EmptyIn": "_mybusiness_32_EmptyIn",
        "EmptyOut": "_mybusiness_33_EmptyOut",
        "AdWordsLocationExtensionsIn": "_mybusiness_34_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusiness_35_AdWordsLocationExtensionsOut",
        "MetadataIn": "_mybusiness_36_MetadataIn",
        "MetadataOut": "_mybusiness_37_MetadataOut",
        "ListAttributeMetadataResponseIn": "_mybusiness_38_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusiness_39_ListAttributeMetadataResponseOut",
        "RelationshipDataIn": "_mybusiness_40_RelationshipDataIn",
        "RelationshipDataOut": "_mybusiness_41_RelationshipDataOut",
        "GoogleLocationIn": "_mybusiness_42_GoogleLocationIn",
        "GoogleLocationOut": "_mybusiness_43_GoogleLocationOut",
        "RelevantLocationIn": "_mybusiness_44_RelevantLocationIn",
        "RelevantLocationOut": "_mybusiness_45_RelevantLocationOut",
        "FreeFormServiceItemIn": "_mybusiness_46_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusiness_47_FreeFormServiceItemOut",
        "SearchChainsResponseIn": "_mybusiness_48_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusiness_49_SearchChainsResponseOut",
        "ProfileIn": "_mybusiness_50_ProfileIn",
        "ProfileOut": "_mybusiness_51_ProfileOut",
        "LatLngIn": "_mybusiness_52_LatLngIn",
        "LatLngOut": "_mybusiness_53_LatLngOut",
        "PlacesIn": "_mybusiness_54_PlacesIn",
        "PlacesOut": "_mybusiness_55_PlacesOut",
        "AssociateLocationRequestIn": "_mybusiness_56_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusiness_57_AssociateLocationRequestOut",
        "ListCategoriesResponseIn": "_mybusiness_58_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusiness_59_ListCategoriesResponseOut",
        "ClearLocationAssociationRequestIn": "_mybusiness_60_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusiness_61_ClearLocationAssociationRequestOut",
        "BusinessHoursIn": "_mybusiness_62_BusinessHoursIn",
        "BusinessHoursOut": "_mybusiness_63_BusinessHoursOut",
        "MoreHoursIn": "_mybusiness_64_MoreHoursIn",
        "MoreHoursOut": "_mybusiness_65_MoreHoursOut",
        "SearchGoogleLocationsResponseIn": "_mybusiness_66_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusiness_67_SearchGoogleLocationsResponseOut",
        "ServiceAreaBusinessIn": "_mybusiness_68_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusiness_69_ServiceAreaBusinessOut",
        "PostalAddressIn": "_mybusiness_70_PostalAddressIn",
        "PostalAddressOut": "_mybusiness_71_PostalAddressOut",
        "ServiceTypeIn": "_mybusiness_72_ServiceTypeIn",
        "ServiceTypeOut": "_mybusiness_73_ServiceTypeOut",
        "AttributeMetadataIn": "_mybusiness_74_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusiness_75_AttributeMetadataOut",
        "CategoryIn": "_mybusiness_76_CategoryIn",
        "CategoryOut": "_mybusiness_77_CategoryOut",
        "StructuredServiceItemIn": "_mybusiness_78_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusiness_79_StructuredServiceItemOut",
        "OpenInfoIn": "_mybusiness_80_OpenInfoIn",
        "OpenInfoOut": "_mybusiness_81_OpenInfoOut",
        "ChainUriIn": "_mybusiness_82_ChainUriIn",
        "ChainUriOut": "_mybusiness_83_ChainUriOut",
        "DateIn": "_mybusiness_84_DateIn",
        "DateOut": "_mybusiness_85_DateOut",
        "BatchGetCategoriesResponseIn": "_mybusiness_86_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusiness_87_BatchGetCategoriesResponseOut",
        "RepeatedEnumAttributeValueIn": "_mybusiness_88_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusiness_89_RepeatedEnumAttributeValueOut",
        "AttributesIn": "_mybusiness_90_AttributesIn",
        "AttributesOut": "_mybusiness_91_AttributesOut",
        "SearchGoogleLocationsRequestIn": "_mybusiness_92_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusiness_93_SearchGoogleLocationsRequestOut",
        "ChainIn": "_mybusiness_94_ChainIn",
        "ChainOut": "_mybusiness_95_ChainOut",
        "GoogleUpdatedLocationIn": "_mybusiness_96_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusiness_97_GoogleUpdatedLocationOut",
        "CategoriesIn": "_mybusiness_98_CategoriesIn",
        "CategoriesOut": "_mybusiness_99_CategoriesOut",
        "TimePeriodIn": "_mybusiness_100_TimePeriodIn",
        "TimePeriodOut": "_mybusiness_101_TimePeriodOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LabelIn"] = t.struct(
        {
            "displayName": t.string(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "displayName": t.string(),
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
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
    types["AttributeIn"] = t.struct(
        {
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueIn"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueIn"])).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "storeCode": t.string().optional(),
            "websiteUri": t.string().optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "title": t.string(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "languageCode": t.string().optional(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "storeCode": t.string().optional(),
            "websiteUri": t.string().optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "title": t.string(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "mapsUri": t.string().optional(),
            "placeId": t.string().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "duplicateLocation": t.string().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["RelationshipDataIn"] = t.struct(
        {
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationIn"])
            ).optional(),
            "parentLocation": t.proxy(renames["RelevantLocationIn"]).optional(),
            "parentChain": t.string().optional(),
        }
    ).named(renames["RelationshipDataIn"])
    types["RelationshipDataOut"] = t.struct(
        {
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationOut"])
            ).optional(),
            "parentLocation": t.proxy(renames["RelevantLocationOut"]).optional(),
            "parentChain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDataOut"])
    types["GoogleLocationIn"] = t.struct(
        {
            "requestAdminRightsUri": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "requestAdminRightsUri": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
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
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
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
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
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
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
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
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "places": t.proxy(renames["PlacesIn"]).optional(),
            "businessType": t.string(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "businessType": t.string(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sortingCode": t.string().optional(),
            "revision": t.integer().optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["ServiceTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ServiceTypeIn"]
    )
    types["ServiceTypeOut"] = t.struct(
        {
            "serviceTypeId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceTypeOut"])
    types["AttributeMetadataIn"] = t.struct(
        {
            "repeatable": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "valueType": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "groupDisplayName": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "repeatable": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "valueType": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
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
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
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
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
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
    types["ChainIn"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "locationCount": t.integer().optional(),
            "name": t.string(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "locationCount": t.integer().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
    types["GoogleUpdatedLocationIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "pendingMask": t.string().optional(),
            "diffMask": t.string().optional(),
        }
    ).named(renames["GoogleUpdatedLocationIn"])
    types["GoogleUpdatedLocationOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "pendingMask": t.string().optional(),
            "diffMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationOut"])
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
    types["TimePeriodIn"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "closeDay": t.string(),
            "openDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "closeDay": t.string(),
            "openDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])

    functions = {}
    functions["attributesList"] = mybusiness.get(
        "v1/attributes",
        t.struct(
            {
                "showAll": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "regionCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "categoryName": t.string().optional(),
                "languageCode": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsClearLocationAssociation"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAssociate"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetAttributes"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetGoogleUpdated"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPatch"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
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
    functions["categoriesBatchGet"] = mybusiness.get(
        "v1/categories",
        t.struct(
            {
                "regionCode": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "languageCode": t.string(),
                "view": t.string(),
                "filter": t.string().optional(),
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
                "regionCode": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "languageCode": t.string(),
                "view": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsCreate"] = mybusiness.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsList"] = mybusiness.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleLocationsSearch"] = mybusiness.post(
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
    functions["chainsSearch"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["chainsGet"] = mybusiness.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ChainOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusiness",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
