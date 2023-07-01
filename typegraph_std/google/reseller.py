from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_reseller():
    reseller = HTTPRuntime("https://reseller.googleapis.com/")

    renames = {
        "ErrorResponse": "_reseller_1_ErrorResponse",
        "SeatsIn": "_reseller_2_SeatsIn",
        "SeatsOut": "_reseller_3_SeatsOut",
        "PrimaryAdminIn": "_reseller_4_PrimaryAdminIn",
        "PrimaryAdminOut": "_reseller_5_PrimaryAdminOut",
        "SubscriptionsIn": "_reseller_6_SubscriptionsIn",
        "SubscriptionsOut": "_reseller_7_SubscriptionsOut",
        "ResellernotifyResourceIn": "_reseller_8_ResellernotifyResourceIn",
        "ResellernotifyResourceOut": "_reseller_9_ResellernotifyResourceOut",
        "CustomerIn": "_reseller_10_CustomerIn",
        "CustomerOut": "_reseller_11_CustomerOut",
        "ChangePlanRequestIn": "_reseller_12_ChangePlanRequestIn",
        "ChangePlanRequestOut": "_reseller_13_ChangePlanRequestOut",
        "ResellernotifyGetwatchdetailsResponseIn": "_reseller_14_ResellernotifyGetwatchdetailsResponseIn",
        "ResellernotifyGetwatchdetailsResponseOut": "_reseller_15_ResellernotifyGetwatchdetailsResponseOut",
        "SubscriptionIn": "_reseller_16_SubscriptionIn",
        "SubscriptionOut": "_reseller_17_SubscriptionOut",
        "AddressIn": "_reseller_18_AddressIn",
        "AddressOut": "_reseller_19_AddressOut",
        "RenewalSettingsIn": "_reseller_20_RenewalSettingsIn",
        "RenewalSettingsOut": "_reseller_21_RenewalSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SeatsIn"] = t.struct(
        {
            "licensedNumberOfSeats": t.integer().optional(),
            "numberOfSeats": t.integer().optional(),
            "kind": t.string().optional(),
            "maximumNumberOfSeats": t.integer().optional(),
        }
    ).named(renames["SeatsIn"])
    types["SeatsOut"] = t.struct(
        {
            "licensedNumberOfSeats": t.integer().optional(),
            "numberOfSeats": t.integer().optional(),
            "kind": t.string().optional(),
            "maximumNumberOfSeats": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeatsOut"])
    types["PrimaryAdminIn"] = t.struct({"primaryEmail": t.string().optional()}).named(
        renames["PrimaryAdminIn"]
    )
    types["PrimaryAdminOut"] = t.struct(
        {
            "primaryEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryAdminOut"])
    types["SubscriptionsIn"] = t.struct(
        {
            "subscriptions": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["SubscriptionsIn"])
    types["SubscriptionsOut"] = t.struct(
        {
            "subscriptions": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionsOut"])
    types["ResellernotifyResourceIn"] = t.struct(
        {"topicName": t.string().optional()}
    ).named(renames["ResellernotifyResourceIn"])
    types["ResellernotifyResourceOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResellernotifyResourceOut"])
    types["CustomerIn"] = t.struct(
        {
            "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
            "postalAddress": t.proxy(renames["AddressIn"]).optional(),
            "phoneNumber": t.string().optional(),
            "customerId": t.string().optional(),
            "resourceUiUrl": t.string().optional(),
            "customerType": t.string().optional(),
            "customerDomainVerified": t.boolean().optional(),
            "alternateEmail": t.string().optional(),
            "kind": t.string().optional(),
            "customerDomain": t.string().optional(),
        }
    ).named(renames["CustomerIn"])
    types["CustomerOut"] = t.struct(
        {
            "primaryAdmin": t.proxy(renames["PrimaryAdminOut"]).optional(),
            "postalAddress": t.proxy(renames["AddressOut"]).optional(),
            "phoneNumber": t.string().optional(),
            "customerId": t.string().optional(),
            "resourceUiUrl": t.string().optional(),
            "customerType": t.string().optional(),
            "customerDomainVerified": t.boolean().optional(),
            "alternateEmail": t.string().optional(),
            "kind": t.string().optional(),
            "customerDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerOut"])
    types["ChangePlanRequestIn"] = t.struct(
        {
            "dealCode": t.string().optional(),
            "planName": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrderId": t.string().optional(),
            "seats": t.proxy(renames["SeatsIn"]).optional(),
        }
    ).named(renames["ChangePlanRequestIn"])
    types["ChangePlanRequestOut"] = t.struct(
        {
            "dealCode": t.string().optional(),
            "planName": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrderId": t.string().optional(),
            "seats": t.proxy(renames["SeatsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangePlanRequestOut"])
    types["ResellernotifyGetwatchdetailsResponseIn"] = t.struct(
        {
            "topicName": t.string().optional(),
            "serviceAccountEmailAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["ResellernotifyGetwatchdetailsResponseIn"])
    types["ResellernotifyGetwatchdetailsResponseOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "serviceAccountEmailAddresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResellernotifyGetwatchdetailsResponseOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "billingMethod": t.string().optional(),
            "transferInfo": t.struct(
                {
                    "transferabilityExpirationTime": t.string().optional(),
                    "currentLegacySkuId": t.string().optional(),
                    "minimumTransferableSeats": t.integer().optional(),
                }
            ).optional(),
            "plan": t.struct(
                {
                    "isCommitmentPlan": t.boolean().optional(),
                    "commitmentInterval": t.struct(
                        {
                            "endTime": t.string().optional(),
                            "startTime": t.string().optional(),
                        }
                    ).optional(),
                    "planName": t.string().optional(),
                }
            ).optional(),
            "customerId": t.string().optional(),
            "kind": t.string().optional(),
            "customerDomain": t.string().optional(),
            "dealCode": t.string().optional(),
            "resourceUiUrl": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "purchaseOrderId": t.string().optional(),
            "subscriptionId": t.string().optional(),
            "trialSettings": t.struct(
                {
                    "isInTrial": t.boolean().optional(),
                    "trialEndTime": t.string().optional(),
                }
            ).optional(),
            "seats": t.proxy(renames["SeatsIn"]).optional(),
            "renewalSettings": t.proxy(renames["RenewalSettingsIn"]).optional(),
            "skuName": t.string().optional(),
            "creationTime": t.string().optional(),
            "status": t.string().optional(),
            "skuId": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "billingMethod": t.string().optional(),
            "transferInfo": t.struct(
                {
                    "transferabilityExpirationTime": t.string().optional(),
                    "currentLegacySkuId": t.string().optional(),
                    "minimumTransferableSeats": t.integer().optional(),
                }
            ).optional(),
            "plan": t.struct(
                {
                    "isCommitmentPlan": t.boolean().optional(),
                    "commitmentInterval": t.struct(
                        {
                            "endTime": t.string().optional(),
                            "startTime": t.string().optional(),
                        }
                    ).optional(),
                    "planName": t.string().optional(),
                }
            ).optional(),
            "customerId": t.string().optional(),
            "kind": t.string().optional(),
            "customerDomain": t.string().optional(),
            "dealCode": t.string().optional(),
            "resourceUiUrl": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "purchaseOrderId": t.string().optional(),
            "subscriptionId": t.string().optional(),
            "trialSettings": t.struct(
                {
                    "isInTrial": t.boolean().optional(),
                    "trialEndTime": t.string().optional(),
                }
            ).optional(),
            "seats": t.proxy(renames["SeatsOut"]).optional(),
            "renewalSettings": t.proxy(renames["RenewalSettingsOut"]).optional(),
            "skuName": t.string().optional(),
            "creationTime": t.string().optional(),
            "status": t.string().optional(),
            "skuId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["AddressIn"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "kind": t.string().optional(),
            "locality": t.string().optional(),
            "addressLine2": t.string().optional(),
            "addressLine1": t.string().optional(),
            "addressLine3": t.string().optional(),
            "organizationName": t.string().optional(),
            "contactName": t.string().optional(),
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "countryCode": t.string().optional(),
            "kind": t.string().optional(),
            "locality": t.string().optional(),
            "addressLine2": t.string().optional(),
            "addressLine1": t.string().optional(),
            "addressLine3": t.string().optional(),
            "organizationName": t.string().optional(),
            "contactName": t.string().optional(),
            "region": t.string().optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["RenewalSettingsIn"] = t.struct(
        {"renewalType": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["RenewalSettingsIn"])
    types["RenewalSettingsOut"] = t.struct(
        {
            "renewalType": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenewalSettingsOut"])

    functions = {}
    functions["customersInsert"] = reseller.get(
        "apps/reseller/v1/customers/{customerId}",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPatch"] = reseller.get(
        "apps/reseller/v1/customers/{customerId}",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUpdate"] = reseller.get(
        "apps/reseller/v1/customers/{customerId}",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersGet"] = reseller.get(
        "apps/reseller/v1/customers/{customerId}",
        t.struct({"customerId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resellernotifyGetwatchdetails"] = reseller.post(
        "apps/reseller/v1/resellernotify/unregister",
        t.struct(
            {
                "serviceAccountEmailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResellernotifyResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resellernotifyRegister"] = reseller.post(
        "apps/reseller/v1/resellernotify/unregister",
        t.struct(
            {
                "serviceAccountEmailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResellernotifyResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resellernotifyUnregister"] = reseller.post(
        "apps/reseller/v1/resellernotify/unregister",
        t.struct(
            {
                "serviceAccountEmailAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResellernotifyResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsDelete"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangeSeats"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsGet"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsInsert"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangeRenewalSettings"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsList"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsActivate"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsStartPaidService"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangePlan"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsSuspend"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/suspend",
        t.struct(
            {
                "customerId": t.string().optional(),
                "subscriptionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="reseller", renames=renames, types=Box(types), functions=Box(functions)
    )
