from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ApigatewayBindingIn: t.typedef = ...
    ApigatewayBindingOut: t.typedef = ...
    ApigatewayTestIamPermissionsRequestIn: t.typedef = ...
    ApigatewayTestIamPermissionsRequestOut: t.typedef = ...
    ApigatewayListApisResponseIn: t.typedef = ...
    ApigatewayListApisResponseOut: t.typedef = ...
    ApigatewayListLocationsResponseIn: t.typedef = ...
    ApigatewayListLocationsResponseOut: t.typedef = ...
    ApigatewayApiConfigIn: t.typedef = ...
    ApigatewayApiConfigOut: t.typedef = ...
    ApigatewayListOperationsResponseIn: t.typedef = ...
    ApigatewayListOperationsResponseOut: t.typedef = ...
    ApigatewayAuditConfigIn: t.typedef = ...
    ApigatewayAuditConfigOut: t.typedef = ...
    ApigatewayCancelOperationRequestIn: t.typedef = ...
    ApigatewayCancelOperationRequestOut: t.typedef = ...
    ApigatewayListApiConfigsResponseIn: t.typedef = ...
    ApigatewayListApiConfigsResponseOut: t.typedef = ...
    ApigatewayGatewayIn: t.typedef = ...
    ApigatewayGatewayOut: t.typedef = ...
    ApigatewayAuditLogConfigIn: t.typedef = ...
    ApigatewayAuditLogConfigOut: t.typedef = ...
    ApigatewayTestIamPermissionsResponseIn: t.typedef = ...
    ApigatewayTestIamPermissionsResponseOut: t.typedef = ...
    ApigatewayExprIn: t.typedef = ...
    ApigatewayExprOut: t.typedef = ...
    ApigatewayStatusIn: t.typedef = ...
    ApigatewayStatusOut: t.typedef = ...
    ApigatewayApiConfigOpenApiDocumentIn: t.typedef = ...
    ApigatewayApiConfigOpenApiDocumentOut: t.typedef = ...
    ApigatewaySetIamPolicyRequestIn: t.typedef = ...
    ApigatewaySetIamPolicyRequestOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ApigatewayOperationMetadataIn: t.typedef = ...
    ApigatewayOperationMetadataOut: t.typedef = ...
    ApigatewayApiConfigFileIn: t.typedef = ...
    ApigatewayApiConfigFileOut: t.typedef = ...
    ApigatewayPolicyIn: t.typedef = ...
    ApigatewayPolicyOut: t.typedef = ...
    ApigatewayLocationIn: t.typedef = ...
    ApigatewayLocationOut: t.typedef = ...
    ApigatewayOperationIn: t.typedef = ...
    ApigatewayOperationOut: t.typedef = ...
    ApigatewayApiConfigGrpcServiceDefinitionIn: t.typedef = ...
    ApigatewayApiConfigGrpcServiceDefinitionOut: t.typedef = ...
    ApigatewayApiIn: t.typedef = ...
    ApigatewayApiOut: t.typedef = ...
    ApigatewayOperationMetadataDiagnosticIn: t.typedef = ...
    ApigatewayOperationMetadataDiagnosticOut: t.typedef = ...
    ApigatewayListGatewaysResponseIn: t.typedef = ...
    ApigatewayListGatewaysResponseOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsGatewaysPatch: t.func = ...
    projectsLocationsGatewaysDelete: t.func = ...
    projectsLocationsGatewaysGetIamPolicy: t.func = ...
    projectsLocationsGatewaysTestIamPermissions: t.func = ...
    projectsLocationsGatewaysCreate: t.func = ...
    projectsLocationsGatewaysList: t.func = ...
    projectsLocationsGatewaysGet: t.func = ...
    projectsLocationsGatewaysSetIamPolicy: t.func = ...
    projectsLocationsApisList: t.func = ...
    projectsLocationsApisPatch: t.func = ...
    projectsLocationsApisGetIamPolicy: t.func = ...
    projectsLocationsApisCreate: t.func = ...
    projectsLocationsApisGet: t.func = ...
    projectsLocationsApisTestIamPermissions: t.func = ...
    projectsLocationsApisSetIamPolicy: t.func = ...
    projectsLocationsApisDelete: t.func = ...
    projectsLocationsApisConfigsGetIamPolicy: t.func = ...
    projectsLocationsApisConfigsGet: t.func = ...
    projectsLocationsApisConfigsPatch: t.func = ...
    projectsLocationsApisConfigsTestIamPermissions: t.func = ...
    projectsLocationsApisConfigsList: t.func = ...
    projectsLocationsApisConfigsDelete: t.func = ...
    projectsLocationsApisConfigsSetIamPolicy: t.func = ...
    projectsLocationsApisConfigsCreate: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_apigateway() -> Import: ...