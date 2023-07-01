from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebaserules():
    firebaserules = HTTPRuntime("https://firebaserules.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaserules_1_ErrorResponse",
        "TestSuiteIn": "_firebaserules_2_TestSuiteIn",
        "TestSuiteOut": "_firebaserules_3_TestSuiteOut",
        "MetadataIn": "_firebaserules_4_MetadataIn",
        "MetadataOut": "_firebaserules_5_MetadataOut",
        "SourcePositionIn": "_firebaserules_6_SourcePositionIn",
        "SourcePositionOut": "_firebaserules_7_SourcePositionOut",
        "SourceIn": "_firebaserules_8_SourceIn",
        "SourceOut": "_firebaserules_9_SourceOut",
        "FunctionMockIn": "_firebaserules_10_FunctionMockIn",
        "FunctionMockOut": "_firebaserules_11_FunctionMockOut",
        "TestResultIn": "_firebaserules_12_TestResultIn",
        "TestResultOut": "_firebaserules_13_TestResultOut",
        "ValueCountIn": "_firebaserules_14_ValueCountIn",
        "ValueCountOut": "_firebaserules_15_ValueCountOut",
        "TestCaseIn": "_firebaserules_16_TestCaseIn",
        "TestCaseOut": "_firebaserules_17_TestCaseOut",
        "UpdateReleaseRequestIn": "_firebaserules_18_UpdateReleaseRequestIn",
        "UpdateReleaseRequestOut": "_firebaserules_19_UpdateReleaseRequestOut",
        "ExpressionReportIn": "_firebaserules_20_ExpressionReportIn",
        "ExpressionReportOut": "_firebaserules_21_ExpressionReportOut",
        "GetReleaseExecutableResponseIn": "_firebaserules_22_GetReleaseExecutableResponseIn",
        "GetReleaseExecutableResponseOut": "_firebaserules_23_GetReleaseExecutableResponseOut",
        "ListReleasesResponseIn": "_firebaserules_24_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_firebaserules_25_ListReleasesResponseOut",
        "IssueIn": "_firebaserules_26_IssueIn",
        "IssueOut": "_firebaserules_27_IssueOut",
        "ResultIn": "_firebaserules_28_ResultIn",
        "ResultOut": "_firebaserules_29_ResultOut",
        "FunctionCallIn": "_firebaserules_30_FunctionCallIn",
        "FunctionCallOut": "_firebaserules_31_FunctionCallOut",
        "ArgIn": "_firebaserules_32_ArgIn",
        "ArgOut": "_firebaserules_33_ArgOut",
        "ReleaseIn": "_firebaserules_34_ReleaseIn",
        "ReleaseOut": "_firebaserules_35_ReleaseOut",
        "RulesetIn": "_firebaserules_36_RulesetIn",
        "RulesetOut": "_firebaserules_37_RulesetOut",
        "ListRulesetsResponseIn": "_firebaserules_38_ListRulesetsResponseIn",
        "ListRulesetsResponseOut": "_firebaserules_39_ListRulesetsResponseOut",
        "TestRulesetResponseIn": "_firebaserules_40_TestRulesetResponseIn",
        "TestRulesetResponseOut": "_firebaserules_41_TestRulesetResponseOut",
        "FileIn": "_firebaserules_42_FileIn",
        "FileOut": "_firebaserules_43_FileOut",
        "VisitedExpressionIn": "_firebaserules_44_VisitedExpressionIn",
        "VisitedExpressionOut": "_firebaserules_45_VisitedExpressionOut",
        "TestRulesetRequestIn": "_firebaserules_46_TestRulesetRequestIn",
        "TestRulesetRequestOut": "_firebaserules_47_TestRulesetRequestOut",
        "EmptyIn": "_firebaserules_48_EmptyIn",
        "EmptyOut": "_firebaserules_49_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestSuiteIn"] = t.struct(
        {"testCases": t.array(t.proxy(renames["TestCaseIn"])).optional()}
    ).named(renames["TestSuiteIn"])
    types["TestSuiteOut"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOut"])
    types["MetadataIn"] = t.struct({"services": t.array(t.string()).optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["SourcePositionIn"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "fileName": t.string().optional(),
            "column": t.integer().optional(),
            "endOffset": t.integer().optional(),
            "line": t.integer().optional(),
        }
    ).named(renames["SourcePositionIn"])
    types["SourcePositionOut"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "fileName": t.string().optional(),
            "column": t.integer().optional(),
            "endOffset": t.integer().optional(),
            "line": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourcePositionOut"])
    types["SourceIn"] = t.struct({"files": t.array(t.proxy(renames["FileIn"]))}).named(
        renames["SourceIn"]
    )
    types["SourceOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["FunctionMockIn"] = t.struct(
        {
            "args": t.array(t.proxy(renames["ArgIn"])).optional(),
            "result": t.proxy(renames["ResultIn"]).optional(),
            "function": t.string().optional(),
        }
    ).named(renames["FunctionMockIn"])
    types["FunctionMockOut"] = t.struct(
        {
            "args": t.array(t.proxy(renames["ArgOut"])).optional(),
            "result": t.proxy(renames["ResultOut"]).optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionMockOut"])
    types["TestResultIn"] = t.struct(
        {
            "debugMessages": t.array(t.string()).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportIn"])
            ).optional(),
            "state": t.string().optional(),
            "functionCalls": t.array(t.proxy(renames["FunctionCallIn"])).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionIn"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionIn"]).optional(),
        }
    ).named(renames["TestResultIn"])
    types["TestResultOut"] = t.struct(
        {
            "debugMessages": t.array(t.string()).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportOut"])
            ).optional(),
            "state": t.string().optional(),
            "functionCalls": t.array(t.proxy(renames["FunctionCallOut"])).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionOut"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestResultOut"])
    types["ValueCountIn"] = t.struct(
        {
            "count": t.integer().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ValueCountIn"])
    types["ValueCountOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueCountOut"])
    types["TestCaseIn"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockIn"])).optional(),
            "pathEncoding": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "expectation": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "expressionReportLevel": t.string().optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockOut"])).optional(),
            "pathEncoding": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "expectation": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "expressionReportLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["UpdateReleaseRequestIn"] = t.struct(
        {"updateMask": t.string().optional(), "release": t.proxy(renames["ReleaseIn"])}
    ).named(renames["UpdateReleaseRequestIn"])
    types["UpdateReleaseRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "release": t.proxy(renames["ReleaseOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateReleaseRequestOut"])
    types["ExpressionReportIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueCountIn"])).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportIn"])).optional(),
        }
    ).named(renames["ExpressionReportIn"])
    types["ExpressionReportOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueCountOut"])).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpressionReportOut"])
    types["GetReleaseExecutableResponseIn"] = t.struct(
        {
            "rulesetName": t.string().optional(),
            "executableVersion": t.string().optional(),
            "executable": t.string().optional(),
            "language": t.string().optional(),
            "updateTime": t.string().optional(),
            "syncTime": t.string().optional(),
        }
    ).named(renames["GetReleaseExecutableResponseIn"])
    types["GetReleaseExecutableResponseOut"] = t.struct(
        {
            "rulesetName": t.string().optional(),
            "executableVersion": t.string().optional(),
            "executable": t.string().optional(),
            "language": t.string().optional(),
            "updateTime": t.string().optional(),
            "syncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReleaseExecutableResponseOut"])
    types["ListReleasesResponseIn"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["IssueIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["ResultIn"] = t.struct(
        {
            "undefined": t.proxy(renames["EmptyIn"]).optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "undefined": t.proxy(renames["EmptyOut"]).optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["FunctionCallIn"] = t.struct(
        {
            "function": t.string().optional(),
            "args": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["FunctionCallIn"])
    types["FunctionCallOut"] = t.struct(
        {
            "function": t.string().optional(),
            "args": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionCallOut"])
    types["ArgIn"] = t.struct(
        {
            "exactValue": t.struct({"_": t.string().optional()}).optional(),
            "anyValue": t.proxy(renames["EmptyIn"]).optional(),
        }
    ).named(renames["ArgIn"])
    types["ArgOut"] = t.struct(
        {
            "exactValue": t.struct({"_": t.string().optional()}).optional(),
            "anyValue": t.proxy(renames["EmptyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArgOut"])
    types["ReleaseIn"] = t.struct(
        {"rulesetName": t.string(), "name": t.string()}
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "rulesetName": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["RulesetIn"] = t.struct({"source": t.proxy(renames["SourceIn"])}).named(
        renames["RulesetIn"]
    )
    types["RulesetOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RulesetOut"])
    types["ListRulesetsResponseIn"] = t.struct(
        {
            "rulesets": t.array(t.proxy(renames["RulesetIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRulesetsResponseIn"])
    types["ListRulesetsResponseOut"] = t.struct(
        {
            "rulesets": t.array(t.proxy(renames["RulesetOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRulesetsResponseOut"])
    types["TestRulesetResponseIn"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
            "testResults": t.array(t.proxy(renames["TestResultIn"])).optional(),
        }
    ).named(renames["TestRulesetResponseIn"])
    types["TestRulesetResponseOut"] = t.struct(
        {
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "testResults": t.array(t.proxy(renames["TestResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestRulesetResponseOut"])
    types["FileIn"] = t.struct(
        {
            "content": t.string(),
            "name": t.string(),
            "fingerprint": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "content": t.string(),
            "name": t.string(),
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["VisitedExpressionIn"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["VisitedExpressionIn"])
    types["VisitedExpressionOut"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisitedExpressionOut"])
    types["TestRulesetRequestIn"] = t.struct(
        {
            "source": t.proxy(renames["SourceIn"]).optional(),
            "testSuite": t.proxy(renames["TestSuiteIn"]).optional(),
        }
    ).named(renames["TestRulesetRequestIn"])
    types["TestRulesetRequestOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]).optional(),
            "testSuite": t.proxy(renames["TestSuiteOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestRulesetRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["projectsTest"] = firebaserules.post(
        "v1/{name}:test",
        t.struct(
            {
                "name": t.string(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "testSuite": t.proxy(renames["TestSuiteIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestRulesetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesGetExecutable"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesPatch"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesCreate"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesGet"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesList"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesDelete"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsList"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsCreate"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsGet"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsDelete"] = firebaserules.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaserules",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
