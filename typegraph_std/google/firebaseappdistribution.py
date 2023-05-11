from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebaseappdistribution() -> Import:
    firebaseappdistribution = HTTPRuntime(
        "https://firebaseappdistribution.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_firebaseappdistribution_1_ErrorResponse",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn": "_firebaseappdistribution_2_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut": "_firebaseappdistribution_3_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut",
        "GdataMediaIn": "_firebaseappdistribution_4_GdataMediaIn",
        "GdataMediaOut": "_firebaseappdistribution_5_GdataMediaOut",
        "GoogleProtobufEmptyIn": "_firebaseappdistribution_6_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_firebaseappdistribution_7_GoogleProtobufEmptyOut",
        "GoogleLongrunningOperationIn": "_firebaseappdistribution_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firebaseappdistribution_9_GoogleLongrunningOperationOut",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn": "_firebaseappdistribution_10_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut": "_firebaseappdistribution_11_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestIn": "_firebaseappdistribution_12_GoogleFirebaseAppdistroV1DistributeReleaseRequestIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestOut": "_firebaseappdistribution_13_GoogleFirebaseAppdistroV1DistributeReleaseRequestOut",
        "GoogleFirebaseAppdistroV1ListGroupsResponseIn": "_firebaseappdistribution_14_GoogleFirebaseAppdistroV1ListGroupsResponseIn",
        "GoogleFirebaseAppdistroV1ListGroupsResponseOut": "_firebaseappdistribution_15_GoogleFirebaseAppdistroV1ListGroupsResponseOut",
        "GdataDiffUploadRequestIn": "_firebaseappdistribution_16_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_firebaseappdistribution_17_GdataDiffUploadRequestOut",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataIn": "_firebaseappdistribution_18_GoogleFirebaseAppdistroV1UploadReleaseMetadataIn",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataOut": "_firebaseappdistribution_19_GoogleFirebaseAppdistroV1UploadReleaseMetadataOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn": "_firebaseappdistribution_20_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut": "_firebaseappdistribution_21_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseIn": "_firebaseappdistribution_22_GoogleFirebaseAppdistroV1DistributeReleaseResponseIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseOut": "_firebaseappdistribution_23_GoogleFirebaseAppdistroV1DistributeReleaseResponseOut",
        "GoogleFirebaseAppdistroV1TestCertificateIn": "_firebaseappdistribution_24_GoogleFirebaseAppdistroV1TestCertificateIn",
        "GoogleFirebaseAppdistroV1TestCertificateOut": "_firebaseappdistribution_25_GoogleFirebaseAppdistroV1TestCertificateOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseIn": "_firebaseappdistribution_26_GoogleFirebaseAppdistroV1BatchAddTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseOut": "_firebaseappdistribution_27_GoogleFirebaseAppdistroV1BatchAddTestersResponseOut",
        "GoogleRpcStatusIn": "_firebaseappdistribution_28_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_firebaseappdistribution_29_GoogleRpcStatusOut",
        "GdataObjectIdIn": "_firebaseappdistribution_30_GdataObjectIdIn",
        "GdataObjectIdOut": "_firebaseappdistribution_31_GdataObjectIdOut",
        "GdataBlobstore2InfoIn": "_firebaseappdistribution_32_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_firebaseappdistribution_33_GdataBlobstore2InfoOut",
        "GdataDiffUploadResponseIn": "_firebaseappdistribution_34_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_firebaseappdistribution_35_GdataDiffUploadResponseOut",
        "GoogleFirebaseAppdistroV1GroupIn": "_firebaseappdistribution_36_GoogleFirebaseAppdistroV1GroupIn",
        "GoogleFirebaseAppdistroV1GroupOut": "_firebaseappdistribution_37_GoogleFirebaseAppdistroV1GroupOut",
        "GdataContentTypeInfoIn": "_firebaseappdistribution_38_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_firebaseappdistribution_39_GdataContentTypeInfoOut",
        "GdataDownloadParametersIn": "_firebaseappdistribution_40_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_firebaseappdistribution_41_GdataDownloadParametersOut",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseIn": "_firebaseappdistribution_42_GoogleFirebaseAppdistroV1UploadReleaseResponseIn",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseOut": "_firebaseappdistribution_43_GoogleFirebaseAppdistroV1UploadReleaseResponseOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestIn": "_firebaseappdistribution_44_GoogleFirebaseAppdistroV1BatchAddTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestOut": "_firebaseappdistribution_45_GoogleFirebaseAppdistroV1BatchAddTestersRequestOut",
        "GdataDiffDownloadResponseIn": "_firebaseappdistribution_46_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_firebaseappdistribution_47_GdataDiffDownloadResponseOut",
        "GoogleLongrunningWaitOperationRequestIn": "_firebaseappdistribution_48_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_firebaseappdistribution_49_GoogleLongrunningWaitOperationRequestOut",
        "GoogleFirebaseAppdistroV1TesterIn": "_firebaseappdistribution_50_GoogleFirebaseAppdistroV1TesterIn",
        "GoogleFirebaseAppdistroV1TesterOut": "_firebaseappdistribution_51_GoogleFirebaseAppdistroV1TesterOut",
        "GoogleFirebaseAppdistroV1ListReleasesResponseIn": "_firebaseappdistribution_52_GoogleFirebaseAppdistroV1ListReleasesResponseIn",
        "GoogleFirebaseAppdistroV1ListReleasesResponseOut": "_firebaseappdistribution_53_GoogleFirebaseAppdistroV1ListReleasesResponseOut",
        "GdataCompositeMediaIn": "_firebaseappdistribution_54_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_firebaseappdistribution_55_GdataCompositeMediaOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firebaseappdistribution_56_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firebaseappdistribution_57_GoogleLongrunningCancelOperationRequestOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn": "_firebaseappdistribution_58_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut": "_firebaseappdistribution_59_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn": "_firebaseappdistribution_60_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut": "_firebaseappdistribution_61_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut",
        "GoogleFirebaseAppdistroV1ReleaseNotesIn": "_firebaseappdistribution_62_GoogleFirebaseAppdistroV1ReleaseNotesIn",
        "GoogleFirebaseAppdistroV1ReleaseNotesOut": "_firebaseappdistribution_63_GoogleFirebaseAppdistroV1ReleaseNotesOut",
        "GoogleFirebaseAppdistroV1ListTestersResponseIn": "_firebaseappdistribution_64_GoogleFirebaseAppdistroV1ListTestersResponseIn",
        "GoogleFirebaseAppdistroV1ListTestersResponseOut": "_firebaseappdistribution_65_GoogleFirebaseAppdistroV1ListTestersResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_firebaseappdistribution_66_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firebaseappdistribution_67_GoogleLongrunningListOperationsResponseOut",
        "GoogleFirebaseAppdistroV1ReleaseIn": "_firebaseappdistribution_68_GoogleFirebaseAppdistroV1ReleaseIn",
        "GoogleFirebaseAppdistroV1ReleaseOut": "_firebaseappdistribution_69_GoogleFirebaseAppdistroV1ReleaseOut",
        "GdataDiffChecksumsResponseIn": "_firebaseappdistribution_70_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_firebaseappdistribution_71_GdataDiffChecksumsResponseOut",
        "GdataDiffVersionResponseIn": "_firebaseappdistribution_72_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_firebaseappdistribution_73_GdataDiffVersionResponseOut",
        "GoogleFirebaseAppdistroV1AabInfoIn": "_firebaseappdistribution_74_GoogleFirebaseAppdistroV1AabInfoIn",
        "GoogleFirebaseAppdistroV1AabInfoOut": "_firebaseappdistribution_75_GoogleFirebaseAppdistroV1AabInfoOut",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn": "_firebaseappdistribution_76_GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut": "_firebaseappdistribution_77_GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut",
        "GoogleFirebaseAppdistroV1FeedbackReportIn": "_firebaseappdistribution_78_GoogleFirebaseAppdistroV1FeedbackReportIn",
        "GoogleFirebaseAppdistroV1FeedbackReportOut": "_firebaseappdistribution_79_GoogleFirebaseAppdistroV1FeedbackReportOut",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestIn": "_firebaseappdistribution_80_GoogleFirebaseAppdistroV1UploadReleaseRequestIn",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestOut": "_firebaseappdistribution_81_GoogleFirebaseAppdistroV1UploadReleaseRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"])
    types["GdataMediaIn"] = t.struct(
        {
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "path": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "token": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "filename": t.string().optional(),
            "mediaId": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "referenceType": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "algorithm": t.string().optional(),
            "md5Hash": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "length": t.string().optional(),
            "hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "sha1Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "inline": t.string().optional(),
            "blobRef": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "timestamp": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "path": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "token": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "filename": t.string().optional(),
            "mediaId": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "referenceType": t.string().optional(),
            "isPotentialRetry": t.boolean().optional(),
            "algorithm": t.string().optional(),
            "md5Hash": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "length": t.string().optional(),
            "hash": t.string().optional(),
            "crc32cHash": t.integer().optional(),
            "sha1Hash": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "sha256Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "inline": t.string().optional(),
            "blobRef": t.string().optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "timestamp": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"])
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
    types["GdataDiffUploadRequestIn"] = t.struct(
        {
            "objectInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffUploadRequestIn"])
    types["GdataDiffUploadRequestOut"] = t.struct(
        {
            "objectInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "checksumsInfo": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffUploadRequestOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"] = t.struct(
        {"emails": t.array(t.string()).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"])
    types["GoogleFirebaseAppdistroV1TestCertificateIn"] = t.struct(
        {
            "hashSha1": t.string().optional(),
            "hashMd5": t.string().optional(),
            "hashSha256": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateIn"])
    types["GoogleFirebaseAppdistroV1TestCertificateOut"] = t.struct(
        {
            "hashSha1": t.string().optional(),
            "hashMd5": t.string().optional(),
            "hashSha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "blobId": t.string().optional(),
            "readToken": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
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
    types["GoogleFirebaseAppdistroV1GroupIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string()}
    ).named(renames["GoogleFirebaseAppdistroV1GroupIn"])
    types["GoogleFirebaseAppdistroV1GroupOut"] = t.struct(
        {
            "inviteLinkCount": t.integer().optional(),
            "releaseCount": t.integer().optional(),
            "testerCount": t.integer().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1GroupOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
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
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
    types["GoogleFirebaseAppdistroV1TesterIn"] = t.struct(
        {
            "groups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterIn"])
    types["GoogleFirebaseAppdistroV1TesterOut"] = t.struct(
        {
            "lastActivityTime": t.string().optional(),
            "groups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterOut"])
    types["GoogleFirebaseAppdistroV1ListReleasesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1ReleaseIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListReleasesResponseIn"])
    types["GoogleFirebaseAppdistroV1ListReleasesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "releases": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"])
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "md5Hash": t.string().optional(),
            "blobRef": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "crc32cHash": t.integer().optional(),
            "inline": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "path": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "cosmoBinaryReference": t.string().optional(),
            "referenceType": t.string().optional(),
            "length": t.string().optional(),
            "md5Hash": t.string().optional(),
            "blobRef": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"])
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
    types["GoogleFirebaseAppdistroV1ReleaseNotesIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesIn"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"])
    types["GoogleFirebaseAppdistroV1ListTestersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterIn"])
            ).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1ListTestersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "testers": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListTestersResponseOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
            "buildVersion": t.string().optional(),
            "name": t.string().optional(),
            "binaryDownloadUri": t.string().optional(),
            "testingUri": t.string().optional(),
            "displayVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectVersion": t.string().optional(),
            "chunkSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
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
    types["GoogleFirebaseAppdistroV1AabInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateIn"]
            ).optional(),
            "integrationState": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoIn"])
    types["GoogleFirebaseAppdistroV1AabInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateOut"]
            ).optional(),
            "integrationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoOut"])
    types["GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn"] = t.struct(
        {"createMissingTesters": t.boolean().optional(), "emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut"] = t.struct(
        {
            "createMissingTesters": t.boolean().optional(),
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut"])
    types["GoogleFirebaseAppdistroV1FeedbackReportIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
    types["GoogleFirebaseAppdistroV1FeedbackReportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "tester": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "screenshotUri": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"] = t.struct(
        {"blob": t.proxy(renames["GdataMediaIn"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"] = t.struct(
        {
            "blob": t.proxy(renames["GdataMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"])

    functions = {}
    functions["projectsGroupsBatchJoin"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsBatchLeave"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsPatch"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchAdd"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "groups": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchRemove"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "groups": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersList"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "groups": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersPatch"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "groups": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1TesterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsGetAabInfo"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1AabInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesDistribute"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesBatchDelete"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesGet"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesPatch"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesList"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
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
    functions["projectsAppsReleasesOperationsList"] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsGet"] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsCancel"] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsWait"] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsDelete"] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
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
        types=types,
        functions=functions,
    )
