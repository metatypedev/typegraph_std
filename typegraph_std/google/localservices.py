from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_localservices():
    localservices = HTTPRuntime("https://localservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_localservices_1_ErrorResponse",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn": "_localservices_2_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut": "_localservices_3_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut",
        "GoogleTypeTimeZoneIn": "_localservices_4_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_localservices_5_GoogleTypeTimeZoneOut",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn": "_localservices_6_GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut": "_localservices_7_GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadIn": "_localservices_8_GoogleAdsHomeservicesLocalservicesV1MessageLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadOut": "_localservices_9_GoogleAdsHomeservicesLocalservicesV1MessageLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn": "_localservices_10_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut": "_localservices_11_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn": "_localservices_12_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut": "_localservices_13_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadIn": "_localservices_14_GoogleAdsHomeservicesLocalservicesV1BookingLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadOut": "_localservices_15_GoogleAdsHomeservicesLocalservicesV1BookingLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn": "_localservices_16_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut": "_localservices_17_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportIn": "_localservices_18_GoogleAdsHomeservicesLocalservicesV1AccountReportIn",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportOut": "_localservices_19_GoogleAdsHomeservicesLocalservicesV1AccountReportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"] = t.struct(
        {
            "chargedCallTimestamp": t.string().optional(),
            "chargedConnectedCallDurationSeconds": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"] = t.struct(
        {
            "chargedCallTimestamp": t.string().optional(),
            "chargedConnectedCallDurationSeconds": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"] = t.struct(
        {
            "consumerPhoneNumber": t.string().optional(),
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "jobType": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"] = t.struct(
        {
            "consumerPhoneNumber": t.string().optional(),
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"])
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
            "consumerPhoneNumber": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "jobType": t.string().optional(),
            "consumerEmail": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"] = t.struct(
        {
            "customerName": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "jobType": t.string().optional(),
            "consumerEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"] = t.struct(
        {
            "timezone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"]
            ).optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"]
            ).optional(),
            "leadId": t.string().optional(),
            "geo": t.string().optional(),
            "businessName": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"]
            ).optional(),
            "leadPrice": t.number().optional(),
            "disputeStatus": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "leadCategory": t.string().optional(),
            "accountId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "leadType": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "chargeStatus": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"] = t.struct(
        {
            "timezone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"]
            ).optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"]
            ).optional(),
            "leadId": t.string().optional(),
            "geo": t.string().optional(),
            "businessName": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"]
            ).optional(),
            "leadPrice": t.number().optional(),
            "disputeStatus": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "leadCategory": t.string().optional(),
            "accountId": t.string().optional(),
            "currencyCode": t.string().optional(),
            "leadType": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "chargeStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"] = t.struct(
        {
            "averageFiveStarRating": t.number().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "currencyCode": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "totalReview": t.integer().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "accountId": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "businessName": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"] = t.struct(
        {
            "averageFiveStarRating": t.number().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "currencyCode": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "totalReview": t.integer().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "accountId": t.string().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "businessName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])

    functions = {}
    functions["detailedLeadReportsSearch"] = localservices.get(
        "v1/detailedLeadReports:search",
        t.struct(
            {
                "endDate.day": t.integer().optional(),
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "query": t.string().optional(),
                "endDate.month": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
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
                "startDate.year": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "pageToken": t.string().optional(),
                "startDate.month": t.integer().optional(),
                "query": t.string().optional(),
                "endDate.day": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "pageSize": t.integer().optional(),
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
