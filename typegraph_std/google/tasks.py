from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_tasks():
    tasks = HTTPRuntime("https://tasks.googleapis.com/")

    renames = {
        "ErrorResponse": "_tasks_1_ErrorResponse",
        "TaskListsIn": "_tasks_2_TaskListsIn",
        "TaskListsOut": "_tasks_3_TaskListsOut",
        "TaskListIn": "_tasks_4_TaskListIn",
        "TaskListOut": "_tasks_5_TaskListOut",
        "TaskIn": "_tasks_6_TaskIn",
        "TaskOut": "_tasks_7_TaskOut",
        "TasksIn": "_tasks_8_TasksIn",
        "TasksOut": "_tasks_9_TasksOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TaskListsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskListIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["TaskListsIn"])
    types["TaskListsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskListOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskListsOut"])
    types["TaskListIn"] = t.struct(
        {
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "updated": t.string().optional(),
        }
    ).named(renames["TaskListIn"])
    types["TaskListOut"] = t.struct(
        {
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskListOut"])
    types["TaskIn"] = t.struct(
        {
            "status": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "completed": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "hidden": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "links": t.array(
                t.struct(
                    {
                        "link": t.string().optional(),
                        "type": t.string().optional(),
                        "description": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "due": t.string().optional(),
            "deleted": t.boolean().optional(),
            "position": t.string().optional(),
            "notes": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "status": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "completed": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "hidden": t.boolean().optional(),
            "selfLink": t.string().optional(),
            "links": t.array(
                t.struct(
                    {
                        "link": t.string().optional(),
                        "type": t.string().optional(),
                        "description": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "due": t.string().optional(),
            "deleted": t.boolean().optional(),
            "position": t.string().optional(),
            "notes": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
    types["TasksIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskIn"])).optional(),
        }
    ).named(renames["TasksIn"])
    types["TasksOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TasksOut"])

    functions = {}
    functions["tasklistsDelete"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsUpdate"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsPatch"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsInsert"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsGet"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsList"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksClear"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksUpdate"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksDelete"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksGet"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksList"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksInsert"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksPatch"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksMove"] = tasks.post(
        "tasks/v1/lists/{tasklist}/tasks/{task}/move",
        t.struct(
            {
                "parent": t.string().optional(),
                "previous": t.string().optional(),
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="tasks", renames=renames, types=Box(types), functions=Box(functions)
    )
