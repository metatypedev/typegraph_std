from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datapipelines() -> Import:
    datapipelines = HTTPRuntime("https://datapipelines.googleapis.com/")

    renames = {
        "ErrorResponse": "_datapipelines_1_ErrorResponse",
        "GoogleCloudDatapipelinesV1SdkVersionIn": "_datapipelines_2_GoogleCloudDatapipelinesV1SdkVersionIn",
        "GoogleCloudDatapipelinesV1SdkVersionOut": "_datapipelines_3_GoogleCloudDatapipelinesV1SdkVersionOut",
        "GoogleProtobufEmptyIn": "_datapipelines_4_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datapipelines_5_GoogleProtobufEmptyOut",
        "GoogleRpcStatusIn": "_datapipelines_6_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datapipelines_7_GoogleRpcStatusOut",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentIn": "_datapipelines_8_GoogleCloudDatapipelinesV1RuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentOut": "_datapipelines_9_GoogleCloudDatapipelinesV1RuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn": "_datapipelines_10_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut": "_datapipelines_11_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut",
        "GoogleCloudDatapipelinesV1RunPipelineRequestIn": "_datapipelines_12_GoogleCloudDatapipelinesV1RunPipelineRequestIn",
        "GoogleCloudDatapipelinesV1RunPipelineRequestOut": "_datapipelines_13_GoogleCloudDatapipelinesV1RunPipelineRequestOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersIn": "_datapipelines_14_GoogleCloudDatapipelinesV1LaunchTemplateParametersIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersOut": "_datapipelines_15_GoogleCloudDatapipelinesV1LaunchTemplateParametersOut",
        "GoogleCloudDatapipelinesV1WorkloadIn": "_datapipelines_16_GoogleCloudDatapipelinesV1WorkloadIn",
        "GoogleCloudDatapipelinesV1WorkloadOut": "_datapipelines_17_GoogleCloudDatapipelinesV1WorkloadOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn": "_datapipelines_18_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut": "_datapipelines_19_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut",
        "GoogleCloudDatapipelinesV1RunPipelineResponseIn": "_datapipelines_20_GoogleCloudDatapipelinesV1RunPipelineResponseIn",
        "GoogleCloudDatapipelinesV1RunPipelineResponseOut": "_datapipelines_21_GoogleCloudDatapipelinesV1RunPipelineResponseOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestIn": "_datapipelines_22_GoogleCloudDatapipelinesV1LaunchTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestOut": "_datapipelines_23_GoogleCloudDatapipelinesV1LaunchTemplateRequestOut",
        "GoogleCloudDatapipelinesV1StopPipelineRequestIn": "_datapipelines_24_GoogleCloudDatapipelinesV1StopPipelineRequestIn",
        "GoogleCloudDatapipelinesV1StopPipelineRequestOut": "_datapipelines_25_GoogleCloudDatapipelinesV1StopPipelineRequestOut",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsIn": "_datapipelines_26_GoogleCloudDatapipelinesV1DataflowJobDetailsIn",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsOut": "_datapipelines_27_GoogleCloudDatapipelinesV1DataflowJobDetailsOut",
        "GoogleCloudDatapipelinesV1ScheduleSpecIn": "_datapipelines_28_GoogleCloudDatapipelinesV1ScheduleSpecIn",
        "GoogleCloudDatapipelinesV1ScheduleSpecOut": "_datapipelines_29_GoogleCloudDatapipelinesV1ScheduleSpecOut",
        "GoogleCloudDatapipelinesV1JobIn": "_datapipelines_30_GoogleCloudDatapipelinesV1JobIn",
        "GoogleCloudDatapipelinesV1JobOut": "_datapipelines_31_GoogleCloudDatapipelinesV1JobOut",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseIn": "_datapipelines_32_GoogleCloudDatapipelinesV1ListPipelinesResponseIn",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseOut": "_datapipelines_33_GoogleCloudDatapipelinesV1ListPipelinesResponseOut",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn": "_datapipelines_34_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut": "_datapipelines_35_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1ListJobsResponseIn": "_datapipelines_36_GoogleCloudDatapipelinesV1ListJobsResponseIn",
        "GoogleCloudDatapipelinesV1ListJobsResponseOut": "_datapipelines_37_GoogleCloudDatapipelinesV1ListJobsResponseOut",
        "GoogleCloudDatapipelinesV1PipelineIn": "_datapipelines_38_GoogleCloudDatapipelinesV1PipelineIn",
        "GoogleCloudDatapipelinesV1PipelineOut": "_datapipelines_39_GoogleCloudDatapipelinesV1PipelineOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatapipelinesV1SdkVersionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "versionDisplayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionIn"])
    types["GoogleCloudDatapipelinesV1SdkVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "versionDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "zone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "workerRegion": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "workerZone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "zone": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "subnetwork": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "workerRegion": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "workerZone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "location": t.string(),
            "projectId": t.string(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"]
            ),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "location": t.string(),
            "projectId": t.string(),
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
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"]
            ).optional(),
            "jobName": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"]
            ).optional(),
            "jobName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"])
    types["GoogleCloudDatapipelinesV1WorkloadIn"] = t.struct(
        {
            "dataflowFlexTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"]
            ).optional(),
            "dataflowLaunchTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1WorkloadIn"])
    types["GoogleCloudDatapipelinesV1WorkloadOut"] = t.struct(
        {
            "dataflowFlexTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"]
            ).optional(),
            "dataflowLaunchTemplateRequest": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1WorkloadOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "update": t.boolean().optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "jobName": t.string(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "update": t.boolean().optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDatapipelinesV1JobIn"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDatapipelinesV1JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseOut"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"] = t.struct(
        {
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"]
            ).optional(),
            "location": t.string().optional(),
            "gcsPath": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"]
            ).optional(),
            "location": t.string().optional(),
            "gcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"] = t.struct(
        {"resourceInfo": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"])
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"] = t.struct(
        {
            "currentWorkers": t.integer().optional(),
            "sdkVersion": t.proxy(
                renames["GoogleCloudDatapipelinesV1SdkVersionOut"]
            ).optional(),
            "resourceInfo": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecIn"] = t.struct(
        {"schedule": t.string().optional(), "timeZone": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecOut"] = t.struct(
        {
            "nextJobTime": t.string().optional(),
            "schedule": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"])
    types["GoogleCloudDatapipelinesV1JobIn"] = t.struct(
        {
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"]
            ).optional(),
            "state": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobIn"])
    types["GoogleCloudDatapipelinesV1JobOut"] = t.struct(
        {
            "id": t.string().optional(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobOut"])
    types["GoogleCloudDatapipelinesV1ListPipelinesResponseIn"] = t.struct(
        {
            "pipelines": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1PipelineIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListPipelinesResponseIn"])
    types["GoogleCloudDatapipelinesV1ListPipelinesResponseOut"] = t.struct(
        {
            "pipelines": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListPipelinesResponseOut"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "tempLocation": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "workerZone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "maxWorkers": t.integer().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "serviceAccountEmail": t.string().optional(),
            "tempLocation": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "network": t.string().optional(),
            "workerZone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "maxWorkers": t.integer().optional(),
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
    types["GoogleCloudDatapipelinesV1PipelineIn"] = t.struct(
        {
            "state": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
            ).optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadIn"]
            ).optional(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineIn"])
    types["GoogleCloudDatapipelinesV1PipelineOut"] = t.struct(
        {
            "state": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"]
            ).optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdateTime": t.string().optional(),
            "type": t.string(),
            "createTime": t.string().optional(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadOut"]
            ).optional(),
            "jobCount": t.integer().optional(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineOut"])

    functions = {}
    functions["projectsLocationsPipelinesRun"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesPatch"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesDelete"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesStop"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesList"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesCreate"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesGet"] = datapipelines.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesJobsList"] = datapipelines.get(
        "v1/{parent}/jobs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1ListJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datapipelines", renames=renames, types=types, functions=functions
    )
