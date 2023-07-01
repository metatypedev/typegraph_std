from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datapipelines():
    datapipelines = HTTPRuntime("https://datapipelines.googleapis.com/")

    renames = {
        "ErrorResponse": "_datapipelines_1_ErrorResponse",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestIn": "_datapipelines_2_GoogleCloudDatapipelinesV1LaunchTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateRequestOut": "_datapipelines_3_GoogleCloudDatapipelinesV1LaunchTemplateRequestOut",
        "GoogleCloudDatapipelinesV1WorkloadIn": "_datapipelines_4_GoogleCloudDatapipelinesV1WorkloadIn",
        "GoogleCloudDatapipelinesV1WorkloadOut": "_datapipelines_5_GoogleCloudDatapipelinesV1WorkloadOut",
        "GoogleCloudDatapipelinesV1SdkVersionIn": "_datapipelines_6_GoogleCloudDatapipelinesV1SdkVersionIn",
        "GoogleCloudDatapipelinesV1SdkVersionOut": "_datapipelines_7_GoogleCloudDatapipelinesV1SdkVersionOut",
        "GoogleCloudDatapipelinesV1ListJobsResponseIn": "_datapipelines_8_GoogleCloudDatapipelinesV1ListJobsResponseIn",
        "GoogleCloudDatapipelinesV1ListJobsResponseOut": "_datapipelines_9_GoogleCloudDatapipelinesV1ListJobsResponseOut",
        "GoogleCloudDatapipelinesV1RunPipelineRequestIn": "_datapipelines_10_GoogleCloudDatapipelinesV1RunPipelineRequestIn",
        "GoogleCloudDatapipelinesV1RunPipelineRequestOut": "_datapipelines_11_GoogleCloudDatapipelinesV1RunPipelineRequestOut",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersIn": "_datapipelines_12_GoogleCloudDatapipelinesV1LaunchTemplateParametersIn",
        "GoogleCloudDatapipelinesV1LaunchTemplateParametersOut": "_datapipelines_13_GoogleCloudDatapipelinesV1LaunchTemplateParametersOut",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsIn": "_datapipelines_14_GoogleCloudDatapipelinesV1DataflowJobDetailsIn",
        "GoogleCloudDatapipelinesV1DataflowJobDetailsOut": "_datapipelines_15_GoogleCloudDatapipelinesV1DataflowJobDetailsOut",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn": "_datapipelines_16_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut": "_datapipelines_17_GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1ScheduleSpecIn": "_datapipelines_18_GoogleCloudDatapipelinesV1ScheduleSpecIn",
        "GoogleCloudDatapipelinesV1ScheduleSpecOut": "_datapipelines_19_GoogleCloudDatapipelinesV1ScheduleSpecOut",
        "GoogleCloudDatapipelinesV1StopPipelineRequestIn": "_datapipelines_20_GoogleCloudDatapipelinesV1StopPipelineRequestIn",
        "GoogleCloudDatapipelinesV1StopPipelineRequestOut": "_datapipelines_21_GoogleCloudDatapipelinesV1StopPipelineRequestOut",
        "GoogleCloudDatapipelinesV1PipelineIn": "_datapipelines_22_GoogleCloudDatapipelinesV1PipelineIn",
        "GoogleCloudDatapipelinesV1PipelineOut": "_datapipelines_23_GoogleCloudDatapipelinesV1PipelineOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn": "_datapipelines_24_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut": "_datapipelines_25_GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseIn": "_datapipelines_26_GoogleCloudDatapipelinesV1ListPipelinesResponseIn",
        "GoogleCloudDatapipelinesV1ListPipelinesResponseOut": "_datapipelines_27_GoogleCloudDatapipelinesV1ListPipelinesResponseOut",
        "GoogleRpcStatusIn": "_datapipelines_28_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_datapipelines_29_GoogleRpcStatusOut",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentIn": "_datapipelines_30_GoogleCloudDatapipelinesV1RuntimeEnvironmentIn",
        "GoogleCloudDatapipelinesV1RuntimeEnvironmentOut": "_datapipelines_31_GoogleCloudDatapipelinesV1RuntimeEnvironmentOut",
        "GoogleCloudDatapipelinesV1JobIn": "_datapipelines_32_GoogleCloudDatapipelinesV1JobIn",
        "GoogleCloudDatapipelinesV1JobOut": "_datapipelines_33_GoogleCloudDatapipelinesV1JobOut",
        "GoogleCloudDatapipelinesV1RunPipelineResponseIn": "_datapipelines_34_GoogleCloudDatapipelinesV1RunPipelineResponseIn",
        "GoogleCloudDatapipelinesV1RunPipelineResponseOut": "_datapipelines_35_GoogleCloudDatapipelinesV1RunPipelineResponseOut",
        "GoogleProtobufEmptyIn": "_datapipelines_36_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_datapipelines_37_GoogleProtobufEmptyOut",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn": "_datapipelines_38_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn",
        "GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut": "_datapipelines_39_GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string(),
            "gcsPath": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string(),
            "gcsPath": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "launchParameters": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateRequestOut"])
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
    types["GoogleCloudDatapipelinesV1SdkVersionIn"] = t.struct(
        {
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionIn"])
    types["GoogleCloudDatapipelinesV1SdkVersionOut"] = t.struct(
        {
            "versionDisplayName": t.string().optional(),
            "sdkSupportStatus": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1SdkVersionOut"])
    types["GoogleCloudDatapipelinesV1ListJobsResponseIn"] = t.struct(
        {
            "jobs": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1JobIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListJobsResponseIn"])
    types["GoogleCloudDatapipelinesV1ListJobsResponseOut"] = t.struct(
        {
            "jobs": t.array(
                t.proxy(renames["GoogleCloudDatapipelinesV1JobOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ListJobsResponseOut"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1RunPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1RunPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersIn"])
    types["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"]
            ).optional(),
            "update": t.boolean().optional(),
            "jobName": t.string(),
            "transformNameMapping": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchTemplateParametersOut"])
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
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"] = t.struct(
        {
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "tempLocation": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "workerZone": t.string().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"] = t.struct(
        {
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "zone": t.string().optional(),
            "workerRegion": t.string().optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "numWorkers": t.integer().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "subnetwork": t.string().optional(),
            "flexrsGoal": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "tempLocation": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "workerZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecIn"] = t.struct(
        {"schedule": t.string().optional(), "timeZone": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"])
    types["GoogleCloudDatapipelinesV1ScheduleSpecOut"] = t.struct(
        {
            "schedule": t.string().optional(),
            "timeZone": t.string().optional(),
            "nextJobTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestIn"])
    types["GoogleCloudDatapipelinesV1StopPipelineRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudDatapipelinesV1StopPipelineRequestOut"])
    types["GoogleCloudDatapipelinesV1PipelineIn"] = t.struct(
        {
            "schedulerServiceAccountEmail": t.string().optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadIn"]
            ).optional(),
            "displayName": t.string(),
            "name": t.string().optional(),
            "type": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineIn"])
    types["GoogleCloudDatapipelinesV1PipelineOut"] = t.struct(
        {
            "schedulerServiceAccountEmail": t.string().optional(),
            "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string(),
            "workload": t.proxy(
                renames["GoogleCloudDatapipelinesV1WorkloadOut"]
            ).optional(),
            "displayName": t.string(),
            "jobCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string(),
            "scheduleInfo": t.proxy(
                renames["GoogleCloudDatapipelinesV1ScheduleSpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1PipelineOut"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"] = t.struct(
        {
            "location": t.string(),
            "validateOnly": t.boolean().optional(),
            "projectId": t.string(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"]
            ),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"] = t.struct(
        {
            "location": t.string(),
            "validateOnly": t.boolean().optional(),
            "projectId": t.string(),
            "launchParameter": t.proxy(
                renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateRequestOut"])
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
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "serviceAccountEmail": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentIn"])
    types["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"] = t.struct(
        {
            "workerZone": t.string().optional(),
            "additionalUserLabels": t.struct({"_": t.string().optional()}).optional(),
            "additionalExperiments": t.array(t.string()).optional(),
            "serviceAccountEmail": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "ipConfiguration": t.string().optional(),
            "machineType": t.string().optional(),
            "workerRegion": t.string().optional(),
            "bypassTempDirValidation": t.boolean().optional(),
            "numWorkers": t.integer().optional(),
            "zone": t.string().optional(),
            "maxWorkers": t.integer().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "tempLocation": t.string().optional(),
            "enableStreamingEngine": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1RuntimeEnvironmentOut"])
    types["GoogleCloudDatapipelinesV1JobIn"] = t.struct(
        {
            "state": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobIn"])
    types["GoogleCloudDatapipelinesV1JobOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "status": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "name": t.string(),
            "dataflowJobDetails": t.proxy(
                renames["GoogleCloudDatapipelinesV1DataflowJobDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1JobOut"])
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
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentIn"]
            ).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterIn"])
    types["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"] = t.struct(
        {
            "environment": t.proxy(
                renames["GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironmentOut"]
            ).optional(),
            "containerSpecGcsPath": t.string().optional(),
            "jobName": t.string(),
            "launchOptions": t.struct({"_": t.string().optional()}).optional(),
            "update": t.boolean().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "transformNameMappings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudDatapipelinesV1LaunchFlexTemplateParameterOut"])

    functions = {}
    functions["projectsLocationsPipelinesStop"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesRun"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesList"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesCreate"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesGet"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesDelete"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudDatapipelinesV1PipelineOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsPipelinesPatch"] = datapipelines.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "schedulerServiceAccountEmail": t.string().optional(),
                "pipelineSources": t.struct({"_": t.string().optional()}).optional(),
                "state": t.string(),
                "workload": t.proxy(
                    renames["GoogleCloudDatapipelinesV1WorkloadIn"]
                ).optional(),
                "displayName": t.string(),
                "type": t.string(),
                "scheduleInfo": t.proxy(
                    renames["GoogleCloudDatapipelinesV1ScheduleSpecIn"]
                ).optional(),
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
