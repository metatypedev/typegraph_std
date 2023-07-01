from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    JwtIn: t.typedef = ...
    JwtOut: t.typedef = ...
    SignatureIn: t.typedef = ...
    SignatureOut: t.typedef = ...
    AttestorPublicKeyIn: t.typedef = ...
    AttestorPublicKeyOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    AttestationOccurrenceIn: t.typedef = ...
    AttestationOccurrenceOut: t.typedef = ...
    AdmissionWhitelistPatternIn: t.typedef = ...
    AdmissionWhitelistPatternOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    ValidateAttestationOccurrenceRequestIn: t.typedef = ...
    ValidateAttestationOccurrenceRequestOut: t.typedef = ...
    AdmissionRuleIn: t.typedef = ...
    AdmissionRuleOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    AttestorIn: t.typedef = ...
    AttestorOut: t.typedef = ...
    PkixPublicKeyIn: t.typedef = ...
    PkixPublicKeyOut: t.typedef = ...
    ListAttestorsResponseIn: t.typedef = ...
    ListAttestorsResponseOut: t.typedef = ...
    UserOwnedGrafeasNoteIn: t.typedef = ...
    UserOwnedGrafeasNoteOut: t.typedef = ...
    ValidateAttestationOccurrenceResponseIn: t.typedef = ...
    ValidateAttestationOccurrenceResponseOut: t.typedef = ...
    IamPolicyIn: t.typedef = ...
    IamPolicyOut: t.typedef = ...

class FuncList:
    projectsGetPolicy: t.func = ...
    projectsUpdatePolicy: t.func = ...
    projectsAttestorsCreate: t.func = ...
    projectsAttestorsGet: t.func = ...
    projectsAttestorsDelete: t.func = ...
    projectsAttestorsSetIamPolicy: t.func = ...
    projectsAttestorsList: t.func = ...
    projectsAttestorsValidateAttestationOccurrence: t.func = ...
    projectsAttestorsTestIamPermissions: t.func = ...
    projectsAttestorsGetIamPolicy: t.func = ...
    projectsAttestorsUpdate: t.func = ...
    projectsPolicyGetIamPolicy: t.func = ...
    projectsPolicyTestIamPermissions: t.func = ...
    projectsPolicySetIamPolicy: t.func = ...
    systempolicyGetPolicy: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_binaryauthorization() -> Import: ...
