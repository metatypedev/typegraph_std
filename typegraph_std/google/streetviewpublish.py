from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_streetviewpublish():
    streetviewpublish = HTTPRuntime("https://streetviewpublish.googleapis.com/")

    renames = {
        "ErrorResponse": "_streetviewpublish_1_ErrorResponse",
        "BatchUpdatePhotosResponseIn": "_streetviewpublish_2_BatchUpdatePhotosResponseIn",
        "BatchUpdatePhotosResponseOut": "_streetviewpublish_3_BatchUpdatePhotosResponseOut",
        "BatchUpdatePhotosRequestIn": "_streetviewpublish_4_BatchUpdatePhotosRequestIn",
        "BatchUpdatePhotosRequestOut": "_streetviewpublish_5_BatchUpdatePhotosRequestOut",
        "LatLngBoundsIn": "_streetviewpublish_6_LatLngBoundsIn",
        "LatLngBoundsOut": "_streetviewpublish_7_LatLngBoundsOut",
        "NotOutdoorsFailureDetailsIn": "_streetviewpublish_8_NotOutdoorsFailureDetailsIn",
        "NotOutdoorsFailureDetailsOut": "_streetviewpublish_9_NotOutdoorsFailureDetailsOut",
        "InsufficientGpsFailureDetailsIn": "_streetviewpublish_10_InsufficientGpsFailureDetailsIn",
        "InsufficientGpsFailureDetailsOut": "_streetviewpublish_11_InsufficientGpsFailureDetailsOut",
        "LevelIn": "_streetviewpublish_12_LevelIn",
        "LevelOut": "_streetviewpublish_13_LevelOut",
        "ProcessingFailureDetailsIn": "_streetviewpublish_14_ProcessingFailureDetailsIn",
        "ProcessingFailureDetailsOut": "_streetviewpublish_15_ProcessingFailureDetailsOut",
        "Measurement3dIn": "_streetviewpublish_16_Measurement3dIn",
        "Measurement3dOut": "_streetviewpublish_17_Measurement3dOut",
        "UpdatePhotoRequestIn": "_streetviewpublish_18_UpdatePhotoRequestIn",
        "UpdatePhotoRequestOut": "_streetviewpublish_19_UpdatePhotoRequestOut",
        "ListPhotoSequencesResponseIn": "_streetviewpublish_20_ListPhotoSequencesResponseIn",
        "ListPhotoSequencesResponseOut": "_streetviewpublish_21_ListPhotoSequencesResponseOut",
        "PoseIn": "_streetviewpublish_22_PoseIn",
        "PoseOut": "_streetviewpublish_23_PoseOut",
        "ListPhotosResponseIn": "_streetviewpublish_24_ListPhotosResponseIn",
        "ListPhotosResponseOut": "_streetviewpublish_25_ListPhotosResponseOut",
        "NoOverlapGpsFailureDetailsIn": "_streetviewpublish_26_NoOverlapGpsFailureDetailsIn",
        "NoOverlapGpsFailureDetailsOut": "_streetviewpublish_27_NoOverlapGpsFailureDetailsOut",
        "PhotoIn": "_streetviewpublish_28_PhotoIn",
        "PhotoOut": "_streetviewpublish_29_PhotoOut",
        "OperationIn": "_streetviewpublish_30_OperationIn",
        "OperationOut": "_streetviewpublish_31_OperationOut",
        "ConnectionIn": "_streetviewpublish_32_ConnectionIn",
        "ConnectionOut": "_streetviewpublish_33_ConnectionOut",
        "EmptyIn": "_streetviewpublish_34_EmptyIn",
        "EmptyOut": "_streetviewpublish_35_EmptyOut",
        "BatchDeletePhotosRequestIn": "_streetviewpublish_36_BatchDeletePhotosRequestIn",
        "BatchDeletePhotosRequestOut": "_streetviewpublish_37_BatchDeletePhotosRequestOut",
        "PhotoResponseIn": "_streetviewpublish_38_PhotoResponseIn",
        "PhotoResponseOut": "_streetviewpublish_39_PhotoResponseOut",
        "BatchGetPhotosResponseIn": "_streetviewpublish_40_BatchGetPhotosResponseIn",
        "BatchGetPhotosResponseOut": "_streetviewpublish_41_BatchGetPhotosResponseOut",
        "LatLngIn": "_streetviewpublish_42_LatLngIn",
        "LatLngOut": "_streetviewpublish_43_LatLngOut",
        "PlaceIn": "_streetviewpublish_44_PlaceIn",
        "PlaceOut": "_streetviewpublish_45_PlaceOut",
        "ImuDataGapFailureDetailsIn": "_streetviewpublish_46_ImuDataGapFailureDetailsIn",
        "ImuDataGapFailureDetailsOut": "_streetviewpublish_47_ImuDataGapFailureDetailsOut",
        "PhotoSequenceIn": "_streetviewpublish_48_PhotoSequenceIn",
        "PhotoSequenceOut": "_streetviewpublish_49_PhotoSequenceOut",
        "GpsDataGapFailureDetailsIn": "_streetviewpublish_50_GpsDataGapFailureDetailsIn",
        "GpsDataGapFailureDetailsOut": "_streetviewpublish_51_GpsDataGapFailureDetailsOut",
        "BatchDeletePhotosResponseIn": "_streetviewpublish_52_BatchDeletePhotosResponseIn",
        "BatchDeletePhotosResponseOut": "_streetviewpublish_53_BatchDeletePhotosResponseOut",
        "PhotoIdIn": "_streetviewpublish_54_PhotoIdIn",
        "PhotoIdOut": "_streetviewpublish_55_PhotoIdOut",
        "UploadRefIn": "_streetviewpublish_56_UploadRefIn",
        "UploadRefOut": "_streetviewpublish_57_UploadRefOut",
        "StatusIn": "_streetviewpublish_58_StatusIn",
        "StatusOut": "_streetviewpublish_59_StatusOut",
        "ImuIn": "_streetviewpublish_60_ImuIn",
        "ImuOut": "_streetviewpublish_61_ImuOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchUpdatePhotosResponseIn"] = t.struct(
        {"results": t.array(t.proxy(renames["PhotoResponseIn"])).optional()}
    ).named(renames["BatchUpdatePhotosResponseIn"])
    types["BatchUpdatePhotosResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["PhotoResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdatePhotosResponseOut"])
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
    types["NotOutdoorsFailureDetailsIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["NotOutdoorsFailureDetailsIn"])
    types["NotOutdoorsFailureDetailsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotOutdoorsFailureDetailsOut"])
    types["InsufficientGpsFailureDetailsIn"] = t.struct(
        {"gpsPointsFound": t.integer().optional()}
    ).named(renames["InsufficientGpsFailureDetailsIn"])
    types["InsufficientGpsFailureDetailsOut"] = t.struct(
        {
            "gpsPointsFound": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InsufficientGpsFailureDetailsOut"])
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
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsIn"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsIn"]
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
            "insufficientGpsDetails": t.proxy(
                renames["InsufficientGpsFailureDetailsOut"]
            ).optional(),
            "gpsDataGapDetails": t.proxy(
                renames["GpsDataGapFailureDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingFailureDetailsOut"])
    types["Measurement3dIn"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "captureTime": t.string().optional(),
            "z": t.number().optional(),
        }
    ).named(renames["Measurement3dIn"])
    types["Measurement3dOut"] = t.struct(
        {
            "x": t.number().optional(),
            "y": t.number().optional(),
            "captureTime": t.string().optional(),
            "z": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Measurement3dOut"])
    types["UpdatePhotoRequestIn"] = t.struct(
        {"updateMask": t.string(), "photo": t.proxy(renames["PhotoIn"])}
    ).named(renames["UpdatePhotoRequestIn"])
    types["UpdatePhotoRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "photo": t.proxy(renames["PhotoOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePhotoRequestOut"])
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
    types["PoseIn"] = t.struct(
        {
            "roll": t.number().optional(),
            "level": t.proxy(renames["LevelIn"]).optional(),
            "heading": t.number().optional(),
            "latLngPair": t.proxy(renames["LatLngIn"]).optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "altitude": t.number().optional(),
            "pitch": t.number().optional(),
            "accuracyMeters": t.number().optional(),
        }
    ).named(renames["PoseIn"])
    types["PoseOut"] = t.struct(
        {
            "roll": t.number().optional(),
            "level": t.proxy(renames["LevelOut"]).optional(),
            "heading": t.number().optional(),
            "latLngPair": t.proxy(renames["LatLngOut"]).optional(),
            "gpsRecordTimestampUnixEpoch": t.string().optional(),
            "altitude": t.number().optional(),
            "pitch": t.number().optional(),
            "accuracyMeters": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PoseOut"])
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
    types["PhotoIn"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["ConnectionIn"])).optional(),
            "places": t.array(t.proxy(renames["PlaceIn"])).optional(),
            "captureTime": t.string().optional(),
            "pose": t.proxy(renames["PoseIn"]).optional(),
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
        }
    ).named(renames["PhotoIn"])
    types["PhotoOut"] = t.struct(
        {
            "transferStatus": t.string().optional(),
            "uploadTime": t.string().optional(),
            "downloadUrl": t.string().optional(),
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "viewCount": t.string().optional(),
            "places": t.array(t.proxy(renames["PlaceOut"])).optional(),
            "captureTime": t.string().optional(),
            "shareLink": t.string().optional(),
            "pose": t.proxy(renames["PoseOut"]).optional(),
            "thumbnailUrl": t.string().optional(),
            "photoId": t.proxy(renames["PhotoIdOut"]),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "mapsPublishStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ConnectionIn"] = t.struct({"target": t.proxy(renames["PhotoIdIn"])}).named(
        renames["ConnectionIn"]
    )
    types["ConnectionOut"] = t.struct(
        {
            "target": t.proxy(renames["PhotoIdOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchDeletePhotosRequestIn"] = t.struct(
        {"photoIds": t.array(t.string())}
    ).named(renames["BatchDeletePhotosRequestIn"])
    types["BatchDeletePhotosRequestOut"] = t.struct(
        {
            "photoIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosRequestOut"])
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
        {"latitude": t.number().optional(), "longitude": t.number().optional()}
    ).named(renames["LatLngIn"])
    types["LatLngOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LatLngOut"])
    types["PlaceIn"] = t.struct({"placeId": t.string().optional()}).named(
        renames["PlaceIn"]
    )
    types["PlaceOut"] = t.struct(
        {
            "placeId": t.string().optional(),
            "languageCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PlaceOut"])
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
    types["PhotoSequenceIn"] = t.struct(
        {
            "uploadReference": t.proxy(renames["UploadRefIn"]).optional(),
            "imu": t.proxy(renames["ImuIn"]).optional(),
            "captureTimeOverride": t.string().optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseIn"])).optional(),
            "gpsSource": t.string().optional(),
        }
    ).named(renames["PhotoSequenceIn"])
    types["PhotoSequenceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "uploadTime": t.string().optional(),
            "uploadReference": t.proxy(renames["UploadRefOut"]).optional(),
            "viewCount": t.string().optional(),
            "processingState": t.string().optional(),
            "distanceMeters": t.number().optional(),
            "photos": t.array(t.proxy(renames["PhotoOut"])).optional(),
            "takedown": t.boolean().optional(),
            "failureReason": t.string().optional(),
            "failureDetails": t.proxy(
                renames["ProcessingFailureDetailsOut"]
            ).optional(),
            "imu": t.proxy(renames["ImuOut"]).optional(),
            "captureTimeOverride": t.string().optional(),
            "sequenceBounds": t.proxy(renames["LatLngBoundsOut"]).optional(),
            "rawGpsTimeline": t.array(t.proxy(renames["PoseOut"])).optional(),
            "gpsSource": t.string().optional(),
            "filename": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoSequenceOut"])
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
    types["BatchDeletePhotosResponseIn"] = t.struct(
        {"status": t.array(t.proxy(renames["StatusIn"])).optional()}
    ).named(renames["BatchDeletePhotosResponseIn"])
    types["BatchDeletePhotosResponseOut"] = t.struct(
        {
            "status": t.array(t.proxy(renames["StatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeletePhotosResponseOut"])
    types["PhotoIdIn"] = t.struct({"id": t.string().optional()}).named(
        renames["PhotoIdIn"]
    )
    types["PhotoIdOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhotoIdOut"])
    types["UploadRefIn"] = t.struct({"uploadUrl": t.string().optional()}).named(
        renames["UploadRefIn"]
    )
    types["UploadRefOut"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadRefOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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

    functions = {}
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
    functions["photoDelete"] = streetviewpublish.get(
        "v1/photo/{photoId}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "view": t.string(),
                "photoId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoStartUpload"] = streetviewpublish.get(
        "v1/photo/{photoId}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "view": t.string(),
                "photoId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoCreate"] = streetviewpublish.get(
        "v1/photo/{photoId}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "view": t.string(),
                "photoId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoUpdate"] = streetviewpublish.get(
        "v1/photo/{photoId}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "view": t.string(),
                "photoId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoGet"] = streetviewpublish.get(
        "v1/photo/{photoId}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "view": t.string(),
                "photoId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PhotoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceGet"] = streetviewpublish.post(
        "v1/photoSequence:startUpload",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UploadRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceDelete"] = streetviewpublish.post(
        "v1/photoSequence:startUpload",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UploadRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceCreate"] = streetviewpublish.post(
        "v1/photoSequence:startUpload",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UploadRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["photoSequenceStartUpload"] = streetviewpublish.post(
        "v1/photoSequence:startUpload",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UploadRefOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="streetviewpublish",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
