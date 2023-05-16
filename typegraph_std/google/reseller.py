from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_reseller() -> Import:
    reseller = HTTPRuntime("https://reseller.googleapis.com/")

    renames = {
        "ErrorResponse": "_reseller_1_ErrorResponse",
        "RenewalSettingsIn": "_reseller_2_RenewalSettingsIn",
        "RenewalSettingsOut": "_reseller_3_RenewalSettingsOut",
        "SubscriptionsIn": "_reseller_4_SubscriptionsIn",
        "SubscriptionsOut": "_reseller_5_SubscriptionsOut",
        "SeatsIn": "_reseller_6_SeatsIn",
        "SeatsOut": "_reseller_7_SeatsOut",
        "ResellernotifyGetwatchdetailsResponseIn": "_reseller_8_ResellernotifyGetwatchdetailsResponseIn",
        "ResellernotifyGetwatchdetailsResponseOut": "_reseller_9_ResellernotifyGetwatchdetailsResponseOut",
        "PrimaryAdminIn": "_reseller_10_PrimaryAdminIn",
        "PrimaryAdminOut": "_reseller_11_PrimaryAdminOut",
        "ChangePlanRequestIn": "_reseller_12_ChangePlanRequestIn",
        "ChangePlanRequestOut": "_reseller_13_ChangePlanRequestOut",
        "SubscriptionIn": "_reseller_14_SubscriptionIn",
        "SubscriptionOut": "_reseller_15_SubscriptionOut",
        "CustomerIn": "_reseller_16_CustomerIn",
        "CustomerOut": "_reseller_17_CustomerOut",
        "AddressIn": "_reseller_18_AddressIn",
        "AddressOut": "_reseller_19_AddressOut",
        "ResellernotifyResourceIn": "_reseller_20_ResellernotifyResourceIn",
        "ResellernotifyResourceOut": "_reseller_21_ResellernotifyResourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SeatsIn"] = t.struct(
        {
            "numberOfSeats": t.integer().optional(),
            "kind": t.string().optional(),
            "licensedNumberOfSeats": t.integer().optional(),
            "maximumNumberOfSeats": t.integer().optional(),
        }
    ).named(renames["SeatsIn"])
    types["SeatsOut"] = t.struct(
        {
            "numberOfSeats": t.integer().optional(),
            "kind": t.string().optional(),
            "licensedNumberOfSeats": t.integer().optional(),
            "maximumNumberOfSeats": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeatsOut"])
    types["ResellernotifyGetwatchdetailsResponseIn"] = t.struct(
        {
            "serviceAccountEmailAddresses": t.array(t.string()).optional(),
            "topicName": t.string().optional(),
        }
    ).named(renames["ResellernotifyGetwatchdetailsResponseIn"])
    types["ResellernotifyGetwatchdetailsResponseOut"] = t.struct(
        {
            "serviceAccountEmailAddresses": t.array(t.string()).optional(),
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResellernotifyGetwatchdetailsResponseOut"])
    types["PrimaryAdminIn"] = t.struct({"primaryEmail": t.string().optional()}).named(
        renames["PrimaryAdminIn"]
    )
    types["PrimaryAdminOut"] = t.struct(
        {
            "primaryEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrimaryAdminOut"])
    types["ChangePlanRequestIn"] = t.struct(
        {
            "planName": t.string().optional(),
            "seats": t.proxy(renames["SeatsIn"]).optional(),
            "dealCode": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrderId": t.string().optional(),
        }
    ).named(renames["ChangePlanRequestIn"])
    types["ChangePlanRequestOut"] = t.struct(
        {
            "planName": t.string().optional(),
            "seats": t.proxy(renames["SeatsOut"]).optional(),
            "dealCode": t.string().optional(),
            "kind": t.string().optional(),
            "purchaseOrderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangePlanRequestOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "subscriptionId": t.string().optional(),
            "plan": t.struct(
                {
                    "planName": t.string().optional(),
                    "commitmentInterval": t.struct(
                        {
                            "startTime": t.string().optional(),
                            "endTime": t.string().optional(),
                        }
                    ).optional(),
                    "isCommitmentPlan": t.boolean().optional(),
                }
            ).optional(),
            "creationTime": t.string().optional(),
            "skuId": t.string().optional(),
            "transferInfo": t.struct(
                {
                    "transferabilityExpirationTime": t.string().optional(),
                    "currentLegacySkuId": t.string().optional(),
                    "minimumTransferableSeats": t.integer().optional(),
                }
            ).optional(),
            "customerId": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "purchaseOrderId": t.string().optional(),
            "customerDomain": t.string().optional(),
            "seats": t.proxy(renames["SeatsIn"]).optional(),
            "resourceUiUrl": t.string().optional(),
            "billingMethod": t.string().optional(),
            "trialSettings": t.struct(
                {
                    "trialEndTime": t.string().optional(),
                    "isInTrial": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "dealCode": t.string().optional(),
            "status": t.string().optional(),
            "renewalSettings": t.proxy(renames["RenewalSettingsIn"]).optional(),
            "skuName": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "subscriptionId": t.string().optional(),
            "plan": t.struct(
                {
                    "planName": t.string().optional(),
                    "commitmentInterval": t.struct(
                        {
                            "startTime": t.string().optional(),
                            "endTime": t.string().optional(),
                        }
                    ).optional(),
                    "isCommitmentPlan": t.boolean().optional(),
                }
            ).optional(),
            "creationTime": t.string().optional(),
            "skuId": t.string().optional(),
            "transferInfo": t.struct(
                {
                    "transferabilityExpirationTime": t.string().optional(),
                    "currentLegacySkuId": t.string().optional(),
                    "minimumTransferableSeats": t.integer().optional(),
                }
            ).optional(),
            "customerId": t.string().optional(),
            "suspensionReasons": t.array(t.string()).optional(),
            "purchaseOrderId": t.string().optional(),
            "customerDomain": t.string().optional(),
            "seats": t.proxy(renames["SeatsOut"]).optional(),
            "resourceUiUrl": t.string().optional(),
            "billingMethod": t.string().optional(),
            "trialSettings": t.struct(
                {
                    "trialEndTime": t.string().optional(),
                    "isInTrial": t.boolean().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "dealCode": t.string().optional(),
            "status": t.string().optional(),
            "renewalSettings": t.proxy(renames["RenewalSettingsOut"]).optional(),
            "skuName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["CustomerIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "alternateEmail": t.string().optional(),
            "customerType": t.string().optional(),
            "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
            "customerId": t.string().optional(),
            "postalAddress": t.proxy(renames["AddressIn"]).optional(),
            "customerDomainVerified": t.boolean().optional(),
            "resourceUiUrl": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "customerDomain": t.string().optional(),
        }
    ).named(renames["CustomerIn"])
    types["CustomerOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "alternateEmail": t.string().optional(),
            "customerType": t.string().optional(),
            "primaryAdmin": t.proxy(renames["PrimaryAdminOut"]).optional(),
            "customerId": t.string().optional(),
            "postalAddress": t.proxy(renames["AddressOut"]).optional(),
            "customerDomainVerified": t.boolean().optional(),
            "resourceUiUrl": t.string().optional(),
            "phoneNumber": t.string().optional(),
            "customerDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerOut"])
    types["AddressIn"] = t.struct(
        {
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLine3": t.string().optional(),
            "region": t.string().optional(),
            "countryCode": t.string().optional(),
            "addressLine2": t.string().optional(),
            "contactName": t.string().optional(),
            "organizationName": t.string().optional(),
            "addressLine1": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "locality": t.string().optional(),
            "postalCode": t.string().optional(),
            "addressLine3": t.string().optional(),
            "region": t.string().optional(),
            "countryCode": t.string().optional(),
            "addressLine2": t.string().optional(),
            "contactName": t.string().optional(),
            "organizationName": t.string().optional(),
            "addressLine1": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["ResellernotifyResourceIn"] = t.struct(
        {"topicName": t.string().optional()}
    ).named(renames["ResellernotifyResourceIn"])
    types["ResellernotifyResourceOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResellernotifyResourceOut"])

    functions = {}
    functions["resellernotifyUnregister"] = reseller.get(
        "apps/reseller/v1/resellernotify/getwatchdetails",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ResellernotifyGetwatchdetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resellernotifyRegister"] = reseller.get(
        "apps/reseller/v1/resellernotify/getwatchdetails",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ResellernotifyGetwatchdetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resellernotifyGetwatchdetails"] = reseller.get(
        "apps/reseller/v1/resellernotify/getwatchdetails",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ResellernotifyGetwatchdetailsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUpdate"] = reseller.post(
        "apps/reseller/v1/customers",
        t.struct(
            {
                "customerAuthToken": t.string().optional(),
                "kind": t.string().optional(),
                "alternateEmail": t.string().optional(),
                "customerType": t.string().optional(),
                "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
                "customerId": t.string().optional(),
                "postalAddress": t.proxy(renames["AddressIn"]).optional(),
                "customerDomainVerified": t.boolean().optional(),
                "resourceUiUrl": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "customerDomain": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersGet"] = reseller.post(
        "apps/reseller/v1/customers",
        t.struct(
            {
                "customerAuthToken": t.string().optional(),
                "kind": t.string().optional(),
                "alternateEmail": t.string().optional(),
                "customerType": t.string().optional(),
                "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
                "customerId": t.string().optional(),
                "postalAddress": t.proxy(renames["AddressIn"]).optional(),
                "customerDomainVerified": t.boolean().optional(),
                "resourceUiUrl": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "customerDomain": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPatch"] = reseller.post(
        "apps/reseller/v1/customers",
        t.struct(
            {
                "customerAuthToken": t.string().optional(),
                "kind": t.string().optional(),
                "alternateEmail": t.string().optional(),
                "customerType": t.string().optional(),
                "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
                "customerId": t.string().optional(),
                "postalAddress": t.proxy(renames["AddressIn"]).optional(),
                "customerDomainVerified": t.boolean().optional(),
                "resourceUiUrl": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "customerDomain": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersInsert"] = reseller.post(
        "apps/reseller/v1/customers",
        t.struct(
            {
                "customerAuthToken": t.string().optional(),
                "kind": t.string().optional(),
                "alternateEmail": t.string().optional(),
                "customerType": t.string().optional(),
                "primaryAdmin": t.proxy(renames["PrimaryAdminIn"]).optional(),
                "customerId": t.string().optional(),
                "postalAddress": t.proxy(renames["AddressIn"]).optional(),
                "customerDomainVerified": t.boolean().optional(),
                "resourceUiUrl": t.string().optional(),
                "phoneNumber": t.string().optional(),
                "customerDomain": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsInsert"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangePlan"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsGet"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangeSeats"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsActivate"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsStartPaidService"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsList"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsSuspend"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsDelete"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["subscriptionsChangeRenewalSettings"] = reseller.post(
        "apps/reseller/v1/customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings",
        t.struct(
            {
                "subscriptionId": t.string().optional(),
                "customerId": t.string().optional(),
                "renewalType": t.string().optional(),
                "kind": t.string().optional(),
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
