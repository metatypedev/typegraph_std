from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_manufacturers() -> Import:
    manufacturers = HTTPRuntime("https://manufacturers.googleapis.com/")

    renames = {
        "ErrorResponse": "_manufacturers_1_ErrorResponse",
        "EmptyIn": "_manufacturers_2_EmptyIn",
        "EmptyOut": "_manufacturers_3_EmptyOut",
        "ListProductsResponseIn": "_manufacturers_4_ListProductsResponseIn",
        "ListProductsResponseOut": "_manufacturers_5_ListProductsResponseOut",
        "DestinationStatusIn": "_manufacturers_6_DestinationStatusIn",
        "DestinationStatusOut": "_manufacturers_7_DestinationStatusOut",
        "ProductCertificationIn": "_manufacturers_8_ProductCertificationIn",
        "ProductCertificationOut": "_manufacturers_9_ProductCertificationOut",
        "ListProductCertificationsResponseIn": "_manufacturers_10_ListProductCertificationsResponseIn",
        "ListProductCertificationsResponseOut": "_manufacturers_11_ListProductCertificationsResponseOut",
        "ProductIn": "_manufacturers_12_ProductIn",
        "ProductOut": "_manufacturers_13_ProductOut",
        "PriceIn": "_manufacturers_14_PriceIn",
        "PriceOut": "_manufacturers_15_PriceOut",
        "ImageIn": "_manufacturers_16_ImageIn",
        "ImageOut": "_manufacturers_17_ImageOut",
        "IssueIn": "_manufacturers_18_IssueIn",
        "IssueOut": "_manufacturers_19_IssueOut",
        "CertificationIn": "_manufacturers_20_CertificationIn",
        "CertificationOut": "_manufacturers_21_CertificationOut",
        "VoluntaryNutritionFactIn": "_manufacturers_22_VoluntaryNutritionFactIn",
        "VoluntaryNutritionFactOut": "_manufacturers_23_VoluntaryNutritionFactOut",
        "CountIn": "_manufacturers_24_CountIn",
        "CountOut": "_manufacturers_25_CountOut",
        "GroceryIn": "_manufacturers_26_GroceryIn",
        "GroceryOut": "_manufacturers_27_GroceryOut",
        "ProductDetailIn": "_manufacturers_28_ProductDetailIn",
        "ProductDetailOut": "_manufacturers_29_ProductDetailOut",
        "NutritionIn": "_manufacturers_30_NutritionIn",
        "NutritionOut": "_manufacturers_31_NutritionOut",
        "FloatUnitIn": "_manufacturers_32_FloatUnitIn",
        "FloatUnitOut": "_manufacturers_33_FloatUnitOut",
        "FeatureDescriptionIn": "_manufacturers_34_FeatureDescriptionIn",
        "FeatureDescriptionOut": "_manufacturers_35_FeatureDescriptionOut",
        "CapacityIn": "_manufacturers_36_CapacityIn",
        "CapacityOut": "_manufacturers_37_CapacityOut",
        "AttributesIn": "_manufacturers_38_AttributesIn",
        "AttributesOut": "_manufacturers_39_AttributesOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ProductCertificationIn"] = t.struct(
        {
            "mpn": t.array(t.string()).optional(),
            "certification": t.array(t.proxy(renames["CertificationIn"])),
            "name": t.string(),
            "productCode": t.array(t.string()).optional(),
            "title": t.string(),
            "countryCode": t.array(t.string()).optional(),
            "brand": t.string(),
            "productType": t.array(t.string()).optional(),
        }
    ).named(renames["ProductCertificationIn"])
    types["ProductCertificationOut"] = t.struct(
        {
            "mpn": t.array(t.string()).optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "certification": t.array(t.proxy(renames["CertificationOut"])),
            "name": t.string(),
            "productCode": t.array(t.string()).optional(),
            "title": t.string(),
            "countryCode": t.array(t.string()).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "brand": t.string(),
            "productType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductCertificationOut"])
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
    types["ProductIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "targetCountry": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusIn"])
            ).optional(),
            "productId": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "targetCountry": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "destinationStatuses": t.array(
                t.proxy(renames["DestinationStatusOut"])
            ).optional(),
            "productId": t.string().optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["IssueIn"] = t.struct(
        {
            "description": t.string().optional(),
            "timestamp": t.string().optional(),
            "title": t.string().optional(),
            "destination": t.string().optional(),
            "attribute": t.string().optional(),
            "type": t.string().optional(),
            "resolution": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "description": t.string().optional(),
            "timestamp": t.string().optional(),
            "title": t.string().optional(),
            "destination": t.string().optional(),
            "attribute": t.string().optional(),
            "type": t.string().optional(),
            "resolution": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["CertificationIn"] = t.struct(
        {
            "logo": t.string().optional(),
            "link": t.string().optional(),
            "value": t.string(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "authority": t.string(),
        }
    ).named(renames["CertificationIn"])
    types["CertificationOut"] = t.struct(
        {
            "logo": t.string().optional(),
            "link": t.string().optional(),
            "value": t.string(),
            "name": t.string(),
            "validUntil": t.string().optional(),
            "authority": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificationOut"])
    types["VoluntaryNutritionFactIn"] = t.struct(
        {
            "dailyPercentage": t.number().optional(),
            "value": t.proxy(renames["FloatUnitIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VoluntaryNutritionFactIn"])
    types["VoluntaryNutritionFactOut"] = t.struct(
        {
            "dailyPercentage": t.number().optional(),
            "value": t.proxy(renames["FloatUnitOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoluntaryNutritionFactOut"])
    types["CountIn"] = t.struct(
        {"value": t.string().optional(), "unit": t.string().optional()}
    ).named(renames["CountIn"])
    types["CountOut"] = t.struct(
        {
            "value": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CountOut"])
    types["GroceryIn"] = t.struct(
        {
            "allergens": t.string().optional(),
            "alcoholByVolume": t.number().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "directions": t.string().optional(),
            "storageInstructions": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
        }
    ).named(renames["GroceryIn"])
    types["GroceryOut"] = t.struct(
        {
            "allergens": t.string().optional(),
            "alcoholByVolume": t.number().optional(),
            "indications": t.string().optional(),
            "derivedNutritionClaim": t.array(t.string()).optional(),
            "directions": t.string().optional(),
            "storageInstructions": t.string().optional(),
            "activeIngredients": t.string().optional(),
            "nutritionClaim": t.array(t.string()).optional(),
            "ingredients": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroceryOut"])
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
    types["NutritionIn"] = t.struct(
        {
            "potassiumDailyPercentage": t.number().optional(),
            "transFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "servingsPerContainer": t.string().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitIn"]).optional(),
            "polyols": t.proxy(renames["FloatUnitIn"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitIn"]).optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitIn"]).optional(),
            "proteinDailyPercentage": t.number().optional(),
            "ironDailyPercentage": t.number().optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "energy": t.proxy(renames["FloatUnitIn"]).optional(),
            "potassium": t.proxy(renames["FloatUnitIn"]).optional(),
            "iron": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitIn"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "addedSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "calciumDailyPercentage": t.number().optional(),
            "protein": t.proxy(renames["FloatUnitIn"]).optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "folateDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "totalSugars": t.proxy(renames["FloatUnitIn"]).optional(),
            "sodium": t.proxy(renames["FloatUnitIn"]).optional(),
            "calcium": t.proxy(renames["FloatUnitIn"]).optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitIn"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitIn"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactIn"])
            ).optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitIn"]).optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "starch": t.proxy(renames["FloatUnitIn"]).optional(),
        }
    ).named(renames["NutritionIn"])
    types["NutritionOut"] = t.struct(
        {
            "potassiumDailyPercentage": t.number().optional(),
            "transFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "preparedSizeDescription": t.string().optional(),
            "servingsPerContainer": t.string().optional(),
            "cholesterolDailyPercentage": t.number().optional(),
            "totalCarbohydrate": t.proxy(renames["FloatUnitOut"]).optional(),
            "polyols": t.proxy(renames["FloatUnitOut"]).optional(),
            "cholesterol": t.proxy(renames["FloatUnitOut"]).optional(),
            "folateFolicAcid": t.proxy(renames["FloatUnitOut"]).optional(),
            "proteinDailyPercentage": t.number().optional(),
            "ironDailyPercentage": t.number().optional(),
            "vitaminDDailyPercentage": t.number().optional(),
            "energy": t.proxy(renames["FloatUnitOut"]).optional(),
            "potassium": t.proxy(renames["FloatUnitOut"]).optional(),
            "iron": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingSizeMeasure": t.proxy(renames["FloatUnitOut"]).optional(),
            "transFatDailyPercentage": t.number().optional(),
            "totalFatDailyPercentage": t.number().optional(),
            "folateMcgDfe": t.number().optional(),
            "polyunsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "saturatedFatDailyPercentage": t.number().optional(),
            "sodiumDailyPercentage": t.number().optional(),
            "addedSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "calciumDailyPercentage": t.number().optional(),
            "protein": t.proxy(renames["FloatUnitOut"]).optional(),
            "dietaryFiberDailyPercentage": t.number().optional(),
            "addedSugarsDailyPercentage": t.number().optional(),
            "folateDailyPercentage": t.number().optional(),
            "totalCarbohydrateDailyPercentage": t.number().optional(),
            "energyFromFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "servingSizeDescription": t.string().optional(),
            "saturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "nutritionFactMeasure": t.string().optional(),
            "totalSugars": t.proxy(renames["FloatUnitOut"]).optional(),
            "sodium": t.proxy(renames["FloatUnitOut"]).optional(),
            "calcium": t.proxy(renames["FloatUnitOut"]).optional(),
            "dietaryFiber": t.proxy(renames["FloatUnitOut"]).optional(),
            "vitaminD": t.proxy(renames["FloatUnitOut"]).optional(),
            "voluntaryNutritionFact": t.array(
                t.proxy(renames["VoluntaryNutritionFactOut"])
            ).optional(),
            "monounsaturatedFat": t.proxy(renames["FloatUnitOut"]).optional(),
            "totalSugarsDailyPercentage": t.number().optional(),
            "starch": t.proxy(renames["FloatUnitOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NutritionOut"])
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
    types["AttributesIn"] = t.struct(
        {
            "grocery": t.proxy(renames["GroceryIn"]).optional(),
            "productName": t.string().optional(),
            "targetClientId": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "count": t.proxy(renames["CountIn"]).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceIn"]).optional(),
            "sizeType": t.array(t.string()).optional(),
            "nutrition": t.proxy(renames["NutritionIn"]).optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailIn"])).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
            "sizeSystem": t.string().optional(),
            "size": t.string().optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageIn"])).optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionIn"])
            ).optional(),
            "brand": t.string().optional(),
            "productLine": t.string().optional(),
            "scent": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "mpn": t.string().optional(),
            "gender": t.string().optional(),
            "material": t.string().optional(),
            "format": t.string().optional(),
            "releaseDate": t.string().optional(),
            "flavor": t.string().optional(),
            "imageLink": t.proxy(renames["ImageIn"]).optional(),
            "pattern": t.string().optional(),
            "description": t.string().optional(),
            "productPageUrl": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "theme": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "title": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "grocery": t.proxy(renames["GroceryOut"]).optional(),
            "productName": t.string().optional(),
            "targetClientId": t.string().optional(),
            "includedDestination": t.array(t.string()).optional(),
            "count": t.proxy(renames["CountOut"]).optional(),
            "suggestedRetailPrice": t.proxy(renames["PriceOut"]).optional(),
            "sizeType": t.array(t.string()).optional(),
            "nutrition": t.proxy(renames["NutritionOut"]).optional(),
            "excludedDestination": t.array(t.string()).optional(),
            "itemGroupId": t.string().optional(),
            "productDetail": t.array(t.proxy(renames["ProductDetailOut"])).optional(),
            "productType": t.array(t.string()).optional(),
            "ageGroup": t.string().optional(),
            "richProductContent": t.array(t.string()).optional(),
            "sizeSystem": t.string().optional(),
            "size": t.string().optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "additionalImageLink": t.array(t.proxy(renames["ImageOut"])).optional(),
            "featureDescription": t.array(
                t.proxy(renames["FeatureDescriptionOut"])
            ).optional(),
            "brand": t.string().optional(),
            "productLine": t.string().optional(),
            "scent": t.string().optional(),
            "gtin": t.array(t.string()).optional(),
            "color": t.string().optional(),
            "mpn": t.string().optional(),
            "gender": t.string().optional(),
            "material": t.string().optional(),
            "format": t.string().optional(),
            "releaseDate": t.string().optional(),
            "flavor": t.string().optional(),
            "imageLink": t.proxy(renames["ImageOut"]).optional(),
            "pattern": t.string().optional(),
            "description": t.string().optional(),
            "productPageUrl": t.string().optional(),
            "videoLink": t.array(t.string()).optional(),
            "theme": t.string().optional(),
            "disclosureDate": t.string().optional(),
            "title": t.string().optional(),
            "productHighlight": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])

    functions = {}
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
    functions["accountsLanguagesProductCertificationsDelete"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsLanguagesProductCertificationsPatch"] = manufacturers.get(
        "v1/{parent}/productCertifications",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProductCertificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="manufacturers",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
