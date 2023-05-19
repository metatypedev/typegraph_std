from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_clouddebugger() -> Import:
    clouddebugger = HTTPRuntime("https://clouddebugger.googleapis.com/")

    renames = {
        "ErrorResponse": "_clouddebugger_1_ErrorResponse",
        "CloudWorkspaceIdIn": "_clouddebugger_2_CloudWorkspaceIdIn",
        "CloudWorkspaceIdOut": "_clouddebugger_3_CloudWorkspaceIdOut",
        "EmptyIn": "_clouddebugger_4_EmptyIn",
        "EmptyOut": "_clouddebugger_5_EmptyOut",
        "SourceLocationIn": "_clouddebugger_6_SourceLocationIn",
        "SourceLocationOut": "_clouddebugger_7_SourceLocationOut",
        "FormatMessageIn": "_clouddebugger_8_FormatMessageIn",
        "FormatMessageOut": "_clouddebugger_9_FormatMessageOut",
        "ExtendedSourceContextIn": "_clouddebugger_10_ExtendedSourceContextIn",
        "ExtendedSourceContextOut": "_clouddebugger_11_ExtendedSourceContextOut",
        "VariableIn": "_clouddebugger_12_VariableIn",
        "VariableOut": "_clouddebugger_13_VariableOut",
        "CloudWorkspaceSourceContextIn": "_clouddebugger_14_CloudWorkspaceSourceContextIn",
        "CloudWorkspaceSourceContextOut": "_clouddebugger_15_CloudWorkspaceSourceContextOut",
        "GitSourceContextIn": "_clouddebugger_16_GitSourceContextIn",
        "GitSourceContextOut": "_clouddebugger_17_GitSourceContextOut",
        "UpdateActiveBreakpointResponseIn": "_clouddebugger_18_UpdateActiveBreakpointResponseIn",
        "UpdateActiveBreakpointResponseOut": "_clouddebugger_19_UpdateActiveBreakpointResponseOut",
        "GetBreakpointResponseIn": "_clouddebugger_20_GetBreakpointResponseIn",
        "GetBreakpointResponseOut": "_clouddebugger_21_GetBreakpointResponseOut",
        "ProjectRepoIdIn": "_clouddebugger_22_ProjectRepoIdIn",
        "ProjectRepoIdOut": "_clouddebugger_23_ProjectRepoIdOut",
        "RegisterDebuggeeRequestIn": "_clouddebugger_24_RegisterDebuggeeRequestIn",
        "RegisterDebuggeeRequestOut": "_clouddebugger_25_RegisterDebuggeeRequestOut",
        "ListActiveBreakpointsResponseIn": "_clouddebugger_26_ListActiveBreakpointsResponseIn",
        "ListActiveBreakpointsResponseOut": "_clouddebugger_27_ListActiveBreakpointsResponseOut",
        "CloudRepoSourceContextIn": "_clouddebugger_28_CloudRepoSourceContextIn",
        "CloudRepoSourceContextOut": "_clouddebugger_29_CloudRepoSourceContextOut",
        "ListDebuggeesResponseIn": "_clouddebugger_30_ListDebuggeesResponseIn",
        "ListDebuggeesResponseOut": "_clouddebugger_31_ListDebuggeesResponseOut",
        "DebuggeeIn": "_clouddebugger_32_DebuggeeIn",
        "DebuggeeOut": "_clouddebugger_33_DebuggeeOut",
        "UpdateActiveBreakpointRequestIn": "_clouddebugger_34_UpdateActiveBreakpointRequestIn",
        "UpdateActiveBreakpointRequestOut": "_clouddebugger_35_UpdateActiveBreakpointRequestOut",
        "RegisterDebuggeeResponseIn": "_clouddebugger_36_RegisterDebuggeeResponseIn",
        "RegisterDebuggeeResponseOut": "_clouddebugger_37_RegisterDebuggeeResponseOut",
        "GerritSourceContextIn": "_clouddebugger_38_GerritSourceContextIn",
        "GerritSourceContextOut": "_clouddebugger_39_GerritSourceContextOut",
        "StackFrameIn": "_clouddebugger_40_StackFrameIn",
        "StackFrameOut": "_clouddebugger_41_StackFrameOut",
        "SetBreakpointResponseIn": "_clouddebugger_42_SetBreakpointResponseIn",
        "SetBreakpointResponseOut": "_clouddebugger_43_SetBreakpointResponseOut",
        "RepoIdIn": "_clouddebugger_44_RepoIdIn",
        "RepoIdOut": "_clouddebugger_45_RepoIdOut",
        "StatusMessageIn": "_clouddebugger_46_StatusMessageIn",
        "StatusMessageOut": "_clouddebugger_47_StatusMessageOut",
        "BreakpointIn": "_clouddebugger_48_BreakpointIn",
        "BreakpointOut": "_clouddebugger_49_BreakpointOut",
        "AliasContextIn": "_clouddebugger_50_AliasContextIn",
        "AliasContextOut": "_clouddebugger_51_AliasContextOut",
        "ListBreakpointsResponseIn": "_clouddebugger_52_ListBreakpointsResponseIn",
        "ListBreakpointsResponseOut": "_clouddebugger_53_ListBreakpointsResponseOut",
        "SourceContextIn": "_clouddebugger_54_SourceContextIn",
        "SourceContextOut": "_clouddebugger_55_SourceContextOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SourceLocationIn"] = t.struct(
        {
            "line": t.integer().optional(),
            "path": t.string().optional(),
            "column": t.integer().optional(),
        }
    ).named(renames["SourceLocationIn"])
    types["SourceLocationOut"] = t.struct(
        {
            "line": t.integer().optional(),
            "path": t.string().optional(),
            "column": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceLocationOut"])
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
    types["VariableIn"] = t.struct(
        {
            "members": t.array(t.proxy(renames["VariableIn"])).optional(),
            "varTableIndex": t.integer().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["VariableIn"])
    types["VariableOut"] = t.struct(
        {
            "members": t.array(t.proxy(renames["VariableOut"])).optional(),
            "varTableIndex": t.integer().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableOut"])
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
    types["RegisterDebuggeeRequestIn"] = t.struct(
        {"debuggee": t.proxy(renames["DebuggeeIn"])}
    ).named(renames["RegisterDebuggeeRequestIn"])
    types["RegisterDebuggeeRequestOut"] = t.struct(
        {
            "debuggee": t.proxy(renames["DebuggeeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDebuggeeRequestOut"])
    types["ListActiveBreakpointsResponseIn"] = t.struct(
        {
            "breakpoints": t.array(t.proxy(renames["BreakpointIn"])).optional(),
            "waitExpired": t.boolean().optional(),
            "nextWaitToken": t.string().optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseIn"])
    types["ListActiveBreakpointsResponseOut"] = t.struct(
        {
            "breakpoints": t.array(t.proxy(renames["BreakpointOut"])).optional(),
            "waitExpired": t.boolean().optional(),
            "nextWaitToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActiveBreakpointsResponseOut"])
    types["CloudRepoSourceContextIn"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdIn"]).optional(),
            "revisionId": t.string().optional(),
            "aliasName": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextIn"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextIn"])
    types["CloudRepoSourceContextOut"] = t.struct(
        {
            "repoId": t.proxy(renames["RepoIdOut"]).optional(),
            "revisionId": t.string().optional(),
            "aliasName": t.string().optional(),
            "aliasContext": t.proxy(renames["AliasContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudRepoSourceContextOut"])
    types["ListDebuggeesResponseIn"] = t.struct(
        {"debuggees": t.array(t.proxy(renames["DebuggeeIn"])).optional()}
    ).named(renames["ListDebuggeesResponseIn"])
    types["ListDebuggeesResponseOut"] = t.struct(
        {
            "debuggees": t.array(t.proxy(renames["DebuggeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDebuggeesResponseOut"])
    types["DebuggeeIn"] = t.struct(
        {
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextIn"])
            ).optional(),
            "uniquifier": t.string().optional(),
            "isDisabled": t.boolean().optional(),
            "isInactive": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "project": t.string().optional(),
            "agentVersion": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "id": t.string().optional(),
            "canaryMode": t.string().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextIn"])).optional(),
        }
    ).named(renames["DebuggeeIn"])
    types["DebuggeeOut"] = t.struct(
        {
            "extSourceContexts": t.array(
                t.proxy(renames["ExtendedSourceContextOut"])
            ).optional(),
            "uniquifier": t.string().optional(),
            "isDisabled": t.boolean().optional(),
            "isInactive": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "project": t.string().optional(),
            "agentVersion": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "id": t.string().optional(),
            "canaryMode": t.string().optional(),
            "sourceContexts": t.array(t.proxy(renames["SourceContextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebuggeeOut"])
    types["UpdateActiveBreakpointRequestIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"])}
    ).named(renames["UpdateActiveBreakpointRequestIn"])
    types["UpdateActiveBreakpointRequestOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateActiveBreakpointRequestOut"])
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
    types["StackFrameIn"] = t.struct(
        {
            "locals": t.array(t.proxy(renames["VariableIn"])).optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "function": t.string().optional(),
            "arguments": t.array(t.proxy(renames["VariableIn"])).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "locals": t.array(t.proxy(renames["VariableOut"])).optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "function": t.string().optional(),
            "arguments": t.array(t.proxy(renames["VariableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
    types["SetBreakpointResponseIn"] = t.struct(
        {"breakpoint": t.proxy(renames["BreakpointIn"]).optional()}
    ).named(renames["SetBreakpointResponseIn"])
    types["SetBreakpointResponseOut"] = t.struct(
        {
            "breakpoint": t.proxy(renames["BreakpointOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetBreakpointResponseOut"])
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
            "isError": t.boolean().optional(),
            "refersTo": t.string().optional(),
            "description": t.proxy(renames["FormatMessageIn"]).optional(),
        }
    ).named(renames["StatusMessageIn"])
    types["StatusMessageOut"] = t.struct(
        {
            "isError": t.boolean().optional(),
            "refersTo": t.string().optional(),
            "description": t.proxy(renames["FormatMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusMessageOut"])
    types["BreakpointIn"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["StackFrameIn"])).optional(),
            "logLevel": t.string().optional(),
            "action": t.string().optional(),
            "condition": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableIn"])).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "location": t.proxy(renames["SourceLocationIn"]).optional(),
            "canaryExpireTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableIn"])).optional(),
            "finalTime": t.string().optional(),
            "state": t.string().optional(),
            "status": t.proxy(renames["StatusMessageIn"]).optional(),
            "expressions": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "isFinalState": t.boolean().optional(),
        }
    ).named(renames["BreakpointIn"])
    types["BreakpointOut"] = t.struct(
        {
            "stackFrames": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "logLevel": t.string().optional(),
            "action": t.string().optional(),
            "condition": t.string().optional(),
            "logMessageFormat": t.string().optional(),
            "variableTable": t.array(t.proxy(renames["VariableOut"])).optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "location": t.proxy(renames["SourceLocationOut"]).optional(),
            "canaryExpireTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "evaluatedExpressions": t.array(t.proxy(renames["VariableOut"])).optional(),
            "finalTime": t.string().optional(),
            "state": t.string().optional(),
            "status": t.proxy(renames["StatusMessageOut"]).optional(),
            "expressions": t.array(t.string()).optional(),
            "userEmail": t.string().optional(),
            "isFinalState": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BreakpointOut"])
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
    types["SourceContextIn"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextIn"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextIn"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextIn"]
            ).optional(),
            "git": t.proxy(renames["GitSourceContextIn"]).optional(),
        }
    ).named(renames["SourceContextIn"])
    types["SourceContextOut"] = t.struct(
        {
            "gerrit": t.proxy(renames["GerritSourceContextOut"]).optional(),
            "cloudRepo": t.proxy(renames["CloudRepoSourceContextOut"]).optional(),
            "cloudWorkspace": t.proxy(
                renames["CloudWorkspaceSourceContextOut"]
            ).optional(),
            "git": t.proxy(renames["GitSourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])

    functions = {}
    functions["debuggerDebuggeesList"] = clouddebugger.get(
        "v2/debugger/debuggees",
        t.struct(
            {
                "project": t.string(),
                "clientVersion": t.string(),
                "includeInactive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDebuggeesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsGet"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "stripResults": t.boolean().optional(),
                "action.value": t.string().optional(),
                "includeAllUsers": t.boolean().optional(),
                "includeInactive": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBreakpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsSet"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "stripResults": t.boolean().optional(),
                "action.value": t.string().optional(),
                "includeAllUsers": t.boolean().optional(),
                "includeInactive": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBreakpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsDelete"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "stripResults": t.boolean().optional(),
                "action.value": t.string().optional(),
                "includeAllUsers": t.boolean().optional(),
                "includeInactive": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBreakpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["debuggerDebuggeesBreakpointsList"] = clouddebugger.get(
        "v2/debugger/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "stripResults": t.boolean().optional(),
                "action.value": t.string().optional(),
                "includeAllUsers": t.boolean().optional(),
                "includeInactive": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "clientVersion": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBreakpointsResponseOut"]),
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
    functions["controllerDebuggeesBreakpointsUpdate"] = clouddebugger.get(
        "v2/controller/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "agentId": t.string().optional(),
                "successOnTimeout": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListActiveBreakpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["controllerDebuggeesBreakpointsList"] = clouddebugger.get(
        "v2/controller/debuggees/{debuggeeId}/breakpoints",
        t.struct(
            {
                "agentId": t.string().optional(),
                "successOnTimeout": t.boolean().optional(),
                "waitToken": t.string().optional(),
                "debuggeeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListActiveBreakpointsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="clouddebugger",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
