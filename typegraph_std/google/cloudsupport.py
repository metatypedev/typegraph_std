from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudsupport() -> Import:
    cloudsupport = HTTPRuntime("https://cloudsupport.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsupport_1_ErrorResponse",
        "DiffChecksumsResponseIn": "_cloudsupport_2_DiffChecksumsResponseIn",
        "DiffChecksumsResponseOut": "_cloudsupport_3_DiffChecksumsResponseOut",
        "DiffVersionResponseIn": "_cloudsupport_4_DiffVersionResponseIn",
        "DiffVersionResponseOut": "_cloudsupport_5_DiffVersionResponseOut",
        "Blobstore2InfoIn": "_cloudsupport_6_Blobstore2InfoIn",
        "Blobstore2InfoOut": "_cloudsupport_7_Blobstore2InfoOut",
        "SearchCasesResponseIn": "_cloudsupport_8_SearchCasesResponseIn",
        "SearchCasesResponseOut": "_cloudsupport_9_SearchCasesResponseOut",
        "CompositeMediaIn": "_cloudsupport_10_CompositeMediaIn",
        "CompositeMediaOut": "_cloudsupport_11_CompositeMediaOut",
        "EscalationIn": "_cloudsupport_12_EscalationIn",
        "EscalationOut": "_cloudsupport_13_EscalationOut",
        "DownloadParametersIn": "_cloudsupport_14_DownloadParametersIn",
        "DownloadParametersOut": "_cloudsupport_15_DownloadParametersOut",
        "WorkflowOperationMetadataIn": "_cloudsupport_16_WorkflowOperationMetadataIn",
        "WorkflowOperationMetadataOut": "_cloudsupport_17_WorkflowOperationMetadataOut",
        "ListAttachmentsResponseIn": "_cloudsupport_18_ListAttachmentsResponseIn",
        "ListAttachmentsResponseOut": "_cloudsupport_19_ListAttachmentsResponseOut",
        "ListCasesResponseIn": "_cloudsupport_20_ListCasesResponseIn",
        "ListCasesResponseOut": "_cloudsupport_21_ListCasesResponseOut",
        "ContentTypeInfoIn": "_cloudsupport_22_ContentTypeInfoIn",
        "ContentTypeInfoOut": "_cloudsupport_23_ContentTypeInfoOut",
        "CaseIn": "_cloudsupport_24_CaseIn",
        "CaseOut": "_cloudsupport_25_CaseOut",
        "DiffUploadRequestIn": "_cloudsupport_26_DiffUploadRequestIn",
        "DiffUploadRequestOut": "_cloudsupport_27_DiffUploadRequestOut",
        "DiffDownloadResponseIn": "_cloudsupport_28_DiffDownloadResponseIn",
        "DiffDownloadResponseOut": "_cloudsupport_29_DiffDownloadResponseOut",
        "DiffUploadResponseIn": "_cloudsupport_30_DiffUploadResponseIn",
        "DiffUploadResponseOut": "_cloudsupport_31_DiffUploadResponseOut",
        "CloseCaseRequestIn": "_cloudsupport_32_CloseCaseRequestIn",
        "CloseCaseRequestOut": "_cloudsupport_33_CloseCaseRequestOut",
        "CreateAttachmentRequestIn": "_cloudsupport_34_CreateAttachmentRequestIn",
        "CreateAttachmentRequestOut": "_cloudsupport_35_CreateAttachmentRequestOut",
        "MediaIn": "_cloudsupport_36_MediaIn",
        "MediaOut": "_cloudsupport_37_MediaOut",
        "CommentIn": "_cloudsupport_38_CommentIn",
        "CommentOut": "_cloudsupport_39_CommentOut",
        "ListCommentsResponseIn": "_cloudsupport_40_ListCommentsResponseIn",
        "ListCommentsResponseOut": "_cloudsupport_41_ListCommentsResponseOut",
        "CaseClassificationIn": "_cloudsupport_42_CaseClassificationIn",
        "CaseClassificationOut": "_cloudsupport_43_CaseClassificationOut",
        "EscalateCaseRequestIn": "_cloudsupport_44_EscalateCaseRequestIn",
        "EscalateCaseRequestOut": "_cloudsupport_45_EscalateCaseRequestOut",
        "SearchCaseClassificationsResponseIn": "_cloudsupport_46_SearchCaseClassificationsResponseIn",
        "SearchCaseClassificationsResponseOut": "_cloudsupport_47_SearchCaseClassificationsResponseOut",
        "AttachmentIn": "_cloudsupport_48_AttachmentIn",
        "AttachmentOut": "_cloudsupport_49_AttachmentOut",
        "ObjectIdIn": "_cloudsupport_50_ObjectIdIn",
        "ObjectIdOut": "_cloudsupport_51_ObjectIdOut",
        "ActorIn": "_cloudsupport_52_ActorIn",
        "ActorOut": "_cloudsupport_53_ActorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DiffChecksumsResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["DiffChecksumsResponseIn"])
    types["DiffChecksumsResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
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
    types["Blobstore2InfoIn"] = t.struct(
        {
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobGeneration": t.string().optional(),
        }
    ).named(renames["Blobstore2InfoIn"])
    types["Blobstore2InfoOut"] = t.struct(
        {
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Blobstore2InfoOut"])
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
    types["CompositeMediaIn"] = t.struct(
        {
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "inline": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "blobRef": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
        }
    ).named(renames["CompositeMediaIn"])
    types["CompositeMediaOut"] = t.struct(
        {
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "inline": t.string().optional(),
            "path": t.string().optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "blobRef": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeMediaOut"])
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
    types["ListAttachmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentIn"])).optional(),
        }
    ).named(renames["ListAttachmentsResponseIn"])
    types["ListAttachmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "attachments": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttachmentsResponseOut"])
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
    types["ContentTypeInfoIn"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
        }
    ).named(renames["ContentTypeInfoIn"])
    types["ContentTypeInfoOut"] = t.struct(
        {
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "bestGuess": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentTypeInfoOut"])
    types["CaseIn"] = t.struct(
        {
            "creator": t.proxy(renames["ActorIn"]).optional(),
            "severity": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "priority": t.string().optional(),
            "contactEmail": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "testCase": t.boolean().optional(),
            "classification": t.proxy(renames["CaseClassificationIn"]).optional(),
            "escalated": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["CaseIn"])
    types["CaseOut"] = t.struct(
        {
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "severity": t.string().optional(),
            "state": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "priority": t.string().optional(),
            "contactEmail": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "testCase": t.boolean().optional(),
            "classification": t.proxy(renames["CaseClassificationOut"]).optional(),
            "escalated": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseOut"])
    types["DiffUploadRequestIn"] = t.struct(
        {
            "objectInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "checksumsInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["DiffUploadRequestIn"])
    types["DiffUploadRequestOut"] = t.struct(
        {
            "objectInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "checksumsInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadRequestOut"])
    types["DiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["CompositeMediaIn"]).optional()}
    ).named(renames["DiffDownloadResponseIn"])
    types["DiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffDownloadResponseOut"])
    types["DiffUploadResponseIn"] = t.struct(
        {
            "originalObject": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["DiffUploadResponseIn"])
    types["DiffUploadResponseOut"] = t.struct(
        {
            "originalObject": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadResponseOut"])
    types["CloseCaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseCaseRequestIn"]
    )
    types["CloseCaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseCaseRequestOut"])
    types["CreateAttachmentRequestIn"] = t.struct(
        {"attachment": t.proxy(renames["AttachmentIn"])}
    ).named(renames["CreateAttachmentRequestIn"])
    types["CreateAttachmentRequestOut"] = t.struct(
        {
            "attachment": t.proxy(renames["AttachmentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAttachmentRequestOut"])
    types["MediaIn"] = t.struct(
        {
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseIn"]
            ).optional(),
            "token": t.string().optional(),
            "inline": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "timestamp": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersIn"]).optional(),
            "hash": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "mediaId": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseIn"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "diffVersionResponse": t.proxy(renames["DiffVersionResponseIn"]).optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "contentType": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoIn"]).optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "length": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseIn"]
            ).optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaIn"])).optional(),
            "filename": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "path": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestIn"]).optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
        }
    ).named(renames["MediaIn"])
    types["MediaOut"] = t.struct(
        {
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseOut"]
            ).optional(),
            "token": t.string().optional(),
            "inline": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "timestamp": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersOut"]).optional(),
            "hash": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "mediaId": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseOut"]).optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["DiffVersionResponseOut"]
            ).optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "contentType": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoOut"]).optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "length": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseOut"]
            ).optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaOut"])).optional(),
            "filename": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "path": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestOut"]).optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
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
    types["CaseClassificationIn"] = t.struct(
        {"id": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["CaseClassificationIn"])
    types["CaseClassificationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseClassificationOut"])
    types["EscalateCaseRequestIn"] = t.struct(
        {"escalation": t.proxy(renames["EscalationIn"]).optional()}
    ).named(renames["EscalateCaseRequestIn"])
    types["EscalateCaseRequestOut"] = t.struct(
        {
            "escalation": t.proxy(renames["EscalationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalateCaseRequestOut"])
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
    types["AttachmentIn"] = t.struct({"filename": t.string().optional()}).named(
        renames["AttachmentIn"]
    )
    types["AttachmentOut"] = t.struct(
        {
            "filename": t.string().optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["ObjectIdIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
        }
    ).named(renames["ObjectIdIn"])
    types["ObjectIdOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectIdOut"])
    types["ActorIn"] = t.struct(
        {"email": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "email": t.string().optional(),
            "googleSupport": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActorOut"])

    functions = {}
    functions["casesEscalate"] = cloudsupport.get(
        "v2beta/{parent}/cases",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCommentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["caseClassificationsSearch"] = cloudsupport.get(
        "v2beta/caseClassifications:search",
        t.struct(
            {
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCaseClassificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="cloudsupport",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
