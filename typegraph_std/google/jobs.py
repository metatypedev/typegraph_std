from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_jobs() -> Import:
    jobs = HTTPRuntime("https://jobs.googleapis.com/")

    renames = {
        "ErrorResponse": "_jobs_1_ErrorResponse",
        "OperationIn": "_jobs_2_OperationIn",
        "OperationOut": "_jobs_3_OperationOut",
        "StatusIn": "_jobs_4_StatusIn",
        "StatusOut": "_jobs_5_StatusOut",
        "CompanyIn": "_jobs_6_CompanyIn",
        "CompanyOut": "_jobs_7_CompanyOut",
        "CompanyDerivedInfoIn": "_jobs_8_CompanyDerivedInfoIn",
        "CompanyDerivedInfoOut": "_jobs_9_CompanyDerivedInfoOut",
        "LocationIn": "_jobs_10_LocationIn",
        "LocationOut": "_jobs_11_LocationOut",
        "PostalAddressIn": "_jobs_12_PostalAddressIn",
        "PostalAddressOut": "_jobs_13_PostalAddressOut",
        "LatLngIn": "_jobs_14_LatLngIn",
        "LatLngOut": "_jobs_15_LatLngOut",
        "EmptyIn": "_jobs_16_EmptyIn",
        "EmptyOut": "_jobs_17_EmptyOut",
        "ListCompaniesResponseIn": "_jobs_18_ListCompaniesResponseIn",
        "ListCompaniesResponseOut": "_jobs_19_ListCompaniesResponseOut",
        "ResponseMetadataIn": "_jobs_20_ResponseMetadataIn",
        "ResponseMetadataOut": "_jobs_21_ResponseMetadataOut",
        "CompleteQueryResponseIn": "_jobs_22_CompleteQueryResponseIn",
        "CompleteQueryResponseOut": "_jobs_23_CompleteQueryResponseOut",
        "CompletionResultIn": "_jobs_24_CompletionResultIn",
        "CompletionResultOut": "_jobs_25_CompletionResultOut",
        "ClientEventIn": "_jobs_26_ClientEventIn",
        "ClientEventOut": "_jobs_27_ClientEventOut",
        "JobEventIn": "_jobs_28_JobEventIn",
        "JobEventOut": "_jobs_29_JobEventOut",
        "JobIn": "_jobs_30_JobIn",
        "JobOut": "_jobs_31_JobOut",
        "ApplicationInfoIn": "_jobs_32_ApplicationInfoIn",
        "ApplicationInfoOut": "_jobs_33_ApplicationInfoOut",
        "CompensationInfoIn": "_jobs_34_CompensationInfoIn",
        "CompensationInfoOut": "_jobs_35_CompensationInfoOut",
        "CompensationEntryIn": "_jobs_36_CompensationEntryIn",
        "CompensationEntryOut": "_jobs_37_CompensationEntryOut",
        "MoneyIn": "_jobs_38_MoneyIn",
        "MoneyOut": "_jobs_39_MoneyOut",
        "CompensationRangeIn": "_jobs_40_CompensationRangeIn",
        "CompensationRangeOut": "_jobs_41_CompensationRangeOut",
        "CustomAttributeIn": "_jobs_42_CustomAttributeIn",
        "CustomAttributeOut": "_jobs_43_CustomAttributeOut",
        "JobDerivedInfoIn": "_jobs_44_JobDerivedInfoIn",
        "JobDerivedInfoOut": "_jobs_45_JobDerivedInfoOut",
        "ProcessingOptionsIn": "_jobs_46_ProcessingOptionsIn",
        "ProcessingOptionsOut": "_jobs_47_ProcessingOptionsOut",
        "BatchCreateJobsRequestIn": "_jobs_48_BatchCreateJobsRequestIn",
        "BatchCreateJobsRequestOut": "_jobs_49_BatchCreateJobsRequestOut",
        "BatchUpdateJobsRequestIn": "_jobs_50_BatchUpdateJobsRequestIn",
        "BatchUpdateJobsRequestOut": "_jobs_51_BatchUpdateJobsRequestOut",
        "BatchDeleteJobsRequestIn": "_jobs_52_BatchDeleteJobsRequestIn",
        "BatchDeleteJobsRequestOut": "_jobs_53_BatchDeleteJobsRequestOut",
        "ListJobsResponseIn": "_jobs_54_ListJobsResponseIn",
        "ListJobsResponseOut": "_jobs_55_ListJobsResponseOut",
        "SearchJobsRequestIn": "_jobs_56_SearchJobsRequestIn",
        "SearchJobsRequestOut": "_jobs_57_SearchJobsRequestOut",
        "RequestMetadataIn": "_jobs_58_RequestMetadataIn",
        "RequestMetadataOut": "_jobs_59_RequestMetadataOut",
        "DeviceInfoIn": "_jobs_60_DeviceInfoIn",
        "DeviceInfoOut": "_jobs_61_DeviceInfoOut",
        "JobQueryIn": "_jobs_62_JobQueryIn",
        "JobQueryOut": "_jobs_63_JobQueryOut",
        "LocationFilterIn": "_jobs_64_LocationFilterIn",
        "LocationFilterOut": "_jobs_65_LocationFilterOut",
        "CommuteFilterIn": "_jobs_66_CommuteFilterIn",
        "CommuteFilterOut": "_jobs_67_CommuteFilterOut",
        "TimeOfDayIn": "_jobs_68_TimeOfDayIn",
        "TimeOfDayOut": "_jobs_69_TimeOfDayOut",
        "CompensationFilterIn": "_jobs_70_CompensationFilterIn",
        "CompensationFilterOut": "_jobs_71_CompensationFilterOut",
        "TimestampRangeIn": "_jobs_72_TimestampRangeIn",
        "TimestampRangeOut": "_jobs_73_TimestampRangeOut",
        "HistogramQueryIn": "_jobs_74_HistogramQueryIn",
        "HistogramQueryOut": "_jobs_75_HistogramQueryOut",
        "CustomRankingInfoIn": "_jobs_76_CustomRankingInfoIn",
        "CustomRankingInfoOut": "_jobs_77_CustomRankingInfoOut",
        "SearchJobsResponseIn": "_jobs_78_SearchJobsResponseIn",
        "SearchJobsResponseOut": "_jobs_79_SearchJobsResponseOut",
        "MatchingJobIn": "_jobs_80_MatchingJobIn",
        "MatchingJobOut": "_jobs_81_MatchingJobOut",
        "CommuteInfoIn": "_jobs_82_CommuteInfoIn",
        "CommuteInfoOut": "_jobs_83_CommuteInfoOut",
        "HistogramQueryResultIn": "_jobs_84_HistogramQueryResultIn",
        "HistogramQueryResultOut": "_jobs_85_HistogramQueryResultOut",
        "SpellingCorrectionIn": "_jobs_86_SpellingCorrectionIn",
        "SpellingCorrectionOut": "_jobs_87_SpellingCorrectionOut",
        "TenantIn": "_jobs_88_TenantIn",
        "TenantOut": "_jobs_89_TenantOut",
        "ListTenantsResponseIn": "_jobs_90_ListTenantsResponseIn",
        "ListTenantsResponseOut": "_jobs_91_ListTenantsResponseOut",
        "BatchOperationMetadataIn": "_jobs_92_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_jobs_93_BatchOperationMetadataOut",
        "BatchCreateJobsResponseIn": "_jobs_94_BatchCreateJobsResponseIn",
        "BatchCreateJobsResponseOut": "_jobs_95_BatchCreateJobsResponseOut",
        "JobResultIn": "_jobs_96_JobResultIn",
        "JobResultOut": "_jobs_97_JobResultOut",
        "BatchUpdateJobsResponseIn": "_jobs_98_BatchUpdateJobsResponseIn",
        "BatchUpdateJobsResponseOut": "_jobs_99_BatchUpdateJobsResponseOut",
        "BatchDeleteJobsResponseIn": "_jobs_100_BatchDeleteJobsResponseIn",
        "BatchDeleteJobsResponseOut": "_jobs_101_BatchDeleteJobsResponseOut",
        "MendelDebugInputIn": "_jobs_102_MendelDebugInputIn",
        "MendelDebugInputOut": "_jobs_103_MendelDebugInputOut",
        "NamespacedDebugInputIn": "_jobs_104_NamespacedDebugInputIn",
        "NamespacedDebugInputOut": "_jobs_105_NamespacedDebugInputOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["CompanyIn"] = t.struct(
        {
            "name": t.string(),
            "displayName": t.string(),
            "externalId": t.string(),
            "size": t.string().optional(),
            "headquartersAddress": t.string().optional(),
            "hiringAgency": t.boolean().optional(),
            "eeoText": t.string().optional(),
            "websiteUri": t.string().optional(),
            "careerSiteUri": t.string().optional(),
            "imageUri": t.string().optional(),
            "keywordSearchableJobCustomAttributes": t.array(t.string()).optional(),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "name": t.string(),
            "displayName": t.string(),
            "externalId": t.string(),
            "size": t.string().optional(),
            "headquartersAddress": t.string().optional(),
            "hiringAgency": t.boolean().optional(),
            "eeoText": t.string().optional(),
            "websiteUri": t.string().optional(),
            "careerSiteUri": t.string().optional(),
            "imageUri": t.string().optional(),
            "keywordSearchableJobCustomAttributes": t.array(t.string()).optional(),
            "derivedInfo": t.proxy(renames["CompanyDerivedInfoOut"]).optional(),
            "suspended": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyOut"])
    types["CompanyDerivedInfoIn"] = t.struct(
        {"headquartersLocation": t.proxy(renames["LocationIn"]).optional()}
    ).named(renames["CompanyDerivedInfoIn"])
    types["CompanyDerivedInfoOut"] = t.struct(
        {
            "headquartersLocation": t.proxy(renames["LocationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyDerivedInfoOut"])
    types["LocationIn"] = t.struct(
        {
            "locationType": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "latLng": t.proxy(renames["LatLngIn"]).optional(),
            "radiusMiles": t.number().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationType": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "radiusMiles": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "revision": t.integer().optional(),
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListCompaniesResponseIn"] = t.struct(
        {
            "companies": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
        }
    ).named(renames["ListCompaniesResponseIn"])
    types["ListCompaniesResponseOut"] = t.struct(
        {
            "companies": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCompaniesResponseOut"])
    types["ResponseMetadataIn"] = t.struct({"requestId": t.string().optional()}).named(
        renames["ResponseMetadataIn"]
    )
    types["ResponseMetadataOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetadataOut"])
    types["CompleteQueryResponseIn"] = t.struct(
        {
            "completionResults": t.array(
                t.proxy(renames["CompletionResultIn"])
            ).optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
        }
    ).named(renames["CompleteQueryResponseIn"])
    types["CompleteQueryResponseOut"] = t.struct(
        {
            "completionResults": t.array(
                t.proxy(renames["CompletionResultOut"])
            ).optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteQueryResponseOut"])
    types["CompletionResultIn"] = t.struct(
        {
            "suggestion": t.string().optional(),
            "type": t.string().optional(),
            "imageUri": t.string().optional(),
        }
    ).named(renames["CompletionResultIn"])
    types["CompletionResultOut"] = t.struct(
        {
            "suggestion": t.string().optional(),
            "type": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletionResultOut"])
    types["ClientEventIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "eventId": t.string(),
            "createTime": t.string(),
            "jobEvent": t.proxy(renames["JobEventIn"]).optional(),
            "eventNotes": t.string().optional(),
        }
    ).named(renames["ClientEventIn"])
    types["ClientEventOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "eventId": t.string(),
            "createTime": t.string(),
            "jobEvent": t.proxy(renames["JobEventOut"]).optional(),
            "eventNotes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientEventOut"])
    types["JobEventIn"] = t.struct(
        {"type": t.string(), "jobs": t.array(t.string())}
    ).named(renames["JobEventIn"])
    types["JobEventOut"] = t.struct(
        {
            "type": t.string(),
            "jobs": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobEventOut"])
    types["JobIn"] = t.struct(
        {
            "name": t.string(),
            "company": t.string(),
            "requisitionId": t.string(),
            "title": t.string(),
            "description": t.string(),
            "addresses": t.array(t.string()).optional(),
            "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
            "jobBenefits": t.array(t.string()).optional(),
            "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
            "customAttributes": t.struct({"_": t.string().optional()}).optional(),
            "degreeTypes": t.array(t.string()).optional(),
            "department": t.string().optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "incentives": t.string().optional(),
            "languageCode": t.string().optional(),
            "jobLevel": t.string().optional(),
            "promotionValue": t.integer().optional(),
            "qualifications": t.string().optional(),
            "responsibilities": t.string().optional(),
            "postingRegion": t.string().optional(),
            "visibility": t.string().optional(),
            "jobStartTime": t.string().optional(),
            "jobEndTime": t.string().optional(),
            "postingPublishTime": t.string().optional(),
            "postingExpireTime": t.string().optional(),
            "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "name": t.string(),
            "company": t.string(),
            "requisitionId": t.string(),
            "title": t.string(),
            "description": t.string(),
            "addresses": t.array(t.string()).optional(),
            "applicationInfo": t.proxy(renames["ApplicationInfoOut"]).optional(),
            "jobBenefits": t.array(t.string()).optional(),
            "compensationInfo": t.proxy(renames["CompensationInfoOut"]).optional(),
            "customAttributes": t.struct({"_": t.string().optional()}).optional(),
            "degreeTypes": t.array(t.string()).optional(),
            "department": t.string().optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "incentives": t.string().optional(),
            "languageCode": t.string().optional(),
            "jobLevel": t.string().optional(),
            "promotionValue": t.integer().optional(),
            "qualifications": t.string().optional(),
            "responsibilities": t.string().optional(),
            "postingRegion": t.string().optional(),
            "visibility": t.string().optional(),
            "jobStartTime": t.string().optional(),
            "jobEndTime": t.string().optional(),
            "postingPublishTime": t.string().optional(),
            "postingExpireTime": t.string().optional(),
            "postingCreateTime": t.string().optional(),
            "postingUpdateTime": t.string().optional(),
            "companyDisplayName": t.string().optional(),
            "derivedInfo": t.proxy(renames["JobDerivedInfoOut"]).optional(),
            "processingOptions": t.proxy(renames["ProcessingOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["ApplicationInfoIn"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "instruction": t.string().optional(),
            "uris": t.array(t.string()).optional(),
        }
    ).named(renames["ApplicationInfoIn"])
    types["ApplicationInfoOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "instruction": t.string().optional(),
            "uris": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationInfoOut"])
    types["CompensationInfoIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["CompensationEntryIn"])).optional()}
    ).named(renames["CompensationInfoIn"])
    types["CompensationInfoOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["CompensationEntryOut"])).optional(),
            "annualizedBaseCompensationRange": t.proxy(
                renames["CompensationRangeOut"]
            ).optional(),
            "annualizedTotalCompensationRange": t.proxy(
                renames["CompensationRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationInfoOut"])
    types["CompensationEntryIn"] = t.struct(
        {
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "amount": t.proxy(renames["MoneyIn"]).optional(),
            "range": t.proxy(renames["CompensationRangeIn"]).optional(),
            "description": t.string().optional(),
            "expectedUnitsPerYear": t.number().optional(),
        }
    ).named(renames["CompensationEntryIn"])
    types["CompensationEntryOut"] = t.struct(
        {
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "range": t.proxy(renames["CompensationRangeOut"]).optional(),
            "description": t.string().optional(),
            "expectedUnitsPerYear": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationEntryOut"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["CompensationRangeIn"] = t.struct(
        {
            "maxCompensation": t.proxy(renames["MoneyIn"]).optional(),
            "minCompensation": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["CompensationRangeIn"])
    types["CompensationRangeOut"] = t.struct(
        {
            "maxCompensation": t.proxy(renames["MoneyOut"]).optional(),
            "minCompensation": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationRangeOut"])
    types["CustomAttributeIn"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "longValues": t.array(t.string()).optional(),
            "filterable": t.boolean().optional(),
            "keywordSearchable": t.boolean().optional(),
        }
    ).named(renames["CustomAttributeIn"])
    types["CustomAttributeOut"] = t.struct(
        {
            "stringValues": t.array(t.string()).optional(),
            "longValues": t.array(t.string()).optional(),
            "filterable": t.boolean().optional(),
            "keywordSearchable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAttributeOut"])
    types["JobDerivedInfoIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "jobCategories": t.array(t.string()).optional(),
        }
    ).named(renames["JobDerivedInfoIn"])
    types["JobDerivedInfoOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "jobCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobDerivedInfoOut"])
    types["ProcessingOptionsIn"] = t.struct(
        {
            "disableStreetAddressResolution": t.boolean().optional(),
            "htmlSanitization": t.string().optional(),
        }
    ).named(renames["ProcessingOptionsIn"])
    types["ProcessingOptionsOut"] = t.struct(
        {
            "disableStreetAddressResolution": t.boolean().optional(),
            "htmlSanitization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingOptionsOut"])
    types["BatchCreateJobsRequestIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["JobIn"]))}
    ).named(renames["BatchCreateJobsRequestIn"])
    types["BatchCreateJobsRequestOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateJobsRequestOut"])
    types["BatchUpdateJobsRequestIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])),
            "updateMask": t.string().optional(),
        }
    ).named(renames["BatchUpdateJobsRequestIn"])
    types["BatchUpdateJobsRequestOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateJobsRequestOut"])
    types["BatchDeleteJobsRequestIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteJobsRequestIn"])
    types["BatchDeleteJobsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteJobsRequestOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["SearchJobsRequestIn"] = t.struct(
        {
            "searchMode": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
            "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
            "enableBroadening": t.boolean().optional(),
            "histogramQueries": t.array(
                t.proxy(renames["HistogramQueryIn"])
            ).optional(),
            "jobView": t.string().optional(),
            "offset": t.integer().optional(),
            "maxPageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
            "diversificationLevel": t.string().optional(),
            "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
            "disableKeywordMatch": t.boolean().optional(),
            "keywordMatchMode": t.string().optional(),
        }
    ).named(renames["SearchJobsRequestIn"])
    types["SearchJobsRequestOut"] = t.struct(
        {
            "searchMode": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]),
            "jobQuery": t.proxy(renames["JobQueryOut"]).optional(),
            "enableBroadening": t.boolean().optional(),
            "histogramQueries": t.array(
                t.proxy(renames["HistogramQueryOut"])
            ).optional(),
            "jobView": t.string().optional(),
            "offset": t.integer().optional(),
            "maxPageSize": t.integer().optional(),
            "pageToken": t.string().optional(),
            "orderBy": t.string().optional(),
            "diversificationLevel": t.string().optional(),
            "customRankingInfo": t.proxy(renames["CustomRankingInfoOut"]).optional(),
            "disableKeywordMatch": t.boolean().optional(),
            "keywordMatchMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchJobsRequestOut"])
    types["RequestMetadataIn"] = t.struct(
        {
            "domain": t.string(),
            "sessionId": t.string(),
            "userId": t.string(),
            "allowMissingIds": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "domain": t.string(),
            "sessionId": t.string(),
            "userId": t.string(),
            "allowMissingIds": t.boolean().optional(),
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["DeviceInfoIn"] = t.struct(
        {"deviceType": t.string().optional(), "id": t.string().optional()}
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["JobQueryIn"] = t.struct(
        {
            "query": t.string().optional(),
            "queryLanguageCode": t.string().optional(),
            "companies": t.array(t.string()).optional(),
            "locationFilters": t.array(t.proxy(renames["LocationFilterIn"])).optional(),
            "jobCategories": t.array(t.string()).optional(),
            "commuteFilter": t.proxy(renames["CommuteFilterIn"]).optional(),
            "companyDisplayNames": t.array(t.string()).optional(),
            "compensationFilter": t.proxy(renames["CompensationFilterIn"]).optional(),
            "customAttributeFilter": t.string().optional(),
            "disableSpellCheck": t.boolean().optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "languageCodes": t.array(t.string()).optional(),
            "publishTimeRange": t.proxy(renames["TimestampRangeIn"]).optional(),
            "excludedJobs": t.array(t.string()).optional(),
        }
    ).named(renames["JobQueryIn"])
    types["JobQueryOut"] = t.struct(
        {
            "query": t.string().optional(),
            "queryLanguageCode": t.string().optional(),
            "companies": t.array(t.string()).optional(),
            "locationFilters": t.array(
                t.proxy(renames["LocationFilterOut"])
            ).optional(),
            "jobCategories": t.array(t.string()).optional(),
            "commuteFilter": t.proxy(renames["CommuteFilterOut"]).optional(),
            "companyDisplayNames": t.array(t.string()).optional(),
            "compensationFilter": t.proxy(renames["CompensationFilterOut"]).optional(),
            "customAttributeFilter": t.string().optional(),
            "disableSpellCheck": t.boolean().optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "languageCodes": t.array(t.string()).optional(),
            "publishTimeRange": t.proxy(renames["TimestampRangeOut"]).optional(),
            "excludedJobs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobQueryOut"])
    types["LocationFilterIn"] = t.struct(
        {
            "address": t.string().optional(),
            "regionCode": t.string().optional(),
            "latLng": t.proxy(renames["LatLngIn"]).optional(),
            "distanceInMiles": t.number().optional(),
            "telecommutePreference": t.string().optional(),
        }
    ).named(renames["LocationFilterIn"])
    types["LocationFilterOut"] = t.struct(
        {
            "address": t.string().optional(),
            "regionCode": t.string().optional(),
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "distanceInMiles": t.number().optional(),
            "telecommutePreference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationFilterOut"])
    types["CommuteFilterIn"] = t.struct(
        {
            "commuteMethod": t.string(),
            "startCoordinates": t.proxy(renames["LatLngIn"]),
            "travelDuration": t.string(),
            "allowImpreciseAddresses": t.boolean().optional(),
            "roadTraffic": t.string().optional(),
            "departureTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["CommuteFilterIn"])
    types["CommuteFilterOut"] = t.struct(
        {
            "commuteMethod": t.string(),
            "startCoordinates": t.proxy(renames["LatLngOut"]),
            "travelDuration": t.string(),
            "allowImpreciseAddresses": t.boolean().optional(),
            "roadTraffic": t.string().optional(),
            "departureTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommuteFilterOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["CompensationFilterIn"] = t.struct(
        {
            "type": t.string(),
            "units": t.array(t.string()),
            "range": t.proxy(renames["CompensationRangeIn"]).optional(),
            "includeJobsWithUnspecifiedCompensationRange": t.boolean().optional(),
        }
    ).named(renames["CompensationFilterIn"])
    types["CompensationFilterOut"] = t.struct(
        {
            "type": t.string(),
            "units": t.array(t.string()),
            "range": t.proxy(renames["CompensationRangeOut"]).optional(),
            "includeJobsWithUnspecifiedCompensationRange": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationFilterOut"])
    types["TimestampRangeIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimestampRangeIn"])
    types["TimestampRangeOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimestampRangeOut"])
    types["HistogramQueryIn"] = t.struct(
        {"histogramQuery": t.string().optional()}
    ).named(renames["HistogramQueryIn"])
    types["HistogramQueryOut"] = t.struct(
        {
            "histogramQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramQueryOut"])
    types["CustomRankingInfoIn"] = t.struct(
        {"importanceLevel": t.string(), "rankingExpression": t.string()}
    ).named(renames["CustomRankingInfoIn"])
    types["CustomRankingInfoOut"] = t.struct(
        {
            "importanceLevel": t.string(),
            "rankingExpression": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomRankingInfoOut"])
    types["SearchJobsResponseIn"] = t.struct(
        {
            "matchingJobs": t.array(t.proxy(renames["MatchingJobIn"])).optional(),
            "histogramQueryResults": t.array(
                t.proxy(renames["HistogramQueryResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "locationFilters": t.array(t.proxy(renames["LocationIn"])).optional(),
            "totalSize": t.integer().optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
            "broadenedQueryJobsCount": t.integer().optional(),
            "spellCorrection": t.proxy(renames["SpellingCorrectionIn"]).optional(),
        }
    ).named(renames["SearchJobsResponseIn"])
    types["SearchJobsResponseOut"] = t.struct(
        {
            "matchingJobs": t.array(t.proxy(renames["MatchingJobOut"])).optional(),
            "histogramQueryResults": t.array(
                t.proxy(renames["HistogramQueryResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "locationFilters": t.array(t.proxy(renames["LocationOut"])).optional(),
            "totalSize": t.integer().optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "broadenedQueryJobsCount": t.integer().optional(),
            "spellCorrection": t.proxy(renames["SpellingCorrectionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchJobsResponseOut"])
    types["MatchingJobIn"] = t.struct(
        {
            "job": t.proxy(renames["JobIn"]).optional(),
            "jobSummary": t.string().optional(),
            "jobTitleSnippet": t.string().optional(),
            "searchTextSnippet": t.string().optional(),
            "commuteInfo": t.proxy(renames["CommuteInfoIn"]).optional(),
        }
    ).named(renames["MatchingJobIn"])
    types["MatchingJobOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "jobSummary": t.string().optional(),
            "jobTitleSnippet": t.string().optional(),
            "searchTextSnippet": t.string().optional(),
            "commuteInfo": t.proxy(renames["CommuteInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchingJobOut"])
    types["CommuteInfoIn"] = t.struct(
        {
            "jobLocation": t.proxy(renames["LocationIn"]).optional(),
            "travelDuration": t.string().optional(),
        }
    ).named(renames["CommuteInfoIn"])
    types["CommuteInfoOut"] = t.struct(
        {
            "jobLocation": t.proxy(renames["LocationOut"]).optional(),
            "travelDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommuteInfoOut"])
    types["HistogramQueryResultIn"] = t.struct(
        {
            "histogramQuery": t.string().optional(),
            "histogram": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["HistogramQueryResultIn"])
    types["HistogramQueryResultOut"] = t.struct(
        {
            "histogramQuery": t.string().optional(),
            "histogram": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramQueryResultOut"])
    types["SpellingCorrectionIn"] = t.struct(
        {
            "corrected": t.boolean().optional(),
            "correctedText": t.string().optional(),
            "correctedHtml": t.string().optional(),
        }
    ).named(renames["SpellingCorrectionIn"])
    types["SpellingCorrectionOut"] = t.struct(
        {
            "corrected": t.boolean().optional(),
            "correctedText": t.string().optional(),
            "correctedHtml": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellingCorrectionOut"])
    types["TenantIn"] = t.struct({"name": t.string(), "externalId": t.string()}).named(
        renames["TenantIn"]
    )
    types["TenantOut"] = t.struct(
        {
            "name": t.string(),
            "externalId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantOut"])
    types["ListTenantsResponseIn"] = t.struct(
        {
            "tenants": t.array(t.proxy(renames["TenantIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
        }
    ).named(renames["ListTenantsResponseIn"])
    types["ListTenantsResponseOut"] = t.struct(
        {
            "tenants": t.array(t.proxy(renames["TenantOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTenantsResponseOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "state": t.string().optional(),
            "stateDescription": t.string().optional(),
            "successCount": t.integer().optional(),
            "failureCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateDescription": t.string().optional(),
            "successCount": t.integer().optional(),
            "failureCount": t.integer().optional(),
            "totalCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["BatchCreateJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchCreateJobsResponseIn"])
    types["BatchCreateJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateJobsResponseOut"])
    types["JobResultIn"] = t.struct(
        {
            "job": t.proxy(renames["JobIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["JobResultIn"])
    types["JobResultOut"] = t.struct(
        {
            "job": t.proxy(renames["JobOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobResultOut"])
    types["BatchUpdateJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchUpdateJobsResponseIn"])
    types["BatchUpdateJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateJobsResponseOut"])
    types["BatchDeleteJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchDeleteJobsResponseIn"])
    types["BatchDeleteJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteJobsResponseOut"])
    types["MendelDebugInputIn"] = t.struct(
        {"namespacedDebugInput": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MendelDebugInputIn"])
    types["MendelDebugInputOut"] = t.struct(
        {
            "namespacedDebugInput": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MendelDebugInputOut"])
    types["NamespacedDebugInputIn"] = t.struct(
        {
            "forcedFlags": t.struct({"_": t.string().optional()}).optional(),
            "forcedRollouts": t.struct({"_": t.string().optional()}).optional(),
            "absolutelyForcedExps": t.array(t.integer()).optional(),
            "conditionallyForcedExps": t.array(t.integer()).optional(),
            "absolutelyForcedExpTags": t.array(t.string()).optional(),
            "conditionallyForcedExpTags": t.array(t.string()).optional(),
            "absolutelyForcedExpNames": t.array(t.string()).optional(),
            "conditionallyForcedExpNames": t.array(t.string()).optional(),
            "disableOrganicSelection": t.boolean().optional(),
            "disableManualEnrollmentSelection": t.boolean().optional(),
            "disableAutomaticEnrollmentSelection": t.boolean().optional(),
            "disableExps": t.array(t.integer()).optional(),
            "disableExpNames": t.array(t.string()).optional(),
            "disableExpTags": t.array(t.string()).optional(),
            "testingMode": t.string().optional(),
        }
    ).named(renames["NamespacedDebugInputIn"])
    types["NamespacedDebugInputOut"] = t.struct(
        {
            "forcedFlags": t.struct({"_": t.string().optional()}).optional(),
            "forcedRollouts": t.struct({"_": t.string().optional()}).optional(),
            "absolutelyForcedExps": t.array(t.integer()).optional(),
            "conditionallyForcedExps": t.array(t.integer()).optional(),
            "absolutelyForcedExpTags": t.array(t.string()).optional(),
            "conditionallyForcedExpTags": t.array(t.string()).optional(),
            "absolutelyForcedExpNames": t.array(t.string()).optional(),
            "conditionallyForcedExpNames": t.array(t.string()).optional(),
            "disableOrganicSelection": t.boolean().optional(),
            "disableManualEnrollmentSelection": t.boolean().optional(),
            "disableAutomaticEnrollmentSelection": t.boolean().optional(),
            "disableExps": t.array(t.integer()).optional(),
            "disableExpNames": t.array(t.string()).optional(),
            "disableExpTags": t.array(t.string()).optional(),
            "testingMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedDebugInputOut"])

    functions = {}
    functions["projectsOperationsGet"] = jobs.get(
        "v4/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompleteQuery"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCreate"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsGet"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsPatch"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsDelete"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsList"] = jobs.get(
        "v4/{parent}/tenants",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTenantsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesCreate"] = jobs.get(
        "v4/{parent}/companies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "requireOpenJobs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCompaniesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesGet"] = jobs.get(
        "v4/{parent}/companies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "requireOpenJobs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCompaniesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesPatch"] = jobs.get(
        "v4/{parent}/companies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "requireOpenJobs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCompaniesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesDelete"] = jobs.get(
        "v4/{parent}/companies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "requireOpenJobs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCompaniesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesList"] = jobs.get(
        "v4/{parent}/companies",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "requireOpenJobs": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCompaniesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsClientEventsCreate"] = jobs.post(
        "v4/{parent}/clientEvents",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "eventId": t.string(),
                "createTime": t.string(),
                "jobEvent": t.proxy(renames["JobEventIn"]).optional(),
                "eventNotes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsCreate"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchCreate"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsGet"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsPatch"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchUpdate"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsDelete"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchDelete"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsList"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsSearch"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsSearchForAlert"] = jobs.post(
        "v4/{parent}/jobs:searchForAlert",
        t.struct(
            {
                "parent": t.string(),
                "searchMode": t.string().optional(),
                "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
                "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
                "enableBroadening": t.boolean().optional(),
                "histogramQueries": t.array(
                    t.proxy(renames["HistogramQueryIn"])
                ).optional(),
                "jobView": t.string().optional(),
                "offset": t.integer().optional(),
                "maxPageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "diversificationLevel": t.string().optional(),
                "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
                "disableKeywordMatch": t.boolean().optional(),
                "keywordMatchMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="jobs", renames=renames, types=types, functions=functions)
