from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_youtubereporting():
    youtubereporting = HTTPRuntime("https://youtubereporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubereporting_1_ErrorResponse",
        "ListReportsResponseIn": "_youtubereporting_2_ListReportsResponseIn",
        "ListReportsResponseOut": "_youtubereporting_3_ListReportsResponseOut",
        "ReportIn": "_youtubereporting_4_ReportIn",
        "ReportOut": "_youtubereporting_5_ReportOut",
        "JobIn": "_youtubereporting_6_JobIn",
        "JobOut": "_youtubereporting_7_JobOut",
        "GdataCompositeMediaIn": "_youtubereporting_8_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_youtubereporting_9_GdataCompositeMediaOut",
        "GdataDiffDownloadResponseIn": "_youtubereporting_10_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_youtubereporting_11_GdataDiffDownloadResponseOut",
        "GdataMediaIn": "_youtubereporting_12_GdataMediaIn",
        "GdataMediaOut": "_youtubereporting_13_GdataMediaOut",
        "GdataDiffChecksumsResponseIn": "_youtubereporting_14_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_youtubereporting_15_GdataDiffChecksumsResponseOut",
        "GdataBlobstore2InfoIn": "_youtubereporting_16_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_youtubereporting_17_GdataBlobstore2InfoOut",
        "ReportTypeIn": "_youtubereporting_18_ReportTypeIn",
        "ReportTypeOut": "_youtubereporting_19_ReportTypeOut",
        "ListJobsResponseIn": "_youtubereporting_20_ListJobsResponseIn",
        "ListJobsResponseOut": "_youtubereporting_21_ListJobsResponseOut",
        "GdataDiffVersionResponseIn": "_youtubereporting_22_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_youtubereporting_23_GdataDiffVersionResponseOut",
        "GdataObjectIdIn": "_youtubereporting_24_GdataObjectIdIn",
        "GdataObjectIdOut": "_youtubereporting_25_GdataObjectIdOut",
        "GdataDiffUploadResponseIn": "_youtubereporting_26_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_youtubereporting_27_GdataDiffUploadResponseOut",
        "GdataContentTypeInfoIn": "_youtubereporting_28_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_youtubereporting_29_GdataContentTypeInfoOut",
        "EmptyIn": "_youtubereporting_30_EmptyIn",
        "EmptyOut": "_youtubereporting_31_EmptyOut",
        "GdataDiffUploadRequestIn": "_youtubereporting_32_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_youtubereporting_33_GdataDiffUploadRequestOut",
        "ListReportTypesResponseIn": "_youtubereporting_34_ListReportTypesResponseIn",
        "ListReportTypesResponseOut": "_youtubereporting_35_ListReportTypesResponseOut",
        "GdataDownloadParametersIn": "_youtubereporting_36_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_youtubereporting_37_GdataDownloadParametersOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportIn"])).optional(),
        }
    ).named(renames["ListReportsResponseIn"])
    types["ListReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reports": t.array(t.proxy(renames["ReportOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportsResponseOut"])
    types["ReportIn"] = t.struct(
        {
            "id": t.string().optional(),
            "jobId": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "id": t.string().optional(),
            "jobId": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["JobIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "expireTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "expireTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "crc32cHash": t.integer().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "crc32cHash": t.integer().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
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
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "algorithm": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "length": t.string().optional(),
            "timestamp": t.string().optional(),
            "hash": t.string().optional(),
            "contentType": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "referenceType": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "token": t.string().optional(),
            "blobRef": t.string().optional(),
            "mediaId": t.string().optional(),
            "filename": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "algorithm": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "length": t.string().optional(),
            "timestamp": t.string().optional(),
            "hash": t.string().optional(),
            "contentType": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "referenceType": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "token": t.string().optional(),
            "blobRef": t.string().optional(),
            "mediaId": t.string().optional(),
            "filename": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
    types["ReportTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "deprecateTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ReportTypeIn"])
    types["ReportTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deprecateTime": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportTypeOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["GdataDiffVersionResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffVersionResponseIn"])
    types["GdataDiffVersionResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffVersionResponseOut"])
    types["GdataObjectIdIn"] = t.struct(
        {
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
        }
    ).named(renames["GdataObjectIdIn"])
    types["GdataObjectIdOut"] = t.struct(
        {
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataObjectIdOut"])
    types["GdataDiffUploadResponseIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "originalObject": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffUploadResponseIn"])
    types["GdataDiffUploadResponseOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "originalObject": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadResponseOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromHeader": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GdataDiffUploadRequestIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestIn"])
    types["GdataDiffUploadRequestOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestOut"])
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
    types["GdataDownloadParametersIn"] = t.struct(
        {
            "ignoreRange": t.boolean().optional(),
            "allowGzipCompression": t.boolean().optional(),
        }
    ).named(renames["GdataDownloadParametersIn"])
    types["GdataDownloadParametersOut"] = t.struct(
        {
            "ignoreRange": t.boolean().optional(),
            "allowGzipCompression": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDownloadParametersOut"])

    functions = {}
    functions["reportTypesList"] = youtubereporting.get(
        "v1/reportTypes",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportTypesResponseOut"]),
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
    functions["jobsCreate"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsDelete"] = youtubereporting.get(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
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
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
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
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
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
                "reportId": t.string().optional(),
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
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
                "reportId": t.string().optional(),
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubereporting",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
