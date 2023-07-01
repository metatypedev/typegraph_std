from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebaseappdistribution():
    firebaseappdistribution = HTTPRuntime(
        "https://firebaseappdistribution.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_firebaseappdistribution_1_ErrorResponse",
        "GoogleLongrunningOperationIn": "_firebaseappdistribution_2_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firebaseappdistribution_3_GoogleLongrunningOperationOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firebaseappdistribution_4_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firebaseappdistribution_5_GoogleLongrunningCancelOperationRequestOut",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestIn": "_firebaseappdistribution_6_GoogleFirebaseAppdistroV1UploadReleaseRequestIn",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestOut": "_firebaseappdistribution_7_GoogleFirebaseAppdistroV1UploadReleaseRequestOut",
        "GoogleFirebaseAppdistroV1AabInfoIn": "_firebaseappdistribution_8_GoogleFirebaseAppdistroV1AabInfoIn",
        "GoogleFirebaseAppdistroV1AabInfoOut": "_firebaseappdistribution_9_GoogleFirebaseAppdistroV1AabInfoOut",
        "GoogleFirebaseAppdistroV1ListReleasesResponseIn": "_firebaseappdistribution_10_GoogleFirebaseAppdistroV1ListReleasesResponseIn",
        "GoogleFirebaseAppdistroV1ListReleasesResponseOut": "_firebaseappdistribution_11_GoogleFirebaseAppdistroV1ListReleasesResponseOut",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataIn": "_firebaseappdistribution_12_GoogleFirebaseAppdistroV1UploadReleaseMetadataIn",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataOut": "_firebaseappdistribution_13_GoogleFirebaseAppdistroV1UploadReleaseMetadataOut",
        "GoogleFirebaseAppdistroV1ListTestersResponseIn": "_firebaseappdistribution_14_GoogleFirebaseAppdistroV1ListTestersResponseIn",
        "GoogleFirebaseAppdistroV1ListTestersResponseOut": "_firebaseappdistribution_15_GoogleFirebaseAppdistroV1ListTestersResponseOut",
        "GdataDiffUploadRequestIn": "_firebaseappdistribution_16_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_firebaseappdistribution_17_GdataDiffUploadRequestOut",
        "GoogleFirebaseAppdistroV1TestCertificateIn": "_firebaseappdistribution_18_GoogleFirebaseAppdistroV1TestCertificateIn",
        "GoogleFirebaseAppdistroV1TestCertificateOut": "_firebaseappdistribution_19_GoogleFirebaseAppdistroV1TestCertificateOut",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn": "_firebaseappdistribution_20_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut": "_firebaseappdistribution_21_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut",
        "GdataDiffVersionResponseIn": "_firebaseappdistribution_22_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_firebaseappdistribution_23_GdataDiffVersionResponseOut",
        "GoogleLongrunningWaitOperationRequestIn": "_firebaseappdistribution_24_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_firebaseappdistribution_25_GoogleLongrunningWaitOperationRequestOut",
        "GoogleFirebaseAppdistroV1ListGroupsResponseIn": "_firebaseappdistribution_26_GoogleFirebaseAppdistroV1ListGroupsResponseIn",
        "GoogleFirebaseAppdistroV1ListGroupsResponseOut": "_firebaseappdistribution_27_GoogleFirebaseAppdistroV1ListGroupsResponseOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestIn": "_firebaseappdistribution_28_GoogleFirebaseAppdistroV1DistributeReleaseRequestIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestOut": "_firebaseappdistribution_29_GoogleFirebaseAppdistroV1DistributeReleaseRequestOut",
        "GdataCompositeMediaIn": "_firebaseappdistribution_30_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_firebaseappdistribution_31_GdataCompositeMediaOut",
        "GdataDiffChecksumsResponseIn": "_firebaseappdistribution_32_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_firebaseappdistribution_33_GdataDiffChecksumsResponseOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestIn": "_firebaseappdistribution_34_GoogleFirebaseAppdistroV1BatchAddTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestOut": "_firebaseappdistribution_35_GoogleFirebaseAppdistroV1BatchAddTestersRequestOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn": "_firebaseappdistribution_36_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut": "_firebaseappdistribution_37_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseIn": "_firebaseappdistribution_38_GoogleFirebaseAppdistroV1UploadReleaseResponseIn",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseOut": "_firebaseappdistribution_39_GoogleFirebaseAppdistroV1UploadReleaseResponseOut",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn": "_firebaseappdistribution_40_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut": "_firebaseappdistribution_41_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut",
        "GoogleFirebaseAppdistroV1GroupIn": "_firebaseappdistribution_42_GoogleFirebaseAppdistroV1GroupIn",
        "GoogleFirebaseAppdistroV1GroupOut": "_firebaseappdistribution_43_GoogleFirebaseAppdistroV1GroupOut",
        "GdataDiffDownloadResponseIn": "_firebaseappdistribution_44_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_firebaseappdistribution_45_GdataDiffDownloadResponseOut",
        "GdataDownloadParametersIn": "_firebaseappdistribution_46_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_firebaseappdistribution_47_GdataDownloadParametersOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn": "_firebaseappdistribution_48_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut": "_firebaseappdistribution_49_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut",
        "GdataDiffUploadResponseIn": "_firebaseappdistribution_50_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_firebaseappdistribution_51_GdataDiffUploadResponseOut",
        "GoogleFirebaseAppdistroV1TesterIn": "_firebaseappdistribution_52_GoogleFirebaseAppdistroV1TesterIn",
        "GoogleFirebaseAppdistroV1TesterOut": "_firebaseappdistribution_53_GoogleFirebaseAppdistroV1TesterOut",
        "GoogleProtobufEmptyIn": "_firebaseappdistribution_54_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_firebaseappdistribution_55_GoogleProtobufEmptyOut",
        "GoogleRpcStatusIn": "_firebaseappdistribution_56_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_firebaseappdistribution_57_GoogleRpcStatusOut",
        "GoogleFirebaseAppdistroV1FeedbackReportIn": "_firebaseappdistribution_58_GoogleFirebaseAppdistroV1FeedbackReportIn",
        "GoogleFirebaseAppdistroV1FeedbackReportOut": "_firebaseappdistribution_59_GoogleFirebaseAppdistroV1FeedbackReportOut",
        "GoogleFirebaseAppdistroV1ReleaseNotesIn": "_firebaseappdistribution_60_GoogleFirebaseAppdistroV1ReleaseNotesIn",
        "GoogleFirebaseAppdistroV1ReleaseNotesOut": "_firebaseappdistribution_61_GoogleFirebaseAppdistroV1ReleaseNotesOut",
        "GdataBlobstore2InfoIn": "_firebaseappdistribution_62_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_firebaseappdistribution_63_GdataBlobstore2InfoOut",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn": "_firebaseappdistribution_64_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut": "_firebaseappdistribution_65_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut",
        "GdataObjectIdIn": "_firebaseappdistribution_66_GdataObjectIdIn",
        "GdataObjectIdOut": "_firebaseappdistribution_67_GdataObjectIdOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseIn": "_firebaseappdistribution_68_GoogleFirebaseAppdistroV1BatchAddTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseOut": "_firebaseappdistribution_69_GoogleFirebaseAppdistroV1BatchAddTestersResponseOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseIn": "_firebaseappdistribution_70_GoogleFirebaseAppdistroV1DistributeReleaseResponseIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseOut": "_firebaseappdistribution_71_GoogleFirebaseAppdistroV1DistributeReleaseResponseOut",
        "GdataContentTypeInfoIn": "_firebaseappdistribution_72_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_firebaseappdistribution_73_GdataContentTypeInfoOut",
        "GoogleLongrunningListOperationsResponseIn": "_firebaseappdistribution_74_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firebaseappdistribution_75_GoogleLongrunningListOperationsResponseOut",
        "GdataMediaIn": "_firebaseappdistribution_76_GdataMediaIn",
        "GdataMediaOut": "_firebaseappdistribution_77_GdataMediaOut",
        "GoogleFirebaseAppdistroV1ReleaseIn": "_firebaseappdistribution_78_GoogleFirebaseAppdistroV1ReleaseIn",
        "GoogleFirebaseAppdistroV1ReleaseOut": "_firebaseappdistribution_79_GoogleFirebaseAppdistroV1ReleaseOut",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn": "_firebaseappdistribution_80_GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut": "_firebaseappdistribution_81_GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"] = t.struct(
        {"blob": t.proxy(renames["GdataMediaIn"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"] = t.struct(
        {
            "blob": t.proxy(renames["GdataMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"])
    types["GoogleFirebaseAppdistroV1AabInfoIn"] = t.struct(
        {
            "integrationState": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateIn"]
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoIn"])
    types["GoogleFirebaseAppdistroV1AabInfoOut"] = t.struct(
        {
            "integrationState": t.string().optional(),
            "testCertificate": t.proxy(
                renames["GoogleFirebaseAppdistroV1TestCertificateOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1AabInfoOut"])
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
    types["GoogleFirebaseAppdistroV1TestCertificateIn"] = t.struct(
        {
            "hashMd5": t.string().optional(),
            "hashSha1": t.string().optional(),
            "hashSha256": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateIn"])
    types["GoogleFirebaseAppdistroV1TestCertificateOut"] = t.struct(
        {
            "hashMd5": t.string().optional(),
            "hashSha1": t.string().optional(),
            "hashSha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateOut"])
    types["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn"] = t.struct(
        {
            "feedbackReports": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn"])
    types["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut"] = t.struct(
        {
            "feedbackReports": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut"])
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
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
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
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "path": t.string().optional(),
            "blobRef": t.string().optional(),
            "inline": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "length": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "crc32cHash": t.integer().optional(),
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "path": t.string().optional(),
            "blobRef": t.string().optional(),
            "inline": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "length": t.string().optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "crc32cHash": t.integer().optional(),
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "referenceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
    types["GdataDiffChecksumsResponseIn"] = t.struct(
        {
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseIn"])
    types["GdataDiffChecksumsResponseOut"] = t.struct(
        {
            "chunkSizeBytes": t.string().optional(),
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "checksumsLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "objectSizeBytes": t.string().optional(),
            "objectVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffChecksumsResponseOut"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"] = t.struct(
        {"emails": t.array(t.string()).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"])
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
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"])
    types["GoogleFirebaseAppdistroV1GroupIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string()}
    ).named(renames["GoogleFirebaseAppdistroV1GroupIn"])
    types["GoogleFirebaseAppdistroV1GroupOut"] = t.struct(
        {
            "releaseCount": t.integer().optional(),
            "name": t.string().optional(),
            "testerCount": t.integer().optional(),
            "inviteLinkCount": t.integer().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1GroupOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
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
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"])
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
    types["GoogleFirebaseAppdistroV1TesterIn"] = t.struct(
        {
            "groups": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterIn"])
    types["GoogleFirebaseAppdistroV1TesterOut"] = t.struct(
        {
            "groups": t.array(t.string()).optional(),
            "lastActivityTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TesterOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleFirebaseAppdistroV1FeedbackReportIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
    types["GoogleFirebaseAppdistroV1FeedbackReportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "tester": t.string().optional(),
            "text": t.string().optional(),
            "screenshotUri": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesIn"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"])
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "readToken": t.string().optional(),
            "blobId": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "readToken": t.string().optional(),
            "blobId": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"] = t.struct(
        {"names": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut"])
    types["GdataObjectIdIn"] = t.struct(
        {
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["GdataObjectIdIn"])
    types["GdataObjectIdOut"] = t.struct(
        {
            "objectName": t.string().optional(),
            "bucketName": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataObjectIdOut"])
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
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "fromHeader": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "bestGuess": t.string().optional(),
            "fromBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
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
    types["GdataMediaIn"] = t.struct(
        {
            "cosmoBinaryReference": t.string().optional(),
            "contentType": t.string().optional(),
            "blobRef": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "path": t.string().optional(),
            "timestamp": t.string().optional(),
            "token": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "mediaId": t.string().optional(),
            "filename": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "length": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "sha1Hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "sha256Hash": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "referenceType": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "cosmoBinaryReference": t.string().optional(),
            "contentType": t.string().optional(),
            "blobRef": t.string().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "path": t.string().optional(),
            "timestamp": t.string().optional(),
            "token": t.string().optional(),
            "hashVerified": t.boolean().optional(),
            "mediaId": t.string().optional(),
            "filename": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "inline": t.string().optional(),
            "md5Hash": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "length": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "sha1Hash": t.string().optional(),
            "algorithm": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "sha256Hash": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "referenceType": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
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
            "createTime": t.string().optional(),
            "releaseNotes": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"]
            ).optional(),
            "displayVersion": t.string().optional(),
            "testingUri": t.string().optional(),
            "buildVersion": t.string().optional(),
            "binaryDownloadUri": t.string().optional(),
            "firebaseConsoleUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
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

    functions = {}
    functions["projectsGroupsBatchLeave"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsDelete"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsGet"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsList"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsCreate"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsBatchJoin"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsPatch"] = firebaseappdistribution.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "displayName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersPatch"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchAdd",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersList"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchAdd",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchRemove"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchAdd",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestersBatchAdd"] = firebaseappdistribution.post(
        "v1/{project}/testers:batchAdd",
        t.struct(
            {
                "project": t.string(),
                "emails": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1BatchAddTestersResponseOut"]),
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
    functions["projectsAppsReleasesBatchDelete"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesDistribute"] = firebaseappdistribution.get(
        "v1/{parent}/releases",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsCancel"] = firebaseappdistribution.post(
        "v1/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsList"] = firebaseappdistribution.post(
        "v1/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsGet"] = firebaseappdistribution.post(
        "v1/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsDelete"] = firebaseappdistribution.post(
        "v1/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAppsReleasesOperationsWait"] = firebaseappdistribution.post(
        "v1/{name}:wait",
        t.struct(
            {
                "name": t.string().optional(),
                "timeout": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAppsReleasesFeedbackReportsList"
    ] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAppsReleasesFeedbackReportsGet"
    ] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAppsReleasesFeedbackReportsDelete"
    ] = firebaseappdistribution.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
        types=Box(types),
        functions=Box(functions),
    )
