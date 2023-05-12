from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_recommender() -> Import:
    recommender = HTTPRuntime("https://recommender.googleapis.com/")

    renames = {
        "ErrorResponse": "_recommender_1_ErrorResponse",
        "GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn": "_recommender_2_GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut": "_recommender_3_GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut",
        "GoogleCloudRecommenderV1ReliabilityProjectionIn": "_recommender_4_GoogleCloudRecommenderV1ReliabilityProjectionIn",
        "GoogleCloudRecommenderV1ReliabilityProjectionOut": "_recommender_5_GoogleCloudRecommenderV1ReliabilityProjectionOut",
        "GoogleCloudRecommenderV1CostProjectionIn": "_recommender_6_GoogleCloudRecommenderV1CostProjectionIn",
        "GoogleCloudRecommenderV1CostProjectionOut": "_recommender_7_GoogleCloudRecommenderV1CostProjectionOut",
        "GoogleCloudRecommenderV1OperationIn": "_recommender_8_GoogleCloudRecommenderV1OperationIn",
        "GoogleCloudRecommenderV1OperationOut": "_recommender_9_GoogleCloudRecommenderV1OperationOut",
        "GoogleCloudRecommenderV1ListRecommendationsResponseIn": "_recommender_10_GoogleCloudRecommenderV1ListRecommendationsResponseIn",
        "GoogleCloudRecommenderV1ListRecommendationsResponseOut": "_recommender_11_GoogleCloudRecommenderV1ListRecommendationsResponseOut",
        "GoogleCloudRecommenderV1OperationGroupIn": "_recommender_12_GoogleCloudRecommenderV1OperationGroupIn",
        "GoogleCloudRecommenderV1OperationGroupOut": "_recommender_13_GoogleCloudRecommenderV1OperationGroupOut",
        "GoogleCloudRecommenderV1InsightRecommendationReferenceIn": "_recommender_14_GoogleCloudRecommenderV1InsightRecommendationReferenceIn",
        "GoogleCloudRecommenderV1InsightRecommendationReferenceOut": "_recommender_15_GoogleCloudRecommenderV1InsightRecommendationReferenceOut",
        "GoogleCloudRecommenderV1InsightTypeConfigIn": "_recommender_16_GoogleCloudRecommenderV1InsightTypeConfigIn",
        "GoogleCloudRecommenderV1InsightTypeConfigOut": "_recommender_17_GoogleCloudRecommenderV1InsightTypeConfigOut",
        "GoogleCloudRecommenderV1InsightStateInfoIn": "_recommender_18_GoogleCloudRecommenderV1InsightStateInfoIn",
        "GoogleCloudRecommenderV1InsightStateInfoOut": "_recommender_19_GoogleCloudRecommenderV1InsightStateInfoOut",
        "GoogleCloudRecommenderV1SecurityProjectionIn": "_recommender_20_GoogleCloudRecommenderV1SecurityProjectionIn",
        "GoogleCloudRecommenderV1SecurityProjectionOut": "_recommender_21_GoogleCloudRecommenderV1SecurityProjectionOut",
        "GoogleCloudRecommenderV1RecommenderConfigIn": "_recommender_22_GoogleCloudRecommenderV1RecommenderConfigIn",
        "GoogleCloudRecommenderV1RecommenderConfigOut": "_recommender_23_GoogleCloudRecommenderV1RecommenderConfigOut",
        "GoogleCloudRecommenderV1InsightIn": "_recommender_24_GoogleCloudRecommenderV1InsightIn",
        "GoogleCloudRecommenderV1InsightOut": "_recommender_25_GoogleCloudRecommenderV1InsightOut",
        "GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn": "_recommender_26_GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut": "_recommender_27_GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut",
        "GoogleCloudRecommenderV1RecommenderGenerationConfigIn": "_recommender_28_GoogleCloudRecommenderV1RecommenderGenerationConfigIn",
        "GoogleCloudRecommenderV1RecommenderGenerationConfigOut": "_recommender_29_GoogleCloudRecommenderV1RecommenderGenerationConfigOut",
        "GoogleCloudRecommenderV1RecommendationContentIn": "_recommender_30_GoogleCloudRecommenderV1RecommendationContentIn",
        "GoogleCloudRecommenderV1RecommendationContentOut": "_recommender_31_GoogleCloudRecommenderV1RecommendationContentOut",
        "GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn": "_recommender_32_GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut": "_recommender_33_GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut",
        "GoogleCloudRecommenderV1InsightTypeGenerationConfigIn": "_recommender_34_GoogleCloudRecommenderV1InsightTypeGenerationConfigIn",
        "GoogleCloudRecommenderV1InsightTypeGenerationConfigOut": "_recommender_35_GoogleCloudRecommenderV1InsightTypeGenerationConfigOut",
        "GoogleCloudRecommenderV1RecommendationInsightReferenceIn": "_recommender_36_GoogleCloudRecommenderV1RecommendationInsightReferenceIn",
        "GoogleCloudRecommenderV1RecommendationInsightReferenceOut": "_recommender_37_GoogleCloudRecommenderV1RecommendationInsightReferenceOut",
        "GoogleCloudRecommenderV1ValueMatcherIn": "_recommender_38_GoogleCloudRecommenderV1ValueMatcherIn",
        "GoogleCloudRecommenderV1ValueMatcherOut": "_recommender_39_GoogleCloudRecommenderV1ValueMatcherOut",
        "GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn": "_recommender_40_GoogleCloudRecommenderV1MarkInsightAcceptedRequestIn",
        "GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut": "_recommender_41_GoogleCloudRecommenderV1MarkInsightAcceptedRequestOut",
        "GoogleCloudRecommenderV1RecommendationStateInfoIn": "_recommender_42_GoogleCloudRecommenderV1RecommendationStateInfoIn",
        "GoogleCloudRecommenderV1RecommendationStateInfoOut": "_recommender_43_GoogleCloudRecommenderV1RecommendationStateInfoOut",
        "GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn": "_recommender_44_GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn",
        "GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut": "_recommender_45_GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut",
        "GoogleCloudRecommenderV1SustainabilityProjectionIn": "_recommender_46_GoogleCloudRecommenderV1SustainabilityProjectionIn",
        "GoogleCloudRecommenderV1SustainabilityProjectionOut": "_recommender_47_GoogleCloudRecommenderV1SustainabilityProjectionOut",
        "GoogleCloudRecommenderV1ListInsightsResponseIn": "_recommender_48_GoogleCloudRecommenderV1ListInsightsResponseIn",
        "GoogleCloudRecommenderV1ListInsightsResponseOut": "_recommender_49_GoogleCloudRecommenderV1ListInsightsResponseOut",
        "GoogleCloudRecommenderV1RecommendationIn": "_recommender_50_GoogleCloudRecommenderV1RecommendationIn",
        "GoogleCloudRecommenderV1RecommendationOut": "_recommender_51_GoogleCloudRecommenderV1RecommendationOut",
        "GoogleCloudRecommenderV1ImpactIn": "_recommender_52_GoogleCloudRecommenderV1ImpactIn",
        "GoogleCloudRecommenderV1ImpactOut": "_recommender_53_GoogleCloudRecommenderV1ImpactOut",
        "GoogleTypeMoneyIn": "_recommender_54_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_recommender_55_GoogleTypeMoneyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationFailedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationFailedRequestOut"])
    types["GoogleCloudRecommenderV1ReliabilityProjectionIn"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "risks": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ReliabilityProjectionIn"])
    types["GoogleCloudRecommenderV1ReliabilityProjectionOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "risks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ReliabilityProjectionOut"])
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
    types["GoogleCloudRecommenderV1OperationIn"] = t.struct(
        {
            "action": t.string().optional(),
            "resourceType": t.string().optional(),
            "sourceResource": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.string().optional(),
            "path": t.string().optional(),
            "sourcePath": t.string().optional(),
            "valueMatcher": t.proxy(
                renames["GoogleCloudRecommenderV1ValueMatcherIn"]
            ).optional(),
            "pathFilters": t.struct({"_": t.string().optional()}).optional(),
            "pathValueMatchers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1OperationIn"])
    types["GoogleCloudRecommenderV1OperationOut"] = t.struct(
        {
            "action": t.string().optional(),
            "resourceType": t.string().optional(),
            "sourceResource": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.string().optional(),
            "path": t.string().optional(),
            "sourcePath": t.string().optional(),
            "valueMatcher": t.proxy(
                renames["GoogleCloudRecommenderV1ValueMatcherOut"]
            ).optional(),
            "pathFilters": t.struct({"_": t.string().optional()}).optional(),
            "pathValueMatchers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1OperationOut"])
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
    types["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"] = t.struct(
        {"recommendation": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"])
    types["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"] = t.struct(
        {
            "recommendation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"])
    types["GoogleCloudRecommenderV1InsightTypeConfigIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "insightTypeGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeConfigIn"])
    types["GoogleCloudRecommenderV1InsightTypeConfigOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "insightTypeGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"])
    types["GoogleCloudRecommenderV1InsightStateInfoIn"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightStateInfoIn"])
    types["GoogleCloudRecommenderV1InsightStateInfoOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightStateInfoOut"])
    types["GoogleCloudRecommenderV1SecurityProjectionIn"] = t.struct(
        {"details": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1SecurityProjectionIn"])
    types["GoogleCloudRecommenderV1SecurityProjectionOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1SecurityProjectionOut"])
    types["GoogleCloudRecommenderV1RecommenderConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "recommenderGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderConfigIn"])
    types["GoogleCloudRecommenderV1RecommenderConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "revisionId": t.string().optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "recommenderGenerationConfig": t.proxy(
                renames["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderConfigOut"])
    types["GoogleCloudRecommenderV1InsightIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "associatedRecommendations": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1InsightRecommendationReferenceIn"]
                )
            ).optional(),
            "lastRefreshTime": t.string().optional(),
            "observationPeriod": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1InsightStateInfoIn"]
            ).optional(),
            "etag": t.string().optional(),
            "targetResources": t.array(t.string()).optional(),
            "content": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "insightSubtype": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightIn"])
    types["GoogleCloudRecommenderV1InsightOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "associatedRecommendations": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1InsightRecommendationReferenceOut"]
                )
            ).optional(),
            "lastRefreshTime": t.string().optional(),
            "observationPeriod": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1InsightStateInfoOut"]
            ).optional(),
            "etag": t.string().optional(),
            "targetResources": t.array(t.string()).optional(),
            "content": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "category": t.string().optional(),
            "insightSubtype": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationDismissedRequestOut"])
    types["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"])
    types["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommenderGenerationConfigOut"])
    types["GoogleCloudRecommenderV1RecommendationContentIn"] = t.struct(
        {
            "overview": t.struct({"_": t.string().optional()}).optional(),
            "operationGroups": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationGroupIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationContentIn"])
    types["GoogleCloudRecommenderV1RecommendationContentOut"] = t.struct(
        {
            "overview": t.struct({"_": t.string().optional()}).optional(),
            "operationGroups": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1OperationGroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationContentOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationClaimedRequestOut"])
    types["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"] = t.struct(
        {"params": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"])
    types["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigOut"])
    types["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"] = t.struct(
        {"insight": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"])
    types["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"] = t.struct(
        {
            "insight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"])
    types["GoogleCloudRecommenderV1ValueMatcherIn"] = t.struct(
        {"matchesPattern": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1ValueMatcherIn"])
    types["GoogleCloudRecommenderV1ValueMatcherOut"] = t.struct(
        {
            "matchesPattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ValueMatcherOut"])
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
    types["GoogleCloudRecommenderV1RecommendationStateInfoIn"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationStateInfoIn"])
    types["GoogleCloudRecommenderV1RecommendationStateInfoOut"] = t.struct(
        {
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationStateInfoOut"])
    types["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestIn"])
    types["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut"] = t.struct(
        {
            "etag": t.string(),
            "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1MarkRecommendationSucceededRequestOut"])
    types["GoogleCloudRecommenderV1SustainabilityProjectionIn"] = t.struct(
        {"kgCO2e": t.number().optional(), "duration": t.string().optional()}
    ).named(renames["GoogleCloudRecommenderV1SustainabilityProjectionIn"])
    types["GoogleCloudRecommenderV1SustainabilityProjectionOut"] = t.struct(
        {
            "kgCO2e": t.number().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1SustainabilityProjectionOut"])
    types["GoogleCloudRecommenderV1ListInsightsResponseIn"] = t.struct(
        {
            "insights": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1InsightIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListInsightsResponseIn"])
    types["GoogleCloudRecommenderV1ListInsightsResponseOut"] = t.struct(
        {
            "insights": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1InsightOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"])
    types["GoogleCloudRecommenderV1RecommendationIn"] = t.struct(
        {
            "recommenderSubtype": t.string().optional(),
            "associatedInsights": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1RecommendationInsightReferenceIn"]
                )
            ).optional(),
            "additionalImpact": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1ImpactIn"])
            ).optional(),
            "xorGroupId": t.string().optional(),
            "priority": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationStateInfoIn"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "etag": t.string().optional(),
            "content": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationContentIn"]
            ).optional(),
            "primaryImpact": t.proxy(
                renames["GoogleCloudRecommenderV1ImpactIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationIn"])
    types["GoogleCloudRecommenderV1RecommendationOut"] = t.struct(
        {
            "recommenderSubtype": t.string().optional(),
            "associatedInsights": t.array(
                t.proxy(
                    renames["GoogleCloudRecommenderV1RecommendationInsightReferenceOut"]
                )
            ).optional(),
            "additionalImpact": t.array(
                t.proxy(renames["GoogleCloudRecommenderV1ImpactOut"])
            ).optional(),
            "xorGroupId": t.string().optional(),
            "priority": t.string().optional(),
            "stateInfo": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationStateInfoOut"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "lastRefreshTime": t.string().optional(),
            "etag": t.string().optional(),
            "content": t.proxy(
                renames["GoogleCloudRecommenderV1RecommendationContentOut"]
            ).optional(),
            "primaryImpact": t.proxy(
                renames["GoogleCloudRecommenderV1ImpactOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1RecommendationOut"])
    types["GoogleCloudRecommenderV1ImpactIn"] = t.struct(
        {
            "sustainabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SustainabilityProjectionIn"]
            ).optional(),
            "reliabilityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1ReliabilityProjectionIn"]
            ).optional(),
            "securityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SecurityProjectionIn"]
            ).optional(),
            "category": t.string().optional(),
            "costProjection": t.proxy(
                renames["GoogleCloudRecommenderV1CostProjectionIn"]
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
            "securityProjection": t.proxy(
                renames["GoogleCloudRecommenderV1SecurityProjectionOut"]
            ).optional(),
            "category": t.string().optional(),
            "costProjection": t.proxy(
                renames["GoogleCloudRecommenderV1CostProjectionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudRecommenderV1ImpactOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])

    functions = {}
    functions["foldersLocationsInsightTypesInsightsMarkAccepted"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
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
    functions[
        "foldersLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
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
        "foldersLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.get(
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
    functions["foldersLocationsRecommendersRecommendationsGet"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
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
                "updateMask": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsGet"] = recommender.post(
        "v1/{name}:markAccepted",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsList"] = recommender.post(
        "v1/{name}:markAccepted",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightTypesInsightsMarkAccepted"] = recommender.post(
        "v1/{name}:markAccepted",
        t.struct(
            {
                "name": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRecommendersUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "v1/{name}:markClaimed",
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
        "v1/{name}:markClaimed",
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
        "projectsLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "v1/{name}:markClaimed",
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
        "v1/{name}:markClaimed",
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
    functions["organizationsLocationsRecommendersGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
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
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
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
                "etag": t.string(),
                "stateMetadata": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommendationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "insightTypeGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1InsightTypeGenerationConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{parent}/insights",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1ListInsightsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsRecommendersGetConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsRecommendersUpdateConfig"] = recommender.patch(
        "v1/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "recommenderGenerationConfig": t.proxy(
                    renames["GoogleCloudRecommenderV1RecommenderGenerationConfigIn"]
                ).optional(),
                "updateTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudRecommenderV1RecommenderConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsRecommendersRecommendationsMarkFailed"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "billingAccountsLocationsRecommendersRecommendationsMarkDismissed"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "billingAccountsLocationsRecommendersRecommendationsMarkSucceeded"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "billingAccountsLocationsRecommendersRecommendationsGet"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "billingAccountsLocationsRecommendersRecommendationsList"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
        "billingAccountsLocationsRecommendersRecommendationsMarkClaimed"
    ] = recommender.post(
        "v1/{name}:markClaimed",
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
    functions["billingAccountsLocationsInsightTypesUpdateConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesGetConfig"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightTypeConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "billingAccountsLocationsInsightTypesInsightsMarkAccepted"
    ] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesInsightsList"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsLocationsInsightTypesInsightsGet"] = recommender.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudRecommenderV1InsightOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="recommender",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
