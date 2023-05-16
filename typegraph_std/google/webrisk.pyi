from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleCloudWebriskV1ComputeThreatListDiffResponseIn: t.typedef = ...
    GoogleCloudWebriskV1ComputeThreatListDiffResponseOut: t.typedef = ...
    GoogleCloudWebriskV1SubmissionIn: t.typedef = ...
    GoogleCloudWebriskV1SubmissionOut: t.typedef = ...
    GoogleRpcStatusIn: t.typedef = ...
    GoogleRpcStatusOut: t.typedef = ...
    GoogleLongrunningOperationIn: t.typedef = ...
    GoogleLongrunningOperationOut: t.typedef = ...
    GoogleCloudWebriskV1SearchUrisResponseIn: t.typedef = ...
    GoogleCloudWebriskV1SearchUrisResponseOut: t.typedef = ...
    GoogleCloudWebriskV1SearchHashesResponseThreatHashIn: t.typedef = ...
    GoogleCloudWebriskV1SearchHashesResponseThreatHashOut: t.typedef = ...
    GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn: t.typedef = ...
    GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut: t.typedef = ...
    GoogleCloudWebriskV1ThreatEntryRemovalsIn: t.typedef = ...
    GoogleCloudWebriskV1ThreatEntryRemovalsOut: t.typedef = ...
    GoogleCloudWebriskV1ThreatEntryAdditionsIn: t.typedef = ...
    GoogleCloudWebriskV1ThreatEntryAdditionsOut: t.typedef = ...
    GoogleCloudWebriskV1RawHashesIn: t.typedef = ...
    GoogleCloudWebriskV1RawHashesOut: t.typedef = ...
    GoogleCloudWebriskV1RawIndicesIn: t.typedef = ...
    GoogleCloudWebriskV1RawIndicesOut: t.typedef = ...
    GoogleCloudWebriskV1SearchHashesResponseIn: t.typedef = ...
    GoogleCloudWebriskV1SearchHashesResponseOut: t.typedef = ...
    GoogleProtobufEmptyIn: t.typedef = ...
    GoogleProtobufEmptyOut: t.typedef = ...
    GoogleCloudWebriskV1RiceDeltaEncodingIn: t.typedef = ...
    GoogleCloudWebriskV1RiceDeltaEncodingOut: t.typedef = ...
    GoogleLongrunningCancelOperationRequestIn: t.typedef = ...
    GoogleLongrunningCancelOperationRequestOut: t.typedef = ...
    GoogleCloudWebriskV1SearchUrisResponseThreatUriIn: t.typedef = ...
    GoogleCloudWebriskV1SearchUrisResponseThreatUriOut: t.typedef = ...
    GoogleLongrunningListOperationsResponseIn: t.typedef = ...
    GoogleLongrunningListOperationsResponseOut: t.typedef = ...

class FuncList:
    urisSearch: t.func = ...
    hashesSearch: t.func = ...
    projectsSubmissionsCreate: t.func = ...
    projectsOperationsList: t.func = ...
    projectsOperationsDelete: t.func = ...
    projectsOperationsGet: t.func = ...
    projectsOperationsCancel: t.func = ...
    threatListsComputeDiff: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_webrisk() -> Import: ...
