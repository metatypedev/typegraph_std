from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_streetviewpublish() -> Import:
    streetviewpublish = HTTPRuntime("https://streetviewpublish.googleapis.com/")

    renames = {
        "ErrorResponse": "_streetviewpublish_1_ErrorResponse",
        "PhotoResponseIn": "_streetviewpublish_2_PhotoResponseIn",
        "PhotoResponseOut": "_streetviewpublish_3_PhotoResponseOut",
        "PlaceIn": "_streetviewpublish_4_PlaceIn",
        "PlaceOut": "_streetviewpublish_5_PlaceOut",
        "PhotoIn": "_streetviewpublish_6_PhotoIn",
        "PhotoOut": "_streetviewpublish_7_PhotoOut",
        "BatchUpdatePhotosRequestIn": "_streetviewpublish_8_BatchUpdatePhotosRequestIn",
        "BatchUpdatePhotosRequestOut": "_streetviewpublish_9_BatchUpdatePhotosRequestOut",
        "LatLngBoundsIn": "_streetviewpublish_10_LatLngBoundsIn",
        "LatLngBoundsOut": "_streetviewpublish_11_LatLngBoundsOut",
        "Measurement3dIn": "_streetviewpublish_12_Measurement3dIn",
        "Measurement3dOut": "_streetviewpublish_13_Measurement3dOut",
        "StatusIn": "_streetviewpublish_14_StatusIn",
        "StatusOut": "_streetviewpublish_15_StatusOut",
        "PoseIn": "_streetviewpublish_16_PoseIn",
        "PoseOut": "_streetviewpublish_17_PoseOut",
        "UpdatePhotoRequestIn": "_streetviewpublish_18_UpdatePhotoRequestIn",
        "UpdatePhotoRequestOut": "_streetviewpublish_19_UpdatePhotoRequestOut",
        "ImuIn": "_streetviewpublish_20_ImuIn",
        "ImuOut": "_streetviewpublish_21_ImuOut",
        "GpsDataGapFailureDetailsIn": "_streetviewpublish_22_GpsDataGapFailureDetailsIn",
        "GpsDataGapFailureDetailsOut": "_streetviewpublish_23_GpsDataGapFailureDetailsOut",
        "ListPhotoSequencesResponseIn": "_streetviewpublish_24_ListPhotoSequencesResponseIn",
        "ListPhotoSequencesResponseOut": "_streetviewpublish_25_ListPhotoSequencesResponseOut",
        "LevelIn": "_streetviewpublish_26_LevelIn",
        "LevelOut": "_streetviewpublish_27_LevelOut",
        "BatchUpdatePhotosResponseIn": "_streetviewpublish_28_BatchUpdatePhotosResponseIn",
        "BatchUpdatePhotosResponseOut": "_streetviewpublish_29_BatchUpdatePhotosResponseOut",
        "NoOverlapGpsFailureDetailsIn": "_streetviewpublish_30_NoOverlapGpsFailureDetailsIn",
        "NoOverlapGpsFailureDetailsOut": "_streetviewpublish_31_NoOverlapGpsFailureDetailsOut",
        "LatLngIn": "_streetviewpublish_32_LatLngIn",
        "LatLngOut": "_streetviewpublish_33_LatLngOut",
        "InsufficientGpsFailureDetailsIn": "_streetviewpublish_34_InsufficientGpsFailureDetailsIn",
        "InsufficientGpsFailureDetailsOut": "_streetviewpublish_35_InsufficientGpsFailureDetailsOut",
        "PhotoSequenceIn": "_streetviewpublish_36_PhotoSequenceIn",
        "PhotoSequenceOut": "_streetviewpublish_37_PhotoSequenceOut",
        "ImuDataGapFailureDetailsIn": "_streetviewpublish_38_ImuDataGapFailureDetailsIn",
        "ImuDataGapFailureDetailsOut": "_streetviewpublish_39_ImuDataGapFailureDetailsOut",
        "ProcessingFailureDetailsIn": "_streetviewpublish_40_ProcessingFailureDetailsIn",
        "ProcessingFailureDetailsOut": "_streetviewpublish_41_ProcessingFailureDetailsOut",
        "UploadRefIn": "_streetviewpublish_42_UploadRefIn",
        "UploadRefOut": "_streetviewpublish_43_UploadRefOut",
        "OperationIn": "_streetviewpublish_44_OperationIn",
        "OperationOut": "_streetviewpublish_45_OperationOut",
        "BatchGetPhotosResponseIn": "_streetviewpublish_46_BatchGetPhotosResponseIn",
        "BatchGetPhotosResponseOut": "_streetviewpublish_47_BatchGetPhotosResponseOut",
        "BatchDeletePhotosRequestIn": "_streetviewpublish_48_BatchDeletePhotosRequestIn",
        "BatchDeletePhotosRequestOut": "_streetviewpublish_49_BatchDeletePhotosRequestOut",
        "ConnectionIn": "_streetviewpublish_50_ConnectionIn",
        "ConnectionOut": "_streetviewpublish_51_ConnectionOut",
        "PhotoIdIn": "_streetviewpublish_52_PhotoIdIn",
        "PhotoIdOut": "_streetviewpublish_53_PhotoIdOut",
        "NotOutdoorsFailureDetailsIn": "_streetviewpublish_54_NotOutdoorsFailureDetailsIn",
        "NotOutdoorsFailureDetailsOut": "_streetviewpublish_55_NotOutdoorsFailureDetailsOut",
        "BatchDeletePhotosResponseIn": "_streetviewpublish_56_BatchDeletePhotosResponseIn",
        "BatchDeletePhotosResponseOut": "_streetviewpublish_57_BatchDeletePhotosResponseOut",
        "EmptyIn": "_streetviewpublish_58_EmptyIn",
        "EmptyOut": "_streetviewpublish_59_EmptyOut",
        "ListPhotosResponseIn": "_streetviewpublish_60_ListPhotosResponseIn",
        "ListPhotosResponseOut": "_streetviewpublish_61_ListPhotosResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PhotoResponseIn"] = t.struct(
        {
            "photo": t.proxy(renames["PhotoIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["PhotoResponseIn"])
    types["PhotoResponseOut"] = t.struct(
        {
            "photo": t.proxy(renames["PhotoOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoResponseOut"])
    types["PlaceIn"] = t.struct({"placeId": t.string().optional()}).named(
        renames["PlaceIn"]
    )
    types["PlaceOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "placeId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceOut"])
    types["PhotoIn"] = t.struct(
        {
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
            "pose": t.proxy(renames["PoseIn"]).optional(),
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "captureTime": t.string().optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "downloadUrl": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "thumbnailUrl": t.string().optional(),
            "places": t.array(t.proxy(renames["PlaceOut"])).optional(),
            "shareLink": t.string().optional(),
            "photoId": t.proxy(renames["PhotoIdOut"]),
            "pose": t.proxy(renames["PoseOut"]).optional(),
            "uploadTime": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "captureTime": t.string().optional(),
            "transferStatus": t.string().optional(),
            "viewCount": t.string().optional(),
            "mapsPublishStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["BatchUpdatePhotosRequestIn"] = t.struct(
        {"updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestIn"]))}
    ).named(renames["BatchUpdatePhotosRequestIn"])
    types["BatchUpdatePhotosRequestOut"] = t.struct(
        {
            "updatePhotoRequests": t.array(t.proxy(renames["UpdatePhotoRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosRequestOut"])
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
    types["Measurement3dIn"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "captureTime": t.string().optional(),
        }
    ).named(renames["Measurement3dIn"])
    types["Measurement3dOut"] = t.struct(
        {
            "x": t.number().optional(),
            "z": t.number().optional(),
            "y": t.number().optional(),
            "captureTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Measurement3dOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["PoseIn"] = t.struct(
        {
            "heading": t.number().optional(),
            "accuracyMeters": t.number().optional(),
            "altitude": t.number().optional(),
            "level": t.proxy(renames["LevelIn"]).optional(),
            "roll": t.number().optional(),
            "latLngPair": t.proxy(renames["LatLngIn"]).optional(),
            "pitch": t.number().optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
        }
    ).named(renames["PoseIn"])
    types["PoseOut"] = t.struct(
        {
            "heading": t.number().optional(),
            "accuracyMeters": t.number().optional(),
            "altitude": t.number().optional(),
            "level": t.proxy(renames["LevelOut"]).optional(),
            "roll": t.number().optional(),
            "latLngPair": t.proxy(renames["LatLngOut"]).optional(),
            "pitch": t.number().optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoseOut"])
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
    types["ListPhotoSequencesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "photoSequences": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListPhotoSequencesResponseIn"])
    types["ListPhotoSequencesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "photoSequences": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPhotoSequencesResponseOut"])
    types["LevelIn"] = t.struct(
        {"number": t.number().optional(), "name": t.string()}
    ).named(renames["LevelIn"])
    types["LevelOut"] = t.struct(
        {
            "number": t.number().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LevelOut"])
    types["BatchUpdatePhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchUpdatePhotosResponseIn"])
    types["BatchUpdatePhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosResponseOut"])
    types["NoOverlapGpsFailureDetailsIn"] = t.struct(
        {
            "videoStartTime": t.string().optional(),
            "gpsStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsIn"])
    types["NoOverlapGpsFailureDetailsOut"] = t.struct(
        {
            "videoStartTime": t.string().optional(),
            "gpsStartTime": t.string().optional(),
            "gpsEndTime": t.string().optional(),
            "videoEndTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoOverlapGpsFailureDetailsOut"])
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
    types["PhotoSequenceIn"] = t.struct(
        {
            "gpsSource": t.string().optional(),
            "captureTimeOverride": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
            "imu": t.proxy(renames["ImuIn"]).optional(),
        }
    ).named(renames["PhotoSequenceIn"])
    types["PhotoSequenceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "gpsSource": t.string().optional(),
            "sequenceBounds": t.proxy(renames["LatLngBoundsOut"]).optional(),
            "captureTimeOverride": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "failureReason": t.string().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "viewCount": t.string().optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseOut"])).optional(),
            "distanceMeters": t.number().optional(),
            "failureDetails": t.proxy(
                renames["ProcessingFailureDetailsOut"]
            ).optional(),
            "processingState": t.string().optional(),
            "filename": t.string().optional(),
            "imu": t.proxy(renames["ImuOut"]).optional(),
            "uploadTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoSequenceOut"])
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
    types["ProcessingFailureDetailsIn"] = t.struct(
        {
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsIn"]
            ).optional(),
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsIn"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsIn"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsIn"]
            ).optional(),
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsIn"]
            ).optional(),
        }
    ).named(renames["ProcessingFailureDetailsIn"])
    types["ProcessingFailureDetailsOut"] = t.struct(
        {
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsOut"]
            ).optional(),
            "notOutdoorsDetails": t.proxy(
                renames["NotOutdoorsFailureDetailsOut"]
            ).optional(),
            "noOverlapGpsDetails": t.proxy(
                renames["NoOverlapGpsFailureDetailsOut"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsOut"]
            ).optional(),
            "imuDataGapDetails": t.proxy(
                renames["ImuDataGapFailureDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingFailureDetailsOut"])
    types["UploadRefIn"] = t.struct({"uploadUrl": t.string().optional()}).named(
        renames["UploadRefIn"]
    )
    types["UploadRefOut"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadRefOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["BatchGetPhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchGetPhotosResponseIn"])
    types["BatchGetPhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetPhotosResponseOut"])
    types["BatchDeletePhotosRequestIn"] = t.struct(
        {"photoIds": t.array(t.string())}
    ).named(renames["BatchDeletePhotosRequestIn"])
    types["BatchDeletePhotosRequestOut"] = t.struct(
        {
            "photoIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosRequestOut"])
    types["ConnectionIn"] = t.struct({"target": t.proxy(renames["PhotoIdIn"])}).named(
        renames["ConnectionIn"]
    )
    types["ConnectionOut"] = t.struct(
        {
            "target": t.proxy(renames["PhotoIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["PhotoIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["PhotoIdIn"]
    )
    types["PhotoIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoIdOut"])
    types["NotOutdoorsFailureDetailsIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["NotOutdoorsFailureDetailsIn"])
    types["NotOutdoorsFailureDetailsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotOutdoorsFailureDetailsOut"])
    types["BatchDeletePhotosResponseIn"] = t.struct(
        {"status": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BatchDeletePhotosResponseIn"])
    types["BatchDeletePhotosResponseOut"] = t.struct(
        {
            "status": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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

    functions = {}
    functions["photoSequenceCreate"] = streetviewpublish.get(
        "v1/photoSequence/{sequenceId}",
        t.struct(
            {
                "filter": t.string().optional(),
                "sequenceId": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceStartUpload"] = streetviewpublish.get(
        "v1/photoSequence/{sequenceId}",
        t.struct(
            {
                "filter": t.string().optional(),
                "sequenceId": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceDelete"] = streetviewpublish.get(
        "v1/photoSequence/{sequenceId}",
        t.struct(
            {
                "filter": t.string().optional(),
                "sequenceId": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceGet"] = streetviewpublish.get(
        "v1/photoSequence/{sequenceId}",
        t.struct(
            {
                "filter": t.string().optional(),
                "sequenceId": t.string(),
                "view": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["photoGet"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "updateMask": t.string(),
                "id": t.string().optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
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
                "updateMask": t.string(),
                "id": t.string().optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoStartUpload"] = streetviewpublish.put(
        "v1/photo/{id}",
        t.struct(
            {
                "updateMask": t.string(),
                "id": t.string().optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
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
                "updateMask": t.string(),
                "id": t.string().optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
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
                "updateMask": t.string(),
                "id": t.string().optional(),
                "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
                "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
                "pose": t.proxy(renames["PoseIn"]).optional(),
                "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
                "captureTime": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosList"] = streetviewpublish.post(
        "v1/photos:batchUpdate",
        t.struct(
            {
                "updatePhotoRequests": t.array(
                    t.proxy(renames["UpdatePhotoRequestIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdatePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchGet"] = streetviewpublish.post(
        "v1/photos:batchUpdate",
        t.struct(
            {
                "updatePhotoRequests": t.array(
                    t.proxy(renames["UpdatePhotoRequestIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdatePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchDelete"] = streetviewpublish.post(
        "v1/photos:batchUpdate",
        t.struct(
            {
                "updatePhotoRequests": t.array(
                    t.proxy(renames["UpdatePhotoRequestIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdatePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photosBatchUpdate"] = streetviewpublish.post(
        "v1/photos:batchUpdate",
        t.struct(
            {
                "updatePhotoRequests": t.array(
                    t.proxy(renames["UpdatePhotoRequestIn"])
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdatePhotosResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="streetviewpublish",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
