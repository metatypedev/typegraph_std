from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_youtubereporting() -> Import:
    youtubereporting = HTTPRuntime("https://youtubereporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubereporting_1_ErrorResponse",
        "ListReportsResponseIn": "_youtubereporting_2_ListReportsResponseIn",
        "ListReportsResponseOut": "_youtubereporting_3_ListReportsResponseOut",
        "ReportTypeIn": "_youtubereporting_4_ReportTypeIn",
        "ReportTypeOut": "_youtubereporting_5_ReportTypeOut",
        "EmptyIn": "_youtubereporting_6_EmptyIn",
        "EmptyOut": "_youtubereporting_7_EmptyOut",
        "ListJobsResponseIn": "_youtubereporting_8_ListJobsResponseIn",
        "ListJobsResponseOut": "_youtubereporting_9_ListJobsResponseOut",
        "JobIn": "_youtubereporting_10_JobIn",
        "JobOut": "_youtubereporting_11_JobOut",
        "GdataCompositeMediaIn": "_youtubereporting_12_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_youtubereporting_13_GdataCompositeMediaOut",
        "GdataContentTypeInfoIn": "_youtubereporting_14_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_youtubereporting_15_GdataContentTypeInfoOut",
        "GdataDiffDownloadResponseIn": "_youtubereporting_16_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_youtubereporting_17_GdataDiffDownloadResponseOut",
        "GdataDiffChecksumsResponseIn": "_youtubereporting_18_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_youtubereporting_19_GdataDiffChecksumsResponseOut",
        "GdataDiffUploadRequestIn": "_youtubereporting_20_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_youtubereporting_21_GdataDiffUploadRequestOut",
        "GdataDiffUploadResponseIn": "_youtubereporting_22_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_youtubereporting_23_GdataDiffUploadResponseOut",
        "GdataObjectIdIn": "_youtubereporting_24_GdataObjectIdIn",
        "GdataObjectIdOut": "_youtubereporting_25_GdataObjectIdOut",
        "ListReportTypesResponseIn": "_youtubereporting_26_ListReportTypesResponseIn",
        "ListReportTypesResponseOut": "_youtubereporting_27_ListReportTypesResponseOut",
        "ReportIn": "_youtubereporting_28_ReportIn",
        "ReportOut": "_youtubereporting_29_ReportOut",
        "GdataMediaIn": "_youtubereporting_30_GdataMediaIn",
        "GdataMediaOut": "_youtubereporting_31_GdataMediaOut",
        "GdataDownloadParametersIn": "_youtubereporting_32_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_youtubereporting_33_GdataDownloadParametersOut",
        "GdataDiffVersionResponseIn": "_youtubereporting_34_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_youtubereporting_35_GdataDiffVersionResponseOut",
        "GdataBlobstore2InfoIn": "_youtubereporting_36_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_youtubereporting_37_GdataBlobstore2InfoOut",
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
    types["ReportTypeIn"] = t.struct(
        {
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
            "deprecateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ReportTypeIn"])
    types["ReportTypeOut"] = t.struct(
        {
            "systemManaged": t.boolean().optional(),
            "id": t.string().optional(),
            "deprecateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportTypeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["JobIn"] = t.struct(
        {
            "id": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "createTime": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "id": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "createTime": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "blobRef": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "blobRef": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromUrlPath": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GdataDiffUploadRequestIn"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffUploadRequestIn"])
    types["GdataDiffUploadRequestOut"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestOut"])
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
    types["ListReportTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reportTypes": t.array(t.proxy(renames["ReportTypeIn"])).optional(),
        }
    ).named(renames["ListReportTypesResponseIn"])
    types["ListReportTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reportTypes": t.array(t.proxy(renames["ReportTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReportTypesResponseOut"])
    types["ReportIn"] = t.struct(
        {
            "id": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "startTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "endTime": t.string().optional(),
            "jobId": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "id": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "startTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "endTime": t.string().optional(),
            "jobId": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
    types["GdataMediaIn"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "blobRef": t.string().optional(),
            "length": t.string().optional(),
            "hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "contentType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "referenceType": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "filename": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "token": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "md5Hash": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "algorithm": t.string().optional(),
            "path": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "sha1Hash": t.string().optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "blobRef": t.string().optional(),
            "length": t.string().optional(),
            "hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "contentType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "referenceType": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "filename": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "token": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "md5Hash": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "algorithm": t.string().optional(),
            "path": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
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

    functions = {}
    functions["jobsGet"] = youtubereporting.post(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "systemManaged": t.boolean().optional(),
                "createTime": t.string().optional(),
                "reportTypeId": t.string().optional(),
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsList"] = youtubereporting.post(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "systemManaged": t.boolean().optional(),
                "createTime": t.string().optional(),
                "reportTypeId": t.string().optional(),
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsDelete"] = youtubereporting.post(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "systemManaged": t.boolean().optional(),
                "createTime": t.string().optional(),
                "reportTypeId": t.string().optional(),
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsCreate"] = youtubereporting.post(
        "v1/jobs",
        t.struct(
            {
                "onBehalfOfContentOwner": t.string().optional(),
                "id": t.string().optional(),
                "systemManaged": t.boolean().optional(),
                "createTime": t.string().optional(),
                "reportTypeId": t.string().optional(),
                "name": t.string().optional(),
                "expireTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "includeSystemManaged": t.boolean().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReportTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="youtubereporting", renames=renames, types=types, functions=functions
    )
