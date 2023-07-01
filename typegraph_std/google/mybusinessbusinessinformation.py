from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessbusinessinformation():
    mybusinessbusinessinformation = HTTPRuntime(
        "https://mybusinessbusinessinformation.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_mybusinessbusinessinformation_1_ErrorResponse",
        "RelationshipDataIn": "_mybusinessbusinessinformation_2_RelationshipDataIn",
        "RelationshipDataOut": "_mybusinessbusinessinformation_3_RelationshipDataOut",
        "FreeFormServiceItemIn": "_mybusinessbusinessinformation_4_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusinessbusinessinformation_5_FreeFormServiceItemOut",
        "ListCategoriesResponseIn": "_mybusinessbusinessinformation_6_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusinessbusinessinformation_7_ListCategoriesResponseOut",
        "ListLocationsResponseIn": "_mybusinessbusinessinformation_8_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusinessbusinessinformation_9_ListLocationsResponseOut",
        "SpecialHourPeriodIn": "_mybusinessbusinessinformation_10_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusinessbusinessinformation_11_SpecialHourPeriodOut",
        "BusinessHoursIn": "_mybusinessbusinessinformation_12_BusinessHoursIn",
        "BusinessHoursOut": "_mybusinessbusinessinformation_13_BusinessHoursOut",
        "AttributesIn": "_mybusinessbusinessinformation_14_AttributesIn",
        "AttributesOut": "_mybusinessbusinessinformation_15_AttributesOut",
        "StructuredServiceItemIn": "_mybusinessbusinessinformation_16_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusinessbusinessinformation_17_StructuredServiceItemOut",
        "MoreHoursIn": "_mybusinessbusinessinformation_18_MoreHoursIn",
        "MoreHoursOut": "_mybusinessbusinessinformation_19_MoreHoursOut",
        "ServiceAreaBusinessIn": "_mybusinessbusinessinformation_20_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusinessbusinessinformation_21_ServiceAreaBusinessOut",
        "TimePeriodIn": "_mybusinessbusinessinformation_22_TimePeriodIn",
        "TimePeriodOut": "_mybusinessbusinessinformation_23_TimePeriodOut",
        "ProfileIn": "_mybusinessbusinessinformation_24_ProfileIn",
        "ProfileOut": "_mybusinessbusinessinformation_25_ProfileOut",
        "BatchGetCategoriesResponseIn": "_mybusinessbusinessinformation_26_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusinessbusinessinformation_27_BatchGetCategoriesResponseOut",
        "LatLngIn": "_mybusinessbusinessinformation_28_LatLngIn",
        "LatLngOut": "_mybusinessbusinessinformation_29_LatLngOut",
        "OpenInfoIn": "_mybusinessbusinessinformation_30_OpenInfoIn",
        "OpenInfoOut": "_mybusinessbusinessinformation_31_OpenInfoOut",
        "MoneyIn": "_mybusinessbusinessinformation_32_MoneyIn",
        "MoneyOut": "_mybusinessbusinessinformation_33_MoneyOut",
        "SpecialHoursIn": "_mybusinessbusinessinformation_34_SpecialHoursIn",
        "SpecialHoursOut": "_mybusinessbusinessinformation_35_SpecialHoursOut",
        "RepeatedEnumAttributeValueIn": "_mybusinessbusinessinformation_36_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusinessbusinessinformation_37_RepeatedEnumAttributeValueOut",
        "AttributeIn": "_mybusinessbusinessinformation_38_AttributeIn",
        "AttributeOut": "_mybusinessbusinessinformation_39_AttributeOut",
        "CategoryIn": "_mybusinessbusinessinformation_40_CategoryIn",
        "CategoryOut": "_mybusinessbusinessinformation_41_CategoryOut",
        "SearchGoogleLocationsResponseIn": "_mybusinessbusinessinformation_42_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusinessbusinessinformation_43_SearchGoogleLocationsResponseOut",
        "ListAttributeMetadataResponseIn": "_mybusinessbusinessinformation_44_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusinessbusinessinformation_45_ListAttributeMetadataResponseOut",
        "DateIn": "_mybusinessbusinessinformation_46_DateIn",
        "DateOut": "_mybusinessbusinessinformation_47_DateOut",
        "CategoriesIn": "_mybusinessbusinessinformation_48_CategoriesIn",
        "CategoriesOut": "_mybusinessbusinessinformation_49_CategoriesOut",
        "TimeOfDayIn": "_mybusinessbusinessinformation_50_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinessbusinessinformation_51_TimeOfDayOut",
        "ServiceItemIn": "_mybusinessbusinessinformation_52_ServiceItemIn",
        "ServiceItemOut": "_mybusinessbusinessinformation_53_ServiceItemOut",
        "PhoneNumbersIn": "_mybusinessbusinessinformation_54_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusinessbusinessinformation_55_PhoneNumbersOut",
        "PlaceInfoIn": "_mybusinessbusinessinformation_56_PlaceInfoIn",
        "PlaceInfoOut": "_mybusinessbusinessinformation_57_PlaceInfoOut",
        "PlacesIn": "_mybusinessbusinessinformation_58_PlacesIn",
        "PlacesOut": "_mybusinessbusinessinformation_59_PlacesOut",
        "SearchGoogleLocationsRequestIn": "_mybusinessbusinessinformation_60_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusinessbusinessinformation_61_SearchGoogleLocationsRequestOut",
        "MetadataIn": "_mybusinessbusinessinformation_62_MetadataIn",
        "MetadataOut": "_mybusinessbusinessinformation_63_MetadataOut",
        "ChainIn": "_mybusinessbusinessinformation_64_ChainIn",
        "ChainOut": "_mybusinessbusinessinformation_65_ChainOut",
        "GoogleUpdatedLocationIn": "_mybusinessbusinessinformation_66_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusinessbusinessinformation_67_GoogleUpdatedLocationOut",
        "AttributeValueMetadataIn": "_mybusinessbusinessinformation_68_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusinessbusinessinformation_69_AttributeValueMetadataOut",
        "GoogleLocationIn": "_mybusinessbusinessinformation_70_GoogleLocationIn",
        "GoogleLocationOut": "_mybusinessbusinessinformation_71_GoogleLocationOut",
        "ServiceTypeIn": "_mybusinessbusinessinformation_72_ServiceTypeIn",
        "ServiceTypeOut": "_mybusinessbusinessinformation_73_ServiceTypeOut",
        "EmptyIn": "_mybusinessbusinessinformation_74_EmptyIn",
        "EmptyOut": "_mybusinessbusinessinformation_75_EmptyOut",
        "UriAttributeValueIn": "_mybusinessbusinessinformation_76_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusinessbusinessinformation_77_UriAttributeValueOut",
        "LabelIn": "_mybusinessbusinessinformation_78_LabelIn",
        "LabelOut": "_mybusinessbusinessinformation_79_LabelOut",
        "LocationIn": "_mybusinessbusinessinformation_80_LocationIn",
        "LocationOut": "_mybusinessbusinessinformation_81_LocationOut",
        "AttributeMetadataIn": "_mybusinessbusinessinformation_82_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusinessbusinessinformation_83_AttributeMetadataOut",
        "ChainUriIn": "_mybusinessbusinessinformation_84_ChainUriIn",
        "ChainUriOut": "_mybusinessbusinessinformation_85_ChainUriOut",
        "SearchChainsResponseIn": "_mybusinessbusinessinformation_86_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusinessbusinessinformation_87_SearchChainsResponseOut",
        "PostalAddressIn": "_mybusinessbusinessinformation_88_PostalAddressIn",
        "PostalAddressOut": "_mybusinessbusinessinformation_89_PostalAddressOut",
        "ChainNameIn": "_mybusinessbusinessinformation_90_ChainNameIn",
        "ChainNameOut": "_mybusinessbusinessinformation_91_ChainNameOut",
        "AdWordsLocationExtensionsIn": "_mybusinessbusinessinformation_92_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusinessbusinessinformation_93_AdWordsLocationExtensionsOut",
        "RelevantLocationIn": "_mybusinessbusinessinformation_94_RelevantLocationIn",
        "RelevantLocationOut": "_mybusinessbusinessinformation_95_RelevantLocationOut",
        "MoreHoursTypeIn": "_mybusinessbusinessinformation_96_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusinessbusinessinformation_97_MoreHoursTypeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RelationshipDataIn"] = t.struct(
        {
            "parentLocation": t.proxy(renames["RelevantLocationIn"]).optional(),
            "parentChain": t.string().optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationIn"])
            ).optional(),
        }
    ).named(renames["RelationshipDataIn"])
    types["RelationshipDataOut"] = t.struct(
        {
            "parentLocation": t.proxy(renames["RelevantLocationOut"]).optional(),
            "parentChain": t.string().optional(),
            "childrenLocations": t.array(
                t.proxy(renames["RelevantLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDataOut"])
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
    types["ListLocationsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
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
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "businessType": t.string(),
            "regionCode": t.string().optional(),
            "places": t.proxy(renames["PlacesIn"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "businessType": t.string(),
            "regionCode": t.string().optional(),
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
    types["TimePeriodIn"] = t.struct(
        {
            "openDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "closeDay": t.string(),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "openDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "closeDay": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
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
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
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
    types["AttributeIn"] = t.struct(
        {
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueIn"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueIn"])).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["AttributeIn"])
    types["AttributeOut"] = t.struct(
        {
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
    types["CategoryIn"] = t.struct({"name": t.string()}).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "name": t.string(),
            "moreHoursTypes": t.array(t.proxy(renames["MoreHoursTypeOut"])).optional(),
            "serviceTypes": t.array(t.proxy(renames["ServiceTypeOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
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
    types["CategoriesIn"] = t.struct(
        {
            "additionalCategories": t.array(t.proxy(renames["CategoryIn"])).optional(),
            "primaryCategory": t.proxy(renames["CategoryIn"]),
        }
    ).named(renames["CategoriesIn"])
    types["CategoriesOut"] = t.struct(
        {
            "additionalCategories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "primaryCategory": t.proxy(renames["CategoryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoriesOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["ServiceItemIn"] = t.struct(
        {
            "freeFormServiceItem": t.proxy(renames["FreeFormServiceItemIn"]).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemIn"]
            ).optional(),
            "price": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["ServiceItemIn"])
    types["ServiceItemOut"] = t.struct(
        {
            "freeFormServiceItem": t.proxy(
                renames["FreeFormServiceItemOut"]
            ).optional(),
            "structuredServiceItem": t.proxy(
                renames["StructuredServiceItemOut"]
            ).optional(),
            "price": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceItemOut"])
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
        {"placeName": t.string(), "placeId": t.string()}
    ).named(renames["PlaceInfoIn"])
    types["PlaceInfoOut"] = t.struct(
        {
            "placeName": t.string(),
            "placeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceInfoOut"])
    types["PlacesIn"] = t.struct(
        {"placeInfos": t.array(t.proxy(renames["PlaceInfoIn"])).optional()}
    ).named(renames["PlacesIn"])
    types["PlacesOut"] = t.struct(
        {
            "placeInfos": t.array(t.proxy(renames["PlaceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlacesOut"])
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
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "duplicateLocation": t.string().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
            "pendingMask": t.string().optional(),
            "diffMask": t.string().optional(),
            "location": t.proxy(renames["LocationIn"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationIn"])
    types["GoogleUpdatedLocationOut"] = t.struct(
        {
            "pendingMask": t.string().optional(),
            "diffMask": t.string().optional(),
            "location": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleUpdatedLocationOut"])
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
    types["GoogleLocationIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "requestAdminRightsUri": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLocationIn"])
    types["GoogleLocationOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "requestAdminRightsUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLocationOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["LabelIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["LabelIn"])
    types["LabelOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelOut"])
    types["LocationIn"] = t.struct(
        {
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "websiteUri": t.string().optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "name": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "labels": t.array(t.string()).optional(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "title": t.string(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "storeCode": t.string().optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "languageCode": t.string().optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "websiteUri": t.string().optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "name": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "labels": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "title": t.string(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "storeCode": t.string().optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "languageCode": t.string().optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AttributeMetadataIn"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "parent": t.string().optional(),
            "valueType": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "parent": t.string().optional(),
            "valueType": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "sortingCode": t.string().optional(),
            "regionCode": t.string(),
            "organization": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "sortingCode": t.string().optional(),
            "regionCode": t.string(),
            "organization": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
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

    functions = {}
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
                "pageToken": t.string().optional(),
                "showAll": t.boolean().optional(),
                "languageCode": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "regionCode": t.string().optional(),
                "categoryName": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["locationsPatch"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetAttributes"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetGoogleUpdated"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusinessbusinessinformation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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

    return Import(
        importer="mybusinessbusinessinformation",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
