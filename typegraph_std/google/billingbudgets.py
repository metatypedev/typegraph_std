from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_billingbudgets() -> Import:
    billingbudgets = HTTPRuntime("https://billingbudgets.googleapis.com/")

    renames = {
        "ErrorResponse": "_billingbudgets_1_ErrorResponse",
        "GoogleCloudBillingBudgetsV1CustomPeriodIn": "_billingbudgets_2_GoogleCloudBillingBudgetsV1CustomPeriodIn",
        "GoogleCloudBillingBudgetsV1CustomPeriodOut": "_billingbudgets_3_GoogleCloudBillingBudgetsV1CustomPeriodOut",
        "GoogleTypeDateIn": "_billingbudgets_4_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_billingbudgets_5_GoogleTypeDateOut",
        "GoogleCloudBillingBudgetsV1FilterIn": "_billingbudgets_6_GoogleCloudBillingBudgetsV1FilterIn",
        "GoogleCloudBillingBudgetsV1FilterOut": "_billingbudgets_7_GoogleCloudBillingBudgetsV1FilterOut",
        "GoogleCloudBillingBudgetsV1ThresholdRuleIn": "_billingbudgets_8_GoogleCloudBillingBudgetsV1ThresholdRuleIn",
        "GoogleCloudBillingBudgetsV1ThresholdRuleOut": "_billingbudgets_9_GoogleCloudBillingBudgetsV1ThresholdRuleOut",
        "GoogleProtobufEmptyIn": "_billingbudgets_10_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_billingbudgets_11_GoogleProtobufEmptyOut",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountIn": "_billingbudgets_12_GoogleCloudBillingBudgetsV1LastPeriodAmountIn",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountOut": "_billingbudgets_13_GoogleCloudBillingBudgetsV1LastPeriodAmountOut",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseIn": "_billingbudgets_14_GoogleCloudBillingBudgetsV1ListBudgetsResponseIn",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseOut": "_billingbudgets_15_GoogleCloudBillingBudgetsV1ListBudgetsResponseOut",
        "GoogleCloudBillingBudgetsV1BudgetIn": "_billingbudgets_16_GoogleCloudBillingBudgetsV1BudgetIn",
        "GoogleCloudBillingBudgetsV1BudgetOut": "_billingbudgets_17_GoogleCloudBillingBudgetsV1BudgetOut",
        "GoogleCloudBillingBudgetsV1NotificationsRuleIn": "_billingbudgets_18_GoogleCloudBillingBudgetsV1NotificationsRuleIn",
        "GoogleCloudBillingBudgetsV1NotificationsRuleOut": "_billingbudgets_19_GoogleCloudBillingBudgetsV1NotificationsRuleOut",
        "GoogleCloudBillingBudgetsV1BudgetAmountIn": "_billingbudgets_20_GoogleCloudBillingBudgetsV1BudgetAmountIn",
        "GoogleCloudBillingBudgetsV1BudgetAmountOut": "_billingbudgets_21_GoogleCloudBillingBudgetsV1BudgetAmountOut",
        "GoogleTypeMoneyIn": "_billingbudgets_22_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_billingbudgets_23_GoogleTypeMoneyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBillingBudgetsV1CustomPeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["GoogleTypeDateIn"]),
            "endDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1CustomPeriodIn"])
    types["GoogleCloudBillingBudgetsV1CustomPeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["GoogleTypeDateOut"]),
            "endDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1CustomPeriodOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudBillingBudgetsV1FilterIn"] = t.struct(
        {
            "subaccounts": t.array(t.string()).optional(),
            "creditTypesTreatment": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodIn"]
            ).optional(),
            "projects": t.array(t.string()).optional(),
            "creditTypes": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterIn"])
    types["GoogleCloudBillingBudgetsV1FilterOut"] = t.struct(
        {
            "subaccounts": t.array(t.string()).optional(),
            "creditTypesTreatment": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodOut"]
            ).optional(),
            "projects": t.array(t.string()).optional(),
            "creditTypes": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterOut"])
    types["GoogleCloudBillingBudgetsV1ThresholdRuleIn"] = t.struct(
        {"thresholdPercent": t.number(), "spendBasis": t.string().optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
    types["GoogleCloudBillingBudgetsV1ThresholdRuleOut"] = t.struct(
        {
            "thresholdPercent": t.number(),
            "spendBasis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ThresholdRuleOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"])
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
    types["GoogleCloudBillingBudgetsV1BudgetIn"] = t.struct(
        {
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterIn"]
            ).optional(),
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
            ).optional(),
            "etag": t.string().optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetIn"])
    types["GoogleCloudBillingBudgetsV1BudgetOut"] = t.struct(
        {
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterOut"]
            ).optional(),
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleOut"])
            ).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetOut"])
    types["GoogleCloudBillingBudgetsV1NotificationsRuleIn"] = t.struct(
        {
            "disableDefaultIamRecipients": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "schemaVersion": t.string().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"])
    types["GoogleCloudBillingBudgetsV1NotificationsRuleOut"] = t.struct(
        {
            "disableDefaultIamRecipients": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "schemaVersion": t.string().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"])
    types["GoogleCloudBillingBudgetsV1BudgetAmountIn"] = t.struct(
        {
            "lastPeriodAmount": t.proxy(
                renames["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"]
            ).optional(),
            "specifiedAmount": t.proxy(renames["GoogleTypeMoneyIn"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"])
    types["GoogleCloudBillingBudgetsV1BudgetAmountOut"] = t.struct(
        {
            "lastPeriodAmount": t.proxy(
                renames["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"]
            ).optional(),
            "specifiedAmount": t.proxy(renames["GoogleTypeMoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetAmountOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])

    functions = {}
    functions["billingAccountsBudgetsList"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "etag": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
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
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "etag": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
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
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "etag": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsGet"] = billingbudgets.post(
        "v1/{parent}/budgets",
        t.struct(
            {
                "parent": t.string(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "etag": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
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
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "etag": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
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
