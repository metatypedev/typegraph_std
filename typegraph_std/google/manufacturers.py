from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_manufacturers():
    manufacturers = HTTPRuntime("https://manufacturers.googleapis.com/")

    renames = {
        "ErrorResponse": "_manufacturers_1_ErrorResponse",
        "ProductIn": "_manufacturers_2_ProductIn",
        "ProductOut": "_manufacturers_3_ProductOut",
        "ListProductCertificationsResponseIn": "_manufacturers_4_ListProductCertificationsResponseIn",
        "ListProductCertificationsResponseOut": "_manufacturers_5_ListProductCertificationsResponseOut",
        "EmptyIn": "_manufacturers_6_EmptyIn",
        "EmptyOut": "_manufacturers_7_EmptyOut",
        "PriceIn": "_manufacturers_8_PriceIn",
        "PriceOut": "_manufacturers_9_PriceOut",
        "GroceryIn": "_manufacturers_10_GroceryIn",
        "GroceryOut": "_manufacturers_11_GroceryOut",
        "ImageIn": "_manufacturers_12_ImageIn",
        "ImageOut": "_manufacturers_13_ImageOut",
        "FeatureDescriptionIn": "_manufacturers_14_FeatureDescriptionIn",
        "FeatureDescriptionOut": "_manufacturers_15_FeatureDescriptionOut",
        "ProductDetailIn": "_manufacturers_16_ProductDetailIn",
        "ProductDetailOut": "_manufacturers_17_ProductDetailOut",
        "ListProductsResponseIn": "_manufacturers_18_ListProductsResponseIn",
        "ListProductsResponseOut": "_manufacturers_19_ListProductsResponseOut",
        "CertificationIn": "_manufacturers_20_CertificationIn",
        "CertificationOut": "_manufacturers_21_CertificationOut",
        "FloatUnitIn": "_manufacturers_22_FloatUnitIn",
        "FloatUnitOut": "_manufacturers_23_FloatUnitOut",
        "IssueIn": "_manufacturers_24_IssueIn",
        "IssueOut": "_manufacturers_25_IssueOut",
        "CountIn": "_manufacturers_26_CountIn",
        "CountOut": "_manufacturers_27_CountOut",
        "AttributesIn": "_manufacturers_28_AttributesIn",
        "AttributesOut": "_manufacturers_29_AttributesOut",
        "DestinationStatusIn": "_manufacturers_30_DestinationStatusIn",
        "DestinationStatusOut": "_manufacturers_31_DestinationStatusOut",
        "CapacityIn": "_manufacturers_32_CapacityIn",
        "CapacityOut": "_manufacturers_33_CapacityOut",
        "ProductCertificationIn": "_manufacturers_34_ProductCertificationIn",
        "ProductCertificationOut": "_manufacturers_35_ProductCertificationOut",
        "VoluntaryNutritionFactIn": "_manufacturers_36_VoluntaryNutritionFactIn",
        "VoluntaryNutritionFactOut": "_manufacturers_37_VoluntaryNutritionFactOut",
        "NutritionIn": "_manufacturers_38_NutritionIn",
        "NutritionOut": "_manufacturers_39_NutritionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ProductIn"] = t.struct(
        {
            "targetCountry": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "productId": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
            "parent": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "targetCountry": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "productId": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "parent": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["PriceIn"] = t.struct(
        {"amount": t.string().optional(), "currency": t.string().optional()}
    ).named(renames["PriceIn"])
    types["PriceOut"] = t.struct(
        {
            "amount": t.string().optional(),
            "currency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PriceOut"])
    types["GroceryIn"] = t.struct(
        {
            "alcoholByVolume": t.number().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
            "allergens": t.string().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "directions": t.string().optional(),
        }
    ).named(renames["GroceryIn"])
    types["GroceryOut"] = t.struct(
        {
            "alcoholByVolume": t.number().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
            "allergens": t.string().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "directions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroceryOut"])
    types["ImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "status": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "status": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["FeatureDescriptionIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "text": t.string().optional(),
            "headline": t.string().optional(),
        }
    ).named(renames["FeatureDescriptionIn"])
    types["FeatureDescriptionOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "text": t.string().optional(),
            "headline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureDescriptionOut"])
    types["ProductDetailIn"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "sectionName": t.string().optional(),
            "attributeValue": t.string().optional(),
        }
    ).named(renames["ProductDetailIn"])
    types["ProductDetailOut"] = t.struct(
        {
            "attributeName": t.string().optional(),
            "sectionName": t.string().optional(),
            "attributeValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDetailOut"])
    types["ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductIn"])).optional(),
        }
    ).named(renames["ListProductsResponseIn"])
    types["ListProductsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(t.proxy(renames["ProductOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProductsResponseOut"])
    types["CertificationIn"] = t.struct(
        {
            "value": t.string(),
            "link": t.string().optional(),
            "logo": t.string().optional(),
            "authority": t.string(),
            "validUntil": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["CertificationIn"])
    types["CertificationOut"] = t.struct(
        {
            "value": t.string(),
            "link": t.string().optional(),
            "logo": t.string().optional(),
            "authority": t.string(),
            "validUntil": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificationOut"])
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
    types["IssueIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "destination": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "attribute": t.string().optional(),
            "type": t.string().optional(),
            "resolution": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "destination": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "attribute": t.string().optional(),
            "type": t.string().optional(),
            "resolution": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
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
            "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
            "productHighlight": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "brand": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionIn"]).optional(),
            "scent": t.string().optional(),
            "size": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "imageLink": t.proxy(renames["ImageIn"]).optional(),
            "mpn": t.string().optional(),
            "grocery": t.proxy(renames["GroceryIn"]).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "gender": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "virtualModelLink": t.string().optional(),
            "releaseDate": t.string().optional(),
            "title": t.string().optional(),
            "count": t.proxy(renames["CountIn"]).optional(),
            "flavor": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "theme": t.string().optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "targetClientId": t.string().optional(),
            "sizeType": t.array(t.string()).optional(),
            "material": t.string().optional(),
            "productName": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "format": t.string().optional(),
            "color": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionIn"])
            ).optional(),
            "gtin": t.array(t.string()).optional(),
            "pattern": t.string().optional(),
            "productLine": t.string().optional(),
            "productPageUrl": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailIn"])).optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "additionalImageLink": t.array(t.proxy(renames["ImageOut"])).optional(),
            "productHighlight": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "brand": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionOut"]).optional(),
            "scent": t.string().optional(),
            "size": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "imageLink": t.proxy(renames["ImageOut"]).optional(),
            "mpn": t.string().optional(),
            "grocery": t.proxy(renames["GroceryOut"]).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceOut"]).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "gender": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "virtualModelLink": t.string().optional(),
            "releaseDate": t.string().optional(),
            "title": t.string().optional(),
            "count": t.proxy(renames["CountOut"]).optional(),
            "flavor": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "theme": t.string().optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "targetClientId": t.string().optional(),
            "sizeType": t.array(t.string()).optional(),
            "material": t.string().optional(),
            "productName": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "format": t.string().optional(),
            "color": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionOut"])
            ).optional(),
            "gtin": t.array(t.string()).optional(),
            "pattern": t.string().optional(),
            "productLine": t.string().optional(),
            "productPageUrl": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
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
    types["CapacityIn"] = t.struct(
        {"value": t.string().optional(), "unit": t.string().optional()}
    ).named(renames["CapacityIn"])
    types["CapacityOut"] = t.struct(
        {
            "value": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityOut"])
    types["ProductCertificationIn"] = t.struct(
        {
            "productCode": t.array(t.string()).optional(),
            "name": t.string(),
            "title": t.string(),
            "brand": t.string(),
            "countryCode": t.array(t.string()).optional(),
            "certification": t.array(t.proxy(renames["CertificationIn"])),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
        }
    ).named(renames["ProductCertificationIn"])
    types["ProductCertificationOut"] = t.struct(
        {
            "productCode": t.array(t.string()).optional(),
            "name": t.string(),
            "title": t.string(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "brand": t.string(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "countryCode": t.array(t.string()).optional(),
            "certification": t.array(t.proxy(renames["CertificationOut"])),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductCertificationOut"])
    types["VoluntaryNutritionFactIn"] = t.struct(
        {
            "value": t.proxy(renames["FloatUnitIn"]).optional(),
            "name": t.string().optional(),
            "dailyPercentage": t.number().optional(),
        }
    ).named(renames["VoluntaryNutritionFactIn"])
    types["VoluntaryNutritionFactOut"] = t.struct(
        {
            "value": t.proxy(renames["FloatUnitOut"]).optional(),
            "name": t.string().optional(),
            "dailyPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoluntaryNutritionFactOut"])
    types["NutritionIn"] = t.struct(
        {
            "proteinDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "polyols": t.proxy(renames["FloatUnitIn"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "iron": t.proxy(renames["FloatUnitIn"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "energy": t.proxy(renames["FloatUnitIn"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "protein": t.proxy(renames["FloatUnitIn"]).optional(),
            "potassium": t.proxy(renames["FloatUnitIn"]).optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "addedSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "totalFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitIn"]).optional(),
            "saturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactIn"])
            ).optional(),
            "folateDailyPercentage": t.number().optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitIn"]).optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "calciumDailyPercentage": t.number().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "sodium": t.proxy(renames["FloatUnitIn"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "servingSizeDescription": t.string().optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitIn"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitIn"]).optional(),
            "starch": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingsPerContainer": t.string().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
        }
    ).named(renames["NutritionIn"])
    types["NutritionOut"] = t.struct(
        {
            "proteinDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "polyols": t.proxy(renames["FloatUnitOut"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "iron": t.proxy(renames["FloatUnitOut"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "energy": t.proxy(renames["FloatUnitOut"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "protein": t.proxy(renames["FloatUnitOut"]).optional(),
            "potassium": t.proxy(renames["FloatUnitOut"]).optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "addedSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "totalFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitOut"]).optional(),
            "saturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactOut"])
            ).optional(),
            "folateDailyPercentage": t.number().optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitOut"]).optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "calciumDailyPercentage": t.number().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "sodium": t.proxy(renames["FloatUnitOut"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "servingSizeDescription": t.string().optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitOut"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitOut"]).optional(),
            "starch": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingsPerContainer": t.string().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NutritionOut"])

    functions = {}
    functions["accountsProductsUpdate"] = manufacturers.delete(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsList"] = manufacturers.delete(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsGet"] = manufacturers.delete(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsDelete"] = manufacturers.delete(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsList"] = manufacturers.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "productCode": t.array(t.string()).optional(),
                "title": t.string(),
                "brand": t.string(),
                "countryCode": t.array(t.string()).optional(),
                "certification": t.array(t.proxy(renames["CertificationIn"])),
                "mpn": t.array(t.string()).optional(),
                "productType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductCertificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsGet"] = manufacturers.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "productCode": t.array(t.string()).optional(),
                "title": t.string(),
                "brand": t.string(),
                "countryCode": t.array(t.string()).optional(),
                "certification": t.array(t.proxy(renames["CertificationIn"])),
                "mpn": t.array(t.string()).optional(),
                "productType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductCertificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsDelete"] = manufacturers.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "productCode": t.array(t.string()).optional(),
                "title": t.string(),
                "brand": t.string(),
                "countryCode": t.array(t.string()).optional(),
                "certification": t.array(t.proxy(renames["CertificationIn"])),
                "mpn": t.array(t.string()).optional(),
                "productType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductCertificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsPatch"] = manufacturers.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string(),
                "productCode": t.array(t.string()).optional(),
                "title": t.string(),
                "brand": t.string(),
                "countryCode": t.array(t.string()).optional(),
                "certification": t.array(t.proxy(renames["CertificationIn"])),
                "mpn": t.array(t.string()).optional(),
                "productType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductCertificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="manufacturers",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
