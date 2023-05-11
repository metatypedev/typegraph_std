from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinesslodging() -> Import:
    mybusinesslodging = HTTPRuntime("https://mybusinesslodging.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinesslodging_1_ErrorResponse",
        "LivingAreaEatingIn": "_mybusinesslodging_2_LivingAreaEatingIn",
        "LivingAreaEatingOut": "_mybusinesslodging_3_LivingAreaEatingOut",
        "LodgingIn": "_mybusinesslodging_4_LodgingIn",
        "LodgingOut": "_mybusinesslodging_5_LodgingOut",
        "HealthAndSafetyIn": "_mybusinesslodging_6_HealthAndSafetyIn",
        "HealthAndSafetyOut": "_mybusinesslodging_7_HealthAndSafetyOut",
        "PhysicalDistancingIn": "_mybusinesslodging_8_PhysicalDistancingIn",
        "PhysicalDistancingOut": "_mybusinesslodging_9_PhysicalDistancingOut",
        "PropertyIn": "_mybusinesslodging_10_PropertyIn",
        "PropertyOut": "_mybusinesslodging_11_PropertyOut",
        "ParkingIn": "_mybusinesslodging_12_ParkingIn",
        "ParkingOut": "_mybusinesslodging_13_ParkingOut",
        "ConnectivityIn": "_mybusinesslodging_14_ConnectivityIn",
        "ConnectivityOut": "_mybusinesslodging_15_ConnectivityOut",
        "LivingAreaLayoutIn": "_mybusinesslodging_16_LivingAreaLayoutIn",
        "LivingAreaLayoutOut": "_mybusinesslodging_17_LivingAreaLayoutOut",
        "GuestUnitFeaturesIn": "_mybusinesslodging_18_GuestUnitFeaturesIn",
        "GuestUnitFeaturesOut": "_mybusinesslodging_19_GuestUnitFeaturesOut",
        "ServicesIn": "_mybusinesslodging_20_ServicesIn",
        "ServicesOut": "_mybusinesslodging_21_ServicesOut",
        "PersonalProtectionIn": "_mybusinesslodging_22_PersonalProtectionIn",
        "PersonalProtectionOut": "_mybusinesslodging_23_PersonalProtectionOut",
        "LivingAreaFeaturesIn": "_mybusinesslodging_24_LivingAreaFeaturesIn",
        "LivingAreaFeaturesOut": "_mybusinesslodging_25_LivingAreaFeaturesOut",
        "FoodAndDrinkIn": "_mybusinesslodging_26_FoodAndDrinkIn",
        "FoodAndDrinkOut": "_mybusinesslodging_27_FoodAndDrinkOut",
        "ActivitiesIn": "_mybusinesslodging_28_ActivitiesIn",
        "ActivitiesOut": "_mybusinesslodging_29_ActivitiesOut",
        "PoolsIn": "_mybusinesslodging_30_PoolsIn",
        "PoolsOut": "_mybusinesslodging_31_PoolsOut",
        "HousekeepingIn": "_mybusinesslodging_32_HousekeepingIn",
        "HousekeepingOut": "_mybusinesslodging_33_HousekeepingOut",
        "SustainableSourcingIn": "_mybusinesslodging_34_SustainableSourcingIn",
        "SustainableSourcingOut": "_mybusinesslodging_35_SustainableSourcingOut",
        "PaymentOptionsIn": "_mybusinesslodging_36_PaymentOptionsIn",
        "PaymentOptionsOut": "_mybusinesslodging_37_PaymentOptionsOut",
        "GetGoogleUpdatedLodgingResponseIn": "_mybusinesslodging_38_GetGoogleUpdatedLodgingResponseIn",
        "GetGoogleUpdatedLodgingResponseOut": "_mybusinesslodging_39_GetGoogleUpdatedLodgingResponseOut",
        "EnergyEfficiencyIn": "_mybusinesslodging_40_EnergyEfficiencyIn",
        "EnergyEfficiencyOut": "_mybusinesslodging_41_EnergyEfficiencyOut",
        "EnhancedCleaningIn": "_mybusinesslodging_42_EnhancedCleaningIn",
        "EnhancedCleaningOut": "_mybusinesslodging_43_EnhancedCleaningOut",
        "LivingAreaSleepingIn": "_mybusinesslodging_44_LivingAreaSleepingIn",
        "LivingAreaSleepingOut": "_mybusinesslodging_45_LivingAreaSleepingOut",
        "BusinessIn": "_mybusinesslodging_46_BusinessIn",
        "BusinessOut": "_mybusinesslodging_47_BusinessOut",
        "SustainabilityIn": "_mybusinesslodging_48_SustainabilityIn",
        "SustainabilityOut": "_mybusinesslodging_49_SustainabilityOut",
        "TimeOfDayIn": "_mybusinesslodging_50_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinesslodging_51_TimeOfDayOut",
        "EcoCertificationIn": "_mybusinesslodging_52_EcoCertificationIn",
        "EcoCertificationOut": "_mybusinesslodging_53_EcoCertificationOut",
        "WaterConservationIn": "_mybusinesslodging_54_WaterConservationIn",
        "WaterConservationOut": "_mybusinesslodging_55_WaterConservationOut",
        "IncreasedFoodSafetyIn": "_mybusinesslodging_56_IncreasedFoodSafetyIn",
        "IncreasedFoodSafetyOut": "_mybusinesslodging_57_IncreasedFoodSafetyOut",
        "PetsIn": "_mybusinesslodging_58_PetsIn",
        "PetsOut": "_mybusinesslodging_59_PetsOut",
        "ViewsFromUnitIn": "_mybusinesslodging_60_ViewsFromUnitIn",
        "ViewsFromUnitOut": "_mybusinesslodging_61_ViewsFromUnitOut",
        "FamiliesIn": "_mybusinesslodging_62_FamiliesIn",
        "FamiliesOut": "_mybusinesslodging_63_FamiliesOut",
        "WellnessIn": "_mybusinesslodging_64_WellnessIn",
        "WellnessOut": "_mybusinesslodging_65_WellnessOut",
        "WasteReductionIn": "_mybusinesslodging_66_WasteReductionIn",
        "WasteReductionOut": "_mybusinesslodging_67_WasteReductionOut",
        "LivingAreaAccessibilityIn": "_mybusinesslodging_68_LivingAreaAccessibilityIn",
        "LivingAreaAccessibilityOut": "_mybusinesslodging_69_LivingAreaAccessibilityOut",
        "AccessibilityIn": "_mybusinesslodging_70_AccessibilityIn",
        "AccessibilityOut": "_mybusinesslodging_71_AccessibilityOut",
        "SustainabilityCertificationsIn": "_mybusinesslodging_72_SustainabilityCertificationsIn",
        "SustainabilityCertificationsOut": "_mybusinesslodging_73_SustainabilityCertificationsOut",
        "LivingAreaIn": "_mybusinesslodging_74_LivingAreaIn",
        "LivingAreaOut": "_mybusinesslodging_75_LivingAreaOut",
        "LanguageSpokenIn": "_mybusinesslodging_76_LanguageSpokenIn",
        "LanguageSpokenOut": "_mybusinesslodging_77_LanguageSpokenOut",
        "MinimizedContactIn": "_mybusinesslodging_78_MinimizedContactIn",
        "MinimizedContactOut": "_mybusinesslodging_79_MinimizedContactOut",
        "TransportationIn": "_mybusinesslodging_80_TransportationIn",
        "TransportationOut": "_mybusinesslodging_81_TransportationOut",
        "PoliciesIn": "_mybusinesslodging_82_PoliciesIn",
        "PoliciesOut": "_mybusinesslodging_83_PoliciesOut",
        "LodgingMetadataIn": "_mybusinesslodging_84_LodgingMetadataIn",
        "LodgingMetadataOut": "_mybusinesslodging_85_LodgingMetadataOut",
        "GuestUnitTypeIn": "_mybusinesslodging_86_GuestUnitTypeIn",
        "GuestUnitTypeOut": "_mybusinesslodging_87_GuestUnitTypeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LivingAreaEatingIn"] = t.struct(
        {
            "minibarException": t.string().optional(),
            "sinkException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "refrigeratorException": t.string().optional(),
            "kettleException": t.string().optional(),
            "sink": t.boolean().optional(),
            "indoorGrillException": t.string().optional(),
            "ovenException": t.string().optional(),
            "stove": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "cookwareException": t.string().optional(),
            "cookware": t.boolean().optional(),
            "microwave": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "coffeeMaker": t.boolean().optional(),
            "outdoorGrill": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "kettle": t.boolean().optional(),
            "outdoorGrillException": t.string().optional(),
            "stoveException": t.string().optional(),
            "microwaveException": t.string().optional(),
            "coffeeMakerException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "oven": t.boolean().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "snackbar": t.boolean().optional(),
            "toaster": t.boolean().optional(),
            "refrigerator": t.boolean().optional(),
            "minibar": t.boolean().optional(),
        }
    ).named(renames["LivingAreaEatingIn"])
    types["LivingAreaEatingOut"] = t.struct(
        {
            "minibarException": t.string().optional(),
            "sinkException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "refrigeratorException": t.string().optional(),
            "kettleException": t.string().optional(),
            "sink": t.boolean().optional(),
            "indoorGrillException": t.string().optional(),
            "ovenException": t.string().optional(),
            "stove": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "cookwareException": t.string().optional(),
            "cookware": t.boolean().optional(),
            "microwave": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "coffeeMaker": t.boolean().optional(),
            "outdoorGrill": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "kettle": t.boolean().optional(),
            "outdoorGrillException": t.string().optional(),
            "stoveException": t.string().optional(),
            "microwaveException": t.string().optional(),
            "coffeeMakerException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "oven": t.boolean().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "snackbar": t.boolean().optional(),
            "toaster": t.boolean().optional(),
            "refrigerator": t.boolean().optional(),
            "minibar": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaEatingOut"])
    types["LodgingIn"] = t.struct(
        {
            "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
            "activities": t.proxy(renames["ActivitiesIn"]).optional(),
            "parking": t.proxy(renames["ParkingIn"]).optional(),
            "pools": t.proxy(renames["PoolsIn"]).optional(),
            "name": t.string(),
            "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
            "services": t.proxy(renames["ServicesIn"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataIn"]),
            "policies": t.proxy(renames["PoliciesIn"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
            "pets": t.proxy(renames["PetsIn"]).optional(),
            "business": t.proxy(renames["BusinessIn"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
            "wellness": t.proxy(renames["WellnessIn"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
            "property": t.proxy(renames["PropertyIn"]).optional(),
            "transportation": t.proxy(renames["TransportationIn"]).optional(),
            "families": t.proxy(renames["FamiliesIn"]).optional(),
        }
    ).named(renames["LodgingIn"])
    types["LodgingOut"] = t.struct(
        {
            "accessibility": t.proxy(renames["AccessibilityOut"]).optional(),
            "activities": t.proxy(renames["ActivitiesOut"]).optional(),
            "parking": t.proxy(renames["ParkingOut"]).optional(),
            "pools": t.proxy(renames["PoolsOut"]).optional(),
            "name": t.string(),
            "someUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingOut"]).optional(),
            "services": t.proxy(renames["ServicesOut"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityOut"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataOut"]),
            "policies": t.proxy(renames["PoliciesOut"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeOut"])).optional(),
            "pets": t.proxy(renames["PetsOut"]).optional(),
            "business": t.proxy(renames["BusinessOut"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaOut"]).optional(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkOut"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyOut"]).optional(),
            "wellness": t.proxy(renames["WellnessOut"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityOut"]).optional(),
            "property": t.proxy(renames["PropertyOut"]).optional(),
            "allUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "transportation": t.proxy(renames["TransportationOut"]).optional(),
            "families": t.proxy(renames["FamiliesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingOut"])
    types["HealthAndSafetyIn"] = t.struct(
        {
            "physicalDistancing": t.proxy(renames["PhysicalDistancingIn"]).optional(),
            "increasedFoodSafety": t.proxy(renames["IncreasedFoodSafetyIn"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionIn"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactIn"]).optional(),
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningIn"]).optional(),
        }
    ).named(renames["HealthAndSafetyIn"])
    types["HealthAndSafetyOut"] = t.struct(
        {
            "physicalDistancing": t.proxy(renames["PhysicalDistancingOut"]).optional(),
            "increasedFoodSafety": t.proxy(
                renames["IncreasedFoodSafetyOut"]
            ).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionOut"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactOut"]).optional(),
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthAndSafetyOut"])
    types["PhysicalDistancingIn"] = t.struct(
        {
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "safetyDividersException": t.string().optional(),
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
        }
    ).named(renames["PhysicalDistancingIn"])
    types["PhysicalDistancingOut"] = t.struct(
        {
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "safetyDividersException": t.string().optional(),
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalDistancingOut"])
    types["PropertyIn"] = t.struct(
        {
            "builtYear": t.integer().optional(),
            "roomsCount": t.integer().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "floorsCountException": t.string().optional(),
            "roomsCountException": t.string().optional(),
            "floorsCount": t.integer().optional(),
            "lastRenovatedYearException": t.string().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "builtYear": t.integer().optional(),
            "roomsCount": t.integer().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "floorsCountException": t.string().optional(),
            "roomsCountException": t.string().optional(),
            "floorsCount": t.integer().optional(),
            "lastRenovatedYearException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["ParkingIn"] = t.struct(
        {
            "valetParkingAvailable": t.boolean().optional(),
            "freeSelfParking": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
            "parkingAvailableException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "parkingAvailable": t.boolean().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeValetParkingException": t.string().optional(),
            "selfParkingAvailableException": t.string().optional(),
        }
    ).named(renames["ParkingIn"])
    types["ParkingOut"] = t.struct(
        {
            "valetParkingAvailable": t.boolean().optional(),
            "freeSelfParking": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
            "parkingAvailableException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "parkingAvailable": t.boolean().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeValetParkingException": t.string().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParkingOut"])
    types["ConnectivityIn"] = t.struct(
        {
            "wifiAvailable": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
            "freeWifi": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
        }
    ).named(renames["ConnectivityIn"])
    types["ConnectivityOut"] = t.struct(
        {
            "wifiAvailable": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
            "freeWifi": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityOut"])
    types["LivingAreaLayoutIn"] = t.struct(
        {
            "livingAreaSqMetersException": t.string().optional(),
            "patioException": t.string().optional(),
            "nonSmokingException": t.string().optional(),
            "balconyException": t.string().optional(),
            "nonSmoking": t.boolean().optional(),
            "balcony": t.boolean().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "patio": t.boolean().optional(),
            "loft": t.boolean().optional(),
            "stairsException": t.string().optional(),
            "loftException": t.string().optional(),
            "stairs": t.boolean().optional(),
        }
    ).named(renames["LivingAreaLayoutIn"])
    types["LivingAreaLayoutOut"] = t.struct(
        {
            "livingAreaSqMetersException": t.string().optional(),
            "patioException": t.string().optional(),
            "nonSmokingException": t.string().optional(),
            "balconyException": t.string().optional(),
            "nonSmoking": t.boolean().optional(),
            "balcony": t.boolean().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "patio": t.boolean().optional(),
            "loft": t.boolean().optional(),
            "stairsException": t.string().optional(),
            "loftException": t.string().optional(),
            "stairs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaLayoutOut"])
    types["GuestUnitFeaturesIn"] = t.struct(
        {
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "tierException": t.string().optional(),
            "suiteException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "executiveFloor": t.boolean().optional(),
            "privateHome": t.boolean().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaIn"]).optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "tier": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "views": t.proxy(renames["ViewsFromUnitIn"]).optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "executiveFloorException": t.string().optional(),
            "suite": t.boolean().optional(),
        }
    ).named(renames["GuestUnitFeaturesIn"])
    types["GuestUnitFeaturesOut"] = t.struct(
        {
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "tierException": t.string().optional(),
            "suiteException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "executiveFloor": t.boolean().optional(),
            "privateHome": t.boolean().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaOut"]).optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "tier": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "views": t.proxy(renames["ViewsFromUnitOut"]).optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "executiveFloorException": t.string().optional(),
            "suite": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitFeaturesOut"])
    types["ServicesIn"] = t.struct(
        {
            "currencyExchange": t.boolean().optional(),
            "frontDeskException": t.string().optional(),
            "elevatorException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "convenienceStore": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "languagesSpoken": t.array(t.proxy(renames["LanguageSpokenIn"])).optional(),
            "giftShop": t.boolean().optional(),
            "wakeUpCallsException": t.string().optional(),
            "convenienceStoreException": t.string().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "concierge": t.boolean().optional(),
            "frontDesk": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "elevator": t.boolean().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "socialHourException": t.string().optional(),
        }
    ).named(renames["ServicesIn"])
    types["ServicesOut"] = t.struct(
        {
            "currencyExchange": t.boolean().optional(),
            "frontDeskException": t.string().optional(),
            "elevatorException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "convenienceStore": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "languagesSpoken": t.array(
                t.proxy(renames["LanguageSpokenOut"])
            ).optional(),
            "giftShop": t.boolean().optional(),
            "wakeUpCallsException": t.string().optional(),
            "convenienceStoreException": t.string().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "concierge": t.boolean().optional(),
            "frontDesk": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "elevator": t.boolean().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "socialHourException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicesOut"])
    types["PersonalProtectionIn"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
        }
    ).named(renames["PersonalProtectionIn"])
    types["PersonalProtectionOut"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalProtectionOut"])
    types["LivingAreaFeaturesIn"] = t.struct(
        {
            "ironingEquipmentException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "airConditioning": t.boolean().optional(),
            "tvCasting": t.boolean().optional(),
            "toilet": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "dryerException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "hairdryer": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "heatingException": t.string().optional(),
            "heating": t.boolean().optional(),
            "tvException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "shower": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "tvStreaming": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "hairdryerException": t.string().optional(),
            "dryer": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "fireplace": t.boolean().optional(),
            "washer": t.boolean().optional(),
            "toiletException": t.string().optional(),
            "bathtubException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "washerException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "bidetException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "showerException": t.string().optional(),
        }
    ).named(renames["LivingAreaFeaturesIn"])
    types["LivingAreaFeaturesOut"] = t.struct(
        {
            "ironingEquipmentException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "airConditioning": t.boolean().optional(),
            "tvCasting": t.boolean().optional(),
            "toilet": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "dryerException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "hairdryer": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "heatingException": t.string().optional(),
            "heating": t.boolean().optional(),
            "tvException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "shower": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "tvStreaming": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "hairdryerException": t.string().optional(),
            "dryer": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "fireplace": t.boolean().optional(),
            "washer": t.boolean().optional(),
            "toiletException": t.string().optional(),
            "bathtubException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "washerException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "bidetException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "showerException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaFeaturesOut"])
    types["FoodAndDrinkIn"] = t.struct(
        {
            "breakfastBuffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurant": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "freeBreakfastException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "freeBreakfast": t.boolean().optional(),
            "roomServiceException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "restaurantsCount": t.integer().optional(),
            "vendingMachineException": t.string().optional(),
            "roomService": t.boolean().optional(),
            "breakfastBuffetException": t.string().optional(),
            "buffetException": t.string().optional(),
            "barException": t.string().optional(),
            "bar": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "tableService": t.boolean().optional(),
            "breakfastAvailableException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "tableServiceException": t.string().optional(),
        }
    ).named(renames["FoodAndDrinkIn"])
    types["FoodAndDrinkOut"] = t.struct(
        {
            "breakfastBuffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurant": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "freeBreakfastException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "freeBreakfast": t.boolean().optional(),
            "roomServiceException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "restaurantsCount": t.integer().optional(),
            "vendingMachineException": t.string().optional(),
            "roomService": t.boolean().optional(),
            "breakfastBuffetException": t.string().optional(),
            "buffetException": t.string().optional(),
            "barException": t.string().optional(),
            "bar": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "tableService": t.boolean().optional(),
            "breakfastAvailableException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "tableServiceException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FoodAndDrinkOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "casinoException": t.string().optional(),
            "bicycleRental": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "beachAccessException": t.string().optional(),
            "bicycleRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "boutiqueStores": t.boolean().optional(),
            "gameRoom": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "privateBeach": t.boolean().optional(),
            "golf": t.boolean().optional(),
            "beachFront": t.boolean().optional(),
            "nightclub": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "golfException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
            "horsebackRidingException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "scuba": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "scubaException": t.string().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "horsebackRiding": t.boolean().optional(),
            "tennis": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "gameRoomException": t.string().optional(),
            "snorkeling": t.boolean().optional(),
            "waterSkiing": t.boolean().optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "casinoException": t.string().optional(),
            "bicycleRental": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "beachAccessException": t.string().optional(),
            "bicycleRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "boutiqueStores": t.boolean().optional(),
            "gameRoom": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "privateBeach": t.boolean().optional(),
            "golf": t.boolean().optional(),
            "beachFront": t.boolean().optional(),
            "nightclub": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "golfException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
            "horsebackRidingException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "scuba": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "scubaException": t.string().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "horsebackRiding": t.boolean().optional(),
            "tennis": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "gameRoomException": t.string().optional(),
            "snorkeling": t.boolean().optional(),
            "waterSkiing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["PoolsIn"] = t.struct(
        {
            "outdoorPoolsCount": t.integer().optional(),
            "lifeguardException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "wavePool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "outdoorPoolException": t.string().optional(),
            "outdoorPool": t.boolean().optional(),
            "indoorPoolException": t.string().optional(),
            "wadingPool": t.boolean().optional(),
            "adultPoolException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "wadingPoolException": t.string().optional(),
            "lazyRiverException": t.string().optional(),
            "waterslideException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "pool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "poolException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "waterParkException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
            "adultPool": t.boolean().optional(),
            "lifeguard": t.boolean().optional(),
        }
    ).named(renames["PoolsIn"])
    types["PoolsOut"] = t.struct(
        {
            "outdoorPoolsCount": t.integer().optional(),
            "lifeguardException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "wavePool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "outdoorPoolException": t.string().optional(),
            "outdoorPool": t.boolean().optional(),
            "indoorPoolException": t.string().optional(),
            "wadingPool": t.boolean().optional(),
            "adultPoolException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "wadingPoolException": t.string().optional(),
            "lazyRiverException": t.string().optional(),
            "waterslideException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "pool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "poolException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "waterParkException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
            "adultPool": t.boolean().optional(),
            "lifeguard": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolsOut"])
    types["HousekeepingIn"] = t.struct(
        {
            "dailyHousekeepingException": t.string().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "housekeepingAvailableException": t.string().optional(),
        }
    ).named(renames["HousekeepingIn"])
    types["HousekeepingOut"] = t.struct(
        {
            "dailyHousekeepingException": t.string().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "housekeepingAvailableException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HousekeepingOut"])
    types["SustainableSourcingIn"] = t.struct(
        {
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "vegetarianMealsException": t.string().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "veganMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
        }
    ).named(renames["SustainableSourcingIn"])
    types["SustainableSourcingOut"] = t.struct(
        {
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "vegetarianMealsException": t.string().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "veganMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainableSourcingOut"])
    types["PaymentOptionsIn"] = t.struct(
        {
            "debitCard": t.boolean().optional(),
            "cashException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "cash": t.boolean().optional(),
            "creditCardException": t.string().optional(),
            "creditCard": t.boolean().optional(),
            "debitCardException": t.string().optional(),
            "cheque": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "chequeException": t.string().optional(),
        }
    ).named(renames["PaymentOptionsIn"])
    types["PaymentOptionsOut"] = t.struct(
        {
            "debitCard": t.boolean().optional(),
            "cashException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "cash": t.boolean().optional(),
            "creditCardException": t.string().optional(),
            "creditCard": t.boolean().optional(),
            "debitCardException": t.string().optional(),
            "cheque": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "chequeException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOptionsOut"])
    types["GetGoogleUpdatedLodgingResponseIn"] = t.struct(
        {"diffMask": t.string(), "lodging": t.proxy(renames["LodgingIn"])}
    ).named(renames["GetGoogleUpdatedLodgingResponseIn"])
    types["GetGoogleUpdatedLodgingResponseOut"] = t.struct(
        {
            "diffMask": t.string(),
            "lodging": t.proxy(renames["LodgingOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetGoogleUpdatedLodgingResponseOut"])
    types["EnergyEfficiencyIn"] = t.struct(
        {
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyConservationProgramException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "energyEfficientLightingException": t.string().optional(),
        }
    ).named(renames["EnergyEfficiencyIn"])
    types["EnergyEfficiencyOut"] = t.struct(
        {
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "greenBuildingDesignException": t.string().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyConservationProgramException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "greenBuildingDesign": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnergyEfficiencyOut"])
    types["EnhancedCleaningIn"] = t.struct(
        {
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
        }
    ).named(renames["EnhancedCleaningIn"])
    types["EnhancedCleaningOut"] = t.struct(
        {
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnhancedCleaningOut"])
    types["LivingAreaSleepingIn"] = t.struct(
        {
            "featherPillows": t.boolean().optional(),
            "sofaBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCount": t.integer().optional(),
            "cribsCountException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "bunkBedsCountException": t.string().optional(),
            "sofaBedsCountException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "doubleBedsCountException": t.string().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "kingBedsCount": t.integer().optional(),
            "bedsCount": t.integer().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "queenBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "syntheticPillows": t.boolean().optional(),
            "otherBedsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "bunkBedsCount": t.integer().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "bedsCountException": t.string().optional(),
        }
    ).named(renames["LivingAreaSleepingIn"])
    types["LivingAreaSleepingOut"] = t.struct(
        {
            "featherPillows": t.boolean().optional(),
            "sofaBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCount": t.integer().optional(),
            "cribsCountException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "bunkBedsCountException": t.string().optional(),
            "sofaBedsCountException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "doubleBedsCountException": t.string().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "kingBedsCount": t.integer().optional(),
            "bedsCount": t.integer().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "queenBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "syntheticPillows": t.boolean().optional(),
            "otherBedsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "bunkBedsCount": t.integer().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "bedsCountException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaSleepingOut"])
    types["BusinessIn"] = t.struct(
        {
            "meetingRooms": t.boolean().optional(),
            "meetingRoomsException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "businessCenter": t.boolean().optional(),
        }
    ).named(renames["BusinessIn"])
    types["BusinessOut"] = t.struct(
        {
            "meetingRooms": t.boolean().optional(),
            "meetingRoomsException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "businessCenter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessOut"])
    types["SustainabilityIn"] = t.struct(
        {
            "sustainableSourcing": t.proxy(renames["SustainableSourcingIn"]).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyIn"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsIn"]
            ).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionIn"]).optional(),
            "waterConservation": t.proxy(renames["WaterConservationIn"]).optional(),
        }
    ).named(renames["SustainabilityIn"])
    types["SustainabilityOut"] = t.struct(
        {
            "sustainableSourcing": t.proxy(
                renames["SustainableSourcingOut"]
            ).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyOut"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsOut"]
            ).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionOut"]).optional(),
            "waterConservation": t.proxy(renames["WaterConservationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["EcoCertificationIn"] = t.struct(
        {
            "awardedException": t.string().optional(),
            "awarded": t.boolean().optional(),
            "ecoCertificate": t.string(),
        }
    ).named(renames["EcoCertificationIn"])
    types["EcoCertificationOut"] = t.struct(
        {
            "awardedException": t.string().optional(),
            "awarded": t.boolean().optional(),
            "ecoCertificate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcoCertificationOut"])
    types["WaterConservationIn"] = t.struct(
        {
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "linenReuseProgramException": t.string().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
        }
    ).named(renames["WaterConservationIn"])
    types["WaterConservationOut"] = t.struct(
        {
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "linenReuseProgramException": t.string().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterConservationOut"])
    types["IncreasedFoodSafetyIn"] = t.struct(
        {
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "disposableFlatwareException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "disposableFlatware": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
        }
    ).named(renames["IncreasedFoodSafetyIn"])
    types["IncreasedFoodSafetyOut"] = t.struct(
        {
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "disposableFlatwareException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "disposableFlatware": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncreasedFoodSafetyOut"])
    types["PetsIn"] = t.struct(
        {
            "catsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowed": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowedFreeException": t.string().optional(),
        }
    ).named(renames["PetsIn"])
    types["PetsOut"] = t.struct(
        {
            "catsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowed": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowedFreeException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PetsOut"])
    types["ViewsFromUnitIn"] = t.struct(
        {
            "gardenViewException": t.string().optional(),
            "cityViewException": t.string().optional(),
            "valleyViewException": t.string().optional(),
            "gardenView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "lakeViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "beachViewException": t.string().optional(),
            "oceanView": t.boolean().optional(),
            "oceanViewException": t.string().optional(),
            "landmarkView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "valleyView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
        }
    ).named(renames["ViewsFromUnitIn"])
    types["ViewsFromUnitOut"] = t.struct(
        {
            "gardenViewException": t.string().optional(),
            "cityViewException": t.string().optional(),
            "valleyViewException": t.string().optional(),
            "gardenView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "lakeViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "beachViewException": t.string().optional(),
            "oceanView": t.boolean().optional(),
            "oceanViewException": t.string().optional(),
            "landmarkView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "valleyView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewsFromUnitOut"])
    types["FamiliesIn"] = t.struct(
        {
            "kidsActivities": t.boolean().optional(),
            "kidsFriendly": t.boolean().optional(),
            "kidsActivitiesException": t.string().optional(),
            "babysitting": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
            "babysittingException": t.string().optional(),
        }
    ).named(renames["FamiliesIn"])
    types["FamiliesOut"] = t.struct(
        {
            "kidsActivities": t.boolean().optional(),
            "kidsFriendly": t.boolean().optional(),
            "kidsActivitiesException": t.string().optional(),
            "babysitting": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
            "babysittingException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamiliesOut"])
    types["WellnessIn"] = t.struct(
        {
            "treadmillException": t.string().optional(),
            "weightMachine": t.boolean().optional(),
            "massage": t.boolean().optional(),
            "fitnessCenterException": t.string().optional(),
            "freeFitnessCenter": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "saunaException": t.string().optional(),
            "freeWeights": t.boolean().optional(),
            "massageException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "doctorOnCallException": t.string().optional(),
            "salonException": t.string().optional(),
            "freeWeightsException": t.string().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "salon": t.boolean().optional(),
            "fitnessCenter": t.boolean().optional(),
            "spaException": t.string().optional(),
            "weightMachineException": t.string().optional(),
        }
    ).named(renames["WellnessIn"])
    types["WellnessOut"] = t.struct(
        {
            "treadmillException": t.string().optional(),
            "weightMachine": t.boolean().optional(),
            "massage": t.boolean().optional(),
            "fitnessCenterException": t.string().optional(),
            "freeFitnessCenter": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "saunaException": t.string().optional(),
            "freeWeights": t.boolean().optional(),
            "massageException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "doctorOnCallException": t.string().optional(),
            "salonException": t.string().optional(),
            "freeWeightsException": t.string().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "salon": t.boolean().optional(),
            "fitnessCenter": t.boolean().optional(),
            "spaException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WellnessOut"])
    types["WasteReductionIn"] = t.struct(
        {
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "recyclingProgramException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
        }
    ).named(renames["WasteReductionIn"])
    types["WasteReductionOut"] = t.struct(
        {
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "recyclingProgramException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WasteReductionOut"])
    types["LivingAreaAccessibilityIn"] = t.struct(
        {
            "hearingAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
        }
    ).named(renames["LivingAreaAccessibilityIn"])
    types["LivingAreaAccessibilityOut"] = t.struct(
        {
            "hearingAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaAccessibilityOut"])
    types["AccessibilityIn"] = t.struct(
        {
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
        }
    ).named(renames["AccessibilityIn"])
    types["AccessibilityOut"] = t.struct(
        {
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessibilityOut"])
    types["SustainabilityCertificationsIn"] = t.struct(
        {
            "breeamCertificationException": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationIn"])
            ).optional(),
            "leedCertification": t.string().optional(),
        }
    ).named(renames["SustainabilityCertificationsIn"])
    types["SustainabilityCertificationsOut"] = t.struct(
        {
            "breeamCertificationException": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationOut"])
            ).optional(),
            "leedCertification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityCertificationsOut"])
    types["LivingAreaIn"] = t.struct(
        {
            "features": t.proxy(renames["LivingAreaFeaturesIn"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingIn"]).optional(),
            "layout": t.proxy(renames["LivingAreaLayoutIn"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingIn"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityIn"]).optional(),
        }
    ).named(renames["LivingAreaIn"])
    types["LivingAreaOut"] = t.struct(
        {
            "features": t.proxy(renames["LivingAreaFeaturesOut"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingOut"]).optional(),
            "layout": t.proxy(renames["LivingAreaLayoutOut"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingOut"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaOut"])
    types["LanguageSpokenIn"] = t.struct(
        {
            "spokenException": t.string().optional(),
            "languageCode": t.string(),
            "spoken": t.boolean().optional(),
        }
    ).named(renames["LanguageSpokenIn"])
    types["LanguageSpokenOut"] = t.struct(
        {
            "spokenException": t.string().optional(),
            "languageCode": t.string(),
            "spoken": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSpokenOut"])
    types["MinimizedContactIn"] = t.struct(
        {
            "contactlessCheckinCheckout": t.boolean().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
        }
    ).named(renames["MinimizedContactIn"])
    types["MinimizedContactOut"] = t.struct(
        {
            "contactlessCheckinCheckout": t.boolean().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimizedContactOut"])
    types["TransportationIn"] = t.struct(
        {
            "freePrivateCarService": t.boolean().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "transferException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "localShuttleException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "transfer": t.boolean().optional(),
        }
    ).named(renames["TransportationIn"])
    types["TransportationOut"] = t.struct(
        {
            "freePrivateCarService": t.boolean().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "transferException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "localShuttleException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "transfer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportationOut"])
    types["PoliciesIn"] = t.struct(
        {
            "checkinTimeException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "checkoutTimeException": t.string().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "kidsStayFree": t.boolean().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "maxChildAgeException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "maxChildAge": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsIn"]).optional(),
            "kidsStayFreeException": t.string().optional(),
        }
    ).named(renames["PoliciesIn"])
    types["PoliciesOut"] = t.struct(
        {
            "checkinTimeException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "checkoutTimeException": t.string().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "kidsStayFree": t.boolean().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "maxChildAgeException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "maxChildAge": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsOut"]).optional(),
            "kidsStayFreeException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesOut"])
    types["LodgingMetadataIn"] = t.struct({"updateTime": t.string()}).named(
        renames["LodgingMetadataIn"]
    )
    types["LodgingMetadataOut"] = t.struct(
        {
            "updateTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingMetadataOut"])
    types["GuestUnitTypeIn"] = t.struct(
        {
            "label": t.string(),
            "codes": t.array(t.string()),
            "features": t.proxy(renames["GuestUnitFeaturesIn"]).optional(),
        }
    ).named(renames["GuestUnitTypeIn"])
    types["GuestUnitTypeOut"] = t.struct(
        {
            "label": t.string(),
            "codes": t.array(t.string()),
            "features": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitTypeOut"])

    functions = {}
    functions["locationsUpdateLodging"] = mybusinesslodging.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LodgingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsGetLodging"] = mybusinesslodging.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LodgingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsLodgingGetGoogleUpdated"] = mybusinesslodging.get(
        "v1/{name}:getGoogleUpdated",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GetGoogleUpdatedLodgingResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinesslodging", renames=renames, types=types, functions=functions
    )
