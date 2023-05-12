from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datapipelines() -> Import:
    datapipelines = HTTPRuntime("https://datapipelines.googleapis.com/")

    renames = {
        "ErrorResponse": "_datapipelines_1_ErrorResponse",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentIn": "_datapipelines_2_GoogleCloudDatapipelinesV1RuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentOut": "_datapipelines_3_GoogleCloudDatapipelinesV1RuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1ScheduleSpecIn": "_datapipelines_4_GoogleCloudDatapipelinesV1ScheduleSpecIn",
        "GoogleCloudDatapipelinesV1ScheduleSpecOut": "_datapipelines_5_GoogleCloudDatapipelinesV1ScheduleSpecOut",
        "GoogleCloudDatapipelinesV1RunPipelineResponseIn": "_datapipelines_6_GoogleCloudDatapipelinesV1RunPipelineResponseIn",
        "GoogleCloudDatapipelinesV1RunPipelineResponseOut": "_datapipelines_7_GoogleCloudDatapipelinesV1RunPipelineResponseOut",
        "GoogleProtobufEmptyIn": "_datapipelines_8_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datapipelines_9_GoogleProtobufEmptyOut",
        "GoogleCloudDatapipelinesV1WorkloadIn": "_datapipelines_10_GoogleCloudDatapipelinesV1WorkloadIn",
        "GoogleCloudDatapipelinesV1WorkloadOut": "_datapipelines_11_GoogleCloudDatapipelinesV1WorkloadOut",
        "GoogleRpcStatusIn": "_datapipelines_12_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datapipelines_13_GoogleRpcStatusOut",
        "GoogleCloudDatapipelinesV1RunPipelineRequestIn": "_datapipelines_14_GoogleCloudDatapipelinesV1RunPipelineRequestIn",
        "GoogleCloudDatapipelinesV1RunPipelineRequestOut": "_datapipelines_15_GoogleCloudDatapipelinesV1RunPipelineRequestOut",
        "GoogleCloudDatapipelinesV1ListJobsResponseIn": "_datapipelines_16_GoogleCloudDatapipelinesV1ListJobsResponseIn",
        "GoogleCloudDatapipelinesV1ListJobsResponseOut": "_datapipelines_17_GoogleCloudDatapipelinesV1ListJobsResponseOut",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsIn": "_datapipelines_18_GoogleCloudDatapipelinesV1DataflowJobDetailsIn",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsOut": "_datapipelines_19_GoogleCloudDatapipelinesV1DataflowJobDetailsOut",
        "GoogleCloudDatapipelinesV1PipelineIn": "_datapipelines_20_GoogleCloudDatapipelinesV1PipelineIn",
        "GoogleCloudDatapipelinesV1PipelineOut": "_datapipelines_21_GoogleCloudDatapipelinesV1PipelineOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersIn": "_datapipelines_22_GoogleCloudDatapipelinesV1LaunchTemplateParametersIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersOut": "_datapipelines_23_GoogleCloudDatapipelinesV1LaunchTemplateParametersOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestIn": "_datapipelines_24_GoogleCloudDatapipelinesV1LaunchTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestOut": "_datapipelines_25_GoogleCloudDatapipelinesV1LaunchTemplateRequestOut",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn": "_datapipelines_26_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut": "_datapipelines_27_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1StopPipelineRequestIn": "_datapipelines_28_GoogleCloudDatapipelinesV1StopPipelineRequestIn",
        "GoogleCloudDatapipelinesV1StopPipelineRequestOut": "_datapipelines_29_GoogleCloudDatapipelinesV1StopPipelineRequestOut",
        "GoogleCloudDatapipelinesV1SdkVersionIn": "_datapipelines_30_GoogleCloudDatapipelinesV1SdkVersionIn",
        "GoogleCloudDatapipelinesV1SdkVersionOut": "_datapipelines_31_GoogleCloudDatapipelinesV1SdkVersionOut",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseIn": "_datapipelines_32_GoogleCloudDatapipelinesV1ListPipelinesResponseIn",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseOut": "_datapipelines_33_GoogleCloudDatapipelinesV1ListPipelinesResponseOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn": "_datapipelines_34_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut": "_datapipelines_35_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut",
        "GoogleCloudDatapipelinesV1JobIn": "_datapipelines_36_GoogleCloudDatapipelinesV1JobIn",
        "GoogleCloudDatapipelinesV1JobOut": "_datapipelines_37_GoogleCloudDatapipelinesV1JobOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn": "_datapipelines_38_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut": "_datapipelines_39_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "workerZone": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "subnetwork": t.string().optional(),
            "workerZone": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "kmsKeyName": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "workerRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecIn"] = t.struct(
        {"timeZone": t.string().optional(), "schedule": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "schedule": t.string().optional(),
            "nextJobTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseIn"] = t.struct(
        {"job": t.proxy(renames["GoogleCloudDatapipelinesV1JobIn"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineResponseOut"] = t.struct(
        {
            "job": t.proxy(renames["GoogleCloudDatapipelinesV1JobOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestOut"])
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
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"] = t.struct(
        {"resourceInfo": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"])
    types["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"] = t.struct(
        {
            "resourceInfo": t.struct({"_": t.string().optional()}).optional(),
            "sdkVersion": t.proxy(
                renames["GoogleCloudDatapipelinesV1SdkVersionOut"]
            ).optional(),
            "currentWorkers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"])
    types["GoogleCloudDatapipelinesV1PipelineIn"] = t.struct(
        {
            "type": t.string(),
            "displayName": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
            ).optional(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadIn"]
            ).optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineIn"])
    types["GoogleCloudDatapipelinesV1PipelineOut"] = t.struct(
        {
            "jobCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "type": t.string(),
            "displayName": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"]
            ).optional(),
            "lastUpdateTime": t.string().optional(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadOut"]
            ).optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "schedulerServiceAccountEmail": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineOut"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "update": t.boolean().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"]
            ).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "jobName": t.string(),
            "update": t.boolean().optional(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"]
            ).optional(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "gcsPath": t.string().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"]
            ).optional(),
            "projectId": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "gcsPath": t.string().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"]
            ).optional(),
            "projectId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "tempLocation": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string().optional(),
            "machineType": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "tempLocation": t.string().optional(),
            "network": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "serviceAccountEmail": t.string().optional(),
            "workerRegion": t.string().optional(),
            "machineType": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1SdkVersionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionIn"])
    types["GoogleCloudDatapipelinesV1SdkVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionOut"])
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
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"]
            ),
            "location": t.string(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "projectId": t.string(),
            "validateOnly": t.boolean().optional(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"]
            ),
            "location": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"])
    types["GoogleCloudDatapipelinesV1JobIn"] = t.struct(
        {
            "state": t.string().optional(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"]
            ).optional(),
            "name": t.string(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobIn"])
    types["GoogleCloudDatapipelinesV1JobOut"] = t.struct(
        {
            "id": t.string().optional(),
            "state": t.string().optional(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "update": t.boolean().optional(),
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "update": t.boolean().optional(),
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"])

    functions = {}
    functions["projectsLocationsPipelinesPatch"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesGet"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesStop"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesList"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesRun"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesDelete"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesCreate"] = datapipelines.post(
        "v1/{parent}/pipelines",
        t.struct(
            {
                "parent": t.string(),
                "type": t.string(),
                "displayName": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "name": t.string().optional(),
                "state": t.string(),
                "auth": t.string().optional(),
            }
        ),
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
        importer="datapipelines",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
