from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_libraryagent() -> Import:
    libraryagent = HTTPRuntime("https://libraryagent.googleapis.com/")

    renames = {
        "ErrorResponse": "_libraryagent_1_ErrorResponse",
        "GoogleExampleLibraryagentV1ShelfIn": "_libraryagent_2_GoogleExampleLibraryagentV1ShelfIn",
        "GoogleExampleLibraryagentV1ShelfOut": "_libraryagent_3_GoogleExampleLibraryagentV1ShelfOut",
        "GoogleExampleLibraryagentV1ListBooksResponseIn": "_libraryagent_4_GoogleExampleLibraryagentV1ListBooksResponseIn",
        "GoogleExampleLibraryagentV1ListBooksResponseOut": "_libraryagent_5_GoogleExampleLibraryagentV1ListBooksResponseOut",
        "GoogleExampleLibraryagentV1ListShelvesResponseIn": "_libraryagent_6_GoogleExampleLibraryagentV1ListShelvesResponseIn",
        "GoogleExampleLibraryagentV1ListShelvesResponseOut": "_libraryagent_7_GoogleExampleLibraryagentV1ListShelvesResponseOut",
        "GoogleExampleLibraryagentV1BookIn": "_libraryagent_8_GoogleExampleLibraryagentV1BookIn",
        "GoogleExampleLibraryagentV1BookOut": "_libraryagent_9_GoogleExampleLibraryagentV1BookOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleExampleLibraryagentV1ShelfIn"] = t.struct(
        {"theme": t.string().optional(), "name": t.string().optional()}
    ).named(renames["GoogleExampleLibraryagentV1ShelfIn"])
    types["GoogleExampleLibraryagentV1ShelfOut"] = t.struct(
        {
            "theme": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1ShelfOut"])
    types["GoogleExampleLibraryagentV1ListBooksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "books": t.array(
                t.proxy(renames["GoogleExampleLibraryagentV1BookIn"])
            ).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1ListBooksResponseIn"])
    types["GoogleExampleLibraryagentV1ListBooksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "books": t.array(
                t.proxy(renames["GoogleExampleLibraryagentV1BookOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1ListBooksResponseOut"])
    types["GoogleExampleLibraryagentV1ListShelvesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "shelves": t.array(
                t.proxy(renames["GoogleExampleLibraryagentV1ShelfIn"])
            ).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1ListShelvesResponseIn"])
    types["GoogleExampleLibraryagentV1ListShelvesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "shelves": t.array(
                t.proxy(renames["GoogleExampleLibraryagentV1ShelfOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1ListShelvesResponseOut"])
    types["GoogleExampleLibraryagentV1BookIn"] = t.struct(
        {
            "author": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "read": t.boolean().optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1BookIn"])
    types["GoogleExampleLibraryagentV1BookOut"] = t.struct(
        {
            "author": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "read": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleExampleLibraryagentV1BookOut"])

    functions = {}
    functions["shelvesList"] = libraryagent.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1ShelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shelvesGet"] = libraryagent.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1ShelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shelvesBooksGet"] = libraryagent.post(
        "v1/{name}:return",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1BookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shelvesBooksList"] = libraryagent.post(
        "v1/{name}:return",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1BookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shelvesBooksBorrow"] = libraryagent.post(
        "v1/{name}:return",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1BookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shelvesBooksReturn"] = libraryagent.post(
        "v1/{name}:return",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleExampleLibraryagentV1BookOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="libraryagent", renames=renames, types=types, functions=functions
    )
