from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_workloadmanager() -> Import:
    workloadmanager = HTTPRuntime("https://workloadmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_workloadmanager_1_ErrorResponse",
        "ResourceStatusIn": "_workloadmanager_2_ResourceStatusIn",
        "ResourceStatusOut": "_workloadmanager_3_ResourceStatusOut",
        "InsightIn": "_workloadmanager_4_InsightIn",
        "InsightOut": "_workloadmanager_5_InsightOut",
        "RuleIn": "_workloadmanager_6_RuleIn",
        "RuleOut": "_workloadmanager_7_RuleOut",
        "LocationIn": "_workloadmanager_8_LocationIn",
        "LocationOut": "_workloadmanager_9_LocationOut",
        "SapValidationValidationDetailIn": "_workloadmanager_10_SapValidationValidationDetailIn",
        "SapValidationValidationDetailOut": "_workloadmanager_11_SapValidationValidationDetailOut",
        "SapDiscoveryMetadataIn": "_workloadmanager_12_SapDiscoveryMetadataIn",
        "SapDiscoveryMetadataOut": "_workloadmanager_13_SapDiscoveryMetadataOut",
        "ExecutionIn": "_workloadmanager_14_ExecutionIn",
        "ExecutionOut": "_workloadmanager_15_ExecutionOut",
        "ListRulesResponseIn": "_workloadmanager_16_ListRulesResponseIn",
        "ListRulesResponseOut": "_workloadmanager_17_ListRulesResponseOut",
        "SapDiscoveryIn": "_workloadmanager_18_SapDiscoveryIn",
        "SapDiscoveryOut": "_workloadmanager_19_SapDiscoveryOut",
        "ListScannedResourcesResponseIn": "_workloadmanager_20_ListScannedResourcesResponseIn",
        "ListScannedResourcesResponseOut": "_workloadmanager_21_ListScannedResourcesResponseOut",
        "ResourceIn": "_workloadmanager_22_ResourceIn",
        "ResourceOut": "_workloadmanager_23_ResourceOut",
        "EvaluationIn": "_workloadmanager_24_EvaluationIn",
        "EvaluationOut": "_workloadmanager_25_EvaluationOut",
        "EmptyIn": "_workloadmanager_26_EmptyIn",
        "EmptyOut": "_workloadmanager_27_EmptyOut",
        "ListExecutionResultsResponseIn": "_workloadmanager_28_ListExecutionResultsResponseIn",
        "ListExecutionResultsResponseOut": "_workloadmanager_29_ListExecutionResultsResponseOut",
        "WriteInsightRequestIn": "_workloadmanager_30_WriteInsightRequestIn",
        "WriteInsightRequestOut": "_workloadmanager_31_WriteInsightRequestOut",
        "ListLocationsResponseIn": "_workloadmanager_32_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workloadmanager_33_ListLocationsResponseOut",
        "SapDiscoveryComponentIn": "_workloadmanager_34_SapDiscoveryComponentIn",
        "SapDiscoveryComponentOut": "_workloadmanager_35_SapDiscoveryComponentOut",
        "OperationMetadataIn": "_workloadmanager_36_OperationMetadataIn",
        "OperationMetadataOut": "_workloadmanager_37_OperationMetadataOut",
        "StatusIn": "_workloadmanager_38_StatusIn",
        "StatusOut": "_workloadmanager_39_StatusOut",
        "CancelOperationRequestIn": "_workloadmanager_40_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workloadmanager_41_CancelOperationRequestOut",
        "ListExecutionsResponseIn": "_workloadmanager_42_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workloadmanager_43_ListExecutionsResponseOut",
        "SapValidationIn": "_workloadmanager_44_SapValidationIn",
        "SapValidationOut": "_workloadmanager_45_SapValidationOut",
        "ListEvaluationsResponseIn": "_workloadmanager_46_ListEvaluationsResponseIn",
        "ListEvaluationsResponseOut": "_workloadmanager_47_ListEvaluationsResponseOut",
        "WriteInsightResponseIn": "_workloadmanager_48_WriteInsightResponseIn",
        "WriteInsightResponseOut": "_workloadmanager_49_WriteInsightResponseOut",
        "OperationIn": "_workloadmanager_50_OperationIn",
        "OperationOut": "_workloadmanager_51_OperationOut",
        "ResourceFilterIn": "_workloadmanager_52_ResourceFilterIn",
        "ResourceFilterOut": "_workloadmanager_53_ResourceFilterOut",
        "GceInstanceFilterIn": "_workloadmanager_54_GceInstanceFilterIn",
        "GceInstanceFilterOut": "_workloadmanager_55_GceInstanceFilterOut",
        "ScannedResourceIn": "_workloadmanager_56_ScannedResourceIn",
        "ScannedResourceOut": "_workloadmanager_57_ScannedResourceOut",
        "ExecutionResultIn": "_workloadmanager_58_ExecutionResultIn",
        "ExecutionResultOut": "_workloadmanager_59_ExecutionResultOut",
        "SapDiscoveryResourceIn": "_workloadmanager_60_SapDiscoveryResourceIn",
        "SapDiscoveryResourceOut": "_workloadmanager_61_SapDiscoveryResourceOut",
        "RunEvaluationRequestIn": "_workloadmanager_62_RunEvaluationRequestIn",
        "RunEvaluationRequestOut": "_workloadmanager_63_RunEvaluationRequestOut",
        "ListOperationsResponseIn": "_workloadmanager_64_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workloadmanager_65_ListOperationsResponseOut",
        "ViolationDetailsIn": "_workloadmanager_66_ViolationDetailsIn",
        "ViolationDetailsOut": "_workloadmanager_67_ViolationDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResourceStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "rulesNewerVersions": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceStatusIn"])
    types["ResourceStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "rulesNewerVersions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceStatusOut"])
    types["InsightIn"] = t.struct(
        {
            "sapDiscovery": t.proxy(renames["SapDiscoveryIn"]).optional(),
            "sapValidation": t.proxy(renames["SapValidationIn"]).optional(),
        }
    ).named(renames["InsightIn"])
    types["InsightOut"] = t.struct(
        {
            "sapDiscovery": t.proxy(renames["SapDiscoveryOut"]).optional(),
            "sentTime": t.string().optional(),
            "sapValidation": t.proxy(renames["SapValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["RuleIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "severity": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "errorMessage": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "remediation": t.string().optional(),
            "primaryCategory": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "severity": t.string().optional(),
            "revisionId": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "errorMessage": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "remediation": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
            "sapProduct": t.string().optional(),
            "definedSystem": t.string().optional(),
            "environmentType": t.string().optional(),
            "customerRegion": t.string().optional(),
        }
    ).named(renames["SapDiscoveryMetadataIn"])
    types["SapDiscoveryMetadataOut"] = t.struct(
        {
            "sapProduct": t.string().optional(),
            "definedSystem": t.string().optional(),
            "environmentType": t.string().optional(),
            "customerRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryMetadataOut"])
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
            "inventoryTime": t.string().optional(),
            "evaluationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
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
    types["SapDiscoveryIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
            "metadata": t.proxy(renames["SapDiscoveryMetadataIn"]).optional(),
            "systemId": t.string().optional(),
        }
    ).named(renames["SapDiscoveryIn"])
    types["SapDiscoveryOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "metadata": t.proxy(renames["SapDiscoveryMetadataOut"]).optional(),
            "systemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryOut"])
    types["ListScannedResourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scannedResources": t.array(
                t.proxy(renames["ScannedResourceIn"])
            ).optional(),
        }
    ).named(renames["ListScannedResourcesResponseIn"])
    types["ListScannedResourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scannedResources": t.array(
                t.proxy(renames["ScannedResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScannedResourcesResponseOut"])
    types["ResourceIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["EvaluationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "schedule": t.string().optional(),
            "name": t.string().optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
            "ruleNames": t.array(t.string()).optional(),
        }
    ).named(renames["EvaluationIn"])
    types["EvaluationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "ruleVersions": t.array(t.string()).optional(),
            "schedule": t.string().optional(),
            "name": t.string().optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterOut"]).optional(),
            "ruleNames": t.array(t.string()).optional(),
            "resourceStatus": t.proxy(renames["ResourceStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListExecutionResultsResponseIn"] = t.struct(
        {
            "executionResults": t.array(
                t.proxy(renames["ExecutionResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExecutionResultsResponseIn"])
    types["ListExecutionResultsResponseOut"] = t.struct(
        {
            "executionResults": t.array(
                t.proxy(renames["ExecutionResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionResultsResponseOut"])
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
    types["SapDiscoveryComponentIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["SapDiscoveryResourceIn"])).optional(),
            "sid": t.string().optional(),
            "applicationType": t.string().optional(),
            "hostProject": t.string().optional(),
            "databaseType": t.string().optional(),
        }
    ).named(renames["SapDiscoveryComponentIn"])
    types["SapDiscoveryComponentOut"] = t.struct(
        {
            "resources": t.array(
                t.proxy(renames["SapDiscoveryResourceOut"])
            ).optional(),
            "sid": t.string().optional(),
            "applicationType": t.string().optional(),
            "hostProject": t.string().optional(),
            "databaseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryComponentOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
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
    types["ListEvaluationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListEvaluationsResponseIn"])
    types["ListEvaluationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEvaluationsResponseOut"])
    types["WriteInsightResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteInsightResponseIn"]
    )
    types["WriteInsightResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteInsightResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ResourceFilterIn"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterIn"]).optional(),
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResourceFilterIn"])
    types["ResourceFilterOut"] = t.struct(
        {
            "scopes": t.array(t.string()).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterOut"]).optional(),
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceFilterOut"])
    types["GceInstanceFilterIn"] = t.struct(
        {"serviceAccounts": t.array(t.string()).optional()}
    ).named(renames["GceInstanceFilterIn"])
    types["GceInstanceFilterOut"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceFilterOut"])
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
            "severity": t.string().optional(),
            "violationMessage": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsIn"]).optional(),
            "rule": t.string().optional(),
        }
    ).named(renames["ExecutionResultIn"])
    types["ExecutionResultOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "violationMessage": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsOut"]).optional(),
            "rule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResultOut"])
    types["SapDiscoveryResourceIn"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "resourceKind": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceState": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["SapDiscoveryResourceIn"])
    types["SapDiscoveryResourceOut"] = t.struct(
        {
            "resourceUri": t.string().optional(),
            "resourceKind": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceState": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryResourceOut"])
    types["RunEvaluationRequestIn"] = t.struct(
        {
            "executionId": t.string(),
            "requestId": t.string().optional(),
            "execution": t.proxy(renames["ExecutionIn"]),
        }
    ).named(renames["RunEvaluationRequestIn"])
    types["RunEvaluationRequestOut"] = t.struct(
        {
            "executionId": t.string(),
            "requestId": t.string().optional(),
            "execution": t.proxy(renames["ExecutionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunEvaluationRequestOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ViolationDetailsIn"] = t.struct(
        {
            "observed": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "asset": t.string().optional(),
        }
    ).named(renames["ViolationDetailsIn"])
    types["ViolationDetailsOut"] = t.struct(
        {
            "observed": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "asset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationDetailsOut"])

    functions = {}
    functions["projectsLocationsList"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
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
    functions["projectsLocationsEvaluationsExecutionsGet"] = workloadmanager.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsRun"] = workloadmanager.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsList"] = workloadmanager.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEvaluationsExecutionsScannedResourcesList"
    ] = workloadmanager.get(
        "v1/{parent}/scannedResources",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "rule": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRulesList"] = workloadmanager.get(
        "v1/{parent}/rules",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workloadmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
