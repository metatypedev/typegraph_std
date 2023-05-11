from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudsupport() -> Import:
    cloudsupport = HTTPRuntime("https://cloudsupport.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsupport_1_ErrorResponse",
        "CreateAttachmentRequestIn": "_cloudsupport_2_CreateAttachmentRequestIn",
        "CreateAttachmentRequestOut": "_cloudsupport_3_CreateAttachmentRequestOut",
        "ListAttachmentsResponseIn": "_cloudsupport_4_ListAttachmentsResponseIn",
        "ListAttachmentsResponseOut": "_cloudsupport_5_ListAttachmentsResponseOut",
        "MediaIn": "_cloudsupport_6_MediaIn",
        "MediaOut": "_cloudsupport_7_MediaOut",
        "CommentIn": "_cloudsupport_8_CommentIn",
        "CommentOut": "_cloudsupport_9_CommentOut",
        "Blobstore2InfoIn": "_cloudsupport_10_Blobstore2InfoIn",
        "Blobstore2InfoOut": "_cloudsupport_11_Blobstore2InfoOut",
        "ObjectIdIn": "_cloudsupport_12_ObjectIdIn",
        "ObjectIdOut": "_cloudsupport_13_ObjectIdOut",
        "CaseClassificationIn": "_cloudsupport_14_CaseClassificationIn",
        "CaseClassificationOut": "_cloudsupport_15_CaseClassificationOut",
        "DiffChecksumsResponseIn": "_cloudsupport_16_DiffChecksumsResponseIn",
        "DiffChecksumsResponseOut": "_cloudsupport_17_DiffChecksumsResponseOut",
        "DiffVersionResponseIn": "_cloudsupport_18_DiffVersionResponseIn",
        "DiffVersionResponseOut": "_cloudsupport_19_DiffVersionResponseOut",
        "DiffUploadResponseIn": "_cloudsupport_20_DiffUploadResponseIn",
        "DiffUploadResponseOut": "_cloudsupport_21_DiffUploadResponseOut",
        "SearchCasesResponseIn": "_cloudsupport_22_SearchCasesResponseIn",
        "SearchCasesResponseOut": "_cloudsupport_23_SearchCasesResponseOut",
        "ActorIn": "_cloudsupport_24_ActorIn",
        "ActorOut": "_cloudsupport_25_ActorOut",
        "ListCommentsResponseIn": "_cloudsupport_26_ListCommentsResponseIn",
        "ListCommentsResponseOut": "_cloudsupport_27_ListCommentsResponseOut",
        "ListCasesResponseIn": "_cloudsupport_28_ListCasesResponseIn",
        "ListCasesResponseOut": "_cloudsupport_29_ListCasesResponseOut",
        "CloseCaseRequestIn": "_cloudsupport_30_CloseCaseRequestIn",
        "CloseCaseRequestOut": "_cloudsupport_31_CloseCaseRequestOut",
        "CompositeMediaIn": "_cloudsupport_32_CompositeMediaIn",
        "CompositeMediaOut": "_cloudsupport_33_CompositeMediaOut",
        "ContentTypeInfoIn": "_cloudsupport_34_ContentTypeInfoIn",
        "ContentTypeInfoOut": "_cloudsupport_35_ContentTypeInfoOut",
        "EscalationIn": "_cloudsupport_36_EscalationIn",
        "EscalationOut": "_cloudsupport_37_EscalationOut",
        "WorkflowOperationMetadataIn": "_cloudsupport_38_WorkflowOperationMetadataIn",
        "WorkflowOperationMetadataOut": "_cloudsupport_39_WorkflowOperationMetadataOut",
        "AttachmentIn": "_cloudsupport_40_AttachmentIn",
        "AttachmentOut": "_cloudsupport_41_AttachmentOut",
        "DiffUploadRequestIn": "_cloudsupport_42_DiffUploadRequestIn",
        "DiffUploadRequestOut": "_cloudsupport_43_DiffUploadRequestOut",
        "DownloadParametersIn": "_cloudsupport_44_DownloadParametersIn",
        "DownloadParametersOut": "_cloudsupport_45_DownloadParametersOut",
        "SearchCaseClassificationsResponseIn": "_cloudsupport_46_SearchCaseClassificationsResponseIn",
        "SearchCaseClassificationsResponseOut": "_cloudsupport_47_SearchCaseClassificationsResponseOut",
        "CaseIn": "_cloudsupport_48_CaseIn",
        "CaseOut": "_cloudsupport_49_CaseOut",
        "EscalateCaseRequestIn": "_cloudsupport_50_EscalateCaseRequestIn",
        "EscalateCaseRequestOut": "_cloudsupport_51_EscalateCaseRequestOut",
        "DiffDownloadResponseIn": "_cloudsupport_52_DiffDownloadResponseIn",
        "DiffDownloadResponseOut": "_cloudsupport_53_DiffDownloadResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CreateAttachmentRequestIn"] = t.struct(
        {"attachment": t.proxy(renames["AttachmentIn"])}
    ).named(renames["CreateAttachmentRequestIn"])
    types["CreateAttachmentRequestOut"] = t.struct(
        {
            "attachment": t.proxy(renames["AttachmentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAttachmentRequestOut"])
    types["ListAttachmentsResponseIn"] = t.struct(
        {
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAttachmentsResponseIn"])
    types["ListAttachmentsResponseOut"] = t.struct(
        {
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttachmentsResponseOut"])
    types["MediaIn"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaIn"])).optional(),
            "inline": t.string().optional(),
            "path": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseIn"]
            ).optional(),
            "referenceType": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "hash": t.string().optional(),
            "contentType": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "filename": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoIn"]).optional(),
            "diffVersionResponse": t.proxy(renames["DiffVersionResponseIn"]).optional(),
            "token": t.string().optional(),
            "blobRef": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseIn"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseIn"]
            ).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "length": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestIn"]).optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersIn"]).optional(),
            "algorithm": t.string().optional(),
        }
    ).named(renames["MediaIn"])
    types["MediaOut"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaOut"])).optional(),
            "inline": t.string().optional(),
            "path": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseOut"]
            ).optional(),
            "referenceType": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "hash": t.string().optional(),
            "contentType": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "filename": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoOut"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["DiffVersionResponseOut"]
            ).optional(),
            "token": t.string().optional(),
            "blobRef": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseOut"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseOut"]
            ).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "length": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestOut"]).optional(),
            "mediaId": t.string().optional(),
            "timestamp": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersOut"]).optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["CommentIn"] = t.struct({"body": t.string().optional()}).named(
        renames["CommentIn"]
    )
    types["CommentOut"] = t.struct(
        {
            "plainTextBody": t.string().optional(),
            "createTime": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "body": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["Blobstore2InfoIn"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
        }
    ).named(renames["Blobstore2InfoIn"])
    types["Blobstore2InfoOut"] = t.struct(
        {
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Blobstore2InfoOut"])
    types["ObjectIdIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
        }
    ).named(renames["ObjectIdIn"])
    types["ObjectIdOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["CaseClassificationIn"] = t.struct(
        {"displayName": t.string().optional(), "id": t.string().optional()}
    ).named(renames["CaseClassificationIn"])
    types["CaseClassificationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseClassificationOut"])
    types["DiffChecksumsResponseIn"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
        }
    ).named(renames["DiffChecksumsResponseIn"])
    types["DiffChecksumsResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffChecksumsResponseOut"])
    types["DiffVersionResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["DiffVersionResponseIn"])
    types["DiffVersionResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffVersionResponseOut"])
    types["DiffUploadResponseIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "originalObject": t.proxy(renames["CompositeMediaIn"]).optional(),
        }
    ).named(renames["DiffUploadResponseIn"])
    types["DiffUploadResponseOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "originalObject": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadResponseOut"])
    types["SearchCasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cases": t.array(t.proxy(renames["CaseIn"])).optional(),
        }
    ).named(renames["SearchCasesResponseIn"])
    types["SearchCasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cases": t.array(t.proxy(renames["CaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchCasesResponseOut"])
    types["ActorIn"] = t.struct(
        {"displayName": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "googleSupport": t.boolean().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])
    types["ListCommentsResponseIn"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCommentsResponseIn"])
    types["ListCommentsResponseOut"] = t.struct(
        {
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCommentsResponseOut"])
    types["ListCasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cases": t.array(t.proxy(renames["CaseIn"])).optional(),
        }
    ).named(renames["ListCasesResponseIn"])
    types["ListCasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cases": t.array(t.proxy(renames["CaseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCasesResponseOut"])
    types["CloseCaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseCaseRequestIn"]
    )
    types["CloseCaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseCaseRequestOut"])
    types["CompositeMediaIn"] = t.struct(
        {
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "blobRef": t.string().optional(),
            "length": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "path": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "referenceType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
        }
    ).named(renames["CompositeMediaIn"])
    types["CompositeMediaOut"] = t.struct(
        {
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "blobRef": t.string().optional(),
            "length": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "path": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "referenceType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeMediaOut"])
    types["ContentTypeInfoIn"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
        }
    ).named(renames["ContentTypeInfoIn"])
    types["ContentTypeInfoOut"] = t.struct(
        {
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentTypeInfoOut"])
    types["EscalationIn"] = t.struct(
        {"justification": t.string(), "reason": t.string()}
    ).named(renames["EscalationIn"])
    types["EscalationOut"] = t.struct(
        {
            "justification": t.string(),
            "reason": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalationOut"])
    types["WorkflowOperationMetadataIn"] = t.struct(
        {
            "workflowOperationType": t.string().optional(),
            "namespace": t.string().optional(),
            "operationAction": t.string().optional(),
        }
    ).named(renames["WorkflowOperationMetadataIn"])
    types["WorkflowOperationMetadataOut"] = t.struct(
        {
            "workflowOperationType": t.string().optional(),
            "namespace": t.string().optional(),
            "operationAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkflowOperationMetadataOut"])
    types["AttachmentIn"] = t.struct({"filename": t.string().optional()}).named(
        renames["AttachmentIn"]
    )
    types["AttachmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "filename": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["DiffUploadRequestIn"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["DiffUploadRequestIn"])
    types["DiffUploadRequestOut"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadRequestOut"])
    types["DownloadParametersIn"] = t.struct(
        {
            "ignoreRange": t.boolean().optional(),
            "allowGzipCompression": t.boolean().optional(),
        }
    ).named(renames["DownloadParametersIn"])
    types["DownloadParametersOut"] = t.struct(
        {
            "ignoreRange": t.boolean().optional(),
            "allowGzipCompression": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadParametersOut"])
    types["SearchCaseClassificationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "caseClassifications": t.array(
                t.proxy(renames["CaseClassificationIn"])
            ).optional(),
        }
    ).named(renames["SearchCaseClassificationsResponseIn"])
    types["SearchCaseClassificationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "caseClassifications": t.array(
                t.proxy(renames["CaseClassificationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchCaseClassificationsResponseOut"])
    types["CaseIn"] = t.struct(
        {
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "escalated": t.boolean().optional(),
            "classification": t.proxy(renames["CaseClassificationIn"]).optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "testCase": t.boolean().optional(),
            "severity": t.string().optional(),
            "priority": t.string().optional(),
            "creator": t.proxy(renames["ActorIn"]).optional(),
            "contactEmail": t.string().optional(),
            "timeZone": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CaseIn"])
    types["CaseOut"] = t.struct(
        {
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "escalated": t.boolean().optional(),
            "classification": t.proxy(renames["CaseClassificationOut"]).optional(),
            "description": t.string().optional(),
            "languageCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "testCase": t.boolean().optional(),
            "severity": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "priority": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "contactEmail": t.string().optional(),
            "timeZone": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseOut"])
    types["EscalateCaseRequestIn"] = t.struct(
        {"escalation": t.proxy(renames["EscalationIn"]).optional()}
    ).named(renames["EscalateCaseRequestIn"])
    types["EscalateCaseRequestOut"] = t.struct(
        {
            "escalation": t.proxy(renames["EscalationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalateCaseRequestOut"])
    types["DiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["CompositeMediaIn"]).optional()}
    ).named(renames["DiffDownloadResponseIn"])
    types["DiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffDownloadResponseOut"])

    functions = {}
    functions["mediaUpload"] = cloudsupport.get(
        "v2beta/{name}:download",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = cloudsupport.get(
        "v2beta/{name}:download",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["caseClassificationsSearch"] = cloudsupport.get(
        "v2beta/caseClassifications:search",
        t.struct(
            {
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCaseClassificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesEscalate"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesSearch"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesClose"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCreate"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesPatch"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesGet"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesList"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesAttachmentsList"] = cloudsupport.get(
        "v2beta/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttachmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCommentsCreate"] = cloudsupport.get(
        "v2beta/{parent}/comments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCommentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCommentsList"] = cloudsupport.get(
        "v2beta/{parent}/comments",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCommentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsupport", renames=renames, types=types, functions=functions
    )
