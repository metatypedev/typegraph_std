from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebaserules() -> Import:
    firebaserules = HTTPRuntime("https://firebaserules.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaserules_1_ErrorResponse",
        "TestResultIn": "_firebaserules_2_TestResultIn",
        "TestResultOut": "_firebaserules_3_TestResultOut",
        "ValueCountIn": "_firebaserules_4_ValueCountIn",
        "ValueCountOut": "_firebaserules_5_ValueCountOut",
        "ArgIn": "_firebaserules_6_ArgIn",
        "ArgOut": "_firebaserules_7_ArgOut",
        "ResultIn": "_firebaserules_8_ResultIn",
        "ResultOut": "_firebaserules_9_ResultOut",
        "SourceIn": "_firebaserules_10_SourceIn",
        "SourceOut": "_firebaserules_11_SourceOut",
        "TestRulesetRequestIn": "_firebaserules_12_TestRulesetRequestIn",
        "TestRulesetRequestOut": "_firebaserules_13_TestRulesetRequestOut",
        "ExpressionReportIn": "_firebaserules_14_ExpressionReportIn",
        "ExpressionReportOut": "_firebaserules_15_ExpressionReportOut",
        "EmptyIn": "_firebaserules_16_EmptyIn",
        "EmptyOut": "_firebaserules_17_EmptyOut",
        "FunctionCallIn": "_firebaserules_18_FunctionCallIn",
        "FunctionCallOut": "_firebaserules_19_FunctionCallOut",
        "IssueIn": "_firebaserules_20_IssueIn",
        "IssueOut": "_firebaserules_21_IssueOut",
        "ReleaseIn": "_firebaserules_22_ReleaseIn",
        "ReleaseOut": "_firebaserules_23_ReleaseOut",
        "TestCaseIn": "_firebaserules_24_TestCaseIn",
        "TestCaseOut": "_firebaserules_25_TestCaseOut",
        "TestRulesetResponseIn": "_firebaserules_26_TestRulesetResponseIn",
        "TestRulesetResponseOut": "_firebaserules_27_TestRulesetResponseOut",
        "FunctionMockIn": "_firebaserules_28_FunctionMockIn",
        "FunctionMockOut": "_firebaserules_29_FunctionMockOut",
        "GetReleaseExecutableResponseIn": "_firebaserules_30_GetReleaseExecutableResponseIn",
        "GetReleaseExecutableResponseOut": "_firebaserules_31_GetReleaseExecutableResponseOut",
        "UpdateReleaseRequestIn": "_firebaserules_32_UpdateReleaseRequestIn",
        "UpdateReleaseRequestOut": "_firebaserules_33_UpdateReleaseRequestOut",
        "SourcePositionIn": "_firebaserules_34_SourcePositionIn",
        "SourcePositionOut": "_firebaserules_35_SourcePositionOut",
        "MetadataIn": "_firebaserules_36_MetadataIn",
        "MetadataOut": "_firebaserules_37_MetadataOut",
        "VisitedExpressionIn": "_firebaserules_38_VisitedExpressionIn",
        "VisitedExpressionOut": "_firebaserules_39_VisitedExpressionOut",
        "ListRulesetsResponseIn": "_firebaserules_40_ListRulesetsResponseIn",
        "ListRulesetsResponseOut": "_firebaserules_41_ListRulesetsResponseOut",
        "RulesetIn": "_firebaserules_42_RulesetIn",
        "RulesetOut": "_firebaserules_43_RulesetOut",
        "FileIn": "_firebaserules_44_FileIn",
        "FileOut": "_firebaserules_45_FileOut",
        "TestSuiteIn": "_firebaserules_46_TestSuiteIn",
        "TestSuiteOut": "_firebaserules_47_TestSuiteOut",
        "ListReleasesResponseIn": "_firebaserules_48_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_firebaserules_49_ListReleasesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestResultIn"] = t.struct(
        {
            "functionCalls": t.array(t.proxy(renames["FunctionCallIn"])).optional(),
            "debugMessages": t.array(t.string()).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionIn"])
            ).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportIn"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["TestResultIn"])
    types["TestResultOut"] = t.struct(
        {
            "functionCalls": t.array(t.proxy(renames["FunctionCallOut"])).optional(),
            "debugMessages": t.array(t.string()).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionOut"])
            ).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportOut"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "state": t.string().optional(),
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
    types["ArgIn"] = t.struct(
        {
            "anyValue": t.proxy(renames["EmptyIn"]).optional(),
            "exactValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ArgIn"])
    types["ArgOut"] = t.struct(
        {
            "anyValue": t.proxy(renames["EmptyOut"]).optional(),
            "exactValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArgOut"])
    types["ResultIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "undefined": t.proxy(renames["EmptyIn"]).optional(),
        }
    ).named(renames["ResultIn"])
    types["ResultOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "undefined": t.proxy(renames["EmptyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultOut"])
    types["SourceIn"] = t.struct({"files": t.array(t.proxy(renames["FileIn"]))}).named(
        renames["SourceIn"]
    )
    types["SourceOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["TestRulesetRequestIn"] = t.struct(
        {
            "testSuite": t.proxy(renames["TestSuiteIn"]).optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
        }
    ).named(renames["TestRulesetRequestIn"])
    types["TestRulesetRequestOut"] = t.struct(
        {
            "testSuite": t.proxy(renames["TestSuiteOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestRulesetRequestOut"])
    types["ExpressionReportIn"] = t.struct(
        {
            "children": t.array(t.proxy(renames["ExpressionReportIn"])).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "values": t.array(t.proxy(renames["ValueCountIn"])).optional(),
        }
    ).named(renames["ExpressionReportIn"])
    types["ExpressionReportOut"] = t.struct(
        {
            "children": t.array(t.proxy(renames["ExpressionReportOut"])).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "values": t.array(t.proxy(renames["ValueCountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpressionReportOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["FunctionCallIn"] = t.struct(
        {
            "args": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
        }
    ).named(renames["FunctionCallIn"])
    types["FunctionCallOut"] = t.struct(
        {
            "args": t.array(t.struct({"_": t.string().optional()})).optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionCallOut"])
    types["IssueIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["ReleaseIn"] = t.struct(
        {"rulesetName": t.string(), "name": t.string()}
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "rulesetName": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
    types["TestCaseIn"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockIn"])).optional(),
            "expressionReportLevel": t.string().optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockOut"])).optional(),
            "expressionReportLevel": t.string().optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
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
    types["GetReleaseExecutableResponseIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "language": t.string().optional(),
            "rulesetName": t.string().optional(),
            "executable": t.string().optional(),
            "syncTime": t.string().optional(),
            "executableVersion": t.string().optional(),
        }
    ).named(renames["GetReleaseExecutableResponseIn"])
    types["GetReleaseExecutableResponseOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "language": t.string().optional(),
            "rulesetName": t.string().optional(),
            "executable": t.string().optional(),
            "syncTime": t.string().optional(),
            "executableVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReleaseExecutableResponseOut"])
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
    types["SourcePositionIn"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "fileName": t.string().optional(),
            "column": t.integer().optional(),
            "line": t.integer().optional(),
            "endOffset": t.integer().optional(),
        }
    ).named(renames["SourcePositionIn"])
    types["SourcePositionOut"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "fileName": t.string().optional(),
            "column": t.integer().optional(),
            "line": t.integer().optional(),
            "endOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourcePositionOut"])
    types["MetadataIn"] = t.struct({"services": t.array(t.string()).optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["VisitedExpressionIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
        }
    ).named(renames["VisitedExpressionIn"])
    types["VisitedExpressionOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VisitedExpressionOut"])
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
    types["RulesetIn"] = t.struct({"source": t.proxy(renames["SourceIn"])}).named(
        renames["RulesetIn"]
    )
    types["RulesetOut"] = t.struct(
        {
            "source": t.proxy(renames["SourceOut"]),
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RulesetOut"])
    types["FileIn"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "name": t.string(),
            "content": t.string(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "name": t.string(),
            "content": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["TestSuiteIn"] = t.struct(
        {"testCases": t.array(t.proxy(renames["TestCaseIn"])).optional()}
    ).named(renames["TestSuiteIn"])
    types["TestSuiteOut"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOut"])
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

    functions = {}
    functions["projectsTest"] = firebaserules.post(
        "v1/{name}:test",
        t.struct(
            {
                "name": t.string(),
                "testSuite": t.proxy(renames["TestSuiteIn"]).optional(),
                "source": t.proxy(renames["SourceIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestRulesetResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsDelete"] = firebaserules.post(
        "v1/{name}/rulesets",
        t.struct(
            {
                "name": t.string(),
                "source": t.proxy(renames["SourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsGet"] = firebaserules.post(
        "v1/{name}/rulesets",
        t.struct(
            {
                "name": t.string(),
                "source": t.proxy(renames["SourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsList"] = firebaserules.post(
        "v1/{name}/rulesets",
        t.struct(
            {
                "name": t.string(),
                "source": t.proxy(renames["SourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsCreate"] = firebaserules.post(
        "v1/{name}/rulesets",
        t.struct(
            {
                "name": t.string(),
                "source": t.proxy(renames["SourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesGet"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesCreate"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesDelete"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesList"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesPatch"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesGetExecutable"] = firebaserules.get(
        "v1/{name}:getExecutable",
        t.struct(
            {
                "name": t.string(),
                "executableVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetReleaseExecutableResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaserules", renames=renames, types=types, functions=functions
    )
