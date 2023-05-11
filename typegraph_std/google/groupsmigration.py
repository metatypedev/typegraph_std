from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_groupsmigration() -> Import:
    groupsmigration = HTTPRuntime("https://groupsmigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_groupsmigration_1_ErrorResponse",
        "GroupsIn": "_groupsmigration_2_GroupsIn",
        "GroupsOut": "_groupsmigration_3_GroupsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GroupsIn"] = t.struct(
        {"kind": t.string().optional(), "responseCode": t.string().optional()}
    ).named(renames["GroupsIn"])
    types["GroupsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "responseCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupsOut"])

    functions = {}
    functions["archiveInsert"] = groupsmigration.post(
        "groups/v1/groups/{groupId}/archive",
        t.struct({"groupId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GroupsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="groupsmigration", renames=renames, types=types, functions=functions
    )
