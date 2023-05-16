from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_tasks() -> Import:
    tasks = HTTPRuntime("https://tasks.googleapis.com/")

    renames = {
        "ErrorResponse": "_tasks_1_ErrorResponse",
        "TaskIn": "_tasks_2_TaskIn",
        "TaskOut": "_tasks_3_TaskOut",
        "TaskListsIn": "_tasks_4_TaskListsIn",
        "TaskListsOut": "_tasks_5_TaskListsOut",
        "TasksIn": "_tasks_6_TasksIn",
        "TasksOut": "_tasks_7_TasksOut",
        "TaskListIn": "_tasks_8_TaskListIn",
        "TaskListOut": "_tasks_9_TaskListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TaskIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "links": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "description": t.string().optional(),
                    }
                )
            ).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "due": t.string().optional(),
            "completed": t.string().optional(),
            "parent": t.string().optional(),
            "position": t.string().optional(),
            "deleted": t.boolean().optional(),
            "notes": t.string().optional(),
            "hidden": t.boolean().optional(),
            "etag": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["TaskIn"])
    types["TaskOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "links": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "description": t.string().optional(),
                    }
                )
            ).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "due": t.string().optional(),
            "completed": t.string().optional(),
            "parent": t.string().optional(),
            "position": t.string().optional(),
            "deleted": t.boolean().optional(),
            "notes": t.string().optional(),
            "hidden": t.boolean().optional(),
            "etag": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskOut"])
    types["TaskListsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskListIn"])).optional(),
        }
    ).named(renames["TaskListsIn"])
    types["TaskListsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["TaskListOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskListsOut"])
    types["TasksIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["TaskIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["TasksIn"])
    types["TasksOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["TaskOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TasksOut"])
    types["TaskListIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "title": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["TaskListIn"])
    types["TaskListOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "title": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TaskListOut"])

    functions = {}
    functions["tasklistsUpdate"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasklistsDelete"] = tasks.get(
        "tasks/v1/users/@me/lists",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskListsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksPatch"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksInsert"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksGet"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksClear"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksDelete"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksMove"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksList"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TaskOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tasksUpdate"] = tasks.put(
        "tasks/v1/lists/{tasklist}/tasks/{task}",
        t.struct(
            {
                "tasklist": t.string().optional(),
                "task": t.string().optional(),
                "kind": t.string().optional(),
                "status": t.string().optional(),
                "links": t.array(
                    t.struct(
                        {
                            "type": t.string().optional(),
                            "link": t.string().optional(),
                            "description": t.string().optional(),
                        }
                    )
                ).optional(),
                "updated": t.string().optional(),
                "id": t.string().optional(),
                "title": t.string().optional(),
                "due": t.string().optional(),
                "completed": t.string().optional(),
                "parent": t.string().optional(),
                "position": t.string().optional(),
                "deleted": t.boolean().optional(),
                "notes": t.string().optional(),
                "hidden": t.boolean().optional(),
                "etag": t.string().optional(),
                "selfLink": t.string().optional(),
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
