from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_workloadmanager() -> Import:
    workloadmanager = HTTPRuntime("https://workloadmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_workloadmanager_1_ErrorResponse",
        "WriteInsightRequestIn": "_workloadmanager_2_WriteInsightRequestIn",
        "WriteInsightRequestOut": "_workloadmanager_3_WriteInsightRequestOut",
        "ListOperationsResponseIn": "_workloadmanager_4_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workloadmanager_5_ListOperationsResponseOut",
        "ListEvaluationsResponseIn": "_workloadmanager_6_ListEvaluationsResponseIn",
        "ListEvaluationsResponseOut": "_workloadmanager_7_ListEvaluationsResponseOut",
        "ExecutionResultIn": "_workloadmanager_8_ExecutionResultIn",
        "ExecutionResultOut": "_workloadmanager_9_ExecutionResultOut",
        "LocationIn": "_workloadmanager_10_LocationIn",
        "LocationOut": "_workloadmanager_11_LocationOut",
        "EvaluationIn": "_workloadmanager_12_EvaluationIn",
        "EvaluationOut": "_workloadmanager_13_EvaluationOut",
        "ResourceFilterIn": "_workloadmanager_14_ResourceFilterIn",
        "ResourceFilterOut": "_workloadmanager_15_ResourceFilterOut",
        "SapValidationValidationDetailIn": "_workloadmanager_16_SapValidationValidationDetailIn",
        "SapValidationValidationDetailOut": "_workloadmanager_17_SapValidationValidationDetailOut",
        "SapDiscoveryComponentIn": "_workloadmanager_18_SapDiscoveryComponentIn",
        "SapDiscoveryComponentOut": "_workloadmanager_19_SapDiscoveryComponentOut",
        "ListScannedResourcesResponseIn": "_workloadmanager_20_ListScannedResourcesResponseIn",
        "ListScannedResourcesResponseOut": "_workloadmanager_21_ListScannedResourcesResponseOut",
        "SapDiscoveryResourceIn": "_workloadmanager_22_SapDiscoveryResourceIn",
        "SapDiscoveryResourceOut": "_workloadmanager_23_SapDiscoveryResourceOut",
        "OperationIn": "_workloadmanager_24_OperationIn",
        "OperationOut": "_workloadmanager_25_OperationOut",
        "SapValidationIn": "_workloadmanager_26_SapValidationIn",
        "SapValidationOut": "_workloadmanager_27_SapValidationOut",
        "RuleIn": "_workloadmanager_28_RuleIn",
        "RuleOut": "_workloadmanager_29_RuleOut",
        "ViolationDetailsIn": "_workloadmanager_30_ViolationDetailsIn",
        "ViolationDetailsOut": "_workloadmanager_31_ViolationDetailsOut",
        "InsightIn": "_workloadmanager_32_InsightIn",
        "InsightOut": "_workloadmanager_33_InsightOut",
        "StatusIn": "_workloadmanager_34_StatusIn",
        "StatusOut": "_workloadmanager_35_StatusOut",
        "SapDiscoveryMetadataIn": "_workloadmanager_36_SapDiscoveryMetadataIn",
        "SapDiscoveryMetadataOut": "_workloadmanager_37_SapDiscoveryMetadataOut",
        "WriteInsightResponseIn": "_workloadmanager_38_WriteInsightResponseIn",
        "WriteInsightResponseOut": "_workloadmanager_39_WriteInsightResponseOut",
        "ScannedResourceIn": "_workloadmanager_40_ScannedResourceIn",
        "ScannedResourceOut": "_workloadmanager_41_ScannedResourceOut",
        "OperationMetadataIn": "_workloadmanager_42_OperationMetadataIn",
        "OperationMetadataOut": "_workloadmanager_43_OperationMetadataOut",
        "RunEvaluationRequestIn": "_workloadmanager_44_RunEvaluationRequestIn",
        "RunEvaluationRequestOut": "_workloadmanager_45_RunEvaluationRequestOut",
        "SqlserverValidationIn": "_workloadmanager_46_SqlserverValidationIn",
        "SqlserverValidationOut": "_workloadmanager_47_SqlserverValidationOut",
        "ResourceIn": "_workloadmanager_48_ResourceIn",
        "ResourceOut": "_workloadmanager_49_ResourceOut",
        "CancelOperationRequestIn": "_workloadmanager_50_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workloadmanager_51_CancelOperationRequestOut",
        "SqlserverValidationValidationDetailIn": "_workloadmanager_52_SqlserverValidationValidationDetailIn",
        "SqlserverValidationValidationDetailOut": "_workloadmanager_53_SqlserverValidationValidationDetailOut",
        "SapDiscoveryIn": "_workloadmanager_54_SapDiscoveryIn",
        "SapDiscoveryOut": "_workloadmanager_55_SapDiscoveryOut",
        "ListExecutionsResponseIn": "_workloadmanager_56_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workloadmanager_57_ListExecutionsResponseOut",
        "ListExecutionResultsResponseIn": "_workloadmanager_58_ListExecutionResultsResponseIn",
        "ListExecutionResultsResponseOut": "_workloadmanager_59_ListExecutionResultsResponseOut",
        "GceInstanceFilterIn": "_workloadmanager_60_GceInstanceFilterIn",
        "GceInstanceFilterOut": "_workloadmanager_61_GceInstanceFilterOut",
        "EmptyIn": "_workloadmanager_62_EmptyIn",
        "EmptyOut": "_workloadmanager_63_EmptyOut",
        "ListLocationsResponseIn": "_workloadmanager_64_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workloadmanager_65_ListLocationsResponseOut",
        "ExecutionIn": "_workloadmanager_66_ExecutionIn",
        "ExecutionOut": "_workloadmanager_67_ExecutionOut",
        "ListRulesResponseIn": "_workloadmanager_68_ListRulesResponseIn",
        "ListRulesResponseOut": "_workloadmanager_69_ListRulesResponseOut",
        "ResourceStatusIn": "_workloadmanager_70_ResourceStatusIn",
        "ResourceStatusOut": "_workloadmanager_71_ResourceStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListEvaluationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEvaluationsResponseIn"])
    types["ListEvaluationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEvaluationsResponseOut"])
    types["ExecutionResultIn"] = t.struct(
        {
            "violationMessage": t.string().optional(),
            "rule": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "documentationUrl": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["ExecutionResultIn"])
    types["ExecutionResultOut"] = t.struct(
        {
            "violationMessage": t.string().optional(),
            "rule": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "documentationUrl": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResultOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EvaluationIn"] = t.struct(
        {
            "schedule": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ruleNames": t.array(t.string()).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EvaluationIn"])
    types["EvaluationOut"] = t.struct(
        {
            "schedule": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "resourceStatus": t.proxy(renames["ResourceStatusOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ruleNames": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "ruleVersions": t.array(t.string()).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationOut"])
    types["ResourceFilterIn"] = t.struct(
        {
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterIn"]).optional(),
            "scopes": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceFilterIn"])
    types["ResourceFilterOut"] = t.struct(
        {
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterOut"]).optional(),
            "scopes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceFilterOut"])
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
    types["SapDiscoveryComponentIn"] = t.struct(
        {
            "applicationType": t.string().optional(),
            "hostProject": t.string().optional(),
            "resources": t.array(t.proxy(renames["SapDiscoveryResourceIn"])).optional(),
            "sid": t.string().optional(),
            "databaseType": t.string().optional(),
        }
    ).named(renames["SapDiscoveryComponentIn"])
    types["SapDiscoveryComponentOut"] = t.struct(
        {
            "applicationType": t.string().optional(),
            "hostProject": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["SapDiscoveryResourceOut"])
            ).optional(),
            "sid": t.string().optional(),
            "databaseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryComponentOut"])
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
    types["SapDiscoveryResourceIn"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "resourceType": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "resourceUri": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["SapDiscoveryResourceIn"])
    types["SapDiscoveryResourceOut"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "resourceType": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "resourceUri": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryResourceOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["RuleIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "errorMessage": t.string().optional(),
            "remediation": t.string().optional(),
            "uri": t.string().optional(),
            "primaryCategory": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "severity": t.string().optional(),
            "name": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "errorMessage": t.string().optional(),
            "remediation": t.string().optional(),
            "uri": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])
    types["ViolationDetailsIn"] = t.struct(
        {
            "observed": t.struct({"_": t.string().optional()}).optional(),
            "asset": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["ViolationDetailsIn"])
    types["ViolationDetailsOut"] = t.struct(
        {
            "observed": t.struct({"_": t.string().optional()}).optional(),
            "asset": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationDetailsOut"])
    types["InsightIn"] = t.struct(
        {
            "sqlserverValidation": t.proxy(renames["SqlserverValidationIn"]).optional(),
            "sapValidation": t.proxy(renames["SapValidationIn"]).optional(),
            "sapDiscovery": t.proxy(renames["SapDiscoveryIn"]).optional(),
        }
    ).named(renames["InsightIn"])
    types["InsightOut"] = t.struct(
        {
            "sqlserverValidation": t.proxy(
                renames["SqlserverValidationOut"]
            ).optional(),
            "sentTime": t.string().optional(),
            "sapValidation": t.proxy(renames["SapValidationOut"]).optional(),
            "sapDiscovery": t.proxy(renames["SapDiscoveryOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["SapDiscoveryMetadataIn"] = t.struct(
        {
            "sapProduct": t.string().optional(),
            "environmentType": t.string().optional(),
            "definedSystem": t.string().optional(),
            "customerRegion": t.string().optional(),
        }
    ).named(renames["SapDiscoveryMetadataIn"])
    types["SapDiscoveryMetadataOut"] = t.struct(
        {
            "sapProduct": t.string().optional(),
            "environmentType": t.string().optional(),
            "definedSystem": t.string().optional(),
            "customerRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryMetadataOut"])
    types["WriteInsightResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteInsightResponseIn"]
    )
    types["WriteInsightResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteInsightResponseOut"])
    types["ScannedResourceIn"] = t.struct({"resource": t.string().optional()}).named(
        renames["ScannedResourceIn"]
    )
    types["ScannedResourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScannedResourceOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["SqlserverValidationIn"] = t.struct(
        {
            "agentVersion": t.string().optional(),
            "validationDetails": t.array(
                t.proxy(renames["SqlserverValidationValidationDetailIn"])
            ).optional(),
        }
    ).named(renames["SqlserverValidationIn"])
    types["SqlserverValidationOut"] = t.struct(
        {
            "agentVersion": t.string().optional(),
            "validationDetails": t.array(
                t.proxy(renames["SqlserverValidationValidationDetailOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlserverValidationOut"])
    types["ResourceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["SqlserverValidationValidationDetailIn"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SqlserverValidationValidationDetailIn"])
    types["SqlserverValidationValidationDetailOut"] = t.struct(
        {
            "instanceId": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlserverValidationValidationDetailOut"])
    types["SapDiscoveryIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "metadata": t.proxy(renames["SapDiscoveryMetadataIn"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
        }
    ).named(renames["SapDiscoveryIn"])
    types["SapDiscoveryOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "metadata": t.proxy(renames["SapDiscoveryMetadataOut"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryOut"])
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
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
    types["GceInstanceFilterIn"] = t.struct(
        {"serviceAccounts": t.array(t.string()).optional()}
    ).named(renames["GceInstanceFilterIn"])
    types["GceInstanceFilterOut"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceFilterOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ExecutionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "runType": t.string().optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "inventoryTime": t.string().optional(),
            "startTime": t.string().optional(),
            "evaluationId": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "runType": t.string().optional(),
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

    functions = {}
    functions["projectsLocationsGet"] = workloadmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsList"] = workloadmanager.post(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "evaluationId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "ruleNames": t.array(t.string()).optional(),
                "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsGet"] = workloadmanager.post(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "evaluationId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "ruleNames": t.array(t.string()).optional(),
                "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsCreate"] = workloadmanager.post(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "evaluationId": t.string(),
                "parent": t.string(),
                "requestId": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "ruleNames": t.array(t.string()).optional(),
                "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsRun"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsList"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsGet"] = workloadmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ExecutionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsEvaluationsExecutionsScannedResourcesList"
    ] = workloadmanager.get(
        "v1/{parent}/scannedResources",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "rule": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionResultsResponseOut"]),
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
    functions["projectsLocationsRulesList"] = workloadmanager.get(
        "v1/{parent}/rules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRulesResponseOut"]),
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

    return Import(
        importer="workloadmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
