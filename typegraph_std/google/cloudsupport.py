from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudsupport():
    cloudsupport = HTTPRuntime("https://cloudsupport.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsupport_1_ErrorResponse",
        "ContentTypeInfoIn": "_cloudsupport_2_ContentTypeInfoIn",
        "ContentTypeInfoOut": "_cloudsupport_3_ContentTypeInfoOut",
        "CloseCaseRequestIn": "_cloudsupport_4_CloseCaseRequestIn",
        "CloseCaseRequestOut": "_cloudsupport_5_CloseCaseRequestOut",
        "CaseClassificationIn": "_cloudsupport_6_CaseClassificationIn",
        "CaseClassificationOut": "_cloudsupport_7_CaseClassificationOut",
        "ActorIn": "_cloudsupport_8_ActorIn",
        "ActorOut": "_cloudsupport_9_ActorOut",
        "DiffUploadResponseIn": "_cloudsupport_10_DiffUploadResponseIn",
        "DiffUploadResponseOut": "_cloudsupport_11_DiffUploadResponseOut",
        "SearchCaseClassificationsResponseIn": "_cloudsupport_12_SearchCaseClassificationsResponseIn",
        "SearchCaseClassificationsResponseOut": "_cloudsupport_13_SearchCaseClassificationsResponseOut",
        "DiffUploadRequestIn": "_cloudsupport_14_DiffUploadRequestIn",
        "DiffUploadRequestOut": "_cloudsupport_15_DiffUploadRequestOut",
        "DiffVersionResponseIn": "_cloudsupport_16_DiffVersionResponseIn",
        "DiffVersionResponseOut": "_cloudsupport_17_DiffVersionResponseOut",
        "CommentIn": "_cloudsupport_18_CommentIn",
        "CommentOut": "_cloudsupport_19_CommentOut",
        "ObjectIdIn": "_cloudsupport_20_ObjectIdIn",
        "ObjectIdOut": "_cloudsupport_21_ObjectIdOut",
        "CaseIn": "_cloudsupport_22_CaseIn",
        "CaseOut": "_cloudsupport_23_CaseOut",
        "EscalationIn": "_cloudsupport_24_EscalationIn",
        "EscalationOut": "_cloudsupport_25_EscalationOut",
        "Blobstore2InfoIn": "_cloudsupport_26_Blobstore2InfoIn",
        "Blobstore2InfoOut": "_cloudsupport_27_Blobstore2InfoOut",
        "ListCommentsResponseIn": "_cloudsupport_28_ListCommentsResponseIn",
        "ListCommentsResponseOut": "_cloudsupport_29_ListCommentsResponseOut",
        "EscalateCaseRequestIn": "_cloudsupport_30_EscalateCaseRequestIn",
        "EscalateCaseRequestOut": "_cloudsupport_31_EscalateCaseRequestOut",
        "MediaIn": "_cloudsupport_32_MediaIn",
        "MediaOut": "_cloudsupport_33_MediaOut",
        "DiffChecksumsResponseIn": "_cloudsupport_34_DiffChecksumsResponseIn",
        "DiffChecksumsResponseOut": "_cloudsupport_35_DiffChecksumsResponseOut",
        "CompositeMediaIn": "_cloudsupport_36_CompositeMediaIn",
        "CompositeMediaOut": "_cloudsupport_37_CompositeMediaOut",
        "DiffDownloadResponseIn": "_cloudsupport_38_DiffDownloadResponseIn",
        "DiffDownloadResponseOut": "_cloudsupport_39_DiffDownloadResponseOut",
        "SearchCasesResponseIn": "_cloudsupport_40_SearchCasesResponseIn",
        "SearchCasesResponseOut": "_cloudsupport_41_SearchCasesResponseOut",
        "ListCasesResponseIn": "_cloudsupport_42_ListCasesResponseIn",
        "ListCasesResponseOut": "_cloudsupport_43_ListCasesResponseOut",
        "ListAttachmentsResponseIn": "_cloudsupport_44_ListAttachmentsResponseIn",
        "ListAttachmentsResponseOut": "_cloudsupport_45_ListAttachmentsResponseOut",
        "DownloadParametersIn": "_cloudsupport_46_DownloadParametersIn",
        "DownloadParametersOut": "_cloudsupport_47_DownloadParametersOut",
        "CreateAttachmentRequestIn": "_cloudsupport_48_CreateAttachmentRequestIn",
        "CreateAttachmentRequestOut": "_cloudsupport_49_CreateAttachmentRequestOut",
        "AttachmentIn": "_cloudsupport_50_AttachmentIn",
        "AttachmentOut": "_cloudsupport_51_AttachmentOut",
        "WorkflowOperationMetadataIn": "_cloudsupport_52_WorkflowOperationMetadataIn",
        "WorkflowOperationMetadataOut": "_cloudsupport_53_WorkflowOperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContentTypeInfoIn"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
        }
    ).named(renames["ContentTypeInfoIn"])
    types["ContentTypeInfoOut"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentTypeInfoOut"])
    types["CloseCaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseCaseRequestIn"]
    )
    types["CloseCaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseCaseRequestOut"])
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
    types["ActorIn"] = t.struct(
        {"displayName": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "googleSupport": t.boolean().optional(),
            "displayName": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])
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
    types["SearchCaseClassificationsResponseIn"] = t.struct(
        {
            "caseClassifications": t.array(
                t.proxy(renames["CaseClassificationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchCaseClassificationsResponseIn"])
    types["SearchCaseClassificationsResponseOut"] = t.struct(
        {
            "caseClassifications": t.array(
                t.proxy(renames["CaseClassificationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchCaseClassificationsResponseOut"])
    types["DiffUploadRequestIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "checksumsInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
        }
    ).named(renames["DiffUploadRequestIn"])
    types["DiffUploadRequestOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "checksumsInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadRequestOut"])
    types["DiffVersionResponseIn"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectSizeBytes": t.string().optional(),
        }
    ).named(renames["DiffVersionResponseIn"])
    types["DiffVersionResponseOut"] = t.struct(
        {
            "objectVersion": t.string().optional(),
            "objectSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffVersionResponseOut"])
    types["CommentIn"] = t.struct({"body": t.string().optional()}).named(
        renames["CommentIn"]
    )
    types["CommentOut"] = t.struct(
        {
            "plainTextBody": t.string().optional(),
            "body": t.string().optional(),
            "name": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["ObjectIdIn"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["ObjectIdIn"])
    types["ObjectIdOut"] = t.struct(
        {
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["CaseIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "priority": t.string().optional(),
            "description": t.string().optional(),
            "testCase": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "classification": t.proxy(renames["CaseClassificationIn"]).optional(),
            "creator": t.proxy(renames["ActorIn"]).optional(),
            "contactEmail": t.string().optional(),
            "escalated": t.boolean().optional(),
        }
    ).named(renames["CaseIn"])
    types["CaseOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "priority": t.string().optional(),
            "description": t.string().optional(),
            "testCase": t.boolean().optional(),
            "timeZone": t.string().optional(),
            "createTime": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "classification": t.proxy(renames["CaseClassificationOut"]).optional(),
            "state": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "contactEmail": t.string().optional(),
            "escalated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseOut"])
    types["EscalationIn"] = t.struct(
        {"reason": t.string(), "justification": t.string()}
    ).named(renames["EscalationIn"])
    types["EscalationOut"] = t.struct(
        {
            "reason": t.string(),
            "justification": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalationOut"])
    types["Blobstore2InfoIn"] = t.struct(
        {
            "uploadMetadataContainer": t.string().optional(),
            "blobId": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
            "blobGeneration": t.string().optional(),
        }
    ).named(renames["Blobstore2InfoIn"])
    types["Blobstore2InfoOut"] = t.struct(
        {
            "uploadMetadataContainer": t.string().optional(),
            "blobId": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Blobstore2InfoOut"])
    types["ListCommentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "comments": t.array(t.proxy(renames["CommentIn"])).optional(),
        }
    ).named(renames["ListCommentsResponseIn"])
    types["ListCommentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "comments": t.array(t.proxy(renames["CommentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCommentsResponseOut"])
    types["EscalateCaseRequestIn"] = t.struct(
        {"escalation": t.proxy(renames["EscalationIn"]).optional()}
    ).named(renames["EscalateCaseRequestIn"])
    types["EscalateCaseRequestOut"] = t.struct(
        {
            "escalation": t.proxy(renames["EscalationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalateCaseRequestOut"])
    types["MediaIn"] = t.struct(
        {
            "bigstoreObjectRef": t.string().optional(),
            "length": t.string().optional(),
            "algorithm": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersIn"]).optional(),
            "hashVerified": t.boolean().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaIn"])).optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "path": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "referenceType": t.string().optional(),
            "token": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseIn"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestIn"]).optional(),
            "timestamp": t.string().optional(),
            "md5Hash": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoIn"]).optional(),
            "hash": t.string().optional(),
            "filename": t.string().optional(),
            "mediaId": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "contentType": t.string().optional(),
            "diffVersionResponse": t.proxy(renames["DiffVersionResponseIn"]).optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseIn"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseIn"]
            ).optional(),
            "inline": t.string().optional(),
        }
    ).named(renames["MediaIn"])
    types["MediaOut"] = t.struct(
        {
            "bigstoreObjectRef": t.string().optional(),
            "length": t.string().optional(),
            "algorithm": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersOut"]).optional(),
            "hashVerified": t.boolean().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaOut"])).optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "path": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "referenceType": t.string().optional(),
            "token": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseOut"]
            ).optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestOut"]).optional(),
            "timestamp": t.string().optional(),
            "md5Hash": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoOut"]).optional(),
            "hash": t.string().optional(),
            "filename": t.string().optional(),
            "mediaId": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "contentType": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["DiffVersionResponseOut"]
            ).optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseOut"]).optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseOut"]
            ).optional(),
            "inline": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["DiffChecksumsResponseIn"] = t.struct(
        {
            "checksumsLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
        }
    ).named(renames["DiffChecksumsResponseIn"])
    types["DiffChecksumsResponseOut"] = t.struct(
        {
            "checksumsLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffChecksumsResponseOut"])
    types["CompositeMediaIn"] = t.struct(
        {
            "md5Hash": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "inline": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "crc32cHash": t.integer().optional(),
        }
    ).named(renames["CompositeMediaIn"])
    types["CompositeMediaOut"] = t.struct(
        {
            "md5Hash": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "inline": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "blobRef": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeMediaOut"])
    types["DiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["CompositeMediaIn"]).optional()}
    ).named(renames["DiffDownloadResponseIn"])
    types["DiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffDownloadResponseOut"])
    types["SearchCasesResponseIn"] = t.struct(
        {
            "cases": t.array(t.proxy(renames["CaseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchCasesResponseIn"])
    types["SearchCasesResponseOut"] = t.struct(
        {
            "cases": t.array(t.proxy(renames["CaseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchCasesResponseOut"])
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
    types["CreateAttachmentRequestIn"] = t.struct(
        {"attachment": t.proxy(renames["AttachmentIn"])}
    ).named(renames["CreateAttachmentRequestIn"])
    types["CreateAttachmentRequestOut"] = t.struct(
        {
            "attachment": t.proxy(renames["AttachmentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAttachmentRequestOut"])
    types["AttachmentIn"] = t.struct({"filename": t.string().optional()}).named(
        renames["AttachmentIn"]
    )
    types["AttachmentOut"] = t.struct(
        {
            "filename": t.string().optional(),
            "mimeType": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
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

    functions = {}
    functions["caseClassificationsSearch"] = cloudsupport.get(
        "v2/caseClassifications:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCaseClassificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesPatch"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCreate"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesClose"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesSearch"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesList"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesEscalate"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesGet"] = cloudsupport.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CaseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCommentsList"] = cloudsupport.post(
        "v2/{parent}/comments",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCommentsCreate"] = cloudsupport.post(
        "v2/{parent}/comments",
        t.struct(
            {
                "parent": t.string(),
                "body": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesAttachmentsList"] = cloudsupport.get(
        "v2/{parent}/attachments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttachmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = cloudsupport.post(
        "v2/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "attachment": t.proxy(renames["AttachmentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = cloudsupport.post(
        "v2/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "attachment": t.proxy(renames["AttachmentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudsupport",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
