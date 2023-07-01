from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_workloadmanager():
    workloadmanager = HTTPRuntime("https://workloadmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_workloadmanager_1_ErrorResponse",
        "OperationIn": "_workloadmanager_2_OperationIn",
        "OperationOut": "_workloadmanager_3_OperationOut",
        "OperationMetadataIn": "_workloadmanager_4_OperationMetadataIn",
        "OperationMetadataOut": "_workloadmanager_5_OperationMetadataOut",
        "SqlserverValidationDetailsIn": "_workloadmanager_6_SqlserverValidationDetailsIn",
        "SqlserverValidationDetailsOut": "_workloadmanager_7_SqlserverValidationDetailsOut",
        "SapDiscoveryComponentIn": "_workloadmanager_8_SapDiscoveryComponentIn",
        "SapDiscoveryComponentOut": "_workloadmanager_9_SapDiscoveryComponentOut",
        "ListRulesResponseIn": "_workloadmanager_10_ListRulesResponseIn",
        "ListRulesResponseOut": "_workloadmanager_11_ListRulesResponseOut",
        "CancelOperationRequestIn": "_workloadmanager_12_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workloadmanager_13_CancelOperationRequestOut",
        "ExecutionIn": "_workloadmanager_14_ExecutionIn",
        "ExecutionOut": "_workloadmanager_15_ExecutionOut",
        "SapValidationIn": "_workloadmanager_16_SapValidationIn",
        "SapValidationOut": "_workloadmanager_17_SapValidationOut",
        "ListExecutionsResponseIn": "_workloadmanager_18_ListExecutionsResponseIn",
        "ListExecutionsResponseOut": "_workloadmanager_19_ListExecutionsResponseOut",
        "SqlserverValidationValidationDetailIn": "_workloadmanager_20_SqlserverValidationValidationDetailIn",
        "SqlserverValidationValidationDetailOut": "_workloadmanager_21_SqlserverValidationValidationDetailOut",
        "SapDiscoveryMetadataIn": "_workloadmanager_22_SapDiscoveryMetadataIn",
        "SapDiscoveryMetadataOut": "_workloadmanager_23_SapDiscoveryMetadataOut",
        "ListExecutionResultsResponseIn": "_workloadmanager_24_ListExecutionResultsResponseIn",
        "ListExecutionResultsResponseOut": "_workloadmanager_25_ListExecutionResultsResponseOut",
        "SapDiscoveryIn": "_workloadmanager_26_SapDiscoveryIn",
        "SapDiscoveryOut": "_workloadmanager_27_SapDiscoveryOut",
        "EmptyIn": "_workloadmanager_28_EmptyIn",
        "EmptyOut": "_workloadmanager_29_EmptyOut",
        "ExecutionResultIn": "_workloadmanager_30_ExecutionResultIn",
        "ExecutionResultOut": "_workloadmanager_31_ExecutionResultOut",
        "ViolationDetailsIn": "_workloadmanager_32_ViolationDetailsIn",
        "ViolationDetailsOut": "_workloadmanager_33_ViolationDetailsOut",
        "RunEvaluationRequestIn": "_workloadmanager_34_RunEvaluationRequestIn",
        "RunEvaluationRequestOut": "_workloadmanager_35_RunEvaluationRequestOut",
        "SapDiscoveryResourceIn": "_workloadmanager_36_SapDiscoveryResourceIn",
        "SapDiscoveryResourceOut": "_workloadmanager_37_SapDiscoveryResourceOut",
        "WriteInsightRequestIn": "_workloadmanager_38_WriteInsightRequestIn",
        "WriteInsightRequestOut": "_workloadmanager_39_WriteInsightRequestOut",
        "ListEvaluationsResponseIn": "_workloadmanager_40_ListEvaluationsResponseIn",
        "ListEvaluationsResponseOut": "_workloadmanager_41_ListEvaluationsResponseOut",
        "ScannedResourceIn": "_workloadmanager_42_ScannedResourceIn",
        "ScannedResourceOut": "_workloadmanager_43_ScannedResourceOut",
        "ListOperationsResponseIn": "_workloadmanager_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workloadmanager_45_ListOperationsResponseOut",
        "GceInstanceFilterIn": "_workloadmanager_46_GceInstanceFilterIn",
        "GceInstanceFilterOut": "_workloadmanager_47_GceInstanceFilterOut",
        "LocationIn": "_workloadmanager_48_LocationIn",
        "LocationOut": "_workloadmanager_49_LocationOut",
        "SqlserverValidationIn": "_workloadmanager_50_SqlserverValidationIn",
        "SqlserverValidationOut": "_workloadmanager_51_SqlserverValidationOut",
        "ResourceFilterIn": "_workloadmanager_52_ResourceFilterIn",
        "ResourceFilterOut": "_workloadmanager_53_ResourceFilterOut",
        "ResourceIn": "_workloadmanager_54_ResourceIn",
        "ResourceOut": "_workloadmanager_55_ResourceOut",
        "EvaluationIn": "_workloadmanager_56_EvaluationIn",
        "EvaluationOut": "_workloadmanager_57_EvaluationOut",
        "StatusIn": "_workloadmanager_58_StatusIn",
        "StatusOut": "_workloadmanager_59_StatusOut",
        "InsightIn": "_workloadmanager_60_InsightIn",
        "InsightOut": "_workloadmanager_61_InsightOut",
        "WriteInsightResponseIn": "_workloadmanager_62_WriteInsightResponseIn",
        "WriteInsightResponseOut": "_workloadmanager_63_WriteInsightResponseOut",
        "SapValidationValidationDetailIn": "_workloadmanager_64_SapValidationValidationDetailIn",
        "SapValidationValidationDetailOut": "_workloadmanager_65_SapValidationValidationDetailOut",
        "ListScannedResourcesResponseIn": "_workloadmanager_66_ListScannedResourcesResponseIn",
        "ListScannedResourcesResponseOut": "_workloadmanager_67_ListScannedResourcesResponseOut",
        "ListLocationsResponseIn": "_workloadmanager_68_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_workloadmanager_69_ListLocationsResponseOut",
        "ResourceStatusIn": "_workloadmanager_70_ResourceStatusIn",
        "ResourceStatusOut": "_workloadmanager_71_ResourceStatusOut",
        "RuleIn": "_workloadmanager_72_RuleIn",
        "RuleOut": "_workloadmanager_73_RuleOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SqlserverValidationDetailsIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()})}
    ).named(renames["SqlserverValidationDetailsIn"])
    types["SqlserverValidationDetailsOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlserverValidationDetailsOut"])
    types["SapDiscoveryComponentIn"] = t.struct(
        {
            "applicationType": t.string().optional(),
            "resources": t.array(t.proxy(renames["SapDiscoveryResourceIn"])).optional(),
            "databaseType": t.string().optional(),
            "hostProject": t.string().optional(),
            "sid": t.string().optional(),
        }
    ).named(renames["SapDiscoveryComponentIn"])
    types["SapDiscoveryComponentOut"] = t.struct(
        {
            "applicationType": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["SapDiscoveryResourceOut"])
            ).optional(),
            "databaseType": t.string().optional(),
            "hostProject": t.string().optional(),
            "sid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryComponentOut"])
    types["ListRulesResponseIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRulesResponseIn"])
    types["ListRulesResponseOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["RuleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRulesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ExecutionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "runType": t.string().optional(),
        }
    ).named(renames["ExecutionIn"])
    types["ExecutionOut"] = t.struct(
        {
            "evaluationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "runType": t.string().optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "inventoryTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionOut"])
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
    types["ListExecutionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListExecutionsResponseIn"])
    types["ListExecutionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "executions": t.array(t.proxy(renames["ExecutionOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListExecutionsResponseOut"])
    types["SqlserverValidationValidationDetailIn"] = t.struct(
        {
            "type": t.string().optional(),
            "details": t.array(t.proxy(renames["SqlserverValidationDetailsIn"])),
        }
    ).named(renames["SqlserverValidationValidationDetailIn"])
    types["SqlserverValidationValidationDetailOut"] = t.struct(
        {
            "type": t.string().optional(),
            "details": t.array(t.proxy(renames["SqlserverValidationDetailsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlserverValidationValidationDetailOut"])
    types["SapDiscoveryMetadataIn"] = t.struct(
        {
            "definedSystem": t.string().optional(),
            "sapProduct": t.string().optional(),
            "customerRegion": t.string().optional(),
            "environmentType": t.string().optional(),
        }
    ).named(renames["SapDiscoveryMetadataIn"])
    types["SapDiscoveryMetadataOut"] = t.struct(
        {
            "definedSystem": t.string().optional(),
            "sapProduct": t.string().optional(),
            "customerRegion": t.string().optional(),
            "environmentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryMetadataOut"])
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
    types["SapDiscoveryIn"] = t.struct(
        {
            "metadata": t.proxy(renames["SapDiscoveryMetadataIn"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentIn"]).optional(),
        }
    ).named(renames["SapDiscoveryIn"])
    types["SapDiscoveryOut"] = t.struct(
        {
            "metadata": t.proxy(renames["SapDiscoveryMetadataOut"]).optional(),
            "applicationLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "updateTime": t.string().optional(),
            "systemId": t.string().optional(),
            "databaseLayer": t.proxy(renames["SapDiscoveryComponentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExecutionResultIn"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "severity": t.string().optional(),
            "rule": t.string().optional(),
            "violationMessage": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsIn"]).optional(),
        }
    ).named(renames["ExecutionResultIn"])
    types["ExecutionResultOut"] = t.struct(
        {
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "severity": t.string().optional(),
            "rule": t.string().optional(),
            "violationMessage": t.string().optional(),
            "documentationUrl": t.string().optional(),
            "violationDetails": t.proxy(renames["ViolationDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResultOut"])
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
    types["RunEvaluationRequestIn"] = t.struct(
        {
            "execution": t.proxy(renames["ExecutionIn"]),
            "requestId": t.string().optional(),
            "executionId": t.string(),
        }
    ).named(renames["RunEvaluationRequestIn"])
    types["RunEvaluationRequestOut"] = t.struct(
        {
            "execution": t.proxy(renames["ExecutionOut"]),
            "requestId": t.string().optional(),
            "executionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RunEvaluationRequestOut"])
    types["SapDiscoveryResourceIn"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceUri": t.string().optional(),
        }
    ).named(renames["SapDiscoveryResourceIn"])
    types["SapDiscoveryResourceOut"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "relatedResources": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "resourceType": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapDiscoveryResourceOut"])
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
    types["ListEvaluationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationIn"])).optional(),
        }
    ).named(renames["ListEvaluationsResponseIn"])
    types["ListEvaluationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "evaluations": t.array(t.proxy(renames["EvaluationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEvaluationsResponseOut"])
    types["ScannedResourceIn"] = t.struct({"resource": t.string().optional()}).named(
        renames["ScannedResourceIn"]
    )
    types["ScannedResourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScannedResourceOut"])
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
    types["GceInstanceFilterIn"] = t.struct(
        {"serviceAccounts": t.array(t.string()).optional()}
    ).named(renames["GceInstanceFilterIn"])
    types["GceInstanceFilterOut"] = t.struct(
        {
            "serviceAccounts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceFilterOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["SqlserverValidationIn"] = t.struct(
        {
            "validationDetails": t.array(
                t.proxy(renames["SqlserverValidationValidationDetailIn"])
            ).optional(),
            "agentVersion": t.string().optional(),
        }
    ).named(renames["SqlserverValidationIn"])
    types["SqlserverValidationOut"] = t.struct(
        {
            "validationDetails": t.array(
                t.proxy(renames["SqlserverValidationValidationDetailOut"])
            ).optional(),
            "agentVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlserverValidationOut"])
    types["ResourceFilterIn"] = t.struct(
        {
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "scopes": t.array(t.string()).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterIn"]).optional(),
        }
    ).named(renames["ResourceFilterIn"])
    types["ResourceFilterOut"] = t.struct(
        {
            "resourceIdPatterns": t.array(t.string()).optional(),
            "inclusionLabels": t.struct({"_": t.string().optional()}).optional(),
            "scopes": t.array(t.string()).optional(),
            "gceInstanceFilter": t.proxy(renames["GceInstanceFilterOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceFilterOut"])
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
            "customRulesBucket": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
            "name": t.string().optional(),
            "schedule": t.string().optional(),
            "ruleNames": t.array(t.string()).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EvaluationIn"])
    types["EvaluationOut"] = t.struct(
        {
            "resourceStatus": t.proxy(renames["ResourceStatusOut"]).optional(),
            "customRulesBucket": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "ruleVersions": t.array(t.string()).optional(),
            "resourceFilter": t.proxy(renames["ResourceFilterOut"]).optional(),
            "name": t.string().optional(),
            "schedule": t.string().optional(),
            "ruleNames": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EvaluationOut"])
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
    types["InsightIn"] = t.struct(
        {
            "sapDiscovery": t.proxy(renames["SapDiscoveryIn"]).optional(),
            "sqlserverValidation": t.proxy(renames["SqlserverValidationIn"]).optional(),
            "sapValidation": t.proxy(renames["SapValidationIn"]).optional(),
            "instanceId": t.string(),
        }
    ).named(renames["InsightIn"])
    types["InsightOut"] = t.struct(
        {
            "sapDiscovery": t.proxy(renames["SapDiscoveryOut"]).optional(),
            "sqlserverValidation": t.proxy(
                renames["SqlserverValidationOut"]
            ).optional(),
            "sapValidation": t.proxy(renames["SapValidationOut"]).optional(),
            "instanceId": t.string(),
            "sentTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsightOut"])
    types["WriteInsightResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WriteInsightResponseIn"]
    )
    types["WriteInsightResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WriteInsightResponseOut"])
    types["SapValidationValidationDetailIn"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "sapValidationType": t.string().optional(),
        }
    ).named(renames["SapValidationValidationDetailIn"])
    types["SapValidationValidationDetailOut"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "sapValidationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SapValidationValidationDetailOut"])
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
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
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
    types["RuleIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "uri": t.string().optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "remediation": t.string().optional(),
        }
    ).named(renames["RuleIn"])
    types["RuleOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "secondaryCategory": t.string().optional(),
            "uri": t.string().optional(),
            "errorMessage": t.string().optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "primaryCategory": t.string().optional(),
            "remediation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuleOut"])

    functions = {}
    functions["projectsLocationsGet"] = workloadmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsOperationsList"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsOperationsDelete"] = workloadmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsCreate"] = workloadmanager.get(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEvaluationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsGet"] = workloadmanager.get(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEvaluationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsList"] = workloadmanager.get(
        "v1/{parent}/evaluations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEvaluationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsRun"] = workloadmanager.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEvaluationsExecutionsGet"] = workloadmanager.get(
        "v1/{parent}/executions",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "orderBy": t.string().optional(),
                "rule": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListExecutionResultsResponseOut"]),
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
                "customRulesBucket": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
