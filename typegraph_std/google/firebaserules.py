from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebaserules() -> Import:
    firebaserules = HTTPRuntime("https://firebaserules.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaserules_1_ErrorResponse",
        "TestRulesetRequestIn": "_firebaserules_2_TestRulesetRequestIn",
        "TestRulesetRequestOut": "_firebaserules_3_TestRulesetRequestOut",
        "FunctionMockIn": "_firebaserules_4_FunctionMockIn",
        "FunctionMockOut": "_firebaserules_5_FunctionMockOut",
        "IssueIn": "_firebaserules_6_IssueIn",
        "IssueOut": "_firebaserules_7_IssueOut",
        "RulesetIn": "_firebaserules_8_RulesetIn",
        "RulesetOut": "_firebaserules_9_RulesetOut",
        "SourcePositionIn": "_firebaserules_10_SourcePositionIn",
        "SourcePositionOut": "_firebaserules_11_SourcePositionOut",
        "SourceIn": "_firebaserules_12_SourceIn",
        "SourceOut": "_firebaserules_13_SourceOut",
        "GetReleaseExecutableResponseIn": "_firebaserules_14_GetReleaseExecutableResponseIn",
        "GetReleaseExecutableResponseOut": "_firebaserules_15_GetReleaseExecutableResponseOut",
        "ResultIn": "_firebaserules_16_ResultIn",
        "ResultOut": "_firebaserules_17_ResultOut",
        "TestCaseIn": "_firebaserules_18_TestCaseIn",
        "TestCaseOut": "_firebaserules_19_TestCaseOut",
        "TestSuiteIn": "_firebaserules_20_TestSuiteIn",
        "TestSuiteOut": "_firebaserules_21_TestSuiteOut",
        "EmptyIn": "_firebaserules_22_EmptyIn",
        "EmptyOut": "_firebaserules_23_EmptyOut",
        "FunctionCallIn": "_firebaserules_24_FunctionCallIn",
        "FunctionCallOut": "_firebaserules_25_FunctionCallOut",
        "TestRulesetResponseIn": "_firebaserules_26_TestRulesetResponseIn",
        "TestRulesetResponseOut": "_firebaserules_27_TestRulesetResponseOut",
        "ListReleasesResponseIn": "_firebaserules_28_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_firebaserules_29_ListReleasesResponseOut",
        "MetadataIn": "_firebaserules_30_MetadataIn",
        "MetadataOut": "_firebaserules_31_MetadataOut",
        "ListRulesetsResponseIn": "_firebaserules_32_ListRulesetsResponseIn",
        "ListRulesetsResponseOut": "_firebaserules_33_ListRulesetsResponseOut",
        "VisitedExpressionIn": "_firebaserules_34_VisitedExpressionIn",
        "VisitedExpressionOut": "_firebaserules_35_VisitedExpressionOut",
        "FileIn": "_firebaserules_36_FileIn",
        "FileOut": "_firebaserules_37_FileOut",
        "UpdateReleaseRequestIn": "_firebaserules_38_UpdateReleaseRequestIn",
        "UpdateReleaseRequestOut": "_firebaserules_39_UpdateReleaseRequestOut",
        "ExpressionReportIn": "_firebaserules_40_ExpressionReportIn",
        "ExpressionReportOut": "_firebaserules_41_ExpressionReportOut",
        "TestResultIn": "_firebaserules_42_TestResultIn",
        "TestResultOut": "_firebaserules_43_TestResultOut",
        "ValueCountIn": "_firebaserules_44_ValueCountIn",
        "ValueCountOut": "_firebaserules_45_ValueCountOut",
        "ArgIn": "_firebaserules_46_ArgIn",
        "ArgOut": "_firebaserules_47_ArgOut",
        "ReleaseIn": "_firebaserules_48_ReleaseIn",
        "ReleaseOut": "_firebaserules_49_ReleaseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["FunctionMockIn"] = t.struct(
        {
            "args": t.array(t.proxy(renames["ArgIn"])).optional(),
            "function": t.string().optional(),
            "result": t.proxy(renames["ResultIn"]).optional(),
        }
    ).named(renames["FunctionMockIn"])
    types["FunctionMockOut"] = t.struct(
        {
            "args": t.array(t.proxy(renames["ArgOut"])).optional(),
            "function": t.string().optional(),
            "result": t.proxy(renames["ResultOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionMockOut"])
    types["IssueIn"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "description": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
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
    types["SourcePositionIn"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "column": t.integer().optional(),
            "endOffset": t.integer().optional(),
            "fileName": t.string().optional(),
            "line": t.integer().optional(),
        }
    ).named(renames["SourcePositionIn"])
    types["SourcePositionOut"] = t.struct(
        {
            "currentOffset": t.integer().optional(),
            "column": t.integer().optional(),
            "endOffset": t.integer().optional(),
            "fileName": t.string().optional(),
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
    types["GetReleaseExecutableResponseIn"] = t.struct(
        {
            "rulesetName": t.string().optional(),
            "executableVersion": t.string().optional(),
            "language": t.string().optional(),
            "syncTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "executable": t.string().optional(),
        }
    ).named(renames["GetReleaseExecutableResponseIn"])
    types["GetReleaseExecutableResponseOut"] = t.struct(
        {
            "rulesetName": t.string().optional(),
            "executableVersion": t.string().optional(),
            "language": t.string().optional(),
            "syncTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "executable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReleaseExecutableResponseOut"])
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
    types["TestCaseIn"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockIn"])).optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "expressionReportLevel": t.string().optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockOut"])).optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "expressionReportLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
    types["TestSuiteIn"] = t.struct(
        {"testCases": t.array(t.proxy(renames["TestCaseIn"])).optional()}
    ).named(renames["TestSuiteIn"])
    types["TestSuiteOut"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOut"])
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
    types["TestRulesetResponseIn"] = t.struct(
        {
            "testResults": t.array(t.proxy(renames["TestResultIn"])).optional(),
            "issues": t.array(t.proxy(renames["IssueIn"])).optional(),
        }
    ).named(renames["TestRulesetResponseIn"])
    types["TestRulesetResponseOut"] = t.struct(
        {
            "testResults": t.array(t.proxy(renames["TestResultOut"])).optional(),
            "issues": t.array(t.proxy(renames["IssueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestRulesetResponseOut"])
    types["ListReleasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseIn"])).optional(),
        }
    ).named(renames["ListReleasesResponseIn"])
    types["ListReleasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(t.proxy(renames["ReleaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReleasesResponseOut"])
    types["MetadataIn"] = t.struct({"services": t.array(t.string()).optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["ListRulesetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rulesets": t.array(t.proxy(renames["RulesetIn"])).optional(),
        }
    ).named(renames["ListRulesetsResponseIn"])
    types["ListRulesetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rulesets": t.array(t.proxy(renames["RulesetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRulesetsResponseOut"])
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
    types["FileIn"] = t.struct(
        {
            "name": t.string(),
            "content": t.string(),
            "fingerprint": t.string().optional(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "name": t.string(),
            "content": t.string(),
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["UpdateReleaseRequestIn"] = t.struct(
        {"release": t.proxy(renames["ReleaseIn"]), "updateMask": t.string().optional()}
    ).named(renames["UpdateReleaseRequestIn"])
    types["UpdateReleaseRequestOut"] = t.struct(
        {
            "release": t.proxy(renames["ReleaseOut"]),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateReleaseRequestOut"])
    types["ExpressionReportIn"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "values": t.array(t.proxy(renames["ValueCountIn"])).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportIn"])).optional(),
        }
    ).named(renames["ExpressionReportIn"])
    types["ExpressionReportOut"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "values": t.array(t.proxy(renames["ValueCountOut"])).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpressionReportOut"])
    types["TestResultIn"] = t.struct(
        {
            "state": t.string().optional(),
            "errorPosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "debugMessages": t.array(t.string()).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionIn"])
            ).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportIn"])
            ).optional(),
            "functionCalls": t.array(t.proxy(renames["FunctionCallIn"])).optional(),
        }
    ).named(renames["TestResultIn"])
    types["TestResultOut"] = t.struct(
        {
            "state": t.string().optional(),
            "errorPosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "debugMessages": t.array(t.string()).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionOut"])
            ).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportOut"])
            ).optional(),
            "functionCalls": t.array(t.proxy(renames["FunctionCallOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestResultOut"])
    types["ValueCountIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "count": t.integer().optional(),
        }
    ).named(renames["ValueCountIn"])
    types["ValueCountOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueCountOut"])
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
        {"name": t.string(), "rulesetName": t.string()}
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "name": t.string(),
            "rulesetName": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])

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
    functions["projectsReleasesGet"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesList"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesDelete"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesPatch"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesGetExecutable"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsReleasesCreate"] = firebaserules.post(
        "v1/{name}/releases",
        t.struct(
            {
                "name": t.string(),
                "rulesetName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReleaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsList"] = firebaserules.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsDelete"] = firebaserules.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsCreate"] = firebaserules.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRulesetsGet"] = firebaserules.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RulesetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaserules",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
