from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1MessageInsightPercentsIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1MessageInsightPercentsOut: t.typedef = ...
    GoogleTypeDateIn: t.typedef = ...
    GoogleTypeDateOut: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1MessageOutcomePercentsOut: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1AndroidDeliveryDataOut: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseOut: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1DeliveryPerformancePercentsOut: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1DataIn: t.typedef = ...
    GoogleFirebaseFcmDataV1beta1DataOut: t.typedef = ...

class FuncList:
    projectsAndroidAppsDeliveryDataList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_fcmdata() -> Import: ...
