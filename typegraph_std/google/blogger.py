from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_blogger():
    blogger = HTTPRuntime("https://blogger.googleapis.com/")

    renames = {
        "ErrorResponse": "_blogger_1_ErrorResponse",
        "BlogIn": "_blogger_2_BlogIn",
        "BlogOut": "_blogger_3_BlogOut",
        "UserIn": "_blogger_4_UserIn",
        "UserOut": "_blogger_5_UserOut",
        "BlogListIn": "_blogger_6_BlogListIn",
        "BlogListOut": "_blogger_7_BlogListOut",
        "CommentListIn": "_blogger_8_CommentListIn",
        "CommentListOut": "_blogger_9_CommentListOut",
        "BlogPerUserInfoIn": "_blogger_10_BlogPerUserInfoIn",
        "BlogPerUserInfoOut": "_blogger_11_BlogPerUserInfoOut",
        "PageviewsIn": "_blogger_12_PageviewsIn",
        "PageviewsOut": "_blogger_13_PageviewsOut",
        "PostUserInfoIn": "_blogger_14_PostUserInfoIn",
        "PostUserInfoOut": "_blogger_15_PostUserInfoOut",
        "PostIn": "_blogger_16_PostIn",
        "PostOut": "_blogger_17_PostOut",
        "BlogUserInfoIn": "_blogger_18_BlogUserInfoIn",
        "BlogUserInfoOut": "_blogger_19_BlogUserInfoOut",
        "PostListIn": "_blogger_20_PostListIn",
        "PostListOut": "_blogger_21_PostListOut",
        "CommentIn": "_blogger_22_CommentIn",
        "CommentOut": "_blogger_23_CommentOut",
        "PostUserInfosListIn": "_blogger_24_PostUserInfosListIn",
        "PostUserInfosListOut": "_blogger_25_PostUserInfosListOut",
        "PostPerUserInfoIn": "_blogger_26_PostPerUserInfoIn",
        "PostPerUserInfoOut": "_blogger_27_PostPerUserInfoOut",
        "PageListIn": "_blogger_28_PageListIn",
        "PageListOut": "_blogger_29_PageListOut",
        "PageIn": "_blogger_30_PageIn",
        "PageOut": "_blogger_31_PageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BlogIn"] = t.struct(
        {
            "pages": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "locale": t.struct(
                {
                    "country": t.string().optional(),
                    "variant": t.string().optional(),
                    "language": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "posts": t.struct(
                {
                    "totalItems": t.integer().optional(),
                    "items": t.array(t.proxy(renames["PostIn"])).optional(),
                    "selfLink": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "customMetaData": t.string().optional(),
            "description": t.string().optional(),
            "url": t.string().optional(),
            "published": t.string().optional(),
        }
    ).named(renames["BlogIn"])
    types["BlogOut"] = t.struct(
        {
            "pages": t.struct(
                {
                    "selfLink": t.string().optional(),
                    "totalItems": t.integer().optional(),
                }
            ).optional(),
            "locale": t.struct(
                {
                    "country": t.string().optional(),
                    "variant": t.string().optional(),
                    "language": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "name": t.string().optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "id": t.string().optional(),
            "posts": t.struct(
                {
                    "totalItems": t.integer().optional(),
                    "items": t.array(t.proxy(renames["PostOut"])).optional(),
                    "selfLink": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "customMetaData": t.string().optional(),
            "description": t.string().optional(),
            "url": t.string().optional(),
            "published": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogOut"])
    types["UserIn"] = t.struct(
        {
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "created": t.string().optional(),
            "blogs": t.struct({"selfLink": t.string().optional()}).optional(),
            "url": t.string().optional(),
            "about": t.string().optional(),
            "locale": t.struct(
                {
                    "language": t.string().optional(),
                    "country": t.string().optional(),
                    "variant": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "created": t.string().optional(),
            "blogs": t.struct({"selfLink": t.string().optional()}).optional(),
            "url": t.string().optional(),
            "about": t.string().optional(),
            "locale": t.struct(
                {
                    "language": t.string().optional(),
                    "country": t.string().optional(),
                    "variant": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["BlogListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BlogIn"])).optional(),
            "kind": t.string().optional(),
            "blogUserInfos": t.array(t.proxy(renames["BlogUserInfoIn"])).optional(),
        }
    ).named(renames["BlogListIn"])
    types["BlogListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BlogOut"])).optional(),
            "kind": t.string().optional(),
            "blogUserInfos": t.array(t.proxy(renames["BlogUserInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogListOut"])
    types["CommentListIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CommentListIn"])
    types["CommentListOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "prevPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CommentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentListOut"])
    types["BlogPerUserInfoIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "role": t.string().optional(),
            "photosAlbumKey": t.string().optional(),
            "userId": t.string().optional(),
            "hasAdminAccess": t.boolean().optional(),
        }
    ).named(renames["BlogPerUserInfoIn"])
    types["BlogPerUserInfoOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "blogId": t.string().optional(),
            "role": t.string().optional(),
            "photosAlbumKey": t.string().optional(),
            "userId": t.string().optional(),
            "hasAdminAccess": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogPerUserInfoOut"])
    types["PageviewsIn"] = t.struct(
        {
            "counts": t.array(
                t.struct(
                    {"count": t.string().optional(), "timeRange": t.string().optional()}
                )
            ).optional(),
            "blogId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PageviewsIn"])
    types["PageviewsOut"] = t.struct(
        {
            "counts": t.array(
                t.struct(
                    {"count": t.string().optional(), "timeRange": t.string().optional()}
                )
            ).optional(),
            "blogId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageviewsOut"])
    types["PostUserInfoIn"] = t.struct(
        {
            "post": t.proxy(renames["PostIn"]).optional(),
            "kind": t.string().optional(),
            "post_user_info": t.proxy(renames["PostPerUserInfoIn"]).optional(),
        }
    ).named(renames["PostUserInfoIn"])
    types["PostUserInfoOut"] = t.struct(
        {
            "post": t.proxy(renames["PostOut"]).optional(),
            "kind": t.string().optional(),
            "post_user_info": t.proxy(renames["PostPerUserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostUserInfoOut"])
    types["PostIn"] = t.struct(
        {
            "trashed": t.string().optional(),
            "location": t.struct(
                {
                    "span": t.string().optional(),
                    "lat": t.number().optional(),
                    "name": t.string().optional(),
                    "lng": t.number().optional(),
                }
            ).optional(),
            "readerComments": t.string().optional(),
            "published": t.string().optional(),
            "etag": t.string().optional(),
            "titleLink": t.string().optional(),
            "updated": t.string().optional(),
            "url": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "content": t.string().optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "replies": t.struct(
                {
                    "items": t.array(t.proxy(renames["CommentIn"])).optional(),
                    "selfLink": t.string().optional(),
                    "totalItems": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "customMetaData": t.string().optional(),
            "selfLink": t.string().optional(),
            "author": t.struct(
                {
                    "displayName": t.string().optional(),
                    "url": t.string().optional(),
                    "id": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
            "images": t.array(t.struct({"url": t.string()})).optional(),
        }
    ).named(renames["PostIn"])
    types["PostOut"] = t.struct(
        {
            "trashed": t.string().optional(),
            "location": t.struct(
                {
                    "span": t.string().optional(),
                    "lat": t.number().optional(),
                    "name": t.string().optional(),
                    "lng": t.number().optional(),
                }
            ).optional(),
            "readerComments": t.string().optional(),
            "published": t.string().optional(),
            "etag": t.string().optional(),
            "titleLink": t.string().optional(),
            "updated": t.string().optional(),
            "url": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "content": t.string().optional(),
            "title": t.string().optional(),
            "kind": t.string().optional(),
            "status": t.string().optional(),
            "labels": t.array(t.string()).optional(),
            "replies": t.struct(
                {
                    "items": t.array(t.proxy(renames["CommentOut"])).optional(),
                    "selfLink": t.string().optional(),
                    "totalItems": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "customMetaData": t.string().optional(),
            "selfLink": t.string().optional(),
            "author": t.struct(
                {
                    "displayName": t.string().optional(),
                    "url": t.string().optional(),
                    "id": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
            "images": t.array(t.struct({"url": t.string()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostOut"])
    types["BlogUserInfoIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "blog": t.proxy(renames["BlogIn"]).optional(),
            "blog_user_info": t.proxy(renames["BlogPerUserInfoIn"]).optional(),
        }
    ).named(renames["BlogUserInfoIn"])
    types["BlogUserInfoOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "blog": t.proxy(renames["BlogOut"]).optional(),
            "blog_user_info": t.proxy(renames["BlogPerUserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlogUserInfoOut"])
    types["PostListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PostIn"])).optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PostListIn"])
    types["PostListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["PostOut"])).optional(),
            "prevPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostListOut"])
    types["CommentIn"] = t.struct(
        {
            "post": t.struct({"id": t.string().optional()}).optional(),
            "inReplyTo": t.struct({"id": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "content": t.string().optional(),
            "published": t.string().optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "author": t.struct(
                {
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "displayName": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
        }
    ).named(renames["CommentIn"])
    types["CommentOut"] = t.struct(
        {
            "post": t.struct({"id": t.string().optional()}).optional(),
            "inReplyTo": t.struct({"id": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "content": t.string().optional(),
            "published": t.string().optional(),
            "updated": t.string().optional(),
            "status": t.string().optional(),
            "author": t.struct(
                {
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "displayName": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["PostUserInfosListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostUserInfoIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["PostUserInfosListIn"])
    types["PostUserInfosListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PostUserInfoOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostUserInfosListOut"])
    types["PostPerUserInfoIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "kind": t.string().optional(),
            "hasEditAccess": t.boolean().optional(),
            "blogId": t.string().optional(),
            "postId": t.string().optional(),
        }
    ).named(renames["PostPerUserInfoIn"])
    types["PostPerUserInfoOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "kind": t.string().optional(),
            "hasEditAccess": t.boolean().optional(),
            "blogId": t.string().optional(),
            "postId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostPerUserInfoOut"])
    types["PageListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PageIn"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["PageListIn"])
    types["PageListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["PageOut"])).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageListOut"])
    types["PageIn"] = t.struct(
        {
            "status": t.string().optional(),
            "author": t.struct(
                {
                    "displayName": t.string().optional(),
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "title": t.string().optional(),
            "selfLink": t.string().optional(),
            "content": t.string().optional(),
            "trashed": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "published": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "status": t.string().optional(),
            "author": t.struct(
                {
                    "displayName": t.string().optional(),
                    "id": t.string().optional(),
                    "url": t.string().optional(),
                    "image": t.struct({"url": t.string().optional()}).optional(),
                }
            ).optional(),
            "blog": t.struct({"id": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "title": t.string().optional(),
            "selfLink": t.string().optional(),
            "content": t.string().optional(),
            "trashed": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "published": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])

    functions = {}
    functions["blogUserInfosGet"] = blogger.get(
        "v3/users/{userId}/blogs/{blogId}",
        t.struct(
            {
                "userId": t.string(),
                "blogId": t.string(),
                "maxPosts": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BlogUserInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postUserInfosList"] = blogger.get(
        "v3/users/{userId}/blogs/{blogId}/posts/{postId}",
        t.struct(
            {
                "postId": t.string(),
                "userId": t.string(),
                "blogId": t.string(),
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
                "postId": t.string(),
                "userId": t.string(),
                "blogId": t.string(),
                "maxComments": t.integer(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostUserInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsUpdate"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsSearch"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsGet"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsList"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsDelete"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsGetByPath"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsInsert"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsPatch"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsRevert"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["postsPublish"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/publish",
        t.struct(
            {
                "postId": t.string(),
                "blogId": t.string(),
                "publishDate": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PostOut"]),
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
    functions["commentsApprove"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsDelete"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsGet"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsList"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsRemoveContent"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsListByBlog"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["commentsMarkAsSpam"] = blogger.post(
        "v3/blogs/{blogId}/posts/{postId}/comments/{commentId}/spam",
        t.struct(
            {
                "postId": t.string(),
                "commentId": t.string(),
                "blogId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsGet"] = blogger.get(
        "v3/blogs/byurl",
        t.struct(
            {"view": t.string(), "url": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsListByUser"] = blogger.get(
        "v3/blogs/byurl",
        t.struct(
            {"view": t.string(), "url": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["blogsGetByUrl"] = blogger.get(
        "v3/blogs/byurl",
        t.struct(
            {"view": t.string(), "url": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["BlogOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesPatch"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesDelete"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesRevert"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesGet"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesPublish"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesList"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesInsert"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["pagesUpdate"] = blogger.put(
        "v3/blogs/{blogId}/pages/{pageId}",
        t.struct(
            {
                "revert": t.boolean(),
                "pageId": t.string(),
                "blogId": t.string(),
                "publish": t.boolean(),
                "status": t.string().optional(),
                "author": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "image": t.struct({"url": t.string().optional()}).optional(),
                    }
                ).optional(),
                "blog": t.struct({"id": t.string().optional()}).optional(),
                "updated": t.string().optional(),
                "title": t.string().optional(),
                "selfLink": t.string().optional(),
                "content": t.string().optional(),
                "trashed": t.string().optional(),
                "etag": t.string().optional(),
                "kind": t.string().optional(),
                "id": t.string().optional(),
                "published": t.string().optional(),
                "url": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="blogger", renames=renames, types=Box(types), functions=Box(functions)
    )
