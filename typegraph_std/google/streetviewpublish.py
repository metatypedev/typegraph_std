from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_streetviewpublish() -> Import:
    streetviewpublish = HTTPRuntime("https://streetviewpublish.googleapis.com/")

    renames = {
        "ErrorResponse": "_streetviewpublish_1_ErrorResponse",
        "PhotoIn": "_streetviewpublish_2_PhotoIn",
        "PhotoOut": "_streetviewpublish_3_PhotoOut",
        "EmptyIn": "_streetviewpublish_4_EmptyIn",
        "EmptyOut": "_streetviewpublish_5_EmptyOut",
        "BatchGetPhotosResponseIn": "_streetviewpublish_6_BatchGetPhotosResponseIn",
        "BatchGetPhotosResponseOut": "_streetviewpublish_7_BatchGetPhotosResponseOut",
        "PhotoSequenceIn": "_streetviewpublish_8_PhotoSequenceIn",
        "PhotoSequenceOut": "_streetviewpublish_9_PhotoSequenceOut",
        "ImuIn": "_streetviewpublish_10_ImuIn",
        "ImuOut": "_streetviewpublish_11_ImuOut",
        "BatchDeletePhotosResponseIn": "_streetviewpublish_12_BatchDeletePhotosResponseIn",
        "BatchDeletePhotosResponseOut": "_streetviewpublish_13_BatchDeletePhotosResponseOut",
        "BatchUpdatePhotosResponseIn": "_streetviewpublish_14_BatchUpdatePhotosResponseIn",
        "BatchUpdatePhotosResponseOut": "_streetviewpublish_15_BatchUpdatePhotosResponseOut",
        "StatusIn": "_streetviewpublish_16_StatusIn",
        "StatusOut": "_streetviewpublish_17_StatusOut",
        "PlaceIn": "_streetviewpublish_18_PlaceIn",
        "PlaceOut": "_streetviewpublish_19_PlaceOut",
        "ConnectionIn": "_streetviewpublish_20_ConnectionIn",
        "ConnectionOut": "_streetviewpublish_21_ConnectionOut",
        "LevelIn": "_streetviewpublish_22_LevelIn",
        "LevelOut": "_streetviewpublish_23_LevelOut",
        "NotOutdoorsFailureDetailsIn": "_streetviewpublish_24_NotOutdoorsFailureDetailsIn",
        "NotOutdoorsFailureDetailsOut": "_streetviewpublish_25_NotOutdoorsFailureDetailsOut",
        "BatchUpdatePhotosRequestIn": "_streetviewpublish_26_BatchUpdatePhotosRequestIn",
        "BatchUpdatePhotosRequestOut": "_streetviewpublish_27_BatchUpdatePhotosRequestOut",
        "UploadRefIn": "_streetviewpublish_28_UploadRefIn",
        "UploadRefOut": "_streetviewpublish_29_UploadRefOut",
        "BatchDeletePhotosRequestIn": "_streetviewpublish_30_BatchDeletePhotosRequestIn",
        "BatchDeletePhotosRequestOut": "_streetviewpublish_31_BatchDeletePhotosRequestOut",
        "ImuDataGapFailureDetailsIn": "_streetviewpublish_32_ImuDataGapFailureDetailsIn",
        "ImuDataGapFailureDetailsOut": "_streetviewpublish_33_ImuDataGapFailureDetailsOut",
        "ListPhotoSequencesResponseIn": "_streetviewpublish_34_ListPhotoSequencesResponseIn",
        "ListPhotoSequencesResponseOut": "_streetviewpublish_35_ListPhotoSequencesResponseOut",
        "OperationIn": "_streetviewpublish_36_OperationIn",
        "OperationOut": "_streetviewpublish_37_OperationOut",
        "UpdatePhotoRequestIn": "_streetviewpublish_38_UpdatePhotoRequestIn",
        "UpdatePhotoRequestOut": "_streetviewpublish_39_UpdatePhotoRequestOut",
        "ProcessingFailureDetailsIn": "_streetviewpublish_40_ProcessingFailureDetailsIn",
        "ProcessingFailureDetailsOut": "_streetviewpublish_41_ProcessingFailureDetailsOut",
        "PoseIn": "_streetviewpublish_42_PoseIn",
        "PoseOut": "_streetviewpublish_43_PoseOut",
        "PhotoIdIn": "_streetviewpublish_44_PhotoIdIn",
        "PhotoIdOut": "_streetviewpublish_45_PhotoIdOut",
        "NoOverlapGpsFailureDetailsIn": "_streetviewpublish_46_NoOverlapGpsFailureDetailsIn",
        "NoOverlapGpsFailureDetailsOut": "_streetviewpublish_47_NoOverlapGpsFailureDetailsOut",
        "LatLngBoundsIn": "_streetviewpublish_48_LatLngBoundsIn",
        "LatLngBoundsOut": "_streetviewpublish_49_LatLngBoundsOut",
        "LatLngIn": "_streetviewpublish_50_LatLngIn",
        "LatLngOut": "_streetviewpublish_51_LatLngOut",
        "InsufficientGpsFailureDetailsIn": "_streetviewpublish_52_InsufficientGpsFailureDetailsIn",
        "InsufficientGpsFailureDetailsOut": "_streetviewpublish_53_InsufficientGpsFailureDetailsOut",
        "GpsDataGapFailureDetailsIn": "_streetviewpublish_54_GpsDataGapFailureDetailsIn",
        "GpsDataGapFailureDetailsOut": "_streetviewpublish_55_GpsDataGapFailureDetailsOut",
        "PhotoResponseIn": "_streetviewpublish_56_PhotoResponseIn",
        "PhotoResponseOut": "_streetviewpublish_57_PhotoResponseOut",
        "ListPhotosResponseIn": "_streetviewpublish_58_ListPhotosResponseIn",
        "ListPhotosResponseOut": "_streetviewpublish_59_ListPhotosResponseOut",
        "Measurement3dIn": "_streetviewpublish_60_Measurement3dIn",
        "Measurement3dOut": "_streetviewpublish_61_Measurement3dOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PhotoIn"] = t.struct(
        {
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "pose": t.proxy(renames["PoseIn"]).optional(),
            "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
            "captureTime": t.string().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "thumbnailUrl": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "transferStatus": t.string().optional(),
            "mapsPublishStatus": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "photoId": t.proxy(renames["PhotoIdOut"]),
            "uploadTime": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "pose": t.proxy(renames["PoseOut"]).optional(),
            "places": t.array(t.proxy(renames["PlaceOut"])).optional(),
            "shareLink": t.string().optional(),
            "viewCount": t.string().optional(),
            "captureTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchGetPhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchGetPhotosResponseIn"])
    types["BatchGetPhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetPhotosResponseOut"])
    types["PhotoSequenceIn"] = t.struct(
        {
            "imu": t.proxy(renames["ImuIn"]).optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
            "captureTimeOverride": t.string().optional(),
            "gpsSource": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
        }
    ).named(renames["PhotoSequenceIn"])
    types["PhotoSequenceOut"] = t.struct(
        {
            "filename": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "viewCount": t.string().optional(),
            "imu": t.proxy(renames["ImuOut"]).optional(),
            "failureDetails": t.proxy(
                renames["ProcessingFailureDetailsOut"]
            ).optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseOut"])).optional(),
            "id": t.string().optional(),
            "processingState": t.string().optional(),
            "captureTimeOverride": t.string().optional(),
            "sequenceBounds": t.proxy(renames["LatLngBoundsOut"]).optional(),
            "gpsSource": t.string().optional(),
            "distanceMeters": t.number().optional(),
            "uploadTime": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoSequenceOut"])
    types["ImuIn"] = t.struct(
        {
            "gyroRps": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
            "accelMpsps": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
            "magUt": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
        }
    ).named(renames["ImuIn"])
    types["ImuOut"] = t.struct(
        {
            "gyroRps": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "accelMpsps": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "magUt": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImuOut"])
    types["BatchDeletePhotosResponseIn"] = t.struct(
        {"status": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BatchDeletePhotosResponseIn"])
    types["BatchDeletePhotosResponseOut"] = t.struct(
        {
            "status": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosResponseOut"])
    types["BatchUpdatePhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchUpdatePhotosResponseIn"])
    types["BatchUpdatePhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["PlaceIn"] = t.struct({"placeId": t.string().optional()}).named(
        renames["PlaceIn"]
    )
    types["PlaceOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "placeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceOut"])
    types["ConnectionIn"] = t.struct({"target": t.proxy(renames["PhotoIdIn"])}).named(
        renames["ConnectionIn"]
    )
    types["ConnectionOut"] = t.struct(
        {
            "target": t.proxy(renames["PhotoIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["LevelIn"] = t.struct(
        {"name": t.string(), "number": t.number().optional()}
    ).named(renames["LevelIn"])
    types["LevelOut"] = t.struct(
        {
            "name": t.string(),
            "number": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LevelOut"])
    types["NotOutdoorsFailureDetailsIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["NotOutdoorsFailureDetailsIn"])
    types["NotOutdoorsFailureDetailsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotOutdoorsFailureDetailsOut"])
    types["BatchUpdatePhotosRequestIn"] = t.struct(
        {"updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestIn"]))}
    ).named(renames["BatchUpdatePhotosRequestIn"])
    types["BatchUpdatePhotosRequestOut"] = t.struct(
        {
            "updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosRequestOut"])
    types["UploadRefIn"] = t.struct({"uploadUrl": t.string().optional()}).named(
        renames["UploadRefIn"]
    )
    types["UploadRefOut"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadRefOut"])
    types["BatchDeletePhotosRequestIn"] = t.struct(
        {"photoIds": t.array(t.string())}
    ).named(renames["BatchDeletePhotosRequestIn"])
    types["BatchDeletePhotosRequestOut"] = t.struct(
        {
            "photoIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosRequestOut"])
    types["ImuDataGapFailureDetailsIn"] = t.struct(
        {"gapStartTime": t.string().optional(), "gapDuration": t.string().optional()}
    ).named(renames["ImuDataGapFailureDetailsIn"])
    types["ImuDataGapFailureDetailsOut"] = t.struct(
        {
            "gapStartTime": t.string().optional(),
            "gapDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImuDataGapFailureDetailsOut"])
    types["ListPhotoSequencesResponseIn"] = t.struct(
        {
            "photoSequences": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPhotoSequencesResponseIn"])
    types["ListPhotoSequencesResponseOut"] = t.struct(
        {
            "photoSequences": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhotoSequencesResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["UpdatePhotoRequestIn"] = t.struct(
        {"photo": t.proxy(renames["PhotoIn"]), "updateMask": t.string()}
    ).named(renames["UpdatePhotoRequestIn"])
    types["UpdatePhotoRequestOut"] = t.struct(
        {
            "photo": t.proxy(renames["PhotoOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePhotoRequestOut"])
    types["ProcessingFailureDetailsIn"] = t.struct(
        {
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsIn"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsIn"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsIn"]
            ).optional(),
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsIn"]
            ).optional(),
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsIn"]
            ).optional(),
        }
    ).named(renames["ProcessingFailureDetailsIn"])
    types["ProcessingFailureDetailsOut"] = t.struct(
        {
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsOut"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsOut"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsOut"]
            ).optional(),
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsOut"]
            ).optional(),
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingFailureDetailsOut"])
    types["PoseIn"] = t.struct(
        {
            "accuracyMeters": t.number().optional(),
            "heading": t.number().optional(),
            "altitude": t.number().optional(),
            "roll": t.number().optional(),
            "pitch": t.number().optional(),
            "level": t.proxy(renames["LevelIn"]).optional(),
            "latLngPair": t.proxy(renames["LatLngIn"]).optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
        }
    ).named(renames["PoseIn"])
    types["PoseOut"] = t.struct(
        {
            "accuracyMeters": t.number().optional(),
            "heading": t.number().optional(),
            "altitude": t.number().optional(),
            "roll": t.number().optional(),
            "pitch": t.number().optional(),
            "level": t.proxy(renames["LevelOut"]).optional(),
            "latLngPair": t.proxy(renames["LatLngOut"]).optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoseOut"])
    types["PhotoIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["PhotoIdIn"]
    )
    types["PhotoIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoIdOut"])
    types["NoOverlapGpsFailureDetailsIn"] = t.struct(
        {
            "gpsStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "videoStartTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsIn"])
    types["NoOverlapGpsFailureDetailsOut"] = t.struct(
        {
            "gpsStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "videoStartTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsOut"])
    types["LatLngBoundsIn"] = t.struct(
        {
            "northeast": t.proxy(renames["LatLngIn"]).optional(),
            "southwest": t.proxy(renames["LatLngIn"]).optional(),
        }
    ).named(renames["LatLngBoundsIn"])
    types["LatLngBoundsOut"] = t.struct(
        {
            "northeast": t.proxy(renames["LatLngOut"]).optional(),
            "southwest": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngBoundsOut"])
    types["LatLngIn"] = t.struct(
        {"latitude": t.number().optional(), "longitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["InsufficientGpsFailureDetailsIn"] = t.struct(
        {"gpsPointsFound": t.integer().optional()}
    ).named(renames["InsufficientGpsFailureDetailsIn"])
    types["InsufficientGpsFailureDetailsOut"] = t.struct(
        {
            "gpsPointsFound": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsufficientGpsFailureDetailsOut"])
    types["GpsDataGapFailureDetailsIn"] = t.struct(
        {"gapDuration": t.string().optional(), "gapStartTime": t.string().optional()}
    ).named(renames["GpsDataGapFailureDetailsIn"])
    types["GpsDataGapFailureDetailsOut"] = t.struct(
        {
            "gapDuration": t.string().optional(),
            "gapStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GpsDataGapFailureDetailsOut"])
    types["PhotoResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "photo": t.proxy(renames["PhotoIn"]).optional(),
        }
    ).named(renames["PhotoResponseIn"])
    types["PhotoResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "photo": t.proxy(renames["PhotoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoResponseOut"])
    types["ListPhotosResponseIn"] = t.struct(
        {
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPhotosResponseIn"])
    types["ListPhotosResponseOut"] = t.struct(
        {
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhotosResponseOut"])
    types["Measurement3dIn"] = t.struct(
        {
            "captureTime": t.string().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
        }
    ).named(renames["Measurement3dIn"])
    types["Measurement3dOut"] = t.struct(
        {
            "captureTime": t.string().optional(),
            "z": t.number().optional(),
            "x": t.number().optional(),
            "y": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Measurement3dOut"])

    functions = {}
    functions["photoSequencesList"] = streetviewpublish.get(
        "v1/photoSequences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhotoSequencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosList"] = streetviewpublish.post(
        "v1/photos:batchDelete",
        t.struct({"photoIds": t.array(t.string()), "auth": t.string().optional()}),
        t.proxy(renames["BatchDeletePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchGet"] = streetviewpublish.post(
        "v1/photos:batchDelete",
        t.struct({"photoIds": t.array(t.string()), "auth": t.string().optional()}),
        t.proxy(renames["BatchDeletePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchUpdate"] = streetviewpublish.post(
        "v1/photos:batchDelete",
        t.struct({"photoIds": t.array(t.string()), "auth": t.string().optional()}),
        t.proxy(renames["BatchDeletePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchDelete"] = streetviewpublish.post(
        "v1/photos:batchDelete",
        t.struct({"photoIds": t.array(t.string()), "auth": t.string().optional()}),
        t.proxy(renames["BatchDeletePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceGet"] = streetviewpublish.delete(
        "v1/photoSequence/{sequenceId}",
        t.struct({"sequenceId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceStartUpload"] = streetviewpublish.delete(
        "v1/photoSequence/{sequenceId}",
        t.struct({"sequenceId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceCreate"] = streetviewpublish.delete(
        "v1/photoSequence/{sequenceId}",
        t.struct({"sequenceId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceDelete"] = streetviewpublish.delete(
        "v1/photoSequence/{sequenceId}",
        t.struct({"sequenceId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoStartUpload"] = streetviewpublish.post(
        "v1/photo",
        t.struct(
            {
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoUpdate"] = streetviewpublish.post(
        "v1/photo",
        t.struct(
            {
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoDelete"] = streetviewpublish.post(
        "v1/photo",
        t.struct(
            {
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoGet"] = streetviewpublish.post(
        "v1/photo",
        t.struct(
            {
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoCreate"] = streetviewpublish.post(
        "v1/photo",
        t.struct(
            {
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="streetviewpublish",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
