from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_billingbudgets() -> Import:
    billingbudgets = HTTPRuntime("https://billingbudgets.googleapis.com/")

    renames = {
        "ErrorResponse": "_billingbudgets_1_ErrorResponse",
        "GoogleTypeDateIn": "_billingbudgets_2_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_billingbudgets_3_GoogleTypeDateOut",
        "GoogleProtobufEmptyIn": "_billingbudgets_4_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_billingbudgets_5_GoogleProtobufEmptyOut",
        "GoogleCloudBillingBudgetsV1BudgetIn": "_billingbudgets_6_GoogleCloudBillingBudgetsV1BudgetIn",
        "GoogleCloudBillingBudgetsV1BudgetOut": "_billingbudgets_7_GoogleCloudBillingBudgetsV1BudgetOut",
        "GoogleCloudBillingBudgetsV1CustomPeriodIn": "_billingbudgets_8_GoogleCloudBillingBudgetsV1CustomPeriodIn",
        "GoogleCloudBillingBudgetsV1CustomPeriodOut": "_billingbudgets_9_GoogleCloudBillingBudgetsV1CustomPeriodOut",
        "GoogleCloudBillingBudgetsV1NotificationsRuleIn": "_billingbudgets_10_GoogleCloudBillingBudgetsV1NotificationsRuleIn",
        "GoogleCloudBillingBudgetsV1NotificationsRuleOut": "_billingbudgets_11_GoogleCloudBillingBudgetsV1NotificationsRuleOut",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountIn": "_billingbudgets_12_GoogleCloudBillingBudgetsV1LastPeriodAmountIn",
        "GoogleCloudBillingBudgetsV1LastPeriodAmountOut": "_billingbudgets_13_GoogleCloudBillingBudgetsV1LastPeriodAmountOut",
        "GoogleCloudBillingBudgetsV1FilterIn": "_billingbudgets_14_GoogleCloudBillingBudgetsV1FilterIn",
        "GoogleCloudBillingBudgetsV1FilterOut": "_billingbudgets_15_GoogleCloudBillingBudgetsV1FilterOut",
        "GoogleTypeMoneyIn": "_billingbudgets_16_GoogleTypeMoneyIn",
        "GoogleTypeMoneyOut": "_billingbudgets_17_GoogleTypeMoneyOut",
        "GoogleCloudBillingBudgetsV1BudgetAmountIn": "_billingbudgets_18_GoogleCloudBillingBudgetsV1BudgetAmountIn",
        "GoogleCloudBillingBudgetsV1BudgetAmountOut": "_billingbudgets_19_GoogleCloudBillingBudgetsV1BudgetAmountOut",
        "GoogleCloudBillingBudgetsV1ThresholdRuleIn": "_billingbudgets_20_GoogleCloudBillingBudgetsV1ThresholdRuleIn",
        "GoogleCloudBillingBudgetsV1ThresholdRuleOut": "_billingbudgets_21_GoogleCloudBillingBudgetsV1ThresholdRuleOut",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseIn": "_billingbudgets_22_GoogleCloudBillingBudgetsV1ListBudgetsResponseIn",
        "GoogleCloudBillingBudgetsV1ListBudgetsResponseOut": "_billingbudgets_23_GoogleCloudBillingBudgetsV1ListBudgetsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudBillingBudgetsV1BudgetIn"] = t.struct(
        {
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
            ).optional(),
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
            ).optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetIn"])
    types["GoogleCloudBillingBudgetsV1BudgetOut"] = t.struct(
        {
            "name": t.string().optional(),
            "thresholdRules": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleOut"])
            ).optional(),
            "budgetFilter": t.proxy(
                renames["GoogleCloudBillingBudgetsV1FilterOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "notificationsRule": t.proxy(
                renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"]
            ).optional(),
            "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountOut"]),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1BudgetOut"])
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
    types["GoogleCloudBillingBudgetsV1NotificationsRuleIn"] = t.struct(
        {
            "schemaVersion": t.string().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
            "disableDefaultIamRecipients": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"])
    types["GoogleCloudBillingBudgetsV1NotificationsRuleOut"] = t.struct(
        {
            "schemaVersion": t.string().optional(),
            "monitoringNotificationChannels": t.array(t.string()).optional(),
            "disableDefaultIamRecipients": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1NotificationsRuleOut"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountIn"])
    types["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBillingBudgetsV1LastPeriodAmountOut"])
    types["GoogleCloudBillingBudgetsV1FilterIn"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodIn"]
            ).optional(),
            "projects": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subaccounts": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
            "creditTypesTreatment": t.string().optional(),
            "creditTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterIn"])
    types["GoogleCloudBillingBudgetsV1FilterOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "customPeriod": t.proxy(
                renames["GoogleCloudBillingBudgetsV1CustomPeriodOut"]
            ).optional(),
            "projects": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subaccounts": t.array(t.string()).optional(),
            "calendarPeriod": t.string().optional(),
            "creditTypesTreatment": t.string().optional(),
            "creditTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1FilterOut"])
    types["GoogleTypeMoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
        }
    ).named(renames["GoogleTypeMoneyIn"])
    types["GoogleTypeMoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "units": t.string().optional(),
            "currencyCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeMoneyOut"])
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
    types["GoogleCloudBillingBudgetsV1ListBudgetsResponseIn"] = t.struct(
        {
            "budgets": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ListBudgetsResponseIn"])
    types["GoogleCloudBillingBudgetsV1ListBudgetsResponseOut"] = t.struct(
        {
            "budgets": t.array(
                t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBillingBudgetsV1ListBudgetsResponseOut"])

    functions = {}
    functions["billingAccountsBudgetsGet"] = billingbudgets.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsList"] = billingbudgets.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsDelete"] = billingbudgets.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsCreate"] = billingbudgets.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["billingAccountsBudgetsPatch"] = billingbudgets.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "thresholdRules": t.array(
                    t.proxy(renames["GoogleCloudBillingBudgetsV1ThresholdRuleIn"])
                ).optional(),
                "budgetFilter": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1FilterIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "notificationsRule": t.proxy(
                    renames["GoogleCloudBillingBudgetsV1NotificationsRuleIn"]
                ).optional(),
                "amount": t.proxy(renames["GoogleCloudBillingBudgetsV1BudgetAmountIn"]),
                "etag": t.string().optional(),
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
