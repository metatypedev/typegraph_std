from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_recommender():
    recommender = HTTPRuntime("https://recommender.googleapis.com/")

    renames = {
        "ErrorResponse": "_recommender_1_ErrorResponse",
        "GoogleCloudRecommenderV1RecommenderGenerationConfigIn": "_recommender_2_GoogleCloudRecommenderV1RecommenderGenerationConfigIn",
        "GoogleCloudRecommenderV1RecommenderGenerationConfigOut": "_recommender_3_GoogleCloudRecommenderV1RecommenderGenerationConfigOut",
        "GoogleCloudRecommenderV1ListInsightsResponseIn": "_recommender_4_GoogleCloudRecommenderV1ListInsightsResponseIn",
        "GoogleCloudRecommenderV1ListInsightsResponseOut": "_recommender_5_GoogleCloudRecommenderV1ListInsightsResponseOut",
        "GoogleTypeMoneyIn": "_recommender_6_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_recommender_7_GoogleTypeMoneyOut",
        "GoogleCloudRecommenderV1OperationIn": "_recommender_8_GoogleCloudRecommenderV1OperationIn",
        "GoogleCloudRecommenderV1OperationOut": "_recommender_9_GoogleCloudRecommenderV1OperationOut",
        "GoogleCloudRecommenderV1CostProjectionIn": "_recommender_10_GoogleCloudRecommenderV1CostProjectionIn",
        "GoogleCloudRecommenderV1CostProjectionOut": "_recommender_11_GoogleCloudRecommenderV1CostProjectionOut",
        "GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn": "_recommender_12_GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut": "_recommender_13_GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut",
        "GoogleCloudRecommenderV1InsightStateInfoIn": "_recommender_14_GoogleCloudRecommenderV1InsightStateInfoIn",
        "GoogleCloudRecommenderV1InsightStateInfoOut": "_recommender_15_GoogleCloudRecommenderV1InsightStateInfoOut",
        "GoogleCloudRecommenderV1ValueMatcherIn": "_recommender_16_GoogleCloudRecommenderV1ValueMatcherIn",
        "GoogleCloudRecommenderV1ValueMatcherOut": "_recommender_17_GoogleCloudRecommenderV1ValueMatcherOut",
        "GoogleCloudRecommenderV1InsightRecommendationReferenceIn": "_recommender_18_GoogleCloudRecommenderV1InsightRecommendationReferenceIn",
        "GoogleCloudRecommenderV1InsightRecommendationReferenceOut": "_recommender_19_GoogleCloudRecommenderV1InsightRecommendationReferenceOut",
        "GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn": "_recommender_20_GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut": "_recommender_21_GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut",
        "GoogleCloudRecommenderV1ListRecommendationsResponseIn": "_recommender_22_GoogleCloudRecommenderV1ListRecommendationsResponseIn",
        "GoogleCloudRecommenderV1ListRecommendationsResponseOut": "_recommender_23_GoogleCloudRecommenderV1ListRecommendationsResponseOut",
        "GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn": "_recommender_24_GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut": "_recommender_25_GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut",
        "GoogleCloudRecommenderV1InsightTypeGenerationConfigIn": "_recommender_26_GoogleCloudRecommenderV1InsightTypeGenerationConfigIn",
        "GoogleCloudRecommenderV1InsightTypeGenerationConfigOut": "_recommender_27_GoogleCloudRecommenderV1InsightTypeGenerationConfigOut",
        "GoogleCloudRecommenderV1InsightTypeConfigIn": "_recommender_28_GoogleCloudRecommenderV1InsightTypeConfigIn",
        "GoogleCloudRecommenderV1InsightTypeConfigOut": "_recommender_29_GoogleCloudRecommenderV1InsightTypeConfigOut",
        "GoogleCloudRecommenderV1RecommendationInsightReferenceIn": "_recommender_30_GoogleCloudRecommenderV1RecommendationInsightReferenceIn",
        "GoogleCloudRecommenderV1RecommendationInsightReferenceOut": "_recommender_31_GoogleCloudRecommenderV1RecommendationInsightReferenceOut",
        "GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn": "_recommender_32_GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn",
        "GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut": "_recommender_33_GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut",
        "GoogleCloudRecommenderV1InsightIn": "_recommender_34_GoogleCloudRecommenderV1InsightIn",
        "GoogleCloudRecommenderV1InsightOut": "_recommender_35_GoogleCloudRecommenderV1InsightOut",
        "GoogleCloudRecommenderV1RecommendationIn": "_recommender_36_GoogleCloudRecommenderV1RecommendationIn",
        "GoogleCloudRecommenderV1RecommendationOut": "_recommender_37_GoogleCloudRecommenderV1RecommendationOut",
        "GoogleCloudRecommenderV1RecommendationContentIn": "_recommender_38_GoogleCloudRecommenderV1RecommendationContentIn",
        "GoogleCloudRecommenderV1RecommendationContentOut": "_recommender_39_GoogleCloudRecommenderV1RecommendationContentOut",
        "GoogleCloudRecommenderV1ImpactIn": "_recommender_40_GoogleCloudRecommenderV1ImpactIn",
        "GoogleCloudRecommenderV1ImpactOut": "_recommender_41_GoogleCloudRecommenderV1ImpactOut",
        "GoogleCloudRecommenderV1RecommenderConfigIn": "_recommender_42_GoogleCloudRecommenderV1RecommenderConfigIn",
        "GoogleCloudRecommenderV1RecommenderConfigOut": "_recommender_43_GoogleCloudRecommenderV1RecommenderConfigOut",
        "GoogleCloudRecommenderV1RecommendationStateInfoIn": "_recommender_44_GoogleCloudRecommenderV1RecommendationStateInfoIn",
        "GoogleCloudRecommenderV1RecommendationStateInfoOut": "_recommender_45_GoogleCloudRecommenderV1RecommendationStateInfoOut",
        "GoogleCloudRecommenderV1SecurityProjectionIn": "_recommender_46_GoogleCloudRecommenderV1SecurityProjectionIn",
        "GoogleCloudRecommenderV1SecurityProjectionOut": "_recommender_47_GoogleCloudRecommenderV1SecurityProjectionOut",
        "GoogleCloudRecommenderV1ReliabilityProjectionIn": "_recommender_48_GoogleCloudRecommenderV1ReliabilityProjectionIn",
        "GoogleCloudRecommenderV1ReliabilityProjectionOut": "_recommender_49_GoogleCloudRecommenderV1ReliabilityProjectionOut",
        "GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn": "_recommender_50_GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut": "_recommender_51_GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut",
        "GoogleCloudRecommenderV1OperationGroupIn": "_recommender_52_GoogleCloudRecommenderV1OperationGroupIn",
        "GoogleCloudRecommenderV1OperationGroupOut": "_recommender_53_GoogleCloudRecommenderV1OperationGroupOut",
        "GoogleCloudRecommenderV1SustainabilityProjectionIn": "_recommender_54_GoogleCloudRecommenderV1SustainabilityProjectionIn",
        "GoogleCloudRecommenderV1SustainabilityProjectionOut": "_recommender_55_GoogleCloudRecommenderV1SustainabilityProjectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"])
    types["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"])
    types["GoogleCloudRecommenderV1ListInsightsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "insights": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1InsightIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListInsightsResponseIn"])
    types["GoogleCloudRecommenderV1ListInsightsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "insights": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1InsightOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleCloudRecommenderV1OperationIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "valueMatcher": t.proxy(
                renames["GoogleCloudRecommenderV1ValueMatcherIn"]
            ).optional(),
            "sourceResource": t.string().optional(),
            "pathFilters": t.struct({"_": t.string().optional()}).optional(),
            "sourcePath": t.string().optional(),
            "pathValueMatchers": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1OperationIn"])
    types["GoogleCloudRecommenderV1OperationOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceType": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "valueMatcher": t.proxy(
                renames["GoogleCloudRecommenderV1ValueMatcherOut"]
            ).optional(),
            "sourceResource": t.string().optional(),
            "pathFilters": t.struct({"_": t.string().optional()}).optional(),
            "sourcePath": t.string().optional(),
            "pathValueMatchers": t.struct({"_": t.string().optional()}).optional(),
            "action": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1OperationOut"])
    types["GoogleCloudRecommenderV1CostProjectionIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "cost": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1CostProjectionIn"])
    types["GoogleCloudRecommenderV1CostProjectionOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "cost": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1CostProjectionOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut"])
    types["GoogleCloudRecommenderV1InsightStateInfoIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightStateInfoIn"])
    types["GoogleCloudRecommenderV1InsightStateInfoOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightStateInfoOut"])
    types["GoogleCloudRecommenderV1ValueMatcherIn"] = t.struct(
        {"matchesPattern": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1ValueMatcherIn"])
    types["GoogleCloudRecommenderV1ValueMatcherOut"] = t.struct(
        {
            "matchesPattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ValueMatcherOut"])
    types["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"] = t.struct(
        {"recommendation": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"])
    types["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"] = t.struct(
        {
            "recommendation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut"])
    types["GoogleCloudRecommenderV1ListRecommendationsResponseIn"] = t.struct(
        {
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1RecommendationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListRecommendationsResponseIn"])
    types["GoogleCloudRecommenderV1ListRecommendationsResponseOut"] = t.struct(
        {
            "recommendations": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListRecommendationsResponseOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut"])
    types["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"])
    types["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"])
    types["GoogleCloudRecommenderV1InsightTypeConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "insightTypeGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeConfigIn"])
    types["GoogleCloudRecommenderV1InsightTypeConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "insightTypeGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"]
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "revisionId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"])
    types["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"] = t.struct(
        {"insight": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"])
    types["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"] = t.struct(
        {
            "insight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"])
    types["GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn"])
    types["GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut"])
    types["GoogleCloudRecommenderV1InsightIn"] = t.struct(
        {
            "category": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "associatedRecommendations": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"]
                )
            ).optional(),
            "content": t.struct({"_": t.string().optional()}).optional(),
            "observationPeriod": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "insightSubtype": t.string().optional(),
            "severity": t.string().optional(),
            "targetResources": t.array(t.string()).optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1InsightStateInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightIn"])
    types["GoogleCloudRecommenderV1InsightOut"] = t.struct(
        {
            "category": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "associatedRecommendations": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"]
                )
            ).optional(),
            "content": t.struct({"_": t.string().optional()}).optional(),
            "observationPeriod": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "insightSubtype": t.string().optional(),
            "severity": t.string().optional(),
            "targetResources": t.array(t.string()).optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1InsightStateInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightOut"])
    types["GoogleCloudRecommenderV1RecommendationIn"] = t.struct(
        {
            "priority": t.string().optional(),
            "primaryImpact": t.proxy(
                renames["GoogleCloudRecommenderV1ImpactIn"]
            ).optional(),
            "recommenderSubtype": t.string().optional(),
            "additionalImpact": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1ImpactIn"])
            ).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "associatedInsights": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"]
                )
            ).optional(),
            "xorGroupId": t.string().optional(),
            "content": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationContentIn"]
            ).optional(),
            "name": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationStateInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationIn"])
    types["GoogleCloudRecommenderV1RecommendationOut"] = t.struct(
        {
            "priority": t.string().optional(),
            "primaryImpact": t.proxy(
                renames["GoogleCloudRecommenderV1ImpactOut"]
            ).optional(),
            "recommenderSubtype": t.string().optional(),
            "additionalImpact": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1ImpactOut"])
            ).optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "associatedInsights": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"]
                )
            ).optional(),
            "xorGroupId": t.string().optional(),
            "content": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationContentOut"]
            ).optional(),
            "name": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationStateInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationOut"])
    types["GoogleCloudRecommenderV1RecommendationContentIn"] = t.struct(
        {
            "operationGroups": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationGroupIn"])
            ).optional(),
            "overview": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationContentIn"])
    types["GoogleCloudRecommenderV1RecommendationContentOut"] = t.struct(
        {
            "operationGroups": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationGroupOut"])
            ).optional(),
            "overview": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationContentOut"])
    types["GoogleCloudRecommenderV1ImpactIn"] = t.struct(
        {
            "sustainabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SustainabilityProjectionIn"]
            ).optional(),
            "reliabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1ReliabilityProjectionIn"]
            ).optional(),
            "category": t.string().optional(),
            "costProjection": t.proxy(
                renames["GoogleCloudRecommenderV1CostProjectionIn"]
            ).optional(),
            "securityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SecurityProjectionIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ImpactIn"])
    types["GoogleCloudRecommenderV1ImpactOut"] = t.struct(
        {
            "sustainabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SustainabilityProjectionOut"]
            ).optional(),
            "reliabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1ReliabilityProjectionOut"]
            ).optional(),
            "category": t.string().optional(),
            "costProjection": t.proxy(
                renames["GoogleCloudRecommenderV1CostProjectionOut"]
            ).optional(),
            "securityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SecurityProjectionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ImpactOut"])
    types["GoogleCloudRecommenderV1RecommenderConfigIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "recommenderGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderConfigIn"])
    types["GoogleCloudRecommenderV1RecommenderConfigOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "recommenderGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"]
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderConfigOut"])
    types["GoogleCloudRecommenderV1RecommendationStateInfoIn"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationStateInfoIn"])
    types["GoogleCloudRecommenderV1RecommendationStateInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationStateInfoOut"])
    types["GoogleCloudRecommenderV1SecurityProjectionIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1SecurityProjectionIn"])
    types["GoogleCloudRecommenderV1SecurityProjectionOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1SecurityProjectionOut"])
    types["GoogleCloudRecommenderV1ReliabilityProjectionIn"] = t.struct(
        {
            "risks": t.array(t.string()).optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ReliabilityProjectionIn"])
    types["GoogleCloudRecommenderV1ReliabilityProjectionOut"] = t.struct(
        {
            "risks": t.array(t.string()).optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ReliabilityProjectionOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut"])
    types["GoogleCloudRecommenderV1OperationGroupIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationIn"])
            ).optional()
        }
    ).named(renames["GoogleCloudRecommenderV1OperationGroupIn"])
    types["GoogleCloudRecommenderV1OperationGroupOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1OperationGroupOut"])
    types["GoogleCloudRecommenderV1SustainabilityProjectionIn"] = t.struct(
        {"duration": t.string().optional(), "kgCO2e": t.number().optional()}
    ).named(renames["GoogleCloudRecommenderV1SustainabilityProjectionIn"])
    types["GoogleCloudRecommenderV1SustainabilityProjectionOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "kgCO2e": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1SustainabilityProjectionOut"])

    functions = {}
    functions["projectsLocationsInsightTypesGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsMarkAccepted"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersUpdateConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersGetConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRecommendersRecommendationsMarkSucceeded"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersRecommendationsGet"] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersRecommendationsList"] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "updateTime": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsInsightTypesInsightsMarkAccepted"
    ] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsRecommendersUpdateConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsRecommendersGetConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsList"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsMarkSucceeded"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsGet"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.post(
        "v1/{name}:markDismissed",
        t.struct(
            {
                "name": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsRecommendersGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsRecommendersUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsGet"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsMarkSucceeded"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsList"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.post(
        "v1/{name}:markFailed",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesUpdateConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesGetConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsInsightTypesInsightsMarkAccepted"
    ] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsRecommendersRecommendationsList"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersLocationsRecommendersRecommendationsMarkSucceeded"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "foldersLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsRecommendersRecommendationsGet"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsInsightTypesInsightsMarkAccepted"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recommender",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
