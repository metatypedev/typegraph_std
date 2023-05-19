from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinesslodging() -> Import:
    mybusinesslodging = HTTPRuntime("https://mybusinesslodging.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinesslodging_1_ErrorResponse",
        "EnergyEfficiencyIn": "_mybusinesslodging_2_EnergyEfficiencyIn",
        "EnergyEfficiencyOut": "_mybusinesslodging_3_EnergyEfficiencyOut",
        "LanguageSpokenIn": "_mybusinesslodging_4_LanguageSpokenIn",
        "LanguageSpokenOut": "_mybusinesslodging_5_LanguageSpokenOut",
        "PoolsIn": "_mybusinesslodging_6_PoolsIn",
        "PoolsOut": "_mybusinesslodging_7_PoolsOut",
        "AccessibilityIn": "_mybusinesslodging_8_AccessibilityIn",
        "AccessibilityOut": "_mybusinesslodging_9_AccessibilityOut",
        "ViewsFromUnitIn": "_mybusinesslodging_10_ViewsFromUnitIn",
        "ViewsFromUnitOut": "_mybusinesslodging_11_ViewsFromUnitOut",
        "PoliciesIn": "_mybusinesslodging_12_PoliciesIn",
        "PoliciesOut": "_mybusinesslodging_13_PoliciesOut",
        "EnhancedCleaningIn": "_mybusinesslodging_14_EnhancedCleaningIn",
        "EnhancedCleaningOut": "_mybusinesslodging_15_EnhancedCleaningOut",
        "PaymentOptionsIn": "_mybusinesslodging_16_PaymentOptionsIn",
        "PaymentOptionsOut": "_mybusinesslodging_17_PaymentOptionsOut",
        "ConnectivityIn": "_mybusinesslodging_18_ConnectivityIn",
        "ConnectivityOut": "_mybusinesslodging_19_ConnectivityOut",
        "FamiliesIn": "_mybusinesslodging_20_FamiliesIn",
        "FamiliesOut": "_mybusinesslodging_21_FamiliesOut",
        "PropertyIn": "_mybusinesslodging_22_PropertyIn",
        "PropertyOut": "_mybusinesslodging_23_PropertyOut",
        "GuestUnitFeaturesIn": "_mybusinesslodging_24_GuestUnitFeaturesIn",
        "GuestUnitFeaturesOut": "_mybusinesslodging_25_GuestUnitFeaturesOut",
        "LivingAreaLayoutIn": "_mybusinesslodging_26_LivingAreaLayoutIn",
        "LivingAreaLayoutOut": "_mybusinesslodging_27_LivingAreaLayoutOut",
        "LivingAreaSleepingIn": "_mybusinesslodging_28_LivingAreaSleepingIn",
        "LivingAreaSleepingOut": "_mybusinesslodging_29_LivingAreaSleepingOut",
        "LodgingIn": "_mybusinesslodging_30_LodgingIn",
        "LodgingOut": "_mybusinesslodging_31_LodgingOut",
        "PetsIn": "_mybusinesslodging_32_PetsIn",
        "PetsOut": "_mybusinesslodging_33_PetsOut",
        "MinimizedContactIn": "_mybusinesslodging_34_MinimizedContactIn",
        "MinimizedContactOut": "_mybusinesslodging_35_MinimizedContactOut",
        "PhysicalDistancingIn": "_mybusinesslodging_36_PhysicalDistancingIn",
        "PhysicalDistancingOut": "_mybusinesslodging_37_PhysicalDistancingOut",
        "EcoCertificationIn": "_mybusinesslodging_38_EcoCertificationIn",
        "EcoCertificationOut": "_mybusinesslodging_39_EcoCertificationOut",
        "TimeOfDayIn": "_mybusinesslodging_40_TimeOfDayIn",
        "TimeOfDayOut": "_mybusinesslodging_41_TimeOfDayOut",
        "LodgingMetadataIn": "_mybusinesslodging_42_LodgingMetadataIn",
        "LodgingMetadataOut": "_mybusinesslodging_43_LodgingMetadataOut",
        "SustainableSourcingIn": "_mybusinesslodging_44_SustainableSourcingIn",
        "SustainableSourcingOut": "_mybusinesslodging_45_SustainableSourcingOut",
        "LivingAreaFeaturesIn": "_mybusinesslodging_46_LivingAreaFeaturesIn",
        "LivingAreaFeaturesOut": "_mybusinesslodging_47_LivingAreaFeaturesOut",
        "ActivitiesIn": "_mybusinesslodging_48_ActivitiesIn",
        "ActivitiesOut": "_mybusinesslodging_49_ActivitiesOut",
        "LivingAreaIn": "_mybusinesslodging_50_LivingAreaIn",
        "LivingAreaOut": "_mybusinesslodging_51_LivingAreaOut",
        "SustainabilityIn": "_mybusinesslodging_52_SustainabilityIn",
        "SustainabilityOut": "_mybusinesslodging_53_SustainabilityOut",
        "TransportationIn": "_mybusinesslodging_54_TransportationIn",
        "TransportationOut": "_mybusinesslodging_55_TransportationOut",
        "LivingAreaAccessibilityIn": "_mybusinesslodging_56_LivingAreaAccessibilityIn",
        "LivingAreaAccessibilityOut": "_mybusinesslodging_57_LivingAreaAccessibilityOut",
        "HealthAndSafetyIn": "_mybusinesslodging_58_HealthAndSafetyIn",
        "HealthAndSafetyOut": "_mybusinesslodging_59_HealthAndSafetyOut",
        "ServicesIn": "_mybusinesslodging_60_ServicesIn",
        "ServicesOut": "_mybusinesslodging_61_ServicesOut",
        "SustainabilityCertificationsIn": "_mybusinesslodging_62_SustainabilityCertificationsIn",
        "SustainabilityCertificationsOut": "_mybusinesslodging_63_SustainabilityCertificationsOut",
        "GetGoogleUpdatedLodgingResponseIn": "_mybusinesslodging_64_GetGoogleUpdatedLodgingResponseIn",
        "GetGoogleUpdatedLodgingResponseOut": "_mybusinesslodging_65_GetGoogleUpdatedLodgingResponseOut",
        "BusinessIn": "_mybusinesslodging_66_BusinessIn",
        "BusinessOut": "_mybusinesslodging_67_BusinessOut",
        "PersonalProtectionIn": "_mybusinesslodging_68_PersonalProtectionIn",
        "PersonalProtectionOut": "_mybusinesslodging_69_PersonalProtectionOut",
        "LivingAreaEatingIn": "_mybusinesslodging_70_LivingAreaEatingIn",
        "LivingAreaEatingOut": "_mybusinesslodging_71_LivingAreaEatingOut",
        "ParkingIn": "_mybusinesslodging_72_ParkingIn",
        "ParkingOut": "_mybusinesslodging_73_ParkingOut",
        "WasteReductionIn": "_mybusinesslodging_74_WasteReductionIn",
        "WasteReductionOut": "_mybusinesslodging_75_WasteReductionOut",
        "FoodAndDrinkIn": "_mybusinesslodging_76_FoodAndDrinkIn",
        "FoodAndDrinkOut": "_mybusinesslodging_77_FoodAndDrinkOut",
        "HousekeepingIn": "_mybusinesslodging_78_HousekeepingIn",
        "HousekeepingOut": "_mybusinesslodging_79_HousekeepingOut",
        "WellnessIn": "_mybusinesslodging_80_WellnessIn",
        "WellnessOut": "_mybusinesslodging_81_WellnessOut",
        "IncreasedFoodSafetyIn": "_mybusinesslodging_82_IncreasedFoodSafetyIn",
        "IncreasedFoodSafetyOut": "_mybusinesslodging_83_IncreasedFoodSafetyOut",
        "WaterConservationIn": "_mybusinesslodging_84_WaterConservationIn",
        "WaterConservationOut": "_mybusinesslodging_85_WaterConservationOut",
        "GuestUnitTypeIn": "_mybusinesslodging_86_GuestUnitTypeIn",
        "GuestUnitTypeOut": "_mybusinesslodging_87_GuestUnitTypeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EnergyEfficiencyIn"] = t.struct(
        {
            "energyConservationProgramException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
        }
    ).named(renames["EnergyEfficiencyIn"])
    types["EnergyEfficiencyOut"] = t.struct(
        {
            "greenBuildingDesign": t.boolean().optional(),
            "energyConservationProgramException": t.string().optional(),
            "greenBuildingDesignException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystems": t.boolean().optional(),
            "energySavingThermostatsException": t.string().optional(),
            "energyConservationProgram": t.boolean().optional(),
            "energyEfficientLightingException": t.string().optional(),
            "energySavingThermostats": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUse": t.boolean().optional(),
            "carbonFreeEnergySourcesException": t.string().optional(),
            "energyEfficientHeatingAndCoolingSystemsException": t.string().optional(),
            "carbonFreeEnergySources": t.boolean().optional(),
            "energyEfficientLighting": t.boolean().optional(),
            "independentOrganizationAuditsEnergyUseException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnergyEfficiencyOut"])
    types["LanguageSpokenIn"] = t.struct(
        {
            "spoken": t.boolean().optional(),
            "spokenException": t.string().optional(),
            "languageCode": t.string(),
        }
    ).named(renames["LanguageSpokenIn"])
    types["LanguageSpokenOut"] = t.struct(
        {
            "spoken": t.boolean().optional(),
            "spokenException": t.string().optional(),
            "languageCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LanguageSpokenOut"])
    types["PoolsIn"] = t.struct(
        {
            "poolException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "wavePool": t.boolean().optional(),
            "waterParkException": t.string().optional(),
            "pool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "wadingPoolException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "lazyRiverException": t.string().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "lifeguard": t.boolean().optional(),
            "waterslideException": t.string().optional(),
            "wadingPool": t.boolean().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "adultPoolException": t.string().optional(),
            "hotTub": t.boolean().optional(),
            "outdoorPool": t.boolean().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "indoorPoolException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "outdoorPoolException": t.string().optional(),
            "lifeguardException": t.string().optional(),
        }
    ).named(renames["PoolsIn"])
    types["PoolsOut"] = t.struct(
        {
            "poolException": t.string().optional(),
            "adultPool": t.boolean().optional(),
            "hotTubException": t.string().optional(),
            "wavePool": t.boolean().optional(),
            "waterParkException": t.string().optional(),
            "pool": t.boolean().optional(),
            "waterPark": t.boolean().optional(),
            "wadingPoolException": t.string().optional(),
            "lazyRiver": t.boolean().optional(),
            "lazyRiverException": t.string().optional(),
            "indoorPoolsCount": t.integer().optional(),
            "lifeguard": t.boolean().optional(),
            "waterslideException": t.string().optional(),
            "wadingPool": t.boolean().optional(),
            "outdoorPoolsCount": t.integer().optional(),
            "outdoorPoolsCountException": t.string().optional(),
            "poolsCountException": t.string().optional(),
            "poolsCount": t.integer().optional(),
            "adultPoolException": t.string().optional(),
            "hotTub": t.boolean().optional(),
            "outdoorPool": t.boolean().optional(),
            "indoorPoolsCountException": t.string().optional(),
            "wavePoolException": t.string().optional(),
            "waterslide": t.boolean().optional(),
            "indoorPoolException": t.string().optional(),
            "indoorPool": t.boolean().optional(),
            "outdoorPoolException": t.string().optional(),
            "lifeguardException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoolsOut"])
    types["AccessibilityIn"] = t.struct(
        {
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
        }
    ).named(renames["AccessibilityIn"])
    types["AccessibilityOut"] = t.struct(
        {
            "mobilityAccessible": t.boolean().optional(),
            "mobilityAccessibleParkingException": t.string().optional(),
            "mobilityAccessibleElevatorException": t.string().optional(),
            "mobilityAccessiblePool": t.boolean().optional(),
            "mobilityAccessibleParking": t.boolean().optional(),
            "mobilityAccessiblePoolException": t.string().optional(),
            "mobilityAccessibleException": t.string().optional(),
            "mobilityAccessibleElevator": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessibilityOut"])
    types["ViewsFromUnitIn"] = t.struct(
        {
            "oceanViewException": t.string().optional(),
            "gardenViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "lakeView": t.boolean().optional(),
            "gardenView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "landmarkView": t.boolean().optional(),
            "cityViewException": t.string().optional(),
            "lakeViewException": t.string().optional(),
            "cityView": t.boolean().optional(),
            "oceanView": t.boolean().optional(),
            "poolViewException": t.string().optional(),
            "valleyView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
        }
    ).named(renames["ViewsFromUnitIn"])
    types["ViewsFromUnitOut"] = t.struct(
        {
            "oceanViewException": t.string().optional(),
            "gardenViewException": t.string().optional(),
            "landmarkViewException": t.string().optional(),
            "lakeView": t.boolean().optional(),
            "gardenView": t.boolean().optional(),
            "beachView": t.boolean().optional(),
            "landmarkView": t.boolean().optional(),
            "cityViewException": t.string().optional(),
            "lakeViewException": t.string().optional(),
            "cityView": t.boolean().optional(),
            "oceanView": t.boolean().optional(),
            "poolViewException": t.string().optional(),
            "valleyView": t.boolean().optional(),
            "valleyViewException": t.string().optional(),
            "beachViewException": t.string().optional(),
            "poolView": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViewsFromUnitOut"])
    types["PoliciesIn"] = t.struct(
        {
            "maxChildAge": t.integer().optional(),
            "kidsStayFree": t.boolean().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "checkinTimeException": t.string().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "maxChildAgeException": t.string().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "checkoutTimeException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsIn"]).optional(),
        }
    ).named(renames["PoliciesIn"])
    types["PoliciesOut"] = t.struct(
        {
            "maxChildAge": t.integer().optional(),
            "kidsStayFree": t.boolean().optional(),
            "smokeFreeProperty": t.boolean().optional(),
            "checkinTimeException": t.string().optional(),
            "checkinTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "maxChildAgeException": t.string().optional(),
            "allInclusiveOnlyException": t.string().optional(),
            "maxKidsStayFreeCountException": t.string().optional(),
            "allInclusiveAvailable": t.boolean().optional(),
            "allInclusiveOnly": t.boolean().optional(),
            "allInclusiveAvailableException": t.string().optional(),
            "kidsStayFreeException": t.string().optional(),
            "checkoutTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "checkoutTimeException": t.string().optional(),
            "smokeFreePropertyException": t.string().optional(),
            "maxKidsStayFreeCount": t.integer().optional(),
            "paymentOptions": t.proxy(renames["PaymentOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoliciesOut"])
    types["EnhancedCleaningIn"] = t.struct(
        {
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
        }
    ).named(renames["EnhancedCleaningIn"])
    types["EnhancedCleaningOut"] = t.struct(
        {
            "commercialGradeDisinfectantCleaning": t.boolean().optional(),
            "commercialGradeDisinfectantCleaningException": t.string().optional(),
            "employeesTrainedCleaningProceduresException": t.string().optional(),
            "employeesWearProtectiveEquipmentException": t.string().optional(),
            "employeesTrainedCleaningProcedures": t.boolean().optional(),
            "guestRoomsEnhancedCleaningException": t.string().optional(),
            "guestRoomsEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashingException": t.string().optional(),
            "commonAreasEnhancedCleaning": t.boolean().optional(),
            "employeesTrainedThoroughHandWashing": t.boolean().optional(),
            "employeesWearProtectiveEquipment": t.boolean().optional(),
            "commonAreasEnhancedCleaningException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnhancedCleaningOut"])
    types["PaymentOptionsIn"] = t.struct(
        {
            "creditCard": t.boolean().optional(),
            "cash": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "creditCardException": t.string().optional(),
            "debitCard": t.boolean().optional(),
            "mobileNfc": t.boolean().optional(),
            "cheque": t.boolean().optional(),
            "chequeException": t.string().optional(),
            "cashException": t.string().optional(),
            "debitCardException": t.string().optional(),
        }
    ).named(renames["PaymentOptionsIn"])
    types["PaymentOptionsOut"] = t.struct(
        {
            "creditCard": t.boolean().optional(),
            "cash": t.boolean().optional(),
            "mobileNfcException": t.string().optional(),
            "creditCardException": t.string().optional(),
            "debitCard": t.boolean().optional(),
            "mobileNfc": t.boolean().optional(),
            "cheque": t.boolean().optional(),
            "chequeException": t.string().optional(),
            "cashException": t.string().optional(),
            "debitCardException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PaymentOptionsOut"])
    types["ConnectivityIn"] = t.struct(
        {
            "freeWifi": t.boolean().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "freeWifiException": t.string().optional(),
            "wifiAvailable": t.boolean().optional(),
        }
    ).named(renames["ConnectivityIn"])
    types["ConnectivityOut"] = t.struct(
        {
            "freeWifi": t.boolean().optional(),
            "publicInternetTerminal": t.boolean().optional(),
            "publicAreaWifiAvailable": t.boolean().optional(),
            "publicAreaWifiAvailableException": t.string().optional(),
            "wifiAvailableException": t.string().optional(),
            "publicInternetTerminalException": t.string().optional(),
            "freeWifiException": t.string().optional(),
            "wifiAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectivityOut"])
    types["FamiliesIn"] = t.struct(
        {
            "kidsActivitiesException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
            "kidsFriendly": t.boolean().optional(),
            "kidsActivities": t.boolean().optional(),
            "babysittingException": t.string().optional(),
            "babysitting": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
        }
    ).named(renames["FamiliesIn"])
    types["FamiliesOut"] = t.struct(
        {
            "kidsActivitiesException": t.string().optional(),
            "kidsClub": t.boolean().optional(),
            "kidsFriendly": t.boolean().optional(),
            "kidsActivities": t.boolean().optional(),
            "babysittingException": t.string().optional(),
            "babysitting": t.boolean().optional(),
            "kidsFriendlyException": t.string().optional(),
            "kidsClubException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamiliesOut"])
    types["PropertyIn"] = t.struct(
        {
            "lastRenovatedYearException": t.string().optional(),
            "builtYear": t.integer().optional(),
            "roomsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "floorsCount": t.integer().optional(),
            "floorsCountException": t.string().optional(),
            "roomsCountException": t.string().optional(),
        }
    ).named(renames["PropertyIn"])
    types["PropertyOut"] = t.struct(
        {
            "lastRenovatedYearException": t.string().optional(),
            "builtYear": t.integer().optional(),
            "roomsCount": t.integer().optional(),
            "builtYearException": t.string().optional(),
            "lastRenovatedYear": t.integer().optional(),
            "floorsCount": t.integer().optional(),
            "floorsCountException": t.string().optional(),
            "roomsCountException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PropertyOut"])
    types["GuestUnitFeaturesIn"] = t.struct(
        {
            "maxOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaIn"]).optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "executiveFloor": t.boolean().optional(),
            "privateHome": t.boolean().optional(),
            "suite": t.boolean().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "suiteException": t.string().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "tierException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "tier": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "views": t.proxy(renames["ViewsFromUnitIn"]).optional(),
        }
    ).named(renames["GuestUnitFeaturesIn"])
    types["GuestUnitFeaturesOut"] = t.struct(
        {
            "maxOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCountException": t.string().optional(),
            "totalLivingAreas": t.proxy(renames["LivingAreaOut"]).optional(),
            "bungalowOrVilla": t.boolean().optional(),
            "executiveFloor": t.boolean().optional(),
            "privateHome": t.boolean().optional(),
            "suite": t.boolean().optional(),
            "connectingUnitAvailable": t.boolean().optional(),
            "suiteException": t.string().optional(),
            "maxOccupantsCountException": t.string().optional(),
            "executiveFloorException": t.string().optional(),
            "tierException": t.string().optional(),
            "bungalowOrVillaException": t.string().optional(),
            "tier": t.string().optional(),
            "connectingUnitAvailableException": t.string().optional(),
            "maxAdultOccupantsCountException": t.string().optional(),
            "privateHomeException": t.string().optional(),
            "maxAdultOccupantsCount": t.integer().optional(),
            "maxChildOccupantsCount": t.integer().optional(),
            "views": t.proxy(renames["ViewsFromUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GuestUnitFeaturesOut"])
    types["LivingAreaLayoutIn"] = t.struct(
        {
            "stairsException": t.string().optional(),
            "patioException": t.string().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "nonSmoking": t.boolean().optional(),
            "nonSmokingException": t.string().optional(),
            "patio": t.boolean().optional(),
            "balcony": t.boolean().optional(),
            "stairs": t.boolean().optional(),
            "loftException": t.string().optional(),
            "loft": t.boolean().optional(),
            "balconyException": t.string().optional(),
            "livingAreaSqMetersException": t.string().optional(),
        }
    ).named(renames["LivingAreaLayoutIn"])
    types["LivingAreaLayoutOut"] = t.struct(
        {
            "stairsException": t.string().optional(),
            "patioException": t.string().optional(),
            "livingAreaSqMeters": t.number().optional(),
            "nonSmoking": t.boolean().optional(),
            "nonSmokingException": t.string().optional(),
            "patio": t.boolean().optional(),
            "balcony": t.boolean().optional(),
            "stairs": t.boolean().optional(),
            "loftException": t.string().optional(),
            "loft": t.boolean().optional(),
            "balconyException": t.string().optional(),
            "livingAreaSqMetersException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaLayoutOut"])
    types["LivingAreaSleepingIn"] = t.struct(
        {
            "featherPillows": t.boolean().optional(),
            "syntheticPillows": t.boolean().optional(),
            "doubleBedsCount": t.integer().optional(),
            "cribsCount": t.integer().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "sofaBedsCount": t.integer().optional(),
            "bunkBedsCount": t.integer().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "kingBedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "sofaBedsCountException": t.string().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "bedsCount": t.integer().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCountException": t.string().optional(),
            "otherBedsCountException": t.string().optional(),
            "queenBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "bedsCountException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "bunkBedsCountException": t.string().optional(),
        }
    ).named(renames["LivingAreaSleepingIn"])
    types["LivingAreaSleepingOut"] = t.struct(
        {
            "featherPillows": t.boolean().optional(),
            "syntheticPillows": t.boolean().optional(),
            "doubleBedsCount": t.integer().optional(),
            "cribsCount": t.integer().optional(),
            "hypoallergenicBedding": t.boolean().optional(),
            "sofaBedsCount": t.integer().optional(),
            "bunkBedsCount": t.integer().optional(),
            "rollAwayBedsCount": t.integer().optional(),
            "kingBedsCount": t.integer().optional(),
            "kingBedsCountException": t.string().optional(),
            "otherBedsCount": t.integer().optional(),
            "sofaBedsCountException": t.string().optional(),
            "memoryFoamPillows": t.boolean().optional(),
            "bedsCount": t.integer().optional(),
            "singleOrTwinBedsCountException": t.string().optional(),
            "rollAwayBedsCountException": t.string().optional(),
            "queenBedsCount": t.integer().optional(),
            "syntheticPillowsException": t.string().optional(),
            "doubleBedsCountException": t.string().optional(),
            "otherBedsCountException": t.string().optional(),
            "queenBedsCountException": t.string().optional(),
            "memoryFoamPillowsException": t.string().optional(),
            "bedsCountException": t.string().optional(),
            "singleOrTwinBedsCount": t.integer().optional(),
            "featherPillowsException": t.string().optional(),
            "cribsCountException": t.string().optional(),
            "hypoallergenicBeddingException": t.string().optional(),
            "bunkBedsCountException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaSleepingOut"])
    types["LodgingIn"] = t.struct(
        {
            "foodAndDrink": t.proxy(renames["FoodAndDrinkIn"]).optional(),
            "wellness": t.proxy(renames["WellnessIn"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyIn"]).optional(),
            "pools": t.proxy(renames["PoolsIn"]).optional(),
            "property": t.proxy(renames["PropertyIn"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityIn"]).optional(),
            "business": t.proxy(renames["BusinessIn"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityIn"]).optional(),
            "policies": t.proxy(renames["PoliciesIn"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityIn"]).optional(),
            "parking": t.proxy(renames["ParkingIn"]).optional(),
            "name": t.string(),
            "metadata": t.proxy(renames["LodgingMetadataIn"]),
            "services": t.proxy(renames["ServicesIn"]).optional(),
            "activities": t.proxy(renames["ActivitiesIn"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaIn"]).optional(),
            "pets": t.proxy(renames["PetsIn"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingIn"]).optional(),
            "families": t.proxy(renames["FamiliesIn"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeIn"])).optional(),
            "transportation": t.proxy(renames["TransportationIn"]).optional(),
        }
    ).named(renames["LodgingIn"])
    types["LodgingOut"] = t.struct(
        {
            "foodAndDrink": t.proxy(renames["FoodAndDrinkOut"]).optional(),
            "wellness": t.proxy(renames["WellnessOut"]).optional(),
            "healthAndSafety": t.proxy(renames["HealthAndSafetyOut"]).optional(),
            "pools": t.proxy(renames["PoolsOut"]).optional(),
            "property": t.proxy(renames["PropertyOut"]).optional(),
            "connectivity": t.proxy(renames["ConnectivityOut"]).optional(),
            "business": t.proxy(renames["BusinessOut"]).optional(),
            "accessibility": t.proxy(renames["AccessibilityOut"]).optional(),
            "someUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "policies": t.proxy(renames["PoliciesOut"]).optional(),
            "sustainability": t.proxy(renames["SustainabilityOut"]).optional(),
            "parking": t.proxy(renames["ParkingOut"]).optional(),
            "name": t.string(),
            "metadata": t.proxy(renames["LodgingMetadataOut"]),
            "services": t.proxy(renames["ServicesOut"]).optional(),
            "activities": t.proxy(renames["ActivitiesOut"]).optional(),
            "commonLivingArea": t.proxy(renames["LivingAreaOut"]).optional(),
            "pets": t.proxy(renames["PetsOut"]).optional(),
            "housekeeping": t.proxy(renames["HousekeepingOut"]).optional(),
            "families": t.proxy(renames["FamiliesOut"]).optional(),
            "guestUnits": t.array(t.proxy(renames["GuestUnitTypeOut"])).optional(),
            "allUnits": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "transportation": t.proxy(renames["TransportationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingOut"])
    types["PetsIn"] = t.struct(
        {
            "petsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "petsAllowedException": t.string().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowed": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowedFreeException": t.string().optional(),
        }
    ).named(renames["PetsIn"])
    types["PetsOut"] = t.struct(
        {
            "petsAllowed": t.boolean().optional(),
            "petsAllowedFree": t.boolean().optional(),
            "petsAllowedException": t.string().optional(),
            "catsAllowed": t.boolean().optional(),
            "dogsAllowed": t.boolean().optional(),
            "catsAllowedException": t.string().optional(),
            "dogsAllowedException": t.string().optional(),
            "petsAllowedFreeException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PetsOut"])
    types["MinimizedContactIn"] = t.struct(
        {
            "contactlessCheckinCheckoutException": t.string().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
        }
    ).named(renames["MinimizedContactIn"])
    types["MinimizedContactOut"] = t.struct(
        {
            "contactlessCheckinCheckoutException": t.string().optional(),
            "housekeepingScheduledRequestOnlyException": t.string().optional(),
            "digitalGuestRoomKeys": t.boolean().optional(),
            "roomBookingsBuffer": t.boolean().optional(),
            "housekeepingScheduledRequestOnly": t.boolean().optional(),
            "roomBookingsBufferException": t.string().optional(),
            "noHighTouchItemsCommonAreas": t.boolean().optional(),
            "noHighTouchItemsGuestRoomsException": t.string().optional(),
            "noHighTouchItemsCommonAreasException": t.string().optional(),
            "plasticKeycardsDisinfectedException": t.string().optional(),
            "noHighTouchItemsGuestRooms": t.boolean().optional(),
            "contactlessCheckinCheckout": t.boolean().optional(),
            "plasticKeycardsDisinfected": t.boolean().optional(),
            "digitalGuestRoomKeysException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MinimizedContactOut"])
    types["PhysicalDistancingIn"] = t.struct(
        {
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "safetyDividersException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
        }
    ).named(renames["PhysicalDistancingIn"])
    types["PhysicalDistancingOut"] = t.struct(
        {
            "sharedAreasLimitedOccupancy": t.boolean().optional(),
            "wellnessAreasHavePrivateSpaces": t.boolean().optional(),
            "commonAreasPhysicalDistancingArranged": t.boolean().optional(),
            "safetyDividersException": t.string().optional(),
            "commonAreasPhysicalDistancingArrangedException": t.string().optional(),
            "physicalDistancingRequiredException": t.string().optional(),
            "wellnessAreasHavePrivateSpacesException": t.string().optional(),
            "safetyDividers": t.boolean().optional(),
            "physicalDistancingRequired": t.boolean().optional(),
            "sharedAreasLimitedOccupancyException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhysicalDistancingOut"])
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
    types["LodgingMetadataIn"] = t.struct({"updateTime": t.string()}).named(
        renames["LodgingMetadataIn"]
    )
    types["LodgingMetadataOut"] = t.struct(
        {
            "updateTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LodgingMetadataOut"])
    types["SustainableSourcingIn"] = t.struct(
        {
            "responsiblySourcesSeafoodException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "veganMealsException": t.string().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "veganMeals": t.boolean().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "vegetarianMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
        }
    ).named(renames["SustainableSourcingIn"])
    types["SustainableSourcingOut"] = t.struct(
        {
            "responsiblySourcesSeafoodException": t.string().optional(),
            "responsiblePurchasingPolicyException": t.string().optional(),
            "ecoFriendlyToiletries": t.boolean().optional(),
            "locallySourcedFoodAndBeveragesException": t.string().optional(),
            "organicCageFreeEggsException": t.string().optional(),
            "veganMealsException": t.string().optional(),
            "vegetarianMeals": t.boolean().optional(),
            "ecoFriendlyToiletriesException": t.string().optional(),
            "responsiblePurchasingPolicy": t.boolean().optional(),
            "responsiblySourcesSeafood": t.boolean().optional(),
            "organicFoodAndBeveragesException": t.string().optional(),
            "organicCageFreeEggs": t.boolean().optional(),
            "veganMeals": t.boolean().optional(),
            "locallySourcedFoodAndBeverages": t.boolean().optional(),
            "vegetarianMealsException": t.string().optional(),
            "organicFoodAndBeverages": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainableSourcingOut"])
    types["LivingAreaFeaturesIn"] = t.struct(
        {
            "payPerViewMoviesException": t.string().optional(),
            "washer": t.boolean().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "tvStreamingException": t.string().optional(),
            "tvException": t.string().optional(),
            "tvCasting": t.boolean().optional(),
            "dryerException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "toilet": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "bathtubException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "dryer": t.boolean().optional(),
            "bidetException": t.string().optional(),
            "shower": t.boolean().optional(),
            "washerException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "toiletException": t.string().optional(),
            "fireplace": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "heating": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "hairdryer": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "heatingException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "showerException": t.string().optional(),
            "tvCastingException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "privateBathroomException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "privateBathroom": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
        }
    ).named(renames["LivingAreaFeaturesIn"])
    types["LivingAreaFeaturesOut"] = t.struct(
        {
            "payPerViewMoviesException": t.string().optional(),
            "washer": t.boolean().optional(),
            "inunitWifiAvailableException": t.string().optional(),
            "tvStreamingException": t.string().optional(),
            "tvException": t.string().optional(),
            "tvCasting": t.boolean().optional(),
            "dryerException": t.string().optional(),
            "universalPowerAdapters": t.boolean().optional(),
            "toilet": t.boolean().optional(),
            "inunitWifiAvailable": t.boolean().optional(),
            "bathtubException": t.string().optional(),
            "electronicRoomKey": t.boolean().optional(),
            "dryer": t.boolean().optional(),
            "bidetException": t.string().optional(),
            "shower": t.boolean().optional(),
            "washerException": t.string().optional(),
            "bidet": t.boolean().optional(),
            "toiletException": t.string().optional(),
            "fireplace": t.boolean().optional(),
            "tv": t.boolean().optional(),
            "airConditioning": t.boolean().optional(),
            "heating": t.boolean().optional(),
            "electronicRoomKeyException": t.string().optional(),
            "airConditioningException": t.string().optional(),
            "tvStreaming": t.boolean().optional(),
            "payPerViewMovies": t.boolean().optional(),
            "hairdryer": t.boolean().optional(),
            "bathtub": t.boolean().optional(),
            "heatingException": t.string().optional(),
            "ironingEquipment": t.boolean().optional(),
            "inunitSafe": t.boolean().optional(),
            "showerException": t.string().optional(),
            "tvCastingException": t.string().optional(),
            "ironingEquipmentException": t.string().optional(),
            "universalPowerAdaptersException": t.string().optional(),
            "hairdryerException": t.string().optional(),
            "privateBathroomException": t.string().optional(),
            "fireplaceException": t.string().optional(),
            "privateBathroom": t.boolean().optional(),
            "inunitSafeException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaFeaturesOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "beachAccessException": t.string().optional(),
            "tennis": t.boolean().optional(),
            "golf": t.boolean().optional(),
            "golfException": t.string().optional(),
            "privateBeach": t.boolean().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "bicycleRental": t.boolean().optional(),
            "scuba": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "nightclub": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "beachFront": t.boolean().optional(),
            "horsebackRidingException": t.string().optional(),
            "boutiqueStores": t.boolean().optional(),
            "waterSkiing": t.boolean().optional(),
            "beachAccess": t.boolean().optional(),
            "nightclubException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
            "casinoException": t.string().optional(),
            "snorkeling": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "bicycleRentalException": t.string().optional(),
            "horsebackRiding": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "tennisException": t.string().optional(),
            "scubaException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "watercraftRental": t.boolean().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "gameRoom": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "beachAccessException": t.string().optional(),
            "tennis": t.boolean().optional(),
            "golf": t.boolean().optional(),
            "golfException": t.string().optional(),
            "privateBeach": t.boolean().optional(),
            "freeBicycleRental": t.boolean().optional(),
            "snorkelingException": t.string().optional(),
            "bicycleRental": t.boolean().optional(),
            "scuba": t.boolean().optional(),
            "boutiqueStoresException": t.string().optional(),
            "nightclub": t.boolean().optional(),
            "freeWatercraftRentalException": t.string().optional(),
            "gameRoomException": t.string().optional(),
            "beachFront": t.boolean().optional(),
            "horsebackRidingException": t.string().optional(),
            "boutiqueStores": t.boolean().optional(),
            "waterSkiing": t.boolean().optional(),
            "beachAccess": t.boolean().optional(),
            "nightclubException": t.string().optional(),
            "waterSkiingException": t.string().optional(),
            "casinoException": t.string().optional(),
            "snorkeling": t.boolean().optional(),
            "casino": t.boolean().optional(),
            "bicycleRentalException": t.string().optional(),
            "horsebackRiding": t.boolean().optional(),
            "privateBeachException": t.string().optional(),
            "tennisException": t.string().optional(),
            "scubaException": t.string().optional(),
            "watercraftRentalException": t.string().optional(),
            "watercraftRental": t.boolean().optional(),
            "freeBicycleRentalException": t.string().optional(),
            "gameRoom": t.boolean().optional(),
            "freeWatercraftRental": t.boolean().optional(),
            "beachFrontException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["LivingAreaIn"] = t.struct(
        {
            "layout": t.proxy(renames["LivingAreaLayoutIn"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityIn"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingIn"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingIn"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesIn"]).optional(),
        }
    ).named(renames["LivingAreaIn"])
    types["LivingAreaOut"] = t.struct(
        {
            "layout": t.proxy(renames["LivingAreaLayoutOut"]).optional(),
            "accessibility": t.proxy(renames["LivingAreaAccessibilityOut"]).optional(),
            "sleeping": t.proxy(renames["LivingAreaSleepingOut"]).optional(),
            "eating": t.proxy(renames["LivingAreaEatingOut"]).optional(),
            "features": t.proxy(renames["LivingAreaFeaturesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaOut"])
    types["SustainabilityIn"] = t.struct(
        {
            "wasteReduction": t.proxy(renames["WasteReductionIn"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsIn"]
            ).optional(),
            "sustainableSourcing": t.proxy(renames["SustainableSourcingIn"]).optional(),
            "waterConservation": t.proxy(renames["WaterConservationIn"]).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyIn"]).optional(),
        }
    ).named(renames["SustainabilityIn"])
    types["SustainabilityOut"] = t.struct(
        {
            "wasteReduction": t.proxy(renames["WasteReductionOut"]).optional(),
            "sustainabilityCertifications": t.proxy(
                renames["SustainabilityCertificationsOut"]
            ).optional(),
            "sustainableSourcing": t.proxy(
                renames["SustainableSourcingOut"]
            ).optional(),
            "waterConservation": t.proxy(renames["WaterConservationOut"]).optional(),
            "energyEfficiency": t.proxy(renames["EnergyEfficiencyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityOut"])
    types["TransportationIn"] = t.struct(
        {
            "freeAirportShuttleException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "transferException": t.string().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "transfer": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
        }
    ).named(renames["TransportationIn"])
    types["TransportationOut"] = t.struct(
        {
            "freeAirportShuttleException": t.string().optional(),
            "privateCarServiceException": t.string().optional(),
            "airportShuttle": t.boolean().optional(),
            "carRentalOnPropertyException": t.string().optional(),
            "airportShuttleException": t.string().optional(),
            "freeAirportShuttle": t.boolean().optional(),
            "transferException": t.string().optional(),
            "freePrivateCarService": t.boolean().optional(),
            "privateCarService": t.boolean().optional(),
            "freePrivateCarServiceException": t.string().optional(),
            "localShuttle": t.boolean().optional(),
            "carRentalOnProperty": t.boolean().optional(),
            "transfer": t.boolean().optional(),
            "localShuttleException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransportationOut"])
    types["LivingAreaAccessibilityIn"] = t.struct(
        {
            "mobilityAccessibleToiletException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
        }
    ).named(renames["LivingAreaAccessibilityIn"])
    types["LivingAreaAccessibilityOut"] = t.struct(
        {
            "mobilityAccessibleToiletException": t.string().optional(),
            "mobilityAccessibleBathtub": t.boolean().optional(),
            "hearingAccessibleFireAlarm": t.boolean().optional(),
            "hearingAccessibleUnit": t.boolean().optional(),
            "mobilityAccessibleShowerException": t.string().optional(),
            "adaCompliantUnit": t.boolean().optional(),
            "hearingAccessibleDoorbell": t.boolean().optional(),
            "mobilityAccessibleShower": t.boolean().optional(),
            "hearingAccessibleDoorbellException": t.string().optional(),
            "mobilityAccessibleToilet": t.boolean().optional(),
            "mobilityAccessibleBathtubException": t.string().optional(),
            "mobilityAccessibleUnit": t.boolean().optional(),
            "hearingAccessibleUnitException": t.string().optional(),
            "adaCompliantUnitException": t.string().optional(),
            "mobilityAccessibleUnitException": t.string().optional(),
            "hearingAccessibleFireAlarmException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaAccessibilityOut"])
    types["HealthAndSafetyIn"] = t.struct(
        {
            "minimizedContact": t.proxy(renames["MinimizedContactIn"]).optional(),
            "increasedFoodSafety": t.proxy(renames["IncreasedFoodSafetyIn"]).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingIn"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionIn"]).optional(),
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningIn"]).optional(),
        }
    ).named(renames["HealthAndSafetyIn"])
    types["HealthAndSafetyOut"] = t.struct(
        {
            "minimizedContact": t.proxy(renames["MinimizedContactOut"]).optional(),
            "increasedFoodSafety": t.proxy(
                renames["IncreasedFoodSafetyOut"]
            ).optional(),
            "physicalDistancing": t.proxy(renames["PhysicalDistancingOut"]).optional(),
            "personalProtection": t.proxy(renames["PersonalProtectionOut"]).optional(),
            "enhancedCleaning": t.proxy(renames["EnhancedCleaningOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthAndSafetyOut"])
    types["ServicesIn"] = t.struct(
        {
            "wakeUpCallsException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "concierge": t.boolean().optional(),
            "languagesSpoken": t.array(t.proxy(renames["LanguageSpokenIn"])).optional(),
            "frontDeskException": t.string().optional(),
            "currencyExchange": t.boolean().optional(),
            "socialHourException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "convenienceStoreException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "elevator": t.boolean().optional(),
            "frontDesk": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "giftShop": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "elevatorException": t.string().optional(),
        }
    ).named(renames["ServicesIn"])
    types["ServicesOut"] = t.struct(
        {
            "wakeUpCallsException": t.string().optional(),
            "giftShopException": t.string().optional(),
            "wakeUpCalls": t.boolean().optional(),
            "selfServiceLaundryException": t.string().optional(),
            "concierge": t.boolean().optional(),
            "languagesSpoken": t.array(
                t.proxy(renames["LanguageSpokenOut"])
            ).optional(),
            "frontDeskException": t.string().optional(),
            "currencyExchange": t.boolean().optional(),
            "socialHourException": t.string().optional(),
            "socialHour": t.boolean().optional(),
            "conciergeException": t.string().optional(),
            "twentyFourHourFrontDesk": t.boolean().optional(),
            "convenienceStoreException": t.string().optional(),
            "convenienceStore": t.boolean().optional(),
            "elevator": t.boolean().optional(),
            "frontDesk": t.boolean().optional(),
            "currencyExchangeException": t.string().optional(),
            "fullServiceLaundry": t.boolean().optional(),
            "baggageStorage": t.boolean().optional(),
            "selfServiceLaundry": t.boolean().optional(),
            "twentyFourHourFrontDeskException": t.string().optional(),
            "giftShop": t.boolean().optional(),
            "baggageStorageException": t.string().optional(),
            "fullServiceLaundryException": t.string().optional(),
            "elevatorException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicesOut"])
    types["SustainabilityCertificationsIn"] = t.struct(
        {
            "leedCertification": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationIn"])
            ).optional(),
            "breeamCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
        }
    ).named(renames["SustainabilityCertificationsIn"])
    types["SustainabilityCertificationsOut"] = t.struct(
        {
            "leedCertification": t.string().optional(),
            "leedCertificationException": t.string().optional(),
            "ecoCertifications": t.array(
                t.proxy(renames["EcoCertificationOut"])
            ).optional(),
            "breeamCertificationException": t.string().optional(),
            "breeamCertification": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SustainabilityCertificationsOut"])
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
    types["BusinessIn"] = t.struct(
        {
            "meetingRoomsException": t.string().optional(),
            "meetingRooms": t.boolean().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenter": t.boolean().optional(),
        }
    ).named(renames["BusinessIn"])
    types["BusinessOut"] = t.struct(
        {
            "meetingRoomsException": t.string().optional(),
            "meetingRooms": t.boolean().optional(),
            "meetingRoomsCount": t.integer().optional(),
            "businessCenterException": t.string().optional(),
            "meetingRoomsCountException": t.string().optional(),
            "businessCenter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BusinessOut"])
    types["PersonalProtectionIn"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
        }
    ).named(renames["PersonalProtectionIn"])
    types["PersonalProtectionOut"] = t.struct(
        {
            "protectiveEquipmentAvailable": t.boolean().optional(),
            "faceMaskRequired": t.boolean().optional(),
            "faceMaskRequiredException": t.string().optional(),
            "commonAreasOfferSanitizingItemsException": t.string().optional(),
            "guestRoomHygieneKitsAvailable": t.boolean().optional(),
            "guestRoomHygieneKitsAvailableException": t.string().optional(),
            "commonAreasOfferSanitizingItems": t.boolean().optional(),
            "protectiveEquipmentAvailableException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalProtectionOut"])
    types["LivingAreaEatingIn"] = t.struct(
        {
            "ovenException": t.string().optional(),
            "sinkException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "minibar": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
            "sink": t.boolean().optional(),
            "stoveException": t.string().optional(),
            "microwave": t.boolean().optional(),
            "cookwareException": t.string().optional(),
            "kettleException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "stove": t.boolean().optional(),
            "cookware": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "refrigerator": t.boolean().optional(),
            "oven": t.boolean().optional(),
            "outdoorGrillException": t.string().optional(),
            "coffeeMaker": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "kitchenAvailableException": t.string().optional(),
            "toasterException": t.string().optional(),
            "microwaveException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "snackbar": t.boolean().optional(),
            "kettle": t.boolean().optional(),
            "outdoorGrill": t.boolean().optional(),
            "toaster": t.boolean().optional(),
        }
    ).named(renames["LivingAreaEatingIn"])
    types["LivingAreaEatingOut"] = t.struct(
        {
            "ovenException": t.string().optional(),
            "sinkException": t.string().optional(),
            "indoorGrillException": t.string().optional(),
            "indoorGrill": t.boolean().optional(),
            "dishwasherException": t.string().optional(),
            "dishwasher": t.boolean().optional(),
            "minibar": t.boolean().optional(),
            "coffeeMakerException": t.string().optional(),
            "sink": t.boolean().optional(),
            "stoveException": t.string().optional(),
            "microwave": t.boolean().optional(),
            "cookwareException": t.string().optional(),
            "kettleException": t.string().optional(),
            "snackbarException": t.string().optional(),
            "stove": t.boolean().optional(),
            "cookware": t.boolean().optional(),
            "teaStation": t.boolean().optional(),
            "refrigerator": t.boolean().optional(),
            "oven": t.boolean().optional(),
            "outdoorGrillException": t.string().optional(),
            "coffeeMaker": t.boolean().optional(),
            "minibarException": t.string().optional(),
            "kitchenAvailable": t.boolean().optional(),
            "teaStationException": t.string().optional(),
            "kitchenAvailableException": t.string().optional(),
            "toasterException": t.string().optional(),
            "microwaveException": t.string().optional(),
            "refrigeratorException": t.string().optional(),
            "snackbar": t.boolean().optional(),
            "kettle": t.boolean().optional(),
            "outdoorGrill": t.boolean().optional(),
            "toaster": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivingAreaEatingOut"])
    types["ParkingIn"] = t.struct(
        {
            "parkingAvailableException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "valetParkingAvailable": t.boolean().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "freeParking": t.boolean().optional(),
            "freeValetParkingException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "electricCarChargingStations": t.boolean().optional(),
        }
    ).named(renames["ParkingIn"])
    types["ParkingOut"] = t.struct(
        {
            "parkingAvailableException": t.string().optional(),
            "freeSelfParking": t.boolean().optional(),
            "valetParkingAvailable": t.boolean().optional(),
            "electricCarChargingStationsException": t.string().optional(),
            "freeValetParking": t.boolean().optional(),
            "selfParkingAvailableException": t.string().optional(),
            "valetParkingAvailableException": t.string().optional(),
            "parkingAvailable": t.boolean().optional(),
            "freeParkingException": t.string().optional(),
            "freeParking": t.boolean().optional(),
            "freeValetParkingException": t.string().optional(),
            "freeSelfParkingException": t.string().optional(),
            "selfParkingAvailable": t.boolean().optional(),
            "electricCarChargingStations": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ParkingOut"])
    types["WasteReductionIn"] = t.struct(
        {
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
        }
    ).named(renames["WasteReductionIn"])
    types["WasteReductionOut"] = t.struct(
        {
            "safelyDisposesElectronicsException": t.string().optional(),
            "safelyDisposesLightbulbs": t.boolean().optional(),
            "compostableFoodContainersAndCutleryException": t.string().optional(),
            "safelyHandlesHazardousSubstances": t.boolean().optional(),
            "refillableToiletryContainers": t.boolean().optional(),
            "refillableToiletryContainersException": t.string().optional(),
            "noSingleUsePlasticWaterBottlesException": t.string().optional(),
            "safelyHandlesHazardousSubstancesException": t.string().optional(),
            "noSingleUsePlasticWaterBottles": t.boolean().optional(),
            "recyclingProgram": t.boolean().optional(),
            "toiletryDonationProgram": t.boolean().optional(),
            "soapDonationProgramException": t.string().optional(),
            "safelyDisposesLightbulbsException": t.string().optional(),
            "toiletryDonationProgramException": t.string().optional(),
            "waterBottleFillingStations": t.boolean().optional(),
            "waterBottleFillingStationsException": t.string().optional(),
            "recyclingProgramException": t.string().optional(),
            "noStyrofoamFoodContainers": t.boolean().optional(),
            "safelyDisposesBatteries": t.boolean().optional(),
            "foodWasteReductionProgramException": t.string().optional(),
            "noSingleUsePlasticStraws": t.boolean().optional(),
            "soapDonationProgram": t.boolean().optional(),
            "safelyDisposesElectronics": t.boolean().optional(),
            "compostsExcessFoodException": t.string().optional(),
            "donatesExcessFood": t.boolean().optional(),
            "compostableFoodContainersAndCutlery": t.boolean().optional(),
            "safelyDisposesBatteriesException": t.string().optional(),
            "noSingleUsePlasticStrawsException": t.string().optional(),
            "donatesExcessFoodException": t.string().optional(),
            "foodWasteReductionProgram": t.boolean().optional(),
            "compostsExcessFood": t.boolean().optional(),
            "noStyrofoamFoodContainersException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WasteReductionOut"])
    types["FoodAndDrinkIn"] = t.struct(
        {
            "breakfastAvailableException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "freeBreakfast": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "barException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "restaurant": t.boolean().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "buffetException": t.string().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "tableServiceException": t.string().optional(),
            "bar": t.boolean().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "roomServiceException": t.string().optional(),
            "roomService": t.boolean().optional(),
            "breakfastBuffetException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "tableService": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "restaurantsCount": t.integer().optional(),
            "vendingMachineException": t.string().optional(),
        }
    ).named(renames["FoodAndDrinkIn"])
    types["FoodAndDrinkOut"] = t.struct(
        {
            "breakfastAvailableException": t.string().optional(),
            "restaurantException": t.string().optional(),
            "freeBreakfast": t.boolean().optional(),
            "vendingMachine": t.boolean().optional(),
            "barException": t.string().optional(),
            "freeBreakfastException": t.string().optional(),
            "restaurant": t.boolean().optional(),
            "twentyFourHourRoomService": t.boolean().optional(),
            "breakfastAvailable": t.boolean().optional(),
            "restaurantsCountException": t.string().optional(),
            "dinnerBuffetException": t.string().optional(),
            "buffetException": t.string().optional(),
            "breakfastBuffet": t.boolean().optional(),
            "tableServiceException": t.string().optional(),
            "bar": t.boolean().optional(),
            "dinnerBuffet": t.boolean().optional(),
            "roomServiceException": t.string().optional(),
            "roomService": t.boolean().optional(),
            "breakfastBuffetException": t.string().optional(),
            "buffet": t.boolean().optional(),
            "tableService": t.boolean().optional(),
            "twentyFourHourRoomServiceException": t.string().optional(),
            "restaurantsCount": t.integer().optional(),
            "vendingMachineException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FoodAndDrinkOut"])
    types["HousekeepingIn"] = t.struct(
        {
            "housekeepingAvailableException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "dailyHousekeepingException": t.string().optional(),
        }
    ).named(renames["HousekeepingIn"])
    types["HousekeepingOut"] = t.struct(
        {
            "housekeepingAvailableException": t.string().optional(),
            "turndownService": t.boolean().optional(),
            "turndownServiceException": t.string().optional(),
            "dailyHousekeeping": t.boolean().optional(),
            "housekeepingAvailable": t.boolean().optional(),
            "dailyHousekeepingException": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HousekeepingOut"])
    types["WellnessIn"] = t.struct(
        {
            "treadmill": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "spaException": t.string().optional(),
            "saunaException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "salonException": t.string().optional(),
            "treadmillException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
            "massageException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "fitnessCenterException": t.string().optional(),
            "massage": t.boolean().optional(),
            "freeWeightsException": t.string().optional(),
            "doctorOnCallException": t.string().optional(),
            "freeWeights": t.boolean().optional(),
            "salon": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "freeFitnessCenter": t.boolean().optional(),
        }
    ).named(renames["WellnessIn"])
    types["WellnessOut"] = t.struct(
        {
            "treadmill": t.boolean().optional(),
            "sauna": t.boolean().optional(),
            "ellipticalMachine": t.boolean().optional(),
            "spa": t.boolean().optional(),
            "spaException": t.string().optional(),
            "saunaException": t.string().optional(),
            "ellipticalMachineException": t.string().optional(),
            "doctorOnCall": t.boolean().optional(),
            "freeFitnessCenterException": t.string().optional(),
            "salonException": t.string().optional(),
            "treadmillException": t.string().optional(),
            "fitnessCenter": t.boolean().optional(),
            "massageException": t.string().optional(),
            "weightMachineException": t.string().optional(),
            "fitnessCenterException": t.string().optional(),
            "massage": t.boolean().optional(),
            "freeWeightsException": t.string().optional(),
            "doctorOnCallException": t.string().optional(),
            "freeWeights": t.boolean().optional(),
            "salon": t.boolean().optional(),
            "weightMachine": t.boolean().optional(),
            "freeFitnessCenter": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WellnessOut"])
    types["IncreasedFoodSafetyIn"] = t.struct(
        {
            "disposableFlatwareException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "disposableFlatware": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
        }
    ).named(renames["IncreasedFoodSafetyIn"])
    types["IncreasedFoodSafetyOut"] = t.struct(
        {
            "disposableFlatwareException": t.string().optional(),
            "foodPreparationAndServingAdditionalSafety": t.boolean().optional(),
            "diningAreasAdditionalSanitationException": t.string().optional(),
            "individualPackagedMealsException": t.string().optional(),
            "singleUseFoodMenusException": t.string().optional(),
            "disposableFlatware": t.boolean().optional(),
            "foodPreparationAndServingAdditionalSafetyException": t.string().optional(),
            "individualPackagedMeals": t.boolean().optional(),
            "diningAreasAdditionalSanitation": t.boolean().optional(),
            "singleUseFoodMenus": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IncreasedFoodSafetyOut"])
    types["WaterConservationIn"] = t.struct(
        {
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingShowersException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingSinks": t.boolean().optional(),
        }
    ).named(renames["WaterConservationIn"])
    types["WaterConservationOut"] = t.struct(
        {
            "waterSavingToilets": t.boolean().optional(),
            "waterSavingShowers": t.boolean().optional(),
            "waterSavingToiletsException": t.string().optional(),
            "towelReuseProgramException": t.string().optional(),
            "waterSavingSinksException": t.string().optional(),
            "independentOrganizationAuditsWaterUse": t.boolean().optional(),
            "linenReuseProgram": t.boolean().optional(),
            "independentOrganizationAuditsWaterUseException": t.string().optional(),
            "waterSavingShowersException": t.string().optional(),
            "linenReuseProgramException": t.string().optional(),
            "towelReuseProgram": t.boolean().optional(),
            "waterSavingSinks": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WaterConservationOut"])
    types["GuestUnitTypeIn"] = t.struct(
        {
            "label": t.string(),
            "features": t.proxy(renames["GuestUnitFeaturesIn"]).optional(),
            "codes": t.array(t.string()),
        }
    ).named(renames["GuestUnitTypeIn"])
    types["GuestUnitTypeOut"] = t.struct(
        {
            "label": t.string(),
            "features": t.proxy(renames["GuestUnitFeaturesOut"]).optional(),
            "codes": t.array(t.string()),
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
        importer="mybusinesslodging",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
