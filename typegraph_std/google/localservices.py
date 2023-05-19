from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_localservices() -> Import:
    localservices = HTTPRuntime("https://localservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_localservices_1_ErrorResponse",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn": "_localservices_2_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut": "_localservices_3_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn": "_localservices_4_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut": "_localservices_5_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn": "_localservices_6_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut": "_localservices_7_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn": "_localservices_8_GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut": "_localservices_9_GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadIn": "_localservices_10_GoogleAdsHomeservicesLocalservicesV1BookingLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadOut": "_localservices_11_GoogleAdsHomeservicesLocalservicesV1BookingLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadIn": "_localservices_12_GoogleAdsHomeservicesLocalservicesV1MessageLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadOut": "_localservices_13_GoogleAdsHomeservicesLocalservicesV1MessageLeadOut",
        "GoogleTypeTimeZoneIn": "_localservices_14_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_localservices_15_GoogleTypeTimeZoneOut",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn": "_localservices_16_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut": "_localservices_17_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportIn": "_localservices_18_GoogleAdsHomeservicesLocalservicesV1AccountReportIn",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportOut": "_localservices_19_GoogleAdsHomeservicesLocalservicesV1AccountReportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"] = t.struct(
        {"aggregatorProviderId": t.string().optional()}
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"] = t.struct(
        {
            "aggregatorProviderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"])
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn"
    ] = t.struct(
        {
            "accountReports": t.array(
                t.proxy(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn"]
    )
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut"
    ] = t.struct(
        {
            "accountReports": t.array(
                t.proxy(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut"]
    )
    types[
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "detailedLeadReports": t.array(
                t.proxy(
                    renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"]
                )
            ).optional(),
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
            "nextPageToken": t.string().optional(),
            "detailedLeadReports": t.array(
                t.proxy(
                    renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut"
        ]
    )
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
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"] = t.struct(
        {
            "consumerPhoneNumber": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "customerName": t.string().optional(),
            "jobType": t.string().optional(),
            "consumerEmail": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"] = t.struct(
        {
            "consumerPhoneNumber": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "customerName": t.string().optional(),
            "jobType": t.string().optional(),
            "consumerEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"] = t.struct(
        {
            "jobType": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "postalCode": t.string().optional(),
            "customerName": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"] = t.struct(
        {
            "jobType": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "postalCode": t.string().optional(),
            "customerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"])
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
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"] = t.struct(
        {
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"]
            ).optional(),
            "chargeStatus": t.string().optional(),
            "currencyCode": t.string().optional(),
            "leadId": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "accountId": t.string().optional(),
            "leadType": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"]
            ).optional(),
            "geo": t.string().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"]
            ).optional(),
            "businessName": t.string().optional(),
            "leadPrice": t.number().optional(),
            "leadCategory": t.string().optional(),
            "disputeStatus": t.string().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"] = t.struct(
        {
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"]
            ).optional(),
            "chargeStatus": t.string().optional(),
            "currencyCode": t.string().optional(),
            "leadId": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "leadType": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"]
            ).optional(),
            "geo": t.string().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"]
            ).optional(),
            "businessName": t.string().optional(),
            "leadPrice": t.number().optional(),
            "leadCategory": t.string().optional(),
            "disputeStatus": t.string().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"] = t.struct(
        {
            "totalReview": t.integer().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "businessName": t.string().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "accountId": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"] = t.struct(
        {
            "totalReview": t.integer().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "currencyCode": t.string().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "businessName": t.string().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "accountId": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])

    functions = {}
    functions["detailedLeadReportsSearch"] = localservices.get(
        "v1/detailedLeadReports:search",
        t.struct(
            {
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "endDate.day": t.integer().optional(),
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
                "endDate.month": t.integer().optional(),
                "endDate.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
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
        importer="localservices",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
