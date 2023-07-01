from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_script():
    script = HTTPRuntime("https://script.googleapis.com/")

    renames = {
        "ErrorResponse": "_script_1_ErrorResponse",
        "GoogleAppsScriptTypeWebAppConfigIn": "_script_2_GoogleAppsScriptTypeWebAppConfigIn",
        "GoogleAppsScriptTypeWebAppConfigOut": "_script_3_GoogleAppsScriptTypeWebAppConfigOut",
        "CreateProjectRequestIn": "_script_4_CreateProjectRequestIn",
        "CreateProjectRequestOut": "_script_5_CreateProjectRequestOut",
        "EntryPointIn": "_script_6_EntryPointIn",
        "EntryPointOut": "_script_7_EntryPointOut",
        "ScriptExecutionResultIn": "_script_8_ScriptExecutionResultIn",
        "ScriptExecutionResultOut": "_script_9_ScriptExecutionResultOut",
        "ListVersionsResponseIn": "_script_10_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_script_11_ListVersionsResponseOut",
        "ListUserProcessesResponseIn": "_script_12_ListUserProcessesResponseIn",
        "ListUserProcessesResponseOut": "_script_13_ListUserProcessesResponseOut",
        "ProjectIn": "_script_14_ProjectIn",
        "ProjectOut": "_script_15_ProjectOut",
        "ExecutionResponseIn": "_script_16_ExecutionResponseIn",
        "ExecutionResponseOut": "_script_17_ExecutionResponseOut",
        "ExecutionRequestIn": "_script_18_ExecutionRequestIn",
        "ExecutionRequestOut": "_script_19_ExecutionRequestOut",
        "ListValueIn": "_script_20_ListValueIn",
        "ListValueOut": "_script_21_ListValueOut",
        "EmptyIn": "_script_22_EmptyIn",
        "EmptyOut": "_script_23_EmptyOut",
        "GoogleAppsScriptTypeWebAppEntryPointIn": "_script_24_GoogleAppsScriptTypeWebAppEntryPointIn",
        "GoogleAppsScriptTypeWebAppEntryPointOut": "_script_25_GoogleAppsScriptTypeWebAppEntryPointOut",
        "GoogleAppsScriptTypeExecutionApiEntryPointIn": "_script_26_GoogleAppsScriptTypeExecutionApiEntryPointIn",
        "GoogleAppsScriptTypeExecutionApiEntryPointOut": "_script_27_GoogleAppsScriptTypeExecutionApiEntryPointOut",
        "GoogleAppsScriptTypeUserIn": "_script_28_GoogleAppsScriptTypeUserIn",
        "GoogleAppsScriptTypeUserOut": "_script_29_GoogleAppsScriptTypeUserOut",
        "ListScriptProcessesResponseIn": "_script_30_ListScriptProcessesResponseIn",
        "ListScriptProcessesResponseOut": "_script_31_ListScriptProcessesResponseOut",
        "ExecuteStreamResponseIn": "_script_32_ExecuteStreamResponseIn",
        "ExecuteStreamResponseOut": "_script_33_ExecuteStreamResponseOut",
        "DeploymentIn": "_script_34_DeploymentIn",
        "DeploymentOut": "_script_35_DeploymentOut",
        "GoogleAppsScriptTypeExecutionApiConfigIn": "_script_36_GoogleAppsScriptTypeExecutionApiConfigIn",
        "GoogleAppsScriptTypeExecutionApiConfigOut": "_script_37_GoogleAppsScriptTypeExecutionApiConfigOut",
        "GoogleAppsScriptTypeFunctionIn": "_script_38_GoogleAppsScriptTypeFunctionIn",
        "GoogleAppsScriptTypeFunctionOut": "_script_39_GoogleAppsScriptTypeFunctionOut",
        "DeploymentConfigIn": "_script_40_DeploymentConfigIn",
        "DeploymentConfigOut": "_script_41_DeploymentConfigOut",
        "FileIn": "_script_42_FileIn",
        "FileOut": "_script_43_FileOut",
        "ExecutionErrorIn": "_script_44_ExecutionErrorIn",
        "ExecutionErrorOut": "_script_45_ExecutionErrorOut",
        "ListDeploymentsResponseIn": "_script_46_ListDeploymentsResponseIn",
        "ListDeploymentsResponseOut": "_script_47_ListDeploymentsResponseOut",
        "ContentIn": "_script_48_ContentIn",
        "ContentOut": "_script_49_ContentOut",
        "MetricsIn": "_script_50_MetricsIn",
        "MetricsOut": "_script_51_MetricsOut",
        "GoogleAppsScriptTypeFunctionSetIn": "_script_52_GoogleAppsScriptTypeFunctionSetIn",
        "GoogleAppsScriptTypeFunctionSetOut": "_script_53_GoogleAppsScriptTypeFunctionSetOut",
        "MetricsValueIn": "_script_54_MetricsValueIn",
        "MetricsValueOut": "_script_55_MetricsValueOut",
        "StructIn": "_script_56_StructIn",
        "StructOut": "_script_57_StructOut",
        "ScriptStackTraceElementIn": "_script_58_ScriptStackTraceElementIn",
        "ScriptStackTraceElementOut": "_script_59_ScriptStackTraceElementOut",
        "OperationIn": "_script_60_OperationIn",
        "OperationOut": "_script_61_OperationOut",
        "UpdateDeploymentRequestIn": "_script_62_UpdateDeploymentRequestIn",
        "UpdateDeploymentRequestOut": "_script_63_UpdateDeploymentRequestOut",
        "ValueIn": "_script_64_ValueIn",
        "ValueOut": "_script_65_ValueOut",
        "VersionIn": "_script_66_VersionIn",
        "VersionOut": "_script_67_VersionOut",
        "GoogleAppsScriptTypeProcessIn": "_script_68_GoogleAppsScriptTypeProcessIn",
        "GoogleAppsScriptTypeProcessOut": "_script_69_GoogleAppsScriptTypeProcessOut",
        "GoogleAppsScriptTypeAddOnEntryPointIn": "_script_70_GoogleAppsScriptTypeAddOnEntryPointIn",
        "GoogleAppsScriptTypeAddOnEntryPointOut": "_script_71_GoogleAppsScriptTypeAddOnEntryPointOut",
        "StatusIn": "_script_72_StatusIn",
        "StatusOut": "_script_73_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsScriptTypeWebAppConfigIn"] = t.struct(
        {"executeAs": t.string().optional(), "access": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeWebAppConfigIn"])
    types["GoogleAppsScriptTypeWebAppConfigOut"] = t.struct(
        {
            "executeAs": t.string().optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppConfigOut"])
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
    types["ScriptExecutionResultIn"] = t.struct(
        {"returnValue": t.proxy(renames["ValueIn"]).optional()}
    ).named(renames["ScriptExecutionResultIn"])
    types["ScriptExecutionResultOut"] = t.struct(
        {
            "returnValue": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptExecutionResultOut"])
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
    types["ListUserProcessesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessIn"])
            ).optional(),
        }
    ).named(renames["ListUserProcessesResponseIn"])
    types["ListUserProcessesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserProcessesResponseOut"])
    types["ProjectIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "title": t.string().optional(),
            "parentId": t.string().optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "title": t.string().optional(),
            "parentId": t.string().optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["ExecutionResponseIn"] = t.struct(
        {"result": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecutionResponseIn"])
    types["ExecutionResponseOut"] = t.struct(
        {
            "result": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResponseOut"])
    types["ExecutionRequestIn"] = t.struct(
        {
            "devMode": t.boolean().optional(),
            "function": t.string().optional(),
            "sessionState": t.string().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["ExecutionRequestIn"])
    types["ExecutionRequestOut"] = t.struct(
        {
            "devMode": t.boolean().optional(),
            "function": t.string().optional(),
            "sessionState": t.string().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleAppsScriptTypeWebAppEntryPointIn"] = t.struct(
        {
            "url": t.string().optional(),
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeWebAppConfigIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppEntryPointIn"])
    types["GoogleAppsScriptTypeWebAppEntryPointOut"] = t.struct(
        {
            "url": t.string().optional(),
            "entryPointConfig": t.proxy(
                renames["GoogleAppsScriptTypeWebAppConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeWebAppEntryPointOut"])
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
    types["GoogleAppsScriptTypeUserIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "photoUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserIn"])
    types["GoogleAppsScriptTypeUserOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "photoUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserOut"])
    types["ListScriptProcessesResponseIn"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListScriptProcessesResponseIn"])
    types["ListScriptProcessesResponseOut"] = t.struct(
        {
            "processes": t.array(
                t.proxy(renames["GoogleAppsScriptTypeProcessOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScriptProcessesResponseOut"])
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
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
            "updateTime": t.string().optional(),
            "deploymentId": t.string().optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "deploymentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["GoogleAppsScriptTypeExecutionApiConfigIn"] = t.struct(
        {"access": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigIn"])
    types["GoogleAppsScriptTypeExecutionApiConfigOut"] = t.struct(
        {
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigOut"])
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
    types["DeploymentConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
            "manifestFileName": t.string().optional(),
            "versionNumber": t.integer().optional(),
        }
    ).named(renames["DeploymentConfigIn"])
    types["DeploymentConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
            "manifestFileName": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentConfigOut"])
    types["FileIn"] = t.struct(
        {
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetIn"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "source": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "source": t.string().optional(),
            "createTime": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["ExecutionErrorIn"] = t.struct(
        {
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementIn"])
            ).optional(),
            "errorType": t.string().optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["ExecutionErrorIn"])
    types["ExecutionErrorOut"] = t.struct(
        {
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementOut"])
            ).optional(),
            "errorType": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionErrorOut"])
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
    types["ContentIn"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileIn"])).optional(),
            "scriptId": t.string().optional(),
        }
    ).named(renames["ContentIn"])
    types["ContentOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileOut"])).optional(),
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentOut"])
    types["MetricsIn"] = t.struct(
        {
            "totalExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "activeUsers": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "totalExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "activeUsers": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
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
    types["MetricsValueIn"] = t.struct(
        {"startTime": t.string(), "endTime": t.string(), "value": t.string().optional()}
    ).named(renames["MetricsValueIn"])
    types["MetricsValueOut"] = t.struct(
        {
            "startTime": t.string(),
            "endTime": t.string(),
            "value": t.string().optional(),
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["UpdateDeploymentRequestIn"] = t.struct(
        {"deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional()}
    ).named(renames["UpdateDeploymentRequestIn"])
    types["UpdateDeploymentRequestOut"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeploymentRequestOut"])
    types["ValueIn"] = t.struct(
        {
            "dateValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "structValue": t.proxy(renames["StructIn"]).optional(),
            "nullValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueIn"]).optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "dateValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "stringValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "structValue": t.proxy(renames["StructOut"]).optional(),
            "nullValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueOut"]).optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["VersionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "description": t.string().optional(),
            "versionNumber": t.integer().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "description": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["GoogleAppsScriptTypeProcessIn"] = t.struct(
        {
            "projectName": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "processStatus": t.string().optional(),
            "startTime": t.string().optional(),
            "processType": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "functionName": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessIn"])
    types["GoogleAppsScriptTypeProcessOut"] = t.struct(
        {
            "projectName": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "processStatus": t.string().optional(),
            "startTime": t.string().optional(),
            "processType": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "functionName": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessOut"])
    types["GoogleAppsScriptTypeAddOnEntryPointIn"] = t.struct(
        {
            "addOnType": t.string().optional(),
            "helpUrl": t.string().optional(),
            "title": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
            "description": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointIn"])
    types["GoogleAppsScriptTypeAddOnEntryPointOut"] = t.struct(
        {
            "addOnType": t.string().optional(),
            "helpUrl": t.string().optional(),
            "title": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
            "description": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointOut"])
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

    functions = {}
    functions["projectsGetContent"] = script.get(
        "v1/projects/{scriptId}",
        t.struct({"scriptId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetMetrics"] = script.get(
        "v1/projects/{scriptId}",
        t.struct({"scriptId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateContent"] = script.get(
        "v1/projects/{scriptId}",
        t.struct({"scriptId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = script.get(
        "v1/projects/{scriptId}",
        t.struct({"scriptId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = script.get(
        "v1/projects/{scriptId}",
        t.struct({"scriptId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsGet"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsUpdate"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsDelete"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsCreate"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsList"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsGet"] = script.post(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "createTime": t.string().optional(),
                "description": t.string().optional(),
                "versionNumber": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsList"] = script.post(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "createTime": t.string().optional(),
                "description": t.string().optional(),
                "versionNumber": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsVersionsCreate"] = script.post(
        "v1/projects/{scriptId}/versions",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "createTime": t.string().optional(),
                "description": t.string().optional(),
                "versionNumber": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["processesListScriptProcesses"] = script.get(
        "v1/processes",
        t.struct(
            {
                "userProcessFilter.functionName": t.string().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "userProcessFilter.deploymentId": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.types": t.string().optional(),
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
                "userProcessFilter.functionName": t.string().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "userProcessFilter.deploymentId": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.types": t.string().optional(),
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
                "function": t.string().optional(),
                "sessionState": t.string().optional(),
                "parameters": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="script", renames=renames, types=Box(types), functions=Box(functions)
    )
