from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    AcmeTxtRecordIn: t.typedef = ...
    AcmeTxtRecordOut: t.typedef = ...
    AcmeChallengeSetIn: t.typedef = ...
    AcmeChallengeSetOut: t.typedef = ...
    RotateChallengesRequestIn: t.typedef = ...
    RotateChallengesRequestOut: t.typedef = ...

class FuncList:
    acmeChallengeSetsGet: t.func = ...
    acmeChallengeSetsRotateChallenges: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_acmedns() -> Import: ...