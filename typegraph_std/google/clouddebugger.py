from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_clouddebugger() -> Import:
    clouddebugger = HTTPRuntime("https://clouddebugger.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddebugger_1_ErrorResponse",
        "DebuggeeIn": "_clouddebugger_2_DebuggeeIn",
        "DebuggeeOut": "_clouddebugger_3_DebuggeeOut",
        "BreakpointIn": "_clouddebugger_4_BreakpointIn",
        "BreakpointOut": "_clouddebugger_5_BreakpointOut",
        "CloudWorkspaceIdIn": "_clouddebugger_6_CloudWorkspaceIdIn",
        "CloudWorkspaceIdOut": "_clouddebugger_7_CloudWorkspaceIdOut",
        "UpdateActiveBreakpointRequestIn": "_clouddebugger_8_UpdateActiveBreakpointRequestIn",
        "UpdateActiveBreakpointRequestOut": "_clouddebugger_9_UpdateActiveBreakpointRequestOut",
        "SourceLocationIn": "_clouddebugger_10_SourceLocationIn",
        "SourceLocationOut": "_clouddebugger_11_SourceLocationOut",
        "SetBreakpointResponseIn": "_clouddebugger_12_SetBreakpointResponseIn",
        "SetBreakpointResponseOut": "_clouddebugger_13_SetBreakpointResponseOut",
        "RegisterDebuggeeResponseIn": "_clouddebugger_14_RegisterDebuggeeResponseIn",
        "RegisterDebuggeeResponseOut": "_clouddebugger_15_RegisterDebuggeeResponseOut",
        "ListActiveBreakpointsResponseIn": "_clouddebugger_16_ListActiveBreakpointsResponseIn",
        "ListActiveBreakpointsResponseOut": "_clouddebugger_17_ListActiveBreakpointsResponseOut",
        "CloudWorkspaceSourceContextIn": "_clouddebugger_18_CloudWorkspaceSourceContextIn",
        "CloudWorkspaceSourceContextOut": "_clouddebugger_19_CloudWorkspaceSourceContextOut",
        "RegisterDebuggeeRequestIn": "_clouddebugger_20_RegisterDebuggeeRequestIn",
        "RegisterDebuggeeRequestOut": "_clouddebugger_21_RegisterDebuggeeRequestOut",
        "ListDebuggeesResponseIn": "_clouddebugger_22_ListDebuggeesResponseIn",
        "ListDebuggeesResponseOut": "_clouddebugger_23_ListDebuggeesResponseOut",
        "SourceContextIn": "_clouddebugger_24_SourceContextIn",
        "SourceContextOut": "_clouddebugger_25_SourceContextOut",
        "UpdateActiveBreakpointResponseIn": "_clouddebugger_26_UpdateActiveBreakpointResponseIn",
        "UpdateActiveBreakpointResponseOut": "_clouddebugger_27_UpdateActiveBreakpointResponseOut",
        "ProjectRepoIdIn": "_clouddebugger_28_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_clouddebugger_29_ProjectRepoIdOut",
        "StackFrameIn": "_clouddebugger_30_StackFrameIn",
        "StackFrameOut": "_clouddebugger_31_StackFrameOut",
        "ListBreakpointsResponseIn": "_clouddebugger_32_ListBreakpointsResponseIn",
        "ListBreakpointsResponseOut": "_clouddebugger_33_ListBreakpointsResponseOut",
        "VariableIn": "_clouddebugger_34_VariableIn",
        "VariableOut": "_clouddebugger_35_VariableOut",
        "CloudRepoSourceContextIn": "_clouddebugger_36_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_clouddebugger_37_CloudRepoSourceContextOut",
        "RepoIdIn": "_clouddebugger_38_RepoIdIn",
        "RepoIdOut": "_clouddebugger_39_RepoIdOut",
        "StatusMessageIn": "_clouddebugger_40_StatusMessageIn",
        "StatusMessageOut": "_clouddebugger_41_StatusMessageOut",
        "GitSourceContextIn": "_clouddebugger_42_GitSourceContextIn",
        "GitSourceContextOut": "_clouddebugger_43_GitSourceContextOut",
        "EmptyIn": "_clouddebugger_44_EmptyIn",
        "EmptyOut": "_clouddebugger_45_EmptyOut",
        "ExtendedSourceContextIn": "_clouddebugger_46_ExtendedSourceContextIn",
        "ExtendedSourceContextOut": "_clouddebugger_47_ExtendedSourceContextOut",
        "AliasContextIn": "_clouddebugger_48_AliasContextIn",
        "AliasContextOut": "_clouddebugger_49_AliasContextOut",
        "GetBreakpointResponseIn": "_clouddebugger_50_GetBreakpointResponseIn",
        "GetBreakpointResponseOut": "_clouddebugger_51_GetBreakpointResponseOut",
        "FormatMessageIn": "_clouddebugger_52_FormatMessageIn",
        "FormatMessageOut": "_clouddebugger_53_FormatMessageOut",
        "GerritSourceContextIn": "_clouddebugger_54_GerritSourceContextIn",
        "GerritSourceContextOut": "_clouddebugger_55_GerritSourceContextOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DebuggeeIn"] = t.struct(
        {
            "isDisabled": t.boolean().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextIn"])).optional(),
            "uniquifier": t.string().optional(),
            "agentVersion": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "description": t.string().optional(),
            "isInactive": t.boolean().optional(),
            "project": t.string().optional(),
            "canaryMode": t.string().optional(),
            "id": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextIn"])
            ).optional(),
        }
    ).named(renames["DebuggeeIn"])
    types["DebuggeeOut"] = t.struct(
        {
            "isDisabled": t.boolean().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextOut"])).optional(),
            "uniquifier": t.string().optional(),
            "agentVersion": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "description": t.string().optional(),
            "isInactive": t.boolean().optional(),
            "project": t.string().optional(),
            "canaryMode": t.string().optional(),
            "id": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebuggeeOut"])
    types["BreakpointIn"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["StackFrameIn"])).optional(),
            "variableTable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableIn"])).optional(),
            "logMessageFormat": t.string().optional(),
            "condition": t.string().optional(),
            "logLevel": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "canaryExpireTime": t.string().optional(),
            "isFinalState": t.boolean().optional(),
            "id": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "userEmail": t.string().optional(),
            "finalTime": t.string().optional(),
        }
    ).named(renames["BreakpointIn"])
    types["BreakpointOut"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "variableTable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableOut"])).optional(),
            "logMessageFormat": t.string().optional(),
            "condition": t.string().optional(),
            "logLevel": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "canaryExpireTime": t.string().optional(),
            "isFinalState": t.boolean().optional(),
            "id": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "action": t.string().optional(),
            "createTime": t.string().optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "userEmail": t.string().optional(),
            "finalTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BreakpointOut"])
    types["CloudWorkspaceIdIn"] = t.struct(
        {
            "name": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
        }
    ).named(renames["CloudWorkspaceIdIn"])
    types["CloudWorkspaceIdOut"] = t.struct(
        {
            "name": t.string().optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudWorkspaceIdOut"])
    types["UpdateActiveBreakpointRequestIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"])}
    ).named(renames["UpdateActiveBreakpointRequestIn"])
    types["UpdateActiveBreakpointRequestOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateActiveBreakpointRequestOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "line": t.integer().optional(),
            "column": t.integer().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "line": t.integer().optional(),
            "column": t.integer().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["SetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["SetBreakpointResponseIn"])
    types["SetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBreakpointResponseOut"])
    types["RegisterDebuggeeResponseIn"] = t.struct(
        {
            "agentId": t.string().optional(),
            "debuggee": t.proxy(renames["DebuggeeIn"]).optional(),
        }
    ).named(renames["RegisterDebuggeeResponseIn"])
    types["RegisterDebuggeeResponseOut"] = t.struct(
        {
            "agentId": t.string().optional(),
            "debuggee": t.proxy(renames["DebuggeeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeResponseOut"])
    types["ListActiveBreakpointsResponseIn"] = t.struct(
        {
            "waitExpired": t.boolean().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
            "nextWaitToken": t.string().optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseIn"])
    types["ListActiveBreakpointsResponseOut"] = t.struct(
        {
            "waitExpired": t.boolean().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "nextWaitToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseOut"])
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
    types["RegisterDebuggeeRequestIn"] = t.struct(
        {"debuggee": t.proxy(renames["DebuggeeIn"])}
    ).named(renames["RegisterDebuggeeRequestIn"])
    types["RegisterDebuggeeRequestOut"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeRequestOut"])
    types["ListDebuggeesResponseIn"] = t.struct(
        {"debuggees": t.array(t.proxy(renames["DebuggeeIn"])).optional()}
    ).named(renames["ListDebuggeesResponseIn"])
    types["ListDebuggeesResponseOut"] = t.struct(
        {
            "debuggees": t.array(t.proxy(renames["DebuggeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDebuggeesResponseOut"])
    types["SourceContextIn"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextIn"]
            ).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextOut"]
            ).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["UpdateActiveBreakpointResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateActiveBreakpointResponseIn"])
    types["UpdateActiveBreakpointResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateActiveBreakpointResponseOut"])
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
    types["StackFrameIn"] = t.struct(
        {
            "locals": t.array(t.proxy(renames["VariableIn"])).optional(),
            "arguments": t.array(t.proxy(renames["VariableIn"])).optional(),
            "function": t.string().optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "locals": t.array(t.proxy(renames["VariableOut"])).optional(),
            "arguments": t.array(t.proxy(renames["VariableOut"])).optional(),
            "function": t.string().optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
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
    types["VariableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableIn"])).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "varTableIndex": t.integer().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableOut"])).optional(),
            "value": t.string().optional(),
            "type": t.string().optional(),
            "varTableIndex": t.integer().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
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
    types["StatusMessageIn"] = t.struct(
        {
            "description": t.proxy(renames["FormatMessageIn"]).optional(),
            "isError": t.boolean().optional(),
            "refersTo": t.string().optional(),
        }
    ).named(renames["StatusMessageIn"])
    types["StatusMessageOut"] = t.struct(
        {
            "description": t.proxy(renames["FormatMessageOut"]).optional(),
            "isError": t.boolean().optional(),
            "refersTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusMessageOut"])
    types["GitSourceContextIn"] = t.struct(
        {"revisionId": t.string().optional(), "url": t.string().optional()}
    ).named(renames["GitSourceContextIn"])
    types["GitSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GitSourceContextOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExtendedSourceContextIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["ExtendedSourceContextIn"])
    types["ExtendedSourceContextOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "context": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendedSourceContextOut"])
    types["AliasContextIn"] = t.struct(
        {"kind": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AliasContextIn"])
    types["AliasContextOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AliasContextOut"])
    types["GetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["GetBreakpointResponseIn"])
    types["GetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetBreakpointResponseOut"])
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
    types["GerritSourceContextIn"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "aliasName": t.string().optional(),
            "gerritProject": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "hostUri": t.string().optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "aliasName": t.string().optional(),
            "gerritProject": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "hostUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])

    functions = {}
    functions["debuggerDebuggeesList"] = clouddebugger.get(
        "v2/debugger/debuggees",
        t.struct(
            {
                "project": t.string(),
                "includeInactive": t.boolean().optional(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDebuggeesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsGet"] = clouddebugger.delete(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsList"] = clouddebugger.delete(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsSet"] = clouddebugger.delete(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsDelete"] = clouddebugger.delete(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="clouddebugger",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
