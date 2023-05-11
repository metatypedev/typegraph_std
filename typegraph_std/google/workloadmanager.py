from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_workloadmanager() -> Import:
    workloadmanager = HTTPRuntime("https://workloadmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_workloadmanager_1_ErrorResponse",
        "ListLocationsResponseIn": "_workloadmanager_2_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workloadmanager_3_ListLocationsResponseOut",
        "StatusIn": "_workloadmanager_4_StatusIn",
        "StatusOut": "_workloadmanager_5_StatusOut",
        "ResourceIn": "_workloadmanager_6_ResourceIn",
        "ResourceOut": "_workloadmanager_7_ResourceOut",
        "InsightIn": "_workloadmanager_8_InsightIn",
        "InsightOut": "_workloadmanager_9_InsightOut",
        "ListExecutionsResponseIn": "_workloadmanager_10_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workloadmanager_11_ListExecutionsResponseOut",
        "SapDiscoveryComponentIn": "_workloadmanager_12_SapDiscoveryComponentIn",
        "SapDiscoveryComponentOut": "_workloadmanager_13_SapDiscoveryComponentOut",
        "ViolationDetailsIn": "_workloadmanager_14_ViolationDetailsIn",
        "ViolationDetailsOut": "_workloadmanager_15_ViolationDetailsOut",
        "SapDiscoveryResourceIn": "_workloadmanager_16_SapDiscoveryResourceIn",
        "SapDiscoveryResourceOut": "_workloadmanager_17_SapDiscoveryResourceOut",
        "ResourceStatusIn": "_workloadmanager_18_ResourceStatusIn",
        "ResourceStatusOut": "_workloadmanager_19_ResourceStatusOut",
        "ListRulesResponseIn": "_workloadmanager_20_ListRulesResponseIn",
        "ListRulesResponseOut": "_workloadmanager_21_ListRulesResponseOut",
        "SapValidationValidationDetailIn": "_workloadmanager_22_SapValidationValidationDetailIn",
        "SapValidationValidationDetailOut": "_workloadmanager_23_SapValidationValidationDetailOut",
        "SapDiscoveryMetadataIn": "_workloadmanager_24_SapDiscoveryMetadataIn",
        "SapDiscoveryMetadataOut": "_workloadmanager_25_SapDiscoveryMetadataOut",
        "ListExecutionResultsResponseIn": "_workloadmanager_26_ListExecutionResultsResponseIn",
        "ListExecutionResultsResponseOut": "_workloadmanager_27_ListExecutionResultsResponseOut",
        "RuleIn": "_workloadmanager_28_RuleIn",
        "RuleOut": "_workloadmanager_29_RuleOut",
        "SapDiscoveryIn": "_workloadmanager_30_SapDiscoveryIn",
        "SapDiscoveryOut": "_workloadmanager_31_SapDiscoveryOut",
        "WriteInsightResponseIn": "_workloadmanager_32_WriteInsightResponseIn",
        "WriteInsightResponseOut": "_workloadmanager_33_WriteInsightResponseOut",
        "EvaluationIn": "_workloadmanager_34_EvaluationIn",
        "EvaluationOut": "_workloadmanager_35_EvaluationOut",
        "ListEvaluationsResponseIn": "_workloadmanager_36_ListEvaluationsResponseIn",
        "ListEvaluationsResponseOut": "_workloadmanager_37_ListEvaluationsResponseOut",
        "ListOperationsResponseIn": "_workloadmanager_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workloadmanager_39_ListOperationsResponseOut",
        "ScannedResourceIn": "_workloadmanager_40_ScannedResourceIn",
        "ScannedResourceOut": "_workloadmanager_41_ScannedResourceOut",
        "ExecutionResultIn": "_workloadmanager_42_ExecutionResultIn",
        "ExecutionResultOut": "_workloadmanager_43_ExecutionResultOut",
        "ExecutionIn": "_workloadmanager_44_ExecutionIn",
        "ExecutionOut": "_workloadmanager_45_ExecutionOut",
        "ListScannedResourcesResponseIn": "_workloadmanager_46_ListScannedResourcesResponseIn",
        "ListScannedResourcesResponseOut": "_workloadmanager_47_ListScannedResourcesResponseOut",
        "GceInstanceFilterIn": "_workloadmanager_48_GceInstanceFilterIn",
        "GceInstanceFilterOut": "_workloadmanager_49_GceInstanceFilterOut",
        "OperationIn": "_workloadmanager_50_OperationIn",
        "OperationOut": "_workloadmanager_51_OperationOut",
        "OperationMetadataIn": "_workloadmanager_52_OperationMetadataIn",
        "OperationMetadataOut": "_workloadmanager_53_OperationMetadataOut",
        "SapValidationIn": "_workloadmanager_54_SapValidationIn",
        "SapValidationOut": "_workloadmanager_55_SapValidationOut",
        "CancelOperationRequestIn": "_workloadmanager_56_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workloadmanager_57_CancelOperationRequestOut",
        "LocationIn": "_workloadmanager_58_LocationIn",
        "LocationOut": "_workloadmanager_59_LocationOut",
        "EmptyIn": "_workloadmanager_60_EmptyIn",
        "EmptyOut": "_workloadmanager_61_EmptyOut",
        "RunEvaluationRequestIn": "_workloadmanager_62_RunEvaluationRequestIn",
        "RunEvaluationRequestOut": "_workloadmanager_63_RunEvaluationRequestOut",
        "ResourceFilterIn": "_workloadmanager_64_ResourceFilterIn",
        "ResourceFilterOut": "_workloadmanager_65_ResourceFilterOut",
        "WriteInsightRequestIn": "_workloadmanager_66_WriteInsightRequestIn",
        "WriteInsightRequestOut": "_workloadmanager_67_WriteInsightRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ResourceIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["InsightIn"] = t.struct(
        {
            "sapValidation": t.proxy(renames["SapValidationIn"]).optional(),
            "sapDiscovery": t.proxy(renames["SapDiscoveryIn"]).optional(),
        }
    ).named(renames["InsightIn"])
    types["InsightOut"] = t.struct(
        {
            "sapValidation": t.proxy(renames["SapValidationOut"]).optional(),
            "sapDiscovery": t.proxy(renames["SapDiscoveryOut"]).optional(),
            "sentTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
    types["SapDiscoveryComponentIn"] = t.struct(
        {
            "sid": t.string().optional(),
            "hostProject": t.string().optional(),
            "applicationType": t.string().optional(),
            "databaseType": t.string().optional(),
            "resources": t.array(t.proxy(renames["SapDiscoveryResourceIn"])).optional(),
        }
    ).named(renames["SapDiscoveryComponentIn"])
    types["SapDiscoveryComponentOut"] = t.struct(
        {
            "sid": t.string().optional(),
            "hostProject": t.string().optional(),
            "applicationType": t.string().optional(),
            "databaseType": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["SapDiscoveryResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryComponentOut"])
    types["ViolationDetailsIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "asset": t.string().optional(),
            "observed": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ViolationDetailsIn"])
    types["ViolationDetailsOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "asset": t.string().optional(),
            "observed": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationDetailsOut"])
    types["SapDiscoveryResourceIn"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "resourceState": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resourceType": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["SapDiscoveryResourceIn"])
    types["SapDiscoveryResourceOut"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "resourceState": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resourceType": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryResourceOut"])
    types["ResourceStatusIn"] = t.struct(
        {
            "rulesNewerVersions": t.array(t.string()).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ResourceStatusIn"])
    types["ResourceStatusOut"] = t.struct(
        {
            "rulesNewerVersions": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceStatusOut"])
    types["ListRulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
        }
    ).named(renames["ListRulesResponseIn"])
    types["ListRulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRulesResponseOut"])
    types["SapValidationValidationDetailIn"] = t.struct(
        {
            "sapValidationType": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SapValidationValidationDetailIn"])
    types["SapValidationValidationDetailOut"] = t.struct(
        {
            "sapValidationType": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapValidationValidationDetailOut"])
    types["SapDiscoveryMetadataIn"] = t.struct(
        {
            "environmentType": t.string().optional(),
            "customerRegion": t.string().optional(),
            "definedSystem": t.string().optional(),
            "sapProduct": t.string().optional(),
        }
    ).named(renames["SapDiscoveryMetadataIn"])
    types["SapDiscoveryMetadataOut"] = t.struct(
        {
            "environmentType": t.string().optional(),
            "customerRegion": t.string().optional(),
            "definedSystem": t.string().optional(),
            "sapProduct": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryMetadataOut"])
    types["ListExecutionResultsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executionResults": t.array(
                t.proxy(renames["ExecutionResultIn"])
            ).optional(),
        }
    ).named(renames["ListExecutionResultsResponseIn"])
    types["ListExecutionResultsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executionResults": t.array(
                t.proxy(renames["ExecutionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionResultsResponseOut"])
    types["RuleIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "uri": t.string().optional(),
            "remediation": t.string().optional(),
            "severity": t.string().optional(),
            "secondaryCategory": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "revisionId": t.string().optional(),
            "uri": t.string().optional(),
            "remediation": t.string().optional(),
            "severity": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["SapDiscoveryIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SapDiscoveryMetadataIn"]).optional(),
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
        }
    ).named(renames["SapDiscoveryIn"])
    types["SapDiscoveryOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SapDiscoveryMetadataOut"]).optional(),
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryOut"])
    types["WriteInsightResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteInsightResponseIn"]
    )
    types["WriteInsightResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteInsightResponseOut"])
    types["EvaluationIn"] = t.struct(
        {
            "schedule": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "ruleNames": t.array(t.string()).optional(),
        }
    ).named(renames["EvaluationIn"])
    types["EvaluationOut"] = t.struct(
        {
            "schedule": t.string().optional(),
            "resourceStatus": t.proxy(renames["ResourceStatusOut"]).optional(),
            "ruleVersions": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "ruleNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationOut"])
    types["ListEvaluationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationIn"])).optional(),
        }
    ).named(renames["ListEvaluationsResponseIn"])
    types["ListEvaluationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEvaluationsResponseOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ScannedResourceIn"] = t.struct({"resource": t.string().optional()}).named(
        renames["ScannedResourceIn"]
    )
    types["ScannedResourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScannedResourceOut"])
    types["ExecutionResultIn"] = t.struct(
        {
            "rule": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsIn"]).optional(),
            "violationMessage": t.string().optional(),
            "severity": t.string().optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
        }
    ).named(renames["ExecutionResultIn"])
    types["ExecutionResultOut"] = t.struct(
        {
            "rule": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsOut"]).optional(),
            "violationMessage": t.string().optional(),
            "severity": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResultOut"])
    types["ExecutionIn"] = t.struct(
        {
            "runType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "runType": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "evaluationId": t.string().optional(),
            "inventoryTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
    types["ListScannedResourcesResponseIn"] = t.struct(
        {
            "scannedResources": t.array(
                t.proxy(renames["ScannedResourceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListScannedResourcesResponseIn"])
    types["ListScannedResourcesResponseOut"] = t.struct(
        {
            "scannedResources": t.array(
                t.proxy(renames["ScannedResourceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScannedResourcesResponseOut"])
    types["GceInstanceFilterIn"] = t.struct(
        {"serviceAccounts": t.array(t.string()).optional()}
    ).named(renames["GceInstanceFilterIn"])
    types["GceInstanceFilterOut"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceFilterOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SapValidationIn"] = t.struct(
        {
            "validationDetails": t.array(
                t.proxy(renames["SapValidationValidationDetailIn"])
            ).optional()
        }
    ).named(renames["SapValidationIn"])
    types["SapValidationOut"] = t.struct(
        {
            "validationDetails": t.array(
                t.proxy(renames["SapValidationValidationDetailOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapValidationOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RunEvaluationRequestIn"] = t.struct(
        {
            "execution": t.proxy(renames["ExecutionIn"]),
            "executionId": t.string(),
            "requestId": t.string().optional(),
        }
    ).named(renames["RunEvaluationRequestIn"])
    types["RunEvaluationRequestOut"] = t.struct(
        {
            "execution": t.proxy(renames["ExecutionOut"]),
            "executionId": t.string(),
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunEvaluationRequestOut"])
    types["ResourceFilterIn"] = t.struct(
        {
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterIn"]).optional(),
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "scopes": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceFilterIn"])
    types["ResourceFilterOut"] = t.struct(
        {
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterOut"]).optional(),
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "scopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceFilterOut"])
    types["WriteInsightRequestIn"] = t.struct(
        {"requestId": t.string().optional(), "insight": t.proxy(renames["InsightIn"])}
    ).named(renames["WriteInsightRequestIn"])
    types["WriteInsightRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "insight": t.proxy(renames["InsightOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteInsightRequestOut"])

    functions = {}
    functions["projectsLocationsGet"] = workloadmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = workloadmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInsightsWriteInsight"] = workloadmanager.post(
        "v1/{location}/insights:writeInsight",
        t.struct(
            {
                "location": t.string(),
                "requestId": t.string().optional(),
                "insight": t.proxy(renames["InsightIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WriteInsightResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRulesList"] = workloadmanager.get(
        "v1/{parent}/rules",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsList"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsCreate"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsGet"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EvaluationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsList"] = workloadmanager.post(
        "v1/{name}/executions:run",
        t.struct(
            {
                "name": t.string(),
                "execution": t.proxy(renames["ExecutionIn"]),
                "executionId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsGet"] = workloadmanager.post(
        "v1/{name}/executions:run",
        t.struct(
            {
                "name": t.string(),
                "execution": t.proxy(renames["ExecutionIn"]),
                "executionId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsRun"] = workloadmanager.post(
        "v1/{name}/executions:run",
        t.struct(
            {
                "name": t.string(),
                "execution": t.proxy(renames["ExecutionIn"]),
                "executionId": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEvaluationsExecutionsScannedResourcesList"
    ] = workloadmanager.get(
        "v1/{parent}/scannedResources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "rule": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScannedResourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEvaluationsExecutionsResultsList"
    ] = workloadmanager.get(
        "v1/{parent}/results",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workloadmanager.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workloadmanager.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workloadmanager.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = workloadmanager.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workloadmanager", renames=renames, types=types, functions=functions
    )
