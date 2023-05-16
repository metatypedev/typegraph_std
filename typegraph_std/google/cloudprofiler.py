from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudprofiler() -> Import:
    cloudprofiler = HTTPRuntime("https://cloudprofiler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudprofiler_1_ErrorResponse",
        "ProfileIn": "_cloudprofiler_2_ProfileIn",
        "ProfileOut": "_cloudprofiler_3_ProfileOut",
        "CreateProfileRequestIn": "_cloudprofiler_4_CreateProfileRequestIn",
        "CreateProfileRequestOut": "_cloudprofiler_5_CreateProfileRequestOut",
        "DeploymentIn": "_cloudprofiler_6_DeploymentIn",
        "DeploymentOut": "_cloudprofiler_7_DeploymentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ProfileIn"] = t.struct(
        {
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileType": t.string().optional(),
            "profileBytes": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileType": t.string().optional(),
            "profileBytes": t.string().optional(),
            "name": t.string().optional(),
            "duration": t.string().optional(),
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
    types["DeploymentIn"] = t.struct(
        {
            "target": t.string().optional(),
            "projectId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "target": t.string().optional(),
            "projectId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])

    functions = {}
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
