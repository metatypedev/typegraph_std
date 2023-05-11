from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_manufacturers() -> Import:
    manufacturers = HTTPRuntime("https://manufacturers.googleapis.com/")

    renames = {
        "ErrorResponse": "_manufacturers_1_ErrorResponse",
        "FloatUnitIn": "_manufacturers_2_FloatUnitIn",
        "FloatUnitOut": "_manufacturers_3_FloatUnitOut",
        "NutritionIn": "_manufacturers_4_NutritionIn",
        "NutritionOut": "_manufacturers_5_NutritionOut",
        "ListProductCertificationsResponseIn": "_manufacturers_6_ListProductCertificationsResponseIn",
        "ListProductCertificationsResponseOut": "_manufacturers_7_ListProductCertificationsResponseOut",
        "EmptyIn": "_manufacturers_8_EmptyIn",
        "EmptyOut": "_manufacturers_9_EmptyOut",
        "IssueIn": "_manufacturers_10_IssueIn",
        "IssueOut": "_manufacturers_11_IssueOut",
        "FeatureDescriptionIn": "_manufacturers_12_FeatureDescriptionIn",
        "FeatureDescriptionOut": "_manufacturers_13_FeatureDescriptionOut",
        "CertificationIn": "_manufacturers_14_CertificationIn",
        "CertificationOut": "_manufacturers_15_CertificationOut",
        "ImageIn": "_manufacturers_16_ImageIn",
        "ImageOut": "_manufacturers_17_ImageOut",
        "ProductDetailIn": "_manufacturers_18_ProductDetailIn",
        "ProductDetailOut": "_manufacturers_19_ProductDetailOut",
        "CapacityIn": "_manufacturers_20_CapacityIn",
        "CapacityOut": "_manufacturers_21_CapacityOut",
        "GroceryIn": "_manufacturers_22_GroceryIn",
        "GroceryOut": "_manufacturers_23_GroceryOut",
        "ProductIn": "_manufacturers_24_ProductIn",
        "ProductOut": "_manufacturers_25_ProductOut",
        "DestinationStatusIn": "_manufacturers_26_DestinationStatusIn",
        "DestinationStatusOut": "_manufacturers_27_DestinationStatusOut",
        "VoluntaryNutritionFactIn": "_manufacturers_28_VoluntaryNutritionFactIn",
        "VoluntaryNutritionFactOut": "_manufacturers_29_VoluntaryNutritionFactOut",
        "ProductCertificationIn": "_manufacturers_30_ProductCertificationIn",
        "ProductCertificationOut": "_manufacturers_31_ProductCertificationOut",
        "ListProductsResponseIn": "_manufacturers_32_ListProductsResponseIn",
        "ListProductsResponseOut": "_manufacturers_33_ListProductsResponseOut",
        "PriceIn": "_manufacturers_34_PriceIn",
        "PriceOut": "_manufacturers_35_PriceOut",
        "CountIn": "_manufacturers_36_CountIn",
        "CountOut": "_manufacturers_37_CountOut",
        "AttributesIn": "_manufacturers_38_AttributesIn",
        "AttributesOut": "_manufacturers_39_AttributesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FloatUnitIn"] = t.struct(
        {"amount": t.number().optional(), "unit": t.string().optional()}
    ).named(renames["FloatUnitIn"])
    types["FloatUnitOut"] = t.struct(
        {
            "amount": t.number().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatUnitOut"])
    types["NutritionIn"] = t.struct(
        {
            "monounsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "polyols": t.proxy(renames["FloatUnitIn"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "iron": t.proxy(renames["FloatUnitIn"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "sodium": t.proxy(renames["FloatUnitIn"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitIn"]).optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitIn"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactIn"])
            ).optional(),
            "totalFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "energyFromFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "protein": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingsPerContainer": t.string().optional(),
            "potassium": t.proxy(renames["FloatUnitIn"]).optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitIn"]).optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitIn"]).optional(),
            "addedSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "proteinDailyPercentage": t.number().optional(),
            "energy": t.proxy(renames["FloatUnitIn"]).optional(),
            "folateDailyPercentage": t.number().optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "calciumDailyPercentage": t.number().optional(),
            "totalSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "folateMcgDfe": t.number().optional(),
            "starch": t.proxy(renames["FloatUnitIn"]).optional(),
        }
    ).named(renames["NutritionIn"])
    types["NutritionOut"] = t.struct(
        {
            "monounsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "polyols": t.proxy(renames["FloatUnitOut"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "iron": t.proxy(renames["FloatUnitOut"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "sodium": t.proxy(renames["FloatUnitOut"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitOut"]).optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitOut"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactOut"])
            ).optional(),
            "totalFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "energyFromFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "protein": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingsPerContainer": t.string().optional(),
            "potassium": t.proxy(renames["FloatUnitOut"]).optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitOut"]).optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitOut"]).optional(),
            "addedSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "proteinDailyPercentage": t.number().optional(),
            "energy": t.proxy(renames["FloatUnitOut"]).optional(),
            "folateDailyPercentage": t.number().optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "calciumDailyPercentage": t.number().optional(),
            "totalSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "folateMcgDfe": t.number().optional(),
            "starch": t.proxy(renames["FloatUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NutritionOut"])
    types["ListProductCertificationsResponseIn"] = t.struct(
        {
            "productCertifications": t.array(
                t.proxy(renames["ProductCertificationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductCertificationsResponseIn"])
    types["ListProductCertificationsResponseOut"] = t.struct(
        {
            "productCertifications": t.array(
                t.proxy(renames["ProductCertificationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductCertificationsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["IssueIn"] = t.struct(
        {
            "destination": t.string().optional(),
            "type": t.string().optional(),
            "timestamp": t.string().optional(),
            "attribute": t.string().optional(),
            "title": t.string().optional(),
            "resolution": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "destination": t.string().optional(),
            "type": t.string().optional(),
            "timestamp": t.string().optional(),
            "attribute": t.string().optional(),
            "title": t.string().optional(),
            "resolution": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["FeatureDescriptionIn"] = t.struct(
        {
            "text": t.string().optional(),
            "headline": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["FeatureDescriptionIn"])
    types["FeatureDescriptionOut"] = t.struct(
        {
            "text": t.string().optional(),
            "headline": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureDescriptionOut"])
    types["CertificationIn"] = t.struct(
        {
            "authority": t.string(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "logo": t.string().optional(),
            "value": t.string(),
            "link": t.string().optional(),
        }
    ).named(renames["CertificationIn"])
    types["CertificationOut"] = t.struct(
        {
            "authority": t.string(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "logo": t.string().optional(),
            "value": t.string(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificationOut"])
    types["ImageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "status": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "status": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["ProductDetailIn"] = t.struct(
        {
            "attributeValue": t.string().optional(),
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
        }
    ).named(renames["ProductDetailIn"])
    types["ProductDetailOut"] = t.struct(
        {
            "attributeValue": t.string().optional(),
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDetailOut"])
    types["CapacityIn"] = t.struct(
        {"unit": t.string().optional(), "value": t.string().optional()}
    ).named(renames["CapacityIn"])
    types["CapacityOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityOut"])
    types["GroceryIn"] = t.struct(
        {
            "alcoholByVolume": t.number().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "allergens": t.string().optional(),
            "indications": t.string().optional(),
            "directions": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "ingredients": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
        }
    ).named(renames["GroceryIn"])
    types["GroceryOut"] = t.struct(
        {
            "alcoholByVolume": t.number().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "allergens": t.string().optional(),
            "indications": t.string().optional(),
            "directions": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "ingredients": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroceryOut"])
    types["ProductIn"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusIn"])
            ).optional(),
            "name": t.string().optional(),
            "productId": t.string().optional(),
            "targetCountry": t.string().optional(),
            "parent": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
            "contentLanguage": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "name": t.string().optional(),
            "productId": t.string().optional(),
            "targetCountry": t.string().optional(),
            "parent": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "contentLanguage": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["DestinationStatusIn"] = t.struct(
        {"destination": t.string().optional(), "status": t.string().optional()}
    ).named(renames["DestinationStatusIn"])
    types["DestinationStatusOut"] = t.struct(
        {
            "destination": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationStatusOut"])
    types["VoluntaryNutritionFactIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dailyPercentage": t.number().optional(),
            "value": t.proxy(renames["FloatUnitIn"]).optional(),
        }
    ).named(renames["VoluntaryNutritionFactIn"])
    types["VoluntaryNutritionFactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dailyPercentage": t.number().optional(),
            "value": t.proxy(renames["FloatUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoluntaryNutritionFactOut"])
    types["ProductCertificationIn"] = t.struct(
        {
            "productCode": t.array(t.string()).optional(),
            "name": t.string(),
            "title": t.string(),
            "certification": t.array(t.proxy(renames["CertificationIn"])),
            "countryCode": t.array(t.string()).optional(),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "brand": t.string(),
        }
    ).named(renames["ProductCertificationIn"])
    types["ProductCertificationOut"] = t.struct(
        {
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "productCode": t.array(t.string()).optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "name": t.string(),
            "title": t.string(),
            "certification": t.array(t.proxy(renames["CertificationOut"])),
            "countryCode": t.array(t.string()).optional(),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "brand": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductCertificationOut"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
    types["PriceIn"] = t.struct(
        {"currency": t.string().optional(), "amount": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "currency": t.string().optional(),
            "amount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["CountIn"] = t.struct(
        {"unit": t.string().optional(), "value": t.string().optional()}
    ).named(renames["CountIn"])
    types["CountOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["AttributesIn"] = t.struct(
        {
            "releaseDate": t.string().optional(),
            "grocery": t.proxy(renames["GroceryIn"]).optional(),
            "productPageUrl": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionIn"]).optional(),
            "sizeType": t.array(t.string()).optional(),
            "includedDestination": t.array(t.string()).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
            "productType": t.array(t.string()).optional(),
            "theme": t.string().optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionIn"])
            ).optional(),
            "sizeSystem": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
            "scent": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "ageGroup": t.string().optional(),
            "imageLink": t.proxy(renames["ImageIn"]).optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailIn"])).optional(),
            "targetClientId": t.string().optional(),
            "productLine": t.string().optional(),
            "format": t.string().optional(),
            "material": t.string().optional(),
            "description": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "mpn": t.string().optional(),
            "gender": t.string().optional(),
            "count": t.proxy(renames["CountIn"]).optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "title": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "brand": t.string().optional(),
            "productName": t.string().optional(),
            "flavor": t.string().optional(),
            "pattern": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
            "size": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "releaseDate": t.string().optional(),
            "grocery": t.proxy(renames["GroceryOut"]).optional(),
            "productPageUrl": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionOut"]).optional(),
            "sizeType": t.array(t.string()).optional(),
            "includedDestination": t.array(t.string()).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceOut"]).optional(),
            "productType": t.array(t.string()).optional(),
            "theme": t.string().optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionOut"])
            ).optional(),
            "sizeSystem": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageOut"])).optional(),
            "scent": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "ageGroup": t.string().optional(),
            "imageLink": t.proxy(renames["ImageOut"]).optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailOut"])).optional(),
            "targetClientId": t.string().optional(),
            "productLine": t.string().optional(),
            "format": t.string().optional(),
            "material": t.string().optional(),
            "description": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "mpn": t.string().optional(),
            "gender": t.string().optional(),
            "count": t.proxy(renames["CountOut"]).optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "title": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "brand": t.string().optional(),
            "productName": t.string().optional(),
            "flavor": t.string().optional(),
            "pattern": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
            "size": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])

    functions = {}
    functions["accountsProductsList"] = manufacturers.put(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "releaseDate": t.string().optional(),
                "grocery": t.proxy(renames["GroceryIn"]).optional(),
                "productPageUrl": t.string().optional(),
                "nutrition": t.proxy(renames["NutritionIn"]).optional(),
                "sizeType": t.array(t.string()).optional(),
                "includedDestination": t.array(t.string()).optional(),
                "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "theme": t.string().optional(),
                "featureDescription": t.array(
                    t.proxy(renames["FeatureDescriptionIn"])
                ).optional(),
                "sizeSystem": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
                "scent": t.string().optional(),
                "videoLink": t.array(t.string()).optional(),
                "color": t.string().optional(),
                "ageGroup": t.string().optional(),
                "imageLink": t.proxy(renames["ImageIn"]).optional(),
                "productDetail": t.array(
                    t.proxy(renames["ProductDetailIn"])
                ).optional(),
                "targetClientId": t.string().optional(),
                "productLine": t.string().optional(),
                "format": t.string().optional(),
                "material": t.string().optional(),
                "description": t.string().optional(),
                "excludedDestination": t.array(t.string()).optional(),
                "itemGroupId": t.string().optional(),
                "mpn": t.string().optional(),
                "gender": t.string().optional(),
                "count": t.proxy(renames["CountIn"]).optional(),
                "capacity": t.proxy(renames["CapacityIn"]).optional(),
                "title": t.string().optional(),
                "gtin": t.array(t.string()).optional(),
                "brand": t.string().optional(),
                "productName": t.string().optional(),
                "flavor": t.string().optional(),
                "pattern": t.string().optional(),
                "productHighlight": t.array(t.string()).optional(),
                "size": t.string().optional(),
                "richProductContent": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsGet"] = manufacturers.put(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "releaseDate": t.string().optional(),
                "grocery": t.proxy(renames["GroceryIn"]).optional(),
                "productPageUrl": t.string().optional(),
                "nutrition": t.proxy(renames["NutritionIn"]).optional(),
                "sizeType": t.array(t.string()).optional(),
                "includedDestination": t.array(t.string()).optional(),
                "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "theme": t.string().optional(),
                "featureDescription": t.array(
                    t.proxy(renames["FeatureDescriptionIn"])
                ).optional(),
                "sizeSystem": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
                "scent": t.string().optional(),
                "videoLink": t.array(t.string()).optional(),
                "color": t.string().optional(),
                "ageGroup": t.string().optional(),
                "imageLink": t.proxy(renames["ImageIn"]).optional(),
                "productDetail": t.array(
                    t.proxy(renames["ProductDetailIn"])
                ).optional(),
                "targetClientId": t.string().optional(),
                "productLine": t.string().optional(),
                "format": t.string().optional(),
                "material": t.string().optional(),
                "description": t.string().optional(),
                "excludedDestination": t.array(t.string()).optional(),
                "itemGroupId": t.string().optional(),
                "mpn": t.string().optional(),
                "gender": t.string().optional(),
                "count": t.proxy(renames["CountIn"]).optional(),
                "capacity": t.proxy(renames["CapacityIn"]).optional(),
                "title": t.string().optional(),
                "gtin": t.array(t.string()).optional(),
                "brand": t.string().optional(),
                "productName": t.string().optional(),
                "flavor": t.string().optional(),
                "pattern": t.string().optional(),
                "productHighlight": t.array(t.string()).optional(),
                "size": t.string().optional(),
                "richProductContent": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsDelete"] = manufacturers.put(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "releaseDate": t.string().optional(),
                "grocery": t.proxy(renames["GroceryIn"]).optional(),
                "productPageUrl": t.string().optional(),
                "nutrition": t.proxy(renames["NutritionIn"]).optional(),
                "sizeType": t.array(t.string()).optional(),
                "includedDestination": t.array(t.string()).optional(),
                "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "theme": t.string().optional(),
                "featureDescription": t.array(
                    t.proxy(renames["FeatureDescriptionIn"])
                ).optional(),
                "sizeSystem": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
                "scent": t.string().optional(),
                "videoLink": t.array(t.string()).optional(),
                "color": t.string().optional(),
                "ageGroup": t.string().optional(),
                "imageLink": t.proxy(renames["ImageIn"]).optional(),
                "productDetail": t.array(
                    t.proxy(renames["ProductDetailIn"])
                ).optional(),
                "targetClientId": t.string().optional(),
                "productLine": t.string().optional(),
                "format": t.string().optional(),
                "material": t.string().optional(),
                "description": t.string().optional(),
                "excludedDestination": t.array(t.string()).optional(),
                "itemGroupId": t.string().optional(),
                "mpn": t.string().optional(),
                "gender": t.string().optional(),
                "count": t.proxy(renames["CountIn"]).optional(),
                "capacity": t.proxy(renames["CapacityIn"]).optional(),
                "title": t.string().optional(),
                "gtin": t.array(t.string()).optional(),
                "brand": t.string().optional(),
                "productName": t.string().optional(),
                "flavor": t.string().optional(),
                "pattern": t.string().optional(),
                "productHighlight": t.array(t.string()).optional(),
                "size": t.string().optional(),
                "richProductContent": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsUpdate"] = manufacturers.put(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "releaseDate": t.string().optional(),
                "grocery": t.proxy(renames["GroceryIn"]).optional(),
                "productPageUrl": t.string().optional(),
                "nutrition": t.proxy(renames["NutritionIn"]).optional(),
                "sizeType": t.array(t.string()).optional(),
                "includedDestination": t.array(t.string()).optional(),
                "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
                "productType": t.array(t.string()).optional(),
                "theme": t.string().optional(),
                "featureDescription": t.array(
                    t.proxy(renames["FeatureDescriptionIn"])
                ).optional(),
                "sizeSystem": t.string().optional(),
                "disclosureDate": t.string().optional(),
                "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
                "scent": t.string().optional(),
                "videoLink": t.array(t.string()).optional(),
                "color": t.string().optional(),
                "ageGroup": t.string().optional(),
                "imageLink": t.proxy(renames["ImageIn"]).optional(),
                "productDetail": t.array(
                    t.proxy(renames["ProductDetailIn"])
                ).optional(),
                "targetClientId": t.string().optional(),
                "productLine": t.string().optional(),
                "format": t.string().optional(),
                "material": t.string().optional(),
                "description": t.string().optional(),
                "excludedDestination": t.array(t.string()).optional(),
                "itemGroupId": t.string().optional(),
                "mpn": t.string().optional(),
                "gender": t.string().optional(),
                "count": t.proxy(renames["CountIn"]).optional(),
                "capacity": t.proxy(renames["CapacityIn"]).optional(),
                "title": t.string().optional(),
                "gtin": t.array(t.string()).optional(),
                "brand": t.string().optional(),
                "productName": t.string().optional(),
                "flavor": t.string().optional(),
                "pattern": t.string().optional(),
                "productHighlight": t.array(t.string()).optional(),
                "size": t.string().optional(),
                "richProductContent": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsPatch"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsDelete"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsGet"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsList"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="manufacturers", renames=renames, types=types, functions=functions
    )
