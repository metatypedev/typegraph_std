from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_billingbudgets():
    billingbudgets = HTTPRuntime("https://billingbudgets.googleapis.com/")

    renames = {
        "ErrorResponse": "_billingbudgets_1_ErrorResponse",
        "GoogleCloudBillingBudgetsV1NotificationsRuleIn": "_billingbudgets_2_GoogleCloudBillingBudgetsV1NotificationsRuleIn",
        "GoogleCloudBillingBudgetsV1NotificationsRuleOut": "_billingbudgets_3_GoogleCloudBillingBudgetsV1NotificationsRuleOut",
        "GoogleCloudBillingBudgetsV1FilterIn": "_billingbudgets_4_GoogleCloudBillingBudgetsV1FilterIn",
        "GoogleCloudBillingBudgetsV1FilterOut": "_billingbudgets_5_GoogleCloudBillingBudgetsV1FilterOut",
        "GoogleCloudBillingBudgetsV1BudgetAmountIn": "_billingbudgets_6_GoogleCloudBillingBudgetsV1BudgetAmountIn",
        "GoogleCloudBillingBudgetsV1BudgetAmountOut": "_billingbudgets_7_GoogleCloudBillingBudgetsV1BudgetAmountOut",
        "GoogleProtobufEmptyIn": "_billingbudgets_8_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_billingbudgets_9_GoogleProtobufEmptyOut",
        "GoogleTypeMoneyIn": "_billingbudgets_10_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_billingbudgets_11_GoogleTypeMoneyOut",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseIn": "_billingbudgets_12_GoogleCloudBillingBudgetsV1ListBudgetsResponseIn",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseOut": "_billingbudgets_13_GoogleCloudBillingBudgetsV1ListBudgetsResponseOut",
        "GoogleCloudBillingBudgetsV1CustomPeriodIn": "_billingbudgets_14_GoogleCloudBillingBudgetsV1CustomPeriodIn",
        "GoogleCloudBillingBudgetsV1CustomPeriodOut": "_billingbudgets_15_GoogleCloudBillingBudgetsV1CustomPeriodOut",
        "GoogleCloudBillingBudgetsV1ThresholdRuleIn": "_billingbudgets_16_GoogleCloudBillingBudgetsV1ThresholdRuleIn",
        "GoogleCloudBillingBudgetsV1ThresholdRuleOut": "_billingbudgets_17_GoogleCloudBillingBudgetsV1ThresholdRuleOut",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountIn": "_billingbudgets_18_GoogleCloudBillingBudgetsV1LastPeriodAmountIn",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountOut": "_billingbudgets_19_GoogleCloudBillingBudgetsV1LastPeriodAmountOut",
        "GoogleCloudBillingBudgetsV1BudgetIn": "_billingbudgets_20_GoogleCloudBillingBudgetsV1BudgetIn",
        "GoogleCloudBillingBudgetsV1BudgetOut": "_billingbudgets_21_GoogleCloudBillingBudgetsV1BudgetOut",
        "GoogleTypeDateIn": "_billingbudgets_22_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_billingbudgets_23_GoogleTypeDateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBillingBudgetsV1NotificationsRuleIn"] = t.struct(
        {
            "schemaVersion": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "disableDefaultIamRecipients": t.boolean().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"])
    types["GoogleCloudBillingBudgetsV1NotificationsRuleOut"] = t.struct(
        {
            "schemaVersion": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "disableDefaultIamRecipients": t.boolean().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"])
    types["GoogleCloudBillingBudgetsV1FilterIn"] = t.struct(
        {
            "resourceAncestors": t.array(t.string()).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subaccounts": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
            "creditTypes": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
            "projects": t.array(t.string()).optional(),
            "creditTypesTreatment": t.string().optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterIn"])
    types["GoogleCloudBillingBudgetsV1FilterOut"] = t.struct(
        {
            "resourceAncestors": t.array(t.string()).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subaccounts": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
            "creditTypes": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
            "projects": t.array(t.string()).optional(),
            "creditTypesTreatment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterOut"])
    types["GoogleCloudBillingBudgetsV1BudgetAmountIn"] = t.struct(
        {
            "specifiedAmount": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
            "lastPeriodAmount": t.proxy(
                renames["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"])
    types["GoogleCloudBillingBudgetsV1BudgetAmountOut"] = t.struct(
        {
            "specifiedAmount": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "lastPeriodAmount": t.proxy(
                renames["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetAmountOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
    types["GoogleCloudBillingBudgetsV1ListBudgetsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "budgets": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ListBudgetsResponseIn"])
    types["GoogleCloudBillingBudgetsV1ListBudgetsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "budgets": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ListBudgetsResponseOut"])
    types["GoogleCloudBillingBudgetsV1CustomPeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "startDate": t.proxy(renames["GoogleTypeDateIn"]),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1CustomPeriodIn"])
    types["GoogleCloudBillingBudgetsV1CustomPeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "startDate": t.proxy(renames["GoogleTypeDateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1CustomPeriodOut"])
    types["GoogleCloudBillingBudgetsV1ThresholdRuleIn"] = t.struct(
        {"spendBasis": t.string().optional(), "thresholdPercent": t.number()}
    ).named(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
    types["GoogleCloudBillingBudgetsV1ThresholdRuleOut"] = t.struct(
        {
            "spendBasis": t.string().optional(),
            "thresholdPercent": t.number(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ThresholdRuleOut"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"])
    types["GoogleCloudBillingBudgetsV1BudgetIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
            "etag": t.string().optional(),
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
            ).optional(),
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterIn"]
            ).optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetIn"])
    types["GoogleCloudBillingBudgetsV1BudgetOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountOut"]),
            "etag": t.string().optional(),
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleOut"])
            ).optional(),
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterOut"]
            ).optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])

    functions = {}
    functions["billingAccountsBudgetsGet"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsPatch"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsDelete"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsList"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsCreate"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="billingbudgets",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
