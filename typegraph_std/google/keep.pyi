from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    BatchDeletePermissionsRequestIn: t.typedef = ...
    BatchDeletePermissionsRequestOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    BatchCreatePermissionsResponseIn: t.typedef = ...
    BatchCreatePermissionsResponseOut: t.typedef = ...
    GroupIn: t.typedef = ...
    GroupOut: t.typedef = ...
    PermissionIn: t.typedef = ...
    PermissionOut: t.typedef = ...
    UserIn: t.typedef = ...
    UserOut: t.typedef = ...
    FamilyIn: t.typedef = ...
    FamilyOut: t.typedef = ...
    ListNotesResponseIn: t.typedef = ...
    ListNotesResponseOut: t.typedef = ...
    CreatePermissionRequestIn: t.typedef = ...
    CreatePermissionRequestOut: t.typedef = ...
    AttachmentIn: t.typedef = ...
    AttachmentOut: t.typedef = ...
    ListContentIn: t.typedef = ...
    ListContentOut: t.typedef = ...
    ListItemIn: t.typedef = ...
    ListItemOut: t.typedef = ...
    SectionIn: t.typedef = ...
    SectionOut: t.typedef = ...
    TextContentIn: t.typedef = ...
    TextContentOut: t.typedef = ...
    BatchCreatePermissionsRequestIn: t.typedef = ...
    BatchCreatePermissionsRequestOut: t.typedef = ...
    NoteIn: t.typedef = ...
    NoteOut: t.typedef = ...

class FuncList:
    mediaDownload: t.func = ...
    notesList: t.func = ...
    notesCreate: t.func = ...
    notesDelete: t.func = ...
    notesGet: t.func = ...
    notesPermissionsBatchDelete: t.func = ...
    notesPermissionsBatchCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_keep() -> Import: ...
