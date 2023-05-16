from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_youtubereporting() -> Import:
    youtubereporting = HTTPRuntime("https://youtubereporting.googleapis.com/")

    renames = {
        "ErrorResponse": "_youtubereporting_1_ErrorResponse",
        "GdataCompositeMediaIn": "_youtubereporting_2_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_youtubereporting_3_GdataCompositeMediaOut",
        "ListReportsResponseIn": "_youtubereporting_4_ListReportsResponseIn",
        "ListReportsResponseOut": "_youtubereporting_5_ListReportsResponseOut",
        "EmptyIn": "_youtubereporting_6_EmptyIn",
        "EmptyOut": "_youtubereporting_7_EmptyOut",
        "ReportIn": "_youtubereporting_8_ReportIn",
        "ReportOut": "_youtubereporting_9_ReportOut",
        "GdataDownloadParametersIn": "_youtubereporting_10_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_youtubereporting_11_GdataDownloadParametersOut",
        "GdataContentTypeInfoIn": "_youtubereporting_12_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_youtubereporting_13_GdataContentTypeInfoOut",
        "GdataDiffUploadRequestIn": "_youtubereporting_14_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_youtubereporting_15_GdataDiffUploadRequestOut",
        "GdataDiffVersionResponseIn": "_youtubereporting_16_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_youtubereporting_17_GdataDiffVersionResponseOut",
        "ReportTypeIn": "_youtubereporting_18_ReportTypeIn",
        "ReportTypeOut": "_youtubereporting_19_ReportTypeOut",
        "GdataMediaIn": "_youtubereporting_20_GdataMediaIn",
        "GdataMediaOut": "_youtubereporting_21_GdataMediaOut",
        "GdataDiffUploadResponseIn": "_youtubereporting_22_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_youtubereporting_23_GdataDiffUploadResponseOut",
        "JobIn": "_youtubereporting_24_JobIn",
        "JobOut": "_youtubereporting_25_JobOut",
        "GdataDiffChecksumsResponseIn": "_youtubereporting_26_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_youtubereporting_27_GdataDiffChecksumsResponseOut",
        "GdataDiffDownloadResponseIn": "_youtubereporting_28_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_youtubereporting_29_GdataDiffDownloadResponseOut",
        "ListReportTypesResponseIn": "_youtubereporting_30_ListReportTypesResponseIn",
        "ListReportTypesResponseOut": "_youtubereporting_31_ListReportTypesResponseOut",
        "GdataObjectIdIn": "_youtubereporting_32_GdataObjectIdIn",
        "GdataObjectIdOut": "_youtubereporting_33_GdataObjectIdOut",
        "GdataBlobstore2InfoIn": "_youtubereporting_34_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_youtubereporting_35_GdataBlobstore2InfoOut",
        "ListJobsResponseIn": "_youtubereporting_36_ListJobsResponseIn",
        "ListJobsResponseOut": "_youtubereporting_37_ListJobsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "length": t.string().optional(),
            "referenceType": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "length": t.string().optional(),
            "referenceType": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ReportIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "jobId": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "id": t.string().optional(),
            "downloadUrl": t.string().optional(),
        }
    ).named(renames["ReportIn"])
    types["ReportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "jobId": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "jobExpireTime": t.string().optional(),
            "id": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportOut"])
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
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
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
    types["GdataMediaIn"] = t.struct(
        {
            "hashVerified": t.boolean().optional(),
            "md5Hash": t.string().optional(),
            "hash": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "sha256Hash": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "crc32cHash": t.integer().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "bigstoreObjectRef": t.string().optional(),
            "algorithm": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "filename": t.string().optional(),
            "blobRef": t.string().optional(),
            "contentType": t.string().optional(),
            "inline": t.string().optional(),
            "length": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "referenceType": t.string().optional(),
            "path": t.string().optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "token": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "hashVerified": t.boolean().optional(),
            "md5Hash": t.string().optional(),
            "hash": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "sha256Hash": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "crc32cHash": t.integer().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "bigstoreObjectRef": t.string().optional(),
            "algorithm": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "filename": t.string().optional(),
            "blobRef": t.string().optional(),
            "contentType": t.string().optional(),
            "inline": t.string().optional(),
            "length": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "referenceType": t.string().optional(),
            "path": t.string().optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "token": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
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
    types["JobIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "id": t.string().optional(),
            "reportTypeId": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "systemManaged": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "id": t.string().optional(),
            "reportTypeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
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
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
            "blobId": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
            "blobId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
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

    functions = {}
    functions["jobsDelete"] = youtubereporting.get(
        "v1/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsList"] = youtubereporting.get(
        "v1/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsCreate"] = youtubereporting.get(
        "v1/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["jobsGet"] = youtubereporting.get(
        "v1/jobs/{jobId}",
        t.struct(
            {
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
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
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "reportId": t.string().optional(),
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
                "jobId": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "reportId": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "onBehalfOfContentOwner": t.string().optional(),
                "pageSize": t.integer().optional(),
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
