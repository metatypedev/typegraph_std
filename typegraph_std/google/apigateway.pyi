from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ApigatewayListApisResponseIn: t.typedef = ...
    ApigatewayListApisResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ApigatewayTestIamPermissionsResponseIn: t.typedef = ...
    ApigatewayTestIamPermissionsResponseOut: t.typedef = ...
    ApigatewayOperationMetadataDiagnosticIn: t.typedef = ...
    ApigatewayOperationMetadataDiagnosticOut: t.typedef = ...
    ApigatewayBindingIn: t.typedef = ...
    ApigatewayBindingOut: t.typedef = ...
    ApigatewayApiConfigOpenApiDocumentIn: t.typedef = ...
    ApigatewayApiConfigOpenApiDocumentOut: t.typedef = ...
    ApigatewayCancelOperationRequestIn: t.typedef = ...
    ApigatewayCancelOperationRequestOut: t.typedef = ...
    ApigatewayOperationMetadataIn: t.typedef = ...
    ApigatewayOperationMetadataOut: t.typedef = ...
    ApigatewaySetIamPolicyRequestIn: t.typedef = ...
    ApigatewaySetIamPolicyRequestOut: t.typedef = ...
    ApigatewayAuditConfigIn: t.typedef = ...
    ApigatewayAuditConfigOut: t.typedef = ...
    ApigatewayLocationIn: t.typedef = ...
    ApigatewayLocationOut: t.typedef = ...
    ApigatewayExprIn: t.typedef = ...
    ApigatewayExprOut: t.typedef = ...
    ApigatewayGatewayIn: t.typedef = ...
    ApigatewayGatewayOut: t.typedef = ...
    ApigatewayApiIn: t.typedef = ...
    ApigatewayApiOut: t.typedef = ...
    ApigatewayTestIamPermissionsRequestIn: t.typedef = ...
    ApigatewayTestIamPermissionsRequestOut: t.typedef = ...
    ApigatewayApiConfigFileIn: t.typedef = ...
    ApigatewayApiConfigFileOut: t.typedef = ...
    ApigatewayListApiConfigsResponseIn: t.typedef = ...
    ApigatewayListApiConfigsResponseOut: t.typedef = ...
    ApigatewayStatusIn: t.typedef = ...
    ApigatewayStatusOut: t.typedef = ...
    ApigatewayListGatewaysResponseIn: t.typedef = ...
    ApigatewayListGatewaysResponseOut: t.typedef = ...
    ApigatewayPolicyIn: t.typedef = ...
    ApigatewayPolicyOut: t.typedef = ...
    ApigatewayApiConfigIn: t.typedef = ...
    ApigatewayApiConfigOut: t.typedef = ...
    ApigatewayListOperationsResponseIn: t.typedef = ...
    ApigatewayListOperationsResponseOut: t.typedef = ...
    ApigatewayApiConfigGrpcServiceDefinitionIn: t.typedef = ...
    ApigatewayApiConfigGrpcServiceDefinitionOut: t.typedef = ...
    ApigatewayOperationIn: t.typedef = ...
    ApigatewayOperationOut: t.typedef = ...
    ApigatewayAuditLogConfigIn: t.typedef = ...
    ApigatewayAuditLogConfigOut: t.typedef = ...
    ApigatewayListLocationsResponseIn: t.typedef = ...
    ApigatewayListLocationsResponseOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsApisTestIamPermissions: t.func = ...
    projectsLocationsApisSetIamPolicy: t.func = ...
    projectsLocationsApisList: t.func = ...
    projectsLocationsApisDelete: t.func = ...
    projectsLocationsApisCreate: t.func = ...
    projectsLocationsApisPatch: t.func = ...
    projectsLocationsApisGet: t.func = ...
    projectsLocationsApisGetIamPolicy: t.func = ...
    projectsLocationsApisConfigsGetIamPolicy: t.func = ...
    projectsLocationsApisConfigsGet: t.func = ...
    projectsLocationsApisConfigsCreate: t.func = ...
    projectsLocationsApisConfigsSetIamPolicy: t.func = ...
    projectsLocationsApisConfigsList: t.func = ...
    projectsLocationsApisConfigsPatch: t.func = ...
    projectsLocationsApisConfigsTestIamPermissions: t.func = ...
    projectsLocationsApisConfigsDelete: t.func = ...
    projectsLocationsGatewaysCreate: t.func = ...
    projectsLocationsGatewaysList: t.func = ...
    projectsLocationsGatewaysDelete: t.func = ...
    projectsLocationsGatewaysTestIamPermissions: t.func = ...
    projectsLocationsGatewaysGetIamPolicy: t.func = ...
    projectsLocationsGatewaysGet: t.func = ...
    projectsLocationsGatewaysPatch: t.func = ...
    projectsLocationsGatewaysSetIamPolicy: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_apigateway() -> Import: ...
