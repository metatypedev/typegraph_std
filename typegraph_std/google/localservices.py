from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_localservices() -> Import:
    localservices = HTTPRuntime("https://localservices.googleapis.com/")

    renames = {
        "ErrorResponse": "_localservices_1_ErrorResponse",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn": "_localservices_2_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn",
        "GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut": "_localservices_3_GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportIn": "_localservices_4_GoogleAdsHomeservicesLocalservicesV1AccountReportIn",
        "GoogleAdsHomeservicesLocalservicesV1AccountReportOut": "_localservices_5_GoogleAdsHomeservicesLocalservicesV1AccountReportOut",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadIn": "_localservices_6_GoogleAdsHomeservicesLocalservicesV1BookingLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1BookingLeadOut": "_localservices_7_GoogleAdsHomeservicesLocalservicesV1BookingLeadOut",
        "GoogleTypeTimeZoneIn": "_localservices_8_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_localservices_9_GoogleTypeTimeZoneOut",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadIn": "_localservices_10_GoogleAdsHomeservicesLocalservicesV1MessageLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1MessageLeadOut": "_localservices_11_GoogleAdsHomeservicesLocalservicesV1MessageLeadOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn": "_localservices_12_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut": "_localservices_13_GoogleAdsHomeservicesLocalservicesV1SearchAccountReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn": "_localservices_14_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn",
        "GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut": "_localservices_15_GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn": "_localservices_16_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseIn",
        "GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut": "_localservices_17_GoogleAdsHomeservicesLocalservicesV1SearchDetailedLeadReportsResponseOut",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn": "_localservices_18_GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn",
        "GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut": "_localservices_19_GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"] = t.struct(
        {
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "geo": t.string().optional(),
            "leadCategory": t.string().optional(),
            "currencyCode": t.string().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "disputeStatus": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"]
            ).optional(),
            "leadType": t.string().optional(),
            "businessName": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "chargeStatus": t.string().optional(),
            "leadPrice": t.number().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"]
            ).optional(),
            "leadId": t.string().optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"]
            ).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"] = t.struct(
        {
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "geo": t.string().optional(),
            "leadCategory": t.string().optional(),
            "currencyCode": t.string().optional(),
            "timezone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "disputeStatus": t.string().optional(),
            "phoneLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"]
            ).optional(),
            "leadType": t.string().optional(),
            "businessName": t.string().optional(),
            "leadCreationTimestamp": t.string().optional(),
            "chargeStatus": t.string().optional(),
            "leadPrice": t.number().optional(),
            "bookingLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"]
            ).optional(),
            "leadId": t.string().optional(),
            "messageLead": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"]
            ).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1DetailedLeadReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"] = t.struct(
        {
            "businessName": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoIn"]
            ).optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
            "currencyCode": t.string().optional(),
            "accountId": t.string().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "totalReview": t.integer().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportIn"])
    types["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"] = t.struct(
        {
            "businessName": t.string().optional(),
            "currentPeriodTotalCost": t.number().optional(),
            "phoneLeadResponsiveness": t.number().optional(),
            "aggregatorInfo": t.proxy(
                renames["GoogleAdsHomeservicesLocalservicesV1AggregatorInfoOut"]
            ).optional(),
            "currentPeriodConnectedPhoneCalls": t.string().optional(),
            "averageWeeklyBudget": t.number().optional(),
            "currentPeriodChargedLeads": t.string().optional(),
            "currentPeriodPhoneCalls": t.string().optional(),
            "previousPeriodPhoneCalls": t.string().optional(),
            "previousPeriodTotalCost": t.number().optional(),
            "previousPeriodChargedLeads": t.string().optional(),
            "averageFiveStarRating": t.number().optional(),
            "currencyCode": t.string().optional(),
            "accountId": t.string().optional(),
            "impressionsLastTwoDays": t.string().optional(),
            "previousPeriodConnectedPhoneCalls": t.string().optional(),
            "totalReview": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1AccountReportOut"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"] = t.struct(
        {
            "consumerEmail": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
            "customerName": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"] = t.struct(
        {
            "consumerEmail": t.string().optional(),
            "bookingAppointmentTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "jobType": t.string().optional(),
            "customerName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1BookingLeadOut"])
    types["GoogleTypeTimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "version": t.string().optional()}
    ).named(renames["GoogleTypeTimeZoneIn"])
    types["GoogleTypeTimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeTimeZoneOut"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"] = t.struct(
        {
            "jobType": t.string().optional(),
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1MessageLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1MessageLeadOut"] = t.struct(
        {
            "jobType": t.string().optional(),
            "customerName": t.string().optional(),
            "postalCode": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
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
            "chargedCallTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "chargedConnectedCallDurationSeconds": t.string().optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadIn"])
    types["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"] = t.struct(
        {
            "chargedCallTimestamp": t.string().optional(),
            "consumerPhoneNumber": t.string().optional(),
            "chargedConnectedCallDurationSeconds": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAdsHomeservicesLocalservicesV1PhoneLeadOut"])

    functions = {}
    functions["detailedLeadReportsSearch"] = localservices.get(
        "v1/detailedLeadReports:search",
        t.struct(
            {
                "endDate.month": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "startDate.day": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
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
                "startDate.day": t.integer().optional(),
                "startDate.year": t.integer().optional(),
                "startDate.month": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
                "endDate.month": t.integer().optional(),
                "endDate.year": t.integer().optional(),
                "endDate.day": t.integer().optional(),
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
