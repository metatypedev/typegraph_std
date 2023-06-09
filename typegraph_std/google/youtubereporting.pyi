from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListReportsResponseIn: t.typedef = ...
    ListReportsResponseOut: t.typedef = ...
    ReportIn: t.typedef = ...
    ReportOut: t.typedef = ...
    JobIn: t.typedef = ...
    JobOut: t.typedef = ...
    GdataCompositeMediaIn: t.typedef = ...
    GdataCompositeMediaOut: t.typedef = ...
    GdataDiffDownloadResponseIn: t.typedef = ...
    GdataDiffDownloadResponseOut: t.typedef = ...
    GdataMediaIn: t.typedef = ...
    GdataMediaOut: t.typedef = ...
    GdataDiffChecksumsResponseIn: t.typedef = ...
    GdataDiffChecksumsResponseOut: t.typedef = ...
    GdataBlobstore2InfoIn: t.typedef = ...
    GdataBlobstore2InfoOut: t.typedef = ...
    ReportTypeIn: t.typedef = ...
    ReportTypeOut: t.typedef = ...
    ListJobsResponseIn: t.typedef = ...
    ListJobsResponseOut: t.typedef = ...
    GdataDiffVersionResponseIn: t.typedef = ...
    GdataDiffVersionResponseOut: t.typedef = ...
    GdataObjectIdIn: t.typedef = ...
    GdataObjectIdOut: t.typedef = ...
    GdataDiffUploadResponseIn: t.typedef = ...
    GdataDiffUploadResponseOut: t.typedef = ...
    GdataContentTypeInfoIn: t.typedef = ...
    GdataContentTypeInfoOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    GdataDiffUploadRequestIn: t.typedef = ...
    GdataDiffUploadRequestOut: t.typedef = ...
    ListReportTypesResponseIn: t.typedef = ...
    ListReportTypesResponseOut: t.typedef = ...
    GdataDownloadParametersIn: t.typedef = ...
    GdataDownloadParametersOut: t.typedef = ...

class FuncList:
    reportTypesList: t.func = ...
    mediaDownload: t.func = ...
    jobsCreate: t.func = ...
    jobsDelete: t.func = ...
    jobsGet: t.func = ...
    jobsList: t.func = ...
    jobsReportsList: t.func = ...
    jobsReportsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_youtubereporting() -> Import: ...
