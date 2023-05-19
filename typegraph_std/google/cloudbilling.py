from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudbilling() -> Import:
    cloudbilling = HTTPRuntime("https://cloudbilling.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbilling_1_ErrorResponse",
        "TestIamPermissionsResponseIn": "_cloudbilling_2_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudbilling_3_TestIamPermissionsResponseOut",
        "ExprIn": "_cloudbilling_4_ExprIn",
        "ExprOut": "_cloudbilling_5_ExprOut",
        "ListServicesResponseIn": "_cloudbilling_6_ListServicesResponseIn",
        "ListServicesResponseOut": "_cloudbilling_7_ListServicesResponseOut",
        "ProjectBillingInfoIn": "_cloudbilling_8_ProjectBillingInfoIn",
        "ProjectBillingInfoOut": "_cloudbilling_9_ProjectBillingInfoOut",
        "SkuIn": "_cloudbilling_10_SkuIn",
        "SkuOut": "_cloudbilling_11_SkuOut",
        "TestIamPermissionsRequestIn": "_cloudbilling_12_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudbilling_13_TestIamPermissionsRequestOut",
        "AggregationInfoIn": "_cloudbilling_14_AggregationInfoIn",
        "AggregationInfoOut": "_cloudbilling_15_AggregationInfoOut",
        "SetIamPolicyRequestIn": "_cloudbilling_16_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudbilling_17_SetIamPolicyRequestOut",
        "GeoTaxonomyIn": "_cloudbilling_18_GeoTaxonomyIn",
        "GeoTaxonomyOut": "_cloudbilling_19_GeoTaxonomyOut",
        "PricingExpressionIn": "_cloudbilling_20_PricingExpressionIn",
        "PricingExpressionOut": "_cloudbilling_21_PricingExpressionOut",
        "MoneyIn": "_cloudbilling_22_MoneyIn",
        "MoneyOut": "_cloudbilling_23_MoneyOut",
        "ListBillingAccountsResponseIn": "_cloudbilling_24_ListBillingAccountsResponseIn",
        "ListBillingAccountsResponseOut": "_cloudbilling_25_ListBillingAccountsResponseOut",
        "PricingInfoIn": "_cloudbilling_26_PricingInfoIn",
        "PricingInfoOut": "_cloudbilling_27_PricingInfoOut",
        "BindingIn": "_cloudbilling_28_BindingIn",
        "BindingOut": "_cloudbilling_29_BindingOut",
        "AuditLogConfigIn": "_cloudbilling_30_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudbilling_31_AuditLogConfigOut",
        "ServiceIn": "_cloudbilling_32_ServiceIn",
        "ServiceOut": "_cloudbilling_33_ServiceOut",
        "ListSkusResponseIn": "_cloudbilling_34_ListSkusResponseIn",
        "ListSkusResponseOut": "_cloudbilling_35_ListSkusResponseOut",
        "BillingAccountIn": "_cloudbilling_36_BillingAccountIn",
        "BillingAccountOut": "_cloudbilling_37_BillingAccountOut",
        "ListProjectBillingInfoResponseIn": "_cloudbilling_38_ListProjectBillingInfoResponseIn",
        "ListProjectBillingInfoResponseOut": "_cloudbilling_39_ListProjectBillingInfoResponseOut",
        "PolicyIn": "_cloudbilling_40_PolicyIn",
        "PolicyOut": "_cloudbilling_41_PolicyOut",
        "AuditConfigIn": "_cloudbilling_42_AuditConfigIn",
        "AuditConfigOut": "_cloudbilling_43_AuditConfigOut",
        "CategoryIn": "_cloudbilling_44_CategoryIn",
        "CategoryOut": "_cloudbilling_45_CategoryOut",
        "TierRateIn": "_cloudbilling_46_TierRateIn",
        "TierRateOut": "_cloudbilling_47_TierRateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["ProjectBillingInfoIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "billingAccountName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ProjectBillingInfoIn"])
    types["ProjectBillingInfoOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "billingAccountName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectBillingInfoOut"])
    types["SkuIn"] = t.struct(
        {
            "skuId": t.string().optional(),
            "name": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyIn"]).optional(),
            "category": t.proxy(renames["CategoryIn"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoIn"])).optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "serviceProviderName": t.string().optional(),
        }
    ).named(renames["SkuIn"])
    types["SkuOut"] = t.struct(
        {
            "skuId": t.string().optional(),
            "name": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyOut"]).optional(),
            "category": t.proxy(renames["CategoryOut"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoOut"])).optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "serviceProviderName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkuOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["PricingExpressionIn"] = t.struct(
        {
            "usageUnit": t.string().optional(),
            "baseUnit": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateIn"])).optional(),
            "displayQuantity": t.number().optional(),
            "usageUnitDescription": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
        }
    ).named(renames["PricingExpressionIn"])
    types["PricingExpressionOut"] = t.struct(
        {
            "usageUnit": t.string().optional(),
            "baseUnit": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "tieredRates": t.array(t.proxy(renames["TierRateOut"])).optional(),
            "displayQuantity": t.number().optional(),
            "usageUnitDescription": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingExpressionOut"])
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
    types["PricingInfoIn"] = t.struct(
        {
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionIn"]).optional(),
            "aggregationInfo": t.proxy(renames["AggregationInfoIn"]).optional(),
        }
    ).named(renames["PricingInfoIn"])
    types["PricingInfoOut"] = t.struct(
        {
            "currencyConversionRate": t.number().optional(),
            "effectiveTime": t.string().optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionOut"]).optional(),
            "aggregationInfo": t.proxy(renames["AggregationInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingInfoOut"])
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
            "displayName": t.string().optional(),
            "serviceId": t.string().optional(),
            "name": t.string().optional(),
            "businessEntityName": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "serviceId": t.string().optional(),
            "name": t.string().optional(),
            "businessEntityName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["BillingAccountIn"] = t.struct(
        {
            "masterBillingAccount": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["BillingAccountIn"])
    types["BillingAccountOut"] = t.struct(
        {
            "masterBillingAccount": t.string().optional(),
            "name": t.string().optional(),
            "open": t.boolean().optional(),
            "displayName": t.string().optional(),
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
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["CategoryIn"] = t.struct(
        {
            "resourceFamily": t.string().optional(),
            "usageType": t.string().optional(),
            "resourceGroup": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "resourceFamily": t.string().optional(),
            "usageType": t.string().optional(),
            "resourceGroup": t.string().optional(),
            "serviceDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
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

    functions = {}
    functions["billingAccountsList"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetIamPolicy"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSetIamPolicy"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsTestIamPermissions"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsPatch"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsCreate"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGet"] = cloudbilling.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BillingAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsProjectsList"] = cloudbilling.get(
        "v1/{name}/projects",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProjectBillingInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetBillingInfo"] = cloudbilling.put(
        "v1/{name}/billingInfo",
        t.struct(
            {
                "name": t.string().optional(),
                "projectId": t.string().optional(),
                "billingEnabled": t.boolean().optional(),
                "billingAccountName": t.string().optional(),
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
                "projectId": t.string().optional(),
                "billingEnabled": t.boolean().optional(),
                "billingAccountName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectBillingInfoOut"]),
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
                "currencyCode": t.string().optional(),
                "startTime": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSkusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudbilling",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
