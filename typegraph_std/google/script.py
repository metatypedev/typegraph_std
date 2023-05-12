from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_script() -> Import:
    script = HTTPRuntime("https://script.googleapis.com/")

    renames = {
        "ErrorResponse": "_script_1_ErrorResponse",
        "GoogleAppsScriptTypeFunctionSetIn": "_script_2_GoogleAppsScriptTypeFunctionSetIn",
        "GoogleAppsScriptTypeFunctionSetOut": "_script_3_GoogleAppsScriptTypeFunctionSetOut",
        "GoogleAppsScriptTypeExecutionApiEntryPointIn": "_script_4_GoogleAppsScriptTypeExecutionApiEntryPointIn",
        "GoogleAppsScriptTypeExecutionApiEntryPointOut": "_script_5_GoogleAppsScriptTypeExecutionApiEntryPointOut",
        "ScriptExecutionResultIn": "_script_6_ScriptExecutionResultIn",
        "ScriptExecutionResultOut": "_script_7_ScriptExecutionResultOut",
        "ExecutionResponseIn": "_script_8_ExecutionResponseIn",
        "ExecutionResponseOut": "_script_9_ExecutionResponseOut",
        "GoogleAppsScriptTypeExecutionApiConfigIn": "_script_10_GoogleAppsScriptTypeExecutionApiConfigIn",
        "GoogleAppsScriptTypeExecutionApiConfigOut": "_script_11_GoogleAppsScriptTypeExecutionApiConfigOut",
        "FileIn": "_script_12_FileIn",
        "FileOut": "_script_13_FileOut",
        "GoogleAppsScriptTypeProcessIn": "_script_14_GoogleAppsScriptTypeProcessIn",
        "GoogleAppsScriptTypeProcessOut": "_script_15_GoogleAppsScriptTypeProcessOut",
        "CreateProjectRequestIn": "_script_16_CreateProjectRequestIn",
        "CreateProjectRequestOut": "_script_17_CreateProjectRequestOut",
        "ExecutionErrorIn": "_script_18_ExecutionErrorIn",
        "ExecutionErrorOut": "_script_19_ExecutionErrorOut",
        "OperationIn": "_script_20_OperationIn",
        "OperationOut": "_script_21_OperationOut",
        "ListDeploymentsResponseIn": "_script_22_ListDeploymentsResponseIn",
        "ListDeploymentsResponseOut": "_script_23_ListDeploymentsResponseOut",
        "ListScriptProcessesResponseIn": "_script_24_ListScriptProcessesResponseIn",
        "ListScriptProcessesResponseOut": "_script_25_ListScriptProcessesResponseOut",
        "DeploymentConfigIn": "_script_26_DeploymentConfigIn",
        "DeploymentConfigOut": "_script_27_DeploymentConfigOut",
        "StatusIn": "_script_28_StatusIn",
        "StatusOut": "_script_29_StatusOut",
        "GoogleAppsScriptTypeAddOnEntryPointIn": "_script_30_GoogleAppsScriptTypeAddOnEntryPointIn",
        "GoogleAppsScriptTypeAddOnEntryPointOut": "_script_31_GoogleAppsScriptTypeAddOnEntryPointOut",
        "ProjectIn": "_script_32_ProjectIn",
        "ProjectOut": "_script_33_ProjectOut",
        "ListVersionsResponseIn": "_script_34_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_script_35_ListVersionsResponseOut",
        "ExecuteStreamResponseIn": "_script_36_ExecuteStreamResponseIn",
        "ExecuteStreamResponseOut": "_script_37_ExecuteStreamResponseOut",
        "DeploymentIn": "_script_38_DeploymentIn",
        "DeploymentOut": "_script_39_DeploymentOut",
        "ListUserProcessesResponseIn": "_script_40_ListUserProcessesResponseIn",
        "ListUserProcessesResponseOut": "_script_41_ListUserProcessesResponseOut",
        "GoogleAppsScriptTypeUserIn": "_script_42_GoogleAppsScriptTypeUserIn",
        "GoogleAppsScriptTypeUserOut": "_script_43_GoogleAppsScriptTypeUserOut",
        "GoogleAppsScriptTypeFunctionIn": "_script_44_GoogleAppsScriptTypeFunctionIn",
        "GoogleAppsScriptTypeFunctionOut": "_script_45_GoogleAppsScriptTypeFunctionOut",
        "GoogleAppsScriptTypeWebAppConfigIn": "_script_46_GoogleAppsScriptTypeWebAppConfigIn",
        "GoogleAppsScriptTypeWebAppConfigOut": "_script_47_GoogleAppsScriptTypeWebAppConfigOut",
        "ContentIn": "_script_48_ContentIn",
        "ContentOut": "_script_49_ContentOut",
        "UpdateDeploymentRequestIn": "_script_50_UpdateDeploymentRequestIn",
        "UpdateDeploymentRequestOut": "_script_51_UpdateDeploymentRequestOut",
        "EntryPointIn": "_script_52_EntryPointIn",
        "EntryPointOut": "_script_53_EntryPointOut",
        "EmptyIn": "_script_54_EmptyIn",
        "EmptyOut": "_script_55_EmptyOut",
        "GoogleAppsScriptTypeWebAppEntryPointIn": "_script_56_GoogleAppsScriptTypeWebAppEntryPointIn",
        "GoogleAppsScriptTypeWebAppEntryPointOut": "_script_57_GoogleAppsScriptTypeWebAppEntryPointOut",
        "MetricsIn": "_script_58_MetricsIn",
        "MetricsOut": "_script_59_MetricsOut",
        "VersionIn": "_script_60_VersionIn",
        "VersionOut": "_script_61_VersionOut",
        "ExecutionRequestIn": "_script_62_ExecutionRequestIn",
        "ExecutionRequestOut": "_script_63_ExecutionRequestOut",
        "ListValueIn": "_script_64_ListValueIn",
        "ListValueOut": "_script_65_ListValueOut",
        "ValueIn": "_script_66_ValueIn",
        "ValueOut": "_script_67_ValueOut",
        "ScriptStackTraceElementIn": "_script_68_ScriptStackTraceElementIn",
        "ScriptStackTraceElementOut": "_script_69_ScriptStackTraceElementOut",
        "MetricsValueIn": "_script_70_MetricsValueIn",
        "MetricsValueOut": "_script_71_MetricsValueOut",
        "StructIn": "_script_72_StructIn",
        "StructOut": "_script_73_StructOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsScriptTypeFunctionSetIn"] = t.struct(
        {
            "values": t.array(
                t.proxy(renames["GoogleAppsScriptTypeFunctionIn"])
            ).optional()
        }
    ).named(renames["GoogleAppsScriptTypeFunctionSetIn"])
    types["GoogleAppsScriptTypeFunctionSetOut"] = t.struct(
        {
            "values": t.array(
                t.proxy(renames["GoogleAppsScriptTypeFunctionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeFunctionSetOut"])
    types["GoogleAppsScriptTypeExecutionApiEntryPointIn"] = t.struct(
        {
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiConfigIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsScriptTypeExecutionApiEntryPointIn"])
    types["GoogleAppsScriptTypeExecutionApiEntryPointOut"] = t.struct(
        {
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeExecutionApiEntryPointOut"])
    types["ScriptExecutionResultIn"] = t.struct(
        {"returnValue": t.proxy(renames["ValueIn"]).optional()}
    ).named(renames["ScriptExecutionResultIn"])
    types["ScriptExecutionResultOut"] = t.struct(
        {
            "returnValue": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptExecutionResultOut"])
    types["ExecutionResponseIn"] = t.struct(
        {"result": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecutionResponseIn"])
    types["ExecutionResponseOut"] = t.struct(
        {
            "result": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResponseOut"])
    types["GoogleAppsScriptTypeExecutionApiConfigIn"] = t.struct(
        {"access": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigIn"])
    types["GoogleAppsScriptTypeExecutionApiConfigOut"] = t.struct(
        {
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigOut"])
    types["FileIn"] = t.struct(
        {
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "source": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetIn"]
            ).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "source": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["GoogleAppsScriptTypeProcessIn"] = t.struct(
        {
            "userAccessLevel": t.string().optional(),
            "functionName": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
            "processStatus": t.string().optional(),
            "projectName": t.string().optional(),
            "processType": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessIn"])
    types["GoogleAppsScriptTypeProcessOut"] = t.struct(
        {
            "userAccessLevel": t.string().optional(),
            "functionName": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
            "processStatus": t.string().optional(),
            "projectName": t.string().optional(),
            "processType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessOut"])
    types["CreateProjectRequestIn"] = t.struct(
        {"parentId": t.string().optional(), "title": t.string().optional()}
    ).named(renames["CreateProjectRequestIn"])
    types["CreateProjectRequestOut"] = t.struct(
        {
            "parentId": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProjectRequestOut"])
    types["ExecutionErrorIn"] = t.struct(
        {
            "errorType": t.string().optional(),
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementIn"])
            ).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ExecutionErrorIn"])
    types["ExecutionErrorOut"] = t.struct(
        {
            "errorType": t.string().optional(),
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementOut"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionErrorOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListDeploymentsResponseIn"] = t.struct(
        {
            "deployments": t.array(t.proxy(renames["DeploymentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDeploymentsResponseIn"])
    types["ListDeploymentsResponseOut"] = t.struct(
        {
            "deployments": t.array(t.proxy(renames["DeploymentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeploymentsResponseOut"])
    types["ListScriptProcessesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessIn"])
            ).optional(),
        }
    ).named(renames["ListScriptProcessesResponseIn"])
    types["ListScriptProcessesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScriptProcessesResponseOut"])
    types["DeploymentConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "manifestFileName": t.string().optional(),
        }
    ).named(renames["DeploymentConfigIn"])
    types["DeploymentConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "manifestFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleAppsScriptTypeAddOnEntryPointIn"] = t.struct(
        {
            "addOnType": t.string().optional(),
            "description": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointIn"])
    types["GoogleAppsScriptTypeAddOnEntryPointOut"] = t.struct(
        {
            "addOnType": t.string().optional(),
            "description": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointOut"])
    types["ProjectIn"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "updateTime": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "title": t.string().optional(),
            "parentId": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserOut"]).optional(),
            "updateTime": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "title": t.string().optional(),
            "parentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ExecuteStreamResponseIn"] = t.struct(
        {"result": t.proxy(renames["ScriptExecutionResultIn"]).optional()}
    ).named(renames["ExecuteStreamResponseIn"])
    types["ExecuteStreamResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["ScriptExecutionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteStreamResponseOut"])
    types["DeploymentIn"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
            "deploymentId": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "deploymentId": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["ListUserProcessesResponseIn"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserProcessesResponseIn"])
    types["ListUserProcessesResponseOut"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserProcessesResponseOut"])
    types["GoogleAppsScriptTypeUserIn"] = t.struct(
        {
            "email": t.string().optional(),
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserIn"])
    types["GoogleAppsScriptTypeUserOut"] = t.struct(
        {
            "email": t.string().optional(),
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserOut"])
    types["GoogleAppsScriptTypeFunctionIn"] = t.struct(
        {"name": t.string().optional(), "parameters": t.array(t.string()).optional()}
    ).named(renames["GoogleAppsScriptTypeFunctionIn"])
    types["GoogleAppsScriptTypeFunctionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parameters": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeFunctionOut"])
    types["GoogleAppsScriptTypeWebAppConfigIn"] = t.struct(
        {"access": t.string().optional(), "executeAs": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeWebAppConfigIn"])
    types["GoogleAppsScriptTypeWebAppConfigOut"] = t.struct(
        {
            "access": t.string().optional(),
            "executeAs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppConfigOut"])
    types["ContentIn"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
        }
    ).named(renames["ContentIn"])
    types["ContentOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOut"])
    types["UpdateDeploymentRequestIn"] = t.struct(
        {"deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional()}
    ).named(renames["UpdateDeploymentRequestIn"])
    types["UpdateDeploymentRequestOut"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeploymentRequestOut"])
    types["EntryPointIn"] = t.struct(
        {
            "entryPointType": t.string().optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointIn"]
            ).optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointIn"]
            ).optional(),
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointIn"]
            ).optional(),
        }
    ).named(renames["EntryPointIn"])
    types["EntryPointOut"] = t.struct(
        {
            "entryPointType": t.string().optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointOut"]
            ).optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointOut"]
            ).optional(),
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryPointOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleAppsScriptTypeWebAppEntryPointIn"] = t.struct(
        {
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeWebAppConfigIn"]
            ).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppEntryPointIn"])
    types["GoogleAppsScriptTypeWebAppEntryPointOut"] = t.struct(
        {
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeWebAppConfigOut"]
            ).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppEntryPointOut"])
    types["MetricsIn"] = t.struct(
        {
            "failedExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "activeUsers": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "failedExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "activeUsers": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
    types["VersionIn"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["ExecutionRequestIn"] = t.struct(
        {
            "devMode": t.boolean().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "sessionState": t.string().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["ExecutionRequestIn"])
    types["ExecutionRequestOut"] = t.struct(
        {
            "devMode": t.boolean().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "sessionState": t.string().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionRequestOut"])
    types["ListValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ListValueIn"])
    types["ListValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListValueOut"])
    types["ValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "structValue": t.proxy(renames["StructIn"]).optional(),
            "stringValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "dateValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueIn"]).optional(),
            "nullValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "structValue": t.proxy(renames["StructOut"]).optional(),
            "stringValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "dateValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueOut"]).optional(),
            "nullValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["ScriptStackTraceElementIn"] = t.struct(
        {"function": t.string().optional(), "lineNumber": t.integer().optional()}
    ).named(renames["ScriptStackTraceElementIn"])
    types["ScriptStackTraceElementOut"] = t.struct(
        {
            "function": t.string().optional(),
            "lineNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptStackTraceElementOut"])
    types["MetricsValueIn"] = t.struct(
        {"startTime": t.string(), "value": t.string().optional(), "endTime": t.string()}
    ).named(renames["MetricsValueIn"])
    types["MetricsValueOut"] = t.struct(
        {
            "startTime": t.string(),
            "value": t.string().optional(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsValueOut"])
    types["StructIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["StructIn"])
    types["StructOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructOut"])

    functions = {}
    functions["processesListScriptProcesses"] = script.get(
        "v1/processes",
        t.struct(
            {
                "userProcessFilter.types": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
                "userProcessFilter.deploymentId": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.functionName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserProcessesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["processesList"] = script.get(
        "v1/processes",
        t.struct(
            {
                "userProcessFilter.types": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
                "userProcessFilter.deploymentId": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.functionName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserProcessesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scriptsRun"] = script.post(
        "v1/scripts/{scriptId}:run",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "devMode": t.boolean().optional(),
                "parameters": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "sessionState": t.string().optional(),
                "function": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetMetrics"] = script.post(
        "v1/projects",
        t.struct(
            {
                "parentId": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetContent"] = script.post(
        "v1/projects",
        t.struct(
            {
                "parentId": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateContent"] = script.post(
        "v1/projects",
        t.struct(
            {
                "parentId": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = script.post(
        "v1/projects",
        t.struct(
            {
                "parentId": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = script.post(
        "v1/projects",
        t.struct(
            {
                "parentId": t.string().optional(),
                "title": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsCreate"] = script.delete(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsUpdate"] = script.delete(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsGet"] = script.delete(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsList"] = script.delete(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsDelete"] = script.delete(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsCreate"] = script.get(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsGet"] = script.get(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsList"] = script.get(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="script", renames=renames, types=Box(types), functions=Box(functions)
    )
