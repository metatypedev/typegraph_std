from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudprofiler():
    cloudprofiler = HTTPRuntime("https://cloudprofiler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudprofiler_1_ErrorResponse",
        "DeploymentIn": "_cloudprofiler_2_DeploymentIn",
        "DeploymentOut": "_cloudprofiler_3_DeploymentOut",
        "ProfileIn": "_cloudprofiler_4_ProfileIn",
        "ProfileOut": "_cloudprofiler_5_ProfileOut",
        "CreateProfileRequestIn": "_cloudprofiler_6_CreateProfileRequestIn",
        "CreateProfileRequestOut": "_cloudprofiler_7_CreateProfileRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DeploymentIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "target": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "target": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["ProfileIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileBytes": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "duration": t.string().optional(),
            "profileType": t.string().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "profileBytes": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "duration": t.string().optional(),
            "profileType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["CreateProfileRequestIn"] = t.struct(
        {
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "profileType": t.array(t.string()).optional(),
        }
    ).named(renames["CreateProfileRequestIn"])
    types["CreateProfileRequestOut"] = t.struct(
        {
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "profileType": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProfileRequestOut"])

    functions = {}
    functions["projectsProfilesPatch"] = cloudprofiler.post(
        "v2/{parent}/profiles",
        t.struct(
            {
                "parent": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "profileType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProfilesCreateOffline"] = cloudprofiler.post(
        "v2/{parent}/profiles",
        t.struct(
            {
                "parent": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "profileType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProfilesCreate"] = cloudprofiler.post(
        "v2/{parent}/profiles",
        t.struct(
            {
                "parent": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "profileType": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudprofiler",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
