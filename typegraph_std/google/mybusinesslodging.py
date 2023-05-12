from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_mybusinesslodging() -> Import:
    mybusinesslodging = HTTPRuntime("https://mybusinesslodging.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinesslodging_1_ErrorResponse",
        "PaymentOptionsIn": "_mybusinesslodging_2_PaymentOptionsIn",
        "PaymentOptionsOut": "_mybusinesslodging_3_PaymentOptionsOut",
        "TransportationIn": "_mybusinesslodging_4_TransportationIn",
        "TransportationOut": "_mybusinesslodging_5_TransportationOut",
        "GetGoogleUpdatedLodgingResponseIn": "_mybusinesslodging_6_GetGoogleUpdatedLodgingResponseIn",
        "GetGoogleUpdatedLodgingResponseOut": "_mybusinesslodging_7_GetGoogleUpdatedLodgingResponseOut",
        "LivingAreaFeaturesIn": "_mybusinesslodging_8_LivingAreaFeaturesIn",
        "LivingAreaFeaturesOut": "_mybusinesslodging_9_LivingAreaFeaturesOut",
        "GuestUnitTypeIn": "_mybusinesslodging_10_GuestUnitTypeIn",
        "GuestUnitTypeOut": "_mybusinesslodging_11_GuestUnitTypeOut",
        "ConnectivityIn": "_mybusinesslodging_12_ConnectivityIn",
        "ConnectivityOut": "_mybusinesslodging_13_ConnectivityOut",
        "LivingAreaEatingIn": "_mybusinesslodging_14_LivingAreaEatingIn",
        "LivingAreaEatingOut": "_mybusinesslodging_15_LivingAreaEatingOut",
        "LodgingMetadataIn": "_mybusinesslodging_16_LodgingMetadataIn",
        "LodgingMetadataOut": "_mybusinesslodging_17_LodgingMetadataOut",
        "IncreasedFoodSafetyIn": "_mybusinesslodging_18_IncreasedFoodSafetyIn",
        "IncreasedFoodSafetyOut": "_mybusinesslodging_19_IncreasedFoodSafetyOut",
        "EcoCertificationIn": "_mybusinesslodging_20_EcoCertificationIn",
        "EcoCertificationOut": "_mybusinesslodging_21_EcoCertificationOut",
        "MinimizedContactIn": "_mybusinesslodging_22_MinimizedContactIn",
        "MinimizedContactOut": "_mybusinesslodging_23_MinimizedContactOut",
        "EnhancedCleaningIn": "_mybusinesslodging_24_EnhancedCleaningIn",
        "EnhancedCleaningOut": "_mybusinesslodging_25_EnhancedCleaningOut",
        "SustainabilityIn": "_mybusinesslodging_26_SustainabilityIn",
        "SustainabilityOut": "_mybusinesslodging_27_SustainabilityOut",
        "TimeOfDayIn": "_mybusinesslodging_28_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinesslodging_29_TimeOfDayOut",
        "PersonalProtectionIn": "_mybusinesslodging_30_PersonalProtectionIn",
        "PersonalProtectionOut": "_mybusinesslodging_31_PersonalProtectionOut",
        "WasteReductionIn": "_mybusinesslodging_32_WasteReductionIn",
        "WasteReductionOut": "_mybusinesslodging_33_WasteReductionOut",
        "WaterConservationIn": "_mybusinesslodging_34_WaterConservationIn",
        "WaterConservationOut": "_mybusinesslodging_35_WaterConservationOut",
        "LanguageSpokenIn": "_mybusinesslodging_36_LanguageSpokenIn",
        "LanguageSpokenOut": "_mybusinesslodging_37_LanguageSpokenOut",
        "ServicesIn": "_mybusinesslodging_38_ServicesIn",
        "ServicesOut": "_mybusinesslodging_39_ServicesOut",
        "PropertyIn": "_mybusinesslodging_40_PropertyIn",
        "PropertyOut": "_mybusinesslodging_41_PropertyOut",
        "LivingAreaIn": "_mybusinesslodging_42_LivingAreaIn",
        "LivingAreaOut": "_mybusinesslodging_43_LivingAreaOut",
        "AccessibilityIn": "_mybusinesslodging_44_AccessibilityIn",
        "AccessibilityOut": "_mybusinesslodging_45_AccessibilityOut",
        "ActivitiesIn": "_mybusinesslodging_46_ActivitiesIn",
        "ActivitiesOut": "_mybusinesslodging_47_ActivitiesOut",
        "PoliciesIn": "_mybusinesslodging_48_PoliciesIn",
        "PoliciesOut": "_mybusinesslodging_49_PoliciesOut",
        "PhysicalDistancingIn": "_mybusinesslodging_50_PhysicalDistancingIn",
        "PhysicalDistancingOut": "_mybusinesslodging_51_PhysicalDistancingOut",
        "LivingAreaSleepingIn": "_mybusinesslodging_52_LivingAreaSleepingIn",
        "LivingAreaSleepingOut": "_mybusinesslodging_53_LivingAreaSleepingOut",
        "ViewsFromUnitIn": "_mybusinesslodging_54_ViewsFromUnitIn",
        "ViewsFromUnitOut": "_mybusinesslodging_55_ViewsFromUnitOut",
        "LodgingIn": "_mybusinesslodging_56_LodgingIn",
        "LodgingOut": "_mybusinesslodging_57_LodgingOut",
        "PetsIn": "_mybusinesslodging_58_PetsIn",
        "PetsOut": "_mybusinesslodging_59_PetsOut",
        "BusinessIn": "_mybusinesslodging_60_BusinessIn",
        "BusinessOut": "_mybusinesslodging_61_BusinessOut",
        "WellnessIn": "_mybusinesslodging_62_WellnessIn",
        "WellnessOut": "_mybusinesslodging_63_WellnessOut",
        "GuestUnitFeaturesIn": "_mybusinesslodging_64_GuestUnitFeaturesIn",
        "GuestUnitFeaturesOut": "_mybusinesslodging_65_GuestUnitFeaturesOut",
        "HealthAndSafetyIn": "_mybusinesslodging_66_HealthAndSafetyIn",
        "HealthAndSafetyOut": "_mybusinesslodging_67_HealthAndSafetyOut",
        "FamiliesIn": "_mybusinesslodging_68_FamiliesIn",
        "FamiliesOut": "_mybusinesslodging_69_FamiliesOut",
        "SustainableSourcingIn": "_mybusinesslodging_70_SustainableSourcingIn",
        "SustainableSourcingOut": "_mybusinesslodging_71_SustainableSourcingOut",
        "LivingAreaAccessibilityIn": "_mybusinesslodging_72_LivingAreaAccessibilityIn",
        "LivingAreaAccessibilityOut": "_mybusinesslodging_73_LivingAreaAccessibilityOut",
        "FoodAndDrinkIn": "_mybusinesslodging_74_FoodAndDrinkIn",
        "FoodAndDrinkOut": "_mybusinesslodging_75_FoodAndDrinkOut",
        "EnergyEfficiencyIn": "_mybusinesslodging_76_EnergyEfficiencyIn",
        "EnergyEfficiencyOut": "_mybusinesslodging_77_EnergyEfficiencyOut",
        "PoolsIn": "_mybusinesslodging_78_PoolsIn",
        "PoolsOut": "_mybusinesslodging_79_PoolsOut",
        "LivingAreaLayoutIn": "_mybusinesslodging_80_LivingAreaLayoutIn",
        "LivingAreaLayoutOut": "_mybusinesslodging_81_LivingAreaLayoutOut",
        "ParkingIn": "_mybusinesslodging_82_ParkingIn",
        "ParkingOut": "_mybusinesslodging_83_ParkingOut",
        "HousekeepingIn": "_mybusinesslodging_84_HousekeepingIn",
        "HousekeepingOut": "_mybusinesslodging_85_HousekeepingOut",
        "SustainabilityCertificationsIn": "_mybusinesslodging_86_SustainabilityCertificationsIn",
        "SustainabilityCertificationsOut": "_mybusinesslodging_87_SustainabilityCertificationsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PaymentOptionsIn"] = t.struct(
        {
            "debitCardException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "debitCard": t.boolean().optional(),
            "chequeException": t.string().optional(),
            "cash": t.boolean().optional(),
            "creditCard": t.boolean().optional(),
            "cheque": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "cashException": t.string().optional(),
            "creditCardException": t.string().optional(),
        }
    ).named(renames["PaymentOptionsIn"])
    types["PaymentOptionsOut"] = t.struct(
        {
            "debitCardException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "debitCard": t.boolean().optional(),
            "chequeException": t.string().optional(),
            "cash": t.boolean().optional(),
            "creditCard": t.boolean().optional(),
            "cheque": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "cashException": t.string().optional(),
            "creditCardException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOptionsOut"])
    types["TransportationIn"] = t.struct(
        {
            "privateCarService": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "transfer": t.boolean().optional(),
            "transferException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
        }
    ).named(renames["TransportationIn"])
    types["TransportationOut"] = t.struct(
        {
            "privateCarService": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "transfer": t.boolean().optional(),
            "transferException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportationOut"])
    types["GetGoogleUpdatedLodgingResponseIn"] = t.struct(
        {"lodging": t.proxy(renames["LodgingIn"]), "diffMask": t.string()}
    ).named(renames["GetGoogleUpdatedLodgingResponseIn"])
    types["GetGoogleUpdatedLodgingResponseOut"] = t.struct(
        {
            "lodging": t.proxy(renames["LodgingOut"]),
            "diffMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetGoogleUpdatedLodgingResponseOut"])
    types["LivingAreaFeaturesIn"] = t.struct(
        {
            "tvCasting": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "heating": t.boolean().optional(),
            "fireplace": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "dryerException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "ironingEquipment": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "shower": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "toilet": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "showerException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "tvException": t.string().optional(),
            "washerException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "heatingException": t.string().optional(),
            "washer": t.boolean().optional(),
            "bidet": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "bathtubException": t.string().optional(),
            "bidetException": t.string().optional(),
            "toiletException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "hairdryer": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "dryer": t.boolean().optional(),
        }
    ).named(renames["LivingAreaFeaturesIn"])
    types["LivingAreaFeaturesOut"] = t.struct(
        {
            "tvCasting": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "heating": t.boolean().optional(),
            "fireplace": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "dryerException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "ironingEquipment": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "shower": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "toilet": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "showerException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "tvException": t.string().optional(),
            "washerException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "heatingException": t.string().optional(),
            "washer": t.boolean().optional(),
            "bidet": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "bathtubException": t.string().optional(),
            "bidetException": t.string().optional(),
            "toiletException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "hairdryer": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "dryer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaFeaturesOut"])
    types["GuestUnitTypeIn"] = t.struct(
        {
            "codes": t.array(t.string()),
            "label": t.string(),
            "features": t.proxy(renames["GuestUnitFeaturesIn"]).optional(),
        }
    ).named(renames["GuestUnitTypeIn"])
    types["GuestUnitTypeOut"] = t.struct(
        {
            "codes": t.array(t.string()),
            "label": t.string(),
            "features": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitTypeOut"])
    types["ConnectivityIn"] = t.struct(
        {
            "wifiAvailable": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "freeWifi": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
        }
    ).named(renames["ConnectivityIn"])
    types["ConnectivityOut"] = t.struct(
        {
            "wifiAvailable": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "freeWifi": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityOut"])
    types["LivingAreaEatingIn"] = t.struct(
        {
            "stove": t.boolean().optional(),
            "ovenException": t.string().optional(),
            "oven": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
            "outdoorGrillException": t.string().optional(),
            "kettle": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "refrigerator": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "toaster": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "snackbar": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "cookwareException": t.string().optional(),
            "outdoorGrill": t.boolean().optional(),
            "sink": t.boolean().optional(),
            "coffeeMaker": t.boolean().optional(),
            "kettleException": t.string().optional(),
            "stoveException": t.string().optional(),
            "cookware": t.boolean().optional(),
            "microwave": t.boolean().optional(),
            "microwaveException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "minibar": t.boolean().optional(),
            "sinkException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
        }
    ).named(renames["LivingAreaEatingIn"])
    types["LivingAreaEatingOut"] = t.struct(
        {
            "stove": t.boolean().optional(),
            "ovenException": t.string().optional(),
            "oven": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
            "outdoorGrillException": t.string().optional(),
            "kettle": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "refrigerator": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "toaster": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "snackbar": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "cookwareException": t.string().optional(),
            "outdoorGrill": t.boolean().optional(),
            "sink": t.boolean().optional(),
            "coffeeMaker": t.boolean().optional(),
            "kettleException": t.string().optional(),
            "stoveException": t.string().optional(),
            "cookware": t.boolean().optional(),
            "microwave": t.boolean().optional(),
            "microwaveException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "minibar": t.boolean().optional(),
            "sinkException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaEatingOut"])
    types["LodgingMetadataIn"] = t.struct({"updateTime": t.string()}).named(
        renames["LodgingMetadataIn"]
    )
    types["LodgingMetadataOut"] = t.struct(
        {
            "updateTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingMetadataOut"])
    types["IncreasedFoodSafetyIn"] = t.struct(
        {
            "disposableFlatware": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "disposableFlatwareException": t.string().optional(),
        }
    ).named(renames["IncreasedFoodSafetyIn"])
    types["IncreasedFoodSafetyOut"] = t.struct(
        {
            "disposableFlatware": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "disposableFlatwareException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncreasedFoodSafetyOut"])
    types["EcoCertificationIn"] = t.struct(
        {
            "ecoCertificate": t.string(),
            "awarded": t.boolean().optional(),
            "awardedException": t.string().optional(),
        }
    ).named(renames["EcoCertificationIn"])
    types["EcoCertificationOut"] = t.struct(
        {
            "ecoCertificate": t.string(),
            "awarded": t.boolean().optional(),
            "awardedException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcoCertificationOut"])
    types["MinimizedContactIn"] = t.struct(
        {
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
        }
    ).named(renames["MinimizedContactIn"])
    types["MinimizedContactOut"] = t.struct(
        {
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimizedContactOut"])
    types["EnhancedCleaningIn"] = t.struct(
        {
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
        }
    ).named(renames["EnhancedCleaningIn"])
    types["EnhancedCleaningOut"] = t.struct(
        {
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnhancedCleaningOut"])
    types["SustainabilityIn"] = t.struct(
        {
            "waterConservation": t.proxy(renames["WaterConservationIn"]).optional(),
            "sustainableSourcing": t.proxy(renames["SustainableSourcingIn"]).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionIn"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsIn"]
            ).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyIn"]).optional(),
        }
    ).named(renames["SustainabilityIn"])
    types["SustainabilityOut"] = t.struct(
        {
            "waterConservation": t.proxy(renames["WaterConservationOut"]).optional(),
            "sustainableSourcing": t.proxy(
                renames["SustainableSourcingOut"]
            ).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionOut"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsOut"]
            ).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["PersonalProtectionIn"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "faceMaskRequired": t.boolean().optional(),
        }
    ).named(renames["PersonalProtectionIn"])
    types["PersonalProtectionOut"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalProtectionOut"])
    types["WasteReductionIn"] = t.struct(
        {
            "safelyDisposesBatteries": t.boolean().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
        }
    ).named(renames["WasteReductionIn"])
    types["WasteReductionOut"] = t.struct(
        {
            "safelyDisposesBatteries": t.boolean().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WasteReductionOut"])
    types["WaterConservationIn"] = t.struct(
        {
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
        }
    ).named(renames["WaterConservationIn"])
    types["WaterConservationOut"] = t.struct(
        {
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterConservationOut"])
    types["LanguageSpokenIn"] = t.struct(
        {
            "spokenException": t.string().optional(),
            "spoken": t.boolean().optional(),
            "languageCode": t.string(),
        }
    ).named(renames["LanguageSpokenIn"])
    types["LanguageSpokenOut"] = t.struct(
        {
            "spokenException": t.string().optional(),
            "spoken": t.boolean().optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSpokenOut"])
    types["ServicesIn"] = t.struct(
        {
            "currencyExchange": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "frontDeskException": t.string().optional(),
            "concierge": t.boolean().optional(),
            "elevator": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "socialHourException": t.string().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "elevatorException": t.string().optional(),
            "baggageStorage": t.boolean().optional(),
            "wakeUpCallsException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "frontDesk": t.boolean().optional(),
            "giftShop": t.boolean().optional(),
            "languagesSpoken": t.array(t.proxy(renames["LanguageSpokenIn"])).optional(),
            "baggageStorageException": t.string().optional(),
            "convenienceStoreException": t.string().optional(),
        }
    ).named(renames["ServicesIn"])
    types["ServicesOut"] = t.struct(
        {
            "currencyExchange": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "frontDeskException": t.string().optional(),
            "concierge": t.boolean().optional(),
            "elevator": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "socialHourException": t.string().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "elevatorException": t.string().optional(),
            "baggageStorage": t.boolean().optional(),
            "wakeUpCallsException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "frontDesk": t.boolean().optional(),
            "giftShop": t.boolean().optional(),
            "languagesSpoken": t.array(
                t.proxy(renames["LanguageSpokenOut"])
            ).optional(),
            "baggageStorageException": t.string().optional(),
            "convenienceStoreException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicesOut"])
    types["PropertyIn"] = t.struct(
        {
            "roomsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "roomsCountException": t.string().optional(),
            "floorsCount": t.integer().optional(),
            "builtYear": t.integer().optional(),
            "floorsCountException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "lastRenovatedYearException": t.string().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "roomsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "roomsCountException": t.string().optional(),
            "floorsCount": t.integer().optional(),
            "builtYear": t.integer().optional(),
            "floorsCountException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "lastRenovatedYearException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["LivingAreaIn"] = t.struct(
        {
            "layout": t.proxy(renames["LivingAreaLayoutIn"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingIn"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesIn"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingIn"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityIn"]).optional(),
        }
    ).named(renames["LivingAreaIn"])
    types["LivingAreaOut"] = t.struct(
        {
            "layout": t.proxy(renames["LivingAreaLayoutOut"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingOut"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesOut"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingOut"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaOut"])
    types["AccessibilityIn"] = t.struct(
        {
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
        }
    ).named(renames["AccessibilityIn"])
    types["AccessibilityOut"] = t.struct(
        {
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessibilityOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "freeBicycleRentalException": t.string().optional(),
            "nightclub": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "casinoException": t.string().optional(),
            "waterSkiing": t.boolean().optional(),
            "horsebackRiding": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "golfException": t.string().optional(),
            "tennis": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "beachFront": t.boolean().optional(),
            "bicycleRental": t.boolean().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "snorkeling": t.boolean().optional(),
            "horsebackRidingException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "beachAccessException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "snorkelingException": t.string().optional(),
            "privateBeachException": t.string().optional(),
            "scubaException": t.string().optional(),
            "scuba": t.boolean().optional(),
            "waterSkiingException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "gameRoom": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "boutiqueStores": t.boolean().optional(),
            "privateBeach": t.boolean().optional(),
            "bicycleRentalException": t.string().optional(),
            "golf": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "freeBicycleRentalException": t.string().optional(),
            "nightclub": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "casinoException": t.string().optional(),
            "waterSkiing": t.boolean().optional(),
            "horsebackRiding": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "golfException": t.string().optional(),
            "tennis": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "beachFront": t.boolean().optional(),
            "bicycleRental": t.boolean().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "snorkeling": t.boolean().optional(),
            "horsebackRidingException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "beachAccessException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "snorkelingException": t.string().optional(),
            "privateBeachException": t.string().optional(),
            "scubaException": t.string().optional(),
            "scuba": t.boolean().optional(),
            "waterSkiingException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "gameRoom": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "boutiqueStores": t.boolean().optional(),
            "privateBeach": t.boolean().optional(),
            "bicycleRentalException": t.string().optional(),
            "golf": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["PoliciesIn"] = t.struct(
        {
            "allInclusiveOnly": t.boolean().optional(),
            "checkoutTimeException": t.string().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsIn"]).optional(),
            "checkinTimeException": t.string().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "kidsStayFree": t.boolean().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "maxChildAge": t.integer().optional(),
            "maxChildAgeException": t.string().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
        }
    ).named(renames["PoliciesIn"])
    types["PoliciesOut"] = t.struct(
        {
            "allInclusiveOnly": t.boolean().optional(),
            "checkoutTimeException": t.string().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsOut"]).optional(),
            "checkinTimeException": t.string().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "kidsStayFree": t.boolean().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "maxChildAge": t.integer().optional(),
            "maxChildAgeException": t.string().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesOut"])
    types["PhysicalDistancingIn"] = t.struct(
        {
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "safetyDividers": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "safetyDividersException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
        }
    ).named(renames["PhysicalDistancingIn"])
    types["PhysicalDistancingOut"] = t.struct(
        {
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "safetyDividers": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "safetyDividersException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalDistancingOut"])
    types["LivingAreaSleepingIn"] = t.struct(
        {
            "rollAwayBedsCount": t.integer().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "otherBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "featherPillowsException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "queenBedsCountException": t.string().optional(),
            "kingBedsCount": t.integer().optional(),
            "bunkBedsCountException": t.string().optional(),
            "doubleBedsCount": t.integer().optional(),
            "bunkBedsCount": t.integer().optional(),
            "featherPillows": t.boolean().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "bedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "sofaBedsCount": t.integer().optional(),
            "doubleBedsCountException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "sofaBedsCountException": t.string().optional(),
            "syntheticPillows": t.boolean().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "bedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "syntheticPillowsException": t.string().optional(),
        }
    ).named(renames["LivingAreaSleepingIn"])
    types["LivingAreaSleepingOut"] = t.struct(
        {
            "rollAwayBedsCount": t.integer().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "otherBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "featherPillowsException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "queenBedsCountException": t.string().optional(),
            "kingBedsCount": t.integer().optional(),
            "bunkBedsCountException": t.string().optional(),
            "doubleBedsCount": t.integer().optional(),
            "bunkBedsCount": t.integer().optional(),
            "featherPillows": t.boolean().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "bedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "sofaBedsCount": t.integer().optional(),
            "doubleBedsCountException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "sofaBedsCountException": t.string().optional(),
            "syntheticPillows": t.boolean().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "bedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "syntheticPillowsException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaSleepingOut"])
    types["ViewsFromUnitIn"] = t.struct(
        {
            "oceanView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "oceanViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "landmarkView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
            "landmarkViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "gardenView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "cityViewException": t.string().optional(),
            "lakeViewException": t.string().optional(),
            "valleyView": t.boolean().optional(),
            "gardenViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
        }
    ).named(renames["ViewsFromUnitIn"])
    types["ViewsFromUnitOut"] = t.struct(
        {
            "oceanView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "oceanViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "landmarkView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
            "landmarkViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "gardenView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "cityViewException": t.string().optional(),
            "lakeViewException": t.string().optional(),
            "valleyView": t.boolean().optional(),
            "gardenViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewsFromUnitOut"])
    types["LodgingIn"] = t.struct(
        {
            "pets": t.proxy(renames["PetsIn"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataIn"]),
            "business": t.proxy(renames["BusinessIn"]).optional(),
            "transportation": t.proxy(renames["TransportationIn"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
            "name": t.string(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
            "parking": t.proxy(renames["ParkingIn"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
            "property": t.proxy(renames["PropertyIn"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
            "pools": t.proxy(renames["PoolsIn"]).optional(),
            "wellness": t.proxy(renames["WellnessIn"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
            "policies": t.proxy(renames["PoliciesIn"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
            "services": t.proxy(renames["ServicesIn"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
            "families": t.proxy(renames["FamiliesIn"]).optional(),
            "activities": t.proxy(renames["ActivitiesIn"]).optional(),
        }
    ).named(renames["LodgingIn"])
    types["LodgingOut"] = t.struct(
        {
            "pets": t.proxy(renames["PetsOut"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataOut"]),
            "business": t.proxy(renames["BusinessOut"]).optional(),
            "transportation": t.proxy(renames["TransportationOut"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingOut"]).optional(),
            "someUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "name": t.string(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkOut"]).optional(),
            "allUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "parking": t.proxy(renames["ParkingOut"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityOut"]).optional(),
            "property": t.proxy(renames["PropertyOut"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaOut"]).optional(),
            "pools": t.proxy(renames["PoolsOut"]).optional(),
            "wellness": t.proxy(renames["WellnessOut"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityOut"]).optional(),
            "policies": t.proxy(renames["PoliciesOut"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityOut"]).optional(),
            "services": t.proxy(renames["ServicesOut"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeOut"])).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyOut"]).optional(),
            "families": t.proxy(renames["FamiliesOut"]).optional(),
            "activities": t.proxy(renames["ActivitiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingOut"])
    types["PetsIn"] = t.struct(
        {
            "petsAllowedFreeException": t.string().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
        }
    ).named(renames["PetsIn"])
    types["PetsOut"] = t.struct(
        {
            "petsAllowedFreeException": t.string().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PetsOut"])
    types["BusinessIn"] = t.struct(
        {
            "businessCenter": t.boolean().optional(),
            "meetingRoomsException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "meetingRooms": t.boolean().optional(),
        }
    ).named(renames["BusinessIn"])
    types["BusinessOut"] = t.struct(
        {
            "businessCenter": t.boolean().optional(),
            "meetingRoomsException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "meetingRooms": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessOut"])
    types["WellnessIn"] = t.struct(
        {
            "doctorOnCallException": t.string().optional(),
            "spaException": t.string().optional(),
            "saunaException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "massageException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
            "treadmillException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "fitnessCenterException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "salon": t.boolean().optional(),
            "freeWeightsException": t.string().optional(),
            "freeFitnessCenter": t.boolean().optional(),
            "freeWeights": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "salonException": t.string().optional(),
            "sauna": t.boolean().optional(),
            "massage": t.boolean().optional(),
        }
    ).named(renames["WellnessIn"])
    types["WellnessOut"] = t.struct(
        {
            "doctorOnCallException": t.string().optional(),
            "spaException": t.string().optional(),
            "saunaException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "massageException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
            "treadmillException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "fitnessCenterException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "salon": t.boolean().optional(),
            "freeWeightsException": t.string().optional(),
            "freeFitnessCenter": t.boolean().optional(),
            "freeWeights": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "salonException": t.string().optional(),
            "sauna": t.boolean().optional(),
            "massage": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WellnessOut"])
    types["GuestUnitFeaturesIn"] = t.struct(
        {
            "totalLivingAreas": t.proxy(renames["LivingAreaIn"]).optional(),
            "views": t.proxy(renames["ViewsFromUnitIn"]).optional(),
            "tierException": t.string().optional(),
            "tier": t.string().optional(),
            "executiveFloor": t.boolean().optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "privateHome": t.boolean().optional(),
            "suiteException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "suite": t.boolean().optional(),
        }
    ).named(renames["GuestUnitFeaturesIn"])
    types["GuestUnitFeaturesOut"] = t.struct(
        {
            "totalLivingAreas": t.proxy(renames["LivingAreaOut"]).optional(),
            "views": t.proxy(renames["ViewsFromUnitOut"]).optional(),
            "tierException": t.string().optional(),
            "tier": t.string().optional(),
            "executiveFloor": t.boolean().optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "privateHome": t.boolean().optional(),
            "suiteException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "suite": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitFeaturesOut"])
    types["HealthAndSafetyIn"] = t.struct(
        {
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningIn"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionIn"]).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingIn"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactIn"]).optional(),
            "increasedFoodSafety": t.proxy(renames["IncreasedFoodSafetyIn"]).optional(),
        }
    ).named(renames["HealthAndSafetyIn"])
    types["HealthAndSafetyOut"] = t.struct(
        {
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningOut"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionOut"]).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingOut"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactOut"]).optional(),
            "increasedFoodSafety": t.proxy(
                renames["IncreasedFoodSafetyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthAndSafetyOut"])
    types["FamiliesIn"] = t.struct(
        {
            "kidsActivitiesException": t.string().optional(),
            "kidsFriendly": t.boolean().optional(),
            "babysitting": t.boolean().optional(),
            "kidsActivities": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "babysittingException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
        }
    ).named(renames["FamiliesIn"])
    types["FamiliesOut"] = t.struct(
        {
            "kidsActivitiesException": t.string().optional(),
            "kidsFriendly": t.boolean().optional(),
            "babysitting": t.boolean().optional(),
            "kidsActivities": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "babysittingException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamiliesOut"])
    types["SustainableSourcingIn"] = t.struct(
        {
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "veganMealsException": t.string().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "vegetarianMealsException": t.string().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
        }
    ).named(renames["SustainableSourcingIn"])
    types["SustainableSourcingOut"] = t.struct(
        {
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "veganMealsException": t.string().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "vegetarianMealsException": t.string().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainableSourcingOut"])
    types["LivingAreaAccessibilityIn"] = t.struct(
        {
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
        }
    ).named(renames["LivingAreaAccessibilityIn"])
    types["LivingAreaAccessibilityOut"] = t.struct(
        {
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaAccessibilityOut"])
    types["FoodAndDrinkIn"] = t.struct(
        {
            "restaurantException": t.string().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "buffetException": t.string().optional(),
            "restaurantsCountException": t.string().optional(),
            "roomServiceException": t.string().optional(),
            "breakfastAvailableException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "roomService": t.boolean().optional(),
            "vendingMachineException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurantsCount": t.integer().optional(),
            "barException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "breakfastBuffetException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "dinnerBuffetException": t.string().optional(),
            "bar": t.boolean().optional(),
            "restaurant": t.boolean().optional(),
            "freeBreakfast": t.boolean().optional(),
            "tableServiceException": t.string().optional(),
            "tableService": t.boolean().optional(),
        }
    ).named(renames["FoodAndDrinkIn"])
    types["FoodAndDrinkOut"] = t.struct(
        {
            "restaurantException": t.string().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "buffetException": t.string().optional(),
            "restaurantsCountException": t.string().optional(),
            "roomServiceException": t.string().optional(),
            "breakfastAvailableException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "roomService": t.boolean().optional(),
            "vendingMachineException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurantsCount": t.integer().optional(),
            "barException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "breakfastBuffetException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "dinnerBuffetException": t.string().optional(),
            "bar": t.boolean().optional(),
            "restaurant": t.boolean().optional(),
            "freeBreakfast": t.boolean().optional(),
            "tableServiceException": t.string().optional(),
            "tableService": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FoodAndDrinkOut"])
    types["EnergyEfficiencyIn"] = t.struct(
        {
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyConservationProgramException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
        }
    ).named(renames["EnergyEfficiencyIn"])
    types["EnergyEfficiencyOut"] = t.struct(
        {
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "greenBuildingDesignException": t.string().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyConservationProgramException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "greenBuildingDesign": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnergyEfficiencyOut"])
    types["PoolsIn"] = t.struct(
        {
            "outdoorPoolException": t.string().optional(),
            "wadingPoolException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "wadingPool": t.boolean().optional(),
            "waterslide": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
            "waterParkException": t.string().optional(),
            "pool": t.boolean().optional(),
            "poolException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "lifeguard": t.boolean().optional(),
            "outdoorPool": t.boolean().optional(),
            "adultPoolException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "waterslideException": t.string().optional(),
            "lazyRiverException": t.string().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "wavePoolException": t.string().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "lazyRiver": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "indoorPoolException": t.string().optional(),
            "lifeguardException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "wavePool": t.boolean().optional(),
        }
    ).named(renames["PoolsIn"])
    types["PoolsOut"] = t.struct(
        {
            "outdoorPoolException": t.string().optional(),
            "wadingPoolException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "wadingPool": t.boolean().optional(),
            "waterslide": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
            "waterParkException": t.string().optional(),
            "pool": t.boolean().optional(),
            "poolException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "lifeguard": t.boolean().optional(),
            "outdoorPool": t.boolean().optional(),
            "adultPoolException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "waterslideException": t.string().optional(),
            "lazyRiverException": t.string().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "wavePoolException": t.string().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "lazyRiver": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "indoorPoolException": t.string().optional(),
            "lifeguardException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "wavePool": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolsOut"])
    types["LivingAreaLayoutIn"] = t.struct(
        {
            "nonSmoking": t.boolean().optional(),
            "balconyException": t.string().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "livingAreaSqMetersException": t.string().optional(),
            "stairs": t.boolean().optional(),
            "patioException": t.string().optional(),
            "stairsException": t.string().optional(),
            "nonSmokingException": t.string().optional(),
            "balcony": t.boolean().optional(),
            "loftException": t.string().optional(),
            "loft": t.boolean().optional(),
            "patio": t.boolean().optional(),
        }
    ).named(renames["LivingAreaLayoutIn"])
    types["LivingAreaLayoutOut"] = t.struct(
        {
            "nonSmoking": t.boolean().optional(),
            "balconyException": t.string().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "livingAreaSqMetersException": t.string().optional(),
            "stairs": t.boolean().optional(),
            "patioException": t.string().optional(),
            "stairsException": t.string().optional(),
            "nonSmokingException": t.string().optional(),
            "balcony": t.boolean().optional(),
            "loftException": t.string().optional(),
            "loft": t.boolean().optional(),
            "patio": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaLayoutOut"])
    types["ParkingIn"] = t.struct(
        {
            "freeSelfParkingException": t.string().optional(),
            "freeParkingException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "freeValetParking": t.boolean().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "freeValetParkingException": t.string().optional(),
            "parkingAvailableException": t.string().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "valetParkingAvailable": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
        }
    ).named(renames["ParkingIn"])
    types["ParkingOut"] = t.struct(
        {
            "freeSelfParkingException": t.string().optional(),
            "freeParkingException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "freeValetParking": t.boolean().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "freeValetParkingException": t.string().optional(),
            "parkingAvailableException": t.string().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "valetParkingAvailable": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParkingOut"])
    types["HousekeepingIn"] = t.struct(
        {
            "housekeepingAvailable": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "dailyHousekeepingException": t.string().optional(),
            "housekeepingAvailableException": t.string().optional(),
        }
    ).named(renames["HousekeepingIn"])
    types["HousekeepingOut"] = t.struct(
        {
            "housekeepingAvailable": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "dailyHousekeepingException": t.string().optional(),
            "housekeepingAvailableException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HousekeepingOut"])
    types["SustainabilityCertificationsIn"] = t.struct(
        {
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationIn"])
            ).optional(),
            "leedCertification": t.string().optional(),
            "breeamCertificationException": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
        }
    ).named(renames["SustainabilityCertificationsIn"])
    types["SustainabilityCertificationsOut"] = t.struct(
        {
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationOut"])
            ).optional(),
            "leedCertification": t.string().optional(),
            "breeamCertificationException": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityCertificationsOut"])

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
        importer="mybusinesslodging",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
