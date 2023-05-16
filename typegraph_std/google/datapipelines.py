from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datapipelines() -> Import:
    datapipelines = HTTPRuntime("https://datapipelines.googleapis.com/")

    renames = {
        "ErrorResponse": "_datapipelines_1_ErrorResponse",
        "GoogleCloudDatapipelinesV1PipelineIn": "_datapipelines_2_GoogleCloudDatapipelinesV1PipelineIn",
        "GoogleCloudDatapipelinesV1PipelineOut": "_datapipelines_3_GoogleCloudDatapipelinesV1PipelineOut",
        "GoogleRpcStatusIn": "_datapipelines_4_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datapipelines_5_GoogleRpcStatusOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersIn": "_datapipelines_6_GoogleCloudDatapipelinesV1LaunchTemplateParametersIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersOut": "_datapipelines_7_GoogleCloudDatapipelinesV1LaunchTemplateParametersOut",
        "GoogleCloudDatapipelinesV1WorkloadIn": "_datapipelines_8_GoogleCloudDatapipelinesV1WorkloadIn",
        "GoogleCloudDatapipelinesV1WorkloadOut": "_datapipelines_9_GoogleCloudDatapipelinesV1WorkloadOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn": "_datapipelines_10_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut": "_datapipelines_11_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut",
        "GoogleCloudDatapipelinesV1RunPipelineRequestIn": "_datapipelines_12_GoogleCloudDatapipelinesV1RunPipelineRequestIn",
        "GoogleCloudDatapipelinesV1RunPipelineRequestOut": "_datapipelines_13_GoogleCloudDatapipelinesV1RunPipelineRequestOut",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentIn": "_datapipelines_14_GoogleCloudDatapipelinesV1RuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentOut": "_datapipelines_15_GoogleCloudDatapipelinesV1RuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseIn": "_datapipelines_16_GoogleCloudDatapipelinesV1ListPipelinesResponseIn",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseOut": "_datapipelines_17_GoogleCloudDatapipelinesV1ListPipelinesResponseOut",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsIn": "_datapipelines_18_GoogleCloudDatapipelinesV1DataflowJobDetailsIn",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsOut": "_datapipelines_19_GoogleCloudDatapipelinesV1DataflowJobDetailsOut",
        "GoogleCloudDatapipelinesV1StopPipelineRequestIn": "_datapipelines_20_GoogleCloudDatapipelinesV1StopPipelineRequestIn",
        "GoogleCloudDatapipelinesV1StopPipelineRequestOut": "_datapipelines_21_GoogleCloudDatapipelinesV1StopPipelineRequestOut",
        "GoogleCloudDatapipelinesV1SdkVersionIn": "_datapipelines_22_GoogleCloudDatapipelinesV1SdkVersionIn",
        "GoogleCloudDatapipelinesV1SdkVersionOut": "_datapipelines_23_GoogleCloudDatapipelinesV1SdkVersionOut",
        "GoogleCloudDatapipelinesV1RunPipelineResponseIn": "_datapipelines_24_GoogleCloudDatapipelinesV1RunPipelineResponseIn",
        "GoogleCloudDatapipelinesV1RunPipelineResponseOut": "_datapipelines_25_GoogleCloudDatapipelinesV1RunPipelineResponseOut",
        "GoogleCloudDatapipelinesV1JobIn": "_datapipelines_26_GoogleCloudDatapipelinesV1JobIn",
        "GoogleCloudDatapipelinesV1JobOut": "_datapipelines_27_GoogleCloudDatapipelinesV1JobOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn": "_datapipelines_28_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut": "_datapipelines_29_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn": "_datapipelines_30_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut": "_datapipelines_31_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1ListJobsResponseIn": "_datapipelines_32_GoogleCloudDatapipelinesV1ListJobsResponseIn",
        "GoogleCloudDatapipelinesV1ListJobsResponseOut": "_datapipelines_33_GoogleCloudDatapipelinesV1ListJobsResponseOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestIn": "_datapipelines_34_GoogleCloudDatapipelinesV1LaunchTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestOut": "_datapipelines_35_GoogleCloudDatapipelinesV1LaunchTemplateRequestOut",
        "GoogleProtobufEmptyIn": "_datapipelines_36_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datapipelines_37_GoogleProtobufEmptyOut",
        "GoogleCloudDatapipelinesV1ScheduleSpecIn": "_datapipelines_38_GoogleCloudDatapipelinesV1ScheduleSpecIn",
        "GoogleCloudDatapipelinesV1ScheduleSpecOut": "_datapipelines_39_GoogleCloudDatapipelinesV1ScheduleSpecOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatapipelinesV1PipelineIn"] = t.struct(
        {
            "state": t.string(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "displayName": t.string(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadIn"]
            ).optional(),
            "name": t.string().optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
            ).optional(),
            "type": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineIn"])
    types["GoogleCloudDatapipelinesV1PipelineOut"] = t.struct(
        {
            "state": t.string(),
            "lastUpdateTime": t.string().optional(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "displayName": t.string(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadOut"]
            ).optional(),
            "name": t.string().optional(),
            "jobCount": t.integer().optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"]
            ).optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineOut"])
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
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"])
    types["GoogleCloudDatapipelinesV1WorkloadIn"] = t.struct(
        {
            "dataflowLaunchTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"]
            ).optional(),
            "dataflowFlexTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1WorkloadIn"])
    types["GoogleCloudDatapipelinesV1WorkloadOut"] = t.struct(
        {
            "dataflowLaunchTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"]
            ).optional(),
            "dataflowFlexTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1WorkloadOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "location": t.string(),
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"]
            ),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "location": t.string(),
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "machineType": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "tempLocation": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "subnetwork": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "machineType": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "tempLocation": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "subnetwork": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1ListPipelinesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pipelines": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1PipelineIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListPipelinesResponseIn"])
    types["GoogleCloudDatapipelinesV1ListPipelinesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "pipelines": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListPipelinesResponseOut"])
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"] = t.struct(
        {"resourceInfo": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"])
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"] = t.struct(
        {
            "resourceInfo": t.struct({"_": t.string().optional()}).optional(),
            "currentWorkers": t.integer().optional(),
            "sdkVersion": t.proxy(
                renames["GoogleCloudDatapipelinesV1SdkVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1SdkVersionIn"] = t.struct(
        {
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionIn"])
    types["GoogleCloudDatapipelinesV1SdkVersionOut"] = t.struct(
        {
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDatapipelinesV1JobIn"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDatapipelinesV1JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseOut"])
    types["GoogleCloudDatapipelinesV1JobIn"] = t.struct(
        {
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobIn"])
    types["GoogleCloudDatapipelinesV1JobOut"] = t.struct(
        {
            "id": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "name": t.string(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "containerSpecGcsPath": t.string().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "tempLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string().optional(),
            "zone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "maxWorkers": t.integer().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "flexrsGoal": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "tempLocation": t.string().optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string().optional(),
            "zone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "maxWorkers": t.integer().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "flexrsGoal": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerZone": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1ListJobsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1JobIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListJobsResponseIn"])
    types["GoogleCloudDatapipelinesV1ListJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "jobs": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1JobOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListJobsResponseOut"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"]
            ).optional(),
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "gcsPath": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"]
            ).optional(),
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "gcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecIn"] = t.struct(
        {"timeZone": t.string().optional(), "schedule": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "nextJobTime": t.string().optional(),
            "schedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"])

    functions = {}
    functions["projectsLocationsPipelinesCreate"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesRun"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesStop"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesPatch"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesGet"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesList"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesDelete"] = datapipelines.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesJobsList"] = datapipelines.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datapipelines",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
