from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_playdeveloperreporting() -> Import:
    playdeveloperreporting = HTTPRuntime(
        "https://playdeveloperreporting.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_playdeveloperreporting_1_ErrorResponse",
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseIn": "_playdeveloperreporting_2_GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut": "_playdeveloperreporting_3_GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseIn": "_playdeveloperreporting_4_GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseIn",
        "GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseOut": "_playdeveloperreporting_5_GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseOut",
        "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetIn": "_playdeveloperreporting_6_GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetOut": "_playdeveloperreporting_7_GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestIn": "_playdeveloperreporting_8_GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestOut": "_playdeveloperreporting_9_GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessIn": "_playdeveloperreporting_10_GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessIn",
        "GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessOut": "_playdeveloperreporting_11_GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessOut",
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestIn": "_playdeveloperreporting_12_GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestOut": "_playdeveloperreporting_13_GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestIn": "_playdeveloperreporting_14_GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestOut": "_playdeveloperreporting_15_GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1AnomalyIn": "_playdeveloperreporting_16_GooglePlayDeveloperReportingV1beta1AnomalyIn",
        "GooglePlayDeveloperReportingV1beta1AnomalyOut": "_playdeveloperreporting_17_GooglePlayDeveloperReportingV1beta1AnomalyOut",
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestIn": "_playdeveloperreporting_18_GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestOut": "_playdeveloperreporting_19_GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1TimelineSpecIn": "_playdeveloperreporting_20_GooglePlayDeveloperReportingV1beta1TimelineSpecIn",
        "GooglePlayDeveloperReportingV1beta1TimelineSpecOut": "_playdeveloperreporting_21_GooglePlayDeveloperReportingV1beta1TimelineSpecOut",
        "GooglePlayDeveloperReportingV1beta1CrashRateMetricSetIn": "_playdeveloperreporting_22_GooglePlayDeveloperReportingV1beta1CrashRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut": "_playdeveloperreporting_23_GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestIn": "_playdeveloperreporting_24_GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestOut": "_playdeveloperreporting_25_GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseIn": "_playdeveloperreporting_26_GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseOut": "_playdeveloperreporting_27_GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1FreshnessInfoIn": "_playdeveloperreporting_28_GooglePlayDeveloperReportingV1beta1FreshnessInfoIn",
        "GooglePlayDeveloperReportingV1beta1FreshnessInfoOut": "_playdeveloperreporting_29_GooglePlayDeveloperReportingV1beta1FreshnessInfoOut",
        "GoogleTypeTimeZoneIn": "_playdeveloperreporting_30_GoogleTypeTimeZoneIn",
        "GoogleTypeTimeZoneOut": "_playdeveloperreporting_31_GoogleTypeTimeZoneOut",
        "GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseIn": "_playdeveloperreporting_32_GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseIn",
        "GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseOut": "_playdeveloperreporting_33_GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseOut",
        "GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseIn": "_playdeveloperreporting_34_GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseIn",
        "GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseOut": "_playdeveloperreporting_35_GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseOut",
        "GoogleTypeDateTimeIn": "_playdeveloperreporting_36_GoogleTypeDateTimeIn",
        "GoogleTypeDateTimeOut": "_playdeveloperreporting_37_GoogleTypeDateTimeOut",
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseIn": "_playdeveloperreporting_38_GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut": "_playdeveloperreporting_39_GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1AnrRateMetricSetIn": "_playdeveloperreporting_40_GooglePlayDeveloperReportingV1beta1AnrRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut": "_playdeveloperreporting_41_GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestIn": "_playdeveloperreporting_42_GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestOut": "_playdeveloperreporting_43_GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetIn": "_playdeveloperreporting_44_GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetOut": "_playdeveloperreporting_45_GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1DimensionValueIn": "_playdeveloperreporting_46_GooglePlayDeveloperReportingV1beta1DimensionValueIn",
        "GooglePlayDeveloperReportingV1beta1DimensionValueOut": "_playdeveloperreporting_47_GooglePlayDeveloperReportingV1beta1DimensionValueOut",
        "GooglePlayDeveloperReportingV1beta1MetricValueIn": "_playdeveloperreporting_48_GooglePlayDeveloperReportingV1beta1MetricValueIn",
        "GooglePlayDeveloperReportingV1beta1MetricValueOut": "_playdeveloperreporting_49_GooglePlayDeveloperReportingV1beta1MetricValueOut",
        "GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetIn": "_playdeveloperreporting_50_GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetOut": "_playdeveloperreporting_51_GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetOut",
        "GoogleTypeDecimalIn": "_playdeveloperreporting_52_GoogleTypeDecimalIn",
        "GoogleTypeDecimalOut": "_playdeveloperreporting_53_GoogleTypeDecimalOut",
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseIn": "_playdeveloperreporting_54_GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseOut": "_playdeveloperreporting_55_GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestIn": "_playdeveloperreporting_56_GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestIn",
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestOut": "_playdeveloperreporting_57_GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestOut",
        "GooglePlayDeveloperReportingV1beta1MetricsRowIn": "_playdeveloperreporting_58_GooglePlayDeveloperReportingV1beta1MetricsRowIn",
        "GooglePlayDeveloperReportingV1beta1MetricsRowOut": "_playdeveloperreporting_59_GooglePlayDeveloperReportingV1beta1MetricsRowOut",
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseIn": "_playdeveloperreporting_60_GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut": "_playdeveloperreporting_61_GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetIn": "_playdeveloperreporting_62_GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetOut": "_playdeveloperreporting_63_GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetIn": "_playdeveloperreporting_64_GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetIn",
        "GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetOut": "_playdeveloperreporting_65_GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetOut",
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseIn": "_playdeveloperreporting_66_GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut": "_playdeveloperreporting_67_GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1ErrorIssueIn": "_playdeveloperreporting_68_GooglePlayDeveloperReportingV1beta1ErrorIssueIn",
        "GooglePlayDeveloperReportingV1beta1ErrorIssueOut": "_playdeveloperreporting_69_GooglePlayDeveloperReportingV1beta1ErrorIssueOut",
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseIn": "_playdeveloperreporting_70_GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseIn",
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut": "_playdeveloperreporting_71_GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut",
        "GooglePlayDeveloperReportingV1beta1ErrorReportIn": "_playdeveloperreporting_72_GooglePlayDeveloperReportingV1beta1ErrorReportIn",
        "GooglePlayDeveloperReportingV1beta1ErrorReportOut": "_playdeveloperreporting_73_GooglePlayDeveloperReportingV1beta1ErrorReportOut",
        "GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalIn": "_playdeveloperreporting_74_GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalIn",
        "GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalOut": "_playdeveloperreporting_75_GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseIn"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "errorReports": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1ErrorReportIn"])
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseIn"])
    types[
        "GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "errorReports": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1ErrorReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseOut"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetIn"
    ] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetOut"
    ] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSetOut"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestIn"
    ] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestOut"
    ] = t.struct(
        {
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequestOut"]
    )
    types["GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessIn"] = t.struct(
        {
            "aggregationPeriod": t.string().optional(),
            "latestEndTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessIn"])
    types["GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessOut"] = t.struct(
        {
            "aggregationPeriod": t.string().optional(),
            "latestEndTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestIn"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "metrics": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequestOut"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestIn"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequestOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1AnomalyIn"] = t.struct(
        {
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "name": t.string().optional(),
            "metricSet": t.string().optional(),
            "metric": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1MetricValueIn"]
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1DimensionValueIn"])
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1AnomalyIn"])
    types["GooglePlayDeveloperReportingV1beta1AnomalyOut"] = t.struct(
        {
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "metricSet": t.string().optional(),
            "metric": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1MetricValueOut"]
            ).optional(),
            "dimensions": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1DimensionValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1AnomalyOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestIn"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "filter": t.string().optional(),
            "userCohort": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequestOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"] = t.struct(
        {
            "startTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "endTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "aggregationPeriod": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"])
    types["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"] = t.struct(
        {
            "startTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "endTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "aggregationPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"])
    types["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetIn"])
    types["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestIn"
    ] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userCohort": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "pageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestOut"
    ] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "userCohort": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "pageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequestOut"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponseOut"]
    )
    types["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"] = t.struct(
        {
            "freshnesses": t.array(
                t.proxy(
                    renames[
                        "GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"])
    types["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"] = t.struct(
        {
            "freshnesses": t.array(
                t.proxy(
                    renames[
                        "GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshnessOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"])
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
    types["GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseIn"] = t.struct(
        {
            "anomalies": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1AnomalyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseIn"])
    types["GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseOut"] = t.struct(
        {
            "anomalies": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1AnomalyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseOut"])
    types["GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseIn"] = t.struct(
        {
            "errorIssues": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1ErrorIssueIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseIn"])
    types["GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseOut"] = t.struct(
        {
            "errorIssues": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1ErrorIssueOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseOut"])
    types["GoogleTypeDateTimeIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneIn"]).optional(),
            "year": t.integer().optional(),
            "utcOffset": t.string().optional(),
        }
    ).named(renames["GoogleTypeDateTimeIn"])
    types["GoogleTypeDateTimeOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "timeZone": t.proxy(renames["GoogleTypeTimeZoneOut"]).optional(),
            "year": t.integer().optional(),
            "utcOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateTimeOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetIn"])
    types["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestIn"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "userCohort": t.string().optional(),
            "pageToken": t.string().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestOut"
    ] = t.struct(
        {
            "pageSize": t.integer().optional(),
            "userCohort": t.string().optional(),
            "pageToken": t.string().optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "filter": t.string().optional(),
            "dimensions": t.array(t.string()).optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequestOut"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetIn"
    ] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetOut"
    ] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSetOut"]
    )
    types["GooglePlayDeveloperReportingV1beta1DimensionValueIn"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "valueLabel": t.string().optional(),
            "stringValue": t.string().optional(),
            "dimension": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1DimensionValueIn"])
    types["GooglePlayDeveloperReportingV1beta1DimensionValueOut"] = t.struct(
        {
            "int64Value": t.string().optional(),
            "valueLabel": t.string().optional(),
            "stringValue": t.string().optional(),
            "dimension": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1DimensionValueOut"])
    types["GooglePlayDeveloperReportingV1beta1MetricValueIn"] = t.struct(
        {
            "decimalValueConfidenceInterval": t.proxy(
                renames[
                    "GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalIn"
                ]
            ).optional(),
            "decimalValue": t.proxy(renames["GoogleTypeDecimalIn"]).optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1MetricValueIn"])
    types["GooglePlayDeveloperReportingV1beta1MetricValueOut"] = t.struct(
        {
            "decimalValueConfidenceInterval": t.proxy(
                renames[
                    "GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalOut"
                ]
            ).optional(),
            "decimalValue": t.proxy(renames["GoogleTypeDecimalOut"]).optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1MetricValueOut"])
    types["GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetIn"])
    types["GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorCountMetricSetOut"])
    types["GoogleTypeDecimalIn"] = t.struct({"value": t.string().optional()}).named(
        renames["GoogleTypeDecimalIn"]
    )
    types["GoogleTypeDecimalOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDecimalOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponseOut"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestIn"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
            ).optional(),
            "userCohort": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestOut"
    ] = t.struct(
        {
            "pageToken": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "dimensions": t.array(t.string()).optional(),
            "timelineSpec": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1TimelineSpecOut"]
            ).optional(),
            "userCohort": t.string().optional(),
            "filter": t.string().optional(),
            "pageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequestOut"]
    )
    types["GooglePlayDeveloperReportingV1beta1MetricsRowIn"] = t.struct(
        {
            "aggregationPeriod": t.string().optional(),
            "startTime": t.proxy(renames["GoogleTypeDateTimeIn"]).optional(),
            "dimensions": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1DimensionValueIn"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricValueIn"])
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
    types["GooglePlayDeveloperReportingV1beta1MetricsRowOut"] = t.struct(
        {
            "aggregationPeriod": t.string().optional(),
            "startTime": t.proxy(renames["GoogleTypeDateTimeOut"]).optional(),
            "dimensions": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1DimensionValueOut"])
            ).optional(),
            "metrics": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricValueOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseIn"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseIn"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetIn"] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetIn"])
    types["GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetOut"] = t.struct(
        {
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSetOut"])
    types["GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetIn"] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoIn"]
            ).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetIn"])
    types[
        "GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetOut"
    ] = t.struct(
        {
            "name": t.string().optional(),
            "freshnessInfo": t.proxy(
                renames["GooglePlayDeveloperReportingV1beta1FreshnessInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSetOut"]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1ErrorIssueIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "cause": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorIssueIn"])
    types["GooglePlayDeveloperReportingV1beta1ErrorIssueOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "location": t.string().optional(),
            "cause": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorIssueOut"])
    types[
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseIn"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseIn"
        ]
    )
    types[
        "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut"
    ] = t.struct(
        {
            "rows": t.array(
                t.proxy(renames["GooglePlayDeveloperReportingV1beta1MetricsRowOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut"
        ]
    )
    types["GooglePlayDeveloperReportingV1beta1ErrorReportIn"] = t.struct(
        {
            "name": t.string().optional(),
            "reportText": t.string().optional(),
            "issue": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorReportIn"])
    types["GooglePlayDeveloperReportingV1beta1ErrorReportOut"] = t.struct(
        {
            "name": t.string().optional(),
            "reportText": t.string().optional(),
            "issue": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1ErrorReportOut"])
    types["GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalIn"] = t.struct(
        {
            "upperBound": t.proxy(renames["GoogleTypeDecimalIn"]).optional(),
            "lowerBound": t.proxy(renames["GoogleTypeDecimalIn"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalIn"])
    types["GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalOut"] = t.struct(
        {
            "upperBound": t.proxy(renames["GoogleTypeDecimalOut"]).optional(),
            "lowerBound": t.proxy(renames["GoogleTypeDecimalOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayDeveloperReportingV1beta1DecimalConfidenceIntervalOut"])

    functions = {}
    functions["anomaliesList"] = playdeveloperreporting.get(
        "v1beta1/{parent}/anomalies",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GooglePlayDeveloperReportingV1beta1ListAnomaliesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsErrorsReportsSearch"] = playdeveloperreporting.get(
        "v1beta1/{parent}/errorReports:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "interval.startTime.utcOffset": t.string().optional(),
                "interval.endTime.utcOffset": t.string().optional(),
                "interval.endTime.day": t.integer().optional(),
                "interval.startTime.day": t.integer().optional(),
                "interval.startTime.timeZone.id": t.string().optional(),
                "pageToken": t.string().optional(),
                "interval.startTime.month": t.integer().optional(),
                "interval.startTime.timeZone.version": t.string().optional(),
                "interval.endTime.seconds": t.integer().optional(),
                "interval.startTime.hours": t.integer().optional(),
                "interval.endTime.timeZone.id": t.string().optional(),
                "interval.endTime.month": t.integer().optional(),
                "parent": t.string(),
                "interval.endTime.minutes": t.integer().optional(),
                "interval.endTime.hours": t.integer().optional(),
                "interval.startTime.minutes": t.integer().optional(),
                "interval.endTime.year": t.integer().optional(),
                "interval.startTime.year": t.integer().optional(),
                "interval.startTime.seconds": t.integer().optional(),
                "filter": t.string().optional(),
                "interval.endTime.nanos": t.integer().optional(),
                "interval.startTime.nanos": t.integer().optional(),
                "interval.endTime.timeZone.version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsErrorsIssuesSearch"] = playdeveloperreporting.get(
        "v1beta1/{parent}/errorIssues:search",
        t.struct(
            {
                "interval.endTime.timeZone.version": t.string().optional(),
                "interval.endTime.nanos": t.integer().optional(),
                "interval.endTime.timeZone.id": t.string().optional(),
                "pageToken": t.string().optional(),
                "interval.startTime.hours": t.integer().optional(),
                "interval.endTime.month": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "interval.endTime.minutes": t.integer().optional(),
                "interval.endTime.utcOffset": t.string().optional(),
                "interval.startTime.day": t.integer().optional(),
                "pageSize": t.integer().optional(),
                "interval.endTime.year": t.integer().optional(),
                "interval.endTime.day": t.integer().optional(),
                "interval.startTime.year": t.integer().optional(),
                "interval.startTime.seconds": t.integer().optional(),
                "interval.startTime.timeZone.version": t.string().optional(),
                "interval.startTime.minutes": t.integer().optional(),
                "interval.startTime.nanos": t.integer().optional(),
                "interval.startTime.utcOffset": t.string().optional(),
                "interval.endTime.hours": t.integer().optional(),
                "interval.startTime.month": t.integer().optional(),
                "interval.endTime.seconds": t.integer().optional(),
                "interval.startTime.timeZone.id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsErrorsCountsGet"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "metrics": t.array(t.string()).optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsErrorsCountsQuery"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "dimensions": t.array(t.string()).optional(),
                "metrics": t.array(t.string()).optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsStuckbackgroundwakelockrateGet"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "metrics": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userCohort": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsStuckbackgroundwakelockrateQuery"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "metrics": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userCohort": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsSlowstartrateGet"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "dimensions": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsSlowstartrateQuery"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "dimensions": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsSlowrenderingrateGet"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsSlowrenderingrateQuery"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "metrics": t.array(t.string()).optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsAnrrateQuery"] = playdeveloperreporting.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsAnrrateGet"] = playdeveloperreporting.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePlayDeveloperReportingV1beta1AnrRateMetricSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsExcessivewakeuprateGet"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "metrics": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsExcessivewakeuprateQuery"] = playdeveloperreporting.post(
        "v1beta1/{name}:query",
        t.struct(
            {
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "timelineSpec": t.proxy(
                    renames["GooglePlayDeveloperReportingV1beta1TimelineSpecIn"]
                ).optional(),
                "metrics": t.array(t.string()).optional(),
                "pageToken": t.string().optional(),
                "dimensions": t.array(t.string()).optional(),
                "filter": t.string().optional(),
                "userCohort": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsCrashrateQuery"] = playdeveloperreporting.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["vitalsCrashrateGet"] = playdeveloperreporting.get(
        "v1beta1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GooglePlayDeveloperReportingV1beta1CrashRateMetricSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="playdeveloperreporting",
        renames=renames,
        types=types,
        functions=functions,
    )
