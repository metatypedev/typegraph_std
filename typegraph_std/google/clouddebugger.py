from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_clouddebugger():
    clouddebugger = HTTPRuntime("https://clouddebugger.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddebugger_1_ErrorResponse",
        "FormatMessageIn": "_clouddebugger_2_FormatMessageIn",
        "FormatMessageOut": "_clouddebugger_3_FormatMessageOut",
        "CloudWorkspaceIdIn": "_clouddebugger_4_CloudWorkspaceIdIn",
        "CloudWorkspaceIdOut": "_clouddebugger_5_CloudWorkspaceIdOut",
        "SourceContextIn": "_clouddebugger_6_SourceContextIn",
        "SourceContextOut": "_clouddebugger_7_SourceContextOut",
        "ListBreakpointsResponseIn": "_clouddebugger_8_ListBreakpointsResponseIn",
        "ListBreakpointsResponseOut": "_clouddebugger_9_ListBreakpointsResponseOut",
        "RegisterDebuggeeResponseIn": "_clouddebugger_10_RegisterDebuggeeResponseIn",
        "RegisterDebuggeeResponseOut": "_clouddebugger_11_RegisterDebuggeeResponseOut",
        "ExtendedSourceContextIn": "_clouddebugger_12_ExtendedSourceContextIn",
        "ExtendedSourceContextOut": "_clouddebugger_13_ExtendedSourceContextOut",
        "StackFrameIn": "_clouddebugger_14_StackFrameIn",
        "StackFrameOut": "_clouddebugger_15_StackFrameOut",
        "GerritSourceContextIn": "_clouddebugger_16_GerritSourceContextIn",
        "GerritSourceContextOut": "_clouddebugger_17_GerritSourceContextOut",
        "UpdateActiveBreakpointRequestIn": "_clouddebugger_18_UpdateActiveBreakpointRequestIn",
        "UpdateActiveBreakpointRequestOut": "_clouddebugger_19_UpdateActiveBreakpointRequestOut",
        "ProjectRepoIdIn": "_clouddebugger_20_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_clouddebugger_21_ProjectRepoIdOut",
        "StatusMessageIn": "_clouddebugger_22_StatusMessageIn",
        "StatusMessageOut": "_clouddebugger_23_StatusMessageOut",
        "CloudRepoSourceContextIn": "_clouddebugger_24_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_clouddebugger_25_CloudRepoSourceContextOut",
        "DebuggeeIn": "_clouddebugger_26_DebuggeeIn",
        "DebuggeeOut": "_clouddebugger_27_DebuggeeOut",
        "UpdateActiveBreakpointResponseIn": "_clouddebugger_28_UpdateActiveBreakpointResponseIn",
        "UpdateActiveBreakpointResponseOut": "_clouddebugger_29_UpdateActiveBreakpointResponseOut",
        "GetBreakpointResponseIn": "_clouddebugger_30_GetBreakpointResponseIn",
        "GetBreakpointResponseOut": "_clouddebugger_31_GetBreakpointResponseOut",
        "CloudWorkspaceSourceContextIn": "_clouddebugger_32_CloudWorkspaceSourceContextIn",
        "CloudWorkspaceSourceContextOut": "_clouddebugger_33_CloudWorkspaceSourceContextOut",
        "SourceLocationIn": "_clouddebugger_34_SourceLocationIn",
        "SourceLocationOut": "_clouddebugger_35_SourceLocationOut",
        "VariableIn": "_clouddebugger_36_VariableIn",
        "VariableOut": "_clouddebugger_37_VariableOut",
        "ListDebuggeesResponseIn": "_clouddebugger_38_ListDebuggeesResponseIn",
        "ListDebuggeesResponseOut": "_clouddebugger_39_ListDebuggeesResponseOut",
        "ListActiveBreakpointsResponseIn": "_clouddebugger_40_ListActiveBreakpointsResponseIn",
        "ListActiveBreakpointsResponseOut": "_clouddebugger_41_ListActiveBreakpointsResponseOut",
        "EmptyIn": "_clouddebugger_42_EmptyIn",
        "EmptyOut": "_clouddebugger_43_EmptyOut",
        "BreakpointIn": "_clouddebugger_44_BreakpointIn",
        "BreakpointOut": "_clouddebugger_45_BreakpointOut",
        "RegisterDebuggeeRequestIn": "_clouddebugger_46_RegisterDebuggeeRequestIn",
        "RegisterDebuggeeRequestOut": "_clouddebugger_47_RegisterDebuggeeRequestOut",
        "RepoIdIn": "_clouddebugger_48_RepoIdIn",
        "RepoIdOut": "_clouddebugger_49_RepoIdOut",
        "SetBreakpointResponseIn": "_clouddebugger_50_SetBreakpointResponseIn",
        "SetBreakpointResponseOut": "_clouddebugger_51_SetBreakpointResponseOut",
        "GitSourceContextIn": "_clouddebugger_52_GitSourceContextIn",
        "GitSourceContextOut": "_clouddebugger_53_GitSourceContextOut",
        "AliasContextIn": "_clouddebugger_54_AliasContextIn",
        "AliasContextOut": "_clouddebugger_55_AliasContextOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FormatMessageIn"] = t.struct(
        {"format": t.string().optional(), "parameters": t.array(t.string()).optional()}
    ).named(renames["FormatMessageIn"])
    types["FormatMessageOut"] = t.struct(
        {
            "format": t.string().optional(),
            "parameters": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatMessageOut"])
    types["CloudWorkspaceIdIn"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CloudWorkspaceIdIn"])
    types["CloudWorkspaceIdOut"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudWorkspaceIdOut"])
    types["SourceContextIn"] = t.struct(
        {
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextIn"]
            ).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextOut"]
            ).optional(),
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["ListBreakpointsResponseIn"] = t.struct(
        {
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
            "nextWaitToken": t.string().optional(),
        }
    ).named(renames["ListBreakpointsResponseIn"])
    types["ListBreakpointsResponseOut"] = t.struct(
        {
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "nextWaitToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBreakpointsResponseOut"])
    types["RegisterDebuggeeResponseIn"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeIn"]).optional(),
            "agentId": t.string().optional(),
        }
    ).named(renames["RegisterDebuggeeResponseIn"])
    types["RegisterDebuggeeResponseOut"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeOut"]).optional(),
            "agentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeResponseOut"])
    types["ExtendedSourceContextIn"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ExtendedSourceContextIn"])
    types["ExtendedSourceContextOut"] = t.struct(
        {
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedSourceContextOut"])
    types["StackFrameIn"] = t.struct(
        {
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "locals": t.array(t.proxy(renames["VariableIn"])).optional(),
            "arguments": t.array(t.proxy(renames["VariableIn"])).optional(),
            "function": t.string().optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "locals": t.array(t.proxy(renames["VariableOut"])).optional(),
            "arguments": t.array(t.proxy(renames["VariableOut"])).optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "aliasName": t.string().optional(),
            "hostUri": t.string().optional(),
            "gerritProject": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "aliasName": t.string().optional(),
            "hostUri": t.string().optional(),
            "gerritProject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["UpdateActiveBreakpointRequestIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"])}
    ).named(renames["UpdateActiveBreakpointRequestIn"])
    types["UpdateActiveBreakpointRequestOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateActiveBreakpointRequestOut"])
    types["ProjectRepoIdIn"] = t.struct(
        {"repoName": t.string().optional(), "projectId": t.string().optional()}
    ).named(renames["ProjectRepoIdIn"])
    types["ProjectRepoIdOut"] = t.struct(
        {
            "repoName": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectRepoIdOut"])
    types["StatusMessageIn"] = t.struct(
        {
            "refersTo": t.string().optional(),
            "description": t.proxy(renames["FormatMessageIn"]).optional(),
            "isError": t.boolean().optional(),
        }
    ).named(renames["StatusMessageIn"])
    types["StatusMessageOut"] = t.struct(
        {
            "refersTo": t.string().optional(),
            "description": t.proxy(renames["FormatMessageOut"]).optional(),
            "isError": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusMessageOut"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "aliasName": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "aliasName": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
    types["DebuggeeIn"] = t.struct(
        {
            "id": t.string().optional(),
            "uniquifier": t.string().optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextIn"])
            ).optional(),
            "agentVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "canaryMode": t.string().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextIn"])).optional(),
            "isInactive": t.boolean().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "isDisabled": t.boolean().optional(),
            "description": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["DebuggeeIn"])
    types["DebuggeeOut"] = t.struct(
        {
            "id": t.string().optional(),
            "uniquifier": t.string().optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextOut"])
            ).optional(),
            "agentVersion": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "canaryMode": t.string().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextOut"])).optional(),
            "isInactive": t.boolean().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "isDisabled": t.boolean().optional(),
            "description": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebuggeeOut"])
    types["UpdateActiveBreakpointResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateActiveBreakpointResponseIn"])
    types["UpdateActiveBreakpointResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateActiveBreakpointResponseOut"])
    types["GetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["GetBreakpointResponseIn"])
    types["GetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetBreakpointResponseOut"])
    types["CloudWorkspaceSourceContextIn"] = t.struct(
        {
            "snapshotId": t.string().optional(),
            "workspaceId": t.proxy(renames["CloudWorkspaceIdIn"]).optional(),
        }
    ).named(renames["CloudWorkspaceSourceContextIn"])
    types["CloudWorkspaceSourceContextOut"] = t.struct(
        {
            "snapshotId": t.string().optional(),
            "workspaceId": t.proxy(renames["CloudWorkspaceIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudWorkspaceSourceContextOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "path": t.string().optional(),
            "line": t.integer().optional(),
            "column": t.integer().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "path": t.string().optional(),
            "line": t.integer().optional(),
            "column": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["VariableIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "varTableIndex": t.integer().optional(),
            "value": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableIn"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "varTableIndex": t.integer().optional(),
            "value": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableOut"])).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
    types["ListDebuggeesResponseIn"] = t.struct(
        {"debuggees": t.array(t.proxy(renames["DebuggeeIn"])).optional()}
    ).named(renames["ListDebuggeesResponseIn"])
    types["ListDebuggeesResponseOut"] = t.struct(
        {
            "debuggees": t.array(t.proxy(renames["DebuggeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDebuggeesResponseOut"])
    types["ListActiveBreakpointsResponseIn"] = t.struct(
        {
            "waitExpired": t.boolean().optional(),
            "nextWaitToken": t.string().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseIn"])
    types["ListActiveBreakpointsResponseOut"] = t.struct(
        {
            "waitExpired": t.boolean().optional(),
            "nextWaitToken": t.string().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BreakpointIn"] = t.struct(
        {
            "condition": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "canaryExpireTime": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "id": t.string().optional(),
            "userEmail": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "finalTime": t.string().optional(),
            "isFinalState": t.boolean().optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableIn"])).optional(),
            "logLevel": t.string().optional(),
            "action": t.string().optional(),
            "stackFrames": t.array(t.proxy(renames["StackFrameIn"])).optional(),
        }
    ).named(renames["BreakpointIn"])
    types["BreakpointOut"] = t.struct(
        {
            "condition": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "canaryExpireTime": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "id": t.string().optional(),
            "userEmail": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "finalTime": t.string().optional(),
            "isFinalState": t.boolean().optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableOut"])).optional(),
            "logLevel": t.string().optional(),
            "action": t.string().optional(),
            "stackFrames": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BreakpointOut"])
    types["RegisterDebuggeeRequestIn"] = t.struct(
        {"debuggee": t.proxy(renames["DebuggeeIn"])}
    ).named(renames["RegisterDebuggeeRequestIn"])
    types["RegisterDebuggeeRequestOut"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeRequestOut"])
    types["RepoIdIn"] = t.struct(
        {
            "projectRepoId": t.proxy(renames["ProjectRepoIdIn"]).optional(),
            "uid": t.string().optional(),
        }
    ).named(renames["RepoIdIn"])
    types["RepoIdOut"] = t.struct(
        {
            "projectRepoId": t.proxy(renames["ProjectRepoIdOut"]).optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoIdOut"])
    types["SetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["SetBreakpointResponseIn"])
    types["SetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBreakpointResponseOut"])
    types["GitSourceContextIn"] = t.struct(
        {"url": t.string().optional(), "revisionId": t.string().optional()}
    ).named(renames["GitSourceContextIn"])
    types["GitSourceContextOut"] = t.struct(
        {
            "url": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceContextOut"])
    types["AliasContextIn"] = t.struct(
        {"name": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["AliasContextIn"])
    types["AliasContextOut"] = t.struct(
        {
            "name": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AliasContextOut"])

    functions = {}
    functions["controllerDebuggeesRegister"] = clouddebugger.post(
        "v2/controller/debuggees/register",
        t.struct(
            {"debuggee": t.proxy(renames["DebuggeeIn"]), "auth": t.string().optional()}
        ),
        t.proxy(renames["RegisterDebuggeeResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["controllerDebuggeesBreakpointsList"] = clouddebugger.put(
        "v2/controller/debuggees/{debuggeeId}/breakpoints/{id}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "id": t.string().optional(),
                "breakpoint": t.proxy(renames["BreakpointIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateActiveBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["controllerDebuggeesBreakpointsUpdate"] = clouddebugger.put(
        "v2/controller/debuggees/{debuggeeId}/breakpoints/{id}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "id": t.string().optional(),
                "breakpoint": t.proxy(renames["BreakpointIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UpdateActiveBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesList"] = clouddebugger.get(
        "v2/debugger/debuggees",
        t.struct(
            {
                "includeInactive": t.boolean().optional(),
                "project": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDebuggeesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsSet"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsDelete"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsList"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsGet"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetBreakpointResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddebugger",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
