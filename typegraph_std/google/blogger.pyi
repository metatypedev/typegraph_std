from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    PageListIn: t.typedef = ...
    PageListOut: t.typedef = ...
    PostUserInfosListIn: t.typedef = ...
    PostUserInfosListOut: t.typedef = ...
    BlogListIn: t.typedef = ...
    BlogListOut: t.typedef = ...
    PostListIn: t.typedef = ...
    PostListOut: t.typedef = ...
    PageviewsIn: t.typedef = ...
    PageviewsOut: t.typedef = ...
    CommentIn: t.typedef = ...
    CommentOut: t.typedef = ...
    BlogPerUserInfoIn: t.typedef = ...
    BlogPerUserInfoOut: t.typedef = ...
    PageIn: t.typedef = ...
    PageOut: t.typedef = ...
    BlogUserInfoIn: t.typedef = ...
    BlogUserInfoOut: t.typedef = ...
    UserIn: t.typedef = ...
    UserOut: t.typedef = ...
    PostPerUserInfoIn: t.typedef = ...
    PostPerUserInfoOut: t.typedef = ...
    PostUserInfoIn: t.typedef = ...
    PostUserInfoOut: t.typedef = ...
    CommentListIn: t.typedef = ...
    CommentListOut: t.typedef = ...
    BlogIn: t.typedef = ...
    BlogOut: t.typedef = ...
    PostIn: t.typedef = ...
    PostOut: t.typedef = ...

class FuncList:
    postsUpdate: t.func = ...
    postsPatch: t.func = ...
    postsRevert: t.func = ...
    postsGetByPath: t.func = ...
    postsDelete: t.func = ...
    postsList: t.func = ...
    postsPublish: t.func = ...
    postsGet: t.func = ...
    postsInsert: t.func = ...
    postsSearch: t.func = ...
    pagesInsert: t.func = ...
    pagesRevert: t.func = ...
    pagesGet: t.func = ...
    pagesPublish: t.func = ...
    pagesPatch: t.func = ...
    pagesDelete: t.func = ...
    pagesUpdate: t.func = ...
    pagesList: t.func = ...
    commentsRemoveContent: t.func = ...
    commentsListByBlog: t.func = ...
    commentsApprove: t.func = ...
    commentsMarkAsSpam: t.func = ...
    commentsList: t.func = ...
    commentsGet: t.func = ...
    commentsDelete: t.func = ...
    blogUserInfosGet: t.func = ...
    usersGet: t.func = ...
    pageViewsGet: t.func = ...
    blogsGetByUrl: t.func = ...
    blogsListByUser: t.func = ...
    blogsGet: t.func = ...
    postUserInfosList: t.func = ...
    postUserInfosGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_blogger() -> Import: ...
