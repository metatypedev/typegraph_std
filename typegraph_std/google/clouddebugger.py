from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_clouddebugger() -> Import:
    clouddebugger = HTTPRuntime("https://clouddebugger.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddebugger_1_ErrorResponse",
        "UpdateActiveBreakpointRequestIn": "_clouddebugger_2_UpdateActiveBreakpointRequestIn",
        "UpdateActiveBreakpointRequestOut": "_clouddebugger_3_UpdateActiveBreakpointRequestOut",
        "GerritSourceContextIn": "_clouddebugger_4_GerritSourceContextIn",
        "GerritSourceContextOut": "_clouddebugger_5_GerritSourceContextOut",
        "CloudWorkspaceSourceContextIn": "_clouddebugger_6_CloudWorkspaceSourceContextIn",
        "CloudWorkspaceSourceContextOut": "_clouddebugger_7_CloudWorkspaceSourceContextOut",
        "ProjectRepoIdIn": "_clouddebugger_8_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_clouddebugger_9_ProjectRepoIdOut",
        "FormatMessageIn": "_clouddebugger_10_FormatMessageIn",
        "FormatMessageOut": "_clouddebugger_11_FormatMessageOut",
        "BreakpointIn": "_clouddebugger_12_BreakpointIn",
        "BreakpointOut": "_clouddebugger_13_BreakpointOut",
        "RepoIdIn": "_clouddebugger_14_RepoIdIn",
        "RepoIdOut": "_clouddebugger_15_RepoIdOut",
        "EmptyIn": "_clouddebugger_16_EmptyIn",
        "EmptyOut": "_clouddebugger_17_EmptyOut",
        "RegisterDebuggeeRequestIn": "_clouddebugger_18_RegisterDebuggeeRequestIn",
        "RegisterDebuggeeRequestOut": "_clouddebugger_19_RegisterDebuggeeRequestOut",
        "SetBreakpointResponseIn": "_clouddebugger_20_SetBreakpointResponseIn",
        "SetBreakpointResponseOut": "_clouddebugger_21_SetBreakpointResponseOut",
        "DebuggeeIn": "_clouddebugger_22_DebuggeeIn",
        "DebuggeeOut": "_clouddebugger_23_DebuggeeOut",
        "GitSourceContextIn": "_clouddebugger_24_GitSourceContextIn",
        "GitSourceContextOut": "_clouddebugger_25_GitSourceContextOut",
        "AliasContextIn": "_clouddebugger_26_AliasContextIn",
        "AliasContextOut": "_clouddebugger_27_AliasContextOut",
        "ListActiveBreakpointsResponseIn": "_clouddebugger_28_ListActiveBreakpointsResponseIn",
        "ListActiveBreakpointsResponseOut": "_clouddebugger_29_ListActiveBreakpointsResponseOut",
        "SourceContextIn": "_clouddebugger_30_SourceContextIn",
        "SourceContextOut": "_clouddebugger_31_SourceContextOut",
        "ListBreakpointsResponseIn": "_clouddebugger_32_ListBreakpointsResponseIn",
        "ListBreakpointsResponseOut": "_clouddebugger_33_ListBreakpointsResponseOut",
        "VariableIn": "_clouddebugger_34_VariableIn",
        "VariableOut": "_clouddebugger_35_VariableOut",
        "CloudWorkspaceIdIn": "_clouddebugger_36_CloudWorkspaceIdIn",
        "CloudWorkspaceIdOut": "_clouddebugger_37_CloudWorkspaceIdOut",
        "GetBreakpointResponseIn": "_clouddebugger_38_GetBreakpointResponseIn",
        "GetBreakpointResponseOut": "_clouddebugger_39_GetBreakpointResponseOut",
        "RegisterDebuggeeResponseIn": "_clouddebugger_40_RegisterDebuggeeResponseIn",
        "RegisterDebuggeeResponseOut": "_clouddebugger_41_RegisterDebuggeeResponseOut",
        "StatusMessageIn": "_clouddebugger_42_StatusMessageIn",
        "StatusMessageOut": "_clouddebugger_43_StatusMessageOut",
        "ListDebuggeesResponseIn": "_clouddebugger_44_ListDebuggeesResponseIn",
        "ListDebuggeesResponseOut": "_clouddebugger_45_ListDebuggeesResponseOut",
        "ExtendedSourceContextIn": "_clouddebugger_46_ExtendedSourceContextIn",
        "ExtendedSourceContextOut": "_clouddebugger_47_ExtendedSourceContextOut",
        "CloudRepoSourceContextIn": "_clouddebugger_48_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_clouddebugger_49_CloudRepoSourceContextOut",
        "SourceLocationIn": "_clouddebugger_50_SourceLocationIn",
        "SourceLocationOut": "_clouddebugger_51_SourceLocationOut",
        "StackFrameIn": "_clouddebugger_52_StackFrameIn",
        "StackFrameOut": "_clouddebugger_53_StackFrameOut",
        "UpdateActiveBreakpointResponseIn": "_clouddebugger_54_UpdateActiveBreakpointResponseIn",
        "UpdateActiveBreakpointResponseOut": "_clouddebugger_55_UpdateActiveBreakpointResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpdateActiveBreakpointRequestIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"])}
    ).named(renames["UpdateActiveBreakpointRequestIn"])
    types["UpdateActiveBreakpointRequestOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateActiveBreakpointRequestOut"])
    types["GerritSourceContextIn"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["GerritSourceContextIn"])
    types["GerritSourceContextOut"] = t.struct(
        {
            "gerritProject": t.string().optional(),
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
            "hostUri": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GerritSourceContextOut"])
    types["CloudWorkspaceSourceContextIn"] = t.struct(
        {
            "workspaceId": t.proxy(renames["CloudWorkspaceIdIn"]).optional(),
            "snapshotId": t.string().optional(),
        }
    ).named(renames["CloudWorkspaceSourceContextIn"])
    types["CloudWorkspaceSourceContextOut"] = t.struct(
        {
            "workspaceId": t.proxy(renames["CloudWorkspaceIdOut"]).optional(),
            "snapshotId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudWorkspaceSourceContextOut"])
    types["ProjectRepoIdIn"] = t.struct(
        {"projectId": t.string().optional(), "repoName": t.string().optional()}
    ).named(renames["ProjectRepoIdIn"])
    types["ProjectRepoIdOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectRepoIdOut"])
    types["FormatMessageIn"] = t.struct(
        {"parameters": t.array(t.string()).optional(), "format": t.string().optional()}
    ).named(renames["FormatMessageIn"])
    types["FormatMessageOut"] = t.struct(
        {
            "parameters": t.array(t.string()).optional(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormatMessageOut"])
    types["BreakpointIn"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "finalTime": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "isFinalState": t.boolean().optional(),
            "createTime": t.string().optional(),
            "canaryExpireTime": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "stackFrames": t.array(t.proxy(renames["StackFrameIn"])).optional(),
            "action": t.string().optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "condition": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "logLevel": t.string().optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BreakpointIn"])
    types["BreakpointOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "finalTime": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "isFinalState": t.boolean().optional(),
            "createTime": t.string().optional(),
            "canaryExpireTime": t.string().optional(),
            "expressions": t.array(t.string()).optional(),
            "stackFrames": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "action": t.string().optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "id": t.string().optional(),
            "state": t.string().optional(),
            "condition": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "logLevel": t.string().optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BreakpointOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RegisterDebuggeeRequestIn"] = t.struct(
        {"debuggee": t.proxy(renames["DebuggeeIn"])}
    ).named(renames["RegisterDebuggeeRequestIn"])
    types["RegisterDebuggeeRequestOut"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeRequestOut"])
    types["SetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["SetBreakpointResponseIn"])
    types["SetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBreakpointResponseOut"])
    types["DebuggeeIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextIn"])).optional(),
            "uniquifier": t.string().optional(),
            "project": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "id": t.string().optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextIn"])
            ).optional(),
            "isDisabled": t.boolean().optional(),
            "agentVersion": t.string().optional(),
            "isInactive": t.boolean().optional(),
            "description": t.string().optional(),
            "canaryMode": t.string().optional(),
        }
    ).named(renames["DebuggeeIn"])
    types["DebuggeeOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextOut"])).optional(),
            "uniquifier": t.string().optional(),
            "project": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "id": t.string().optional(),
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextOut"])
            ).optional(),
            "isDisabled": t.boolean().optional(),
            "agentVersion": t.string().optional(),
            "isInactive": t.boolean().optional(),
            "description": t.string().optional(),
            "canaryMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebuggeeOut"])
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
    types["ListActiveBreakpointsResponseIn"] = t.struct(
        {
            "nextWaitToken": t.string().optional(),
            "waitExpired": t.boolean().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseIn"])
    types["ListActiveBreakpointsResponseOut"] = t.struct(
        {
            "nextWaitToken": t.string().optional(),
            "waitExpired": t.boolean().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseOut"])
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
            "nextWaitToken": t.string().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
        }
    ).named(renames["ListBreakpointsResponseIn"])
    types["ListBreakpointsResponseOut"] = t.struct(
        {
            "nextWaitToken": t.string().optional(),
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBreakpointsResponseOut"])
    types["VariableIn"] = t.struct(
        {
            "name": t.string().optional(),
            "varTableIndex": t.integer().optional(),
            "type": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "value": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableIn"])).optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "name": t.string().optional(),
            "varTableIndex": t.integer().optional(),
            "type": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "value": t.string().optional(),
            "members": t.array(t.proxy(renames["VariableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
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
    types["GetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["GetBreakpointResponseIn"])
    types["GetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetBreakpointResponseOut"])
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
    types["StatusMessageIn"] = t.struct(
        {
            "isError": t.boolean().optional(),
            "description": t.proxy(renames["FormatMessageIn"]).optional(),
            "refersTo": t.string().optional(),
        }
    ).named(renames["StatusMessageIn"])
    types["StatusMessageOut"] = t.struct(
        {
            "isError": t.boolean().optional(),
            "description": t.proxy(renames["FormatMessageOut"]).optional(),
            "refersTo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusMessageOut"])
    types["ListDebuggeesResponseIn"] = t.struct(
        {"debuggees": t.array(t.proxy(renames["DebuggeeIn"])).optional()}
    ).named(renames["ListDebuggeesResponseIn"])
    types["ListDebuggeesResponseOut"] = t.struct(
        {
            "debuggees": t.array(t.proxy(renames["DebuggeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDebuggeesResponseOut"])
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
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "aliasName": t.string().optional(),
            "revisionId": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "column": t.integer().optional(),
            "line": t.integer().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "column": t.integer().optional(),
            "line": t.integer().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
    types["StackFrameIn"] = t.struct(
        {
            "arguments": t.array(t.proxy(renames["VariableIn"])).optional(),
            "function": t.string().optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "locals": t.array(t.proxy(renames["VariableIn"])).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "arguments": t.array(t.proxy(renames["VariableOut"])).optional(),
            "function": t.string().optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "locals": t.array(t.proxy(renames["VariableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
    types["UpdateActiveBreakpointResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateActiveBreakpointResponseIn"])
    types["UpdateActiveBreakpointResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateActiveBreakpointResponseOut"])

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
    functions["debuggerDebuggeesBreakpointsSet"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints/{breakpointId}",
        t.struct(
            {
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
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
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
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
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
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
                "debuggeeId": t.string(),
                "breakpointId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetBreakpointResponseOut"]),
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
        importer="clouddebugger", renames=renames, types=types, functions=functions
    )
