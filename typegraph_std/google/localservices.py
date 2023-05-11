from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_localservices() -> Import:
    localservices = HTTPRuntime("https://localservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_localservices_1_ErrorResponse",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn": "_localservices_2_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut": "_localservices_3_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportIn": "_localservices_4_GoogleAdsHomeservicesLocalservicesV1AccountReportIn",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportOut": "_localservices_5_GoogleAdsHomeservicesLocalservicesV1AccountReportOut",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn": "_localservices_6_GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut": "_localservices_7_GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn": "_localservices_8_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut": "_localservices_9_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn": "_localservices_10_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut": "_localservices_11_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadIn": "_localservices_12_GoogleAdsHomeservicesLocalservicesV1BookingLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadOut": "_localservices_13_GoogleAdsHomeservicesLocalservicesV1BookingLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn": "_localservices_14_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut": "_localservices_15_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut",
        "GoogleTypeTimeZoneIn": "_localservices_16_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_localservices_17_GoogleTypeTimeZoneOut",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadIn": "_localservices_18_GoogleAdsHomeservicesLocalservicesV1MessageLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadOut": "_localservices_19_GoogleAdsHomeservicesLocalservicesV1MessageLeadOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "businessName": t.string().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"]
            ).optional(),
            "chargeStatus": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "leadId": t.string().optional(),
            "leadPrice": t.number().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "geo": t.string().optional(),
            "disputeStatus": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "leadCategory": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"]
            ).optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"]
            ).optional(),
            "leadType": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "businessName": t.string().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"]
            ).optional(),
            "chargeStatus": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "leadId": t.string().optional(),
            "leadPrice": t.number().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "geo": t.string().optional(),
            "disputeStatus": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "leadCategory": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"]
            ).optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"]
            ).optional(),
            "leadType": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"] = t.struct(
        {
            "previousPeriodTotalCost": t.number().optional(),
            "totalReview": t.integer().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "currencyCode": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "accountId": t.string().optional(),
            "businessName": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"] = t.struct(
        {
            "previousPeriodTotalCost": t.number().optional(),
            "totalReview": t.integer().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "currencyCode": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "accountId": t.string().optional(),
            "businessName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"] = t.struct(
        {
            "chargedConnectedCallDurationSeconds": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "chargedCallTimestamp": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"] = t.struct(
        {
            "chargedConnectedCallDurationSeconds": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "chargedCallTimestamp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"])
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn"
    ] = t.struct(
        {
            "detailedLeadReports": t.array(
                t.proxy(
                    renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn"
        ]
    )
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut"
    ] = t.struct(
        {
            "detailedLeadReports": t.array(
                t.proxy(
                    renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut"
        ]
    )
    types["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"] = t.struct(
        {"aggregatorProviderId": t.string().optional()}
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"] = t.struct(
        {
            "aggregatorProviderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"] = t.struct(
        {
            "customerName": t.string().optional(),
            "consumerEmail": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"] = t.struct(
        {
            "customerName": t.string().optional(),
            "consumerEmail": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"])
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accountReports": t.array(
                t.proxy(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn"]
    )
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accountReports": t.array(
                t.proxy(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut"]
    )
    types["GoogleTypeTimeZoneIn"] = t.struct(
        {"version": t.string().optional(), "id": t.string().optional()}
    ).named(renames["GoogleTypeTimeZoneIn"])
    types["GoogleTypeTimeZoneOut"] = t.struct(
        {
            "version": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeZoneOut"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"] = t.struct(
        {
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"] = t.struct(
        {
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"])

    functions = {}
    functions["detailedLeadReportsSearch"] = localservices.get(
        "v1/detailedLeadReports:search",
        t.struct(
            {
                "query": t.string().optional(),
                "endDate.year": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountReportsSearch"] = localservices.get(
        "v1/accountReports:search",
        t.struct(
            {
                "startDate.day": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="localservices", renames=renames, types=types, functions=functions
    )
