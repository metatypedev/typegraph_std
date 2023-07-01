from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_jobs():
    jobs = HTTPRuntime("https://jobs.googleapis.com/")

    renames = {
        "ErrorResponse": "_jobs_1_ErrorResponse",
        "CompletionResultIn": "_jobs_2_CompletionResultIn",
        "CompletionResultOut": "_jobs_3_CompletionResultOut",
        "BatchCreateJobsRequestIn": "_jobs_4_BatchCreateJobsRequestIn",
        "BatchCreateJobsRequestOut": "_jobs_5_BatchCreateJobsRequestOut",
        "BatchOperationMetadataIn": "_jobs_6_BatchOperationMetadataIn",
        "BatchOperationMetadataOut": "_jobs_7_BatchOperationMetadataOut",
        "TimeOfDayIn": "_jobs_8_TimeOfDayIn",
        "TimeOfDayOut": "_jobs_9_TimeOfDayOut",
        "MendelDebugInputIn": "_jobs_10_MendelDebugInputIn",
        "MendelDebugInputOut": "_jobs_11_MendelDebugInputOut",
        "ListJobsResponseIn": "_jobs_12_ListJobsResponseIn",
        "ListJobsResponseOut": "_jobs_13_ListJobsResponseOut",
        "RequestMetadataIn": "_jobs_14_RequestMetadataIn",
        "RequestMetadataOut": "_jobs_15_RequestMetadataOut",
        "CompensationRangeIn": "_jobs_16_CompensationRangeIn",
        "CompensationRangeOut": "_jobs_17_CompensationRangeOut",
        "CustomRankingInfoIn": "_jobs_18_CustomRankingInfoIn",
        "CustomRankingInfoOut": "_jobs_19_CustomRankingInfoOut",
        "CompensationFilterIn": "_jobs_20_CompensationFilterIn",
        "CompensationFilterOut": "_jobs_21_CompensationFilterOut",
        "CompensationEntryIn": "_jobs_22_CompensationEntryIn",
        "CompensationEntryOut": "_jobs_23_CompensationEntryOut",
        "CompleteQueryResponseIn": "_jobs_24_CompleteQueryResponseIn",
        "CompleteQueryResponseOut": "_jobs_25_CompleteQueryResponseOut",
        "SearchJobsRequestIn": "_jobs_26_SearchJobsRequestIn",
        "SearchJobsRequestOut": "_jobs_27_SearchJobsRequestOut",
        "HistogramQueryIn": "_jobs_28_HistogramQueryIn",
        "HistogramQueryOut": "_jobs_29_HistogramQueryOut",
        "OperationIn": "_jobs_30_OperationIn",
        "OperationOut": "_jobs_31_OperationOut",
        "ListTenantsResponseIn": "_jobs_32_ListTenantsResponseIn",
        "ListTenantsResponseOut": "_jobs_33_ListTenantsResponseOut",
        "MoneyIn": "_jobs_34_MoneyIn",
        "MoneyOut": "_jobs_35_MoneyOut",
        "MatchingJobIn": "_jobs_36_MatchingJobIn",
        "MatchingJobOut": "_jobs_37_MatchingJobOut",
        "TenantIn": "_jobs_38_TenantIn",
        "TenantOut": "_jobs_39_TenantOut",
        "EmptyIn": "_jobs_40_EmptyIn",
        "EmptyOut": "_jobs_41_EmptyOut",
        "BatchDeleteJobsResponseIn": "_jobs_42_BatchDeleteJobsResponseIn",
        "BatchDeleteJobsResponseOut": "_jobs_43_BatchDeleteJobsResponseOut",
        "CommuteFilterIn": "_jobs_44_CommuteFilterIn",
        "CommuteFilterOut": "_jobs_45_CommuteFilterOut",
        "BatchDeleteJobsRequestIn": "_jobs_46_BatchDeleteJobsRequestIn",
        "BatchDeleteJobsRequestOut": "_jobs_47_BatchDeleteJobsRequestOut",
        "JobQueryIn": "_jobs_48_JobQueryIn",
        "JobQueryOut": "_jobs_49_JobQueryOut",
        "NamespacedDebugInputIn": "_jobs_50_NamespacedDebugInputIn",
        "NamespacedDebugInputOut": "_jobs_51_NamespacedDebugInputOut",
        "BatchUpdateJobsResponseIn": "_jobs_52_BatchUpdateJobsResponseIn",
        "BatchUpdateJobsResponseOut": "_jobs_53_BatchUpdateJobsResponseOut",
        "ProcessingOptionsIn": "_jobs_54_ProcessingOptionsIn",
        "ProcessingOptionsOut": "_jobs_55_ProcessingOptionsOut",
        "JobIn": "_jobs_56_JobIn",
        "JobOut": "_jobs_57_JobOut",
        "DeviceInfoIn": "_jobs_58_DeviceInfoIn",
        "DeviceInfoOut": "_jobs_59_DeviceInfoOut",
        "SearchJobsResponseIn": "_jobs_60_SearchJobsResponseIn",
        "SearchJobsResponseOut": "_jobs_61_SearchJobsResponseOut",
        "CompanyDerivedInfoIn": "_jobs_62_CompanyDerivedInfoIn",
        "CompanyDerivedInfoOut": "_jobs_63_CompanyDerivedInfoOut",
        "LocationIn": "_jobs_64_LocationIn",
        "LocationOut": "_jobs_65_LocationOut",
        "TimestampRangeIn": "_jobs_66_TimestampRangeIn",
        "TimestampRangeOut": "_jobs_67_TimestampRangeOut",
        "CustomAttributeIn": "_jobs_68_CustomAttributeIn",
        "CustomAttributeOut": "_jobs_69_CustomAttributeOut",
        "ResponseMetadataIn": "_jobs_70_ResponseMetadataIn",
        "ResponseMetadataOut": "_jobs_71_ResponseMetadataOut",
        "JobEventIn": "_jobs_72_JobEventIn",
        "JobEventOut": "_jobs_73_JobEventOut",
        "BatchUpdateJobsRequestIn": "_jobs_74_BatchUpdateJobsRequestIn",
        "BatchUpdateJobsRequestOut": "_jobs_75_BatchUpdateJobsRequestOut",
        "CommuteInfoIn": "_jobs_76_CommuteInfoIn",
        "CommuteInfoOut": "_jobs_77_CommuteInfoOut",
        "JobDerivedInfoIn": "_jobs_78_JobDerivedInfoIn",
        "JobDerivedInfoOut": "_jobs_79_JobDerivedInfoOut",
        "LocationFilterIn": "_jobs_80_LocationFilterIn",
        "LocationFilterOut": "_jobs_81_LocationFilterOut",
        "JobResultIn": "_jobs_82_JobResultIn",
        "JobResultOut": "_jobs_83_JobResultOut",
        "CompanyIn": "_jobs_84_CompanyIn",
        "CompanyOut": "_jobs_85_CompanyOut",
        "CompensationInfoIn": "_jobs_86_CompensationInfoIn",
        "CompensationInfoOut": "_jobs_87_CompensationInfoOut",
        "ListCompaniesResponseIn": "_jobs_88_ListCompaniesResponseIn",
        "ListCompaniesResponseOut": "_jobs_89_ListCompaniesResponseOut",
        "SpellingCorrectionIn": "_jobs_90_SpellingCorrectionIn",
        "SpellingCorrectionOut": "_jobs_91_SpellingCorrectionOut",
        "LatLngIn": "_jobs_92_LatLngIn",
        "LatLngOut": "_jobs_93_LatLngOut",
        "ApplicationInfoIn": "_jobs_94_ApplicationInfoIn",
        "ApplicationInfoOut": "_jobs_95_ApplicationInfoOut",
        "HistogramQueryResultIn": "_jobs_96_HistogramQueryResultIn",
        "HistogramQueryResultOut": "_jobs_97_HistogramQueryResultOut",
        "ClientEventIn": "_jobs_98_ClientEventIn",
        "ClientEventOut": "_jobs_99_ClientEventOut",
        "StatusIn": "_jobs_100_StatusIn",
        "StatusOut": "_jobs_101_StatusOut",
        "PostalAddressIn": "_jobs_102_PostalAddressIn",
        "PostalAddressOut": "_jobs_103_PostalAddressOut",
        "BatchCreateJobsResponseIn": "_jobs_104_BatchCreateJobsResponseIn",
        "BatchCreateJobsResponseOut": "_jobs_105_BatchCreateJobsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CompletionResultIn"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "suggestion": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["CompletionResultIn"])
    types["CompletionResultOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "suggestion": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompletionResultOut"])
    types["BatchCreateJobsRequestIn"] = t.struct(
        {"jobs": t.array(t.proxy(renames["JobIn"]))}
    ).named(renames["BatchCreateJobsRequestIn"])
    types["BatchCreateJobsRequestOut"] = t.struct(
        {
            "jobs": t.array(t.proxy(renames["JobOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateJobsRequestOut"])
    types["BatchOperationMetadataIn"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.integer().optional(),
            "endTime": t.string().optional(),
            "stateDescription": t.string().optional(),
            "state": t.string().optional(),
            "failureCount": t.integer().optional(),
        }
    ).named(renames["BatchOperationMetadataIn"])
    types["BatchOperationMetadataOut"] = t.struct(
        {
            "totalCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "successCount": t.integer().optional(),
            "endTime": t.string().optional(),
            "stateDescription": t.string().optional(),
            "state": t.string().optional(),
            "failureCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchOperationMetadataOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["MendelDebugInputIn"] = t.struct(
        {"namespacedDebugInput": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["MendelDebugInputIn"])
    types["MendelDebugInputOut"] = t.struct(
        {
            "namespacedDebugInput": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MendelDebugInputOut"])
    types["ListJobsResponseIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
            "jobs": t.array(t.proxy(renames["JobIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListJobsResponseIn"])
    types["ListJobsResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "jobs": t.array(t.proxy(renames["JobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListJobsResponseOut"])
    types["RequestMetadataIn"] = t.struct(
        {
            "deviceInfo": t.proxy(renames["DeviceInfoIn"]).optional(),
            "domain": t.string(),
            "allowMissingIds": t.boolean().optional(),
            "sessionId": t.string(),
            "userId": t.string(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "deviceInfo": t.proxy(renames["DeviceInfoOut"]).optional(),
            "domain": t.string(),
            "allowMissingIds": t.boolean().optional(),
            "sessionId": t.string(),
            "userId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["CompensationRangeIn"] = t.struct(
        {
            "minCompensation": t.proxy(renames["MoneyIn"]).optional(),
            "maxCompensation": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["CompensationRangeIn"])
    types["CompensationRangeOut"] = t.struct(
        {
            "minCompensation": t.proxy(renames["MoneyOut"]).optional(),
            "maxCompensation": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationRangeOut"])
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
    types["CompensationFilterIn"] = t.struct(
        {
            "units": t.array(t.string()),
            "type": t.string(),
            "includeJobsWithUnspecifiedCompensationRange": t.boolean().optional(),
            "range": t.proxy(renames["CompensationRangeIn"]).optional(),
        }
    ).named(renames["CompensationFilterIn"])
    types["CompensationFilterOut"] = t.struct(
        {
            "units": t.array(t.string()),
            "type": t.string(),
            "includeJobsWithUnspecifiedCompensationRange": t.boolean().optional(),
            "range": t.proxy(renames["CompensationRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationFilterOut"])
    types["CompensationEntryIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "amount": t.proxy(renames["MoneyIn"]).optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "expectedUnitsPerYear": t.number().optional(),
            "range": t.proxy(renames["CompensationRangeIn"]).optional(),
        }
    ).named(renames["CompensationEntryIn"])
    types["CompensationEntryOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "amount": t.proxy(renames["MoneyOut"]).optional(),
            "type": t.string().optional(),
            "description": t.string().optional(),
            "expectedUnitsPerYear": t.number().optional(),
            "range": t.proxy(renames["CompensationRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationEntryOut"])
    types["CompleteQueryResponseIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
            "completionResults": t.array(
                t.proxy(renames["CompletionResultIn"])
            ).optional(),
        }
    ).named(renames["CompleteQueryResponseIn"])
    types["CompleteQueryResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "completionResults": t.array(
                t.proxy(renames["CompletionResultOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompleteQueryResponseOut"])
    types["SearchJobsRequestIn"] = t.struct(
        {
            "customRankingInfo": t.proxy(renames["CustomRankingInfoIn"]).optional(),
            "diversificationLevel": t.string().optional(),
            "histogramQueries": t.array(
                t.proxy(renames["HistogramQueryIn"])
            ).optional(),
            "pageToken": t.string().optional(),
            "disableKeywordMatch": t.boolean().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.string().optional(),
            "keywordMatchMode": t.string().optional(),
            "enableBroadening": t.boolean().optional(),
            "searchMode": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]),
            "jobView": t.string().optional(),
            "jobQuery": t.proxy(renames["JobQueryIn"]).optional(),
            "maxPageSize": t.integer().optional(),
        }
    ).named(renames["SearchJobsRequestIn"])
    types["SearchJobsRequestOut"] = t.struct(
        {
            "customRankingInfo": t.proxy(renames["CustomRankingInfoOut"]).optional(),
            "diversificationLevel": t.string().optional(),
            "histogramQueries": t.array(
                t.proxy(renames["HistogramQueryOut"])
            ).optional(),
            "pageToken": t.string().optional(),
            "disableKeywordMatch": t.boolean().optional(),
            "offset": t.integer().optional(),
            "orderBy": t.string().optional(),
            "keywordMatchMode": t.string().optional(),
            "enableBroadening": t.boolean().optional(),
            "searchMode": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]),
            "jobView": t.string().optional(),
            "jobQuery": t.proxy(renames["JobQueryOut"]).optional(),
            "maxPageSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchJobsRequestOut"])
    types["HistogramQueryIn"] = t.struct(
        {"histogramQuery": t.string().optional()}
    ).named(renames["HistogramQueryIn"])
    types["HistogramQueryOut"] = t.struct(
        {
            "histogramQuery": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HistogramQueryOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListTenantsResponseIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
            "tenants": t.array(t.proxy(renames["TenantIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTenantsResponseIn"])
    types["ListTenantsResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "tenants": t.array(t.proxy(renames["TenantOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTenantsResponseOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
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
    types["TenantIn"] = t.struct({"externalId": t.string(), "name": t.string()}).named(
        renames["TenantIn"]
    )
    types["TenantOut"] = t.struct(
        {
            "externalId": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BatchDeleteJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchDeleteJobsResponseIn"])
    types["BatchDeleteJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteJobsResponseOut"])
    types["CommuteFilterIn"] = t.struct(
        {
            "allowImpreciseAddresses": t.boolean().optional(),
            "roadTraffic": t.string().optional(),
            "travelDuration": t.string(),
            "departureTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "commuteMethod": t.string(),
            "startCoordinates": t.proxy(renames["LatLngIn"]),
        }
    ).named(renames["CommuteFilterIn"])
    types["CommuteFilterOut"] = t.struct(
        {
            "allowImpreciseAddresses": t.boolean().optional(),
            "roadTraffic": t.string().optional(),
            "travelDuration": t.string(),
            "departureTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "commuteMethod": t.string(),
            "startCoordinates": t.proxy(renames["LatLngOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommuteFilterOut"])
    types["BatchDeleteJobsRequestIn"] = t.struct(
        {"names": t.array(t.string()).optional()}
    ).named(renames["BatchDeleteJobsRequestIn"])
    types["BatchDeleteJobsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteJobsRequestOut"])
    types["JobQueryIn"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "disableSpellCheck": t.boolean().optional(),
            "compensationFilter": t.proxy(renames["CompensationFilterIn"]).optional(),
            "companyDisplayNames": t.array(t.string()).optional(),
            "publishTimeRange": t.proxy(renames["TimestampRangeIn"]).optional(),
            "customAttributeFilter": t.string().optional(),
            "companies": t.array(t.string()).optional(),
            "locationFilters": t.array(t.proxy(renames["LocationFilterIn"])).optional(),
            "commuteFilter": t.proxy(renames["CommuteFilterIn"]).optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "excludedJobs": t.array(t.string()).optional(),
            "query": t.string().optional(),
            "queryLanguageCode": t.string().optional(),
            "jobCategories": t.array(t.string()).optional(),
        }
    ).named(renames["JobQueryIn"])
    types["JobQueryOut"] = t.struct(
        {
            "languageCodes": t.array(t.string()).optional(),
            "disableSpellCheck": t.boolean().optional(),
            "compensationFilter": t.proxy(renames["CompensationFilterOut"]).optional(),
            "companyDisplayNames": t.array(t.string()).optional(),
            "publishTimeRange": t.proxy(renames["TimestampRangeOut"]).optional(),
            "customAttributeFilter": t.string().optional(),
            "companies": t.array(t.string()).optional(),
            "locationFilters": t.array(
                t.proxy(renames["LocationFilterOut"])
            ).optional(),
            "commuteFilter": t.proxy(renames["CommuteFilterOut"]).optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "excludedJobs": t.array(t.string()).optional(),
            "query": t.string().optional(),
            "queryLanguageCode": t.string().optional(),
            "jobCategories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobQueryOut"])
    types["NamespacedDebugInputIn"] = t.struct(
        {
            "absolutelyForcedExps": t.array(t.integer()).optional(),
            "conditionallyForcedExpNames": t.array(t.string()).optional(),
            "absolutelyForcedExpNames": t.array(t.string()).optional(),
            "conditionallyForcedExpTags": t.array(t.string()).optional(),
            "forcedRollouts": t.struct({"_": t.string().optional()}).optional(),
            "disableAutomaticEnrollmentSelection": t.boolean().optional(),
            "disableManualEnrollmentSelection": t.boolean().optional(),
            "disableOrganicSelection": t.boolean().optional(),
            "disableExpNames": t.array(t.string()).optional(),
            "forcedFlags": t.struct({"_": t.string().optional()}).optional(),
            "testingMode": t.string().optional(),
            "conditionallyForcedExps": t.array(t.integer()).optional(),
            "absolutelyForcedExpTags": t.array(t.string()).optional(),
            "disableExps": t.array(t.integer()).optional(),
            "disableExpTags": t.array(t.string()).optional(),
        }
    ).named(renames["NamespacedDebugInputIn"])
    types["NamespacedDebugInputOut"] = t.struct(
        {
            "absolutelyForcedExps": t.array(t.integer()).optional(),
            "conditionallyForcedExpNames": t.array(t.string()).optional(),
            "absolutelyForcedExpNames": t.array(t.string()).optional(),
            "conditionallyForcedExpTags": t.array(t.string()).optional(),
            "forcedRollouts": t.struct({"_": t.string().optional()}).optional(),
            "disableAutomaticEnrollmentSelection": t.boolean().optional(),
            "disableManualEnrollmentSelection": t.boolean().optional(),
            "disableOrganicSelection": t.boolean().optional(),
            "disableExpNames": t.array(t.string()).optional(),
            "forcedFlags": t.struct({"_": t.string().optional()}).optional(),
            "testingMode": t.string().optional(),
            "conditionallyForcedExps": t.array(t.integer()).optional(),
            "absolutelyForcedExpTags": t.array(t.string()).optional(),
            "disableExps": t.array(t.integer()).optional(),
            "disableExpTags": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedDebugInputOut"])
    types["BatchUpdateJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchUpdateJobsResponseIn"])
    types["BatchUpdateJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateJobsResponseOut"])
    types["ProcessingOptionsIn"] = t.struct(
        {
            "htmlSanitization": t.string().optional(),
            "disableStreetAddressResolution": t.boolean().optional(),
        }
    ).named(renames["ProcessingOptionsIn"])
    types["ProcessingOptionsOut"] = t.struct(
        {
            "htmlSanitization": t.string().optional(),
            "disableStreetAddressResolution": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProcessingOptionsOut"])
    types["JobIn"] = t.struct(
        {
            "postingExpireTime": t.string().optional(),
            "title": t.string(),
            "addresses": t.array(t.string()).optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "visibility": t.string().optional(),
            "jobLevel": t.string().optional(),
            "customAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "jobStartTime": t.string().optional(),
            "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
            "requisitionId": t.string(),
            "jobEndTime": t.string().optional(),
            "department": t.string().optional(),
            "jobBenefits": t.array(t.string()).optional(),
            "postingPublishTime": t.string().optional(),
            "degreeTypes": t.array(t.string()).optional(),
            "postingRegion": t.string().optional(),
            "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
            "description": t.string(),
            "company": t.string(),
            "promotionValue": t.integer().optional(),
            "qualifications": t.string().optional(),
            "languageCode": t.string().optional(),
            "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
            "incentives": t.string().optional(),
            "responsibilities": t.string().optional(),
        }
    ).named(renames["JobIn"])
    types["JobOut"] = t.struct(
        {
            "postingExpireTime": t.string().optional(),
            "postingUpdateTime": t.string().optional(),
            "title": t.string(),
            "addresses": t.array(t.string()).optional(),
            "employmentTypes": t.array(t.string()).optional(),
            "visibility": t.string().optional(),
            "jobLevel": t.string().optional(),
            "customAttributes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "jobStartTime": t.string().optional(),
            "postingCreateTime": t.string().optional(),
            "processingOptions": t.proxy(renames["ProcessingOptionsOut"]).optional(),
            "requisitionId": t.string(),
            "jobEndTime": t.string().optional(),
            "department": t.string().optional(),
            "companyDisplayName": t.string().optional(),
            "jobBenefits": t.array(t.string()).optional(),
            "postingPublishTime": t.string().optional(),
            "degreeTypes": t.array(t.string()).optional(),
            "postingRegion": t.string().optional(),
            "applicationInfo": t.proxy(renames["ApplicationInfoOut"]).optional(),
            "description": t.string(),
            "derivedInfo": t.proxy(renames["JobDerivedInfoOut"]).optional(),
            "company": t.string(),
            "promotionValue": t.integer().optional(),
            "qualifications": t.string().optional(),
            "languageCode": t.string().optional(),
            "compensationInfo": t.proxy(renames["CompensationInfoOut"]).optional(),
            "incentives": t.string().optional(),
            "responsibilities": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JobOut"])
    types["DeviceInfoIn"] = t.struct(
        {"id": t.string().optional(), "deviceType": t.string().optional()}
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "id": t.string().optional(),
            "deviceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["SearchJobsResponseIn"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
            "totalSize": t.integer().optional(),
            "matchingJobs": t.array(t.proxy(renames["MatchingJobIn"])).optional(),
            "locationFilters": t.array(t.proxy(renames["LocationIn"])).optional(),
            "histogramQueryResults": t.array(
                t.proxy(renames["HistogramQueryResultIn"])
            ).optional(),
            "spellCorrection": t.proxy(renames["SpellingCorrectionIn"]).optional(),
            "nextPageToken": t.string().optional(),
            "broadenedQueryJobsCount": t.integer().optional(),
        }
    ).named(renames["SearchJobsResponseIn"])
    types["SearchJobsResponseOut"] = t.struct(
        {
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "totalSize": t.integer().optional(),
            "matchingJobs": t.array(t.proxy(renames["MatchingJobOut"])).optional(),
            "locationFilters": t.array(t.proxy(renames["LocationOut"])).optional(),
            "histogramQueryResults": t.array(
                t.proxy(renames["HistogramQueryResultOut"])
            ).optional(),
            "spellCorrection": t.proxy(renames["SpellingCorrectionOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "broadenedQueryJobsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchJobsResponseOut"])
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
            "latLng": t.proxy(renames["LatLngIn"]).optional(),
            "postalAddress": t.proxy(renames["PostalAddressIn"]).optional(),
            "radiusMiles": t.number().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationType": t.string().optional(),
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "postalAddress": t.proxy(renames["PostalAddressOut"]).optional(),
            "radiusMiles": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["CustomAttributeIn"] = t.struct(
        {
            "longValues": t.array(t.string()).optional(),
            "stringValues": t.array(t.string()).optional(),
            "filterable": t.boolean().optional(),
            "keywordSearchable": t.boolean().optional(),
        }
    ).named(renames["CustomAttributeIn"])
    types["CustomAttributeOut"] = t.struct(
        {
            "longValues": t.array(t.string()).optional(),
            "stringValues": t.array(t.string()).optional(),
            "filterable": t.boolean().optional(),
            "keywordSearchable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAttributeOut"])
    types["ResponseMetadataIn"] = t.struct({"requestId": t.string().optional()}).named(
        renames["ResponseMetadataIn"]
    )
    types["ResponseMetadataOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseMetadataOut"])
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
    types["LocationFilterIn"] = t.struct(
        {
            "distanceInMiles": t.number().optional(),
            "regionCode": t.string().optional(),
            "latLng": t.proxy(renames["LatLngIn"]).optional(),
            "address": t.string().optional(),
            "telecommutePreference": t.string().optional(),
        }
    ).named(renames["LocationFilterIn"])
    types["LocationFilterOut"] = t.struct(
        {
            "distanceInMiles": t.number().optional(),
            "regionCode": t.string().optional(),
            "latLng": t.proxy(renames["LatLngOut"]).optional(),
            "address": t.string().optional(),
            "telecommutePreference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationFilterOut"])
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
    types["CompanyIn"] = t.struct(
        {
            "eeoText": t.string().optional(),
            "size": t.string().optional(),
            "displayName": t.string(),
            "websiteUri": t.string().optional(),
            "headquartersAddress": t.string().optional(),
            "careerSiteUri": t.string().optional(),
            "hiringAgency": t.boolean().optional(),
            "name": t.string(),
            "keywordSearchableJobCustomAttributes": t.array(t.string()).optional(),
            "externalId": t.string(),
            "imageUri": t.string().optional(),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "eeoText": t.string().optional(),
            "size": t.string().optional(),
            "displayName": t.string(),
            "websiteUri": t.string().optional(),
            "headquartersAddress": t.string().optional(),
            "careerSiteUri": t.string().optional(),
            "hiringAgency": t.boolean().optional(),
            "derivedInfo": t.proxy(renames["CompanyDerivedInfoOut"]).optional(),
            "name": t.string(),
            "keywordSearchableJobCustomAttributes": t.array(t.string()).optional(),
            "externalId": t.string(),
            "imageUri": t.string().optional(),
            "suspended": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyOut"])
    types["CompensationInfoIn"] = t.struct(
        {"entries": t.array(t.proxy(renames["CompensationEntryIn"])).optional()}
    ).named(renames["CompensationInfoIn"])
    types["CompensationInfoOut"] = t.struct(
        {
            "annualizedBaseCompensationRange": t.proxy(
                renames["CompensationRangeOut"]
            ).optional(),
            "entries": t.array(t.proxy(renames["CompensationEntryOut"])).optional(),
            "annualizedTotalCompensationRange": t.proxy(
                renames["CompensationRangeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompensationInfoOut"])
    types["ListCompaniesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "companies": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "metadata": t.proxy(renames["ResponseMetadataIn"]).optional(),
        }
    ).named(renames["ListCompaniesResponseIn"])
    types["ListCompaniesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "companies": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "metadata": t.proxy(renames["ResponseMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCompaniesResponseOut"])
    types["SpellingCorrectionIn"] = t.struct(
        {
            "correctedHtml": t.string().optional(),
            "correctedText": t.string().optional(),
            "corrected": t.boolean().optional(),
        }
    ).named(renames["SpellingCorrectionIn"])
    types["SpellingCorrectionOut"] = t.struct(
        {
            "correctedHtml": t.string().optional(),
            "correctedText": t.string().optional(),
            "corrected": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpellingCorrectionOut"])
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
    types["ApplicationInfoIn"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "instruction": t.string().optional(),
        }
    ).named(renames["ApplicationInfoIn"])
    types["ApplicationInfoOut"] = t.struct(
        {
            "emails": t.array(t.string()).optional(),
            "uris": t.array(t.string()).optional(),
            "instruction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationInfoOut"])
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
    types["ClientEventIn"] = t.struct(
        {
            "createTime": t.string(),
            "eventId": t.string(),
            "jobEvent": t.proxy(renames["JobEventIn"]).optional(),
            "requestId": t.string().optional(),
            "eventNotes": t.string().optional(),
        }
    ).named(renames["ClientEventIn"])
    types["ClientEventOut"] = t.struct(
        {
            "createTime": t.string(),
            "eventId": t.string(),
            "jobEvent": t.proxy(renames["JobEventOut"]).optional(),
            "requestId": t.string().optional(),
            "eventNotes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientEventOut"])
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
    types["PostalAddressIn"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "locality": t.string().optional(),
            "sortingCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "regionCode": t.string(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "revision": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["BatchCreateJobsResponseIn"] = t.struct(
        {"jobResults": t.array(t.proxy(renames["JobResultIn"])).optional()}
    ).named(renames["BatchCreateJobsResponseIn"])
    types["BatchCreateJobsResponseOut"] = t.struct(
        {
            "jobResults": t.array(t.proxy(renames["JobResultOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateJobsResponseOut"])

    functions = {}
    functions["projectsOperationsGet"] = jobs.get(
        "v4/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCreate"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsList"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompleteQuery"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsGet"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsDelete"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsPatch"] = jobs.patch(
        "v4/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string().optional(),
                "externalId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TenantOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesPatch"] = jobs.delete(
        "v4/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesGet"] = jobs.delete(
        "v4/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesList"] = jobs.delete(
        "v4/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesCreate"] = jobs.delete(
        "v4/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsCompaniesDelete"] = jobs.delete(
        "v4/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchUpdate"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchCreate"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsDelete"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsBatchDelete"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsSearchForAlert"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsGet"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsPatch"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsSearch"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsList"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsJobsCreate"] = jobs.post(
        "v4/{parent}/jobs",
        t.struct(
            {
                "parent": t.string(),
                "postingExpireTime": t.string().optional(),
                "title": t.string(),
                "addresses": t.array(t.string()).optional(),
                "employmentTypes": t.array(t.string()).optional(),
                "visibility": t.string().optional(),
                "jobLevel": t.string().optional(),
                "customAttributes": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "jobStartTime": t.string().optional(),
                "processingOptions": t.proxy(renames["ProcessingOptionsIn"]).optional(),
                "requisitionId": t.string(),
                "jobEndTime": t.string().optional(),
                "department": t.string().optional(),
                "jobBenefits": t.array(t.string()).optional(),
                "postingPublishTime": t.string().optional(),
                "degreeTypes": t.array(t.string()).optional(),
                "postingRegion": t.string().optional(),
                "applicationInfo": t.proxy(renames["ApplicationInfoIn"]).optional(),
                "description": t.string(),
                "company": t.string(),
                "promotionValue": t.integer().optional(),
                "qualifications": t.string().optional(),
                "languageCode": t.string().optional(),
                "compensationInfo": t.proxy(renames["CompensationInfoIn"]).optional(),
                "incentives": t.string().optional(),
                "responsibilities": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["JobOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTenantsClientEventsCreate"] = jobs.post(
        "v4/{parent}/clientEvents",
        t.struct(
            {
                "parent": t.string(),
                "createTime": t.string(),
                "eventId": t.string(),
                "jobEvent": t.proxy(renames["JobEventIn"]).optional(),
                "requestId": t.string().optional(),
                "eventNotes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientEventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="jobs", renames=renames, types=Box(types), functions=Box(functions)
    )
