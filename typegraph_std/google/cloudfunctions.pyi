from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    ListRuntimesResponseIn: t.typedef = ...
    ListRuntimesResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    GoogleCloudFunctionsV2alphaStateMessageIn: t.typedef = ...
    GoogleCloudFunctionsV2alphaStateMessageOut: t.typedef = ...
    GenerateUploadUrlRequestIn: t.typedef = ...
    GenerateUploadUrlRequestOut: t.typedef = ...
    GoogleCloudFunctionsV2alphaStageIn: t.typedef = ...
    GoogleCloudFunctionsV2alphaStageOut: t.typedef = ...
    ListFunctionsResponseIn: t.typedef = ...
    ListFunctionsResponseOut: t.typedef = ...
    StorageSourceIn: t.typedef = ...
    StorageSourceOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    BuildConfigIn: t.typedef = ...
    BuildConfigOut: t.typedef = ...
    GenerateDownloadUrlResponseIn: t.typedef = ...
    GenerateDownloadUrlResponseOut: t.typedef = ...
    GoogleCloudFunctionsV2betaStageIn: t.typedef = ...
    GoogleCloudFunctionsV2betaStageOut: t.typedef = ...
    GenerateDownloadUrlRequestIn: t.typedef = ...
    GenerateDownloadUrlRequestOut: t.typedef = ...
    GoogleCloudFunctionsV2betaStateMessageIn: t.typedef = ...
    GoogleCloudFunctionsV2betaStateMessageOut: t.typedef = ...
    GoogleCloudFunctionsV2OperationMetadataIn: t.typedef = ...
    GoogleCloudFunctionsV2OperationMetadataOut: t.typedef = ...
    OperationMetadataV1In: t.typedef = ...
    OperationMetadataV1Out: t.typedef = ...
    FunctionIn: t.typedef = ...
    FunctionOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    GoogleCloudFunctionsV2StageIn: t.typedef = ...
    GoogleCloudFunctionsV2StageOut: t.typedef = ...
    SourceIn: t.typedef = ...
    SourceOut: t.typedef = ...
    SourceProvenanceIn: t.typedef = ...
    SourceProvenanceOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    SecretVersionIn: t.typedef = ...
    SecretVersionOut: t.typedef = ...
    SecretEnvVarIn: t.typedef = ...
    SecretEnvVarOut: t.typedef = ...
    ServiceConfigIn: t.typedef = ...
    ServiceConfigOut: t.typedef = ...
    GoogleCloudFunctionsV2betaOperationMetadataIn: t.typedef = ...
    GoogleCloudFunctionsV2betaOperationMetadataOut: t.typedef = ...
    EventFilterIn: t.typedef = ...
    EventFilterOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    SecretVolumeIn: t.typedef = ...
    SecretVolumeOut: t.typedef = ...
    GenerateUploadUrlResponseIn: t.typedef = ...
    GenerateUploadUrlResponseOut: t.typedef = ...
    RepoSourceIn: t.typedef = ...
    RepoSourceOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    EventTriggerIn: t.typedef = ...
    EventTriggerOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    RuntimeIn: t.typedef = ...
    RuntimeOut: t.typedef = ...
    GoogleCloudFunctionsV2alphaOperationMetadataIn: t.typedef = ...
    GoogleCloudFunctionsV2alphaOperationMetadataOut: t.typedef = ...
    GoogleCloudFunctionsV2StateMessageIn: t.typedef = ...
    GoogleCloudFunctionsV2StateMessageOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsRuntimesList: t.func = ...
    projectsLocationsFunctionsGet: t.func = ...
    projectsLocationsFunctionsDelete: t.func = ...
    projectsLocationsFunctionsGenerateUploadUrl: t.func = ...
    projectsLocationsFunctionsCreate: t.func = ...
    projectsLocationsFunctionsList: t.func = ...
    projectsLocationsFunctionsGetIamPolicy: t.func = ...
    projectsLocationsFunctionsPatch: t.func = ...
    projectsLocationsFunctionsTestIamPermissions: t.func = ...
    projectsLocationsFunctionsGenerateDownloadUrl: t.func = ...
    projectsLocationsFunctionsSetIamPolicy: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudfunctions() -> Import: ...
