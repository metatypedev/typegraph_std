from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_script() -> Import:
    script = HTTPRuntime("https://script.googleapis.com/")

    renames = {
        "ErrorResponse": "_script_1_ErrorResponse",
        "ListValueIn": "_script_2_ListValueIn",
        "ListValueOut": "_script_3_ListValueOut",
        "EmptyIn": "_script_4_EmptyIn",
        "EmptyOut": "_script_5_EmptyOut",
        "MetricsIn": "_script_6_MetricsIn",
        "MetricsOut": "_script_7_MetricsOut",
        "GoogleAppsScriptTypeExecutionApiConfigIn": "_script_8_GoogleAppsScriptTypeExecutionApiConfigIn",
        "GoogleAppsScriptTypeExecutionApiConfigOut": "_script_9_GoogleAppsScriptTypeExecutionApiConfigOut",
        "CreateProjectRequestIn": "_script_10_CreateProjectRequestIn",
        "CreateProjectRequestOut": "_script_11_CreateProjectRequestOut",
        "GoogleAppsScriptTypeFunctionSetIn": "_script_12_GoogleAppsScriptTypeFunctionSetIn",
        "GoogleAppsScriptTypeFunctionSetOut": "_script_13_GoogleAppsScriptTypeFunctionSetOut",
        "GoogleAppsScriptTypeFunctionIn": "_script_14_GoogleAppsScriptTypeFunctionIn",
        "GoogleAppsScriptTypeFunctionOut": "_script_15_GoogleAppsScriptTypeFunctionOut",
        "ProjectIn": "_script_16_ProjectIn",
        "ProjectOut": "_script_17_ProjectOut",
        "MetricsValueIn": "_script_18_MetricsValueIn",
        "MetricsValueOut": "_script_19_MetricsValueOut",
        "ValueIn": "_script_20_ValueIn",
        "ValueOut": "_script_21_ValueOut",
        "VersionIn": "_script_22_VersionIn",
        "VersionOut": "_script_23_VersionOut",
        "UpdateDeploymentRequestIn": "_script_24_UpdateDeploymentRequestIn",
        "UpdateDeploymentRequestOut": "_script_25_UpdateDeploymentRequestOut",
        "DeploymentConfigIn": "_script_26_DeploymentConfigIn",
        "DeploymentConfigOut": "_script_27_DeploymentConfigOut",
        "GoogleAppsScriptTypeUserIn": "_script_28_GoogleAppsScriptTypeUserIn",
        "GoogleAppsScriptTypeUserOut": "_script_29_GoogleAppsScriptTypeUserOut",
        "GoogleAppsScriptTypeWebAppConfigIn": "_script_30_GoogleAppsScriptTypeWebAppConfigIn",
        "GoogleAppsScriptTypeWebAppConfigOut": "_script_31_GoogleAppsScriptTypeWebAppConfigOut",
        "ExecutionResponseIn": "_script_32_ExecutionResponseIn",
        "ExecutionResponseOut": "_script_33_ExecutionResponseOut",
        "FileIn": "_script_34_FileIn",
        "FileOut": "_script_35_FileOut",
        "ContentIn": "_script_36_ContentIn",
        "ContentOut": "_script_37_ContentOut",
        "ScriptExecutionResultIn": "_script_38_ScriptExecutionResultIn",
        "ScriptExecutionResultOut": "_script_39_ScriptExecutionResultOut",
        "OperationIn": "_script_40_OperationIn",
        "OperationOut": "_script_41_OperationOut",
        "GoogleAppsScriptTypeWebAppEntryPointIn": "_script_42_GoogleAppsScriptTypeWebAppEntryPointIn",
        "GoogleAppsScriptTypeWebAppEntryPointOut": "_script_43_GoogleAppsScriptTypeWebAppEntryPointOut",
        "StatusIn": "_script_44_StatusIn",
        "StatusOut": "_script_45_StatusOut",
        "GoogleAppsScriptTypeAddOnEntryPointIn": "_script_46_GoogleAppsScriptTypeAddOnEntryPointIn",
        "GoogleAppsScriptTypeAddOnEntryPointOut": "_script_47_GoogleAppsScriptTypeAddOnEntryPointOut",
        "ListDeploymentsResponseIn": "_script_48_ListDeploymentsResponseIn",
        "ListDeploymentsResponseOut": "_script_49_ListDeploymentsResponseOut",
        "ExecuteStreamResponseIn": "_script_50_ExecuteStreamResponseIn",
        "ExecuteStreamResponseOut": "_script_51_ExecuteStreamResponseOut",
        "ScriptStackTraceElementIn": "_script_52_ScriptStackTraceElementIn",
        "ScriptStackTraceElementOut": "_script_53_ScriptStackTraceElementOut",
        "ListVersionsResponseIn": "_script_54_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_script_55_ListVersionsResponseOut",
        "EntryPointIn": "_script_56_EntryPointIn",
        "EntryPointOut": "_script_57_EntryPointOut",
        "GoogleAppsScriptTypeExecutionApiEntryPointIn": "_script_58_GoogleAppsScriptTypeExecutionApiEntryPointIn",
        "GoogleAppsScriptTypeExecutionApiEntryPointOut": "_script_59_GoogleAppsScriptTypeExecutionApiEntryPointOut",
        "GoogleAppsScriptTypeProcessIn": "_script_60_GoogleAppsScriptTypeProcessIn",
        "GoogleAppsScriptTypeProcessOut": "_script_61_GoogleAppsScriptTypeProcessOut",
        "ListUserProcessesResponseIn": "_script_62_ListUserProcessesResponseIn",
        "ListUserProcessesResponseOut": "_script_63_ListUserProcessesResponseOut",
        "DeploymentIn": "_script_64_DeploymentIn",
        "DeploymentOut": "_script_65_DeploymentOut",
        "ExecutionRequestIn": "_script_66_ExecutionRequestIn",
        "ExecutionRequestOut": "_script_67_ExecutionRequestOut",
        "StructIn": "_script_68_StructIn",
        "StructOut": "_script_69_StructOut",
        "ExecutionErrorIn": "_script_70_ExecutionErrorIn",
        "ExecutionErrorOut": "_script_71_ExecutionErrorOut",
        "ListScriptProcessesResponseIn": "_script_72_ListScriptProcessesResponseIn",
        "ListScriptProcessesResponseOut": "_script_73_ListScriptProcessesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MetricsIn"] = t.struct(
        {
            "activeUsers": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "activeUsers": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
    types["GoogleAppsScriptTypeExecutionApiConfigIn"] = t.struct(
        {"access": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigIn"])
    types["GoogleAppsScriptTypeExecutionApiConfigOut"] = t.struct(
        {
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeExecutionApiConfigOut"])
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
    types["GoogleAppsScriptTypeFunctionIn"] = t.struct(
        {"parameters": t.array(t.string()).optional(), "name": t.string().optional()}
    ).named(renames["GoogleAppsScriptTypeFunctionIn"])
    types["GoogleAppsScriptTypeFunctionOut"] = t.struct(
        {
            "parameters": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeFunctionOut"])
    types["ProjectIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "parentId": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "scriptId": t.string().optional(),
            "parentId": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["MetricsValueIn"] = t.struct(
        {"endTime": t.string(), "value": t.string().optional(), "startTime": t.string()}
    ).named(renames["MetricsValueIn"])
    types["MetricsValueOut"] = t.struct(
        {
            "endTime": t.string(),
            "value": t.string().optional(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsValueOut"])
    types["ValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "dateValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "structValue": t.proxy(renames["StructIn"]).optional(),
            "boolValue": t.boolean().optional(),
            "listValue": t.proxy(renames["ListValueIn"]).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "nullValue": t.string().optional(),
            "dateValue": t.string().optional(),
            "bytesValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "structValue": t.proxy(renames["StructOut"]).optional(),
            "boolValue": t.boolean().optional(),
            "listValue": t.proxy(renames["ListValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["VersionIn"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "scriptId": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["UpdateDeploymentRequestIn"] = t.struct(
        {"deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional()}
    ).named(renames["UpdateDeploymentRequestIn"])
    types["UpdateDeploymentRequestOut"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeploymentRequestOut"])
    types["DeploymentConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "manifestFileName": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "scriptId": t.string().optional(),
        }
    ).named(renames["DeploymentConfigIn"])
    types["DeploymentConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "manifestFileName": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentConfigOut"])
    types["GoogleAppsScriptTypeUserIn"] = t.struct(
        {
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "email": t.string().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserIn"])
    types["GoogleAppsScriptTypeUserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "email": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserOut"])
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
    types["ExecutionResponseIn"] = t.struct(
        {"result": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecutionResponseIn"])
    types["ExecutionResponseOut"] = t.struct(
        {
            "result": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionResponseOut"])
    types["FileIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetIn"]
            ).optional(),
            "source": t.string().optional(),
            "type": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetOut"]
            ).optional(),
            "source": t.string().optional(),
            "type": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
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
    types["ScriptExecutionResultIn"] = t.struct(
        {"returnValue": t.proxy(renames["ValueIn"]).optional()}
    ).named(renames["ScriptExecutionResultIn"])
    types["ScriptExecutionResultOut"] = t.struct(
        {
            "returnValue": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptExecutionResultOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["GoogleAppsScriptTypeAddOnEntryPointIn"] = t.struct(
        {
            "postInstallTipUrl": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
            "addOnType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointIn"])
    types["GoogleAppsScriptTypeAddOnEntryPointOut"] = t.struct(
        {
            "postInstallTipUrl": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "title": t.string().optional(),
            "helpUrl": t.string().optional(),
            "addOnType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointOut"])
    types["ListDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(t.proxy(renames["DeploymentIn"])).optional(),
        }
    ).named(renames["ListDeploymentsResponseIn"])
    types["ListDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(t.proxy(renames["DeploymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDeploymentsResponseOut"])
    types["ExecuteStreamResponseIn"] = t.struct(
        {"result": t.proxy(renames["ScriptExecutionResultIn"]).optional()}
    ).named(renames["ExecuteStreamResponseIn"])
    types["ExecuteStreamResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["ScriptExecutionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteStreamResponseOut"])
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
    types["EntryPointIn"] = t.struct(
        {
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointIn"]
            ).optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointIn"]
            ).optional(),
            "entryPointType": t.string().optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointIn"]
            ).optional(),
        }
    ).named(renames["EntryPointIn"])
    types["EntryPointOut"] = t.struct(
        {
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointOut"]
            ).optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointOut"]
            ).optional(),
            "entryPointType": t.string().optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryPointOut"])
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
    types["GoogleAppsScriptTypeProcessIn"] = t.struct(
        {
            "processType": t.string().optional(),
            "functionName": t.string().optional(),
            "projectName": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "duration": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "processStatus": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessIn"])
    types["GoogleAppsScriptTypeProcessOut"] = t.struct(
        {
            "processType": t.string().optional(),
            "functionName": t.string().optional(),
            "projectName": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "duration": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "processStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessOut"])
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
    types["DeploymentIn"] = t.struct(
        {
            "deploymentId": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
            "updateTime": t.string().optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "deploymentId": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "updateTime": t.string().optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["ExecutionRequestIn"] = t.struct(
        {
            "sessionState": t.string().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
            "devMode": t.boolean().optional(),
        }
    ).named(renames["ExecutionRequestIn"])
    types["ExecutionRequestOut"] = t.struct(
        {
            "sessionState": t.string().optional(),
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
            "devMode": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionRequestOut"])
    types["StructIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["StructIn"])
    types["StructOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructOut"])
    types["ExecutionErrorIn"] = t.struct(
        {
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementIn"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "errorType": t.string().optional(),
        }
    ).named(renames["ExecutionErrorIn"])
    types["ExecutionErrorOut"] = t.struct(
        {
            "scriptStackTraceElements": t.array(
                t.proxy(renames["ScriptStackTraceElementOut"])
            ).optional(),
            "errorMessage": t.string().optional(),
            "errorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionErrorOut"])
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

    functions = {}
    functions["scriptsRun"] = script.post(
        "v1/scripts/{scriptId}:run",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "sessionState": t.string().optional(),
                "parameters": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "function": t.string().optional(),
                "devMode": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["processesList"] = script.get(
        "v1/processes:listScriptProcesses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "scriptProcessFilter.functionName": t.string().optional(),
                "scriptId": t.string().optional(),
                "scriptProcessFilter.endTime": t.string().optional(),
                "scriptProcessFilter.userAccessLevels": t.string().optional(),
                "scriptProcessFilter.startTime": t.string().optional(),
                "scriptProcessFilter.deploymentId": t.string().optional(),
                "pageToken": t.string().optional(),
                "scriptProcessFilter.types": t.string().optional(),
                "scriptProcessFilter.statuses": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScriptProcessesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["processesListScriptProcesses"] = script.get(
        "v1/processes:listScriptProcesses",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "scriptProcessFilter.functionName": t.string().optional(),
                "scriptId": t.string().optional(),
                "scriptProcessFilter.endTime": t.string().optional(),
                "scriptProcessFilter.userAccessLevels": t.string().optional(),
                "scriptProcessFilter.startTime": t.string().optional(),
                "scriptProcessFilter.deploymentId": t.string().optional(),
                "pageToken": t.string().optional(),
                "scriptProcessFilter.types": t.string().optional(),
                "scriptProcessFilter.statuses": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScriptProcessesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = script.put(
        "v1/projects/{scriptId}/content",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetContent"] = script.put(
        "v1/projects/{scriptId}/content",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetMetrics"] = script.put(
        "v1/projects/{scriptId}/content",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = script.put(
        "v1/projects/{scriptId}/content",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdateContent"] = script.put(
        "v1/projects/{scriptId}/content",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "files": t.array(t.proxy(renames["FileIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ContentOut"]),
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
    functions["projectsDeploymentsCreate"] = script.put(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsGet"] = script.put(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsList"] = script.put(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsDelete"] = script.put(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsUpdate"] = script.put(
        "v1/projects/{scriptId}/deployments/{deploymentId}",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "deploymentId": t.string().optional(),
                "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="script", renames=renames, types=Box(types), functions=Box(functions)
    )
