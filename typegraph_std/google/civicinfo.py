from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_civicinfo():
    civicinfo = HTTPRuntime("https://civicinfo.googleapis.com/")

    renames = {
        "ErrorResponse": "_civicinfo_1_ErrorResponse",
        "OfficialIn": "_civicinfo_2_OfficialIn",
        "OfficialOut": "_civicinfo_3_OfficialOut",
        "GeographicDivisionIn": "_civicinfo_4_GeographicDivisionIn",
        "GeographicDivisionOut": "_civicinfo_5_GeographicDivisionOut",
        "RepresentativeInfoDataIn": "_civicinfo_6_RepresentativeInfoDataIn",
        "RepresentativeInfoDataOut": "_civicinfo_7_RepresentativeInfoDataOut",
        "AdministrationRegionIn": "_civicinfo_8_AdministrationRegionIn",
        "AdministrationRegionOut": "_civicinfo_9_AdministrationRegionOut",
        "ElectoralDistrictIn": "_civicinfo_10_ElectoralDistrictIn",
        "ElectoralDistrictOut": "_civicinfo_11_ElectoralDistrictOut",
        "PollingLocationIn": "_civicinfo_12_PollingLocationIn",
        "PollingLocationOut": "_civicinfo_13_PollingLocationOut",
        "SourceIn": "_civicinfo_14_SourceIn",
        "SourceOut": "_civicinfo_15_SourceOut",
        "DivisionSearchResponseIn": "_civicinfo_16_DivisionSearchResponseIn",
        "DivisionSearchResponseOut": "_civicinfo_17_DivisionSearchResponseOut",
        "RepresentativeInfoResponseIn": "_civicinfo_18_RepresentativeInfoResponseIn",
        "RepresentativeInfoResponseOut": "_civicinfo_19_RepresentativeInfoResponseOut",
        "SimpleAddressTypeIn": "_civicinfo_20_SimpleAddressTypeIn",
        "SimpleAddressTypeOut": "_civicinfo_21_SimpleAddressTypeOut",
        "ElectionsQueryResponseIn": "_civicinfo_22_ElectionsQueryResponseIn",
        "ElectionsQueryResponseOut": "_civicinfo_23_ElectionsQueryResponseOut",
        "ChannelIn": "_civicinfo_24_ChannelIn",
        "ChannelOut": "_civicinfo_25_ChannelOut",
        "DivisionSearchResultIn": "_civicinfo_26_DivisionSearchResultIn",
        "DivisionSearchResultOut": "_civicinfo_27_DivisionSearchResultOut",
        "ElectionOfficialIn": "_civicinfo_28_ElectionOfficialIn",
        "ElectionOfficialOut": "_civicinfo_29_ElectionOfficialOut",
        "OfficeIn": "_civicinfo_30_OfficeIn",
        "OfficeOut": "_civicinfo_31_OfficeOut",
        "VoterInfoResponseIn": "_civicinfo_32_VoterInfoResponseIn",
        "VoterInfoResponseOut": "_civicinfo_33_VoterInfoResponseOut",
        "ContestIn": "_civicinfo_34_ContestIn",
        "ContestOut": "_civicinfo_35_ContestOut",
        "CandidateIn": "_civicinfo_36_CandidateIn",
        "CandidateOut": "_civicinfo_37_CandidateOut",
        "AdministrativeBodyIn": "_civicinfo_38_AdministrativeBodyIn",
        "AdministrativeBodyOut": "_civicinfo_39_AdministrativeBodyOut",
        "PrecinctIn": "_civicinfo_40_PrecinctIn",
        "PrecinctOut": "_civicinfo_41_PrecinctOut",
        "ElectionIn": "_civicinfo_42_ElectionIn",
        "ElectionOut": "_civicinfo_43_ElectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OfficialIn"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "phones": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "emails": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeIn"])).optional(),
        }
    ).named(renames["OfficialIn"])
    types["OfficialOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "phones": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "emails": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficialOut"])
    types["GeographicDivisionIn"] = t.struct(
        {
            "officeIndices": t.array(t.integer()).optional(),
            "name": t.string().optional(),
            "alsoKnownAs": t.array(t.string()).optional(),
        }
    ).named(renames["GeographicDivisionIn"])
    types["GeographicDivisionOut"] = t.struct(
        {
            "officeIndices": t.array(t.integer()).optional(),
            "name": t.string().optional(),
            "alsoKnownAs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeographicDivisionOut"])
    types["RepresentativeInfoDataIn"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RepresentativeInfoDataIn"])
    types["RepresentativeInfoDataOut"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoDataOut"])
    types["AdministrationRegionIn"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyIn"]
            ).optional(),
            "name": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "local_jurisdiction": t.proxy(renames["AdministrationRegionIn"]).optional(),
        }
    ).named(renames["AdministrationRegionIn"])
    types["AdministrationRegionOut"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyOut"]
            ).optional(),
            "name": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "local_jurisdiction": t.proxy(
                renames["AdministrationRegionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrationRegionOut"])
    types["ElectoralDistrictIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["ElectoralDistrictIn"])
    types["ElectoralDistrictOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectoralDistrictOut"])
    types["PollingLocationIn"] = t.struct(
        {
            "pollingHours": t.string().optional(),
            "latitude": t.number().optional(),
            "notes": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "address": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "name": t.string().optional(),
            "startDate": t.string().optional(),
            "voterServices": t.string().optional(),
            "longitude": t.number().optional(),
        }
    ).named(renames["PollingLocationIn"])
    types["PollingLocationOut"] = t.struct(
        {
            "pollingHours": t.string().optional(),
            "latitude": t.number().optional(),
            "notes": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "address": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "name": t.string().optional(),
            "startDate": t.string().optional(),
            "voterServices": t.string().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollingLocationOut"])
    types["SourceIn"] = t.struct(
        {"name": t.string().optional(), "official": t.boolean().optional()}
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "official": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["DivisionSearchResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["DivisionSearchResultIn"])),
            "kind": t.string().optional(),
        }
    ).named(renames["DivisionSearchResponseIn"])
    types["DivisionSearchResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["DivisionSearchResultOut"])),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DivisionSearchResponseOut"])
    types["RepresentativeInfoResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoResponseIn"])
    types["RepresentativeInfoResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoResponseOut"])
    types["SimpleAddressTypeIn"] = t.struct(
        {
            "line3": t.string().optional(),
            "line2": t.string().optional(),
            "zip": t.string().optional(),
            "line1": t.string().optional(),
            "locationName": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
        }
    ).named(renames["SimpleAddressTypeIn"])
    types["SimpleAddressTypeOut"] = t.struct(
        {
            "line3": t.string().optional(),
            "line2": t.string().optional(),
            "zip": t.string().optional(),
            "line1": t.string().optional(),
            "locationName": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleAddressTypeOut"])
    types["ElectionsQueryResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "elections": t.array(t.proxy(renames["ElectionIn"])).optional(),
        }
    ).named(renames["ElectionsQueryResponseIn"])
    types["ElectionsQueryResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "elections": t.array(t.proxy(renames["ElectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionsQueryResponseOut"])
    types["ChannelIn"] = t.struct(
        {"id": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["DivisionSearchResultIn"] = t.struct(
        {
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "ocdId": t.string().optional(),
        }
    ).named(renames["DivisionSearchResultIn"])
    types["DivisionSearchResultOut"] = t.struct(
        {
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "ocdId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DivisionSearchResultOut"])
    types["ElectionOfficialIn"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "faxNumber": t.string().optional(),
            "title": t.string().optional(),
            "emailAddress": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ElectionOfficialIn"])
    types["ElectionOfficialOut"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "faxNumber": t.string().optional(),
            "title": t.string().optional(),
            "emailAddress": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOfficialOut"])
    types["OfficeIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "name": t.string().optional(),
            "divisionId": t.string().optional(),
            "levels": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "officialIndices": t.array(t.integer()).optional(),
        }
    ).named(renames["OfficeIn"])
    types["OfficeOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "name": t.string().optional(),
            "divisionId": t.string().optional(),
            "levels": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficeOut"])
    types["VoterInfoResponseIn"] = t.struct(
        {
            "contests": t.array(t.proxy(renames["ContestIn"])).optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionIn"])).optional(),
            "precinctId": t.string(),
            "earlyVoteSites": t.array(t.proxy(renames["PollingLocationIn"])).optional(),
            "election": t.proxy(renames["ElectionIn"]).optional(),
            "kind": t.string().optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionIn"])).optional(),
            "mailOnly": t.boolean().optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "precincts": t.array(t.proxy(renames["PrecinctIn"])).optional(),
        }
    ).named(renames["VoterInfoResponseIn"])
    types["VoterInfoResponseOut"] = t.struct(
        {
            "contests": t.array(t.proxy(renames["ContestOut"])).optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionOut"])).optional(),
            "precinctId": t.string(),
            "earlyVoteSites": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "election": t.proxy(renames["ElectionOut"]).optional(),
            "kind": t.string().optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionOut"])).optional(),
            "mailOnly": t.boolean().optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "precincts": t.array(t.proxy(renames["PrecinctOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoterInfoResponseOut"])
    types["ContestIn"] = t.struct(
        {
            "ballotTitle": t.string().optional(),
            "electorateSpecifications": t.string().optional(),
            "special": t.string().optional(),
            "type": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "referendumConStatement": t.string().optional(),
            "referendumSubtitle": t.string().optional(),
            "ballotPlacement": t.string().optional(),
            "office": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "candidates": t.array(t.proxy(renames["CandidateIn"])).optional(),
            "level": t.array(t.string()).optional(),
            "referendumPassageThreshold": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumText": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "referendumBrief": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "district": t.proxy(renames["ElectoralDistrictIn"]).optional(),
        }
    ).named(renames["ContestIn"])
    types["ContestOut"] = t.struct(
        {
            "ballotTitle": t.string().optional(),
            "electorateSpecifications": t.string().optional(),
            "special": t.string().optional(),
            "type": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "referendumConStatement": t.string().optional(),
            "referendumSubtitle": t.string().optional(),
            "ballotPlacement": t.string().optional(),
            "office": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "candidates": t.array(t.proxy(renames["CandidateOut"])).optional(),
            "level": t.array(t.string()).optional(),
            "referendumPassageThreshold": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumText": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "referendumBrief": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "district": t.proxy(renames["ElectoralDistrictOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContestOut"])
    types["CandidateIn"] = t.struct(
        {
            "phone": t.string().optional(),
            "email": t.string().optional(),
            "candidateUrl": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "photoUrl": t.string().optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "orderOnBallot": t.string().optional(),
        }
    ).named(renames["CandidateIn"])
    types["CandidateOut"] = t.struct(
        {
            "phone": t.string().optional(),
            "email": t.string().optional(),
            "candidateUrl": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "photoUrl": t.string().optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "orderOnBallot": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandidateOut"])
    types["AdministrativeBodyIn"] = t.struct(
        {
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialIn"])
            ).optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "electionRulesUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "name": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
            "correspondenceAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
        }
    ).named(renames["AdministrativeBodyIn"])
    types["AdministrativeBodyOut"] = t.struct(
        {
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialOut"])
            ).optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "electionRulesUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "name": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
            "correspondenceAddress": t.proxy(
                renames["SimpleAddressTypeOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrativeBodyOut"])
    types["PrecinctIn"] = t.struct(
        {
            "splitName": t.string().optional(),
            "mailOnly": t.boolean().optional(),
            "contestId": t.array(t.string()).optional(),
            "administrationRegionId": t.string().optional(),
            "ocdId": t.array(t.string()).optional(),
            "number": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "pollingLocationId": t.array(t.string()).optional(),
            "name": t.string(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "id": t.string(),
            "ward": t.string().optional(),
        }
    ).named(renames["PrecinctIn"])
    types["PrecinctOut"] = t.struct(
        {
            "splitName": t.string().optional(),
            "mailOnly": t.boolean().optional(),
            "contestId": t.array(t.string()).optional(),
            "administrationRegionId": t.string().optional(),
            "ocdId": t.array(t.string()).optional(),
            "number": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "pollingLocationId": t.array(t.string()).optional(),
            "name": t.string(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "id": t.string(),
            "ward": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrecinctOut"])
    types["ElectionIn"] = t.struct(
        {
            "id": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "name": t.string().optional(),
            "shapeLookupBehavior": t.string(),
            "electionDay": t.string().optional(),
        }
    ).named(renames["ElectionIn"])
    types["ElectionOut"] = t.struct(
        {
            "id": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "name": t.string().optional(),
            "shapeLookupBehavior": t.string(),
            "electionDay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOut"])

    functions = {}
    functions["electionsVoterInfoQuery"] = civicinfo.get(
        "civicinfo/v2/elections",
        t.struct(
            {
                "productionDataOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ElectionsQueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["electionsElectionQuery"] = civicinfo.get(
        "civicinfo/v2/elections",
        t.struct(
            {
                "productionDataOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ElectionsQueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["representativesRepresentativeInfoByDivision"] = civicinfo.get(
        "civicinfo/v2/representatives",
        t.struct(
            {
                "levels": t.string().optional(),
                "includeOffices": t.boolean().optional(),
                "address": t.string().optional(),
                "roles": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepresentativeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["representativesRepresentativeInfoByAddress"] = civicinfo.get(
        "civicinfo/v2/representatives",
        t.struct(
            {
                "levels": t.string().optional(),
                "includeOffices": t.boolean().optional(),
                "address": t.string().optional(),
                "roles": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepresentativeInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["divisionsSearch"] = civicinfo.get(
        "civicinfo/v2/divisions",
        t.struct({"query": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DivisionSearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="civicinfo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
