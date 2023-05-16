from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListCasesResponseIn: t.typedef = ...
    ListCasesResponseOut: t.typedef = ...
    ActorIn: t.typedef = ...
    ActorOut: t.typedef = ...
    DiffUploadResponseIn: t.typedef = ...
    DiffUploadResponseOut: t.typedef = ...
    ObjectIdIn: t.typedef = ...
    ObjectIdOut: t.typedef = ...
    EscalateCaseRequestIn: t.typedef = ...
    EscalateCaseRequestOut: t.typedef = ...
    CompositeMediaIn: t.typedef = ...
    CompositeMediaOut: t.typedef = ...
    AttachmentIn: t.typedef = ...
    AttachmentOut: t.typedef = ...
    DiffVersionResponseIn: t.typedef = ...
    DiffVersionResponseOut: t.typedef = ...
    DiffDownloadResponseIn: t.typedef = ...
    DiffDownloadResponseOut: t.typedef = ...
    SearchCaseClassificationsResponseIn: t.typedef = ...
    SearchCaseClassificationsResponseOut: t.typedef = ...
    WorkflowOperationMetadataIn: t.typedef = ...
    WorkflowOperationMetadataOut: t.typedef = ...
    CaseClassificationIn: t.typedef = ...
    CaseClassificationOut: t.typedef = ...
    EscalationIn: t.typedef = ...
    EscalationOut: t.typedef = ...
    ListCommentsResponseIn: t.typedef = ...
    ListCommentsResponseOut: t.typedef = ...
    CreateAttachmentRequestIn: t.typedef = ...
    CreateAttachmentRequestOut: t.typedef = ...
    CloseCaseRequestIn: t.typedef = ...
    CloseCaseRequestOut: t.typedef = ...
    Blobstore2InfoIn: t.typedef = ...
    Blobstore2InfoOut: t.typedef = ...
    ListAttachmentsResponseIn: t.typedef = ...
    ListAttachmentsResponseOut: t.typedef = ...
    CommentIn: t.typedef = ...
    CommentOut: t.typedef = ...
    CaseIn: t.typedef = ...
    CaseOut: t.typedef = ...
    DownloadParametersIn: t.typedef = ...
    DownloadParametersOut: t.typedef = ...
    MediaIn: t.typedef = ...
    MediaOut: t.typedef = ...
    DiffChecksumsResponseIn: t.typedef = ...
    DiffChecksumsResponseOut: t.typedef = ...
    SearchCasesResponseIn: t.typedef = ...
    SearchCasesResponseOut: t.typedef = ...
    ContentTypeInfoIn: t.typedef = ...
    ContentTypeInfoOut: t.typedef = ...
    DiffUploadRequestIn: t.typedef = ...
    DiffUploadRequestOut: t.typedef = ...

class FuncList:
    casesList: t.func = ...
    casesCreate: t.func = ...
    casesClose: t.func = ...
    casesPatch: t.func = ...
    casesGet: t.func = ...
    casesEscalate: t.func = ...
    casesSearch: t.func = ...
    casesAttachmentsList: t.func = ...
    casesCommentsCreate: t.func = ...
    casesCommentsList: t.func = ...
    caseClassificationsSearch: t.func = ...
    mediaDownload: t.func = ...
    mediaUpload: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudsupport() -> Import: ...
