from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_streetviewpublish() -> Import:
    streetviewpublish = HTTPRuntime("https://streetviewpublish.googleapis.com/")

    renames = {
        "ErrorResponse": "_streetviewpublish_1_ErrorResponse",
        "InsufficientGpsFailureDetailsIn": "_streetviewpublish_2_InsufficientGpsFailureDetailsIn",
        "InsufficientGpsFailureDetailsOut": "_streetviewpublish_3_InsufficientGpsFailureDetailsOut",
        "PhotoResponseIn": "_streetviewpublish_4_PhotoResponseIn",
        "PhotoResponseOut": "_streetviewpublish_5_PhotoResponseOut",
        "ImuIn": "_streetviewpublish_6_ImuIn",
        "ImuOut": "_streetviewpublish_7_ImuOut",
        "ImuDataGapFailureDetailsIn": "_streetviewpublish_8_ImuDataGapFailureDetailsIn",
        "ImuDataGapFailureDetailsOut": "_streetviewpublish_9_ImuDataGapFailureDetailsOut",
        "UpdatePhotoRequestIn": "_streetviewpublish_10_UpdatePhotoRequestIn",
        "UpdatePhotoRequestOut": "_streetviewpublish_11_UpdatePhotoRequestOut",
        "BatchDeletePhotosResponseIn": "_streetviewpublish_12_BatchDeletePhotosResponseIn",
        "BatchDeletePhotosResponseOut": "_streetviewpublish_13_BatchDeletePhotosResponseOut",
        "NotOutdoorsFailureDetailsIn": "_streetviewpublish_14_NotOutdoorsFailureDetailsIn",
        "NotOutdoorsFailureDetailsOut": "_streetviewpublish_15_NotOutdoorsFailureDetailsOut",
        "PhotoIdIn": "_streetviewpublish_16_PhotoIdIn",
        "PhotoIdOut": "_streetviewpublish_17_PhotoIdOut",
        "BatchGetPhotosResponseIn": "_streetviewpublish_18_BatchGetPhotosResponseIn",
        "BatchGetPhotosResponseOut": "_streetviewpublish_19_BatchGetPhotosResponseOut",
        "LatLngIn": "_streetviewpublish_20_LatLngIn",
        "LatLngOut": "_streetviewpublish_21_LatLngOut",
        "BatchUpdatePhotosResponseIn": "_streetviewpublish_22_BatchUpdatePhotosResponseIn",
        "BatchUpdatePhotosResponseOut": "_streetviewpublish_23_BatchUpdatePhotosResponseOut",
        "UploadRefIn": "_streetviewpublish_24_UploadRefIn",
        "UploadRefOut": "_streetviewpublish_25_UploadRefOut",
        "ListPhotosResponseIn": "_streetviewpublish_26_ListPhotosResponseIn",
        "ListPhotosResponseOut": "_streetviewpublish_27_ListPhotosResponseOut",
        "BatchDeletePhotosRequestIn": "_streetviewpublish_28_BatchDeletePhotosRequestIn",
        "BatchDeletePhotosRequestOut": "_streetviewpublish_29_BatchDeletePhotosRequestOut",
        "Measurement3dIn": "_streetviewpublish_30_Measurement3dIn",
        "Measurement3dOut": "_streetviewpublish_31_Measurement3dOut",
        "LevelIn": "_streetviewpublish_32_LevelIn",
        "LevelOut": "_streetviewpublish_33_LevelOut",
        "OperationIn": "_streetviewpublish_34_OperationIn",
        "OperationOut": "_streetviewpublish_35_OperationOut",
        "PhotoSequenceIn": "_streetviewpublish_36_PhotoSequenceIn",
        "PhotoSequenceOut": "_streetviewpublish_37_PhotoSequenceOut",
        "PhotoIn": "_streetviewpublish_38_PhotoIn",
        "PhotoOut": "_streetviewpublish_39_PhotoOut",
        "ConnectionIn": "_streetviewpublish_40_ConnectionIn",
        "ConnectionOut": "_streetviewpublish_41_ConnectionOut",
        "PlaceIn": "_streetviewpublish_42_PlaceIn",
        "PlaceOut": "_streetviewpublish_43_PlaceOut",
        "ListPhotoSequencesResponseIn": "_streetviewpublish_44_ListPhotoSequencesResponseIn",
        "ListPhotoSequencesResponseOut": "_streetviewpublish_45_ListPhotoSequencesResponseOut",
        "LatLngBoundsIn": "_streetviewpublish_46_LatLngBoundsIn",
        "LatLngBoundsOut": "_streetviewpublish_47_LatLngBoundsOut",
        "ProcessingFailureDetailsIn": "_streetviewpublish_48_ProcessingFailureDetailsIn",
        "ProcessingFailureDetailsOut": "_streetviewpublish_49_ProcessingFailureDetailsOut",
        "GpsDataGapFailureDetailsIn": "_streetviewpublish_50_GpsDataGapFailureDetailsIn",
        "GpsDataGapFailureDetailsOut": "_streetviewpublish_51_GpsDataGapFailureDetailsOut",
        "EmptyIn": "_streetviewpublish_52_EmptyIn",
        "EmptyOut": "_streetviewpublish_53_EmptyOut",
        "StatusIn": "_streetviewpublish_54_StatusIn",
        "StatusOut": "_streetviewpublish_55_StatusOut",
        "NoOverlapGpsFailureDetailsIn": "_streetviewpublish_56_NoOverlapGpsFailureDetailsIn",
        "NoOverlapGpsFailureDetailsOut": "_streetviewpublish_57_NoOverlapGpsFailureDetailsOut",
        "PoseIn": "_streetviewpublish_58_PoseIn",
        "PoseOut": "_streetviewpublish_59_PoseOut",
        "BatchUpdatePhotosRequestIn": "_streetviewpublish_60_BatchUpdatePhotosRequestIn",
        "BatchUpdatePhotosRequestOut": "_streetviewpublish_61_BatchUpdatePhotosRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["InsufficientGpsFailureDetailsIn"] = t.struct(
        {"gpsPointsFound": t.integer().optional()}
    ).named(renames["InsufficientGpsFailureDetailsIn"])
    types["InsufficientGpsFailureDetailsOut"] = t.struct(
        {
            "gpsPointsFound": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsufficientGpsFailureDetailsOut"])
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
    types["ImuIn"] = t.struct(
        {
            "magUt": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
            "accelMpsps": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
            "gyroRps": t.array(t.proxy(renames["Measurement3dIn"])).optional(),
        }
    ).named(renames["ImuIn"])
    types["ImuOut"] = t.struct(
        {
            "magUt": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "accelMpsps": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "gyroRps": t.array(t.proxy(renames["Measurement3dOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImuOut"])
    types["ImuDataGapFailureDetailsIn"] = t.struct(
        {"gapDuration": t.string().optional(), "gapStartTime": t.string().optional()}
    ).named(renames["ImuDataGapFailureDetailsIn"])
    types["ImuDataGapFailureDetailsOut"] = t.struct(
        {
            "gapDuration": t.string().optional(),
            "gapStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImuDataGapFailureDetailsOut"])
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
    types["BatchDeletePhotosResponseIn"] = t.struct(
        {"status": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BatchDeletePhotosResponseIn"])
    types["BatchDeletePhotosResponseOut"] = t.struct(
        {
            "status": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosResponseOut"])
    types["NotOutdoorsFailureDetailsIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["NotOutdoorsFailureDetailsIn"])
    types["NotOutdoorsFailureDetailsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotOutdoorsFailureDetailsOut"])
    types["PhotoIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["PhotoIdIn"]
    )
    types["PhotoIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoIdOut"])
    types["BatchGetPhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchGetPhotosResponseIn"])
    types["BatchGetPhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetPhotosResponseOut"])
    types["LatLngIn"] = t.struct(
        {"longitude": t.number().optional(), "latitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["BatchUpdatePhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchUpdatePhotosResponseIn"])
    types["BatchUpdatePhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosResponseOut"])
    types["UploadRefIn"] = t.struct({"uploadUrl": t.string().optional()}).named(
        renames["UploadRefIn"]
    )
    types["UploadRefOut"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadRefOut"])
    types["ListPhotosResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoIn"])).optional(),
        }
    ).named(renames["ListPhotosResponseIn"])
    types["ListPhotosResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhotosResponseOut"])
    types["BatchDeletePhotosRequestIn"] = t.struct(
        {"photoIds": t.array(t.string())}
    ).named(renames["BatchDeletePhotosRequestIn"])
    types["BatchDeletePhotosRequestOut"] = t.struct(
        {
            "photoIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosRequestOut"])
    types["Measurement3dIn"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "captureTime": t.string().optional(),
            "x": t.number().optional(),
        }
    ).named(renames["Measurement3dIn"])
    types["Measurement3dOut"] = t.struct(
        {
            "y": t.number().optional(),
            "z": t.number().optional(),
            "captureTime": t.string().optional(),
            "x": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Measurement3dOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["PhotoSequenceIn"] = t.struct(
        {
            "captureTimeOverride": t.string().optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
            "imu": t.proxy(renames["ImuIn"]).optional(),
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "gpsSource": t.string().optional(),
        }
    ).named(renames["PhotoSequenceIn"])
    types["PhotoSequenceOut"] = t.struct(
        {
            "captureTimeOverride": t.string().optional(),
            "id": t.string().optional(),
            "sequenceBounds": t.proxy(renames["LatLngBoundsOut"]).optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseOut"])).optional(),
            "imu": t.proxy(renames["ImuOut"]).optional(),
            "filename": t.string().optional(),
            "failureDetails": t.proxy(
                renames["ProcessingFailureDetailsOut"]
            ).optional(),
            "viewCount": t.string().optional(),
            "processingState": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "distanceMeters": t.number().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "failureReason": t.string().optional(),
            "uploadTime": t.string().optional(),
            "gpsSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoSequenceOut"])
    types["PhotoIn"] = t.struct(
        {
            "pose": t.proxy(renames["PoseIn"]).optional(),
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
            "captureTime": t.string().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "viewCount": t.string().optional(),
            "pose": t.proxy(renames["PoseOut"]).optional(),
            "photoId": t.proxy(renames["PhotoIdOut"]),
            "uploadTime": t.string().optional(),
            "shareLink": t.string().optional(),
            "transferStatus": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "places": t.array(t.proxy(renames["PlaceOut"])).optional(),
            "captureTime": t.string().optional(),
            "thumbnailUrl": t.string().optional(),
            "mapsPublishStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["ConnectionIn"] = t.struct({"target": t.proxy(renames["PhotoIdIn"])}).named(
        renames["ConnectionIn"]
    )
    types["ConnectionOut"] = t.struct(
        {
            "target": t.proxy(renames["PhotoIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["PlaceIn"] = t.struct({"placeId": t.string().optional()}).named(
        renames["PlaceIn"]
    )
    types["PlaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "placeId": t.string().optional(),
            "languageCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceOut"])
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
    types["LatLngBoundsIn"] = t.struct(
        {
            "southwest": t.proxy(renames["LatLngIn"]).optional(),
            "northeast": t.proxy(renames["LatLngIn"]).optional(),
        }
    ).named(renames["LatLngBoundsIn"])
    types["LatLngBoundsOut"] = t.struct(
        {
            "southwest": t.proxy(renames["LatLngOut"]).optional(),
            "northeast": t.proxy(renames["LatLngOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngBoundsOut"])
    types["ProcessingFailureDetailsIn"] = t.struct(
        {
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsIn"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsIn"]
            ).optional(),
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsIn"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsIn"]
            ).optional(),
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsIn"]
            ).optional(),
        }
    ).named(renames["ProcessingFailureDetailsIn"])
    types["ProcessingFailureDetailsOut"] = t.struct(
        {
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsOut"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsOut"]
            ).optional(),
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsOut"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsOut"]
            ).optional(),
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingFailureDetailsOut"])
    types["GpsDataGapFailureDetailsIn"] = t.struct(
        {"gapStartTime": t.string().optional(), "gapDuration": t.string().optional()}
    ).named(renames["GpsDataGapFailureDetailsIn"])
    types["GpsDataGapFailureDetailsOut"] = t.struct(
        {
            "gapStartTime": t.string().optional(),
            "gapDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GpsDataGapFailureDetailsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["NoOverlapGpsFailureDetailsIn"] = t.struct(
        {
            "videoStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "gpsStartTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsIn"])
    types["NoOverlapGpsFailureDetailsOut"] = t.struct(
        {
            "videoStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "gpsStartTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsOut"])
    types["PoseIn"] = t.struct(
        {
            "heading": t.number().optional(),
            "pitch": t.number().optional(),
            "roll": t.number().optional(),
            "altitude": t.number().optional(),
            "accuracyMeters": t.number().optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "latLngPair": t.proxy(renames["LatLngIn"]).optional(),
            "level": t.proxy(renames["LevelIn"]).optional(),
        }
    ).named(renames["PoseIn"])
    types["PoseOut"] = t.struct(
        {
            "heading": t.number().optional(),
            "pitch": t.number().optional(),
            "roll": t.number().optional(),
            "altitude": t.number().optional(),
            "accuracyMeters": t.number().optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "latLngPair": t.proxy(renames["LatLngOut"]).optional(),
            "level": t.proxy(renames["LevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoseOut"])
    types["BatchUpdatePhotosRequestIn"] = t.struct(
        {"updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestIn"]))}
    ).named(renames["BatchUpdatePhotosRequestIn"])
    types["BatchUpdatePhotosRequestOut"] = t.struct(
        {
            "updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosRequestOut"])

    functions = {}
    functions["photoSequencesList"] = streetviewpublish.get(
        "v1/photoSequences",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPhotoSequencesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceGet"] = streetviewpublish.post(
        "v1/photoSequence",
        t.struct(
            {
                "inputType": t.string(),
                "captureTimeOverride": t.string().optional(),
                "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
                "imu": t.proxy(renames["ImuIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "gpsSource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceDelete"] = streetviewpublish.post(
        "v1/photoSequence",
        t.struct(
            {
                "inputType": t.string(),
                "captureTimeOverride": t.string().optional(),
                "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
                "imu": t.proxy(renames["ImuIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "gpsSource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceStartUpload"] = streetviewpublish.post(
        "v1/photoSequence",
        t.struct(
            {
                "inputType": t.string(),
                "captureTimeOverride": t.string().optional(),
                "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
                "imu": t.proxy(renames["ImuIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "gpsSource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceCreate"] = streetviewpublish.post(
        "v1/photoSequence",
        t.struct(
            {
                "inputType": t.string(),
                "captureTimeOverride": t.string().optional(),
                "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
                "imu": t.proxy(renames["ImuIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "gpsSource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoStartUpload"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoGet"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoCreate"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoDelete"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoUpdate"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "id": t.string().optional(),
                "updateMask": t.string(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
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
    functions["photosList"] = streetviewpublish.post(
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

    return Import(
        importer="streetviewpublish", renames=renames, types=types, functions=functions
    )
