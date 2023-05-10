from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import
from typegraph import TypeGraph
from typegraph.runtimes.http import HTTPRuntime


def import_mybusiness() -> Import:
    mybusiness = HTTPRuntime("https://mybusinessbusinessinformation.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusiness_1_ErrorResponse",
        "ServiceTypeIn": "_mybusiness_2_ServiceTypeIn",
        "ServiceTypeOut": "_mybusiness_3_ServiceTypeOut",
        "ServiceAreaBusinessIn": "_mybusiness_4_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusiness_5_ServiceAreaBusinessOut",
        "MetadataIn": "_mybusiness_6_MetadataIn",
        "MetadataOut": "_mybusiness_7_MetadataOut",
        "RelationshipDataIn": "_mybusiness_8_RelationshipDataIn",
        "RelationshipDataOut": "_mybusiness_9_RelationshipDataOut",
        "CategoryIn": "_mybusiness_10_CategoryIn",
        "CategoryOut": "_mybusiness_11_CategoryOut",
        "ChainUriIn": "_mybusiness_12_ChainUriIn",
        "ChainUriOut": "_mybusiness_13_ChainUriOut",
        "UriAttributeValueIn": "_mybusiness_14_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusiness_15_UriAttributeValueOut",
        "SearchGoogleLocationsResponseIn": "_mybusiness_16_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusiness_17_SearchGoogleLocationsResponseOut",
        "MoneyIn": "_mybusiness_18_MoneyIn",
        "MoneyOut": "_mybusiness_19_MoneyOut",
        "ListCategoriesResponseIn": "_mybusiness_20_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusiness_21_ListCategoriesResponseOut",
        "FreeFormServiceItemIn": "_mybusiness_22_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusiness_23_FreeFormServiceItemOut",
        "PhoneNumbersIn": "_mybusiness_24_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusiness_25_PhoneNumbersOut",
        "GoogleLocationIn": "_mybusiness_26_GoogleLocationIn",
        "GoogleLocationOut": "_mybusiness_27_GoogleLocationOut",
        "PlaceInfoIn": "_mybusiness_28_PlaceInfoIn",
        "PlaceInfoOut": "_mybusiness_29_PlaceInfoOut",
        "BatchGetCategoriesResponseIn": "_mybusiness_30_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusiness_31_BatchGetCategoriesResponseOut",
        "OpenInfoIn": "_mybusiness_32_OpenInfoIn",
        "OpenInfoOut": "_mybusiness_33_OpenInfoOut",
        "AttributeMetadataIn": "_mybusiness_34_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusiness_35_AttributeMetadataOut",
        "ListAttributeMetadataResponseIn": "_mybusiness_36_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusiness_37_ListAttributeMetadataResponseOut",
        "SpecialHoursIn": "_mybusiness_38_SpecialHoursIn",
        "SpecialHoursOut": "_mybusiness_39_SpecialHoursOut",
        "PostalAddressIn": "_mybusiness_40_PostalAddressIn",
        "PostalAddressOut": "_mybusiness_41_PostalAddressOut",
        "SearchChainsResponseIn": "_mybusiness_42_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusiness_43_SearchChainsResponseOut",
        "ProfileIn": "_mybusiness_44_ProfileIn",
        "ProfileOut": "_mybusiness_45_ProfileOut",
        "GoogleUpdatedLocationIn": "_mybusiness_46_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusiness_47_GoogleUpdatedLocationOut",
        "ChainNameIn": "_mybusiness_48_ChainNameIn",
        "ChainNameOut": "_mybusiness_49_ChainNameOut",
        "ClearLocationAssociationRequestIn": "_mybusiness_50_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusiness_51_ClearLocationAssociationRequestOut",
        "AttributeIn": "_mybusiness_52_AttributeIn",
        "AttributeOut": "_mybusiness_53_AttributeOut",
        "ServiceItemIn": "_mybusiness_54_ServiceItemIn",
        "ServiceItemOut": "_mybusiness_55_ServiceItemOut",
        "DateIn": "_mybusiness_56_DateIn",
        "DateOut": "_mybusiness_57_DateOut",
        "ChainIn": "_mybusiness_58_ChainIn",
        "ChainOut": "_mybusiness_59_ChainOut",
        "SpecialHourPeriodIn": "_mybusiness_60_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusiness_61_SpecialHourPeriodOut",
        "StructuredServiceItemIn": "_mybusiness_62_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusiness_63_StructuredServiceItemOut",
        "SearchGoogleLocationsRequestIn": "_mybusiness_64_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusiness_65_SearchGoogleLocationsRequestOut",
        "MoreHoursTypeIn": "_mybusiness_66_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusiness_67_MoreHoursTypeOut",
        "TimePeriodIn": "_mybusiness_68_TimePeriodIn",
        "TimePeriodOut": "_mybusiness_69_TimePeriodOut",
        "TimeOfDayIn": "_mybusiness_70_TimeOfDayIn",
        "TimeOfDayOut": "_mybusiness_71_TimeOfDayOut",
        "LabelIn": "_mybusiness_72_LabelIn",
        "LabelOut": "_mybusiness_73_LabelOut",
        "AttributeValueMetadataIn": "_mybusiness_74_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusiness_75_AttributeValueMetadataOut",
        "AdWordsLocationExtensionsIn": "_mybusiness_76_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusiness_77_AdWordsLocationExtensionsOut",
        "PlacesIn": "_mybusiness_78_PlacesIn",
        "PlacesOut": "_mybusiness_79_PlacesOut",
        "AssociateLocationRequestIn": "_mybusiness_80_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusiness_81_AssociateLocationRequestOut",
        "MoreHoursIn": "_mybusiness_82_MoreHoursIn",
        "MoreHoursOut": "_mybusiness_83_MoreHoursOut",
        "BusinessHoursIn": "_mybusiness_84_BusinessHoursIn",
        "BusinessHoursOut": "_mybusiness_85_BusinessHoursOut",
        "EmptyIn": "_mybusiness_86_EmptyIn",
        "EmptyOut": "_mybusiness_87_EmptyOut",
        "CategoriesIn": "_mybusiness_88_CategoriesIn",
        "CategoriesOut": "_mybusiness_89_CategoriesOut",
        "LatLngIn": "_mybusiness_90_LatLngIn",
        "LatLngOut": "_mybusiness_91_LatLngOut",
        "RelevantLocationIn": "_mybusiness_92_RelevantLocationIn",
        "RelevantLocationOut": "_mybusiness_93_RelevantLocationOut",
        "LocationIn": "_mybusiness_94_LocationIn",
        "LocationOut": "_mybusiness_95_LocationOut",
        "RepeatedEnumAttributeValueIn": "_mybusiness_96_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusiness_97_RepeatedEnumAttributeValueOut",
        "AttributesIn": "_mybusiness_98_AttributesIn",
        "AttributesOut": "_mybusiness_99_AttributesOut",
        "ListLocationsResponseIn": "_mybusiness_100_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusiness_101_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "mapsUri": t.string().optional(),
            "duplicateLocation": t.string().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
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
    types["CategoryIn"] = t.struct({"name": t.string()}).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "moreHoursTypes": t.array(t.proxy(renames["MoreHoursTypeOut"])).optional(),
            "name": t.string(),
            "serviceTypes": t.array(t.proxy(renames["ServiceTypeOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
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
    types["MoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
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
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
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
    types["AttributeMetadataIn"] = t.struct(
        {
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "repeatable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "groupDisplayName": t.string().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
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
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
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
            "valueType": t.string().optional(),
            "values": t.array(t.struct({"_": t.string().optional()})).optional(),
            "name": t.string(),
            "repeatedEnumValue": t.proxy(
                renames["RepeatedEnumAttributeValueOut"]
            ).optional(),
            "uriValues": t.array(t.proxy(renames["UriAttributeValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeOut"])
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
    types["ChainIn"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "locationCount": t.integer().optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "locationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]),
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]),
            "closed": t.boolean().optional(),
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
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
    types["SearchGoogleLocationsRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]).optional(),
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestIn"])
    types["SearchGoogleLocationsRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]).optional(),
            "query": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGoogleLocationsRequestOut"])
    types["MoreHoursTypeIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoreHoursTypeIn"]
    )
    types["MoreHoursTypeOut"] = t.struct(
        {
            "localizedDisplayName": t.string().optional(),
            "hoursTypeId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoreHoursTypeOut"])
    types["TimePeriodIn"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
            "openDay": t.string(),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "openDay": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
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
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
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
    types["BusinessHoursIn"] = t.struct(
        {"periods": t.array(t.proxy(renames["TimePeriodIn"]))}
    ).named(renames["BusinessHoursIn"])
    types["BusinessHoursOut"] = t.struct(
        {
            "periods": t.array(t.proxy(renames["TimePeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessHoursOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
            "storeCode": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "title": t.string(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "websiteUri": t.string().optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "languageCode": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "storeCode": t.string().optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "title": t.string(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "websiteUri": t.string().optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "languageCode": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "labels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])

    functions = {}
    functions["attributesList"] = mybusiness.get(
        "v1/attributes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "categoryName": t.string().optional(),
                "showAll": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "regionCode": t.string().optional(),
                "parent": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesList"] = mybusiness.get(
        "v1/categories:batchGet",
        t.struct(
            {
                "view": t.string(),
                "names": t.string(),
                "regionCode": t.string().optional(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetCategoriesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["categoriesBatchGet"] = mybusiness.get(
        "v1/categories:batchGet",
        t.struct(
            {
                "view": t.string(),
                "names": t.string(),
                "regionCode": t.string().optional(),
                "languageCode": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchGetCategoriesResponseOut"]),
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
    functions["locationsPatch"] = mybusiness.get(
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
    functions["locationsGetGoogleUpdated"] = mybusiness.get(
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
    functions["locationsClearLocationAssociation"] = mybusiness.get(
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
    functions["accountsLocationsList"] = mybusiness.post(
        "v1/{parent}/locations",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "storeCode": t.string().optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "title": t.string(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "languageCode": t.string().optional(),
                "labels": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
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
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "storeCode": t.string().optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "title": t.string(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "languageCode": t.string().optional(),
                "labels": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["googleLocationsSearch"] = mybusiness.post(
        "v1/googleLocations:search",
        t.struct(
            {
                "location": t.proxy(renames["LocationIn"]).optional(),
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGoogleLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusiness", renames=renames, types=types, functions=functions
    )
