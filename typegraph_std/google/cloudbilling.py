from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudbilling():
    cloudbilling = HTTPRuntime("https://cloudbilling.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbilling_1_ErrorResponse",
        "MoneyIn": "_cloudbilling_2_MoneyIn",
        "MoneyOut": "_cloudbilling_3_MoneyOut",
        "SkuIn": "_cloudbilling_4_SkuIn",
        "SkuOut": "_cloudbilling_5_SkuOut",
        "ListSkusResponseIn": "_cloudbilling_6_ListSkusResponseIn",
        "ListSkusResponseOut": "_cloudbilling_7_ListSkusResponseOut",
        "AuditLogConfigIn": "_cloudbilling_8_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudbilling_9_AuditLogConfigOut",
        "ServiceIn": "_cloudbilling_10_ServiceIn",
        "ServiceOut": "_cloudbilling_11_ServiceOut",
        "PricingInfoIn": "_cloudbilling_12_PricingInfoIn",
        "PricingInfoOut": "_cloudbilling_13_PricingInfoOut",
        "ExprIn": "_cloudbilling_14_ExprIn",
        "ExprOut": "_cloudbilling_15_ExprOut",
        "PricingExpressionIn": "_cloudbilling_16_PricingExpressionIn",
        "PricingExpressionOut": "_cloudbilling_17_PricingExpressionOut",
        "TestIamPermissionsResponseIn": "_cloudbilling_18_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudbilling_19_TestIamPermissionsResponseOut",
        "TestIamPermissionsRequestIn": "_cloudbilling_20_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudbilling_21_TestIamPermissionsRequestOut",
        "ListServicesResponseIn": "_cloudbilling_22_ListServicesResponseIn",
        "ListServicesResponseOut": "_cloudbilling_23_ListServicesResponseOut",
        "BindingIn": "_cloudbilling_24_BindingIn",
        "BindingOut": "_cloudbilling_25_BindingOut",
        "ListBillingAccountsResponseIn": "_cloudbilling_26_ListBillingAccountsResponseIn",
        "ListBillingAccountsResponseOut": "_cloudbilling_27_ListBillingAccountsResponseOut",
        "GeoTaxonomyIn": "_cloudbilling_28_GeoTaxonomyIn",
        "GeoTaxonomyOut": "_cloudbilling_29_GeoTaxonomyOut",
        "TierRateIn": "_cloudbilling_30_TierRateIn",
        "TierRateOut": "_cloudbilling_31_TierRateOut",
        "AggregationInfoIn": "_cloudbilling_32_AggregationInfoIn",
        "AggregationInfoOut": "_cloudbilling_33_AggregationInfoOut",
        "CategoryIn": "_cloudbilling_34_CategoryIn",
        "CategoryOut": "_cloudbilling_35_CategoryOut",
        "AuditConfigIn": "_cloudbilling_36_AuditConfigIn",
        "AuditConfigOut": "_cloudbilling_37_AuditConfigOut",
        "PolicyIn": "_cloudbilling_38_PolicyIn",
        "PolicyOut": "_cloudbilling_39_PolicyOut",
        "BillingAccountIn": "_cloudbilling_40_BillingAccountIn",
        "BillingAccountOut": "_cloudbilling_41_BillingAccountOut",
        "ListProjectBillingInfoResponseIn": "_cloudbilling_42_ListProjectBillingInfoResponseIn",
        "ListProjectBillingInfoResponseOut": "_cloudbilling_43_ListProjectBillingInfoResponseOut",
        "ProjectBillingInfoIn": "_cloudbilling_44_ProjectBillingInfoIn",
        "ProjectBillingInfoOut": "_cloudbilling_45_ProjectBillingInfoOut",
        "SetIamPolicyRequestIn": "_cloudbilling_46_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudbilling_47_SetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["SkuIn"] = t.struct(
        {
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyIn"]).optional(),
            "serviceProviderName": t.string().optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoIn"])).optional(),
            "description": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "skuId": t.string().optional(),
            "category": t.proxy(renames["CategoryIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SkuIn"])
    types["SkuOut"] = t.struct(
        {
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyOut"]).optional(),
            "serviceProviderName": t.string().optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoOut"])).optional(),
            "description": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "skuId": t.string().optional(),
            "category": t.proxy(renames["CategoryOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkuOut"])
    types["ListSkusResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "skus": t.array(t.proxy(renames["SkuIn"])).optional(),
        }
    ).named(renames["ListSkusResponseIn"])
    types["ListSkusResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "skus": t.array(t.proxy(renames["SkuOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSkusResponseOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ServiceIn"] = t.struct(
        {
            "serviceId": t.string().optional(),
            "businessEntityName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "serviceId": t.string().optional(),
            "businessEntityName": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["PricingInfoIn"] = t.struct(
        {
            "aggregationInfo": t.proxy(renames["AggregationInfoIn"]).optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionIn"]).optional(),
            "summary": t.string().optional(),
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
        }
    ).named(renames["PricingInfoIn"])
    types["PricingInfoOut"] = t.struct(
        {
            "aggregationInfo": t.proxy(renames["AggregationInfoOut"]).optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionOut"]).optional(),
            "summary": t.string().optional(),
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingInfoOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PricingExpressionIn"] = t.struct(
        {
            "usageUnitDescription": t.string().optional(),
            "usageUnit": t.string().optional(),
            "displayQuantity": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateIn"])).optional(),
            "baseUnit": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
        }
    ).named(renames["PricingExpressionIn"])
    types["PricingExpressionOut"] = t.struct(
        {
            "usageUnitDescription": t.string().optional(),
            "usageUnit": t.string().optional(),
            "displayQuantity": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateOut"])).optional(),
            "baseUnit": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingExpressionOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ListBillingAccountsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingAccounts": t.array(t.proxy(renames["BillingAccountIn"])).optional(),
        }
    ).named(renames["ListBillingAccountsResponseIn"])
    types["ListBillingAccountsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "billingAccounts": t.array(
                t.proxy(renames["BillingAccountOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBillingAccountsResponseOut"])
    types["GeoTaxonomyIn"] = t.struct(
        {"type": t.string().optional(), "regions": t.array(t.string()).optional()}
    ).named(renames["GeoTaxonomyIn"])
    types["GeoTaxonomyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "regions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoTaxonomyOut"])
    types["TierRateIn"] = t.struct(
        {
            "startUsageAmount": t.number().optional(),
            "unitPrice": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["TierRateIn"])
    types["TierRateOut"] = t.struct(
        {
            "startUsageAmount": t.number().optional(),
            "unitPrice": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierRateOut"])
    types["AggregationInfoIn"] = t.struct(
        {
            "aggregationInterval": t.string(),
            "aggregationCount": t.integer().optional(),
            "aggregationLevel": t.string(),
        }
    ).named(renames["AggregationInfoIn"])
    types["AggregationInfoOut"] = t.struct(
        {
            "aggregationInterval": t.string(),
            "aggregationCount": t.integer().optional(),
            "aggregationLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationInfoOut"])
    types["CategoryIn"] = t.struct(
        {
            "resourceFamily": t.string().optional(),
            "resourceGroup": t.string().optional(),
            "usageType": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "resourceFamily": t.string().optional(),
            "resourceGroup": t.string().optional(),
            "usageType": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BillingAccountIn"] = t.struct(
        {
            "masterBillingAccount": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["BillingAccountIn"])
    types["BillingAccountOut"] = t.struct(
        {
            "open": t.boolean().optional(),
            "masterBillingAccount": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAccountOut"])
    types["ListProjectBillingInfoResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projectBillingInfo": t.array(
                t.proxy(renames["ProjectBillingInfoIn"])
            ).optional(),
        }
    ).named(renames["ListProjectBillingInfoResponseIn"])
    types["ListProjectBillingInfoResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projectBillingInfo": t.array(
                t.proxy(renames["ProjectBillingInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProjectBillingInfoResponseOut"])
    types["ProjectBillingInfoIn"] = t.struct(
        {"billingAccountName": t.string().optional()}
    ).named(renames["ProjectBillingInfoIn"])
    types["ProjectBillingInfoOut"] = t.struct(
        {
            "billingAccountName": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectBillingInfoOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])

    functions = {}
    functions["billingAccountsSetIamPolicy"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGet"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsPatch"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetIamPolicy"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsList"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsTestIamPermissions"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsCreate"] = cloudbilling.post(
        "v1/billingAccounts",
        t.struct(
            {
                "masterBillingAccount": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsProjectsList"] = cloudbilling.get(
        "v1/{name}/projects",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProjectBillingInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = cloudbilling.get(
        "v1/services",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSkusList"] = cloudbilling.get(
        "v1/{parent}/skus",
        t.struct(
            {
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "currencyCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateBillingInfo"] = cloudbilling.get(
        "v1/{name}/billingInfo",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectBillingInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetBillingInfo"] = cloudbilling.get(
        "v1/{name}/billingInfo",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectBillingInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudbilling",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
