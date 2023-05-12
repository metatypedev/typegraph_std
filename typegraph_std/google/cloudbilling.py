from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudbilling() -> Import:
    cloudbilling = HTTPRuntime("https://cloudbilling.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudbilling_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_cloudbilling_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudbilling_3_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_cloudbilling_4_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudbilling_5_TestIamPermissionsResponseOut",
        "AggregationInfoIn": "_cloudbilling_6_AggregationInfoIn",
        "AggregationInfoOut": "_cloudbilling_7_AggregationInfoOut",
        "AuditLogConfigIn": "_cloudbilling_8_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudbilling_9_AuditLogConfigOut",
        "ListProjectBillingInfoResponseIn": "_cloudbilling_10_ListProjectBillingInfoResponseIn",
        "ListProjectBillingInfoResponseOut": "_cloudbilling_11_ListProjectBillingInfoResponseOut",
        "MoneyIn": "_cloudbilling_12_MoneyIn",
        "MoneyOut": "_cloudbilling_13_MoneyOut",
        "BillingAccountIn": "_cloudbilling_14_BillingAccountIn",
        "BillingAccountOut": "_cloudbilling_15_BillingAccountOut",
        "ExprIn": "_cloudbilling_16_ExprIn",
        "ExprOut": "_cloudbilling_17_ExprOut",
        "ProjectBillingInfoIn": "_cloudbilling_18_ProjectBillingInfoIn",
        "ProjectBillingInfoOut": "_cloudbilling_19_ProjectBillingInfoOut",
        "PricingExpressionIn": "_cloudbilling_20_PricingExpressionIn",
        "PricingExpressionOut": "_cloudbilling_21_PricingExpressionOut",
        "TierRateIn": "_cloudbilling_22_TierRateIn",
        "TierRateOut": "_cloudbilling_23_TierRateOut",
        "PolicyIn": "_cloudbilling_24_PolicyIn",
        "PolicyOut": "_cloudbilling_25_PolicyOut",
        "ListServicesResponseIn": "_cloudbilling_26_ListServicesResponseIn",
        "ListServicesResponseOut": "_cloudbilling_27_ListServicesResponseOut",
        "SetIamPolicyRequestIn": "_cloudbilling_28_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudbilling_29_SetIamPolicyRequestOut",
        "SkuIn": "_cloudbilling_30_SkuIn",
        "SkuOut": "_cloudbilling_31_SkuOut",
        "ServiceIn": "_cloudbilling_32_ServiceIn",
        "ServiceOut": "_cloudbilling_33_ServiceOut",
        "BindingIn": "_cloudbilling_34_BindingIn",
        "BindingOut": "_cloudbilling_35_BindingOut",
        "AuditConfigIn": "_cloudbilling_36_AuditConfigIn",
        "AuditConfigOut": "_cloudbilling_37_AuditConfigOut",
        "CategoryIn": "_cloudbilling_38_CategoryIn",
        "CategoryOut": "_cloudbilling_39_CategoryOut",
        "PricingInfoIn": "_cloudbilling_40_PricingInfoIn",
        "PricingInfoOut": "_cloudbilling_41_PricingInfoOut",
        "GeoTaxonomyIn": "_cloudbilling_42_GeoTaxonomyIn",
        "GeoTaxonomyOut": "_cloudbilling_43_GeoTaxonomyOut",
        "ListSkusResponseIn": "_cloudbilling_44_ListSkusResponseIn",
        "ListSkusResponseOut": "_cloudbilling_45_ListSkusResponseOut",
        "ListBillingAccountsResponseIn": "_cloudbilling_46_ListBillingAccountsResponseIn",
        "ListBillingAccountsResponseOut": "_cloudbilling_47_ListBillingAccountsResponseOut",
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AggregationInfoIn"] = t.struct(
        {
            "aggregationCount": t.integer().optional(),
            "aggregationLevel": t.string(),
            "aggregationInterval": t.string(),
        }
    ).named(renames["AggregationInfoIn"])
    types["AggregationInfoOut"] = t.struct(
        {
            "aggregationCount": t.integer().optional(),
            "aggregationLevel": t.string(),
            "aggregationInterval": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregationInfoOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ListProjectBillingInfoResponseIn"] = t.struct(
        {
            "projectBillingInfo": t.array(
                t.proxy(renames["ProjectBillingInfoIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProjectBillingInfoResponseIn"])
    types["ListProjectBillingInfoResponseOut"] = t.struct(
        {
            "projectBillingInfo": t.array(
                t.proxy(renames["ProjectBillingInfoOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProjectBillingInfoResponseOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["BillingAccountIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "masterBillingAccount": t.string().optional(),
        }
    ).named(renames["BillingAccountIn"])
    types["BillingAccountOut"] = t.struct(
        {
            "open": t.boolean().optional(),
            "displayName": t.string().optional(),
            "masterBillingAccount": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingAccountOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ProjectBillingInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "projectId": t.string().optional(),
            "billingAccountName": t.string().optional(),
        }
    ).named(renames["ProjectBillingInfoIn"])
    types["ProjectBillingInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "billingEnabled": t.boolean().optional(),
            "projectId": t.string().optional(),
            "billingAccountName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectBillingInfoOut"])
    types["PricingExpressionIn"] = t.struct(
        {
            "tieredRates": t.array(t.proxy(renames["TierRateIn"])).optional(),
            "usageUnit": t.string().optional(),
            "usageUnitDescription": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnit": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "displayQuantity": t.number().optional(),
        }
    ).named(renames["PricingExpressionIn"])
    types["PricingExpressionOut"] = t.struct(
        {
            "tieredRates": t.array(t.proxy(renames["TierRateOut"])).optional(),
            "usageUnit": t.string().optional(),
            "usageUnitDescription": t.string().optional(),
            "baseUnitDescription": t.string().optional(),
            "baseUnit": t.string().optional(),
            "baseUnitConversionFactor": t.number().optional(),
            "displayQuantity": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingExpressionOut"])
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
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SkuIn"] = t.struct(
        {
            "category": t.proxy(renames["CategoryIn"]).optional(),
            "name": t.string().optional(),
            "serviceProviderName": t.string().optional(),
            "description": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "skuId": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyIn"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoIn"])).optional(),
        }
    ).named(renames["SkuIn"])
    types["SkuOut"] = t.struct(
        {
            "category": t.proxy(renames["CategoryOut"]).optional(),
            "name": t.string().optional(),
            "serviceProviderName": t.string().optional(),
            "description": t.string().optional(),
            "serviceRegions": t.array(t.string()).optional(),
            "skuId": t.string().optional(),
            "geoTaxonomy": t.proxy(renames["GeoTaxonomyOut"]).optional(),
            "pricingInfo": t.array(t.proxy(renames["PricingInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SkuOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["PricingInfoIn"] = t.struct(
        {
            "effectiveTime": t.string().optional(),
            "aggregationInfo": t.proxy(renames["AggregationInfoIn"]).optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionIn"]).optional(),
            "currencyConversionRate": t.number().optional(),
        }
    ).named(renames["PricingInfoIn"])
    types["PricingInfoOut"] = t.struct(
        {
            "effectiveTime": t.string().optional(),
            "aggregationInfo": t.proxy(renames["AggregationInfoOut"]).optional(),
            "summary": t.string().optional(),
            "pricingExpression": t.proxy(renames["PricingExpressionOut"]).optional(),
            "currencyConversionRate": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PricingInfoOut"])
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

    functions = {}
    functions["billingAccountsTestIamPermissions"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGetIamPolicy"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsPatch"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsCreate"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsList"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsGet"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsSetIamPolicy"] = cloudbilling.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsProjectsList"] = cloudbilling.get(
        "v1/{name}/projects",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProjectBillingInfoResponseOut"]),
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
    functions["servicesList"] = cloudbilling.get(
        "v1/services",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "currencyCode": t.string().optional(),
                "startTime": t.string().optional(),
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
