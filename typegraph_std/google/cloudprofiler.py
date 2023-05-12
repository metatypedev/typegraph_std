from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudprofiler() -> Import:
    cloudprofiler = HTTPRuntime("https://cloudprofiler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudprofiler_1_ErrorResponse",
        "ProfileIn": "_cloudprofiler_2_ProfileIn",
        "ProfileOut": "_cloudprofiler_3_ProfileOut",
        "DeploymentIn": "_cloudprofiler_4_DeploymentIn",
        "DeploymentOut": "_cloudprofiler_5_DeploymentOut",
        "CreateProfileRequestIn": "_cloudprofiler_6_CreateProfileRequestIn",
        "CreateProfileRequestOut": "_cloudprofiler_7_CreateProfileRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ProfileIn"] = t.struct(
        {
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "duration": t.string().optional(),
            "profileType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileBytes": t.string().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "duration": t.string().optional(),
            "profileType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProfileOut"])
    types["DeploymentIn"] = t.struct(
        {
            "target": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "target": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
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
