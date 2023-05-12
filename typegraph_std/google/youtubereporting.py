from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_youtubereporting() -> Import:
    youtubereporting = HTTPRuntime("https://youtubereporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubereporting_1_ErrorResponse",
        "EmptyIn": "_youtubereporting_2_EmptyIn",
        "EmptyOut": "_youtubereporting_3_EmptyOut",
        "GdataObjectIdIn": "_youtubereporting_4_GdataObjectIdIn",
        "GdataObjectIdOut": "_youtubereporting_5_GdataObjectIdOut",
        "GdataDiffUploadResponseIn": "_youtubereporting_6_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_youtubereporting_7_GdataDiffUploadResponseOut",
        "GdataDiffChecksumsResponseIn": "_youtubereporting_8_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_youtubereporting_9_GdataDiffChecksumsResponseOut",
        "GdataBlobstore2InfoIn": "_youtubereporting_10_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_youtubereporting_11_GdataBlobstore2InfoOut",
        "GdataDownloadParametersIn": "_youtubereporting_12_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_youtubereporting_13_GdataDownloadParametersOut",
        "ListJobsResponseIn": "_youtubereporting_14_ListJobsResponseIn",
        "ListJobsResponseOut": "_youtubereporting_15_ListJobsResponseOut",
        "ListReportTypesResponseIn": "_youtubereporting_16_ListReportTypesResponseIn",
        "ListReportTypesResponseOut": "_youtubereporting_17_ListReportTypesResponseOut",
        "GdataContentTypeInfoIn": "_youtubereporting_18_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_youtubereporting_19_GdataContentTypeInfoOut",
        "ReportIn": "_youtubereporting_20_ReportIn",
        "ReportOut": "_youtubereporting_21_ReportOut",
        "JobIn": "_youtubereporting_22_JobIn",
        "JobOut": "_youtubereporting_23_JobOut",
        "GdataDiffDownloadResponseIn": "_youtubereporting_24_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_youtubereporting_25_GdataDiffDownloadResponseOut",
        "GdataMediaIn": "_youtubereporting_26_GdataMediaIn",
        "GdataMediaOut": "_youtubereporting_27_GdataMediaOut",
        "ReportTypeIn": "_youtubereporting_28_ReportTypeIn",
        "ReportTypeOut": "_youtubereporting_29_ReportTypeOut",
        "GdataCompositeMediaIn": "_youtubereporting_30_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_youtubereporting_31_GdataCompositeMediaOut",
        "GdataDiffVersionResponseIn": "_youtubereporting_32_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_youtubereporting_33_GdataDiffVersionResponseOut",
        "ListReportsResponseIn": "_youtubereporting_34_ListReportsResponseIn",
        "ListReportsResponseOut": "_youtubereporting_35_ListReportsResponseOut",
        "GdataDiffUploadRequestIn": "_youtubereporting_36_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_youtubereporting_37_GdataDiffUploadRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GdataObjectIdIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["GdataObjectIdIn"])
    types["GdataObjectIdOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataObjectIdOut"])
    types["GdataDiffUploadResponseIn"] = t.struct(
        {
            "originalObject": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffUploadResponseIn"])
    types["GdataDiffUploadResponseOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadResponseOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
    types["GdataDownloadParametersIn"] = t.struct(
        {
            "allowGzipCompression": t.boolean().optional(),
            "ignoreRange": t.boolean().optional(),
        }
    ).named(renames["GdataDownloadParametersIn"])
    types["GdataDownloadParametersOut"] = t.struct(
        {
            "allowGzipCompression": t.boolean().optional(),
            "ignoreRange": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDownloadParametersOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["ListReportTypesResponseIn"] = t.struct(
        {
            "reportTypes": t.array(t.proxy(renames["ReportTypeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReportTypesResponseIn"])
    types["ListReportTypesResponseOut"] = t.struct(
        {
            "reportTypes": t.array(t.proxy(renames["ReportTypeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportTypesResponseOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromHeader": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
    types["ReportIn"] = t.struct(
        {
            "jobId": t.string().optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "startTime": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "jobId": t.string().optional(),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "startTime": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["JobIn"] = t.struct(
        {
            "id": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "id": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
    types["GdataMediaIn"] = t.struct(
        {
            "cosmoBinaryReference": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "length": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "blobRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "mediaId": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "token": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "path": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "timestamp": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "contentType": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "filename": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "bigstoreObjectRef": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "md5Hash": t.string().optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "cosmoBinaryReference": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "length": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "blobRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "mediaId": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "token": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "path": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "timestamp": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "contentType": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "filename": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "bigstoreObjectRef": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "md5Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
    types["ReportTypeIn"] = t.struct(
        {
            "id": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "deprecateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ReportTypeIn"])
    types["ReportTypeOut"] = t.struct(
        {
            "id": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "deprecateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportTypeOut"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
    types["GdataDiffVersionResponseIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectSizeBytes": t.string().optional(),
        }
    ).named(renames["GdataDiffVersionResponseIn"])
    types["GdataDiffVersionResponseOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffVersionResponseOut"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])
    types["GdataDiffUploadRequestIn"] = t.struct(
        {
            "objectInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestIn"])
    types["GdataDiffUploadRequestOut"] = t.struct(
        {
            "objectInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestOut"])

    functions = {}
    functions["jobsDelete"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsCreate"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsGet"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsList"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsReportsList"] = youtubereporting.get(
        "v1/jobs/{jobId}/reports/{reportId}",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "reportId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsReportsGet"] = youtubereporting.get(
        "v1/jobs/{jobId}/reports/{reportId}",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "reportId": t.string().optional(),
                "jobId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = youtubereporting.get(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GdataMediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["reportTypesList"] = youtubereporting.get(
        "v1/reportTypes",
        t.struct(
            {
                "includeSystemManaged": t.boolean().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubereporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
