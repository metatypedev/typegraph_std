from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinesslodging():
    mybusinesslodging = HTTPRuntime("https://mybusinesslodging.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinesslodging_1_ErrorResponse",
        "GuestUnitFeaturesIn": "_mybusinesslodging_2_GuestUnitFeaturesIn",
        "GuestUnitFeaturesOut": "_mybusinesslodging_3_GuestUnitFeaturesOut",
        "TimeOfDayIn": "_mybusinesslodging_4_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinesslodging_5_TimeOfDayOut",
        "EnergyEfficiencyIn": "_mybusinesslodging_6_EnergyEfficiencyIn",
        "EnergyEfficiencyOut": "_mybusinesslodging_7_EnergyEfficiencyOut",
        "SustainabilityIn": "_mybusinesslodging_8_SustainabilityIn",
        "SustainabilityOut": "_mybusinesslodging_9_SustainabilityOut",
        "BusinessIn": "_mybusinesslodging_10_BusinessIn",
        "BusinessOut": "_mybusinesslodging_11_BusinessOut",
        "LivingAreaAccessibilityIn": "_mybusinesslodging_12_LivingAreaAccessibilityIn",
        "LivingAreaAccessibilityOut": "_mybusinesslodging_13_LivingAreaAccessibilityOut",
        "FoodAndDrinkIn": "_mybusinesslodging_14_FoodAndDrinkIn",
        "FoodAndDrinkOut": "_mybusinesslodging_15_FoodAndDrinkOut",
        "ConnectivityIn": "_mybusinesslodging_16_ConnectivityIn",
        "ConnectivityOut": "_mybusinesslodging_17_ConnectivityOut",
        "EnhancedCleaningIn": "_mybusinesslodging_18_EnhancedCleaningIn",
        "EnhancedCleaningOut": "_mybusinesslodging_19_EnhancedCleaningOut",
        "IncreasedFoodSafetyIn": "_mybusinesslodging_20_IncreasedFoodSafetyIn",
        "IncreasedFoodSafetyOut": "_mybusinesslodging_21_IncreasedFoodSafetyOut",
        "PoolsIn": "_mybusinesslodging_22_PoolsIn",
        "PoolsOut": "_mybusinesslodging_23_PoolsOut",
        "ActivitiesIn": "_mybusinesslodging_24_ActivitiesIn",
        "ActivitiesOut": "_mybusinesslodging_25_ActivitiesOut",
        "LivingAreaSleepingIn": "_mybusinesslodging_26_LivingAreaSleepingIn",
        "LivingAreaSleepingOut": "_mybusinesslodging_27_LivingAreaSleepingOut",
        "TransportationIn": "_mybusinesslodging_28_TransportationIn",
        "TransportationOut": "_mybusinesslodging_29_TransportationOut",
        "GetGoogleUpdatedLodgingResponseIn": "_mybusinesslodging_30_GetGoogleUpdatedLodgingResponseIn",
        "GetGoogleUpdatedLodgingResponseOut": "_mybusinesslodging_31_GetGoogleUpdatedLodgingResponseOut",
        "WasteReductionIn": "_mybusinesslodging_32_WasteReductionIn",
        "WasteReductionOut": "_mybusinesslodging_33_WasteReductionOut",
        "HealthAndSafetyIn": "_mybusinesslodging_34_HealthAndSafetyIn",
        "HealthAndSafetyOut": "_mybusinesslodging_35_HealthAndSafetyOut",
        "HousekeepingIn": "_mybusinesslodging_36_HousekeepingIn",
        "HousekeepingOut": "_mybusinesslodging_37_HousekeepingOut",
        "MinimizedContactIn": "_mybusinesslodging_38_MinimizedContactIn",
        "MinimizedContactOut": "_mybusinesslodging_39_MinimizedContactOut",
        "LanguageSpokenIn": "_mybusinesslodging_40_LanguageSpokenIn",
        "LanguageSpokenOut": "_mybusinesslodging_41_LanguageSpokenOut",
        "PetsIn": "_mybusinesslodging_42_PetsIn",
        "PetsOut": "_mybusinesslodging_43_PetsOut",
        "PaymentOptionsIn": "_mybusinesslodging_44_PaymentOptionsIn",
        "PaymentOptionsOut": "_mybusinesslodging_45_PaymentOptionsOut",
        "WellnessIn": "_mybusinesslodging_46_WellnessIn",
        "WellnessOut": "_mybusinesslodging_47_WellnessOut",
        "SustainabilityCertificationsIn": "_mybusinesslodging_48_SustainabilityCertificationsIn",
        "SustainabilityCertificationsOut": "_mybusinesslodging_49_SustainabilityCertificationsOut",
        "ViewsFromUnitIn": "_mybusinesslodging_50_ViewsFromUnitIn",
        "ViewsFromUnitOut": "_mybusinesslodging_51_ViewsFromUnitOut",
        "PhysicalDistancingIn": "_mybusinesslodging_52_PhysicalDistancingIn",
        "PhysicalDistancingOut": "_mybusinesslodging_53_PhysicalDistancingOut",
        "PropertyIn": "_mybusinesslodging_54_PropertyIn",
        "PropertyOut": "_mybusinesslodging_55_PropertyOut",
        "ParkingIn": "_mybusinesslodging_56_ParkingIn",
        "ParkingOut": "_mybusinesslodging_57_ParkingOut",
        "ServicesIn": "_mybusinesslodging_58_ServicesIn",
        "ServicesOut": "_mybusinesslodging_59_ServicesOut",
        "LivingAreaIn": "_mybusinesslodging_60_LivingAreaIn",
        "LivingAreaOut": "_mybusinesslodging_61_LivingAreaOut",
        "PoliciesIn": "_mybusinesslodging_62_PoliciesIn",
        "PoliciesOut": "_mybusinesslodging_63_PoliciesOut",
        "LivingAreaLayoutIn": "_mybusinesslodging_64_LivingAreaLayoutIn",
        "LivingAreaLayoutOut": "_mybusinesslodging_65_LivingAreaLayoutOut",
        "AccessibilityIn": "_mybusinesslodging_66_AccessibilityIn",
        "AccessibilityOut": "_mybusinesslodging_67_AccessibilityOut",
        "SustainableSourcingIn": "_mybusinesslodging_68_SustainableSourcingIn",
        "SustainableSourcingOut": "_mybusinesslodging_69_SustainableSourcingOut",
        "WaterConservationIn": "_mybusinesslodging_70_WaterConservationIn",
        "WaterConservationOut": "_mybusinesslodging_71_WaterConservationOut",
        "LodgingMetadataIn": "_mybusinesslodging_72_LodgingMetadataIn",
        "LodgingMetadataOut": "_mybusinesslodging_73_LodgingMetadataOut",
        "PersonalProtectionIn": "_mybusinesslodging_74_PersonalProtectionIn",
        "PersonalProtectionOut": "_mybusinesslodging_75_PersonalProtectionOut",
        "FamiliesIn": "_mybusinesslodging_76_FamiliesIn",
        "FamiliesOut": "_mybusinesslodging_77_FamiliesOut",
        "LivingAreaFeaturesIn": "_mybusinesslodging_78_LivingAreaFeaturesIn",
        "LivingAreaFeaturesOut": "_mybusinesslodging_79_LivingAreaFeaturesOut",
        "LivingAreaEatingIn": "_mybusinesslodging_80_LivingAreaEatingIn",
        "LivingAreaEatingOut": "_mybusinesslodging_81_LivingAreaEatingOut",
        "EcoCertificationIn": "_mybusinesslodging_82_EcoCertificationIn",
        "EcoCertificationOut": "_mybusinesslodging_83_EcoCertificationOut",
        "GuestUnitTypeIn": "_mybusinesslodging_84_GuestUnitTypeIn",
        "GuestUnitTypeOut": "_mybusinesslodging_85_GuestUnitTypeOut",
        "LodgingIn": "_mybusinesslodging_86_LodgingIn",
        "LodgingOut": "_mybusinesslodging_87_LodgingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GuestUnitFeaturesIn"] = t.struct(
        {
            "suiteException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "suite": t.boolean().optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaIn"]).optional(),
            "executiveFloor": t.boolean().optional(),
            "views": t.proxy(renames["ViewsFromUnitIn"]).optional(),
            "maxOccupantsCountException": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "tier": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "privateHome": t.boolean().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "tierException": t.string().optional(),
        }
    ).named(renames["GuestUnitFeaturesIn"])
    types["GuestUnitFeaturesOut"] = t.struct(
        {
            "suiteException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "suite": t.boolean().optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "maxOccupantsCount": t.integer().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaOut"]).optional(),
            "executiveFloor": t.boolean().optional(),
            "views": t.proxy(renames["ViewsFromUnitOut"]).optional(),
            "maxOccupantsCountException": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "tier": t.string().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "privateHome": t.boolean().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "tierException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitFeaturesOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["EnergyEfficiencyIn"] = t.struct(
        {
            "energyConservationProgram": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyConservationProgramException": t.string().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
        }
    ).named(renames["EnergyEfficiencyIn"])
    types["EnergyEfficiencyOut"] = t.struct(
        {
            "energyConservationProgram": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "greenBuildingDesignException": t.string().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyConservationProgramException": t.string().optional(),
            "greenBuildingDesign": t.boolean().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnergyEfficiencyOut"])
    types["SustainabilityIn"] = t.struct(
        {
            "waterConservation": t.proxy(renames["WaterConservationIn"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsIn"]
            ).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionIn"]).optional(),
            "sustainableSourcing": t.proxy(renames["SustainableSourcingIn"]).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyIn"]).optional(),
        }
    ).named(renames["SustainabilityIn"])
    types["SustainabilityOut"] = t.struct(
        {
            "waterConservation": t.proxy(renames["WaterConservationOut"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsOut"]
            ).optional(),
            "wasteReduction": t.proxy(renames["WasteReductionOut"]).optional(),
            "sustainableSourcing": t.proxy(
                renames["SustainableSourcingOut"]
            ).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityOut"])
    types["BusinessIn"] = t.struct(
        {
            "meetingRooms": t.boolean().optional(),
            "businessCenter": t.boolean().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "meetingRoomsException": t.string().optional(),
        }
    ).named(renames["BusinessIn"])
    types["BusinessOut"] = t.struct(
        {
            "meetingRooms": t.boolean().optional(),
            "businessCenter": t.boolean().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "meetingRoomsException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessOut"])
    types["LivingAreaAccessibilityIn"] = t.struct(
        {
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
        }
    ).named(renames["LivingAreaAccessibilityIn"])
    types["LivingAreaAccessibilityOut"] = t.struct(
        {
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "mobilityAccessibleToiletException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaAccessibilityOut"])
    types["FoodAndDrinkIn"] = t.struct(
        {
            "freeBreakfast": t.boolean().optional(),
            "barException": t.string().optional(),
            "restaurantsCount": t.integer().optional(),
            "roomServiceException": t.string().optional(),
            "breakfastBuffetException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "buffetException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "tableService": t.boolean().optional(),
            "vendingMachineException": t.string().optional(),
            "restaurant": t.boolean().optional(),
            "breakfastAvailableException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "tableServiceException": t.string().optional(),
            "vendingMachine": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "roomService": t.boolean().optional(),
            "bar": t.boolean().optional(),
        }
    ).named(renames["FoodAndDrinkIn"])
    types["FoodAndDrinkOut"] = t.struct(
        {
            "freeBreakfast": t.boolean().optional(),
            "barException": t.string().optional(),
            "restaurantsCount": t.integer().optional(),
            "roomServiceException": t.string().optional(),
            "breakfastBuffetException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "buffetException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "tableService": t.boolean().optional(),
            "vendingMachineException": t.string().optional(),
            "restaurant": t.boolean().optional(),
            "breakfastAvailableException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "tableServiceException": t.string().optional(),
            "vendingMachine": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "roomService": t.boolean().optional(),
            "bar": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FoodAndDrinkOut"])
    types["ConnectivityIn"] = t.struct(
        {
            "freeWifi": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "wifiAvailableException": t.string().optional(),
            "wifiAvailable": t.boolean().optional(),
        }
    ).named(renames["ConnectivityIn"])
    types["ConnectivityOut"] = t.struct(
        {
            "freeWifi": t.boolean().optional(),
            "freeWifiException": t.string().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "wifiAvailableException": t.string().optional(),
            "wifiAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityOut"])
    types["EnhancedCleaningIn"] = t.struct(
        {
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
        }
    ).named(renames["EnhancedCleaningIn"])
    types["EnhancedCleaningOut"] = t.struct(
        {
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnhancedCleaningOut"])
    types["IncreasedFoodSafetyIn"] = t.struct(
        {
            "disposableFlatware": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "disposableFlatwareException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
        }
    ).named(renames["IncreasedFoodSafetyIn"])
    types["IncreasedFoodSafetyOut"] = t.struct(
        {
            "disposableFlatware": t.boolean().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "disposableFlatwareException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncreasedFoodSafetyOut"])
    types["PoolsIn"] = t.struct(
        {
            "outdoorPoolException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "indoorPool": t.boolean().optional(),
            "lazyRiverException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "wavePool": t.boolean().optional(),
            "pool": t.boolean().optional(),
            "poolsCountException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "adultPoolException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "lifeguardException": t.string().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "outdoorPool": t.boolean().optional(),
            "wadingPoolException": t.string().optional(),
            "waterParkException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "wadingPool": t.boolean().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "waterslideException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "lifeguard": t.boolean().optional(),
            "poolException": t.string().optional(),
            "indoorPoolException": t.string().optional(),
            "waterPark": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
        }
    ).named(renames["PoolsIn"])
    types["PoolsOut"] = t.struct(
        {
            "outdoorPoolException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "indoorPool": t.boolean().optional(),
            "lazyRiverException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "wavePool": t.boolean().optional(),
            "pool": t.boolean().optional(),
            "poolsCountException": t.string().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "adultPoolException": t.string().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "lifeguardException": t.string().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "outdoorPool": t.boolean().optional(),
            "wadingPoolException": t.string().optional(),
            "waterParkException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "wadingPool": t.boolean().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "waterslideException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "lifeguard": t.boolean().optional(),
            "poolException": t.string().optional(),
            "indoorPoolException": t.string().optional(),
            "waterPark": t.boolean().optional(),
            "hotTub": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolsOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "beachFront": t.boolean().optional(),
            "privateBeach": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "bicycleRental": t.boolean().optional(),
            "nightclub": t.boolean().optional(),
            "tennis": t.boolean().optional(),
            "snorkeling": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "golfException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "bicycleRentalException": t.string().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "golf": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "horsebackRiding": t.boolean().optional(),
            "watercraftRentalException": t.string().optional(),
            "horsebackRidingException": t.string().optional(),
            "scubaException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "gameRoom": t.boolean().optional(),
            "boutiqueStores": t.boolean().optional(),
            "casinoException": t.string().optional(),
            "boutiqueStoresException": t.string().optional(),
            "beachAccessException": t.string().optional(),
            "waterSkiing": t.boolean().optional(),
            "scuba": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "beachFront": t.boolean().optional(),
            "privateBeach": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "bicycleRental": t.boolean().optional(),
            "nightclub": t.boolean().optional(),
            "tennis": t.boolean().optional(),
            "snorkeling": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "golfException": t.string().optional(),
            "nightclubException": t.string().optional(),
            "beachAccess": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "bicycleRentalException": t.string().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "golf": t.boolean().optional(),
            "watercraftRental": t.boolean().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "tennisException": t.string().optional(),
            "horsebackRiding": t.boolean().optional(),
            "watercraftRentalException": t.string().optional(),
            "horsebackRidingException": t.string().optional(),
            "scubaException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "gameRoom": t.boolean().optional(),
            "boutiqueStores": t.boolean().optional(),
            "casinoException": t.string().optional(),
            "boutiqueStoresException": t.string().optional(),
            "beachAccessException": t.string().optional(),
            "waterSkiing": t.boolean().optional(),
            "scuba": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["LivingAreaSleepingIn"] = t.struct(
        {
            "kingBedsCount": t.integer().optional(),
            "bedsCount": t.integer().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCountException": t.string().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "syntheticPillows": t.boolean().optional(),
            "bedsCountException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "kingBedsCountException": t.string().optional(),
            "bunkBedsCountException": t.string().optional(),
            "otherBedsCountException": t.string().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "queenBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "doubleBedsCount": t.integer().optional(),
            "featherPillows": t.boolean().optional(),
            "bunkBedsCount": t.integer().optional(),
            "sofaBedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "sofaBedsCount": t.integer().optional(),
        }
    ).named(renames["LivingAreaSleepingIn"])
    types["LivingAreaSleepingOut"] = t.struct(
        {
            "kingBedsCount": t.integer().optional(),
            "bedsCount": t.integer().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCountException": t.string().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "syntheticPillows": t.boolean().optional(),
            "bedsCountException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "kingBedsCountException": t.string().optional(),
            "bunkBedsCountException": t.string().optional(),
            "otherBedsCountException": t.string().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "queenBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "doubleBedsCount": t.integer().optional(),
            "featherPillows": t.boolean().optional(),
            "bunkBedsCount": t.integer().optional(),
            "sofaBedsCountException": t.string().optional(),
            "cribsCount": t.integer().optional(),
            "sofaBedsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaSleepingOut"])
    types["TransportationIn"] = t.struct(
        {
            "carRentalOnPropertyException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "transferException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "airportShuttleException": t.string().optional(),
            "transfer": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
        }
    ).named(renames["TransportationIn"])
    types["TransportationOut"] = t.struct(
        {
            "carRentalOnPropertyException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "transferException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "freeAirportShuttleException": t.string().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "airportShuttleException": t.string().optional(),
            "transfer": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportationOut"])
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
    types["WasteReductionIn"] = t.struct(
        {
            "refillableToiletryContainers": t.boolean().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "soapDonationProgramException": t.string().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "recyclingProgram": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
        }
    ).named(renames["WasteReductionIn"])
    types["WasteReductionOut"] = t.struct(
        {
            "refillableToiletryContainers": t.boolean().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "soapDonationProgramException": t.string().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "recyclingProgram": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WasteReductionOut"])
    types["HealthAndSafetyIn"] = t.struct(
        {
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningIn"]).optional(),
            "increasedFoodSafety": t.proxy(renames["IncreasedFoodSafetyIn"]).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingIn"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionIn"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactIn"]).optional(),
        }
    ).named(renames["HealthAndSafetyIn"])
    types["HealthAndSafetyOut"] = t.struct(
        {
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningOut"]).optional(),
            "increasedFoodSafety": t.proxy(
                renames["IncreasedFoodSafetyOut"]
            ).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingOut"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionOut"]).optional(),
            "minimizedContact": t.proxy(renames["MinimizedContactOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthAndSafetyOut"])
    types["HousekeepingIn"] = t.struct(
        {
            "dailyHousekeepingException": t.string().optional(),
            "turndownServiceException": t.string().optional(),
            "housekeepingAvailableException": t.string().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "turndownService": t.boolean().optional(),
        }
    ).named(renames["HousekeepingIn"])
    types["HousekeepingOut"] = t.struct(
        {
            "dailyHousekeepingException": t.string().optional(),
            "turndownServiceException": t.string().optional(),
            "housekeepingAvailableException": t.string().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "turndownService": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HousekeepingOut"])
    types["MinimizedContactIn"] = t.struct(
        {
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
        }
    ).named(renames["MinimizedContactIn"])
    types["MinimizedContactOut"] = t.struct(
        {
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "contactlessCheckinCheckoutException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimizedContactOut"])
    types["LanguageSpokenIn"] = t.struct(
        {
            "languageCode": t.string(),
            "spoken": t.boolean().optional(),
            "spokenException": t.string().optional(),
        }
    ).named(renames["LanguageSpokenIn"])
    types["LanguageSpokenOut"] = t.struct(
        {
            "languageCode": t.string(),
            "spoken": t.boolean().optional(),
            "spokenException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSpokenOut"])
    types["PetsIn"] = t.struct(
        {
            "petsAllowedFreeException": t.string().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowedException": t.string().optional(),
        }
    ).named(renames["PetsIn"])
    types["PetsOut"] = t.struct(
        {
            "petsAllowedFreeException": t.string().optional(),
            "petsAllowedException": t.string().optional(),
            "dogsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "petsAllowed": t.boolean().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowedException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PetsOut"])
    types["PaymentOptionsIn"] = t.struct(
        {
            "mobileNfcException": t.string().optional(),
            "cash": t.boolean().optional(),
            "debitCardException": t.string().optional(),
            "chequeException": t.string().optional(),
            "cheque": t.boolean().optional(),
            "creditCard": t.boolean().optional(),
            "creditCardException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "cashException": t.string().optional(),
            "debitCard": t.boolean().optional(),
        }
    ).named(renames["PaymentOptionsIn"])
    types["PaymentOptionsOut"] = t.struct(
        {
            "mobileNfcException": t.string().optional(),
            "cash": t.boolean().optional(),
            "debitCardException": t.string().optional(),
            "chequeException": t.string().optional(),
            "cheque": t.boolean().optional(),
            "creditCard": t.boolean().optional(),
            "creditCardException": t.string().optional(),
            "mobileNfc": t.boolean().optional(),
            "cashException": t.string().optional(),
            "debitCard": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOptionsOut"])
    types["WellnessIn"] = t.struct(
        {
            "freeFitnessCenter": t.boolean().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeWeights": t.boolean().optional(),
            "ellipticalMachineException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "massage": t.boolean().optional(),
            "salonException": t.string().optional(),
            "spaException": t.string().optional(),
            "treadmillException": t.string().optional(),
            "salon": t.boolean().optional(),
            "saunaException": t.string().optional(),
            "spa": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "fitnessCenterException": t.string().optional(),
            "doctorOnCallException": t.string().optional(),
            "freeWeightsException": t.string().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "massageException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
        }
    ).named(renames["WellnessIn"])
    types["WellnessOut"] = t.struct(
        {
            "freeFitnessCenter": t.boolean().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeWeights": t.boolean().optional(),
            "ellipticalMachineException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "treadmill": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "massage": t.boolean().optional(),
            "salonException": t.string().optional(),
            "spaException": t.string().optional(),
            "treadmillException": t.string().optional(),
            "salon": t.boolean().optional(),
            "saunaException": t.string().optional(),
            "spa": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "fitnessCenterException": t.string().optional(),
            "doctorOnCallException": t.string().optional(),
            "freeWeightsException": t.string().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "massageException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WellnessOut"])
    types["SustainabilityCertificationsIn"] = t.struct(
        {
            "breeamCertification": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationIn"])
            ).optional(),
            "leedCertification": t.string().optional(),
            "breeamCertificationException": t.string().optional(),
        }
    ).named(renames["SustainabilityCertificationsIn"])
    types["SustainabilityCertificationsOut"] = t.struct(
        {
            "breeamCertification": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationOut"])
            ).optional(),
            "leedCertification": t.string().optional(),
            "breeamCertificationException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityCertificationsOut"])
    types["ViewsFromUnitIn"] = t.struct(
        {
            "lakeViewException": t.string().optional(),
            "oceanViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "gardenViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "cityViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "beachView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "gardenView": t.boolean().optional(),
            "landmarkView": t.boolean().optional(),
            "valleyView": t.boolean().optional(),
            "oceanView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
        }
    ).named(renames["ViewsFromUnitIn"])
    types["ViewsFromUnitOut"] = t.struct(
        {
            "lakeViewException": t.string().optional(),
            "oceanViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "poolViewException": t.string().optional(),
            "gardenViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "cityViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "beachView": t.boolean().optional(),
            "cityView": t.boolean().optional(),
            "gardenView": t.boolean().optional(),
            "landmarkView": t.boolean().optional(),
            "valleyView": t.boolean().optional(),
            "oceanView": t.boolean().optional(),
            "lakeView": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewsFromUnitOut"])
    types["PhysicalDistancingIn"] = t.struct(
        {
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "safetyDividersException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
        }
    ).named(renames["PhysicalDistancingIn"])
    types["PhysicalDistancingOut"] = t.struct(
        {
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "safetyDividersException": t.string().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalDistancingOut"])
    types["PropertyIn"] = t.struct(
        {
            "floorsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "roomsCount": t.integer().optional(),
            "roomsCountException": t.string().optional(),
            "lastRenovatedYearException": t.string().optional(),
            "floorsCountException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "builtYear": t.integer().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "floorsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "roomsCount": t.integer().optional(),
            "roomsCountException": t.string().optional(),
            "lastRenovatedYearException": t.string().optional(),
            "floorsCountException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "builtYear": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["ParkingIn"] = t.struct(
        {
            "valetParkingAvailable": t.boolean().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "parkingAvailableException": t.string().optional(),
            "freeValetParkingException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "electricCarChargingStationsException": t.string().optional(),
        }
    ).named(renames["ParkingIn"])
    types["ParkingOut"] = t.struct(
        {
            "valetParkingAvailable": t.boolean().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "freeParking": t.boolean().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "parkingAvailableException": t.string().optional(),
            "freeValetParkingException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParkingOut"])
    types["ServicesIn"] = t.struct(
        {
            "wakeUpCallsException": t.string().optional(),
            "giftShop": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "socialHour": t.boolean().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "socialHourException": t.string().optional(),
            "languagesSpoken": t.array(t.proxy(renames["LanguageSpokenIn"])).optional(),
            "giftShopException": t.string().optional(),
            "elevatorException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "concierge": t.boolean().optional(),
            "currencyExchange": t.boolean().optional(),
            "frontDeskException": t.string().optional(),
            "frontDesk": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "conciergeException": t.string().optional(),
            "elevator": t.boolean().optional(),
            "convenienceStoreException": t.string().optional(),
            "currencyExchangeException": t.string().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
        }
    ).named(renames["ServicesIn"])
    types["ServicesOut"] = t.struct(
        {
            "wakeUpCallsException": t.string().optional(),
            "giftShop": t.boolean().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "socialHour": t.boolean().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "socialHourException": t.string().optional(),
            "languagesSpoken": t.array(
                t.proxy(renames["LanguageSpokenOut"])
            ).optional(),
            "giftShopException": t.string().optional(),
            "elevatorException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "concierge": t.boolean().optional(),
            "currencyExchange": t.boolean().optional(),
            "frontDeskException": t.string().optional(),
            "frontDesk": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "conciergeException": t.string().optional(),
            "elevator": t.boolean().optional(),
            "convenienceStoreException": t.string().optional(),
            "currencyExchangeException": t.string().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicesOut"])
    types["LivingAreaIn"] = t.struct(
        {
            "accessibility": t.proxy(renames["LivingAreaAccessibilityIn"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesIn"]).optional(),
            "layout": t.proxy(renames["LivingAreaLayoutIn"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingIn"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingIn"]).optional(),
        }
    ).named(renames["LivingAreaIn"])
    types["LivingAreaOut"] = t.struct(
        {
            "accessibility": t.proxy(renames["LivingAreaAccessibilityOut"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesOut"]).optional(),
            "layout": t.proxy(renames["LivingAreaLayoutOut"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingOut"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaOut"])
    types["PoliciesIn"] = t.struct(
        {
            "maxChildAgeException": t.string().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "kidsStayFree": t.boolean().optional(),
            "checkoutTimeException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "checkinTimeException": t.string().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "maxChildAge": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsIn"]).optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
        }
    ).named(renames["PoliciesIn"])
    types["PoliciesOut"] = t.struct(
        {
            "maxChildAgeException": t.string().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "kidsStayFree": t.boolean().optional(),
            "checkoutTimeException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "checkinTimeException": t.string().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "maxChildAge": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsOut"]).optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesOut"])
    types["LivingAreaLayoutIn"] = t.struct(
        {
            "patioException": t.string().optional(),
            "stairsException": t.string().optional(),
            "patio": t.boolean().optional(),
            "loft": t.boolean().optional(),
            "loftException": t.string().optional(),
            "balcony": t.boolean().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "balconyException": t.string().optional(),
            "nonSmoking": t.boolean().optional(),
            "livingAreaSqMetersException": t.string().optional(),
            "stairs": t.boolean().optional(),
            "nonSmokingException": t.string().optional(),
        }
    ).named(renames["LivingAreaLayoutIn"])
    types["LivingAreaLayoutOut"] = t.struct(
        {
            "patioException": t.string().optional(),
            "stairsException": t.string().optional(),
            "patio": t.boolean().optional(),
            "loft": t.boolean().optional(),
            "loftException": t.string().optional(),
            "balcony": t.boolean().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "balconyException": t.string().optional(),
            "nonSmoking": t.boolean().optional(),
            "livingAreaSqMetersException": t.string().optional(),
            "stairs": t.boolean().optional(),
            "nonSmokingException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaLayoutOut"])
    types["AccessibilityIn"] = t.struct(
        {
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
        }
    ).named(renames["AccessibilityIn"])
    types["AccessibilityOut"] = t.struct(
        {
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessibilityOut"])
    types["SustainableSourcingIn"] = t.struct(
        {
            "vegetarianMealsException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "veganMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
        }
    ).named(renames["SustainableSourcingIn"])
    types["SustainableSourcingOut"] = t.struct(
        {
            "vegetarianMealsException": t.string().optional(),
            "veganMeals": t.boolean().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "veganMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "responsiblySourcesSeafoodException": t.string().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainableSourcingOut"])
    types["WaterConservationIn"] = t.struct(
        {
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "towelReuseProgramException": t.string().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
        }
    ).named(renames["WaterConservationIn"])
    types["WaterConservationOut"] = t.struct(
        {
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "towelReuseProgramException": t.string().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowersException": t.string().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterConservationOut"])
    types["LodgingMetadataIn"] = t.struct({"updateTime": t.string()}).named(
        renames["LodgingMetadataIn"]
    )
    types["LodgingMetadataOut"] = t.struct(
        {
            "updateTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingMetadataOut"])
    types["PersonalProtectionIn"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
        }
    ).named(renames["PersonalProtectionIn"])
    types["PersonalProtectionOut"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalProtectionOut"])
    types["FamiliesIn"] = t.struct(
        {
            "kidsFriendly": t.boolean().optional(),
            "babysittingException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsActivities": t.boolean().optional(),
            "kidsClub": t.boolean().optional(),
            "kidsActivitiesException": t.string().optional(),
            "babysitting": t.boolean().optional(),
        }
    ).named(renames["FamiliesIn"])
    types["FamiliesOut"] = t.struct(
        {
            "kidsFriendly": t.boolean().optional(),
            "babysittingException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsActivities": t.boolean().optional(),
            "kidsClub": t.boolean().optional(),
            "kidsActivitiesException": t.string().optional(),
            "babysitting": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamiliesOut"])
    types["LivingAreaFeaturesIn"] = t.struct(
        {
            "inunitSafe": t.boolean().optional(),
            "airConditioningException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "dryerException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "tvCasting": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "bathtubException": t.string().optional(),
            "bidetException": t.string().optional(),
            "tvException": t.string().optional(),
            "bathtub": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "washerException": t.string().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "toilet": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "dryer": t.boolean().optional(),
            "fireplace": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "heatingException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "heating": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "toiletException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "hairdryer": t.boolean().optional(),
            "fireplaceException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "shower": t.boolean().optional(),
            "washer": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "showerException": t.string().optional(),
        }
    ).named(renames["LivingAreaFeaturesIn"])
    types["LivingAreaFeaturesOut"] = t.struct(
        {
            "inunitSafe": t.boolean().optional(),
            "airConditioningException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "dryerException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "tvCasting": t.boolean().optional(),
            "privateBathroom": t.boolean().optional(),
            "bathtubException": t.string().optional(),
            "bidetException": t.string().optional(),
            "tvException": t.string().optional(),
            "bathtub": t.boolean().optional(),
            "privateBathroomException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "washerException": t.string().optional(),
            "payPerViewMoviesException": t.string().optional(),
            "toilet": t.boolean().optional(),
            "tvStreamingException": t.string().optional(),
            "dryer": t.boolean().optional(),
            "fireplace": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "heatingException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "heating": t.boolean().optional(),
            "tvCastingException": t.string().optional(),
            "toiletException": t.string().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "hairdryer": t.boolean().optional(),
            "fireplaceException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "shower": t.boolean().optional(),
            "washer": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "showerException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaFeaturesOut"])
    types["LivingAreaEatingIn"] = t.struct(
        {
            "coffeeMaker": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "kettle": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "cookwareException": t.string().optional(),
            "sinkException": t.string().optional(),
            "sink": t.boolean().optional(),
            "oven": t.boolean().optional(),
            "cookware": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "outdoorGrill": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "stoveException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "snackbar": t.boolean().optional(),
            "kettleException": t.string().optional(),
            "microwave": t.boolean().optional(),
            "snackbarException": t.string().optional(),
            "outdoorGrillException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "ovenException": t.string().optional(),
            "refrigerator": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "stove": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "toaster": t.boolean().optional(),
            "microwaveException": t.string().optional(),
            "minibar": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
        }
    ).named(renames["LivingAreaEatingIn"])
    types["LivingAreaEatingOut"] = t.struct(
        {
            "coffeeMaker": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "kettle": t.boolean().optional(),
            "kitchenAvailableException": t.string().optional(),
            "cookwareException": t.string().optional(),
            "sinkException": t.string().optional(),
            "sink": t.boolean().optional(),
            "oven": t.boolean().optional(),
            "cookware": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "outdoorGrill": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "stoveException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "snackbar": t.boolean().optional(),
            "kettleException": t.string().optional(),
            "microwave": t.boolean().optional(),
            "snackbarException": t.string().optional(),
            "outdoorGrillException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "ovenException": t.string().optional(),
            "refrigerator": t.boolean().optional(),
            "toasterException": t.string().optional(),
            "stove": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "toaster": t.boolean().optional(),
            "microwaveException": t.string().optional(),
            "minibar": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaEatingOut"])
    types["EcoCertificationIn"] = t.struct(
        {
            "awarded": t.boolean().optional(),
            "awardedException": t.string().optional(),
            "ecoCertificate": t.string(),
        }
    ).named(renames["EcoCertificationIn"])
    types["EcoCertificationOut"] = t.struct(
        {
            "awarded": t.boolean().optional(),
            "awardedException": t.string().optional(),
            "ecoCertificate": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EcoCertificationOut"])
    types["GuestUnitTypeIn"] = t.struct(
        {
            "features": t.proxy(renames["GuestUnitFeaturesIn"]).optional(),
            "codes": t.array(t.string()),
            "label": t.string(),
        }
    ).named(renames["GuestUnitTypeIn"])
    types["GuestUnitTypeOut"] = t.struct(
        {
            "features": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "codes": t.array(t.string()),
            "label": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitTypeOut"])
    types["LodgingIn"] = t.struct(
        {
            "transportation": t.proxy(renames["TransportationIn"]).optional(),
            "activities": t.proxy(renames["ActivitiesIn"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataIn"]),
            "policies": t.proxy(renames["PoliciesIn"]).optional(),
            "business": t.proxy(renames["BusinessIn"]).optional(),
            "wellness": t.proxy(renames["WellnessIn"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
            "property": t.proxy(renames["PropertyIn"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
            "pools": t.proxy(renames["PoolsIn"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
            "parking": t.proxy(renames["ParkingIn"]).optional(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
            "families": t.proxy(renames["FamiliesIn"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
            "pets": t.proxy(renames["PetsIn"]).optional(),
            "services": t.proxy(renames["ServicesIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["LodgingIn"])
    types["LodgingOut"] = t.struct(
        {
            "transportation": t.proxy(renames["TransportationOut"]).optional(),
            "activities": t.proxy(renames["ActivitiesOut"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityOut"]).optional(),
            "someUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "metadata": t.proxy(renames["LodgingMetadataOut"]),
            "policies": t.proxy(renames["PoliciesOut"]).optional(),
            "business": t.proxy(renames["BusinessOut"]).optional(),
            "wellness": t.proxy(renames["WellnessOut"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyOut"]).optional(),
            "property": t.proxy(renames["PropertyOut"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityOut"]).optional(),
            "allUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "pools": t.proxy(renames["PoolsOut"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityOut"]).optional(),
            "parking": t.proxy(renames["ParkingOut"]).optional(),
            "foodAndDrink": t.proxy(renames["FoodAndDrinkOut"]).optional(),
            "families": t.proxy(renames["FamiliesOut"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingOut"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaOut"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeOut"])).optional(),
            "pets": t.proxy(renames["PetsOut"]).optional(),
            "services": t.proxy(renames["ServicesOut"]).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingOut"])

    functions = {}
    functions["locationsGetLodging"] = mybusinesslodging.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "transportation": t.proxy(renames["TransportationIn"]).optional(),
                "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
                "metadata": t.proxy(renames["LodgingMetadataIn"]),
                "policies": t.proxy(renames["PoliciesIn"]).optional(),
                "business": t.proxy(renames["BusinessIn"]).optional(),
                "wellness": t.proxy(renames["WellnessIn"]).optional(),
                "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
                "property": t.proxy(renames["PropertyIn"]).optional(),
                "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
                "pools": t.proxy(renames["PoolsIn"]).optional(),
                "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
                "parking": t.proxy(renames["ParkingIn"]).optional(),
                "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
                "families": t.proxy(renames["FamiliesIn"]).optional(),
                "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
                "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
                "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
                "pets": t.proxy(renames["PetsIn"]).optional(),
                "services": t.proxy(renames["ServicesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LodgingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsUpdateLodging"] = mybusinesslodging.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "transportation": t.proxy(renames["TransportationIn"]).optional(),
                "activities": t.proxy(renames["ActivitiesIn"]).optional(),
                "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
                "metadata": t.proxy(renames["LodgingMetadataIn"]),
                "policies": t.proxy(renames["PoliciesIn"]).optional(),
                "business": t.proxy(renames["BusinessIn"]).optional(),
                "wellness": t.proxy(renames["WellnessIn"]).optional(),
                "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
                "property": t.proxy(renames["PropertyIn"]).optional(),
                "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
                "pools": t.proxy(renames["PoolsIn"]).optional(),
                "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
                "parking": t.proxy(renames["ParkingIn"]).optional(),
                "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
                "families": t.proxy(renames["FamiliesIn"]).optional(),
                "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
                "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
                "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
                "pets": t.proxy(renames["PetsIn"]).optional(),
                "services": t.proxy(renames["ServicesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
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
