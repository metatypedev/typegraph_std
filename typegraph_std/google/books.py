from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_books():
    books = HTTPRuntime("https://books.googleapis.com/")

    renames = {
        "ErrorResponse": "_books_1_ErrorResponse",
        "RequestAccessDataIn": "_books_2_RequestAccessDataIn",
        "RequestAccessDataOut": "_books_3_RequestAccessDataOut",
        "LayersummariesIn": "_books_4_LayersummariesIn",
        "LayersummariesOut": "_books_5_LayersummariesOut",
        "VolumeIn": "_books_6_VolumeIn",
        "VolumeOut": "_books_7_VolumeOut",
        "ConcurrentAccessRestrictionIn": "_books_8_ConcurrentAccessRestrictionIn",
        "ConcurrentAccessRestrictionOut": "_books_9_ConcurrentAccessRestrictionOut",
        "AnnotationIn": "_books_10_AnnotationIn",
        "AnnotationOut": "_books_11_AnnotationOut",
        "BookshelvesIn": "_books_12_BookshelvesIn",
        "BookshelvesOut": "_books_13_BookshelvesOut",
        "DownloadAccessesIn": "_books_14_DownloadAccessesIn",
        "DownloadAccessesOut": "_books_15_DownloadAccessesOut",
        "OffersIn": "_books_16_OffersIn",
        "OffersOut": "_books_17_OffersOut",
        "FamilyInfoIn": "_books_18_FamilyInfoIn",
        "FamilyInfoOut": "_books_19_FamilyInfoOut",
        "GeoAnnotationdataIn": "_books_20_GeoAnnotationdataIn",
        "GeoAnnotationdataOut": "_books_21_GeoAnnotationdataOut",
        "AnnotationsSummaryIn": "_books_22_AnnotationsSummaryIn",
        "AnnotationsSummaryOut": "_books_23_AnnotationsSummaryOut",
        "VolumeseriesinfoIn": "_books_24_VolumeseriesinfoIn",
        "VolumeseriesinfoOut": "_books_25_VolumeseriesinfoOut",
        "VolumeannotationIn": "_books_26_VolumeannotationIn",
        "VolumeannotationOut": "_books_27_VolumeannotationOut",
        "DictionaryAnnotationdataIn": "_books_28_DictionaryAnnotationdataIn",
        "DictionaryAnnotationdataOut": "_books_29_DictionaryAnnotationdataOut",
        "Volume2In": "_books_30_Volume2In",
        "Volume2Out": "_books_31_Volume2Out",
        "BookshelfIn": "_books_32_BookshelfIn",
        "BookshelfOut": "_books_33_BookshelfOut",
        "DictlayerdataIn": "_books_34_DictlayerdataIn",
        "DictlayerdataOut": "_books_35_DictlayerdataOut",
        "EmptyIn": "_books_36_EmptyIn",
        "EmptyOut": "_books_37_EmptyOut",
        "DownloadAccessRestrictionIn": "_books_38_DownloadAccessRestrictionIn",
        "DownloadAccessRestrictionOut": "_books_39_DownloadAccessRestrictionOut",
        "DiscoveryclustersIn": "_books_40_DiscoveryclustersIn",
        "DiscoveryclustersOut": "_books_41_DiscoveryclustersOut",
        "VolumesIn": "_books_42_VolumesIn",
        "VolumesOut": "_books_43_VolumesOut",
        "BooksVolumesRecommendedRateResponseIn": "_books_44_BooksVolumesRecommendedRateResponseIn",
        "BooksVolumesRecommendedRateResponseOut": "_books_45_BooksVolumesRecommendedRateResponseOut",
        "BooksCloudloadingResourceIn": "_books_46_BooksCloudloadingResourceIn",
        "BooksCloudloadingResourceOut": "_books_47_BooksCloudloadingResourceOut",
        "GeolayerdataIn": "_books_48_GeolayerdataIn",
        "GeolayerdataOut": "_books_49_GeolayerdataOut",
        "BooksAnnotationsRangeIn": "_books_50_BooksAnnotationsRangeIn",
        "BooksAnnotationsRangeOut": "_books_51_BooksAnnotationsRangeOut",
        "MetadataIn": "_books_52_MetadataIn",
        "MetadataOut": "_books_53_MetadataOut",
        "AnnotationsdataIn": "_books_54_AnnotationsdataIn",
        "AnnotationsdataOut": "_books_55_AnnotationsdataOut",
        "SeriesmembershipIn": "_books_56_SeriesmembershipIn",
        "SeriesmembershipOut": "_books_57_SeriesmembershipOut",
        "ReviewIn": "_books_58_ReviewIn",
        "ReviewOut": "_books_59_ReviewOut",
        "ReadingPositionIn": "_books_60_ReadingPositionIn",
        "ReadingPositionOut": "_books_61_ReadingPositionOut",
        "SeriesIn": "_books_62_SeriesIn",
        "SeriesOut": "_books_63_SeriesOut",
        "LayersummaryIn": "_books_64_LayersummaryIn",
        "LayersummaryOut": "_books_65_LayersummaryOut",
        "UsersettingsIn": "_books_66_UsersettingsIn",
        "UsersettingsOut": "_books_67_UsersettingsOut",
        "AnnotationsIn": "_books_68_AnnotationsIn",
        "AnnotationsOut": "_books_69_AnnotationsOut",
        "NotificationIn": "_books_70_NotificationIn",
        "NotificationOut": "_books_71_NotificationOut",
        "CategoryIn": "_books_72_CategoryIn",
        "CategoryOut": "_books_73_CategoryOut",
        "VolumeannotationsIn": "_books_74_VolumeannotationsIn",
        "VolumeannotationsOut": "_books_75_VolumeannotationsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RequestAccessDataIn"] = t.struct(
        {
            "concurrentAccess": t.proxy(
                renames["ConcurrentAccessRestrictionIn"]
            ).optional(),
            "kind": t.string().optional(),
            "downloadAccess": t.proxy(
                renames["DownloadAccessRestrictionIn"]
            ).optional(),
        }
    ).named(renames["RequestAccessDataIn"])
    types["RequestAccessDataOut"] = t.struct(
        {
            "concurrentAccess": t.proxy(
                renames["ConcurrentAccessRestrictionOut"]
            ).optional(),
            "kind": t.string().optional(),
            "downloadAccess": t.proxy(
                renames["DownloadAccessRestrictionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestAccessDataOut"])
    types["LayersummariesIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LayersummaryIn"])).optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["LayersummariesIn"])
    types["LayersummariesOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LayersummaryOut"])).optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayersummariesOut"])
    types["VolumeIn"] = t.struct(
        {
            "searchInfo": t.struct({"textSnippet": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "recommendedInfo": t.struct(
                {"explanation": t.string().optional()}
            ).optional(),
            "volumeInfo": t.struct(
                {
                    "printType": t.string().optional(),
                    "averageRating": t.number().optional(),
                    "readingModes": t.struct(
                        {"text": t.boolean(), "image": t.boolean()}
                    ).optional(),
                    "description": t.string().optional(),
                    "samplePageCount": t.integer().optional(),
                    "language": t.string().optional(),
                    "contentVersion": t.string().optional(),
                    "mainCategory": t.string().optional(),
                    "seriesInfo": t.proxy(renames["VolumeseriesinfoIn"]),
                    "comicsContent": t.boolean().optional(),
                    "ratingsCount": t.integer().optional(),
                    "printedPageCount": t.integer().optional(),
                    "authors": t.array(t.string()).optional(),
                    "industryIdentifiers": t.array(
                        t.struct(
                            {
                                "identifier": t.string().optional(),
                                "type": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "publisher": t.string().optional(),
                    "publishedDate": t.string().optional(),
                    "previewLink": t.string().optional(),
                    "allowAnonLogging": t.boolean().optional(),
                    "pageCount": t.integer().optional(),
                    "dimensions": t.struct(
                        {
                            "width": t.string().optional(),
                            "thickness": t.string().optional(),
                            "height": t.string().optional(),
                        }
                    ).optional(),
                    "maturityRating": t.string(),
                    "imageLinks": t.struct(
                        {
                            "thumbnail": t.string().optional(),
                            "small": t.string().optional(),
                            "medium": t.string().optional(),
                            "smallThumbnail": t.string().optional(),
                            "extraLarge": t.string().optional(),
                            "large": t.string().optional(),
                        }
                    ).optional(),
                    "infoLink": t.string().optional(),
                    "panelizationSummary": t.struct(
                        {
                            "imageBubbleVersion": t.string(),
                            "containsImageBubbles": t.boolean(),
                            "containsEpubBubbles": t.boolean(),
                            "epubBubbleVersion": t.string(),
                        }
                    ).optional(),
                    "subtitle": t.string().optional(),
                    "canonicalVolumeLink": t.string().optional(),
                    "title": t.string().optional(),
                    "categories": t.array(t.string()).optional(),
                }
            ).optional(),
            "userInfo": t.struct(
                {
                    "familySharing": t.struct(
                        {
                            "isSharingDisabledByFop": t.boolean().optional(),
                            "familyRole": t.string().optional(),
                            "isSharingAllowed": t.boolean().optional(),
                        }
                    ).optional(),
                    "acquiredTime": t.string().optional(),
                    "entitlementType": t.integer().optional(),
                    "review": t.proxy(renames["ReviewIn"]).optional(),
                    "isFamilySharedToUser": t.boolean().optional(),
                    "isInMyBooks": t.boolean().optional(),
                    "isFamilySharedFromUser": t.boolean().optional(),
                    "isPreordered": t.boolean().optional(),
                    "acquisitionType": t.integer().optional(),
                    "updated": t.string().optional(),
                    "isFamilySharingAllowed": t.boolean().optional(),
                    "rentalPeriod": t.struct(
                        {"startUtcSec": t.string(), "endUtcSec": t.string()}
                    ).optional(),
                    "isUploaded": t.boolean().optional(),
                    "rentalState": t.string().optional(),
                    "userUploadedVolumeInfo": t.struct({"processingState": t.string()}),
                    "isPurchased": t.boolean().optional(),
                    "readingPosition": t.proxy(renames["ReadingPositionIn"]).optional(),
                    "copy": t.struct(
                        {
                            "limitType": t.string(),
                            "remainingCharacterCount": t.integer(),
                            "allowedCharacterCount": t.integer(),
                            "updated": t.string(),
                        }
                    ).optional(),
                    "isFamilySharingDisabledByFop": t.boolean().optional(),
                }
            ).optional(),
            "layerInfo": t.struct(
                {
                    "layers": t.array(
                        t.struct(
                            {
                                "volumeAnnotationsVersion": t.string().optional(),
                                "layerId": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "accessInfo": t.struct(
                {
                    "quoteSharingAllowed": t.boolean().optional(),
                    "viewability": t.string().optional(),
                    "textToSpeechPermission": t.string().optional(),
                    "downloadAccess": t.proxy(
                        renames["DownloadAccessRestrictionIn"]
                    ).optional(),
                    "epub": t.struct(
                        {
                            "downloadLink": t.string().optional(),
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                        }
                    ).optional(),
                    "accessViewStatus": t.string().optional(),
                    "country": t.string().optional(),
                    "driveImportedContentLink": t.string().optional(),
                    "publicDomain": t.boolean().optional(),
                    "webReaderLink": t.string().optional(),
                    "viewOrderUrl": t.string().optional(),
                    "embeddable": t.boolean().optional(),
                    "explicitOfflineLicenseManagement": t.boolean().optional(),
                    "pdf": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                            "downloadLink": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "saleInfo": t.struct(
                {
                    "listPrice": t.struct(
                        {
                            "amount": t.number().optional(),
                            "currencyCode": t.string().optional(),
                        }
                    ).optional(),
                    "country": t.string().optional(),
                    "buyLink": t.string().optional(),
                    "offers": t.array(
                        t.struct(
                            {
                                "listPrice": t.struct(
                                    {
                                        "amountInMicros": t.number(),
                                        "currencyCode": t.string(),
                                    }
                                ).optional(),
                                "retailPrice": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ).optional(),
                                "finskyOfferType": t.integer().optional(),
                                "giftable": t.boolean().optional(),
                                "rentalDuration": t.struct(
                                    {"unit": t.string(), "count": t.number()}
                                ).optional(),
                            }
                        )
                    ).optional(),
                    "retailPrice": t.struct(
                        {
                            "currencyCode": t.string().optional(),
                            "amount": t.number().optional(),
                        }
                    ).optional(),
                    "saleability": t.string().optional(),
                    "onSaleDate": t.string().optional(),
                    "isEbook": t.boolean().optional(),
                }
            ).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "searchInfo": t.struct({"textSnippet": t.string().optional()}).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "recommendedInfo": t.struct(
                {"explanation": t.string().optional()}
            ).optional(),
            "volumeInfo": t.struct(
                {
                    "printType": t.string().optional(),
                    "averageRating": t.number().optional(),
                    "readingModes": t.struct(
                        {"text": t.boolean(), "image": t.boolean()}
                    ).optional(),
                    "description": t.string().optional(),
                    "samplePageCount": t.integer().optional(),
                    "language": t.string().optional(),
                    "contentVersion": t.string().optional(),
                    "mainCategory": t.string().optional(),
                    "seriesInfo": t.proxy(renames["VolumeseriesinfoOut"]),
                    "comicsContent": t.boolean().optional(),
                    "ratingsCount": t.integer().optional(),
                    "printedPageCount": t.integer().optional(),
                    "authors": t.array(t.string()).optional(),
                    "industryIdentifiers": t.array(
                        t.struct(
                            {
                                "identifier": t.string().optional(),
                                "type": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "publisher": t.string().optional(),
                    "publishedDate": t.string().optional(),
                    "previewLink": t.string().optional(),
                    "allowAnonLogging": t.boolean().optional(),
                    "pageCount": t.integer().optional(),
                    "dimensions": t.struct(
                        {
                            "width": t.string().optional(),
                            "thickness": t.string().optional(),
                            "height": t.string().optional(),
                        }
                    ).optional(),
                    "maturityRating": t.string(),
                    "imageLinks": t.struct(
                        {
                            "thumbnail": t.string().optional(),
                            "small": t.string().optional(),
                            "medium": t.string().optional(),
                            "smallThumbnail": t.string().optional(),
                            "extraLarge": t.string().optional(),
                            "large": t.string().optional(),
                        }
                    ).optional(),
                    "infoLink": t.string().optional(),
                    "panelizationSummary": t.struct(
                        {
                            "imageBubbleVersion": t.string(),
                            "containsImageBubbles": t.boolean(),
                            "containsEpubBubbles": t.boolean(),
                            "epubBubbleVersion": t.string(),
                        }
                    ).optional(),
                    "subtitle": t.string().optional(),
                    "canonicalVolumeLink": t.string().optional(),
                    "title": t.string().optional(),
                    "categories": t.array(t.string()).optional(),
                }
            ).optional(),
            "userInfo": t.struct(
                {
                    "familySharing": t.struct(
                        {
                            "isSharingDisabledByFop": t.boolean().optional(),
                            "familyRole": t.string().optional(),
                            "isSharingAllowed": t.boolean().optional(),
                        }
                    ).optional(),
                    "acquiredTime": t.string().optional(),
                    "entitlementType": t.integer().optional(),
                    "review": t.proxy(renames["ReviewOut"]).optional(),
                    "isFamilySharedToUser": t.boolean().optional(),
                    "isInMyBooks": t.boolean().optional(),
                    "isFamilySharedFromUser": t.boolean().optional(),
                    "isPreordered": t.boolean().optional(),
                    "acquisitionType": t.integer().optional(),
                    "updated": t.string().optional(),
                    "isFamilySharingAllowed": t.boolean().optional(),
                    "rentalPeriod": t.struct(
                        {"startUtcSec": t.string(), "endUtcSec": t.string()}
                    ).optional(),
                    "isUploaded": t.boolean().optional(),
                    "rentalState": t.string().optional(),
                    "userUploadedVolumeInfo": t.struct({"processingState": t.string()}),
                    "isPurchased": t.boolean().optional(),
                    "readingPosition": t.proxy(
                        renames["ReadingPositionOut"]
                    ).optional(),
                    "copy": t.struct(
                        {
                            "limitType": t.string(),
                            "remainingCharacterCount": t.integer(),
                            "allowedCharacterCount": t.integer(),
                            "updated": t.string(),
                        }
                    ).optional(),
                    "isFamilySharingDisabledByFop": t.boolean().optional(),
                }
            ).optional(),
            "layerInfo": t.struct(
                {
                    "layers": t.array(
                        t.struct(
                            {
                                "volumeAnnotationsVersion": t.string().optional(),
                                "layerId": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "accessInfo": t.struct(
                {
                    "quoteSharingAllowed": t.boolean().optional(),
                    "viewability": t.string().optional(),
                    "textToSpeechPermission": t.string().optional(),
                    "downloadAccess": t.proxy(
                        renames["DownloadAccessRestrictionOut"]
                    ).optional(),
                    "epub": t.struct(
                        {
                            "downloadLink": t.string().optional(),
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                        }
                    ).optional(),
                    "accessViewStatus": t.string().optional(),
                    "country": t.string().optional(),
                    "driveImportedContentLink": t.string().optional(),
                    "publicDomain": t.boolean().optional(),
                    "webReaderLink": t.string().optional(),
                    "viewOrderUrl": t.string().optional(),
                    "embeddable": t.boolean().optional(),
                    "explicitOfflineLicenseManagement": t.boolean().optional(),
                    "pdf": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                            "downloadLink": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "saleInfo": t.struct(
                {
                    "listPrice": t.struct(
                        {
                            "amount": t.number().optional(),
                            "currencyCode": t.string().optional(),
                        }
                    ).optional(),
                    "country": t.string().optional(),
                    "buyLink": t.string().optional(),
                    "offers": t.array(
                        t.struct(
                            {
                                "listPrice": t.struct(
                                    {
                                        "amountInMicros": t.number(),
                                        "currencyCode": t.string(),
                                    }
                                ).optional(),
                                "retailPrice": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ).optional(),
                                "finskyOfferType": t.integer().optional(),
                                "giftable": t.boolean().optional(),
                                "rentalDuration": t.struct(
                                    {"unit": t.string(), "count": t.number()}
                                ).optional(),
                            }
                        )
                    ).optional(),
                    "retailPrice": t.struct(
                        {
                            "currencyCode": t.string().optional(),
                            "amount": t.number().optional(),
                        }
                    ).optional(),
                    "saleability": t.string().optional(),
                    "onSaleDate": t.string().optional(),
                    "isEbook": t.boolean().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ConcurrentAccessRestrictionIn"] = t.struct(
        {
            "signature": t.string().optional(),
            "kind": t.string().optional(),
            "timeWindowSeconds": t.integer().optional(),
            "message": t.string().optional(),
            "nonce": t.string().optional(),
            "volumeId": t.string().optional(),
            "source": t.string().optional(),
            "maxConcurrentDevices": t.integer().optional(),
            "reasonCode": t.string().optional(),
            "restricted": t.boolean().optional(),
            "deviceAllowed": t.boolean().optional(),
        }
    ).named(renames["ConcurrentAccessRestrictionIn"])
    types["ConcurrentAccessRestrictionOut"] = t.struct(
        {
            "signature": t.string().optional(),
            "kind": t.string().optional(),
            "timeWindowSeconds": t.integer().optional(),
            "message": t.string().optional(),
            "nonce": t.string().optional(),
            "volumeId": t.string().optional(),
            "source": t.string().optional(),
            "maxConcurrentDevices": t.integer().optional(),
            "reasonCode": t.string().optional(),
            "restricted": t.boolean().optional(),
            "deviceAllowed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcurrentAccessRestrictionOut"])
    types["AnnotationIn"] = t.struct(
        {
            "afterSelectedText": t.string().optional(),
            "highlightStyle": t.string().optional(),
            "selfLink": t.string().optional(),
            "created": t.string().optional(),
            "clientVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "contentVersion": t.string().optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                }
            ).optional(),
            "data": t.string().optional(),
            "kind": t.string().optional(),
            "layerId": t.string().optional(),
            "layerSummary": t.struct(
                {
                    "remainingCharacterCount": t.integer().optional(),
                    "allowedCharacterCount": t.integer().optional(),
                    "limitType": t.string().optional(),
                }
            ),
            "updated": t.string().optional(),
            "beforeSelectedText": t.string().optional(),
            "selectedText": t.string().optional(),
            "deleted": t.boolean().optional(),
            "id": t.string().optional(),
            "currentVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                    "contentVersion": t.string().optional(),
                }
            ).optional(),
            "pageIds": t.array(t.string()).optional(),
            "volumeId": t.string().optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "afterSelectedText": t.string().optional(),
            "highlightStyle": t.string().optional(),
            "selfLink": t.string().optional(),
            "created": t.string().optional(),
            "clientVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "contentVersion": t.string().optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                }
            ).optional(),
            "data": t.string().optional(),
            "kind": t.string().optional(),
            "layerId": t.string().optional(),
            "layerSummary": t.struct(
                {
                    "remainingCharacterCount": t.integer().optional(),
                    "allowedCharacterCount": t.integer().optional(),
                    "limitType": t.string().optional(),
                }
            ),
            "updated": t.string().optional(),
            "beforeSelectedText": t.string().optional(),
            "selectedText": t.string().optional(),
            "deleted": t.boolean().optional(),
            "id": t.string().optional(),
            "currentVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                    "contentVersion": t.string().optional(),
                }
            ).optional(),
            "pageIds": t.array(t.string()).optional(),
            "volumeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["BookshelvesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["BookshelfIn"])).optional(),
        }
    ).named(renames["BookshelvesIn"])
    types["BookshelvesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["BookshelfOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BookshelvesOut"])
    types["DownloadAccessesIn"] = t.struct(
        {
            "downloadAccessList": t.array(
                t.proxy(renames["DownloadAccessRestrictionIn"])
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DownloadAccessesIn"])
    types["DownloadAccessesOut"] = t.struct(
        {
            "downloadAccessList": t.array(
                t.proxy(renames["DownloadAccessRestrictionOut"])
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadAccessesOut"])
    types["OffersIn"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "items": t.array(
                            t.struct(
                                {
                                    "description": t.string(),
                                    "author": t.string(),
                                    "volumeId": t.string(),
                                    "canonicalVolumeLink": t.string(),
                                    "coverUrl": t.string(),
                                    "title": t.string(),
                                }
                            )
                        ),
                        "id": t.string(),
                        "artUrl": t.string(),
                        "gservicesKey": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OffersIn"])
    types["OffersOut"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "items": t.array(
                            t.struct(
                                {
                                    "description": t.string(),
                                    "author": t.string(),
                                    "volumeId": t.string(),
                                    "canonicalVolumeLink": t.string(),
                                    "coverUrl": t.string(),
                                    "title": t.string(),
                                }
                            )
                        ),
                        "id": t.string(),
                        "artUrl": t.string(),
                        "gservicesKey": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OffersOut"])
    types["FamilyInfoIn"] = t.struct(
        {
            "membership": t.struct(
                {
                    "ageGroup": t.string().optional(),
                    "allowedMaturityRating": t.string().optional(),
                    "role": t.string().optional(),
                    "isInFamily": t.boolean(),
                    "acquirePermission": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FamilyInfoIn"])
    types["FamilyInfoOut"] = t.struct(
        {
            "membership": t.struct(
                {
                    "ageGroup": t.string().optional(),
                    "allowedMaturityRating": t.string().optional(),
                    "role": t.string().optional(),
                    "isInFamily": t.boolean(),
                    "acquirePermission": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamilyInfoOut"])
    types["GeoAnnotationdataIn"] = t.struct(
        {
            "id": t.string().optional(),
            "encodedData": t.string().optional(),
            "updated": t.string().optional(),
            "volumeId": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "annotationType": t.string().optional(),
            "data": t.proxy(renames["GeolayerdataIn"]).optional(),
            "layerId": t.string().optional(),
        }
    ).named(renames["GeoAnnotationdataIn"])
    types["GeoAnnotationdataOut"] = t.struct(
        {
            "id": t.string().optional(),
            "encodedData": t.string().optional(),
            "updated": t.string().optional(),
            "volumeId": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "annotationType": t.string().optional(),
            "data": t.proxy(renames["GeolayerdataOut"]).optional(),
            "layerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoAnnotationdataOut"])
    types["AnnotationsSummaryIn"] = t.struct(
        {
            "kind": t.string(),
            "layers": t.array(
                t.struct(
                    {
                        "updated": t.string(),
                        "allowedCharacterCount": t.integer(),
                        "layerId": t.string(),
                        "remainingCharacterCount": t.integer(),
                        "limitType": t.string(),
                    }
                )
            ),
        }
    ).named(renames["AnnotationsSummaryIn"])
    types["AnnotationsSummaryOut"] = t.struct(
        {
            "kind": t.string(),
            "layers": t.array(
                t.struct(
                    {
                        "updated": t.string(),
                        "allowedCharacterCount": t.integer(),
                        "layerId": t.string(),
                        "remainingCharacterCount": t.integer(),
                        "limitType": t.string(),
                    }
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsSummaryOut"])
    types["VolumeseriesinfoIn"] = t.struct(
        {
            "shortSeriesBookTitle": t.string().optional(),
            "bookDisplayNumber": t.string().optional(),
            "kind": t.string().optional(),
            "volumeSeries": t.array(
                t.struct(
                    {
                        "seriesBookType": t.string().optional(),
                        "issue": t.array(
                            t.struct(
                                {
                                    "issueDisplayNumber": t.string(),
                                    "issueOrderNumber": t.integer(),
                                }
                            )
                        ).optional(),
                        "seriesId": t.string().optional(),
                        "orderNumber": t.integer().optional(),
                    }
                )
            ),
        }
    ).named(renames["VolumeseriesinfoIn"])
    types["VolumeseriesinfoOut"] = t.struct(
        {
            "shortSeriesBookTitle": t.string().optional(),
            "bookDisplayNumber": t.string().optional(),
            "kind": t.string().optional(),
            "volumeSeries": t.array(
                t.struct(
                    {
                        "seriesBookType": t.string().optional(),
                        "issue": t.array(
                            t.struct(
                                {
                                    "issueDisplayNumber": t.string(),
                                    "issueOrderNumber": t.integer(),
                                }
                            )
                        ).optional(),
                        "seriesId": t.string().optional(),
                        "orderNumber": t.integer().optional(),
                    }
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeseriesinfoOut"])
    types["VolumeannotationIn"] = t.struct(
        {
            "updated": t.string().optional(),
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "data": t.string().optional(),
            "selectedText": t.string().optional(),
            "annotationDataLink": t.string().optional(),
            "contentRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                    "contentVersion": t.string().optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                }
            ).optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "deleted": t.boolean().optional(),
            "pageIds": t.array(t.string()).optional(),
            "annotationDataId": t.string().optional(),
            "annotationType": t.string().optional(),
        }
    ).named(renames["VolumeannotationIn"])
    types["VolumeannotationOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "data": t.string().optional(),
            "selectedText": t.string().optional(),
            "annotationDataLink": t.string().optional(),
            "contentRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                    "contentVersion": t.string().optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                }
            ).optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "deleted": t.boolean().optional(),
            "pageIds": t.array(t.string()).optional(),
            "annotationDataId": t.string().optional(),
            "annotationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeannotationOut"])
    types["DictionaryAnnotationdataIn"] = t.struct(
        {
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "annotationType": t.string().optional(),
            "id": t.string().optional(),
            "layerId": t.string().optional(),
            "data": t.proxy(renames["DictlayerdataIn"]).optional(),
            "encodedData": t.string().optional(),
        }
    ).named(renames["DictionaryAnnotationdataIn"])
    types["DictionaryAnnotationdataOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "annotationType": t.string().optional(),
            "id": t.string().optional(),
            "layerId": t.string().optional(),
            "data": t.proxy(renames["DictlayerdataOut"]).optional(),
            "encodedData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DictionaryAnnotationdataOut"])
    types["Volume2In"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string(),
            "items": t.array(t.proxy(renames["VolumeIn"])).optional(),
        }
    ).named(renames["Volume2In"])
    types["Volume2Out"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string(),
            "items": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Volume2Out"])
    types["BookshelfIn"] = t.struct(
        {
            "created": t.string().optional(),
            "access": t.string().optional(),
            "description": t.string().optional(),
            "id": t.integer().optional(),
            "kind": t.string().optional(),
            "title": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "updated": t.string().optional(),
            "volumesLastUpdated": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["BookshelfIn"])
    types["BookshelfOut"] = t.struct(
        {
            "created": t.string().optional(),
            "access": t.string().optional(),
            "description": t.string().optional(),
            "id": t.integer().optional(),
            "kind": t.string().optional(),
            "title": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "updated": t.string().optional(),
            "volumesLastUpdated": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BookshelfOut"])
    types["DictlayerdataIn"] = t.struct(
        {
            "dict": t.struct(
                {
                    "words": t.array(
                        t.struct(
                            {
                                "senses": t.array(
                                    t.struct(
                                        {
                                            "pronunciation": t.string(),
                                            "syllabification": t.string(),
                                            "conjugations": t.array(
                                                t.struct(
                                                    {
                                                        "type": t.string(),
                                                        "value": t.string(),
                                                    }
                                                )
                                            ),
                                            "definitions": t.array(
                                                t.struct(
                                                    {
                                                        "definition": t.string(),
                                                        "examples": t.array(
                                                            t.struct(
                                                                {
                                                                    "text": t.string(),
                                                                    "source": t.struct(
                                                                        {
                                                                            "url": t.string(),
                                                                            "attribution": t.string(),
                                                                        }
                                                                    ),
                                                                }
                                                            )
                                                        ),
                                                    }
                                                )
                                            ),
                                            "partOfSpeech": t.string(),
                                            "pronunciationUrl": t.string(),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "synonyms": t.array(
                                                t.struct(
                                                    {
                                                        "text": t.string(),
                                                        "source": t.struct(
                                                            {
                                                                "attribution": t.string(),
                                                                "url": t.string(),
                                                            }
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    )
                                ),
                                "source": t.struct(
                                    {"attribution": t.string(), "url": t.string()}
                                ).optional(),
                                "derivatives": t.array(
                                    t.struct(
                                        {
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "text": t.string(),
                                        }
                                    )
                                ),
                                "examples": t.array(
                                    t.struct(
                                        {
                                            "text": t.string(),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                        }
                                    )
                                ),
                            }
                        )
                    ),
                    "source": t.struct(
                        {"url": t.string(), "attribution": t.string()}
                    ).optional(),
                }
            ),
            "common": t.struct({"title": t.string().optional()}),
            "kind": t.string(),
        }
    ).named(renames["DictlayerdataIn"])
    types["DictlayerdataOut"] = t.struct(
        {
            "dict": t.struct(
                {
                    "words": t.array(
                        t.struct(
                            {
                                "senses": t.array(
                                    t.struct(
                                        {
                                            "pronunciation": t.string(),
                                            "syllabification": t.string(),
                                            "conjugations": t.array(
                                                t.struct(
                                                    {
                                                        "type": t.string(),
                                                        "value": t.string(),
                                                    }
                                                )
                                            ),
                                            "definitions": t.array(
                                                t.struct(
                                                    {
                                                        "definition": t.string(),
                                                        "examples": t.array(
                                                            t.struct(
                                                                {
                                                                    "text": t.string(),
                                                                    "source": t.struct(
                                                                        {
                                                                            "url": t.string(),
                                                                            "attribution": t.string(),
                                                                        }
                                                                    ),
                                                                }
                                                            )
                                                        ),
                                                    }
                                                )
                                            ),
                                            "partOfSpeech": t.string(),
                                            "pronunciationUrl": t.string(),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "synonyms": t.array(
                                                t.struct(
                                                    {
                                                        "text": t.string(),
                                                        "source": t.struct(
                                                            {
                                                                "attribution": t.string(),
                                                                "url": t.string(),
                                                            }
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    )
                                ),
                                "source": t.struct(
                                    {"attribution": t.string(), "url": t.string()}
                                ).optional(),
                                "derivatives": t.array(
                                    t.struct(
                                        {
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "text": t.string(),
                                        }
                                    )
                                ),
                                "examples": t.array(
                                    t.struct(
                                        {
                                            "text": t.string(),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                        }
                                    )
                                ),
                            }
                        )
                    ),
                    "source": t.struct(
                        {"url": t.string(), "attribution": t.string()}
                    ).optional(),
                }
            ),
            "common": t.struct({"title": t.string().optional()}),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DictlayerdataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DownloadAccessRestrictionIn"] = t.struct(
        {
            "message": t.string().optional(),
            "deviceAllowed": t.boolean().optional(),
            "justAcquired": t.boolean().optional(),
            "maxDownloadDevices": t.integer().optional(),
            "volumeId": t.string().optional(),
            "downloadsAcquired": t.integer().optional(),
            "reasonCode": t.string().optional(),
            "nonce": t.string().optional(),
            "kind": t.string().optional(),
            "restricted": t.boolean().optional(),
            "source": t.string().optional(),
            "signature": t.string().optional(),
        }
    ).named(renames["DownloadAccessRestrictionIn"])
    types["DownloadAccessRestrictionOut"] = t.struct(
        {
            "message": t.string().optional(),
            "deviceAllowed": t.boolean().optional(),
            "justAcquired": t.boolean().optional(),
            "maxDownloadDevices": t.integer().optional(),
            "volumeId": t.string().optional(),
            "downloadsAcquired": t.integer().optional(),
            "reasonCode": t.string().optional(),
            "nonce": t.string().optional(),
            "kind": t.string().optional(),
            "restricted": t.boolean().optional(),
            "source": t.string().optional(),
            "signature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadAccessRestrictionOut"])
    types["DiscoveryclustersIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "clusters": t.array(
                t.struct(
                    {
                        "banner_with_content_container": t.struct(
                            {
                                "textColorArgb": t.string(),
                                "moreButtonUrl": t.string(),
                                "fillColorArgb": t.string(),
                                "moreButtonText": t.string(),
                                "imageUrl": t.string(),
                                "maskColorArgb": t.string(),
                            }
                        ),
                        "subTitle": t.string(),
                        "title": t.string(),
                        "totalVolumes": t.integer(),
                        "volumes": t.array(t.proxy(renames["VolumeIn"])),
                        "uid": t.string(),
                    }
                )
            ),
            "totalClusters": t.integer(),
        }
    ).named(renames["DiscoveryclustersIn"])
    types["DiscoveryclustersOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "clusters": t.array(
                t.struct(
                    {
                        "banner_with_content_container": t.struct(
                            {
                                "textColorArgb": t.string(),
                                "moreButtonUrl": t.string(),
                                "fillColorArgb": t.string(),
                                "moreButtonText": t.string(),
                                "imageUrl": t.string(),
                                "maskColorArgb": t.string(),
                            }
                        ),
                        "subTitle": t.string(),
                        "title": t.string(),
                        "totalVolumes": t.integer(),
                        "volumes": t.array(t.proxy(renames["VolumeOut"])),
                        "uid": t.string(),
                    }
                )
            ),
            "totalClusters": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryclustersOut"])
    types["VolumesIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["VolumesIn"])
    types["VolumesOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumesOut"])
    types["BooksVolumesRecommendedRateResponseIn"] = t.struct(
        {"consistency_token": t.string()}
    ).named(renames["BooksVolumesRecommendedRateResponseIn"])
    types["BooksVolumesRecommendedRateResponseOut"] = t.struct(
        {
            "consistency_token": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksVolumesRecommendedRateResponseOut"])
    types["BooksCloudloadingResourceIn"] = t.struct(
        {
            "volumeId": t.string(),
            "title": t.string(),
            "author": t.string(),
            "processingState": t.string(),
        }
    ).named(renames["BooksCloudloadingResourceIn"])
    types["BooksCloudloadingResourceOut"] = t.struct(
        {
            "volumeId": t.string(),
            "title": t.string(),
            "author": t.string(),
            "processingState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksCloudloadingResourceOut"])
    types["GeolayerdataIn"] = t.struct(
        {
            "geo": t.struct(
                {
                    "viewport": t.struct(
                        {
                            "lo": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                            "hi": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                        }
                    ).optional(),
                    "mapType": t.string().optional(),
                    "countryCode": t.string().optional(),
                    "latitude": t.number().optional(),
                    "longitude": t.number().optional(),
                    "boundary": t.array(t.string()).optional(),
                    "cachePolicy": t.string().optional(),
                    "zoom": t.integer().optional(),
                }
            ),
            "kind": t.string(),
            "common": t.struct(
                {
                    "lang": t.string().optional(),
                    "title": t.string().optional(),
                    "snippetUrl": t.string().optional(),
                    "snippet": t.string().optional(),
                    "previewImageUrl": t.string().optional(),
                }
            ),
        }
    ).named(renames["GeolayerdataIn"])
    types["GeolayerdataOut"] = t.struct(
        {
            "geo": t.struct(
                {
                    "viewport": t.struct(
                        {
                            "lo": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                            "hi": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                        }
                    ).optional(),
                    "mapType": t.string().optional(),
                    "countryCode": t.string().optional(),
                    "latitude": t.number().optional(),
                    "longitude": t.number().optional(),
                    "boundary": t.array(t.string()).optional(),
                    "cachePolicy": t.string().optional(),
                    "zoom": t.integer().optional(),
                }
            ),
            "kind": t.string(),
            "common": t.struct(
                {
                    "lang": t.string().optional(),
                    "title": t.string().optional(),
                    "snippetUrl": t.string().optional(),
                    "snippet": t.string().optional(),
                    "previewImageUrl": t.string().optional(),
                }
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolayerdataOut"])
    types["BooksAnnotationsRangeIn"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "endOffset": t.string().optional(),
            "startPosition": t.string().optional(),
            "endPosition": t.string().optional(),
        }
    ).named(renames["BooksAnnotationsRangeIn"])
    types["BooksAnnotationsRangeOut"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "endOffset": t.string().optional(),
            "startPosition": t.string().optional(),
            "endPosition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksAnnotationsRangeOut"])
    types["MetadataIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "size": t.string(),
                        "language": t.string(),
                        "version": t.string(),
                        "download_url": t.string(),
                        "encrypted_key": t.string(),
                    }
                )
            ).optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "size": t.string(),
                        "language": t.string(),
                        "version": t.string(),
                        "download_url": t.string(),
                        "encrypted_key": t.string(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["AnnotationsdataIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["GeoAnnotationdataIn"])).optional(),
        }
    ).named(renames["AnnotationsdataIn"])
    types["AnnotationsdataOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["GeoAnnotationdataOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsdataOut"])
    types["SeriesmembershipIn"] = t.struct(
        {
            "member": t.array(t.proxy(renames["VolumeIn"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string(),
        }
    ).named(renames["SeriesmembershipIn"])
    types["SeriesmembershipOut"] = t.struct(
        {
            "member": t.array(t.proxy(renames["VolumeOut"])),
            "kind": t.string().optional(),
            "nextPageToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeriesmembershipOut"])
    types["ReviewIn"] = t.struct(
        {
            "content": t.string().optional(),
            "kind": t.string().optional(),
            "author": t.struct({"displayName": t.string().optional()}).optional(),
            "fullTextUrl": t.string().optional(),
            "source": t.struct(
                {
                    "description": t.string().optional(),
                    "extraDescription": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "rating": t.string().optional(),
            "volumeId": t.string().optional(),
            "date": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ReviewIn"])
    types["ReviewOut"] = t.struct(
        {
            "content": t.string().optional(),
            "kind": t.string().optional(),
            "author": t.struct({"displayName": t.string().optional()}).optional(),
            "fullTextUrl": t.string().optional(),
            "source": t.struct(
                {
                    "description": t.string().optional(),
                    "extraDescription": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "rating": t.string().optional(),
            "volumeId": t.string().optional(),
            "date": t.string().optional(),
            "type": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewOut"])
    types["ReadingPositionIn"] = t.struct(
        {
            "gbTextPosition": t.string().optional(),
            "volumeId": t.string().optional(),
            "epubCfiPosition": t.string().optional(),
            "pdfPosition": t.string().optional(),
            "kind": t.string().optional(),
            "gbImagePosition": t.string().optional(),
            "updated": t.string().optional(),
        }
    ).named(renames["ReadingPositionIn"])
    types["ReadingPositionOut"] = t.struct(
        {
            "gbTextPosition": t.string().optional(),
            "volumeId": t.string().optional(),
            "epubCfiPosition": t.string().optional(),
            "pdfPosition": t.string().optional(),
            "kind": t.string().optional(),
            "gbImagePosition": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadingPositionOut"])
    types["SeriesIn"] = t.struct(
        {
            "series": t.array(
                t.struct(
                    {
                        "seriesSubscriptionReleaseInfo": t.struct(
                            {
                                "currentReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "cancelTime": t.string(),
                                "nextReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "seriesSubscriptionType": t.string(),
                            }
                        ),
                        "seriesType": t.string(),
                        "imageUrl": t.string(),
                        "isComplete": t.boolean(),
                        "seriesId": t.string(),
                        "bannerImageUrl": t.string(),
                        "seriesFormatType": t.string(),
                        "subscriptionId": t.string(),
                        "eligibleForSubscription": t.boolean(),
                        "title": t.string(),
                    }
                )
            ),
            "kind": t.string().optional(),
        }
    ).named(renames["SeriesIn"])
    types["SeriesOut"] = t.struct(
        {
            "series": t.array(
                t.struct(
                    {
                        "seriesSubscriptionReleaseInfo": t.struct(
                            {
                                "currentReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "cancelTime": t.string(),
                                "nextReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "seriesSubscriptionType": t.string(),
                            }
                        ),
                        "seriesType": t.string(),
                        "imageUrl": t.string(),
                        "isComplete": t.boolean(),
                        "seriesId": t.string(),
                        "bannerImageUrl": t.string(),
                        "seriesFormatType": t.string(),
                        "subscriptionId": t.string(),
                        "eligibleForSubscription": t.boolean(),
                        "title": t.string(),
                    }
                )
            ),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeriesOut"])
    types["LayersummaryIn"] = t.struct(
        {
            "annotationTypes": t.array(t.string()).optional(),
            "updated": t.string().optional(),
            "annotationsLink": t.string().optional(),
            "dataCount": t.integer().optional(),
            "id": t.string().optional(),
            "volumeAnnotationsVersion": t.string().optional(),
            "annotationsDataLink": t.string().optional(),
            "volumeId": t.string().optional(),
            "contentVersion": t.string().optional(),
            "selfLink": t.string().optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
            "annotationCount": t.integer().optional(),
        }
    ).named(renames["LayersummaryIn"])
    types["LayersummaryOut"] = t.struct(
        {
            "annotationTypes": t.array(t.string()).optional(),
            "updated": t.string().optional(),
            "annotationsLink": t.string().optional(),
            "dataCount": t.integer().optional(),
            "id": t.string().optional(),
            "volumeAnnotationsVersion": t.string().optional(),
            "annotationsDataLink": t.string().optional(),
            "volumeId": t.string().optional(),
            "contentVersion": t.string().optional(),
            "selfLink": t.string().optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
            "annotationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayersummaryOut"])
    types["UsersettingsIn"] = t.struct(
        {
            "notification": t.struct(
                {
                    "moreFromAuthors": t.struct({"opted_state": t.string()}),
                    "priceDrop": t.struct({"opted_state": t.string()}),
                    "matchMyInterests": t.struct({"opted_state": t.string()}),
                    "rewardExpirations": t.struct({"opted_state": t.string()}),
                    "moreFromSeries": t.struct({"opted_state": t.string()}),
                }
            ),
            "kind": t.string().optional(),
            "notesExport": t.struct(
                {"isEnabled": t.boolean(), "folderName": t.string()}
            ).optional(),
        }
    ).named(renames["UsersettingsIn"])
    types["UsersettingsOut"] = t.struct(
        {
            "notification": t.struct(
                {
                    "moreFromAuthors": t.struct({"opted_state": t.string()}),
                    "priceDrop": t.struct({"opted_state": t.string()}),
                    "matchMyInterests": t.struct({"opted_state": t.string()}),
                    "rewardExpirations": t.struct({"opted_state": t.string()}),
                    "moreFromSeries": t.struct({"opted_state": t.string()}),
                }
            ),
            "kind": t.string().optional(),
            "notesExport": t.struct(
                {"isEnabled": t.boolean(), "folderName": t.string()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersettingsOut"])
    types["AnnotationsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AnnotationIn"])).optional(),
        }
    ).named(renames["AnnotationsIn"])
    types["AnnotationsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "totalItems": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsOut"])
    types["NotificationIn"] = t.struct(
        {
            "dont_show_notification": t.boolean(),
            "crmExperimentIds": t.array(t.string()).optional(),
            "doc_type": t.string(),
            "pcampaign_id": t.string(),
            "body": t.string(),
            "show_notification_settings_action": t.boolean(),
            "notificationGroup": t.string(),
            "targetUrl": t.string(),
            "kind": t.string().optional(),
            "notification_type": t.string(),
            "doc_id": t.string(),
            "timeToExpireMs": t.string(),
            "reason": t.string(),
            "iconUrl": t.string(),
            "title": t.string(),
            "is_document_mature": t.boolean(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "dont_show_notification": t.boolean(),
            "crmExperimentIds": t.array(t.string()).optional(),
            "doc_type": t.string(),
            "pcampaign_id": t.string(),
            "body": t.string(),
            "show_notification_settings_action": t.boolean(),
            "notificationGroup": t.string(),
            "targetUrl": t.string(),
            "kind": t.string().optional(),
            "notification_type": t.string(),
            "doc_id": t.string(),
            "timeToExpireMs": t.string(),
            "reason": t.string(),
            "iconUrl": t.string(),
            "title": t.string(),
            "is_document_mature": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["CategoryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "badgeUrl": t.string(),
                        "name": t.string(),
                        "categoryId": t.string(),
                    }
                )
            ).optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(
                t.struct(
                    {
                        "badgeUrl": t.string(),
                        "name": t.string(),
                        "categoryId": t.string(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["VolumeannotationsIn"] = t.struct(
        {
            "version": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["VolumeannotationIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VolumeannotationsIn"])
    types["VolumeannotationsOut"] = t.struct(
        {
            "version": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["VolumeannotationOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeannotationsOut"])

    functions = {}
    functions["notificationGet"] = books.get(
        "books/v1/notification/get",
        t.struct(
            {
                "notification_id": t.string().optional(),
                "locale": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["onboardingListCategoryVolumes"] = books.get(
        "books/v1/onboarding/listCategories",
        t.struct({"locale": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["onboardingListCategories"] = books.get(
        "books/v1/onboarding/listCategories",
        t.struct({"locale": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CategoryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["dictionaryListOfflineMetadata"] = books.get(
        "books/v1/dictionary/listOfflineMetadata",
        t.struct({"cpksver": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["MetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryReadingpositionsGet"] = books.post(
        "books/v1/mylibrary/readingpositions/{volumeId}/setPosition",
        t.struct(
            {
                "action": t.string().optional(),
                "position": t.string().optional(),
                "contentVersion": t.string().optional(),
                "timestamp": t.string().optional(),
                "volumeId": t.string().optional(),
                "source": t.string().optional(),
                "deviceCookie": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryReadingpositionsSetPosition"] = books.post(
        "books/v1/mylibrary/readingpositions/{volumeId}/setPosition",
        t.struct(
            {
                "action": t.string().optional(),
                "position": t.string().optional(),
                "contentVersion": t.string().optional(),
                "timestamp": t.string().optional(),
                "volumeId": t.string().optional(),
                "source": t.string().optional(),
                "deviceCookie": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsUpdate"] = books.post(
        "books/v1/mylibrary/annotations",
        t.struct(
            {
                "country": t.string().optional(),
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "showOnlySummaryInResponse": t.boolean().optional(),
                "afterSelectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "selfLink": t.string().optional(),
                "created": t.string().optional(),
                "clientVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "data": t.string().optional(),
                "kind": t.string().optional(),
                "layerId": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                        "limitType": t.string().optional(),
                    }
                ),
                "updated": t.string().optional(),
                "beforeSelectedText": t.string().optional(),
                "selectedText": t.string().optional(),
                "deleted": t.boolean().optional(),
                "id": t.string().optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "pageIds": t.array(t.string()).optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsList"] = books.post(
        "books/v1/mylibrary/annotations",
        t.struct(
            {
                "country": t.string().optional(),
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "showOnlySummaryInResponse": t.boolean().optional(),
                "afterSelectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "selfLink": t.string().optional(),
                "created": t.string().optional(),
                "clientVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "data": t.string().optional(),
                "kind": t.string().optional(),
                "layerId": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                        "limitType": t.string().optional(),
                    }
                ),
                "updated": t.string().optional(),
                "beforeSelectedText": t.string().optional(),
                "selectedText": t.string().optional(),
                "deleted": t.boolean().optional(),
                "id": t.string().optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "pageIds": t.array(t.string()).optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsDelete"] = books.post(
        "books/v1/mylibrary/annotations",
        t.struct(
            {
                "country": t.string().optional(),
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "showOnlySummaryInResponse": t.boolean().optional(),
                "afterSelectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "selfLink": t.string().optional(),
                "created": t.string().optional(),
                "clientVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "data": t.string().optional(),
                "kind": t.string().optional(),
                "layerId": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                        "limitType": t.string().optional(),
                    }
                ),
                "updated": t.string().optional(),
                "beforeSelectedText": t.string().optional(),
                "selectedText": t.string().optional(),
                "deleted": t.boolean().optional(),
                "id": t.string().optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "pageIds": t.array(t.string()).optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsSummary"] = books.post(
        "books/v1/mylibrary/annotations",
        t.struct(
            {
                "country": t.string().optional(),
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "showOnlySummaryInResponse": t.boolean().optional(),
                "afterSelectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "selfLink": t.string().optional(),
                "created": t.string().optional(),
                "clientVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "data": t.string().optional(),
                "kind": t.string().optional(),
                "layerId": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                        "limitType": t.string().optional(),
                    }
                ),
                "updated": t.string().optional(),
                "beforeSelectedText": t.string().optional(),
                "selectedText": t.string().optional(),
                "deleted": t.boolean().optional(),
                "id": t.string().optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "pageIds": t.array(t.string()).optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsInsert"] = books.post(
        "books/v1/mylibrary/annotations",
        t.struct(
            {
                "country": t.string().optional(),
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "showOnlySummaryInResponse": t.boolean().optional(),
                "afterSelectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "selfLink": t.string().optional(),
                "created": t.string().optional(),
                "clientVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "data": t.string().optional(),
                "kind": t.string().optional(),
                "layerId": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                        "limitType": t.string().optional(),
                    }
                ),
                "updated": t.string().optional(),
                "beforeSelectedText": t.string().optional(),
                "selectedText": t.string().optional(),
                "deleted": t.boolean().optional(),
                "id": t.string().optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "pageIds": t.array(t.string()).optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesAddVolume"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesList"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesClearVolumes"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesRemoveVolume"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesGet"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesMoveVolume"] = books.post(
        "books/v1/mylibrary/bookshelves/{shelf}/moveVolume",
        t.struct(
            {
                "volumePosition": t.integer().optional(),
                "volumeId": t.string().optional(),
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesVolumesList"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}/volumes",
        t.struct(
            {
                "source": t.string().optional(),
                "shelf": t.string().optional(),
                "q": t.string().optional(),
                "startIndex": t.integer().optional(),
                "maxResults": t.integer().optional(),
                "country": t.string().optional(),
                "showPreorders": t.boolean().optional(),
                "projection": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersGet"] = books.get(
        "books/v1/volumes/{volumeId}/layersummary",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "contentVersion": t.string().optional(),
                "volumeId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LayersummariesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersList"] = books.get(
        "books/v1/volumes/{volumeId}/layersummary",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "contentVersion": t.string().optional(),
                "volumeId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LayersummariesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersVolumeAnnotationsList"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/annotations/{annotationId}",
        t.struct(
            {
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "layerId": t.string().optional(),
                "source": t.string().optional(),
                "locale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeannotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersVolumeAnnotationsGet"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/annotations/{annotationId}",
        t.struct(
            {
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "layerId": t.string().optional(),
                "source": t.string().optional(),
                "locale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeannotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersAnnotationDataGet"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/data",
        t.struct(
            {
                "locale": t.string().optional(),
                "maxResults": t.integer().optional(),
                "w": t.integer().optional(),
                "source": t.string().optional(),
                "contentVersion": t.string().optional(),
                "pageToken": t.string().optional(),
                "layerId": t.string().optional(),
                "annotationDataId": t.string().optional(),
                "h": t.integer().optional(),
                "updatedMax": t.string().optional(),
                "scale": t.integer().optional(),
                "updatedMin": t.string().optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationsdataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersAnnotationDataList"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/data",
        t.struct(
            {
                "locale": t.string().optional(),
                "maxResults": t.integer().optional(),
                "w": t.integer().optional(),
                "source": t.string().optional(),
                "contentVersion": t.string().optional(),
                "pageToken": t.string().optional(),
                "layerId": t.string().optional(),
                "annotationDataId": t.string().optional(),
                "h": t.integer().optional(),
                "updatedMax": t.string().optional(),
                "scale": t.integer().optional(),
                "updatedMin": t.string().optional(),
                "volumeId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationsdataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesGet"] = books.get(
        "books/v1/volumes",
        t.struct(
            {
                "download": t.string().optional(),
                "q": t.string().optional(),
                "partner": t.string().optional(),
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "showPreorders": t.boolean().optional(),
                "libraryRestrict": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "printType": t.string().optional(),
                "projection": t.string().optional(),
                "orderBy": t.string().optional(),
                "langRestrict": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesList"] = books.get(
        "books/v1/volumes",
        t.struct(
            {
                "download": t.string().optional(),
                "q": t.string().optional(),
                "partner": t.string().optional(),
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "showPreorders": t.boolean().optional(),
                "libraryRestrict": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "startIndex": t.integer().optional(),
                "printType": t.string().optional(),
                "projection": t.string().optional(),
                "orderBy": t.string().optional(),
                "langRestrict": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesMybooksList"] = books.get(
        "books/v1/volumes/mybooks",
        t.struct(
            {
                "processingState": t.string().optional(),
                "country": t.string().optional(),
                "source": t.string().optional(),
                "startIndex": t.integer().optional(),
                "maxResults": t.integer().optional(),
                "locale": t.string().optional(),
                "acquireMethod": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesAssociatedList"] = books.get(
        "books/v1/volumes/{volumeId}/associated",
        t.struct(
            {
                "association": t.string().optional(),
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "volumeId": t.string().optional(),
                "locale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesRecommendedRate"] = books.get(
        "books/v1/volumes/recommended",
        t.struct(
            {
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "locale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesRecommendedList"] = books.get(
        "books/v1/volumes/recommended",
        t.struct(
            {
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "locale": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesUseruploadedList"] = books.get(
        "books/v1/volumes/useruploaded",
        t.struct(
            {
                "volumeId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "source": t.string().optional(),
                "processingState": t.string().optional(),
                "locale": t.string().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesGet"] = books.get(
        "books/v1/users/{userId}/bookshelves",
        t.struct(
            {
                "source": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelvesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesList"] = books.get(
        "books/v1/users/{userId}/bookshelves",
        t.struct(
            {
                "source": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelvesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesVolumesList"] = books.get(
        "books/v1/users/{userId}/bookshelves/{shelf}/volumes",
        t.struct(
            {
                "showPreorders": t.boolean().optional(),
                "userId": t.string().optional(),
                "shelf": t.string().optional(),
                "maxResults": t.integer().optional(),
                "source": t.string().optional(),
                "startIndex": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promoofferDismiss"] = books.get(
        "books/v1/promooffer/get",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "androidId": t.string().optional(),
                "product": t.string().optional(),
                "serial": t.string().optional(),
                "model": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OffersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promoofferAccept"] = books.get(
        "books/v1/promooffer/get",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "androidId": t.string().optional(),
                "product": t.string().optional(),
                "serial": t.string().optional(),
                "model": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OffersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promoofferGet"] = books.get(
        "books/v1/promooffer/get",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "androidId": t.string().optional(),
                "product": t.string().optional(),
                "serial": t.string().optional(),
                "model": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OffersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["personalizedstreamGet"] = books.get(
        "books/v1/personalizedstream/get",
        t.struct(
            {
                "source": t.string().optional(),
                "locale": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DiscoveryclustersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["seriesGet"] = books.get(
        "books/v1/series/get",
        t.struct({"series_id": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SeriesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["seriesMembershipGet"] = books.get(
        "books/v1/series/membership/get",
        t.struct(
            {
                "series_id": t.string().optional(),
                "page_token": t.string().optional(),
                "page_size": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeriesmembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cloudloadingDeleteBook"] = books.post(
        "books/v1/cloudloading/addBook",
        t.struct(
            {
                "drive_document_id": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "mime_type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BooksCloudloadingResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cloudloadingUpdateBook"] = books.post(
        "books/v1/cloudloading/addBook",
        t.struct(
            {
                "drive_document_id": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "mime_type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BooksCloudloadingResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cloudloadingAddBook"] = books.post(
        "books/v1/cloudloading/addBook",
        t.struct(
            {
                "drive_document_id": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "mime_type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BooksCloudloadingResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["familysharingShare"] = books.get(
        "books/v1/familysharing/getFamilyInfo",
        t.struct({"source": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FamilyInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["familysharingUnshare"] = books.get(
        "books/v1/familysharing/getFamilyInfo",
        t.struct({"source": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FamilyInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["familysharingGetFamilyInfo"] = books.get(
        "books/v1/familysharing/getFamilyInfo",
        t.struct({"source": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["FamilyInfoOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigSyncVolumeLicenses"] = books.get(
        "books/v1/myconfig/getUserSettings",
        t.struct({"country": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigUpdateUserSettings"] = books.get(
        "books/v1/myconfig/getUserSettings",
        t.struct({"country": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigReleaseDownloadAccess"] = books.get(
        "books/v1/myconfig/getUserSettings",
        t.struct({"country": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigRequestAccess"] = books.get(
        "books/v1/myconfig/getUserSettings",
        t.struct({"country": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigGetUserSettings"] = books.get(
        "books/v1/myconfig/getUserSettings",
        t.struct({"country": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="books", renames=renames, types=Box(types), functions=Box(functions)
    )
