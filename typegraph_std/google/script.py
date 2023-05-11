from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_script() -> Import:
    script = HTTPRuntime("https://script.googleapis.com/")

    renames = {
        "ErrorResponse": "_script_1_ErrorResponse",
        "ExecutionErrorIn": "_script_2_ExecutionErrorIn",
        "ExecutionErrorOut": "_script_3_ExecutionErrorOut",
        "EntryPointIn": "_script_4_EntryPointIn",
        "EntryPointOut": "_script_5_EntryPointOut",
        "ExecuteStreamResponseIn": "_script_6_ExecuteStreamResponseIn",
        "ExecuteStreamResponseOut": "_script_7_ExecuteStreamResponseOut",
        "OperationIn": "_script_8_OperationIn",
        "OperationOut": "_script_9_OperationOut",
        "DeploymentIn": "_script_10_DeploymentIn",
        "DeploymentOut": "_script_11_DeploymentOut",
        "StructIn": "_script_12_StructIn",
        "StructOut": "_script_13_StructOut",
        "GoogleAppsScriptTypeWebAppConfigIn": "_script_14_GoogleAppsScriptTypeWebAppConfigIn",
        "GoogleAppsScriptTypeWebAppConfigOut": "_script_15_GoogleAppsScriptTypeWebAppConfigOut",
        "ExecutionResponseIn": "_script_16_ExecutionResponseIn",
        "ExecutionResponseOut": "_script_17_ExecutionResponseOut",
        "GoogleAppsScriptTypeExecutionApiConfigIn": "_script_18_GoogleAppsScriptTypeExecutionApiConfigIn",
        "GoogleAppsScriptTypeExecutionApiConfigOut": "_script_19_GoogleAppsScriptTypeExecutionApiConfigOut",
        "ScriptStackTraceElementIn": "_script_20_ScriptStackTraceElementIn",
        "ScriptStackTraceElementOut": "_script_21_ScriptStackTraceElementOut",
        "MetricsValueIn": "_script_22_MetricsValueIn",
        "MetricsValueOut": "_script_23_MetricsValueOut",
        "GoogleAppsScriptTypeFunctionSetIn": "_script_24_GoogleAppsScriptTypeFunctionSetIn",
        "GoogleAppsScriptTypeFunctionSetOut": "_script_25_GoogleAppsScriptTypeFunctionSetOut",
        "GoogleAppsScriptTypeWebAppEntryPointIn": "_script_26_GoogleAppsScriptTypeWebAppEntryPointIn",
        "GoogleAppsScriptTypeWebAppEntryPointOut": "_script_27_GoogleAppsScriptTypeWebAppEntryPointOut",
        "FileIn": "_script_28_FileIn",
        "FileOut": "_script_29_FileOut",
        "MetricsIn": "_script_30_MetricsIn",
        "MetricsOut": "_script_31_MetricsOut",
        "GoogleAppsScriptTypeUserIn": "_script_32_GoogleAppsScriptTypeUserIn",
        "GoogleAppsScriptTypeUserOut": "_script_33_GoogleAppsScriptTypeUserOut",
        "DeploymentConfigIn": "_script_34_DeploymentConfigIn",
        "DeploymentConfigOut": "_script_35_DeploymentConfigOut",
        "StatusIn": "_script_36_StatusIn",
        "StatusOut": "_script_37_StatusOut",
        "GoogleAppsScriptTypeExecutionApiEntryPointIn": "_script_38_GoogleAppsScriptTypeExecutionApiEntryPointIn",
        "GoogleAppsScriptTypeExecutionApiEntryPointOut": "_script_39_GoogleAppsScriptTypeExecutionApiEntryPointOut",
        "ExecutionRequestIn": "_script_40_ExecutionRequestIn",
        "ExecutionRequestOut": "_script_41_ExecutionRequestOut",
        "EmptyIn": "_script_42_EmptyIn",
        "EmptyOut": "_script_43_EmptyOut",
        "GoogleAppsScriptTypeProcessIn": "_script_44_GoogleAppsScriptTypeProcessIn",
        "GoogleAppsScriptTypeProcessOut": "_script_45_GoogleAppsScriptTypeProcessOut",
        "ListVersionsResponseIn": "_script_46_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_script_47_ListVersionsResponseOut",
        "ListValueIn": "_script_48_ListValueIn",
        "ListValueOut": "_script_49_ListValueOut",
        "UpdateDeploymentRequestIn": "_script_50_UpdateDeploymentRequestIn",
        "UpdateDeploymentRequestOut": "_script_51_UpdateDeploymentRequestOut",
        "ListScriptProcessesResponseIn": "_script_52_ListScriptProcessesResponseIn",
        "ListScriptProcessesResponseOut": "_script_53_ListScriptProcessesResponseOut",
        "VersionIn": "_script_54_VersionIn",
        "VersionOut": "_script_55_VersionOut",
        "ValueIn": "_script_56_ValueIn",
        "ValueOut": "_script_57_ValueOut",
        "CreateProjectRequestIn": "_script_58_CreateProjectRequestIn",
        "CreateProjectRequestOut": "_script_59_CreateProjectRequestOut",
        "ListUserProcessesResponseIn": "_script_60_ListUserProcessesResponseIn",
        "ListUserProcessesResponseOut": "_script_61_ListUserProcessesResponseOut",
        "ProjectIn": "_script_62_ProjectIn",
        "ProjectOut": "_script_63_ProjectOut",
        "ListDeploymentsResponseIn": "_script_64_ListDeploymentsResponseIn",
        "ListDeploymentsResponseOut": "_script_65_ListDeploymentsResponseOut",
        "ScriptExecutionResultIn": "_script_66_ScriptExecutionResultIn",
        "ScriptExecutionResultOut": "_script_67_ScriptExecutionResultOut",
        "GoogleAppsScriptTypeAddOnEntryPointIn": "_script_68_GoogleAppsScriptTypeAddOnEntryPointIn",
        "GoogleAppsScriptTypeAddOnEntryPointOut": "_script_69_GoogleAppsScriptTypeAddOnEntryPointOut",
        "ContentIn": "_script_70_ContentIn",
        "ContentOut": "_script_71_ContentOut",
        "GoogleAppsScriptTypeFunctionIn": "_script_72_GoogleAppsScriptTypeFunctionIn",
        "GoogleAppsScriptTypeFunctionOut": "_script_73_GoogleAppsScriptTypeFunctionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EntryPointIn"] = t.struct(
        {
            "entryPointType": t.string().optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointIn"]
            ).optional(),
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointIn"]
            ).optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointIn"]
            ).optional(),
        }
    ).named(renames["EntryPointIn"])
    types["EntryPointOut"] = t.struct(
        {
            "entryPointType": t.string().optional(),
            "webApp": t.proxy(
                renames["GoogleAppsScriptTypeWebAppEntryPointOut"]
            ).optional(),
            "addOn": t.proxy(
                renames["GoogleAppsScriptTypeAddOnEntryPointOut"]
            ).optional(),
            "executionApi": t.proxy(
                renames["GoogleAppsScriptTypeExecutionApiEntryPointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryPointOut"])
    types["ExecuteStreamResponseIn"] = t.struct(
        {"result": t.proxy(renames["ScriptExecutionResultIn"]).optional()}
    ).named(renames["ExecuteStreamResponseIn"])
    types["ExecuteStreamResponseOut"] = t.struct(
        {
            "result": t.proxy(renames["ScriptExecutionResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteStreamResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["DeploymentIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "deploymentId": t.string().optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "deploymentId": t.string().optional(),
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["StructIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["StructIn"])
    types["StructOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructOut"])
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
        {"endTime": t.string(), "startTime": t.string(), "value": t.string().optional()}
    ).named(renames["MetricsValueIn"])
    types["MetricsValueOut"] = t.struct(
        {
            "endTime": t.string(),
            "startTime": t.string(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsValueOut"])
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
    types["FileIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetIn"]
            ).optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "source": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "functionSet": t.proxy(
                renames["GoogleAppsScriptTypeFunctionSetOut"]
            ).optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "source": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["MetricsIn"] = t.struct(
        {
            "activeUsers": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueIn"])).optional(),
        }
    ).named(renames["MetricsIn"])
    types["MetricsOut"] = t.struct(
        {
            "activeUsers": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "failedExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "totalExecutions": t.array(t.proxy(renames["MetricsValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricsOut"])
    types["GoogleAppsScriptTypeUserIn"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserIn"])
    types["GoogleAppsScriptTypeUserOut"] = t.struct(
        {
            "photoUrl": t.string().optional(),
            "domain": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeUserOut"])
    types["DeploymentConfigIn"] = t.struct(
        {
            "description": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "manifestFileName": t.string().optional(),
            "scriptId": t.string().optional(),
        }
    ).named(renames["DeploymentConfigIn"])
    types["DeploymentConfigOut"] = t.struct(
        {
            "description": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "manifestFileName": t.string().optional(),
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["ExecutionRequestIn"] = t.struct(
        {
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
            "sessionState": t.string().optional(),
            "devMode": t.boolean().optional(),
        }
    ).named(renames["ExecutionRequestIn"])
    types["ExecutionRequestOut"] = t.struct(
        {
            "parameters": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
            "sessionState": t.string().optional(),
            "devMode": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecutionRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleAppsScriptTypeProcessIn"] = t.struct(
        {
            "functionName": t.string().optional(),
            "processStatus": t.string().optional(),
            "processType": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "projectName": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessIn"])
    types["GoogleAppsScriptTypeProcessOut"] = t.struct(
        {
            "functionName": t.string().optional(),
            "processStatus": t.string().optional(),
            "processType": t.string().optional(),
            "userAccessLevel": t.string().optional(),
            "projectName": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeProcessOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ListValueIn"] = t.struct(
        {"values": t.array(t.proxy(renames["ValueIn"])).optional()}
    ).named(renames["ListValueIn"])
    types["ListValueOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListValueOut"])
    types["UpdateDeploymentRequestIn"] = t.struct(
        {"deploymentConfig": t.proxy(renames["DeploymentConfigIn"]).optional()}
    ).named(renames["UpdateDeploymentRequestIn"])
    types["UpdateDeploymentRequestOut"] = t.struct(
        {
            "deploymentConfig": t.proxy(renames["DeploymentConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeploymentRequestOut"])
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
    types["VersionIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "versionNumber": t.integer().optional(),
            "description": t.string().optional(),
            "scriptId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["ValueIn"] = t.struct(
        {
            "dateValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "bytesValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "stringValue": t.string().optional(),
            "structValue": t.proxy(renames["StructIn"]).optional(),
            "nullValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueIn"]).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "dateValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "bytesValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "protoValue": t.struct({"_": t.string().optional()}).optional(),
            "stringValue": t.string().optional(),
            "structValue": t.proxy(renames["StructOut"]).optional(),
            "nullValue": t.string().optional(),
            "listValue": t.proxy(renames["ListValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
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
            "parentId": t.string().optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
            "title": t.string().optional(),
            "scriptId": t.string().optional(),
            "lastModifyUser": t.proxy(renames["GoogleAppsScriptTypeUserIn"]).optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "parentId": t.string().optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["GoogleAppsScriptTypeUserOut"]).optional(),
            "title": t.string().optional(),
            "scriptId": t.string().optional(),
            "lastModifyUser": t.proxy(
                renames["GoogleAppsScriptTypeUserOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
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
    types["ScriptExecutionResultIn"] = t.struct(
        {"returnValue": t.proxy(renames["ValueIn"]).optional()}
    ).named(renames["ScriptExecutionResultIn"])
    types["ScriptExecutionResultOut"] = t.struct(
        {
            "returnValue": t.proxy(renames["ValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptExecutionResultOut"])
    types["GoogleAppsScriptTypeAddOnEntryPointIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "helpUrl": t.string().optional(),
            "addOnType": t.string().optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointIn"])
    types["GoogleAppsScriptTypeAddOnEntryPointOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "postInstallTipUrl": t.string().optional(),
            "reportIssueUrl": t.string().optional(),
            "helpUrl": t.string().optional(),
            "addOnType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsScriptTypeAddOnEntryPointOut"])
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

    functions = {}
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
    functions["projectsDeploymentsDelete"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "scriptId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDeploymentsGet"] = script.get(
        "v1/projects/{scriptId}/deployments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "scriptId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "scriptId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "scriptId": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "scriptId": t.string().optional(),
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
                "versionNumber": t.integer().optional(),
                "description": t.string().optional(),
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
                "versionNumber": t.integer().optional(),
                "description": t.string().optional(),
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
                "versionNumber": t.integer().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["scriptsRun"] = script.post(
        "v1/scripts/{scriptId}:run",
        t.struct(
            {
                "scriptId": t.string().optional(),
                "parameters": t.array(
                    t.struct({"_": t.string().optional()})
                ).optional(),
                "function": t.string().optional(),
                "sessionState": t.string().optional(),
                "devMode": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["processesListScriptProcesses"] = script.get(
        "v1/processes",
        t.struct(
            {
                "userProcessFilter.deploymentId": t.string().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "userProcessFilter.types": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "userProcessFilter.functionName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
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
                "userProcessFilter.deploymentId": t.string().optional(),
                "pageToken": t.string().optional(),
                "userProcessFilter.projectName": t.string().optional(),
                "userProcessFilter.endTime": t.string().optional(),
                "userProcessFilter.startTime": t.string().optional(),
                "userProcessFilter.types": t.string().optional(),
                "userProcessFilter.scriptId": t.string().optional(),
                "userProcessFilter.statuses": t.string().optional(),
                "userProcessFilter.functionName": t.string().optional(),
                "pageSize": t.integer().optional(),
                "userProcessFilter.userAccessLevels": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserProcessesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="script", renames=renames, types=types, functions=functions)
