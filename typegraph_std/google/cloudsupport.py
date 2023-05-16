from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudsupport() -> Import:
    cloudsupport = HTTPRuntime("https://cloudsupport.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudsupport_1_ErrorResponse",
        "ListCasesResponseIn": "_cloudsupport_2_ListCasesResponseIn",
        "ListCasesResponseOut": "_cloudsupport_3_ListCasesResponseOut",
        "ActorIn": "_cloudsupport_4_ActorIn",
        "ActorOut": "_cloudsupport_5_ActorOut",
        "DiffUploadResponseIn": "_cloudsupport_6_DiffUploadResponseIn",
        "DiffUploadResponseOut": "_cloudsupport_7_DiffUploadResponseOut",
        "ObjectIdIn": "_cloudsupport_8_ObjectIdIn",
        "ObjectIdOut": "_cloudsupport_9_ObjectIdOut",
        "EscalateCaseRequestIn": "_cloudsupport_10_EscalateCaseRequestIn",
        "EscalateCaseRequestOut": "_cloudsupport_11_EscalateCaseRequestOut",
        "CompositeMediaIn": "_cloudsupport_12_CompositeMediaIn",
        "CompositeMediaOut": "_cloudsupport_13_CompositeMediaOut",
        "AttachmentIn": "_cloudsupport_14_AttachmentIn",
        "AttachmentOut": "_cloudsupport_15_AttachmentOut",
        "DiffVersionResponseIn": "_cloudsupport_16_DiffVersionResponseIn",
        "DiffVersionResponseOut": "_cloudsupport_17_DiffVersionResponseOut",
        "DiffDownloadResponseIn": "_cloudsupport_18_DiffDownloadResponseIn",
        "DiffDownloadResponseOut": "_cloudsupport_19_DiffDownloadResponseOut",
        "SearchCaseClassificationsResponseIn": "_cloudsupport_20_SearchCaseClassificationsResponseIn",
        "SearchCaseClassificationsResponseOut": "_cloudsupport_21_SearchCaseClassificationsResponseOut",
        "WorkflowOperationMetadataIn": "_cloudsupport_22_WorkflowOperationMetadataIn",
        "WorkflowOperationMetadataOut": "_cloudsupport_23_WorkflowOperationMetadataOut",
        "CaseClassificationIn": "_cloudsupport_24_CaseClassificationIn",
        "CaseClassificationOut": "_cloudsupport_25_CaseClassificationOut",
        "EscalationIn": "_cloudsupport_26_EscalationIn",
        "EscalationOut": "_cloudsupport_27_EscalationOut",
        "ListCommentsResponseIn": "_cloudsupport_28_ListCommentsResponseIn",
        "ListCommentsResponseOut": "_cloudsupport_29_ListCommentsResponseOut",
        "CreateAttachmentRequestIn": "_cloudsupport_30_CreateAttachmentRequestIn",
        "CreateAttachmentRequestOut": "_cloudsupport_31_CreateAttachmentRequestOut",
        "CloseCaseRequestIn": "_cloudsupport_32_CloseCaseRequestIn",
        "CloseCaseRequestOut": "_cloudsupport_33_CloseCaseRequestOut",
        "Blobstore2InfoIn": "_cloudsupport_34_Blobstore2InfoIn",
        "Blobstore2InfoOut": "_cloudsupport_35_Blobstore2InfoOut",
        "ListAttachmentsResponseIn": "_cloudsupport_36_ListAttachmentsResponseIn",
        "ListAttachmentsResponseOut": "_cloudsupport_37_ListAttachmentsResponseOut",
        "CommentIn": "_cloudsupport_38_CommentIn",
        "CommentOut": "_cloudsupport_39_CommentOut",
        "CaseIn": "_cloudsupport_40_CaseIn",
        "CaseOut": "_cloudsupport_41_CaseOut",
        "DownloadParametersIn": "_cloudsupport_42_DownloadParametersIn",
        "DownloadParametersOut": "_cloudsupport_43_DownloadParametersOut",
        "MediaIn": "_cloudsupport_44_MediaIn",
        "MediaOut": "_cloudsupport_45_MediaOut",
        "DiffChecksumsResponseIn": "_cloudsupport_46_DiffChecksumsResponseIn",
        "DiffChecksumsResponseOut": "_cloudsupport_47_DiffChecksumsResponseOut",
        "SearchCasesResponseIn": "_cloudsupport_48_SearchCasesResponseIn",
        "SearchCasesResponseOut": "_cloudsupport_49_SearchCasesResponseOut",
        "ContentTypeInfoIn": "_cloudsupport_50_ContentTypeInfoIn",
        "ContentTypeInfoOut": "_cloudsupport_51_ContentTypeInfoOut",
        "DiffUploadRequestIn": "_cloudsupport_52_DiffUploadRequestIn",
        "DiffUploadRequestOut": "_cloudsupport_53_DiffUploadRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ActorIn"] = t.struct(
        {"displayName": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ActorIn"])
    types["ActorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "email": t.string().optional(),
            "googleSupport": t.boolean().optional(),
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
    types["EscalateCaseRequestIn"] = t.struct(
        {"escalation": t.proxy(renames["EscalationIn"]).optional()}
    ).named(renames["EscalateCaseRequestIn"])
    types["EscalateCaseRequestOut"] = t.struct(
        {
            "escalation": t.proxy(renames["EscalationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EscalateCaseRequestOut"])
    types["CompositeMediaIn"] = t.struct(
        {
            "referenceType": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "length": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "inline": t.string().optional(),
            "blobRef": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "path": t.string().optional(),
        }
    ).named(renames["CompositeMediaIn"])
    types["CompositeMediaOut"] = t.struct(
        {
            "referenceType": t.string().optional(),
            "md5Hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "length": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "inline": t.string().optional(),
            "blobRef": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompositeMediaOut"])
    types["AttachmentIn"] = t.struct({"filename": t.string().optional()}).named(
        renames["AttachmentIn"]
    )
    types["AttachmentOut"] = t.struct(
        {
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "name": t.string().optional(),
            "filename": t.string().optional(),
            "mimeType": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
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
    types["DiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["CompositeMediaIn"]).optional()}
    ).named(renames["DiffDownloadResponseIn"])
    types["DiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffDownloadResponseOut"])
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
    types["CreateAttachmentRequestIn"] = t.struct(
        {"attachment": t.proxy(renames["AttachmentIn"])}
    ).named(renames["CreateAttachmentRequestIn"])
    types["CreateAttachmentRequestOut"] = t.struct(
        {
            "attachment": t.proxy(renames["AttachmentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateAttachmentRequestOut"])
    types["CloseCaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloseCaseRequestIn"]
    )
    types["CloseCaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloseCaseRequestOut"])
    types["Blobstore2InfoIn"] = t.struct(
        {
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
            "blobGeneration": t.string().optional(),
        }
    ).named(renames["Blobstore2InfoIn"])
    types["Blobstore2InfoOut"] = t.struct(
        {
            "blobId": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "readToken": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Blobstore2InfoOut"])
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
    types["CommentIn"] = t.struct({"body": t.string().optional()}).named(
        renames["CommentIn"]
    )
    types["CommentOut"] = t.struct(
        {
            "body": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "plainTextBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommentOut"])
    types["CaseIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "priority": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "escalated": t.boolean().optional(),
            "severity": t.string().optional(),
            "contactEmail": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "classification": t.proxy(renames["CaseClassificationIn"]).optional(),
            "creator": t.proxy(renames["ActorIn"]).optional(),
            "name": t.string().optional(),
            "testCase": t.boolean().optional(),
        }
    ).named(renames["CaseIn"])
    types["CaseOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "state": t.string().optional(),
            "priority": t.string().optional(),
            "subscriberEmailAddresses": t.array(t.string()).optional(),
            "languageCode": t.string().optional(),
            "escalated": t.boolean().optional(),
            "severity": t.string().optional(),
            "createTime": t.string().optional(),
            "contactEmail": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "classification": t.proxy(renames["CaseClassificationOut"]).optional(),
            "updateTime": t.string().optional(),
            "creator": t.proxy(renames["ActorOut"]).optional(),
            "name": t.string().optional(),
            "testCase": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CaseOut"])
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
    types["MediaIn"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "filename": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseIn"]
            ).optional(),
            "diffVersionResponse": t.proxy(renames["DiffVersionResponseIn"]).optional(),
            "inline": t.string().optional(),
            "hash": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoIn"]).optional(),
            "sha1Hash": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseIn"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "mediaId": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersIn"]).optional(),
            "sha256Hash": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestIn"]).optional(),
            "timestamp": t.string().optional(),
            "contentType": t.string().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaIn"])).optional(),
            "token": t.string().optional(),
            "path": t.string().optional(),
            "referenceType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoIn"]).optional(),
            "blobRef": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseIn"]
            ).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdIn"]).optional(),
            "length": t.string().optional(),
        }
    ).named(renames["MediaIn"])
    types["MediaOut"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "filename": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["DiffDownloadResponseOut"]
            ).optional(),
            "diffVersionResponse": t.proxy(
                renames["DiffVersionResponseOut"]
            ).optional(),
            "inline": t.string().optional(),
            "hash": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["ContentTypeInfoOut"]).optional(),
            "sha1Hash": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(renames["DiffUploadResponseOut"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "mediaId": t.string().optional(),
            "downloadParameters": t.proxy(renames["DownloadParametersOut"]).optional(),
            "sha256Hash": t.string().optional(),
            "diffUploadRequest": t.proxy(renames["DiffUploadRequestOut"]).optional(),
            "timestamp": t.string().optional(),
            "contentType": t.string().optional(),
            "compositeMedia": t.array(t.proxy(renames["CompositeMediaOut"])).optional(),
            "token": t.string().optional(),
            "path": t.string().optional(),
            "referenceType": t.string().optional(),
            "blobstore2Info": t.proxy(renames["Blobstore2InfoOut"]).optional(),
            "blobRef": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["DiffChecksumsResponseOut"]
            ).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "objectId": t.proxy(renames["ObjectIdOut"]).optional(),
            "length": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["DiffChecksumsResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
        }
    ).named(renames["DiffChecksumsResponseIn"])
    types["DiffChecksumsResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectLocation": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffChecksumsResponseOut"])
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
    types["ContentTypeInfoIn"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromFileName": t.string().optional(),
        }
    ).named(renames["ContentTypeInfoIn"])
    types["ContentTypeInfoOut"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentTypeInfoOut"])
    types["DiffUploadRequestIn"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["CompositeMediaIn"]).optional(),
        }
    ).named(renames["DiffUploadRequestIn"])
    types["DiffUploadRequestOut"] = t.struct(
        {
            "checksumsInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "objectInfo": t.proxy(renames["CompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiffUploadRequestOut"])

    functions = {}
    functions["casesList"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesCreate"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesClose"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesPatch"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesGet"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesEscalate"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesSearch"] = cloudsupport.get(
        "v2beta/cases:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["casesAttachmentsList"] = cloudsupport.get(
        "v2beta/{parent}/attachments",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchCaseClassificationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = cloudsupport.post(
        "v2beta/{parent}/attachments",
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
        "v2beta/{parent}/attachments",
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
