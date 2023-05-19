from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebaseappdistribution() -> Import:
    firebaseappdistribution = HTTPRuntime(
        "https://firebaseappdistribution.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_firebaseappdistribution_1_ErrorResponse",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseIn": "_firebaseappdistribution_2_GoogleFirebaseAppdistroV1UploadReleaseResponseIn",
        "GoogleFirebaseAppdistroV1UploadReleaseResponseOut": "_firebaseappdistribution_3_GoogleFirebaseAppdistroV1UploadReleaseResponseOut",
        "GoogleFirebaseAppdistroV1TesterIn": "_firebaseappdistribution_4_GoogleFirebaseAppdistroV1TesterIn",
        "GoogleFirebaseAppdistroV1TesterOut": "_firebaseappdistribution_5_GoogleFirebaseAppdistroV1TesterOut",
        "GoogleFirebaseAppdistroV1ReleaseIn": "_firebaseappdistribution_6_GoogleFirebaseAppdistroV1ReleaseIn",
        "GoogleFirebaseAppdistroV1ReleaseOut": "_firebaseappdistribution_7_GoogleFirebaseAppdistroV1ReleaseOut",
        "GoogleFirebaseAppdistroV1ReleaseNotesIn": "_firebaseappdistribution_8_GoogleFirebaseAppdistroV1ReleaseNotesIn",
        "GoogleFirebaseAppdistroV1ReleaseNotesOut": "_firebaseappdistribution_9_GoogleFirebaseAppdistroV1ReleaseNotesOut",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn": "_firebaseappdistribution_10_GoogleFirebaseAppdistroV1BatchJoinGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut": "_firebaseappdistribution_11_GoogleFirebaseAppdistroV1BatchJoinGroupRequestOut",
        "GoogleFirebaseAppdistroV1FeedbackReportIn": "_firebaseappdistribution_12_GoogleFirebaseAppdistroV1FeedbackReportIn",
        "GoogleFirebaseAppdistroV1FeedbackReportOut": "_firebaseappdistribution_13_GoogleFirebaseAppdistroV1FeedbackReportOut",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn": "_firebaseappdistribution_14_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseIn",
        "GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut": "_firebaseappdistribution_15_GoogleFirebaseAppdistroV1ListFeedbackReportsResponseOut",
        "GoogleFirebaseAppdistroV1GroupIn": "_firebaseappdistribution_16_GoogleFirebaseAppdistroV1GroupIn",
        "GoogleFirebaseAppdistroV1GroupOut": "_firebaseappdistribution_17_GoogleFirebaseAppdistroV1GroupOut",
        "GoogleProtobufEmptyIn": "_firebaseappdistribution_18_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_firebaseappdistribution_19_GoogleProtobufEmptyOut",
        "GdataBlobstore2InfoIn": "_firebaseappdistribution_20_GdataBlobstore2InfoIn",
        "GdataBlobstore2InfoOut": "_firebaseappdistribution_21_GdataBlobstore2InfoOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseIn": "_firebaseappdistribution_22_GoogleFirebaseAppdistroV1BatchAddTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersResponseOut": "_firebaseappdistribution_23_GoogleFirebaseAppdistroV1BatchAddTestersResponseOut",
        "GoogleFirebaseAppdistroV1AabInfoIn": "_firebaseappdistribution_24_GoogleFirebaseAppdistroV1AabInfoIn",
        "GoogleFirebaseAppdistroV1AabInfoOut": "_firebaseappdistribution_25_GoogleFirebaseAppdistroV1AabInfoOut",
        "GdataDiffVersionResponseIn": "_firebaseappdistribution_26_GdataDiffVersionResponseIn",
        "GdataDiffVersionResponseOut": "_firebaseappdistribution_27_GdataDiffVersionResponseOut",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestIn": "_firebaseappdistribution_28_GoogleFirebaseAppdistroV1BatchAddTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchAddTestersRequestOut": "_firebaseappdistribution_29_GoogleFirebaseAppdistroV1BatchAddTestersRequestOut",
        "GoogleFirebaseAppdistroV1ListGroupsResponseIn": "_firebaseappdistribution_30_GoogleFirebaseAppdistroV1ListGroupsResponseIn",
        "GoogleFirebaseAppdistroV1ListGroupsResponseOut": "_firebaseappdistribution_31_GoogleFirebaseAppdistroV1ListGroupsResponseOut",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn": "_firebaseappdistribution_32_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestIn",
        "GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut": "_firebaseappdistribution_33_GoogleFirebaseAppdistroV1BatchDeleteReleasesRequestOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestIn": "_firebaseappdistribution_34_GoogleFirebaseAppdistroV1DistributeReleaseRequestIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseRequestOut": "_firebaseappdistribution_35_GoogleFirebaseAppdistroV1DistributeReleaseRequestOut",
        "GdataDiffUploadRequestIn": "_firebaseappdistribution_36_GdataDiffUploadRequestIn",
        "GdataDiffUploadRequestOut": "_firebaseappdistribution_37_GdataDiffUploadRequestOut",
        "GoogleFirebaseAppdistroV1ListReleasesResponseIn": "_firebaseappdistribution_38_GoogleFirebaseAppdistroV1ListReleasesResponseIn",
        "GoogleFirebaseAppdistroV1ListReleasesResponseOut": "_firebaseappdistribution_39_GoogleFirebaseAppdistroV1ListReleasesResponseOut",
        "GoogleLongrunningOperationIn": "_firebaseappdistribution_40_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_firebaseappdistribution_41_GoogleLongrunningOperationOut",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestIn": "_firebaseappdistribution_42_GoogleFirebaseAppdistroV1UploadReleaseRequestIn",
        "GoogleFirebaseAppdistroV1UploadReleaseRequestOut": "_firebaseappdistribution_43_GoogleFirebaseAppdistroV1UploadReleaseRequestOut",
        "GdataDiffDownloadResponseIn": "_firebaseappdistribution_44_GdataDiffDownloadResponseIn",
        "GdataDiffDownloadResponseOut": "_firebaseappdistribution_45_GdataDiffDownloadResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_firebaseappdistribution_46_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_firebaseappdistribution_47_GoogleLongrunningListOperationsResponseOut",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn": "_firebaseappdistribution_48_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn",
        "GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut": "_firebaseappdistribution_49_GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataIn": "_firebaseappdistribution_50_GoogleFirebaseAppdistroV1UploadReleaseMetadataIn",
        "GoogleFirebaseAppdistroV1UploadReleaseMetadataOut": "_firebaseappdistribution_51_GoogleFirebaseAppdistroV1UploadReleaseMetadataOut",
        "GdataContentTypeInfoIn": "_firebaseappdistribution_52_GdataContentTypeInfoIn",
        "GdataContentTypeInfoOut": "_firebaseappdistribution_53_GdataContentTypeInfoOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn": "_firebaseappdistribution_54_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut": "_firebaseappdistribution_55_GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut",
        "GdataDiffChecksumsResponseIn": "_firebaseappdistribution_56_GdataDiffChecksumsResponseIn",
        "GdataDiffChecksumsResponseOut": "_firebaseappdistribution_57_GdataDiffChecksumsResponseOut",
        "GoogleRpcStatusIn": "_firebaseappdistribution_58_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_firebaseappdistribution_59_GoogleRpcStatusOut",
        "GoogleFirebaseAppdistroV1ListTestersResponseIn": "_firebaseappdistribution_60_GoogleFirebaseAppdistroV1ListTestersResponseIn",
        "GoogleFirebaseAppdistroV1ListTestersResponseOut": "_firebaseappdistribution_61_GoogleFirebaseAppdistroV1ListTestersResponseOut",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseIn": "_firebaseappdistribution_62_GoogleFirebaseAppdistroV1DistributeReleaseResponseIn",
        "GoogleFirebaseAppdistroV1DistributeReleaseResponseOut": "_firebaseappdistribution_63_GoogleFirebaseAppdistroV1DistributeReleaseResponseOut",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn": "_firebaseappdistribution_64_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn",
        "GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut": "_firebaseappdistribution_65_GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut",
        "GdataMediaIn": "_firebaseappdistribution_66_GdataMediaIn",
        "GdataMediaOut": "_firebaseappdistribution_67_GdataMediaOut",
        "GoogleLongrunningCancelOperationRequestIn": "_firebaseappdistribution_68_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_firebaseappdistribution_69_GoogleLongrunningCancelOperationRequestOut",
        "GoogleFirebaseAppdistroV1TestCertificateIn": "_firebaseappdistribution_70_GoogleFirebaseAppdistroV1TestCertificateIn",
        "GoogleFirebaseAppdistroV1TestCertificateOut": "_firebaseappdistribution_71_GoogleFirebaseAppdistroV1TestCertificateOut",
        "GdataObjectIdIn": "_firebaseappdistribution_72_GdataObjectIdIn",
        "GdataObjectIdOut": "_firebaseappdistribution_73_GdataObjectIdOut",
        "GdataCompositeMediaIn": "_firebaseappdistribution_74_GdataCompositeMediaIn",
        "GdataCompositeMediaOut": "_firebaseappdistribution_75_GdataCompositeMediaOut",
        "GdataDownloadParametersIn": "_firebaseappdistribution_76_GdataDownloadParametersIn",
        "GdataDownloadParametersOut": "_firebaseappdistribution_77_GdataDownloadParametersOut",
        "GoogleLongrunningWaitOperationRequestIn": "_firebaseappdistribution_78_GoogleLongrunningWaitOperationRequestIn",
        "GoogleLongrunningWaitOperationRequestOut": "_firebaseappdistribution_79_GoogleLongrunningWaitOperationRequestOut",
        "GdataDiffUploadResponseIn": "_firebaseappdistribution_80_GdataDiffUploadResponseIn",
        "GdataDiffUploadResponseOut": "_firebaseappdistribution_81_GdataDiffUploadResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "firebaseConsoleUri": t.string().optional(),
            "displayVersion": t.string().optional(),
            "testingUri": t.string().optional(),
            "binaryDownloadUri": t.string().optional(),
            "createTime": t.string().optional(),
            "releaseNotes": t.proxy(
                renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"]
            ).optional(),
            "name": t.string().optional(),
            "buildVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseOut"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesIn"])
    types["GoogleFirebaseAppdistroV1ReleaseNotesOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ReleaseNotesOut"])
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
    types["GoogleFirebaseAppdistroV1FeedbackReportIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportIn"])
    types["GoogleFirebaseAppdistroV1FeedbackReportOut"] = t.struct(
        {
            "firebaseConsoleUri": t.string().optional(),
            "text": t.string().optional(),
            "screenshotUri": t.string().optional(),
            "tester": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1FeedbackReportOut"])
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
    types["GoogleFirebaseAppdistroV1GroupIn"] = t.struct(
        {"name": t.string().optional(), "displayName": t.string()}
    ).named(renames["GoogleFirebaseAppdistroV1GroupIn"])
    types["GoogleFirebaseAppdistroV1GroupOut"] = t.struct(
        {
            "releaseCount": t.integer().optional(),
            "name": t.string().optional(),
            "inviteLinkCount": t.integer().optional(),
            "testerCount": t.integer().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1GroupOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GdataBlobstore2InfoIn"] = t.struct(
        {
            "blobId": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
        }
    ).named(renames["GdataBlobstore2InfoIn"])
    types["GdataBlobstore2InfoOut"] = t.struct(
        {
            "blobId": t.string().optional(),
            "downloadReadHandle": t.string().optional(),
            "blobGeneration": t.string().optional(),
            "uploadMetadataContainer": t.string().optional(),
            "readToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataBlobstore2InfoOut"])
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
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchAddTestersRequestOut"])
    types["GoogleFirebaseAppdistroV1ListGroupsResponseIn"] = t.struct(
        {
            "groups": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1GroupIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListGroupsResponseIn"])
    types["GoogleFirebaseAppdistroV1ListGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(
                t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1ListGroupsResponseOut"])
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
            "testerEmails": t.array(t.string()).optional(),
            "groupAliases": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseRequestOut"] = t.struct(
        {
            "testerEmails": t.array(t.string()).optional(),
            "groupAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseRequestOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"] = t.struct(
        {"blob": t.proxy(renames["GdataMediaIn"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"] = t.struct(
        {
            "blob": t.proxy(renames["GdataMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseRequestOut"])
    types["GdataDiffDownloadResponseIn"] = t.struct(
        {"objectLocation": t.proxy(renames["GdataCompositeMediaIn"]).optional()}
    ).named(renames["GdataDiffDownloadResponseIn"])
    types["GdataDiffDownloadResponseOut"] = t.struct(
        {
            "objectLocation": t.proxy(renames["GdataCompositeMediaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataDiffDownloadResponseOut"])
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
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchLeaveGroupRequestOut"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataIn"])
    types["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1UploadReleaseMetadataOut"])
    types["GdataContentTypeInfoIn"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
        }
    ).named(renames["GdataContentTypeInfoIn"])
    types["GdataContentTypeInfoOut"] = t.struct(
        {
            "bestGuess": t.string().optional(),
            "fromUrlPath": t.string().optional(),
            "fromFileName": t.string().optional(),
            "fromHeader": t.string().optional(),
            "fromBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataContentTypeInfoOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"] = t.struct(
        {"emails": t.array(t.string()).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersResponseOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseIn"])
    types["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleFirebaseAppdistroV1DistributeReleaseResponseOut"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"] = t.struct(
        {"emails": t.array(t.string())}
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestIn"])
    types["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"] = t.struct(
        {
            "emails": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1BatchRemoveTestersRequestOut"])
    types["GdataMediaIn"] = t.struct(
        {
            "length": t.string().optional(),
            "timestamp": t.string().optional(),
            "referenceType": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "hash": t.string().optional(),
            "inline": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "path": t.string().optional(),
            "mediaId": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestIn"]
            ).optional(),
            "blobRef": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoIn"]).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseIn"]
            ).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersIn"]
            ).optional(),
            "filename": t.string().optional(),
            "token": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseIn"]
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "contentType": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseIn"]
            ).optional(),
            "hashVerified": t.boolean().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaIn"])
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "sha1Hash": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseIn"]
            ).optional(),
        }
    ).named(renames["GdataMediaIn"])
    types["GdataMediaOut"] = t.struct(
        {
            "length": t.string().optional(),
            "timestamp": t.string().optional(),
            "referenceType": t.string().optional(),
            "bigstoreObjectRef": t.string().optional(),
            "hash": t.string().optional(),
            "inline": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "path": t.string().optional(),
            "mediaId": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "diffUploadRequest": t.proxy(
                renames["GdataDiffUploadRequestOut"]
            ).optional(),
            "blobRef": t.string().optional(),
            "contentTypeInfo": t.proxy(renames["GdataContentTypeInfoOut"]).optional(),
            "diffUploadResponse": t.proxy(
                renames["GdataDiffUploadResponseOut"]
            ).optional(),
            "downloadParameters": t.proxy(
                renames["GdataDownloadParametersOut"]
            ).optional(),
            "filename": t.string().optional(),
            "token": t.string().optional(),
            "md5Hash": t.string().optional(),
            "diffDownloadResponse": t.proxy(
                renames["GdataDiffDownloadResponseOut"]
            ).optional(),
            "crc32cHash": t.integer().optional(),
            "algorithm": t.string().optional(),
            "contentType": t.string().optional(),
            "diffChecksumsResponse": t.proxy(
                renames["GdataDiffChecksumsResponseOut"]
            ).optional(),
            "hashVerified": t.boolean().optional(),
            "compositeMedia": t.array(
                t.proxy(renames["GdataCompositeMediaOut"])
            ).optional(),
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "isPotentialRetry": t.boolean().optional(),
            "sha1Hash": t.string().optional(),
            "diffVersionResponse": t.proxy(
                renames["GdataDiffVersionResponseOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataMediaOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleFirebaseAppdistroV1TestCertificateIn"] = t.struct(
        {
            "hashMd5": t.string().optional(),
            "hashSha256": t.string().optional(),
            "hashSha1": t.string().optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateIn"])
    types["GoogleFirebaseAppdistroV1TestCertificateOut"] = t.struct(
        {
            "hashMd5": t.string().optional(),
            "hashSha256": t.string().optional(),
            "hashSha1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleFirebaseAppdistroV1TestCertificateOut"])
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
    types["GdataCompositeMediaIn"] = t.struct(
        {
            "objectId": t.proxy(renames["GdataObjectIdIn"]).optional(),
            "length": t.string().optional(),
            "inline": t.string().optional(),
            "referenceType": t.string().optional(),
            "path": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoIn"]).optional(),
            "crc32cHash": t.integer().optional(),
        }
    ).named(renames["GdataCompositeMediaIn"])
    types["GdataCompositeMediaOut"] = t.struct(
        {
            "objectId": t.proxy(renames["GdataObjectIdOut"]).optional(),
            "length": t.string().optional(),
            "inline": t.string().optional(),
            "referenceType": t.string().optional(),
            "path": t.string().optional(),
            "sha1Hash": t.string().optional(),
            "md5Hash": t.string().optional(),
            "cosmoBinaryReference": t.string().optional(),
            "blobRef": t.string().optional(),
            "blobstore2Info": t.proxy(renames["GdataBlobstore2InfoOut"]).optional(),
            "crc32cHash": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GdataCompositeMediaOut"])
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
    types["GoogleLongrunningWaitOperationRequestIn"] = t.struct(
        {"timeout": t.string().optional()}
    ).named(renames["GoogleLongrunningWaitOperationRequestIn"])
    types["GoogleLongrunningWaitOperationRequestOut"] = t.struct(
        {
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningWaitOperationRequestOut"])
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

    functions = {}
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleFirebaseAppdistroV1ListReleasesResponseOut"]),
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
    functions["projectsAppsReleasesOperationsGet"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
        "projectsAppsReleasesFeedbackReportsList"
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
    functions["projectsGroupsPatch"] = firebaseappdistribution.get(
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
    functions["projectsGroupsDelete"] = firebaseappdistribution.get(
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
    functions["projectsGroupsList"] = firebaseappdistribution.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleFirebaseAppdistroV1GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGroupsBatchJoin"] = firebaseappdistribution.get(
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
