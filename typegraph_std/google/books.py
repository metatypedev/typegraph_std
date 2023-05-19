from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_books() -> Import:
    books = HTTPRuntime("https://books.googleapis.com/")

    renames = {
        "ErrorResponse": "_books_1_ErrorResponse",
        "VolumeseriesinfoIn": "_books_2_VolumeseriesinfoIn",
        "VolumeseriesinfoOut": "_books_3_VolumeseriesinfoOut",
        "DiscoveryclustersIn": "_books_4_DiscoveryclustersIn",
        "DiscoveryclustersOut": "_books_5_DiscoveryclustersOut",
        "DictionaryAnnotationdataIn": "_books_6_DictionaryAnnotationdataIn",
        "DictionaryAnnotationdataOut": "_books_7_DictionaryAnnotationdataOut",
        "CategoryIn": "_books_8_CategoryIn",
        "CategoryOut": "_books_9_CategoryOut",
        "LayersummariesIn": "_books_10_LayersummariesIn",
        "LayersummariesOut": "_books_11_LayersummariesOut",
        "DownloadAccessesIn": "_books_12_DownloadAccessesIn",
        "DownloadAccessesOut": "_books_13_DownloadAccessesOut",
        "GeoAnnotationdataIn": "_books_14_GeoAnnotationdataIn",
        "GeoAnnotationdataOut": "_books_15_GeoAnnotationdataOut",
        "VolumeIn": "_books_16_VolumeIn",
        "VolumeOut": "_books_17_VolumeOut",
        "ReviewIn": "_books_18_ReviewIn",
        "ReviewOut": "_books_19_ReviewOut",
        "NotificationIn": "_books_20_NotificationIn",
        "NotificationOut": "_books_21_NotificationOut",
        "BooksAnnotationsRangeIn": "_books_22_BooksAnnotationsRangeIn",
        "BooksAnnotationsRangeOut": "_books_23_BooksAnnotationsRangeOut",
        "SeriesIn": "_books_24_SeriesIn",
        "SeriesOut": "_books_25_SeriesOut",
        "Volume2In": "_books_26_Volume2In",
        "Volume2Out": "_books_27_Volume2Out",
        "ConcurrentAccessRestrictionIn": "_books_28_ConcurrentAccessRestrictionIn",
        "ConcurrentAccessRestrictionOut": "_books_29_ConcurrentAccessRestrictionOut",
        "DownloadAccessRestrictionIn": "_books_30_DownloadAccessRestrictionIn",
        "DownloadAccessRestrictionOut": "_books_31_DownloadAccessRestrictionOut",
        "AnnotationsSummaryIn": "_books_32_AnnotationsSummaryIn",
        "AnnotationsSummaryOut": "_books_33_AnnotationsSummaryOut",
        "ReadingPositionIn": "_books_34_ReadingPositionIn",
        "ReadingPositionOut": "_books_35_ReadingPositionOut",
        "AnnotationIn": "_books_36_AnnotationIn",
        "AnnotationOut": "_books_37_AnnotationOut",
        "BooksCloudloadingResourceIn": "_books_38_BooksCloudloadingResourceIn",
        "BooksCloudloadingResourceOut": "_books_39_BooksCloudloadingResourceOut",
        "LayersummaryIn": "_books_40_LayersummaryIn",
        "LayersummaryOut": "_books_41_LayersummaryOut",
        "VolumeannotationsIn": "_books_42_VolumeannotationsIn",
        "VolumeannotationsOut": "_books_43_VolumeannotationsOut",
        "FamilyInfoIn": "_books_44_FamilyInfoIn",
        "FamilyInfoOut": "_books_45_FamilyInfoOut",
        "DictlayerdataIn": "_books_46_DictlayerdataIn",
        "DictlayerdataOut": "_books_47_DictlayerdataOut",
        "BooksVolumesRecommendedRateResponseIn": "_books_48_BooksVolumesRecommendedRateResponseIn",
        "BooksVolumesRecommendedRateResponseOut": "_books_49_BooksVolumesRecommendedRateResponseOut",
        "GeolayerdataIn": "_books_50_GeolayerdataIn",
        "GeolayerdataOut": "_books_51_GeolayerdataOut",
        "SeriesmembershipIn": "_books_52_SeriesmembershipIn",
        "SeriesmembershipOut": "_books_53_SeriesmembershipOut",
        "EmptyIn": "_books_54_EmptyIn",
        "EmptyOut": "_books_55_EmptyOut",
        "VolumeannotationIn": "_books_56_VolumeannotationIn",
        "VolumeannotationOut": "_books_57_VolumeannotationOut",
        "BookshelfIn": "_books_58_BookshelfIn",
        "BookshelfOut": "_books_59_BookshelfOut",
        "UsersettingsIn": "_books_60_UsersettingsIn",
        "UsersettingsOut": "_books_61_UsersettingsOut",
        "VolumesIn": "_books_62_VolumesIn",
        "VolumesOut": "_books_63_VolumesOut",
        "AnnotationsdataIn": "_books_64_AnnotationsdataIn",
        "AnnotationsdataOut": "_books_65_AnnotationsdataOut",
        "RequestAccessDataIn": "_books_66_RequestAccessDataIn",
        "RequestAccessDataOut": "_books_67_RequestAccessDataOut",
        "BookshelvesIn": "_books_68_BookshelvesIn",
        "BookshelvesOut": "_books_69_BookshelvesOut",
        "OffersIn": "_books_70_OffersIn",
        "OffersOut": "_books_71_OffersOut",
        "MetadataIn": "_books_72_MetadataIn",
        "MetadataOut": "_books_73_MetadataOut",
        "AnnotationsIn": "_books_74_AnnotationsIn",
        "AnnotationsOut": "_books_75_AnnotationsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VolumeseriesinfoIn"] = t.struct(
        {
            "volumeSeries": t.array(
                t.struct(
                    {
                        "orderNumber": t.integer().optional(),
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
                    }
                )
            ),
            "shortSeriesBookTitle": t.string().optional(),
            "kind": t.string().optional(),
            "bookDisplayNumber": t.string().optional(),
        }
    ).named(renames["VolumeseriesinfoIn"])
    types["VolumeseriesinfoOut"] = t.struct(
        {
            "volumeSeries": t.array(
                t.struct(
                    {
                        "orderNumber": t.integer().optional(),
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
                    }
                )
            ),
            "shortSeriesBookTitle": t.string().optional(),
            "kind": t.string().optional(),
            "bookDisplayNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeseriesinfoOut"])
    types["DiscoveryclustersIn"] = t.struct(
        {
            "totalClusters": t.integer(),
            "kind": t.string().optional(),
            "clusters": t.array(
                t.struct(
                    {
                        "subTitle": t.string(),
                        "title": t.string(),
                        "uid": t.string(),
                        "banner_with_content_container": t.struct(
                            {
                                "maskColorArgb": t.string(),
                                "moreButtonText": t.string(),
                                "moreButtonUrl": t.string(),
                                "textColorArgb": t.string(),
                                "imageUrl": t.string(),
                                "fillColorArgb": t.string(),
                            }
                        ),
                        "totalVolumes": t.integer(),
                        "volumes": t.array(t.proxy(renames["VolumeIn"])),
                    }
                )
            ),
        }
    ).named(renames["DiscoveryclustersIn"])
    types["DiscoveryclustersOut"] = t.struct(
        {
            "totalClusters": t.integer(),
            "kind": t.string().optional(),
            "clusters": t.array(
                t.struct(
                    {
                        "subTitle": t.string(),
                        "title": t.string(),
                        "uid": t.string(),
                        "banner_with_content_container": t.struct(
                            {
                                "maskColorArgb": t.string(),
                                "moreButtonText": t.string(),
                                "moreButtonUrl": t.string(),
                                "textColorArgb": t.string(),
                                "imageUrl": t.string(),
                                "fillColorArgb": t.string(),
                            }
                        ),
                        "totalVolumes": t.integer(),
                        "volumes": t.array(t.proxy(renames["VolumeOut"])),
                    }
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiscoveryclustersOut"])
    types["DictionaryAnnotationdataIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "volumeId": t.string().optional(),
            "annotationType": t.string().optional(),
            "data": t.proxy(renames["DictlayerdataIn"]).optional(),
            "updated": t.string().optional(),
            "encodedData": t.string().optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DictionaryAnnotationdataIn"])
    types["DictionaryAnnotationdataOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "id": t.string().optional(),
            "volumeId": t.string().optional(),
            "annotationType": t.string().optional(),
            "data": t.proxy(renames["DictlayerdataOut"]).optional(),
            "updated": t.string().optional(),
            "encodedData": t.string().optional(),
            "layerId": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DictionaryAnnotationdataOut"])
    types["CategoryIn"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "badgeUrl": t.string(),
                        "categoryId": t.string(),
                        "name": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["CategoryIn"])
    types["CategoryOut"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "badgeUrl": t.string(),
                        "categoryId": t.string(),
                        "name": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryOut"])
    types["LayersummariesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["LayersummaryIn"])).optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["LayersummariesIn"])
    types["LayersummariesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["LayersummaryOut"])).optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayersummariesOut"])
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
    types["GeoAnnotationdataIn"] = t.struct(
        {
            "updated": t.string().optional(),
            "annotationType": t.string().optional(),
            "id": t.string().optional(),
            "data": t.proxy(renames["GeolayerdataIn"]).optional(),
            "volumeId": t.string().optional(),
            "layerId": t.string().optional(),
            "encodedData": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["GeoAnnotationdataIn"])
    types["GeoAnnotationdataOut"] = t.struct(
        {
            "updated": t.string().optional(),
            "annotationType": t.string().optional(),
            "id": t.string().optional(),
            "data": t.proxy(renames["GeolayerdataOut"]).optional(),
            "volumeId": t.string().optional(),
            "layerId": t.string().optional(),
            "encodedData": t.string().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeoAnnotationdataOut"])
    types["VolumeIn"] = t.struct(
        {
            "saleInfo": t.struct(
                {
                    "saleability": t.string().optional(),
                    "isEbook": t.boolean().optional(),
                    "retailPrice": t.struct(
                        {
                            "currencyCode": t.string().optional(),
                            "amount": t.number().optional(),
                        }
                    ).optional(),
                    "offers": t.array(
                        t.struct(
                            {
                                "listPrice": t.struct(
                                    {
                                        "amountInMicros": t.number(),
                                        "currencyCode": t.string(),
                                    }
                                ).optional(),
                                "rentalDuration": t.struct(
                                    {"count": t.number(), "unit": t.string()}
                                ).optional(),
                                "retailPrice": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ).optional(),
                                "giftable": t.boolean().optional(),
                                "finskyOfferType": t.integer().optional(),
                            }
                        )
                    ).optional(),
                    "listPrice": t.struct(
                        {
                            "amount": t.number().optional(),
                            "currencyCode": t.string().optional(),
                        }
                    ).optional(),
                    "country": t.string().optional(),
                    "buyLink": t.string().optional(),
                    "onSaleDate": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "recommendedInfo": t.struct(
                {"explanation": t.string().optional()}
            ).optional(),
            "userInfo": t.struct(
                {
                    "userUploadedVolumeInfo": t.struct({"processingState": t.string()}),
                    "rentalPeriod": t.struct(
                        {"startUtcSec": t.string(), "endUtcSec": t.string()}
                    ).optional(),
                    "acquiredTime": t.string().optional(),
                    "isInMyBooks": t.boolean().optional(),
                    "isFamilySharedFromUser": t.boolean().optional(),
                    "isPurchased": t.boolean().optional(),
                    "review": t.proxy(renames["ReviewIn"]).optional(),
                    "copy": t.struct(
                        {
                            "remainingCharacterCount": t.integer(),
                            "limitType": t.string(),
                            "updated": t.string(),
                            "allowedCharacterCount": t.integer(),
                        }
                    ).optional(),
                    "isFamilySharedToUser": t.boolean().optional(),
                    "rentalState": t.string().optional(),
                    "updated": t.string().optional(),
                    "isFamilySharingAllowed": t.boolean().optional(),
                    "familySharing": t.struct(
                        {
                            "isSharingDisabledByFop": t.boolean().optional(),
                            "isSharingAllowed": t.boolean().optional(),
                            "familyRole": t.string().optional(),
                        }
                    ).optional(),
                    "isUploaded": t.boolean().optional(),
                    "readingPosition": t.proxy(renames["ReadingPositionIn"]).optional(),
                    "entitlementType": t.integer().optional(),
                    "isPreordered": t.boolean().optional(),
                    "isFamilySharingDisabledByFop": t.boolean().optional(),
                    "acquisitionType": t.integer().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "searchInfo": t.struct({"textSnippet": t.string().optional()}).optional(),
            "layerInfo": t.struct(
                {
                    "layers": t.array(
                        t.struct(
                            {
                                "layerId": t.string().optional(),
                                "volumeAnnotationsVersion": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "volumeInfo": t.struct(
                {
                    "title": t.string().optional(),
                    "subtitle": t.string().optional(),
                    "dimensions": t.struct(
                        {
                            "height": t.string().optional(),
                            "width": t.string().optional(),
                            "thickness": t.string().optional(),
                        }
                    ).optional(),
                    "readingModes": t.struct(
                        {"text": t.boolean(), "image": t.boolean()}
                    ).optional(),
                    "averageRating": t.number().optional(),
                    "seriesInfo": t.proxy(renames["VolumeseriesinfoIn"]),
                    "allowAnonLogging": t.boolean().optional(),
                    "canonicalVolumeLink": t.string().optional(),
                    "description": t.string().optional(),
                    "categories": t.array(t.string()).optional(),
                    "pageCount": t.integer().optional(),
                    "samplePageCount": t.integer().optional(),
                    "authors": t.array(t.string()).optional(),
                    "contentVersion": t.string().optional(),
                    "imageLinks": t.struct(
                        {
                            "large": t.string().optional(),
                            "thumbnail": t.string().optional(),
                            "small": t.string().optional(),
                            "smallThumbnail": t.string().optional(),
                            "extraLarge": t.string().optional(),
                            "medium": t.string().optional(),
                        }
                    ).optional(),
                    "maturityRating": t.string(),
                    "language": t.string().optional(),
                    "ratingsCount": t.integer().optional(),
                    "panelizationSummary": t.struct(
                        {
                            "containsEpubBubbles": t.boolean(),
                            "epubBubbleVersion": t.string(),
                            "imageBubbleVersion": t.string(),
                            "containsImageBubbles": t.boolean(),
                        }
                    ).optional(),
                    "infoLink": t.string().optional(),
                    "previewLink": t.string().optional(),
                    "publisher": t.string().optional(),
                    "printType": t.string().optional(),
                    "publishedDate": t.string().optional(),
                    "printedPageCount": t.integer().optional(),
                    "industryIdentifiers": t.array(
                        t.struct(
                            {
                                "identifier": t.string().optional(),
                                "type": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "mainCategory": t.string().optional(),
                    "comicsContent": t.boolean().optional(),
                }
            ).optional(),
            "accessInfo": t.struct(
                {
                    "explicitOfflineLicenseManagement": t.boolean().optional(),
                    "downloadAccess": t.proxy(
                        renames["DownloadAccessRestrictionIn"]
                    ).optional(),
                    "driveImportedContentLink": t.string().optional(),
                    "country": t.string().optional(),
                    "publicDomain": t.boolean().optional(),
                    "pdf": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                            "downloadLink": t.string().optional(),
                        }
                    ).optional(),
                    "embeddable": t.boolean().optional(),
                    "accessViewStatus": t.string().optional(),
                    "quoteSharingAllowed": t.boolean().optional(),
                    "textToSpeechPermission": t.string().optional(),
                    "webReaderLink": t.string().optional(),
                    "epub": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "downloadLink": t.string().optional(),
                            "acsTokenLink": t.string().optional(),
                        }
                    ).optional(),
                    "viewOrderUrl": t.string().optional(),
                    "viewability": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "saleInfo": t.struct(
                {
                    "saleability": t.string().optional(),
                    "isEbook": t.boolean().optional(),
                    "retailPrice": t.struct(
                        {
                            "currencyCode": t.string().optional(),
                            "amount": t.number().optional(),
                        }
                    ).optional(),
                    "offers": t.array(
                        t.struct(
                            {
                                "listPrice": t.struct(
                                    {
                                        "amountInMicros": t.number(),
                                        "currencyCode": t.string(),
                                    }
                                ).optional(),
                                "rentalDuration": t.struct(
                                    {"count": t.number(), "unit": t.string()}
                                ).optional(),
                                "retailPrice": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ).optional(),
                                "giftable": t.boolean().optional(),
                                "finskyOfferType": t.integer().optional(),
                            }
                        )
                    ).optional(),
                    "listPrice": t.struct(
                        {
                            "amount": t.number().optional(),
                            "currencyCode": t.string().optional(),
                        }
                    ).optional(),
                    "country": t.string().optional(),
                    "buyLink": t.string().optional(),
                    "onSaleDate": t.string().optional(),
                }
            ).optional(),
            "selfLink": t.string().optional(),
            "kind": t.string().optional(),
            "recommendedInfo": t.struct(
                {"explanation": t.string().optional()}
            ).optional(),
            "userInfo": t.struct(
                {
                    "userUploadedVolumeInfo": t.struct({"processingState": t.string()}),
                    "rentalPeriod": t.struct(
                        {"startUtcSec": t.string(), "endUtcSec": t.string()}
                    ).optional(),
                    "acquiredTime": t.string().optional(),
                    "isInMyBooks": t.boolean().optional(),
                    "isFamilySharedFromUser": t.boolean().optional(),
                    "isPurchased": t.boolean().optional(),
                    "review": t.proxy(renames["ReviewOut"]).optional(),
                    "copy": t.struct(
                        {
                            "remainingCharacterCount": t.integer(),
                            "limitType": t.string(),
                            "updated": t.string(),
                            "allowedCharacterCount": t.integer(),
                        }
                    ).optional(),
                    "isFamilySharedToUser": t.boolean().optional(),
                    "rentalState": t.string().optional(),
                    "updated": t.string().optional(),
                    "isFamilySharingAllowed": t.boolean().optional(),
                    "familySharing": t.struct(
                        {
                            "isSharingDisabledByFop": t.boolean().optional(),
                            "isSharingAllowed": t.boolean().optional(),
                            "familyRole": t.string().optional(),
                        }
                    ).optional(),
                    "isUploaded": t.boolean().optional(),
                    "readingPosition": t.proxy(
                        renames["ReadingPositionOut"]
                    ).optional(),
                    "entitlementType": t.integer().optional(),
                    "isPreordered": t.boolean().optional(),
                    "isFamilySharingDisabledByFop": t.boolean().optional(),
                    "acquisitionType": t.integer().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "searchInfo": t.struct({"textSnippet": t.string().optional()}).optional(),
            "layerInfo": t.struct(
                {
                    "layers": t.array(
                        t.struct(
                            {
                                "layerId": t.string().optional(),
                                "volumeAnnotationsVersion": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "volumeInfo": t.struct(
                {
                    "title": t.string().optional(),
                    "subtitle": t.string().optional(),
                    "dimensions": t.struct(
                        {
                            "height": t.string().optional(),
                            "width": t.string().optional(),
                            "thickness": t.string().optional(),
                        }
                    ).optional(),
                    "readingModes": t.struct(
                        {"text": t.boolean(), "image": t.boolean()}
                    ).optional(),
                    "averageRating": t.number().optional(),
                    "seriesInfo": t.proxy(renames["VolumeseriesinfoOut"]),
                    "allowAnonLogging": t.boolean().optional(),
                    "canonicalVolumeLink": t.string().optional(),
                    "description": t.string().optional(),
                    "categories": t.array(t.string()).optional(),
                    "pageCount": t.integer().optional(),
                    "samplePageCount": t.integer().optional(),
                    "authors": t.array(t.string()).optional(),
                    "contentVersion": t.string().optional(),
                    "imageLinks": t.struct(
                        {
                            "large": t.string().optional(),
                            "thumbnail": t.string().optional(),
                            "small": t.string().optional(),
                            "smallThumbnail": t.string().optional(),
                            "extraLarge": t.string().optional(),
                            "medium": t.string().optional(),
                        }
                    ).optional(),
                    "maturityRating": t.string(),
                    "language": t.string().optional(),
                    "ratingsCount": t.integer().optional(),
                    "panelizationSummary": t.struct(
                        {
                            "containsEpubBubbles": t.boolean(),
                            "epubBubbleVersion": t.string(),
                            "imageBubbleVersion": t.string(),
                            "containsImageBubbles": t.boolean(),
                        }
                    ).optional(),
                    "infoLink": t.string().optional(),
                    "previewLink": t.string().optional(),
                    "publisher": t.string().optional(),
                    "printType": t.string().optional(),
                    "publishedDate": t.string().optional(),
                    "printedPageCount": t.integer().optional(),
                    "industryIdentifiers": t.array(
                        t.struct(
                            {
                                "identifier": t.string().optional(),
                                "type": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "mainCategory": t.string().optional(),
                    "comicsContent": t.boolean().optional(),
                }
            ).optional(),
            "accessInfo": t.struct(
                {
                    "explicitOfflineLicenseManagement": t.boolean().optional(),
                    "downloadAccess": t.proxy(
                        renames["DownloadAccessRestrictionOut"]
                    ).optional(),
                    "driveImportedContentLink": t.string().optional(),
                    "country": t.string().optional(),
                    "publicDomain": t.boolean().optional(),
                    "pdf": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "acsTokenLink": t.string().optional(),
                            "downloadLink": t.string().optional(),
                        }
                    ).optional(),
                    "embeddable": t.boolean().optional(),
                    "accessViewStatus": t.string().optional(),
                    "quoteSharingAllowed": t.boolean().optional(),
                    "textToSpeechPermission": t.string().optional(),
                    "webReaderLink": t.string().optional(),
                    "epub": t.struct(
                        {
                            "isAvailable": t.boolean().optional(),
                            "downloadLink": t.string().optional(),
                            "acsTokenLink": t.string().optional(),
                        }
                    ).optional(),
                    "viewOrderUrl": t.string().optional(),
                    "viewability": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ReviewIn"] = t.struct(
        {
            "fullTextUrl": t.string().optional(),
            "type": t.string().optional(),
            "volumeId": t.string().optional(),
            "source": t.struct(
                {
                    "extraDescription": t.string().optional(),
                    "url": t.string().optional(),
                    "description": t.string().optional(),
                }
            ).optional(),
            "content": t.string().optional(),
            "rating": t.string().optional(),
            "title": t.string().optional(),
            "date": t.string().optional(),
            "kind": t.string().optional(),
            "author": t.struct({"displayName": t.string().optional()}).optional(),
        }
    ).named(renames["ReviewIn"])
    types["ReviewOut"] = t.struct(
        {
            "fullTextUrl": t.string().optional(),
            "type": t.string().optional(),
            "volumeId": t.string().optional(),
            "source": t.struct(
                {
                    "extraDescription": t.string().optional(),
                    "url": t.string().optional(),
                    "description": t.string().optional(),
                }
            ).optional(),
            "content": t.string().optional(),
            "rating": t.string().optional(),
            "title": t.string().optional(),
            "date": t.string().optional(),
            "kind": t.string().optional(),
            "author": t.struct({"displayName": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReviewOut"])
    types["NotificationIn"] = t.struct(
        {
            "pcampaign_id": t.string(),
            "crmExperimentIds": t.array(t.string()).optional(),
            "iconUrl": t.string(),
            "reason": t.string(),
            "doc_type": t.string(),
            "title": t.string(),
            "kind": t.string().optional(),
            "show_notification_settings_action": t.boolean(),
            "notification_type": t.string(),
            "is_document_mature": t.boolean(),
            "body": t.string(),
            "dont_show_notification": t.boolean(),
            "doc_id": t.string(),
            "timeToExpireMs": t.string(),
            "targetUrl": t.string(),
            "notificationGroup": t.string(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "pcampaign_id": t.string(),
            "crmExperimentIds": t.array(t.string()).optional(),
            "iconUrl": t.string(),
            "reason": t.string(),
            "doc_type": t.string(),
            "title": t.string(),
            "kind": t.string().optional(),
            "show_notification_settings_action": t.boolean(),
            "notification_type": t.string(),
            "is_document_mature": t.boolean(),
            "body": t.string(),
            "dont_show_notification": t.boolean(),
            "doc_id": t.string(),
            "timeToExpireMs": t.string(),
            "targetUrl": t.string(),
            "notificationGroup": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["BooksAnnotationsRangeIn"] = t.struct(
        {
            "endOffset": t.string().optional(),
            "endPosition": t.string().optional(),
            "startPosition": t.string().optional(),
            "startOffset": t.string().optional(),
        }
    ).named(renames["BooksAnnotationsRangeIn"])
    types["BooksAnnotationsRangeOut"] = t.struct(
        {
            "endOffset": t.string().optional(),
            "endPosition": t.string().optional(),
            "startPosition": t.string().optional(),
            "startOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksAnnotationsRangeOut"])
    types["SeriesIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "series": t.array(
                t.struct(
                    {
                        "isComplete": t.boolean(),
                        "subscriptionId": t.string(),
                        "imageUrl": t.string(),
                        "seriesSubscriptionReleaseInfo": t.struct(
                            {
                                "nextReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ),
                                "currentReleaseInfo": t.struct(
                                    {
                                        "releaseTime": t.string(),
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "seriesSubscriptionType": t.string(),
                                "cancelTime": t.string(),
                            }
                        ),
                        "seriesId": t.string(),
                        "seriesType": t.string(),
                        "title": t.string(),
                        "bannerImageUrl": t.string(),
                        "seriesFormatType": t.string(),
                        "eligibleForSubscription": t.boolean(),
                    }
                )
            ),
        }
    ).named(renames["SeriesIn"])
    types["SeriesOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "series": t.array(
                t.struct(
                    {
                        "isComplete": t.boolean(),
                        "subscriptionId": t.string(),
                        "imageUrl": t.string(),
                        "seriesSubscriptionReleaseInfo": t.struct(
                            {
                                "nextReleaseInfo": t.struct(
                                    {
                                        "currencyCode": t.string(),
                                        "releaseTime": t.string(),
                                        "releaseNumber": t.string(),
                                        "amountInMicros": t.number(),
                                    }
                                ),
                                "currentReleaseInfo": t.struct(
                                    {
                                        "releaseTime": t.string(),
                                        "currencyCode": t.string(),
                                        "amountInMicros": t.number(),
                                        "releaseNumber": t.string(),
                                    }
                                ),
                                "seriesSubscriptionType": t.string(),
                                "cancelTime": t.string(),
                            }
                        ),
                        "seriesId": t.string(),
                        "seriesType": t.string(),
                        "title": t.string(),
                        "bannerImageUrl": t.string(),
                        "seriesFormatType": t.string(),
                        "eligibleForSubscription": t.boolean(),
                    }
                )
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeriesOut"])
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
    types["ConcurrentAccessRestrictionIn"] = t.struct(
        {
            "deviceAllowed": t.boolean().optional(),
            "reasonCode": t.string().optional(),
            "signature": t.string().optional(),
            "source": t.string().optional(),
            "timeWindowSeconds": t.integer().optional(),
            "maxConcurrentDevices": t.integer().optional(),
            "volumeId": t.string().optional(),
            "nonce": t.string().optional(),
            "kind": t.string().optional(),
            "restricted": t.boolean().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ConcurrentAccessRestrictionIn"])
    types["ConcurrentAccessRestrictionOut"] = t.struct(
        {
            "deviceAllowed": t.boolean().optional(),
            "reasonCode": t.string().optional(),
            "signature": t.string().optional(),
            "source": t.string().optional(),
            "timeWindowSeconds": t.integer().optional(),
            "maxConcurrentDevices": t.integer().optional(),
            "volumeId": t.string().optional(),
            "nonce": t.string().optional(),
            "kind": t.string().optional(),
            "restricted": t.boolean().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConcurrentAccessRestrictionOut"])
    types["DownloadAccessRestrictionIn"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "message": t.string().optional(),
            "deviceAllowed": t.boolean().optional(),
            "nonce": t.string().optional(),
            "reasonCode": t.string().optional(),
            "maxDownloadDevices": t.integer().optional(),
            "signature": t.string().optional(),
            "downloadsAcquired": t.integer().optional(),
            "kind": t.string().optional(),
            "source": t.string().optional(),
            "justAcquired": t.boolean().optional(),
            "restricted": t.boolean().optional(),
        }
    ).named(renames["DownloadAccessRestrictionIn"])
    types["DownloadAccessRestrictionOut"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "message": t.string().optional(),
            "deviceAllowed": t.boolean().optional(),
            "nonce": t.string().optional(),
            "reasonCode": t.string().optional(),
            "maxDownloadDevices": t.integer().optional(),
            "signature": t.string().optional(),
            "downloadsAcquired": t.integer().optional(),
            "kind": t.string().optional(),
            "source": t.string().optional(),
            "justAcquired": t.boolean().optional(),
            "restricted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DownloadAccessRestrictionOut"])
    types["AnnotationsSummaryIn"] = t.struct(
        {
            "layers": t.array(
                t.struct(
                    {
                        "layerId": t.string(),
                        "limitType": t.string(),
                        "allowedCharacterCount": t.integer(),
                        "remainingCharacterCount": t.integer(),
                        "updated": t.string(),
                    }
                )
            ),
            "kind": t.string(),
        }
    ).named(renames["AnnotationsSummaryIn"])
    types["AnnotationsSummaryOut"] = t.struct(
        {
            "layers": t.array(
                t.struct(
                    {
                        "layerId": t.string(),
                        "limitType": t.string(),
                        "allowedCharacterCount": t.integer(),
                        "remainingCharacterCount": t.integer(),
                        "updated": t.string(),
                    }
                )
            ),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsSummaryOut"])
    types["ReadingPositionIn"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "pdfPosition": t.string().optional(),
            "updated": t.string().optional(),
            "epubCfiPosition": t.string().optional(),
            "gbImagePosition": t.string().optional(),
            "gbTextPosition": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ReadingPositionIn"])
    types["ReadingPositionOut"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "pdfPosition": t.string().optional(),
            "updated": t.string().optional(),
            "epubCfiPosition": t.string().optional(),
            "gbImagePosition": t.string().optional(),
            "gbTextPosition": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadingPositionOut"])
    types["AnnotationIn"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "layerSummary": t.struct(
                {
                    "limitType": t.string().optional(),
                    "remainingCharacterCount": t.integer().optional(),
                    "allowedCharacterCount": t.integer().optional(),
                }
            ),
            "id": t.string().optional(),
            "deleted": t.boolean().optional(),
            "updated": t.string().optional(),
            "layerId": t.string().optional(),
            "afterSelectedText": t.string().optional(),
            "kind": t.string().optional(),
            "created": t.string().optional(),
            "data": t.string().optional(),
            "pageIds": t.array(t.string()).optional(),
            "selectedText": t.string().optional(),
            "highlightStyle": t.string().optional(),
            "clientVersionRanges": t.struct(
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
                    "contentVersion": t.string().optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                }
            ).optional(),
            "currentVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                    "contentVersion": t.string().optional(),
                }
            ).optional(),
            "beforeSelectedText": t.string().optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "selfLink": t.string().optional(),
            "layerSummary": t.struct(
                {
                    "limitType": t.string().optional(),
                    "remainingCharacterCount": t.integer().optional(),
                    "allowedCharacterCount": t.integer().optional(),
                }
            ),
            "id": t.string().optional(),
            "deleted": t.boolean().optional(),
            "updated": t.string().optional(),
            "layerId": t.string().optional(),
            "afterSelectedText": t.string().optional(),
            "kind": t.string().optional(),
            "created": t.string().optional(),
            "data": t.string().optional(),
            "pageIds": t.array(t.string()).optional(),
            "selectedText": t.string().optional(),
            "highlightStyle": t.string().optional(),
            "clientVersionRanges": t.struct(
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
                    "contentVersion": t.string().optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                }
            ).optional(),
            "currentVersionRanges": t.struct(
                {
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "imageCfiRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                    "contentVersion": t.string().optional(),
                }
            ).optional(),
            "beforeSelectedText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["BooksCloudloadingResourceIn"] = t.struct(
        {
            "volumeId": t.string(),
            "author": t.string(),
            "title": t.string(),
            "processingState": t.string(),
        }
    ).named(renames["BooksCloudloadingResourceIn"])
    types["BooksCloudloadingResourceOut"] = t.struct(
        {
            "volumeId": t.string(),
            "author": t.string(),
            "title": t.string(),
            "processingState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksCloudloadingResourceOut"])
    types["LayersummaryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "annotationsDataLink": t.string().optional(),
            "contentVersion": t.string().optional(),
            "volumeId": t.string().optional(),
            "annotationsLink": t.string().optional(),
            "dataCount": t.integer().optional(),
            "annotationTypes": t.array(t.string()).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "volumeAnnotationsVersion": t.string().optional(),
            "annotationCount": t.integer().optional(),
            "layerId": t.string().optional(),
        }
    ).named(renames["LayersummaryIn"])
    types["LayersummaryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "annotationsDataLink": t.string().optional(),
            "contentVersion": t.string().optional(),
            "volumeId": t.string().optional(),
            "annotationsLink": t.string().optional(),
            "dataCount": t.integer().optional(),
            "annotationTypes": t.array(t.string()).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
            "volumeAnnotationsVersion": t.string().optional(),
            "annotationCount": t.integer().optional(),
            "layerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LayersummaryOut"])
    types["VolumeannotationsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["VolumeannotationIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "version": t.string().optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["VolumeannotationsIn"])
    types["VolumeannotationsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["VolumeannotationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "version": t.string().optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeannotationsOut"])
    types["FamilyInfoIn"] = t.struct(
        {
            "membership": t.struct(
                {
                    "ageGroup": t.string().optional(),
                    "acquirePermission": t.string().optional(),
                    "isInFamily": t.boolean(),
                    "allowedMaturityRating": t.string().optional(),
                    "role": t.string().optional(),
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
                    "acquirePermission": t.string().optional(),
                    "isInFamily": t.boolean(),
                    "allowedMaturityRating": t.string().optional(),
                    "role": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FamilyInfoOut"])
    types["DictlayerdataIn"] = t.struct(
        {
            "common": t.struct({"title": t.string().optional()}),
            "kind": t.string(),
            "dict": t.struct(
                {
                    "words": t.array(
                        t.struct(
                            {
                                "senses": t.array(
                                    t.struct(
                                        {
                                            "pronunciationUrl": t.string(),
                                            "syllabification": t.string(),
                                            "synonyms": t.array(
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
                                            "partOfSpeech": t.string(),
                                            "conjugations": t.array(
                                                t.struct(
                                                    {
                                                        "type": t.string(),
                                                        "value": t.string(),
                                                    }
                                                )
                                            ),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "definitions": t.array(
                                                t.struct(
                                                    {
                                                        "examples": t.array(
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
                                                        "definition": t.string(),
                                                    }
                                                )
                                            ),
                                            "pronunciation": t.string(),
                                        }
                                    )
                                ),
                                "source": t.struct(
                                    {"url": t.string(), "attribution": t.string()}
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
                                            "source": t.struct(
                                                {
                                                    "attribution": t.string(),
                                                    "url": t.string(),
                                                }
                                            ),
                                            "text": t.string(),
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
        }
    ).named(renames["DictlayerdataIn"])
    types["DictlayerdataOut"] = t.struct(
        {
            "common": t.struct({"title": t.string().optional()}),
            "kind": t.string(),
            "dict": t.struct(
                {
                    "words": t.array(
                        t.struct(
                            {
                                "senses": t.array(
                                    t.struct(
                                        {
                                            "pronunciationUrl": t.string(),
                                            "syllabification": t.string(),
                                            "synonyms": t.array(
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
                                            "partOfSpeech": t.string(),
                                            "conjugations": t.array(
                                                t.struct(
                                                    {
                                                        "type": t.string(),
                                                        "value": t.string(),
                                                    }
                                                )
                                            ),
                                            "source": t.struct(
                                                {
                                                    "url": t.string(),
                                                    "attribution": t.string(),
                                                }
                                            ),
                                            "definitions": t.array(
                                                t.struct(
                                                    {
                                                        "examples": t.array(
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
                                                        "definition": t.string(),
                                                    }
                                                )
                                            ),
                                            "pronunciation": t.string(),
                                        }
                                    )
                                ),
                                "source": t.struct(
                                    {"url": t.string(), "attribution": t.string()}
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
                                            "source": t.struct(
                                                {
                                                    "attribution": t.string(),
                                                    "url": t.string(),
                                                }
                                            ),
                                            "text": t.string(),
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
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DictlayerdataOut"])
    types["BooksVolumesRecommendedRateResponseIn"] = t.struct(
        {"consistency_token": t.string()}
    ).named(renames["BooksVolumesRecommendedRateResponseIn"])
    types["BooksVolumesRecommendedRateResponseOut"] = t.struct(
        {
            "consistency_token": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BooksVolumesRecommendedRateResponseOut"])
    types["GeolayerdataIn"] = t.struct(
        {
            "geo": t.struct(
                {
                    "latitude": t.number().optional(),
                    "longitude": t.number().optional(),
                    "zoom": t.integer().optional(),
                    "viewport": t.struct(
                        {
                            "lo": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                            "hi": t.struct(
                                {"latitude": t.number(), "longitude": t.number()}
                            ),
                        }
                    ).optional(),
                    "cachePolicy": t.string().optional(),
                    "boundary": t.array(t.string()).optional(),
                    "mapType": t.string().optional(),
                    "countryCode": t.string().optional(),
                }
            ),
            "common": t.struct(
                {
                    "snippet": t.string().optional(),
                    "title": t.string().optional(),
                    "snippetUrl": t.string().optional(),
                    "lang": t.string().optional(),
                    "previewImageUrl": t.string().optional(),
                }
            ),
            "kind": t.string(),
        }
    ).named(renames["GeolayerdataIn"])
    types["GeolayerdataOut"] = t.struct(
        {
            "geo": t.struct(
                {
                    "latitude": t.number().optional(),
                    "longitude": t.number().optional(),
                    "zoom": t.integer().optional(),
                    "viewport": t.struct(
                        {
                            "lo": t.struct(
                                {"longitude": t.number(), "latitude": t.number()}
                            ),
                            "hi": t.struct(
                                {"latitude": t.number(), "longitude": t.number()}
                            ),
                        }
                    ).optional(),
                    "cachePolicy": t.string().optional(),
                    "boundary": t.array(t.string()).optional(),
                    "mapType": t.string().optional(),
                    "countryCode": t.string().optional(),
                }
            ),
            "common": t.struct(
                {
                    "snippet": t.string().optional(),
                    "title": t.string().optional(),
                    "snippetUrl": t.string().optional(),
                    "lang": t.string().optional(),
                    "previewImageUrl": t.string().optional(),
                }
            ),
            "kind": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeolayerdataOut"])
    types["SeriesmembershipIn"] = t.struct(
        {
            "nextPageToken": t.string(),
            "member": t.array(t.proxy(renames["VolumeIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["SeriesmembershipIn"])
    types["SeriesmembershipOut"] = t.struct(
        {
            "nextPageToken": t.string(),
            "member": t.array(t.proxy(renames["VolumeOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeriesmembershipOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["VolumeannotationIn"] = t.struct(
        {
            "selectedText": t.string().optional(),
            "contentRanges": t.struct(
                {
                    "contentVersion": t.string().optional(),
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeIn"]).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeIn"]
                    ).optional(),
                }
            ).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "pageIds": t.array(t.string()).optional(),
            "volumeId": t.string().optional(),
            "layerId": t.string().optional(),
            "annotationType": t.string().optional(),
            "selfLink": t.string().optional(),
            "data": t.string().optional(),
            "annotationDataId": t.string().optional(),
            "annotationDataLink": t.string().optional(),
            "kind": t.string().optional(),
            "deleted": t.boolean().optional(),
        }
    ).named(renames["VolumeannotationIn"])
    types["VolumeannotationOut"] = t.struct(
        {
            "selectedText": t.string().optional(),
            "contentRanges": t.struct(
                {
                    "contentVersion": t.string().optional(),
                    "gbImageRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                    "cfiRange": t.proxy(renames["BooksAnnotationsRangeOut"]).optional(),
                    "gbTextRange": t.proxy(
                        renames["BooksAnnotationsRangeOut"]
                    ).optional(),
                }
            ).optional(),
            "updated": t.string().optional(),
            "id": t.string().optional(),
            "pageIds": t.array(t.string()).optional(),
            "volumeId": t.string().optional(),
            "layerId": t.string().optional(),
            "annotationType": t.string().optional(),
            "selfLink": t.string().optional(),
            "data": t.string().optional(),
            "annotationDataId": t.string().optional(),
            "annotationDataLink": t.string().optional(),
            "kind": t.string().optional(),
            "deleted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeannotationOut"])
    types["BookshelfIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "created": t.string().optional(),
            "volumesLastUpdated": t.string().optional(),
            "selfLink": t.string().optional(),
            "description": t.string().optional(),
            "id": t.integer().optional(),
            "title": t.string().optional(),
            "updated": t.string().optional(),
            "access": t.string().optional(),
        }
    ).named(renames["BookshelfIn"])
    types["BookshelfOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "created": t.string().optional(),
            "volumesLastUpdated": t.string().optional(),
            "selfLink": t.string().optional(),
            "description": t.string().optional(),
            "id": t.integer().optional(),
            "title": t.string().optional(),
            "updated": t.string().optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BookshelfOut"])
    types["UsersettingsIn"] = t.struct(
        {
            "notesExport": t.struct(
                {"isEnabled": t.boolean(), "folderName": t.string()}
            ).optional(),
            "kind": t.string().optional(),
            "notification": t.struct(
                {
                    "moreFromSeries": t.struct({"opted_state": t.string()}),
                    "rewardExpirations": t.struct({"opted_state": t.string()}),
                    "priceDrop": t.struct({"opted_state": t.string()}),
                    "moreFromAuthors": t.struct({"opted_state": t.string()}),
                    "matchMyInterests": t.struct({"opted_state": t.string()}),
                }
            ),
        }
    ).named(renames["UsersettingsIn"])
    types["UsersettingsOut"] = t.struct(
        {
            "notesExport": t.struct(
                {"isEnabled": t.boolean(), "folderName": t.string()}
            ).optional(),
            "kind": t.string().optional(),
            "notification": t.struct(
                {
                    "moreFromSeries": t.struct({"opted_state": t.string()}),
                    "rewardExpirations": t.struct({"opted_state": t.string()}),
                    "priceDrop": t.struct({"opted_state": t.string()}),
                    "moreFromAuthors": t.struct({"opted_state": t.string()}),
                    "matchMyInterests": t.struct({"opted_state": t.string()}),
                }
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersettingsOut"])
    types["VolumesIn"] = t.struct(
        {
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["VolumesIn"])
    types["VolumesOut"] = t.struct(
        {
            "totalItems": t.integer().optional(),
            "items": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumesOut"])
    types["AnnotationsdataIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GeoAnnotationdataIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["AnnotationsdataIn"])
    types["AnnotationsdataOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GeoAnnotationdataOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalItems": t.integer().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsdataOut"])
    types["RequestAccessDataIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "concurrentAccess": t.proxy(
                renames["ConcurrentAccessRestrictionIn"]
            ).optional(),
            "downloadAccess": t.proxy(
                renames["DownloadAccessRestrictionIn"]
            ).optional(),
        }
    ).named(renames["RequestAccessDataIn"])
    types["RequestAccessDataOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "concurrentAccess": t.proxy(
                renames["ConcurrentAccessRestrictionOut"]
            ).optional(),
            "downloadAccess": t.proxy(
                renames["DownloadAccessRestrictionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestAccessDataOut"])
    types["BookshelvesIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BookshelfIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BookshelvesIn"])
    types["BookshelvesOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BookshelfOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BookshelvesOut"])
    types["OffersIn"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "artUrl": t.string(),
                        "gservicesKey": t.string(),
                        "items": t.array(
                            t.struct(
                                {
                                    "coverUrl": t.string(),
                                    "volumeId": t.string(),
                                    "canonicalVolumeLink": t.string(),
                                    "title": t.string(),
                                    "description": t.string(),
                                    "author": t.string(),
                                }
                            )
                        ),
                        "id": t.string(),
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
                        "artUrl": t.string(),
                        "gservicesKey": t.string(),
                        "items": t.array(
                            t.struct(
                                {
                                    "coverUrl": t.string(),
                                    "volumeId": t.string(),
                                    "canonicalVolumeLink": t.string(),
                                    "title": t.string(),
                                    "description": t.string(),
                                    "author": t.string(),
                                }
                            )
                        ),
                        "id": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OffersOut"])
    types["MetadataIn"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "download_url": t.string(),
                        "size": t.string(),
                        "encrypted_key": t.string(),
                        "language": t.string(),
                        "version": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["MetadataIn"])
    types["MetadataOut"] = t.struct(
        {
            "items": t.array(
                t.struct(
                    {
                        "download_url": t.string(),
                        "size": t.string(),
                        "encrypted_key": t.string(),
                        "language": t.string(),
                        "version": t.string(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetadataOut"])
    types["AnnotationsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AnnotationIn"])).optional(),
            "totalItems": t.integer().optional(),
        }
    ).named(renames["AnnotationsIn"])
    types["AnnotationsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "totalItems": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationsOut"])

    functions = {}
    functions["myconfigReleaseDownloadAccess"] = books.post(
        "books/v1/myconfig/updateUserSettings",
        t.struct(
            {
                "notesExport": t.struct(
                    {"isEnabled": t.boolean(), "folderName": t.string()}
                ).optional(),
                "kind": t.string().optional(),
                "notification": t.struct(
                    {
                        "moreFromSeries": t.struct({"opted_state": t.string()}),
                        "rewardExpirations": t.struct({"opted_state": t.string()}),
                        "priceDrop": t.struct({"opted_state": t.string()}),
                        "moreFromAuthors": t.struct({"opted_state": t.string()}),
                        "matchMyInterests": t.struct({"opted_state": t.string()}),
                    }
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigGetUserSettings"] = books.post(
        "books/v1/myconfig/updateUserSettings",
        t.struct(
            {
                "notesExport": t.struct(
                    {"isEnabled": t.boolean(), "folderName": t.string()}
                ).optional(),
                "kind": t.string().optional(),
                "notification": t.struct(
                    {
                        "moreFromSeries": t.struct({"opted_state": t.string()}),
                        "rewardExpirations": t.struct({"opted_state": t.string()}),
                        "priceDrop": t.struct({"opted_state": t.string()}),
                        "moreFromAuthors": t.struct({"opted_state": t.string()}),
                        "matchMyInterests": t.struct({"opted_state": t.string()}),
                    }
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigSyncVolumeLicenses"] = books.post(
        "books/v1/myconfig/updateUserSettings",
        t.struct(
            {
                "notesExport": t.struct(
                    {"isEnabled": t.boolean(), "folderName": t.string()}
                ).optional(),
                "kind": t.string().optional(),
                "notification": t.struct(
                    {
                        "moreFromSeries": t.struct({"opted_state": t.string()}),
                        "rewardExpirations": t.struct({"opted_state": t.string()}),
                        "priceDrop": t.struct({"opted_state": t.string()}),
                        "moreFromAuthors": t.struct({"opted_state": t.string()}),
                        "matchMyInterests": t.struct({"opted_state": t.string()}),
                    }
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigRequestAccess"] = books.post(
        "books/v1/myconfig/updateUserSettings",
        t.struct(
            {
                "notesExport": t.struct(
                    {"isEnabled": t.boolean(), "folderName": t.string()}
                ).optional(),
                "kind": t.string().optional(),
                "notification": t.struct(
                    {
                        "moreFromSeries": t.struct({"opted_state": t.string()}),
                        "rewardExpirations": t.struct({"opted_state": t.string()}),
                        "priceDrop": t.struct({"opted_state": t.string()}),
                        "moreFromAuthors": t.struct({"opted_state": t.string()}),
                        "matchMyInterests": t.struct({"opted_state": t.string()}),
                    }
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["myconfigUpdateUserSettings"] = books.post(
        "books/v1/myconfig/updateUserSettings",
        t.struct(
            {
                "notesExport": t.struct(
                    {"isEnabled": t.boolean(), "folderName": t.string()}
                ).optional(),
                "kind": t.string().optional(),
                "notification": t.struct(
                    {
                        "moreFromSeries": t.struct({"opted_state": t.string()}),
                        "rewardExpirations": t.struct({"opted_state": t.string()}),
                        "priceDrop": t.struct({"opted_state": t.string()}),
                        "moreFromAuthors": t.struct({"opted_state": t.string()}),
                        "matchMyInterests": t.struct({"opted_state": t.string()}),
                    }
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsersettingsOut"]),
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
    functions["promoofferAccept"] = books.post(
        "books/v1/promooffer/dismiss",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "product": t.string().optional(),
                "offerId": t.string().optional(),
                "androidId": t.string().optional(),
                "model": t.string().optional(),
                "serial": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promoofferGet"] = books.post(
        "books/v1/promooffer/dismiss",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "product": t.string().optional(),
                "offerId": t.string().optional(),
                "androidId": t.string().optional(),
                "model": t.string().optional(),
                "serial": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["promoofferDismiss"] = books.post(
        "books/v1/promooffer/dismiss",
        t.struct(
            {
                "device": t.string().optional(),
                "manufacturer": t.string().optional(),
                "product": t.string().optional(),
                "offerId": t.string().optional(),
                "androidId": t.string().optional(),
                "model": t.string().optional(),
                "serial": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryReadingpositionsSetPosition"] = books.get(
        "books/v1/mylibrary/readingpositions/{volumeId}",
        t.struct(
            {
                "volumeId": t.string().optional(),
                "contentVersion": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReadingPositionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryReadingpositionsGet"] = books.get(
        "books/v1/mylibrary/readingpositions/{volumeId}",
        t.struct(
            {
                "volumeId": t.string().optional(),
                "contentVersion": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReadingPositionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsSummary"] = books.put(
        "books/v1/mylibrary/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "selfLink": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "limitType": t.string().optional(),
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                    }
                ),
                "id": t.string().optional(),
                "deleted": t.boolean().optional(),
                "updated": t.string().optional(),
                "layerId": t.string().optional(),
                "afterSelectedText": t.string().optional(),
                "kind": t.string().optional(),
                "created": t.string().optional(),
                "data": t.string().optional(),
                "pageIds": t.array(t.string()).optional(),
                "selectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "clientVersionRanges": t.struct(
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
                        "contentVersion": t.string().optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "beforeSelectedText": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsList"] = books.put(
        "books/v1/mylibrary/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "selfLink": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "limitType": t.string().optional(),
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                    }
                ),
                "id": t.string().optional(),
                "deleted": t.boolean().optional(),
                "updated": t.string().optional(),
                "layerId": t.string().optional(),
                "afterSelectedText": t.string().optional(),
                "kind": t.string().optional(),
                "created": t.string().optional(),
                "data": t.string().optional(),
                "pageIds": t.array(t.string()).optional(),
                "selectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "clientVersionRanges": t.struct(
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
                        "contentVersion": t.string().optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "beforeSelectedText": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsInsert"] = books.put(
        "books/v1/mylibrary/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "selfLink": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "limitType": t.string().optional(),
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                    }
                ),
                "id": t.string().optional(),
                "deleted": t.boolean().optional(),
                "updated": t.string().optional(),
                "layerId": t.string().optional(),
                "afterSelectedText": t.string().optional(),
                "kind": t.string().optional(),
                "created": t.string().optional(),
                "data": t.string().optional(),
                "pageIds": t.array(t.string()).optional(),
                "selectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "clientVersionRanges": t.struct(
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
                        "contentVersion": t.string().optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "beforeSelectedText": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsDelete"] = books.put(
        "books/v1/mylibrary/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "selfLink": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "limitType": t.string().optional(),
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                    }
                ),
                "id": t.string().optional(),
                "deleted": t.boolean().optional(),
                "updated": t.string().optional(),
                "layerId": t.string().optional(),
                "afterSelectedText": t.string().optional(),
                "kind": t.string().optional(),
                "created": t.string().optional(),
                "data": t.string().optional(),
                "pageIds": t.array(t.string()).optional(),
                "selectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "clientVersionRanges": t.struct(
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
                        "contentVersion": t.string().optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "beforeSelectedText": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryAnnotationsUpdate"] = books.put(
        "books/v1/mylibrary/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "annotationId": t.string().optional(),
                "volumeId": t.string().optional(),
                "selfLink": t.string().optional(),
                "layerSummary": t.struct(
                    {
                        "limitType": t.string().optional(),
                        "remainingCharacterCount": t.integer().optional(),
                        "allowedCharacterCount": t.integer().optional(),
                    }
                ),
                "id": t.string().optional(),
                "deleted": t.boolean().optional(),
                "updated": t.string().optional(),
                "layerId": t.string().optional(),
                "afterSelectedText": t.string().optional(),
                "kind": t.string().optional(),
                "created": t.string().optional(),
                "data": t.string().optional(),
                "pageIds": t.array(t.string()).optional(),
                "selectedText": t.string().optional(),
                "highlightStyle": t.string().optional(),
                "clientVersionRanges": t.struct(
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
                        "contentVersion": t.string().optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                    }
                ).optional(),
                "currentVersionRanges": t.struct(
                    {
                        "gbImageRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "imageCfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "gbTextRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "cfiRange": t.proxy(
                            renames["BooksAnnotationsRangeIn"]
                        ).optional(),
                        "contentVersion": t.string().optional(),
                    }
                ).optional(),
                "beforeSelectedText": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesClearVolumes"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesRemoveVolume"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesAddVolume"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesList"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesMoveVolume"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesGet"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mylibraryBookshelvesVolumesList"] = books.get(
        "books/v1/mylibrary/bookshelves/{shelf}/volumes",
        t.struct(
            {
                "shelf": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showPreorders": t.boolean().optional(),
                "source": t.string().optional(),
                "projection": t.string().optional(),
                "startIndex": t.integer().optional(),
                "country": t.string().optional(),
                "q": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notificationGet"] = books.get(
        "books/v1/notification/get",
        t.struct(
            {
                "source": t.string().optional(),
                "locale": t.string().optional(),
                "notification_id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["personalizedstreamGet"] = books.get(
        "books/v1/personalizedstream/get",
        t.struct(
            {
                "locale": t.string().optional(),
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DiscoveryclustersOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersList"] = books.get(
        "books/v1/volumes/{volumeId}/layersummary/{summaryId}",
        t.struct(
            {
                "source": t.string().optional(),
                "summaryId": t.string().optional(),
                "volumeId": t.string().optional(),
                "contentVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LayersummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersGet"] = books.get(
        "books/v1/volumes/{volumeId}/layersummary/{summaryId}",
        t.struct(
            {
                "source": t.string().optional(),
                "summaryId": t.string().optional(),
                "volumeId": t.string().optional(),
                "contentVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LayersummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersAnnotationDataList"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/data/{annotationDataId}",
        t.struct(
            {
                "locale": t.string().optional(),
                "h": t.integer().optional(),
                "scale": t.integer().optional(),
                "annotationDataId": t.string().optional(),
                "volumeId": t.string().optional(),
                "w": t.integer().optional(),
                "allowWebDefinitions": t.boolean().optional(),
                "contentVersion": t.string().optional(),
                "source": t.string().optional(),
                "layerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DictionaryAnnotationdataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersAnnotationDataGet"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/data/{annotationDataId}",
        t.struct(
            {
                "locale": t.string().optional(),
                "h": t.integer().optional(),
                "scale": t.integer().optional(),
                "annotationDataId": t.string().optional(),
                "volumeId": t.string().optional(),
                "w": t.integer().optional(),
                "allowWebDefinitions": t.boolean().optional(),
                "contentVersion": t.string().optional(),
                "source": t.string().optional(),
                "layerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DictionaryAnnotationdataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["layersVolumeAnnotationsList"] = books.get(
        "books/v1/volumes/{volumeId}/layers/{layerId}/annotations/{annotationId}",
        t.struct(
            {
                "source": t.string().optional(),
                "volumeId": t.string().optional(),
                "locale": t.string().optional(),
                "annotationId": t.string().optional(),
                "layerId": t.string().optional(),
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
                "source": t.string().optional(),
                "volumeId": t.string().optional(),
                "locale": t.string().optional(),
                "annotationId": t.string().optional(),
                "layerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeannotationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesList"] = books.get(
        "books/v1/users/{userId}/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesGet"] = books.get(
        "books/v1/users/{userId}/bookshelves/{shelf}",
        t.struct(
            {
                "shelf": t.string().optional(),
                "source": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BookshelfOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bookshelvesVolumesList"] = books.get(
        "books/v1/users/{userId}/bookshelves/{shelf}/volumes",
        t.struct(
            {
                "startIndex": t.integer().optional(),
                "source": t.string().optional(),
                "showPreorders": t.boolean().optional(),
                "shelf": t.string().optional(),
                "userId": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
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
    functions["familysharingShare"] = books.get(
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
                "page_size": t.integer().optional(),
                "series_id": t.string().optional(),
                "page_token": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeriesmembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["onboardingListCategories"] = books.get(
        "books/v1/onboarding/listCategoryVolumes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "locale": t.string().optional(),
                "categoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Volume2Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["onboardingListCategoryVolumes"] = books.get(
        "books/v1/onboarding/listCategoryVolumes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "locale": t.string().optional(),
                "categoryId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["Volume2Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cloudloadingUpdateBook"] = books.post(
        "books/v1/cloudloading/addBook",
        t.struct(
            {
                "name": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "drive_document_id": t.string().optional(),
                "mime_type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BooksCloudloadingResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cloudloadingDeleteBook"] = books.post(
        "books/v1/cloudloading/addBook",
        t.struct(
            {
                "name": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "drive_document_id": t.string().optional(),
                "mime_type": t.string().optional(),
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
                "name": t.string().optional(),
                "upload_client_token": t.string().optional(),
                "drive_document_id": t.string().optional(),
                "mime_type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BooksCloudloadingResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesList"] = books.get(
        "books/v1/volumes/{volumeId}",
        t.struct(
            {
                "includeNonComicsSeries": t.boolean().optional(),
                "user_library_consistent_read": t.boolean(),
                "country": t.string().optional(),
                "projection": t.string().optional(),
                "source": t.string().optional(),
                "volumeId": t.string().optional(),
                "partner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesGet"] = books.get(
        "books/v1/volumes/{volumeId}",
        t.struct(
            {
                "includeNonComicsSeries": t.boolean().optional(),
                "user_library_consistent_read": t.boolean(),
                "country": t.string().optional(),
                "projection": t.string().optional(),
                "source": t.string().optional(),
                "volumeId": t.string().optional(),
                "partner": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["volumesUseruploadedList"] = books.get(
        "books/v1/volumes/useruploaded",
        t.struct(
            {
                "source": t.string().optional(),
                "volumeId": t.string().optional(),
                "startIndex": t.integer().optional(),
                "locale": t.string().optional(),
                "maxResults": t.integer().optional(),
                "processingState": t.string().optional(),
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
                "source": t.string().optional(),
                "processingState": t.string().optional(),
                "maxResults": t.integer().optional(),
                "locale": t.string().optional(),
                "country": t.string().optional(),
                "startIndex": t.integer().optional(),
                "acquireMethod": t.string().optional(),
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
                "locale": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
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
                "locale": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
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
                "locale": t.string().optional(),
                "volumeId": t.string().optional(),
                "source": t.string().optional(),
                "maxAllowedMaturityRating": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="books", renames=renames, types=Box(types), functions=Box(functions)
    )
