from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    OfficialIn: t.typedef = ...
    OfficialOut: t.typedef = ...
    GeographicDivisionIn: t.typedef = ...
    GeographicDivisionOut: t.typedef = ...
    RepresentativeInfoDataIn: t.typedef = ...
    RepresentativeInfoDataOut: t.typedef = ...
    AdministrationRegionIn: t.typedef = ...
    AdministrationRegionOut: t.typedef = ...
    ElectoralDistrictIn: t.typedef = ...
    ElectoralDistrictOut: t.typedef = ...
    PollingLocationIn: t.typedef = ...
    PollingLocationOut: t.typedef = ...
    SourceIn: t.typedef = ...
    SourceOut: t.typedef = ...
    DivisionSearchResponseIn: t.typedef = ...
    DivisionSearchResponseOut: t.typedef = ...
    RepresentativeInfoResponseIn: t.typedef = ...
    RepresentativeInfoResponseOut: t.typedef = ...
    SimpleAddressTypeIn: t.typedef = ...
    SimpleAddressTypeOut: t.typedef = ...
    ElectionsQueryResponseIn: t.typedef = ...
    ElectionsQueryResponseOut: t.typedef = ...
    ChannelIn: t.typedef = ...
    ChannelOut: t.typedef = ...
    DivisionSearchResultIn: t.typedef = ...
    DivisionSearchResultOut: t.typedef = ...
    ElectionOfficialIn: t.typedef = ...
    ElectionOfficialOut: t.typedef = ...
    OfficeIn: t.typedef = ...
    OfficeOut: t.typedef = ...
    VoterInfoResponseIn: t.typedef = ...
    VoterInfoResponseOut: t.typedef = ...
    ContestIn: t.typedef = ...
    ContestOut: t.typedef = ...
    CandidateIn: t.typedef = ...
    CandidateOut: t.typedef = ...
    AdministrativeBodyIn: t.typedef = ...
    AdministrativeBodyOut: t.typedef = ...
    PrecinctIn: t.typedef = ...
    PrecinctOut: t.typedef = ...
    ElectionIn: t.typedef = ...
    ElectionOut: t.typedef = ...

class FuncList:
    electionsVoterInfoQuery: t.func = ...
    electionsElectionQuery: t.func = ...
    representativesRepresentativeInfoByDivision: t.func = ...
    representativesRepresentativeInfoByAddress: t.func = ...
    divisionsSearch: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_civicinfo() -> Import: ...
