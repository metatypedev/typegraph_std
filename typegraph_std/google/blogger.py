from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_blogger() -> Import:
    blogger = HTTPRuntime("https://blogger.googleapis.com/")

    renames = {
        "ErrorResponse": "_blogger_1_ErrorResponse",
        "PageListIn": "_blogger_2_PageListIn",
        "PageListOut": "_blogger_3_PageListOut",
        "PostUserInfosListIn": "_blogger_4_PostUserInfosListIn",
        "PostUserInfosListOut": "_blogger_5_PostUserInfosListOut",
        "BlogListIn": "_blogger_6_BlogListIn",
        "BlogListOut": "_blogger_7_BlogListOut",
        "PostListIn": "_blogger_8_PostListIn",
        "PostListOut": "_blogger_9_PostListOut",
        "PageviewsIn": "_blogger_10_PageviewsIn",
        "PageviewsOut": "_blogger_11_PageviewsOut",
        "CommentIn": "_blogger_12_CommentIn",
        "CommentOut": "_blogger_13_CommentOut",
        "BlogPerUserInfoIn": "_blogger_14_BlogPerUserInfoIn",
        "BlogPerUserInfoOut": "_blogger_15_BlogPerUserInfoOut",
        "PageIn": "_blogger_16_PageIn",
        "PageOut": "_blogger_17_PageOut",
        "BlogUserInfoIn": "_blogger_18_BlogUserInfoIn",
        "BlogUserInfoOut": "_blogger_19_BlogUserInfoOut",
        "UserIn": "_blogger_20_UserIn",
        "UserOut": "_blogger_21_UserOut",
        "PostPerUserInfoIn": "_blogger_22_PostPerUserInfoIn",
        "PostPerUserInfoOut": "_blogger_23_PostPerUserInfoOut",
        "PostUserInfoIn": "_blogger_24_PostUserInfoIn",
        "PostUserInfoOut": "_blogger_25_PostUserInfoOut",
        "CommentListIn": "_blogger_26_CommentListIn",
        "CommentListOut": "_blogger_27_CommentListOut",
        "BlogIn": "_blogger_28_BlogIn",
        "BlogOut": "_blogger_29_BlogOut",
        "PostIn": "_blogger_30_PostIn",
        "PostOut": "_blogger_31_PostOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PageListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PageIn"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PageListIn"])
    types["PageListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PageOut"])).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageListOut"])
    types["PostUserInfosListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostUserInfoIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PostUserInfosListIn"])
    types["PostUserInfosListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostUserInfoOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostUserInfosListOut"])
    types["BlogListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogUserInfos": t.array(t.proxy(renames["BlogUserInfoIn"])).optional(),
            "items": t.array(t.proxy(renames["BlogIn"])).optional(),
        }
    ).named(renames["BlogListIn"])
    types["BlogListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogUserInfos": t.array(t.proxy(renames["BlogUserInfoOut"])).optional(),
            "items": t.array(t.proxy(renames["BlogOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogListOut"])
    types["PostListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PostListIn"])
    types["PostListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostListOut"])
    types["PageviewsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "counts": t.array(
                t.struct(
                    {"count": t.string().optional(), "timeRange": t.string().optional()}
                )
            ).optional(),
        }
    ).named(renames["PageviewsIn"])
    types["PageviewsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "counts": t.array(
                t.struct(
                    {"count": t.string().optional(), "timeRange": t.string().optional()}
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageviewsOut"])
    types["CommentIn"] = t.struct(
        {
            "published": t.string().optional(),
            "inReplyTo": t.struct({"id": t.string().optional()}).optional(),
            "author": t.struct(
                {
                    "url": t.string().optional(),
                    "id": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "content": t.string().optional(),
            "selfLink": t.string().optional(),
            "post": t.struct({"id": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "published": t.string().optional(),
            "inReplyTo": t.struct({"id": t.string().optional()}).optional(),
            "author": t.struct(
                {
                    "url": t.string().optional(),
                    "id": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "content": t.string().optional(),
            "selfLink": t.string().optional(),
            "post": t.struct({"id": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["BlogPerUserInfoIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "role": t.string().optional(),
            "hasAdminAccess": t.boolean().optional(),
            "userId": t.string().optional(),
            "photosAlbumKey": t.string().optional(),
        }
    ).named(renames["BlogPerUserInfoIn"])
    types["BlogPerUserInfoOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "role": t.string().optional(),
            "hasAdminAccess": t.boolean().optional(),
            "userId": t.string().optional(),
            "photosAlbumKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogPerUserInfoOut"])
    types["PageIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "content": t.string().optional(),
            "status": t.string().optional(),
            "updated": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "author": t.struct(
                {
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "trashed": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "published": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "etag": t.string().optional(),
            "content": t.string().optional(),
            "status": t.string().optional(),
            "updated": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "author": t.struct(
                {
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "trashed": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "published": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["BlogUserInfoIn"] = t.struct(
        {
            "blog": t.proxy(renames["BlogIn"]).optional(),
            "kind": t.string().optional(),
            "blog_user_info": t.proxy(renames["BlogPerUserInfoIn"]).optional(),
        }
    ).named(renames["BlogUserInfoIn"])
    types["BlogUserInfoOut"] = t.struct(
        {
            "blog": t.proxy(renames["BlogOut"]).optional(),
            "kind": t.string().optional(),
            "blog_user_info": t.proxy(renames["BlogPerUserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogUserInfoOut"])
    types["UserIn"] = t.struct(
        {
            "locale": t.struct(
                {
                    "language": t.string().optional(),
                    "variant": t.string().optional(),
                    "country": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "created": t.string().optional(),
            "about": t.string().optional(),
            "blogs": t.struct({"selfLink": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "locale": t.struct(
                {
                    "language": t.string().optional(),
                    "variant": t.string().optional(),
                    "country": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "created": t.string().optional(),
            "about": t.string().optional(),
            "blogs": t.struct({"selfLink": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["PostPerUserInfoIn"] = t.struct(
        {
            "hasEditAccess": t.boolean().optional(),
            "kind": t.string().optional(),
            "postId": t.string().optional(),
            "blogId": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["PostPerUserInfoIn"])
    types["PostPerUserInfoOut"] = t.struct(
        {
            "hasEditAccess": t.boolean().optional(),
            "kind": t.string().optional(),
            "postId": t.string().optional(),
            "blogId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostPerUserInfoOut"])
    types["PostUserInfoIn"] = t.struct(
        {
            "post": t.proxy(renames["PostIn"]).optional(),
            "post_user_info": t.proxy(renames["PostPerUserInfoIn"]).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PostUserInfoIn"])
    types["PostUserInfoOut"] = t.struct(
        {
            "post": t.proxy(renames["PostOut"]).optional(),
            "post_user_info": t.proxy(renames["PostPerUserInfoOut"]).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostUserInfoOut"])
    types["CommentListIn"] = t.struct(
        {
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CommentListIn"])
    types["CommentListOut"] = t.struct(
        {
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListOut"])
    types["BlogIn"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "updated": t.string().optional(),
            "posts": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "items": t.array(t.proxy(renames["PostIn"])).optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "customMetaData": t.string().optional(),
            "name": t.string().optional(),
            "pages": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "published": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "locale": t.struct(
                {
                    "country": t.string().optional(),
                    "language": t.string().optional(),
                    "variant": t.string().optional(),
                }
            ).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["BlogIn"])
    types["BlogOut"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "updated": t.string().optional(),
            "posts": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "items": t.array(t.proxy(renames["PostOut"])).optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "customMetaData": t.string().optional(),
            "name": t.string().optional(),
            "pages": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "published": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "locale": t.struct(
                {
                    "country": t.string().optional(),
                    "language": t.string().optional(),
                    "variant": t.string().optional(),
                }
            ).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogOut"])
    types["PostIn"] = t.struct(
        {
            "titleLink": t.string().optional(),
            "trashed": t.string().optional(),
            "replies": t.struct(
                {
                    "totalItems": t.string().optional(),
                    "items": t.array(t.proxy(renames["CommentIn"])).optional(),
                    "selfLink": t.string().optional(),
                }
            ).optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "readerComments": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "content": t.string().optional(),
            "url": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "customMetaData": t.string().optional(),
            "published": t.string().optional(),
            "location": t.struct(
                {
                    "lat": t.number().optional(),
                    "name": t.string().optional(),
                    "lng": t.number().optional(),
                    "span": t.string().optional(),
                }
            ).optional(),
            "images": t.array(t.struct({"url": t.string()})).optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "etag": t.string().optional(),
            "author": t.struct(
                {
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "id": t.string().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["PostIn"])
    types["PostOut"] = t.struct(
        {
            "titleLink": t.string().optional(),
            "trashed": t.string().optional(),
            "replies": t.struct(
                {
                    "totalItems": t.string().optional(),
                    "items": t.array(t.proxy(renames["CommentOut"])).optional(),
                    "selfLink": t.string().optional(),
                }
            ).optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "readerComments": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "content": t.string().optional(),
            "url": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "customMetaData": t.string().optional(),
            "published": t.string().optional(),
            "location": t.struct(
                {
                    "lat": t.number().optional(),
                    "name": t.string().optional(),
                    "lng": t.number().optional(),
                    "span": t.string().optional(),
                }
            ).optional(),
            "images": t.array(t.struct({"url": t.string()})).optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "etag": t.string().optional(),
            "author": t.struct(
                {
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                    "id": t.string().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])

    functions = {}
    functions["postsUpdate"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsPatch"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsRevert"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsGetByPath"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsDelete"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsList"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsPublish"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsGet"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsInsert"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsSearch"] = blogger.get(
        "v3/blogs/{blogId}/posts/search",
        t.struct(
            {
                "q": t.string(),
                "orderBy": t.string(),
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesInsert"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesRevert"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesGet"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesPublish"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesPatch"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesDelete"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesUpdate"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesList"] = blogger.get(
        "v3/blogs/{blogId}/pages",
        t.struct(
            {
                "blogId": t.string(),
                "fetchBodies": t.boolean(),
                "view": t.string(),
                "status": t.string(),
                "maxResults": t.integer(),
                "pageToken": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsRemoveContent"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsListByBlog"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsApprove"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsMarkAsSpam"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsGet"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsDelete"] = blogger.delete(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}",
        t.struct(
            {
                "commentId": t.string(),
                "blogId": t.string(),
                "postId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogUserInfosGet"] = blogger.get(
        "v3/users/{userId}/blogs/{blogId}",
        t.struct(
            {
                "blogId": t.string(),
                "maxPosts": t.integer(),
                "userId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BlogUserInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = blogger.get(
        "v3/users/{userId}",
        t.struct({"userId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pageViewsGet"] = blogger.get(
        "v3/blogs/{blogId}/pageviews",
        t.struct(
            {"range": t.string(), "blogId": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["PageviewsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsGetByUrl"] = blogger.get(
        "v3/blogs/{blogId}",
        t.struct(
            {
                "view": t.string(),
                "blogId": t.string(),
                "maxPosts": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsListByUser"] = blogger.get(
        "v3/blogs/{blogId}",
        t.struct(
            {
                "view": t.string(),
                "blogId": t.string(),
                "maxPosts": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsGet"] = blogger.get(
        "v3/blogs/{blogId}",
        t.struct(
            {
                "view": t.string(),
                "blogId": t.string(),
                "maxPosts": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postUserInfosList"] = blogger.get(
        "v3/users/{userId}/blogs/{blogId}/posts/{postId}",
        t.struct(
            {
                "blogId": t.string(),
                "postId": t.string(),
                "userId": t.string(),
                "maxComments": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostUserInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postUserInfosGet"] = blogger.get(
        "v3/users/{userId}/blogs/{blogId}/posts/{postId}",
        t.struct(
            {
                "blogId": t.string(),
                "postId": t.string(),
                "userId": t.string(),
                "maxComments": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostUserInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="blogger", renames=renames, types=Box(types), functions=Box(functions)
    )
