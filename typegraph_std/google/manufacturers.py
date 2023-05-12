from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_manufacturers() -> Import:
    manufacturers = HTTPRuntime("https://manufacturers.googleapis.com/")

    renames = {
        "ErrorResponse": "_manufacturers_1_ErrorResponse",
        "ImageIn": "_manufacturers_2_ImageIn",
        "ImageOut": "_manufacturers_3_ImageOut",
        "ProductCertificationIn": "_manufacturers_4_ProductCertificationIn",
        "ProductCertificationOut": "_manufacturers_5_ProductCertificationOut",
        "CertificationIn": "_manufacturers_6_CertificationIn",
        "CertificationOut": "_manufacturers_7_CertificationOut",
        "IssueIn": "_manufacturers_8_IssueIn",
        "IssueOut": "_manufacturers_9_IssueOut",
        "EmptyIn": "_manufacturers_10_EmptyIn",
        "EmptyOut": "_manufacturers_11_EmptyOut",
        "ProductIn": "_manufacturers_12_ProductIn",
        "ProductOut": "_manufacturers_13_ProductOut",
        "FeatureDescriptionIn": "_manufacturers_14_FeatureDescriptionIn",
        "FeatureDescriptionOut": "_manufacturers_15_FeatureDescriptionOut",
        "CapacityIn": "_manufacturers_16_CapacityIn",
        "CapacityOut": "_manufacturers_17_CapacityOut",
        "ProductDetailIn": "_manufacturers_18_ProductDetailIn",
        "ProductDetailOut": "_manufacturers_19_ProductDetailOut",
        "NutritionIn": "_manufacturers_20_NutritionIn",
        "NutritionOut": "_manufacturers_21_NutritionOut",
        "VoluntaryNutritionFactIn": "_manufacturers_22_VoluntaryNutritionFactIn",
        "VoluntaryNutritionFactOut": "_manufacturers_23_VoluntaryNutritionFactOut",
        "ListProductCertificationsResponseIn": "_manufacturers_24_ListProductCertificationsResponseIn",
        "ListProductCertificationsResponseOut": "_manufacturers_25_ListProductCertificationsResponseOut",
        "ListProductsResponseIn": "_manufacturers_26_ListProductsResponseIn",
        "ListProductsResponseOut": "_manufacturers_27_ListProductsResponseOut",
        "AttributesIn": "_manufacturers_28_AttributesIn",
        "AttributesOut": "_manufacturers_29_AttributesOut",
        "GroceryIn": "_manufacturers_30_GroceryIn",
        "GroceryOut": "_manufacturers_31_GroceryOut",
        "DestinationStatusIn": "_manufacturers_32_DestinationStatusIn",
        "DestinationStatusOut": "_manufacturers_33_DestinationStatusOut",
        "FloatUnitIn": "_manufacturers_34_FloatUnitIn",
        "FloatUnitOut": "_manufacturers_35_FloatUnitOut",
        "CountIn": "_manufacturers_36_CountIn",
        "CountOut": "_manufacturers_37_CountOut",
        "PriceIn": "_manufacturers_38_PriceIn",
        "PriceOut": "_manufacturers_39_PriceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ImageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "imageUrl": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "imageUrl": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["ProductCertificationIn"] = t.struct(
        {
            "title": t.string(),
            "countryCode": t.array(t.string()).optional(),
            "productCode": t.array(t.string()).optional(),
            "name": t.string(),
            "brand": t.string(),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "certification": t.array(t.proxy(renames["CertificationIn"])),
        }
    ).named(renames["ProductCertificationIn"])
    types["ProductCertificationOut"] = t.struct(
        {
            "title": t.string(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "countryCode": t.array(t.string()).optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "productCode": t.array(t.string()).optional(),
            "name": t.string(),
            "brand": t.string(),
            "mpn": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "certification": t.array(t.proxy(renames["CertificationOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductCertificationOut"])
    types["CertificationIn"] = t.struct(
        {
            "logo": t.string().optional(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "authority": t.string(),
            "value": t.string(),
            "link": t.string().optional(),
        }
    ).named(renames["CertificationIn"])
    types["CertificationOut"] = t.struct(
        {
            "logo": t.string().optional(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "authority": t.string(),
            "value": t.string(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificationOut"])
    types["IssueIn"] = t.struct(
        {
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "attribute": t.string().optional(),
            "timestamp": t.string().optional(),
            "title": t.string().optional(),
            "resolution": t.string().optional(),
            "type": t.string().optional(),
            "destination": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "attribute": t.string().optional(),
            "timestamp": t.string().optional(),
            "title": t.string().optional(),
            "resolution": t.string().optional(),
            "type": t.string().optional(),
            "destination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ProductIn"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusIn"])
            ).optional(),
            "name": t.string().optional(),
            "productId": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "parent": t.string().optional(),
            "targetCountry": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "name": t.string().optional(),
            "productId": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "parent": t.string().optional(),
            "targetCountry": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["ProductDetailIn"] = t.struct(
        {
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
            "attributeValue": t.string().optional(),
        }
    ).named(renames["ProductDetailIn"])
    types["ProductDetailOut"] = t.struct(
        {
            "sectionName": t.string().optional(),
            "attributeName": t.string().optional(),
            "attributeValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductDetailOut"])
    types["NutritionIn"] = t.struct(
        {
            "sodiumDailyPercentage": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "polyols": t.proxy(renames["FloatUnitIn"]).optional(),
            "iron": t.proxy(renames["FloatUnitIn"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitIn"]).optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "potassium": t.proxy(renames["FloatUnitIn"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitIn"]).optional(),
            "energy": t.proxy(renames["FloatUnitIn"]).optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitIn"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitIn"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactIn"])
            ).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "vitaminD": t.proxy(renames["FloatUnitIn"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "servingsPerContainer": t.string().optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitIn"]).optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "starch": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "totalSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "proteinDailyPercentage": t.number().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "transFatDailyPercentage": t.number().optional(),
            "calciumDailyPercentage": t.number().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "protein": t.proxy(renames["FloatUnitIn"]).optional(),
            "folateDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "totalFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "sodium": t.proxy(renames["FloatUnitIn"]).optional(),
            "addedSugars": t.proxy(renames["FloatUnitIn"]).optional(),
        }
    ).named(renames["NutritionIn"])
    types["NutritionOut"] = t.struct(
        {
            "sodiumDailyPercentage": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "polyols": t.proxy(renames["FloatUnitOut"]).optional(),
            "iron": t.proxy(renames["FloatUnitOut"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "calcium": t.proxy(renames["FloatUnitOut"]).optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "potassium": t.proxy(renames["FloatUnitOut"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitOut"]).optional(),
            "energy": t.proxy(renames["FloatUnitOut"]).optional(),
            "potassiumDailyPercentage": t.number().optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitOut"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitOut"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactOut"])
            ).optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "vitaminD": t.proxy(renames["FloatUnitOut"]).optional(),
            "ironDailyPercentage": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "servingsPerContainer": t.string().optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitOut"]).optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "starch": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "totalSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "proteinDailyPercentage": t.number().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "transFatDailyPercentage": t.number().optional(),
            "calciumDailyPercentage": t.number().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "protein": t.proxy(renames["FloatUnitOut"]).optional(),
            "folateDailyPercentage": t.number().optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "totalFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "sodium": t.proxy(renames["FloatUnitOut"]).optional(),
            "addedSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NutritionOut"])
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
    types["AttributesIn"] = t.struct(
        {
            "gtin": t.array(t.string()).optional(),
            "scent": t.string().optional(),
            "releaseDate": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailIn"])).optional(),
            "sizeType": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "mpn": t.string().optional(),
            "description": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
            "richProductContent": t.array(t.string()).optional(),
            "targetClientId": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionIn"]).optional(),
            "material": t.string().optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
            "productName": t.string().optional(),
            "theme": t.string().optional(),
            "grocery": t.proxy(renames["GroceryIn"]).optional(),
            "productPageUrl": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "flavor": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "pattern": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionIn"])
            ).optional(),
            "gender": t.string().optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
            "format": t.string().optional(),
            "size": t.string().optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "imageLink": t.proxy(renames["ImageIn"]).optional(),
            "videoLink": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "productLine": t.string().optional(),
            "count": t.proxy(renames["CountIn"]).optional(),
            "brand": t.string().optional(),
            "color": t.string().optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "gtin": t.array(t.string()).optional(),
            "scent": t.string().optional(),
            "releaseDate": t.string().optional(),
            "itemGroupId": t.string().optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailOut"])).optional(),
            "sizeType": t.array(t.string()).optional(),
            "title": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "mpn": t.string().optional(),
            "description": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
            "richProductContent": t.array(t.string()).optional(),
            "targetClientId": t.string().optional(),
            "nutrition": t.proxy(renames["NutritionOut"]).optional(),
            "material": t.string().optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceOut"]).optional(),
            "productName": t.string().optional(),
            "theme": t.string().optional(),
            "grocery": t.proxy(renames["GroceryOut"]).optional(),
            "productPageUrl": t.string().optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "flavor": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "pattern": t.string().optional(),
            "sizeSystem": t.string().optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionOut"])
            ).optional(),
            "gender": t.string().optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageOut"])).optional(),
            "format": t.string().optional(),
            "size": t.string().optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "imageLink": t.proxy(renames["ImageOut"]).optional(),
            "videoLink": t.array(t.string()).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "productLine": t.string().optional(),
            "count": t.proxy(renames["CountOut"]).optional(),
            "brand": t.string().optional(),
            "color": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["GroceryIn"] = t.struct(
        {
            "directions": t.string().optional(),
            "alcoholByVolume": t.number().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
            "allergens": t.string().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
            "activeIngredients": t.string().optional(),
        }
    ).named(renames["GroceryIn"])
    types["GroceryOut"] = t.struct(
        {
            "directions": t.string().optional(),
            "alcoholByVolume": t.number().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
            "allergens": t.string().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "storageInstructions": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroceryOut"])
    types["DestinationStatusIn"] = t.struct(
        {"status": t.string().optional(), "destination": t.string().optional()}
    ).named(renames["DestinationStatusIn"])
    types["DestinationStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "destination": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestinationStatusOut"])
    types["FloatUnitIn"] = t.struct(
        {"unit": t.string().optional(), "amount": t.number().optional()}
    ).named(renames["FloatUnitIn"])
    types["FloatUnitOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "amount": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FloatUnitOut"])
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

    functions = {}
    functions["accountsLanguagesProductCertificationsList"] = manufacturers.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsPatch"] = manufacturers.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsGet"] = manufacturers.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsDelete"] = manufacturers.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsList"] = manufacturers.get(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "include": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsUpdate"] = manufacturers.get(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "include": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsDelete"] = manufacturers.get(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "include": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsProductsGet"] = manufacturers.get(
        "v1/{parent}/products/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "include": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="manufacturers",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
