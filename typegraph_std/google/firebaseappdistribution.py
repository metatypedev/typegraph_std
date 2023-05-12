from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebaseappdistribution() -> Import:
    firebaseappdistribution = HTTPRuntime(
        "https://firebaseappdistribution.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_firebaseappdistribution_1_ErrorResponse",
        "GoogleFirebaseAppdistroV1ReleaseNotesIn": "_firebaseappdistribution_2_GoogleFirebaseAppdistroV1ReleaseNotesIn",
        "GoogleFirebaseAppdistroV1ReleaseNotesOut": "_firebaseappdistribution_3_GoogleFirebaseAppdistroV1ReleaseNotesOut",
        "GoogleFirebaseAppdistroV1TesterIn": "_firebaseappdistribution_4_GoogleFirebaseAppdistroV1TesterIn",
        "GoogleFirebaseAppdistroV1TesterOut": "_firebaseappdistribution_5_GoogleFirebaseAppdistroV1TesterOut",
        "GoogleFirebaseAppdistroV1FeedbackReportIn": "_firebaseappdistribution_6_GoogleFirebaseAppdistroV1FeedbackReportIn",
        "GoogleFirebaseAppdistroV1FeedbackReportOut": "_firebaseappdistribution_7_GoogleFirebaseAppdistroV1FeedbackReportOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firebaseappdistribution_8_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firebaseappdistribution_9_GoogleLongrunningCancelOperationRequestOut",
        "GdataDiffChecksumsResponseIn": "_firebaseappdistribution_10_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_firebaseappdistribution_11_GdataDiffChecksumsResponseOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn": "_firebaseappdistribution_12_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut": "_firebaseappdistribution_13_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut",
        "GoogleFirebaseAppdistroV1AabInfoIn": "_firebaseappdistribution_14_GoogleFirebaseAppdistroV1AabInfoIn",
        "GoogleFirebaseAppdistroV1AabInfoOut": "_firebaseappdistribution_15_GoogleFirebaseAppdistroV1AabInfoOut",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestIn": "_firebaseappdistribution_16_GoogleFirebaseAppdistroV1UploadReleaseRequestIn",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestOut": "_firebaseappdistribution_17_GoogleFirebaseAppdistroV1UploadReleaseRequestOut",
        "GoogleFirebaseAppdistroV1ListGroupsResponseIn": "_firebaseappdistribution_18_GoogleFirebaseAppdistroV1ListGroupsResponseIn",
        "GoogleFirebaseAppdistroV1ListGroupsResponseOut": "_firebaseappdistribution_19_GoogleFirebaseAppdistroV1ListGroupsResponseOut",
        "GoogleFirebaseAppdistroV1GroupIn": "_firebaseappdistribution_20_GoogleFirebaseAppdistroV1GroupIn",
        "GoogleFirebaseAppdistroV1GroupOut": "_firebaseappdistribution_21_GoogleFirebaseAppdistroV1GroupOut",
        "GoogleFirebaseAppdistroV1ListReleasesResponseIn": "_firebaseappdistribution_22_GoogleFirebaseAppdistroV1ListReleasesResponseIn",
        "GoogleFirebaseAppdistroV1ListReleasesResponseOut": "_firebaseappdistribution_23_GoogleFirebaseAppdistroV1ListReleasesResponseOut",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataIn": "_firebaseappdistribution_24_GoogleFirebaseAppdistroV1UploadReleaseMetadataIn",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataOut": "_firebaseappdistribution_25_GoogleFirebaseAppdistroV1UploadReleaseMetadataOut",
        "GdataMediaIn": "_firebaseappdistribution_26_GdataMediaIn",
        "GdataMediaOut": "_firebaseappdistribution_27_GdataMediaOut",
        "GoogleLongrunningWaitOperationRequestIn": "_firebaseappdistribution_28_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_firebaseappdistribution_29_GoogleLongrunningWaitOperationRequestOut",
        "GoogleFirebaseAppdistroV1ReleaseIn": "_firebaseappdistribution_30_GoogleFirebaseAppdistroV1ReleaseIn",
        "GoogleFirebaseAppdistroV1ReleaseOut": "_firebaseappdistribution_31_GoogleFirebaseAppdistroV1ReleaseOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestIn": "_firebaseappdistribution_32_GoogleFirebaseAppdistroV1DistributeReleaseRequestIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestOut": "_firebaseappdistribution_33_GoogleFirebaseAppdistroV1DistributeReleaseRequestOut",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn": "_firebaseappdistribution_34_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut": "_firebaseappdistribution_35_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseIn": "_firebaseappdistribution_36_GoogleFirebaseAppdistroV1DistributeReleaseResponseIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseOut": "_firebaseappdistribution_37_GoogleFirebaseAppdistroV1DistributeReleaseResponseOut",
        "GdataObjectIdIn": "_firebaseappdistribution_38_GdataObjectIdIn",
        "GdataObjectIdOut": "_firebaseappdistribution_39_GdataObjectIdOut",
        "GdataDiffDownloadResponseIn": "_firebaseappdistribution_40_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_firebaseappdistribution_41_GdataDiffDownloadResponseOut",
        "GdataDiffUploadResponseIn": "_firebaseappdistribution_42_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_firebaseappdistribution_43_GdataDiffUploadResponseOut",
        "GoogleProtobufEmptyIn": "_firebaseappdistribution_44_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_firebaseappdistribution_45_GoogleProtobufEmptyOut",
        "GdataDiffUploadRequestIn": "_firebaseappdistribution_46_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_firebaseappdistribution_47_GdataDiffUploadRequestOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn": "_firebaseappdistribution_48_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut": "_firebaseappdistribution_49_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut",
        "GdataDownloadParametersIn": "_firebaseappdistribution_50_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_firebaseappdistribution_51_GdataDownloadParametersOut",
        "GoogleLongrunningListOperationsResponseIn": "_firebaseappdistribution_52_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firebaseappdistribution_53_GoogleLongrunningListOperationsResponseOut",
        "GdataDiffVersionResponseIn": "_firebaseappdistribution_54_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_firebaseappdistribution_55_GdataDiffVersionResponseOut",
        "GdataContentTypeInfoIn": "_firebaseappdistribution_56_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_firebaseappdistribution_57_GdataContentTypeInfoOut",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn": "_firebaseappdistribution_58_GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut": "_firebaseappdistribution_59_GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut",
        "GoogleLongrunningOperationIn": "_firebaseappdistribution_60_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firebaseappdistribution_61_GoogleLongrunningOperationOut",
        "GoogleRpcStatusIn": "_firebaseappdistribution_62_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_firebaseappdistribution_63_GoogleRpcStatusOut",
        "GoogleFirebaseAppdistroV1TestCertificateIn": "_firebaseappdistribution_64_GoogleFirebaseAppdistroV1TestCertificateIn",
        "GoogleFirebaseAppdistroV1TestCertificateOut": "_firebaseappdistribution_65_GoogleFirebaseAppdistroV1TestCertificateOut",
        "GoogleFirebaseAppdistroV1ListTestersResponseIn": "_firebaseappdistribution_66_GoogleFirebaseAppdistroV1ListTestersResponseIn",
        "GoogleFirebaseAppdistroV1ListTestersResponseOut": "_firebaseappdistribution_67_GoogleFirebaseAppdistroV1ListTestersResponseOut",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn": "_firebaseappdistribution_68_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut": "_firebaseappdistribution_69_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn": "_firebaseappdistribution_70_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut": "_firebaseappdistribution_71_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut",
        "GdataCompositeMediaIn": "_firebaseappdistribution_72_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_firebaseappdistribution_73_GdataCompositeMediaOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseIn": "_firebaseappdistribution_74_GoogleFirebaseAppdistroV1BatchAddTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseOut": "_firebaseappdistribution_75_GoogleFirebaseAppdistroV1BatchAddTestersResponseOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestIn": "_firebaseappdistribution_76_GoogleFirebaseAppdistroV1BatchAddTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestOut": "_firebaseappdistribution_77_GoogleFirebaseAppdistroV1BatchAddTestersRequestOut",
        "GdataBlobstore2InfoIn": "_firebaseappdistribution_78_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_firebaseappdistribution_79_GdataBlobstore2InfoOut",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseIn": "_firebaseappdistribution_80_GoogleFirebaseAppdistroV1UploadReleaseResponseIn",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseOut": "_firebaseappdistribution_81_GoogleFirebaseAppdistroV1UploadReleaseResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesIn"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"])
    types["GoogleFirebaseAppdistroV1TesterIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "groups": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterIn"])
    types["GoogleFirebaseAppdistroV1TesterOut"] = t.struct(
        {
            "lastActivityTime": t.string().optional(),
            "displayName": t.string().optional(),
            "groups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterOut"])
    types["GoogleFirebaseAppdistroV1FeedbackReportIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
    types["GoogleFirebaseAppdistroV1FeedbackReportOut"] = t.struct(
        {
            "text": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "tester": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "screenshotUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "objectSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "chunkSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"])
    types["GoogleFirebaseAppdistroV1AabInfoIn"] = t.struct(
        {
            "integrationState": t.string().optional(),
            "name": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateIn"]
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoIn"])
    types["GoogleFirebaseAppdistroV1AabInfoOut"] = t.struct(
        {
            "integrationState": t.string().optional(),
            "name": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"] = t.struct(
        {"blob": t.proxy(renames["GdataMediaIn"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"] = t.struct(
        {
            "blob": t.proxy(renames["GdataMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"])
    types["GoogleFirebaseAppdistroV1ListGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1GroupIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListGroupsResponseIn"])
    types["GoogleFirebaseAppdistroV1ListGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListGroupsResponseOut"])
    types["GoogleFirebaseAppdistroV1GroupIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string()}
    ).named(renames["GoogleFirebaseAppdistroV1GroupIn"])
    types["GoogleFirebaseAppdistroV1GroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "releaseCount": t.integer().optional(),
            "inviteLinkCount": t.integer().optional(),
            "testerCount": t.integer().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1GroupOut"])
    types["GoogleFirebaseAppdistroV1ListReleasesResponseIn"] = t.struct(
        {
            "releases": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1ReleaseIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListReleasesResponseIn"])
    types["GoogleFirebaseAppdistroV1ListReleasesResponseOut"] = t.struct(
        {
            "releases": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"])
    types["GdataMediaIn"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "md5Hash": t.string().optional(),
            "token": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "referenceType": t.string().optional(),
            "filename": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "contentType": t.string().optional(),
            "length": t.string().optional(),
            "inline": t.string().optional(),
            "mediaId": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "hashVerified": t.boolean().optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "timestamp": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "md5Hash": t.string().optional(),
            "token": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "referenceType": t.string().optional(),
            "filename": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "contentType": t.string().optional(),
            "length": t.string().optional(),
            "inline": t.string().optional(),
            "mediaId": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "blobRef": t.string().optional(),
            "path": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
    types["GoogleFirebaseAppdistroV1ReleaseIn"] = t.struct(
        {
            "releaseNotes": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseNotesIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseIn"])
    types["GoogleFirebaseAppdistroV1ReleaseOut"] = t.struct(
        {
            "releaseNotes": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "displayVersion": t.string().optional(),
            "testingUri": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "binaryDownloadUri": t.string().optional(),
            "buildVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseRequestIn"] = t.struct(
        {
            "groupAliases": t.array(t.string()).optional(),
            "testerEmails": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseRequestOut"] = t.struct(
        {
            "groupAliases": t.array(t.string()).optional(),
            "testerEmails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseRequestOut"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"])
    types["GdataObjectIdIn"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
        }
    ).named(renames["GdataObjectIdIn"])
    types["GdataObjectIdOut"] = t.struct(
        {
            "generation": t.string().optional(),
            "bucketName": t.string().optional(),
            "objectName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataObjectIdOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"] = t.struct(
        {"emails": t.array(t.string()).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"])
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
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromHeader": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
    types["GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn"] = t.struct(
        {"emails": t.array(t.string()), "createMissingTesters": t.boolean().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "createMissingTesters": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleFirebaseAppdistroV1TestCertificateIn"] = t.struct(
        {
            "hashSha256": t.string().optional(),
            "hashSha1": t.string().optional(),
            "hashMd5": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateIn"])
    types["GoogleFirebaseAppdistroV1TestCertificateOut"] = t.struct(
        {
            "hashSha256": t.string().optional(),
            "hashSha1": t.string().optional(),
            "hashMd5": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateOut"])
    types["GoogleFirebaseAppdistroV1ListTestersResponseIn"] = t.struct(
        {
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1ListTestersResponseOut"] = t.struct(
        {
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListTestersResponseOut"])
    types["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackReports": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn"])
    types["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "feedbackReports": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "blobRef": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "blobRef": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersResponseIn"] = t.struct(
        {
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterIn"])
            ).optional()
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"] = t.struct(
        {
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"])
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "readToken": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobId": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "readToken": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobId": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseResponseIn"] = t.struct(
        {
            "release": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseIn"]
            ).optional(),
            "result": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseResponseIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseResponseOut"] = t.struct(
        {
            "release": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseOut"]
            ).optional(),
            "result": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseResponseOut"])

    functions = {}
    functions["projectsAppsGetAabInfo"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1AabInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesBatchDelete"] = firebaseappdistribution.post(
        "v1/{name}:distribute",
        t.struct(
            {
                "name": t.string(),
                "groupAliases": t.array(t.string()).optional(),
                "testerEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesGet"] = firebaseappdistribution.post(
        "v1/{name}:distribute",
        t.struct(
            {
                "name": t.string(),
                "groupAliases": t.array(t.string()).optional(),
                "testerEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesPatch"] = firebaseappdistribution.post(
        "v1/{name}:distribute",
        t.struct(
            {
                "name": t.string(),
                "groupAliases": t.array(t.string()).optional(),
                "testerEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesList"] = firebaseappdistribution.post(
        "v1/{name}:distribute",
        t.struct(
            {
                "name": t.string(),
                "groupAliases": t.array(t.string()).optional(),
                "testerEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesDistribute"] = firebaseappdistribution.post(
        "v1/{name}:distribute",
        t.struct(
            {
                "name": t.string(),
                "groupAliases": t.array(t.string()).optional(),
                "testerEmails": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsWait"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsList"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsCancel"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsDelete"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsGet"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAppsReleasesFeedbackReportsDelete"
    ] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesFeedbackReportsList"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesFeedbackReportsGet"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsPatch"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsBatchLeave"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsBatchJoin"] = firebaseappdistribution.post(
        "v1/{group}:batchJoin",
        t.struct(
            {
                "group": t.string(),
                "emails": t.array(t.string()),
                "createMissingTesters": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersPatch"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchRemove",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchAdd"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchRemove",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersList"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchRemove",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchRemove"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchRemove",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = firebaseappdistribution.post(
        "v1/{app}/releases:upload",
        t.struct(
            {
                "app": t.string().optional(),
                "blob": t.proxy(renames["GdataMediaIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebaseappdistribution",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
