from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudprofiler() -> Import:
    cloudprofiler = HTTPRuntime("https://cloudprofiler.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudprofiler_1_ErrorResponse",
        "CreateProfileRequestIn": "_cloudprofiler_2_CreateProfileRequestIn",
        "CreateProfileRequestOut": "_cloudprofiler_3_CreateProfileRequestOut",
        "ProfileIn": "_cloudprofiler_4_ProfileIn",
        "ProfileOut": "_cloudprofiler_5_ProfileOut",
        "DeploymentIn": "_cloudprofiler_6_DeploymentIn",
        "DeploymentOut": "_cloudprofiler_7_DeploymentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CreateProfileRequestIn"] = t.struct(
        {
            "profileType": t.array(t.string()).optional(),
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
        }
    ).named(renames["CreateProfileRequestIn"])
    types["CreateProfileRequestOut"] = t.struct(
        {
            "profileType": t.array(t.string()).optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProfileRequestOut"])
    types["ProfileIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileType": t.string().optional(),
            "profileBytes": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ProfileIn"])
    types["ProfileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "profileType": t.string().optional(),
            "profileBytes": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "duration": t.string().optional(),
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

    functions = {}
    functions["projectsProfilesCreateOffline"] = cloudprofiler.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "profileType": t.string().optional(),
                "profileBytes": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "duration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProfilesCreate"] = cloudprofiler.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "profileType": t.string().optional(),
                "profileBytes": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "duration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsProfilesPatch"] = cloudprofiler.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "profileType": t.string().optional(),
                "profileBytes": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "duration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudprofiler", renames=renames, types=types, functions=functions
    )
