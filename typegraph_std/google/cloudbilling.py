from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudbilling() -> Import:
    cloudbilling = HTTPRuntime("https://cloudbilling.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbilling_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_cloudbilling_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudbilling_3_TestIamPermissionsRequestOut",
        "ListBillingAccountsResponseIn": "_cloudbilling_4_ListBillingAccountsResponseIn",
        "ListBillingAccountsResponseOut": "_cloudbilling_5_ListBillingAccountsResponseOut",
        "SkuIn": "_cloudbilling_6_SkuIn",
        "SkuOut": "_cloudbilling_7_SkuOut",
        "GeoTaxonomyIn": "_cloudbilling_8_GeoTaxonomyIn",
        "GeoTaxonomyOut": "_cloudbilling_9_GeoTaxonomyOut",
        "ProjectBillingInfoIn": "_cloudbilling_10_ProjectBillingInfoIn",
        "ProjectBillingInfoOut": "_cloudbilling_11_ProjectBillingInfoOut",
        "BillingAccountIn": "_cloudbilling_12_BillingAccountIn",
        "BillingAccountOut": "_cloudbilling_13_BillingAccountOut",
        "CategoryIn": "_cloudbilling_14_CategoryIn",
        "CategoryOut": "_cloudbilling_15_CategoryOut",
        "AggregationInfoIn": "_cloudbilling_16_AggregationInfoIn",
        "AggregationInfoOut": "_cloudbilling_17_AggregationInfoOut",
        "BindingIn": "_cloudbilling_18_BindingIn",
        "BindingOut": "_cloudbilling_19_BindingOut",
        "ServiceIn": "_cloudbilling_20_ServiceIn",
        "ServiceOut": "_cloudbilling_21_ServiceOut",
        "ListSkusResponseIn": "_cloudbilling_22_ListSkusResponseIn",
        "ListSkusResponseOut": "_cloudbilling_23_ListSkusResponseOut",
        "SetIamPolicyRequestIn": "_cloudbilling_24_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudbilling_25_SetIamPolicyRequestOut",
        "ListProjectBillingInfoResponseIn": "_cloudbilling_26_ListProjectBillingInfoResponseIn",
        "ListProjectBillingInfoResponseOut": "_cloudbilling_27_ListProjectBillingInfoResponseOut",
        "AuditLogConfigIn": "_cloudbilling_28_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudbilling_29_AuditLogConfigOut",
        "TestIamPermissionsResponseIn": "_cloudbilling_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudbilling_31_TestIamPermissionsResponseOut",
        "MoneyIn": "_cloudbilling_32_MoneyIn",
        "MoneyOut": "_cloudbilling_33_MoneyOut",
        "AuditConfigIn": "_cloudbilling_34_AuditConfigIn",
        "AuditConfigOut": "_cloudbilling_35_AuditConfigOut",
        "ExprIn": "_cloudbilling_36_ExprIn",
        "ExprOut": "_cloudbilling_37_ExprOut",
        "TierRateIn": "_cloudbilling_38_TierRateIn",
        "TierRateOut": "_cloudbilling_39_TierRateOut",
        "PolicyIn": "_cloudbilling_40_PolicyIn",
        "PolicyOut": "_cloudbilling_41_PolicyOut",
        "PricingExpressionIn": "_cloudbilling_42_PricingExpressionIn",
        "PricingExpressionOut": "_cloudbilling_43_PricingExpressionOut",
        "ListServicesResponseIn": "_cloudbilling_44_ListServicesResponseIn",
        "ListServicesResponseOut": "_cloudbilling_45_ListServicesResponseOut",
        "PricingInfoIn": "_cloudbilling_46_PricingInfoIn",
        "PricingInfoOut": "_cloudbilling_47_PricingInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListBillingAccountsResponseIn"] = t.struct(
        {
            "billingAccounts": t.array(t.proxy(renames["BillingAccountIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBillingAccountsResponseIn"])
    types["ListBillingAccountsResponseOut"] = t.struct(
        {
            "billingAccounts": t.array(
                t.proxy(renames["BillingAccountOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBillingAccountsResponseOut"])
    types["SkuIn"] = t.struct(
        {
            "category": t.proxy(renames["CategoryIn"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoIn"])).optional(),
            "serviceProviderName": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyIn"]).optional(),
            "description": t.string().optional(),
            "skuId": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SkuIn"])
    types["SkuOut"] = t.struct(
        {
            "category": t.proxy(renames["CategoryOut"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoOut"])).optional(),
            "serviceProviderName": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyOut"]).optional(),
            "description": t.string().optional(),
            "skuId": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkuOut"])
    types["GeoTaxonomyIn"] = t.struct(
        {"regions": t.array(t.string()).optional(), "type": t.string().optional()}
    ).named(renames["GeoTaxonomyIn"])
    types["GeoTaxonomyOut"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoTaxonomyOut"])
    types["ProjectBillingInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "billingAccountName": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["ProjectBillingInfoIn"])
    types["ProjectBillingInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "billingAccountName": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectBillingInfoOut"])
    types["BillingAccountIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "masterBillingAccount": t.string().optional(),
        }
    ).named(renames["BillingAccountIn"])
    types["BillingAccountOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "open": t.boolean().optional(),
            "masterBillingAccount": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAccountOut"])
    types["CategoryIn"] = t.struct(
        {
            "resourceGroup": t.string().optional(),
            "resourceFamily": t.string().optional(),
            "usageType": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "resourceGroup": t.string().optional(),
            "resourceFamily": t.string().optional(),
            "usageType": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["AggregationInfoIn"] = t.struct(
        {
            "aggregationCount": t.integer().optional(),
            "aggregationInterval": t.string(),
            "aggregationLevel": t.string(),
        }
    ).named(renames["AggregationInfoIn"])
    types["AggregationInfoOut"] = t.struct(
        {
            "aggregationCount": t.integer().optional(),
            "aggregationInterval": t.string(),
            "aggregationLevel": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationInfoOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ServiceIn"] = t.struct(
        {
            "businessEntityName": t.string().optional(),
            "serviceId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "businessEntityName": t.string().optional(),
            "serviceId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["ListSkusResponseIn"] = t.struct(
        {
            "skus": t.array(t.proxy(renames["SkuIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSkusResponseIn"])
    types["ListSkusResponseOut"] = t.struct(
        {
            "skus": t.array(t.proxy(renames["SkuOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSkusResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TierRateIn"] = t.struct(
        {
            "unitPrice": t.proxy(renames["MoneyIn"]).optional(),
            "startUsageAmount": t.number().optional(),
        }
    ).named(renames["TierRateIn"])
    types["TierRateOut"] = t.struct(
        {
            "unitPrice": t.proxy(renames["MoneyOut"]).optional(),
            "startUsageAmount": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TierRateOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["PricingExpressionIn"] = t.struct(
        {
            "baseUnit": t.string().optional(),
            "displayQuantity": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateIn"])).optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "usageUnitDescription": t.string().optional(),
            "usageUnit": t.string().optional(),
        }
    ).named(renames["PricingExpressionIn"])
    types["PricingExpressionOut"] = t.struct(
        {
            "baseUnit": t.string().optional(),
            "displayQuantity": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateOut"])).optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "usageUnitDescription": t.string().optional(),
            "usageUnit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingExpressionOut"])
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
    types["PricingInfoIn"] = t.struct(
        {
            "aggregationInfo": t.proxy(renames["AggregationInfoIn"]).optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionIn"]).optional(),
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
        }
    ).named(renames["PricingInfoIn"])
    types["PricingInfoOut"] = t.struct(
        {
            "aggregationInfo": t.proxy(renames["AggregationInfoOut"]).optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionOut"]).optional(),
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingInfoOut"])

    functions = {}
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
                "parent": t.string(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "currencyCode": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetBillingInfo"] = cloudbilling.put(
        "v1/{name}/billingInfo",
        t.struct(
            {
                "name": t.string().optional(),
                "billingAccountName": t.string().optional(),
                "billingEnabled": t.boolean().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectBillingInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateBillingInfo"] = cloudbilling.put(
        "v1/{name}/billingInfo",
        t.struct(
            {
                "name": t.string().optional(),
                "billingAccountName": t.string().optional(),
                "billingEnabled": t.boolean().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectBillingInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetIamPolicy"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsTestIamPermissions"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGet"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsPatch"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsCreate"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSetIamPolicy"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsList"] = cloudbilling.get(
        "v1/billingAccounts",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBillingAccountsResponseOut"]),
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

    return Import(
        importer="cloudbilling", renames=renames, types=types, functions=functions
    )
