from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebaserules() -> Import:
    firebaserules = HTTPRuntime("https://firebaserules.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebaserules_1_ErrorResponse",
        "SourcePositionIn": "_firebaserules_2_SourcePositionIn",
        "SourcePositionOut": "_firebaserules_3_SourcePositionOut",
        "EmptyIn": "_firebaserules_4_EmptyIn",
        "EmptyOut": "_firebaserules_5_EmptyOut",
        "TestRulesetResponseIn": "_firebaserules_6_TestRulesetResponseIn",
        "TestRulesetResponseOut": "_firebaserules_7_TestRulesetResponseOut",
        "FileIn": "_firebaserules_8_FileIn",
        "FileOut": "_firebaserules_9_FileOut",
        "ReleaseIn": "_firebaserules_10_ReleaseIn",
        "ReleaseOut": "_firebaserules_11_ReleaseOut",
        "ListRulesetsResponseIn": "_firebaserules_12_ListRulesetsResponseIn",
        "ListRulesetsResponseOut": "_firebaserules_13_ListRulesetsResponseOut",
        "MetadataIn": "_firebaserules_14_MetadataIn",
        "MetadataOut": "_firebaserules_15_MetadataOut",
        "SourceIn": "_firebaserules_16_SourceIn",
        "SourceOut": "_firebaserules_17_SourceOut",
        "TestCaseIn": "_firebaserules_18_TestCaseIn",
        "TestCaseOut": "_firebaserules_19_TestCaseOut",
        "ArgIn": "_firebaserules_20_ArgIn",
        "ArgOut": "_firebaserules_21_ArgOut",
        "ExpressionReportIn": "_firebaserules_22_ExpressionReportIn",
        "ExpressionReportOut": "_firebaserules_23_ExpressionReportOut",
        "TestResultIn": "_firebaserules_24_TestResultIn",
        "TestResultOut": "_firebaserules_25_TestResultOut",
        "TestRulesetRequestIn": "_firebaserules_26_TestRulesetRequestIn",
        "TestRulesetRequestOut": "_firebaserules_27_TestRulesetRequestOut",
        "VisitedExpressionIn": "_firebaserules_28_VisitedExpressionIn",
        "VisitedExpressionOut": "_firebaserules_29_VisitedExpressionOut",
        "ListReleasesResponseIn": "_firebaserules_30_ListReleasesResponseIn",
        "ListReleasesResponseOut": "_firebaserules_31_ListReleasesResponseOut",
        "ValueCountIn": "_firebaserules_32_ValueCountIn",
        "ValueCountOut": "_firebaserules_33_ValueCountOut",
        "GetReleaseExecutableResponseIn": "_firebaserules_34_GetReleaseExecutableResponseIn",
        "GetReleaseExecutableResponseOut": "_firebaserules_35_GetReleaseExecutableResponseOut",
        "FunctionCallIn": "_firebaserules_36_FunctionCallIn",
        "FunctionCallOut": "_firebaserules_37_FunctionCallOut",
        "ResultIn": "_firebaserules_38_ResultIn",
        "ResultOut": "_firebaserules_39_ResultOut",
        "UpdateReleaseRequestIn": "_firebaserules_40_UpdateReleaseRequestIn",
        "UpdateReleaseRequestOut": "_firebaserules_41_UpdateReleaseRequestOut",
        "IssueIn": "_firebaserules_42_IssueIn",
        "IssueOut": "_firebaserules_43_IssueOut",
        "TestSuiteIn": "_firebaserules_44_TestSuiteIn",
        "TestSuiteOut": "_firebaserules_45_TestSuiteOut",
        "FunctionMockIn": "_firebaserules_46_FunctionMockIn",
        "FunctionMockOut": "_firebaserules_47_FunctionMockOut",
        "RulesetIn": "_firebaserules_48_RulesetIn",
        "RulesetOut": "_firebaserules_49_RulesetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SourcePositionIn"] = t.struct(
        {
            "endOffset": t.integer().optional(),
            "line": t.integer().optional(),
            "currentOffset": t.integer().optional(),
            "column": t.integer().optional(),
            "fileName": t.string().optional(),
        }
    ).named(renames["SourcePositionIn"])
    types["SourcePositionOut"] = t.struct(
        {
            "endOffset": t.integer().optional(),
            "line": t.integer().optional(),
            "currentOffset": t.integer().optional(),
            "column": t.integer().optional(),
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourcePositionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
            "fingerprint": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["FileIn"])
    types["FileOut"] = t.struct(
        {
            "content": t.string(),
            "fingerprint": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileOut"])
    types["ReleaseIn"] = t.struct(
        {"rulesetName": t.string(), "name": t.string()}
    ).named(renames["ReleaseIn"])
    types["ReleaseOut"] = t.struct(
        {
            "rulesetName": t.string(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReleaseOut"])
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
    types["MetadataIn"] = t.struct({"services": t.array(t.string()).optional()}).named(
        renames["MetadataIn"]
    )
    types["MetadataOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["SourceIn"] = t.struct({"files": t.array(t.proxy(renames["FileIn"]))}).named(
        renames["SourceIn"]
    )
    types["SourceOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["FileOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["TestCaseIn"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockIn"])).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "expressionReportLevel": t.string().optional(),
        }
    ).named(renames["TestCaseIn"])
    types["TestCaseOut"] = t.struct(
        {
            "functionMocks": t.array(t.proxy(renames["FunctionMockOut"])).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "pathEncoding": t.string().optional(),
            "expectation": t.string().optional(),
            "expressionReportLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestCaseOut"])
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
    types["ExpressionReportIn"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportIn"])).optional(),
            "values": t.array(t.proxy(renames["ValueCountIn"])).optional(),
        }
    ).named(renames["ExpressionReportIn"])
    types["ExpressionReportOut"] = t.struct(
        {
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "children": t.array(t.proxy(renames["ExpressionReportOut"])).optional(),
            "values": t.array(t.proxy(renames["ValueCountOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpressionReportOut"])
    types["TestResultIn"] = t.struct(
        {
            "functionCalls": t.array(t.proxy(renames["FunctionCallIn"])).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionIn"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "state": t.string().optional(),
            "debugMessages": t.array(t.string()).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportIn"])
            ).optional(),
        }
    ).named(renames["TestResultIn"])
    types["TestResultOut"] = t.struct(
        {
            "functionCalls": t.array(t.proxy(renames["FunctionCallOut"])).optional(),
            "visitedExpressions": t.array(
                t.proxy(renames["VisitedExpressionOut"])
            ).optional(),
            "errorPosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "state": t.string().optional(),
            "debugMessages": t.array(t.string()).optional(),
            "expressionReports": t.array(
                t.proxy(renames["ExpressionReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestResultOut"])
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
    types["GetReleaseExecutableResponseIn"] = t.struct(
        {
            "executableVersion": t.string().optional(),
            "syncTime": t.string().optional(),
            "rulesetName": t.string().optional(),
            "language": t.string().optional(),
            "executable": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["GetReleaseExecutableResponseIn"])
    types["GetReleaseExecutableResponseOut"] = t.struct(
        {
            "executableVersion": t.string().optional(),
            "syncTime": t.string().optional(),
            "rulesetName": t.string().optional(),
            "language": t.string().optional(),
            "executable": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetReleaseExecutableResponseOut"])
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
    types["IssueIn"] = t.struct(
        {
            "description": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionIn"]).optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["IssueIn"])
    types["IssueOut"] = t.struct(
        {
            "description": t.string().optional(),
            "sourcePosition": t.proxy(renames["SourcePositionOut"]).optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IssueOut"])
    types["TestSuiteIn"] = t.struct(
        {"testCases": t.array(t.proxy(renames["TestCaseIn"])).optional()}
    ).named(renames["TestSuiteIn"])
    types["TestSuiteOut"] = t.struct(
        {
            "testCases": t.array(t.proxy(renames["TestCaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestSuiteOut"])
    types["FunctionMockIn"] = t.struct(
        {
            "result": t.proxy(renames["ResultIn"]).optional(),
            "function": t.string().optional(),
            "args": t.array(t.proxy(renames["ArgIn"])).optional(),
        }
    ).named(renames["FunctionMockIn"])
    types["FunctionMockOut"] = t.struct(
        {
            "result": t.proxy(renames["ResultOut"]).optional(),
            "function": t.string().optional(),
            "args": t.array(t.proxy(renames["ArgOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionMockOut"])
    types["RulesetIn"] = t.struct({"source": t.proxy(renames["SourceIn"])}).named(
        renames["RulesetIn"]
    )
    types["RulesetOut"] = t.struct(
        {
            "metadata": t.proxy(renames["MetadataOut"]).optional(),
            "source": t.proxy(renames["SourceOut"]),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RulesetOut"])

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

    return Import(
        importer="firebaserules",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
