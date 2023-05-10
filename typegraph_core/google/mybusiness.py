from typegraph.runtimes.http import HTTPRuntime
from typegraph import TypeGraph
from typegraph import effects
from typegraph import t
from typegraph.importers.base.importer import Import


def import_mybusiness() -> Import:
    mybusiness = HTTPRuntime("https://mybusinessbusinessinformation.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusiness_1_ErrorResponse",
        "ChainIn": "_mybusiness_2_ChainIn",
        "ChainOut": "_mybusiness_3_ChainOut",
        "EmptyIn": "_mybusiness_4_EmptyIn",
        "EmptyOut": "_mybusiness_5_EmptyOut",
        "ServiceItemIn": "_mybusiness_6_ServiceItemIn",
        "ServiceItemOut": "_mybusiness_7_ServiceItemOut",
        "RelationshipDataIn": "_mybusiness_8_RelationshipDataIn",
        "RelationshipDataOut": "_mybusiness_9_RelationshipDataOut",
        "LabelIn": "_mybusiness_10_LabelIn",
        "LabelOut": "_mybusiness_11_LabelOut",
        "MoreHoursTypeIn": "_mybusiness_12_MoreHoursTypeIn",
        "MoreHoursTypeOut": "_mybusiness_13_MoreHoursTypeOut",
        "AttributeValueMetadataIn": "_mybusiness_14_AttributeValueMetadataIn",
        "AttributeValueMetadataOut": "_mybusiness_15_AttributeValueMetadataOut",
        "BusinessHoursIn": "_mybusiness_16_BusinessHoursIn",
        "BusinessHoursOut": "_mybusiness_17_BusinessHoursOut",
        "AttributesIn": "_mybusiness_18_AttributesIn",
        "AttributesOut": "_mybusiness_19_AttributesOut",
        "ListCategoriesResponseIn": "_mybusiness_20_ListCategoriesResponseIn",
        "ListCategoriesResponseOut": "_mybusiness_21_ListCategoriesResponseOut",
        "RelevantLocationIn": "_mybusiness_22_RelevantLocationIn",
        "RelevantLocationOut": "_mybusiness_23_RelevantLocationOut",
        "SpecialHoursIn": "_mybusiness_24_SpecialHoursIn",
        "SpecialHoursOut": "_mybusiness_25_SpecialHoursOut",
        "SpecialHourPeriodIn": "_mybusiness_26_SpecialHourPeriodIn",
        "SpecialHourPeriodOut": "_mybusiness_27_SpecialHourPeriodOut",
        "LatLngIn": "_mybusiness_28_LatLngIn",
        "LatLngOut": "_mybusiness_29_LatLngOut",
        "FreeFormServiceItemIn": "_mybusiness_30_FreeFormServiceItemIn",
        "FreeFormServiceItemOut": "_mybusiness_31_FreeFormServiceItemOut",
        "AttributeMetadataIn": "_mybusiness_32_AttributeMetadataIn",
        "AttributeMetadataOut": "_mybusiness_33_AttributeMetadataOut",
        "PhoneNumbersIn": "_mybusiness_34_PhoneNumbersIn",
        "PhoneNumbersOut": "_mybusiness_35_PhoneNumbersOut",
        "GoogleLocationIn": "_mybusiness_36_GoogleLocationIn",
        "GoogleLocationOut": "_mybusiness_37_GoogleLocationOut",
        "TimeOfDayIn": "_mybusiness_38_TimeOfDayIn",
        "TimeOfDayOut": "_mybusiness_39_TimeOfDayOut",
        "LocationIn": "_mybusiness_40_LocationIn",
        "LocationOut": "_mybusiness_41_LocationOut",
        "ListAttributeMetadataResponseIn": "_mybusiness_42_ListAttributeMetadataResponseIn",
        "ListAttributeMetadataResponseOut": "_mybusiness_43_ListAttributeMetadataResponseOut",
        "StructuredServiceItemIn": "_mybusiness_44_StructuredServiceItemIn",
        "StructuredServiceItemOut": "_mybusiness_45_StructuredServiceItemOut",
        "MetadataIn": "_mybusiness_46_MetadataIn",
        "MetadataOut": "_mybusiness_47_MetadataOut",
        "ChainUriIn": "_mybusiness_48_ChainUriIn",
        "ChainUriOut": "_mybusiness_49_ChainUriOut",
        "GoogleUpdatedLocationIn": "_mybusiness_50_GoogleUpdatedLocationIn",
        "GoogleUpdatedLocationOut": "_mybusiness_51_GoogleUpdatedLocationOut",
        "SearchGoogleLocationsResponseIn": "_mybusiness_52_SearchGoogleLocationsResponseIn",
        "SearchGoogleLocationsResponseOut": "_mybusiness_53_SearchGoogleLocationsResponseOut",
        "UriAttributeValueIn": "_mybusiness_54_UriAttributeValueIn",
        "UriAttributeValueOut": "_mybusiness_55_UriAttributeValueOut",
        "SearchChainsResponseIn": "_mybusiness_56_SearchChainsResponseIn",
        "SearchChainsResponseOut": "_mybusiness_57_SearchChainsResponseOut",
        "PlacesIn": "_mybusiness_58_PlacesIn",
        "PlacesOut": "_mybusiness_59_PlacesOut",
        "CategoriesIn": "_mybusiness_60_CategoriesIn",
        "CategoriesOut": "_mybusiness_61_CategoriesOut",
        "ServiceTypeIn": "_mybusiness_62_ServiceTypeIn",
        "ServiceTypeOut": "_mybusiness_63_ServiceTypeOut",
        "ProfileIn": "_mybusiness_64_ProfileIn",
        "ProfileOut": "_mybusiness_65_ProfileOut",
        "AttributeIn": "_mybusiness_66_AttributeIn",
        "AttributeOut": "_mybusiness_67_AttributeOut",
        "RepeatedEnumAttributeValueIn": "_mybusiness_68_RepeatedEnumAttributeValueIn",
        "RepeatedEnumAttributeValueOut": "_mybusiness_69_RepeatedEnumAttributeValueOut",
        "SearchGoogleLocationsRequestIn": "_mybusiness_70_SearchGoogleLocationsRequestIn",
        "SearchGoogleLocationsRequestOut": "_mybusiness_71_SearchGoogleLocationsRequestOut",
        "BatchGetCategoriesResponseIn": "_mybusiness_72_BatchGetCategoriesResponseIn",
        "BatchGetCategoriesResponseOut": "_mybusiness_73_BatchGetCategoriesResponseOut",
        "TimePeriodIn": "_mybusiness_74_TimePeriodIn",
        "TimePeriodOut": "_mybusiness_75_TimePeriodOut",
        "DateIn": "_mybusiness_76_DateIn",
        "DateOut": "_mybusiness_77_DateOut",
        "AssociateLocationRequestIn": "_mybusiness_78_AssociateLocationRequestIn",
        "AssociateLocationRequestOut": "_mybusiness_79_AssociateLocationRequestOut",
        "CategoryIn": "_mybusiness_80_CategoryIn",
        "CategoryOut": "_mybusiness_81_CategoryOut",
        "ServiceAreaBusinessIn": "_mybusiness_82_ServiceAreaBusinessIn",
        "ServiceAreaBusinessOut": "_mybusiness_83_ServiceAreaBusinessOut",
        "ChainNameIn": "_mybusiness_84_ChainNameIn",
        "ChainNameOut": "_mybusiness_85_ChainNameOut",
        "MoneyIn": "_mybusiness_86_MoneyIn",
        "MoneyOut": "_mybusiness_87_MoneyOut",
        "ClearLocationAssociationRequestIn": "_mybusiness_88_ClearLocationAssociationRequestIn",
        "ClearLocationAssociationRequestOut": "_mybusiness_89_ClearLocationAssociationRequestOut",
        "PlaceInfoIn": "_mybusiness_90_PlaceInfoIn",
        "PlaceInfoOut": "_mybusiness_91_PlaceInfoOut",
        "ListLocationsResponseIn": "_mybusiness_92_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_mybusiness_93_ListLocationsResponseOut",
        "AdWordsLocationExtensionsIn": "_mybusiness_94_AdWordsLocationExtensionsIn",
        "AdWordsLocationExtensionsOut": "_mybusiness_95_AdWordsLocationExtensionsOut",
        "PostalAddressIn": "_mybusiness_96_PostalAddressIn",
        "PostalAddressOut": "_mybusiness_97_PostalAddressOut",
        "OpenInfoIn": "_mybusiness_98_OpenInfoIn",
        "OpenInfoOut": "_mybusiness_99_OpenInfoOut",
        "MoreHoursIn": "_mybusiness_100_MoreHoursIn",
        "MoreHoursOut": "_mybusiness_101_MoreHoursOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChainIn"] = t.struct(
        {
            "locationCount": t.integer().optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameIn"])).optional(),
            "websites": t.array(t.proxy(renames["ChainUriIn"])).optional(),
        }
    ).named(renames["ChainIn"])
    types["ChainOut"] = t.struct(
        {
            "locationCount": t.integer().optional(),
            "name": t.string(),
            "chainNames": t.array(t.proxy(renames["ChainNameOut"])).optional(),
            "websites": t.array(t.proxy(renames["ChainUriOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["SpecialHoursIn"] = t.struct(
        {"specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodIn"]))}
    ).named(renames["SpecialHoursIn"])
    types["SpecialHoursOut"] = t.struct(
        {
            "specialHourPeriods": t.array(t.proxy(renames["SpecialHourPeriodOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHoursOut"])
    types["SpecialHourPeriodIn"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["SpecialHourPeriodIn"])
    types["SpecialHourPeriodOut"] = t.struct(
        {
            "closeTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]),
            "closed": t.boolean().optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "openTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecialHourPeriodOut"])
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
    types["AttributeMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "valueType": t.string().optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataIn"])
            ).optional(),
        }
    ).named(renames["AttributeMetadataIn"])
    types["AttributeMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "groupDisplayName": t.string().optional(),
            "repeatable": t.boolean().optional(),
            "valueType": t.string().optional(),
            "parent": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "valueMetadata": t.array(
                t.proxy(renames["AttributeValueMetadataOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeMetadataOut"])
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
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["LocationIn"] = t.struct(
        {
            "latlng": t.proxy(renames["LatLngIn"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "profile": t.proxy(renames["ProfileIn"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
            "websiteUri": t.string().optional(),
            "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsIn"]
            ).optional(),
            "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
            "labels": t.array(t.string()).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
            "languageCode": t.string().optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
            "name": t.string().optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "title": t.string(),
            "storeCode": t.string().optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "latlng": t.proxy(renames["LatLngOut"]).optional(),
            "storefrontAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "profile": t.proxy(renames["ProfileOut"]).optional(),
            "relationshipData": t.proxy(renames["RelationshipDataOut"]).optional(),
            "openInfo": t.proxy(renames["OpenInfoOut"]).optional(),
            "websiteUri": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "specialHours": t.proxy(renames["SpecialHoursOut"]).optional(),
            "adWordsLocationExtensions": t.proxy(
                renames["AdWordsLocationExtensionsOut"]
            ).optional(),
            "regularHours": t.proxy(renames["BusinessHoursOut"]).optional(),
            "labels": t.array(t.string()).optional(),
            "serviceArea": t.proxy(renames["ServiceAreaBusinessOut"]).optional(),
            "languageCode": t.string().optional(),
            "moreHours": t.array(t.proxy(renames["MoreHoursOut"])).optional(),
            "serviceItems": t.array(t.proxy(renames["ServiceItemOut"])).optional(),
            "name": t.string().optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "title": t.string(),
            "storeCode": t.string().optional(),
            "phoneNumbers": t.proxy(renames["PhoneNumbersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["MetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "duplicateLocation": t.string().optional(),
            "canOperateHealthData": t.boolean().optional(),
            "newReviewUri": t.string().optional(),
            "placeId": t.string().optional(),
            "canModifyServiceList": t.boolean().optional(),
            "mapsUri": t.string().optional(),
            "canHaveFoodMenus": t.boolean().optional(),
            "canOperateLocalPost": t.boolean().optional(),
            "hasGoogleUpdated": t.boolean().optional(),
            "hasVoiceOfMerchant": t.boolean().optional(),
            "canHaveBusinessCalls": t.boolean().optional(),
            "canDelete": t.boolean().optional(),
            "hasPendingEdits": t.boolean().optional(),
            "canOperateLodgingData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["ChainUriIn"] = t.struct({"uri": t.string().optional()}).named(
        renames["ChainUriIn"]
    )
    types["ChainUriOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChainUriOut"])
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
    types["UriAttributeValueIn"] = t.struct({"uri": t.string()}).named(
        renames["UriAttributeValueIn"]
    )
    types["UriAttributeValueOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UriAttributeValueOut"])
    types["SearchChainsResponseIn"] = t.struct(
        {"chains": t.array(t.proxy(renames["ChainIn"])).optional()}
    ).named(renames["SearchChainsResponseIn"])
    types["SearchChainsResponseOut"] = t.struct(
        {
            "chains": t.array(t.proxy(renames["ChainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchChainsResponseOut"])
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
    types["ProfileIn"] = t.struct({"description": t.string()}).named(
        renames["ProfileIn"]
    )
    types["ProfileOut"] = t.struct(
        {
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
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
    types["BatchGetCategoriesResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["CategoryIn"])).optional()}
    ).named(renames["BatchGetCategoriesResponseIn"])
    types["BatchGetCategoriesResponseOut"] = t.struct(
        {
            "categories": t.array(t.proxy(renames["CategoryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetCategoriesResponseOut"])
    types["TimePeriodIn"] = t.struct(
        {
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayIn"]),
            "closeTime": t.proxy(renames["TimeOfDayIn"]),
            "openDay": t.string(),
        }
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "closeDay": t.string(),
            "openTime": t.proxy(renames["TimeOfDayOut"]),
            "closeTime": t.proxy(renames["TimeOfDayOut"]),
            "openDay": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
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
    types["AssociateLocationRequestIn"] = t.struct(
        {"placeId": t.string().optional()}
    ).named(renames["AssociateLocationRequestIn"])
    types["AssociateLocationRequestOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssociateLocationRequestOut"])
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
    types["ServiceAreaBusinessIn"] = t.struct(
        {
            "businessType": t.string(),
            "places": t.proxy(renames["PlacesIn"]).optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["ServiceAreaBusinessIn"])
    types["ServiceAreaBusinessOut"] = t.struct(
        {
            "businessType": t.string(),
            "places": t.proxy(renames["PlacesOut"]).optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAreaBusinessOut"])
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
    types["ClearLocationAssociationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ClearLocationAssociationRequestIn"])
    types["ClearLocationAssociationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ClearLocationAssociationRequestOut"])
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
    types["AdWordsLocationExtensionsIn"] = t.struct({"adPhone": t.string()}).named(
        renames["AdWordsLocationExtensionsIn"]
    )
    types["AdWordsLocationExtensionsOut"] = t.struct(
        {"adPhone": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdWordsLocationExtensionsOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "sortingCode": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "locality": t.string().optional(),
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "postalCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "sortingCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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

    functions = {}
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
    functions["locationsGetAttributes"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsDelete"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGet"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateAttributes"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetGoogleUpdated"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsClearLocationAssociation"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsAssociate"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsPatch"] = mybusiness.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "latlng": t.proxy(renames["LatLngIn"]).optional(),
                "storefrontAddress": t.proxy(renames["PostalAddressIn"]).optional(),
                "profile": t.proxy(renames["ProfileIn"]).optional(),
                "relationshipData": t.proxy(renames["RelationshipDataIn"]).optional(),
                "openInfo": t.proxy(renames["OpenInfoIn"]).optional(),
                "websiteUri": t.string().optional(),
                "specialHours": t.proxy(renames["SpecialHoursIn"]).optional(),
                "adWordsLocationExtensions": t.proxy(
                    renames["AdWordsLocationExtensionsIn"]
                ).optional(),
                "regularHours": t.proxy(renames["BusinessHoursIn"]).optional(),
                "labels": t.array(t.string()).optional(),
                "serviceArea": t.proxy(renames["ServiceAreaBusinessIn"]).optional(),
                "languageCode": t.string().optional(),
                "moreHours": t.array(t.proxy(renames["MoreHoursIn"])).optional(),
                "serviceItems": t.array(t.proxy(renames["ServiceItemIn"])).optional(),
                "categories": t.proxy(renames["CategoriesIn"]).optional(),
                "title": t.string(),
                "storeCode": t.string().optional(),
                "phoneNumbers": t.proxy(renames["PhoneNumbersIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
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
    functions["attributesList"] = mybusiness.get(
        "v1/attributes",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "showAll": t.boolean().optional(),
                "regionCode": t.string().optional(),
                "parent": t.string().optional(),
                "categoryName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttributeMetadataResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLocationsCreate"] = mybusiness.get(
        "v1/{parent}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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

    return Import(
        importer="mybusiness", renames=renames, types=types, functions=functions
    )
