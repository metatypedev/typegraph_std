from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_paymentsresellersubscription() -> Import:
    paymentsresellersubscription = HTTPRuntime(
        "https://paymentsresellersubscription.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_paymentsresellersubscription_1_ErrorResponse",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadIn": "_paymentsresellersubscription_2_GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadOut": "_paymentsresellersubscription_3_GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadOut",
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseIn": "_paymentsresellersubscription_4_GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseOut": "_paymentsresellersubscription_5_GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseOut",
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseIn": "_paymentsresellersubscription_6_GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseOut": "_paymentsresellersubscription_7_GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseOut",
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestIn": "_paymentsresellersubscription_8_GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestIn",
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestOut": "_paymentsresellersubscription_9_GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn": "_paymentsresellersubscription_10_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOut": "_paymentsresellersubscription_11_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOut",
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseIn": "_paymentsresellersubscription_12_GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseOut": "_paymentsresellersubscription_13_GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseOut",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIn": "_paymentsresellersubscription_14_GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIn",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut": "_paymentsresellersubscription_15_GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn": "_paymentsresellersubscription_16_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut": "_paymentsresellersubscription_17_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseIn": "_paymentsresellersubscription_18_GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseOut": "_paymentsresellersubscription_19_GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestIn": "_paymentsresellersubscription_20_GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestOut": "_paymentsresellersubscription_21_GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductIn": "_paymentsresellersubscription_22_GoogleCloudPaymentsResellerSubscriptionV1ProductIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductOut": "_paymentsresellersubscription_23_GoogleCloudPaymentsResellerSubscriptionV1ProductOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsIn": "_paymentsresellersubscription_24_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsOut": "_paymentsresellersubscription_25_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsOut",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIn": "_paymentsresellersubscription_26_GoogleCloudPaymentsResellerSubscriptionV1PromotionIn",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionOut": "_paymentsresellersubscription_27_GoogleCloudPaymentsResellerSubscriptionV1PromotionOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn": "_paymentsresellersubscription_28_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsOut": "_paymentsresellersubscription_29_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigIn": "_paymentsresellersubscription_30_GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigOut": "_paymentsresellersubscription_31_GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn": "_paymentsresellersubscription_32_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut": "_paymentsresellersubscription_33_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut",
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseIn": "_paymentsresellersubscription_34_GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseOut": "_paymentsresellersubscription_35_GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseOut",
        "GoogleTypeLocalizedTextIn": "_paymentsresellersubscription_36_GoogleTypeLocalizedTextIn",
        "GoogleTypeLocalizedTextOut": "_paymentsresellersubscription_37_GoogleTypeLocalizedTextOut",
        "GoogleCloudPaymentsResellerSubscriptionV1DurationIn": "_paymentsresellersubscription_38_GoogleCloudPaymentsResellerSubscriptionV1DurationIn",
        "GoogleCloudPaymentsResellerSubscriptionV1DurationOut": "_paymentsresellersubscription_39_GoogleCloudPaymentsResellerSubscriptionV1DurationOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtensionIn": "_paymentsresellersubscription_40_GoogleCloudPaymentsResellerSubscriptionV1ExtensionIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ExtensionOut": "_paymentsresellersubscription_41_GoogleCloudPaymentsResellerSubscriptionV1ExtensionOut",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsIn": "_paymentsresellersubscription_42_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsIn",
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsOut": "_paymentsresellersubscription_43_GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseIn": "_paymentsresellersubscription_44_GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut": "_paymentsresellersubscription_45_GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecIn": "_paymentsresellersubscription_46_GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecIn",
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecOut": "_paymentsresellersubscription_47_GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecOut",
        "GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadIn": "_paymentsresellersubscription_48_GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadIn",
        "GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadOut": "_paymentsresellersubscription_49_GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodIn": "_paymentsresellersubscription_50_GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodOut": "_paymentsresellersubscription_51_GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodOut",
        "GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadIn": "_paymentsresellersubscription_52_GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadIn",
        "GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadOut": "_paymentsresellersubscription_53_GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadOut",
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestIn": "_paymentsresellersubscription_54_GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestIn",
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestOut": "_paymentsresellersubscription_55_GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestOut",
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestIn": "_paymentsresellersubscription_56_GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestIn",
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestOut": "_paymentsresellersubscription_57_GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestOut",
        "GoogleCloudPaymentsResellerSubscriptionV1AmountIn": "_paymentsresellersubscription_58_GoogleCloudPaymentsResellerSubscriptionV1AmountIn",
        "GoogleCloudPaymentsResellerSubscriptionV1AmountOut": "_paymentsresellersubscription_59_GoogleCloudPaymentsResellerSubscriptionV1AmountOut",
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestIn": "_paymentsresellersubscription_60_GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestIn",
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestOut": "_paymentsresellersubscription_61_GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestOut",
        "GoogleCloudPaymentsResellerSubscriptionV1LocationIn": "_paymentsresellersubscription_62_GoogleCloudPaymentsResellerSubscriptionV1LocationIn",
        "GoogleCloudPaymentsResellerSubscriptionV1LocationOut": "_paymentsresellersubscription_63_GoogleCloudPaymentsResellerSubscriptionV1LocationOut",
        "GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseIn": "_paymentsresellersubscription_64_GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseIn",
        "GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseOut": "_paymentsresellersubscription_65_GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadIn"] = t.struct(
        {
            "youtubePayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadIn"]
            ).optional(),
            "googleOnePayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadOut"] = t.struct(
        {
            "youtubePayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadOut"]
            ).optional(),
            "googleOnePayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseIn"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn"]
            ).optional()
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseOut"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponseOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionIn"])
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "promotions": t.array(
                t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponseOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestIn"
    ] = t.struct(
        {
            "cancelImmediately": t.boolean().optional(),
            "cancellationReason": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestOut"
    ] = t.struct(
        {
            "cancelImmediately": t.boolean().optional(),
            "cancellationReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequestOut"]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"] = t.struct(
        {
            "productPayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadIn"]
            ).optional(),
            "lineItemPromotionSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                    ]
                )
            ).optional(),
            "product": t.string(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOut"
    ] = t.struct(
        {
            "recurrenceType": t.string().optional(),
            "oneTimeRecurrenceDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsOut"
                ]
            ).optional(),
            "productPayload": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPayloadOut"]
            ).optional(),
            "lineItemFreeTrialEndTime": t.string().optional(),
            "amount": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1AmountOut"]
            ).optional(),
            "lineItemPromotionSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut"
                    ]
                )
            ).optional(),
            "description": t.string().optional(),
            "product": t.string(),
            "lineItemIndex": t.integer().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOut"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseIn"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseOut"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponseOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIn"
    ] = t.struct(
        {
            "introductoryPricingSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecIn"
                    ]
                )
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut"
    ] = t.struct(
        {
            "introductoryPricingSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
    ] = t.struct({"promotion": t.string()}).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut"
    ] = t.struct(
        {
            "type": t.string().optional(),
            "freeTrialDuration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"]
            ).optional(),
            "promotion": t.string(),
            "introductoryPricingDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseIn"
    ] = t.struct(
        {
            "freeTrialEndTime": t.string().optional(),
            "cycleEndTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseOut"
    ] = t.struct(
        {
            "renewalTime": t.string().optional(),
            "freeTrialEndTime": t.string().optional(),
            "cycleEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponseOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestIn"
    ] = t.struct(
        {
            "extension": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ExtensionIn"]
            ),
            "requestId": t.string(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestOut"
    ] = t.struct(
        {
            "extension": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ExtensionOut"]
            ),
            "requestId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequestOut"]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductOut"] = t.struct(
        {
            "regionCodes": t.array(t.string()).optional(),
            "priceConfigs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigOut"
                    ]
                )
            ).optional(),
            "subscriptionBillingCycleDuration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"]
            ).optional(),
            "titles": t.array(
                t.proxy(renames["GoogleTypeLocalizedTextOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsIn"
    ] = t.struct({"reason": t.string().optional()}).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsOut"
    ] = t.struct(
        {
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsOut"
        ]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1PromotionIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "introductoryPricingDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIn"
                ]
            ).optional(),
            "endTime": t.string().optional(),
            "freeTrialDuration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1PromotionOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "applicableProducts": t.array(t.string()).optional(),
            "titles": t.array(
                t.proxy(renames["GoogleTypeLocalizedTextOut"])
            ).optional(),
            "introductoryPricingDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsOut"
                ]
            ).optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "promotionType": t.string().optional(),
            "freeTrialDuration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"]
            ).optional(),
            "regionCodes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
    ] = t.struct(
        {"previousSubscriptionId": t.string(), "billingCycleSpec": t.string()}
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsOut"
    ] = t.struct(
        {
            "previousSubscriptionId": t.string(),
            "billingCycleSpec": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsOut"
        ]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "amount": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1AmountOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfigOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn"] = t.struct(
        {
            "lineItems": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                    ]
                )
            ),
            "partnerUserToken": t.string(),
            "promotionSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                    ]
                )
            ).optional(),
            "products": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "serviceLocation": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
            ),
            "promotions": t.array(t.string()).optional(),
            "upgradeDowngradeDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"] = t.struct(
        {
            "lineItems": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOut"
                    ]
                )
            ),
            "freeTrialEndTime": t.string().optional(),
            "partnerUserToken": t.string(),
            "promotionSpecs": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecOut"
                    ]
                )
            ).optional(),
            "processingState": t.string().optional(),
            "cancellationDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetailsOut"
                ]
            ).optional(),
            "products": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "serviceLocation": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1LocationOut"]
            ),
            "cycleEndTime": t.string().optional(),
            "state": t.string().optional(),
            "redirectUri": t.string().optional(),
            "renewalTime": t.string().optional(),
            "createTime": t.string().optional(),
            "promotions": t.array(t.string()).optional(),
            "endUserEntitled": t.boolean().optional(),
            "upgradeDowngradeDetails": t.proxy(
                renames[
                    "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseIn"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseOut"
    ] = t.struct(
        {
            "subscription": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponseOut"
        ]
    )
    types["GoogleTypeLocalizedTextIn"] = t.struct(
        {"languageCode": t.string().optional(), "text": t.string().optional()}
    ).named(renames["GoogleTypeLocalizedTextIn"])
    types["GoogleTypeLocalizedTextOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeLocalizedTextOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1DurationIn"] = t.struct(
        {"unit": t.string().optional(), "count": t.integer().optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1DurationIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ExtensionIn"] = t.struct(
        {
            "partnerUserToken": t.string(),
            "duration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ExtensionIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ExtensionOut"] = t.struct(
        {
            "partnerUserToken": t.string(),
            "duration": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1DurationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ExtensionOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsIn"
    ] = t.struct(
        {
            "servicePeriod": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodIn"]
            ).optional()
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsOut"
    ] = t.struct(
        {
            "servicePeriod": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetailsOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "promotions": t.array(
                t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "promotions": t.array(
                t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1PromotionOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecOut"
    ] = t.struct(
        {
            "discountAmount": t.proxy(
                renames["GoogleCloudPaymentsResellerSubscriptionV1AmountOut"]
            ).optional(),
            "recurrenceCount": t.integer().optional(),
            "discountRatioMicros": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpecOut"
        ]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadIn"] = t.struct(
        {
            "campaigns": t.array(t.string()).optional(),
            "offering": t.string().optional(),
            "salesChannel": t.string().optional(),
            "storeId": t.string().optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadOut"] = t.struct(
        {
            "campaigns": t.array(t.string()).optional(),
            "offering": t.string().optional(),
            "salesChannel": t.string().optional(),
            "storeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayloadOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodIn"] = t.struct(
        {"startTime": t.string(), "endTime": t.string().optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodOut"] = t.struct(
        {
            "startTime": t.string(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ServicePeriodOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadIn"] = t.struct(
        {"partnerEligibilityIds": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadOut"] = t.struct(
        {
            "partnerEligibilityIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1YoutubePayloadOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestIn"
    ] = t.struct(
        {
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestOut"
    ] = t.struct(
        {
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequestOut"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestIn"
        ]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequestOut"
        ]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1AmountIn"] = t.struct(
        {"amountMicros": t.string(), "currencyCode": t.string()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1AmountIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1AmountOut"] = t.struct(
        {
            "amountMicros": t.string(),
            "currencyCode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1AmountOut"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestIn"]
    )
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames[
            "GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestOut"
        ]
    )
    types["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"] = t.struct(
        {"regionCode": t.string().optional(), "postalCode": t.string().optional()}
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"])
    types["GoogleCloudPaymentsResellerSubscriptionV1LocationOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1LocationOut"])
    types["GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseIn"])
    types[
        "GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "products": t.array(
                t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1ProductOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseOut"]
    )

    functions = {}
    functions["partnersSubscriptionsCancel"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsExtend"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsGet"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsUndoCancel"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsEntitle"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsProvision"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersSubscriptionsCreate"] = paymentsresellersubscription.post(
        "v1/{parent}/subscriptions",
        t.struct(
            {
                "subscriptionId": t.string(),
                "parent": t.string(),
                "lineItems": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemIn"
                        ]
                    )
                ),
                "partnerUserToken": t.string(),
                "promotionSpecs": t.array(
                    t.proxy(
                        renames[
                            "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpecIn"
                        ]
                    )
                ).optional(),
                "products": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "serviceLocation": t.proxy(
                    renames["GoogleCloudPaymentsResellerSubscriptionV1LocationIn"]
                ),
                "promotions": t.array(t.string()).optional(),
                "upgradeDowngradeDetails": t.proxy(
                    renames[
                        "GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetailsIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPaymentsResellerSubscriptionV1SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersProductsList"] = paymentsresellersubscription.get(
        "v1/{parent}/products",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersPromotionsFindEligible"] = paymentsresellersubscription.get(
        "v1/{parent}/promotions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersPromotionsList"] = paymentsresellersubscription.get(
        "v1/{parent}/promotions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="paymentsresellersubscription",
        renames=renames,
        types=types,
        functions=functions,
    )
