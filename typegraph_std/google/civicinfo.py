from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_civicinfo() -> Import:
    civicinfo = HTTPRuntime("https://civicinfo.googleapis.com/")

    renames = {
        "ErrorResponse": "_civicinfo_1_ErrorResponse",
        "RepresentativeInfoDataIn": "_civicinfo_2_RepresentativeInfoDataIn",
        "RepresentativeInfoDataOut": "_civicinfo_3_RepresentativeInfoDataOut",
        "PollingLocationIn": "_civicinfo_4_PollingLocationIn",
        "PollingLocationOut": "_civicinfo_5_PollingLocationOut",
        "OfficialIn": "_civicinfo_6_OfficialIn",
        "OfficialOut": "_civicinfo_7_OfficialOut",
        "FeatureIdProtoIn": "_civicinfo_8_FeatureIdProtoIn",
        "FeatureIdProtoOut": "_civicinfo_9_FeatureIdProtoOut",
        "ElectionOfficialIn": "_civicinfo_10_ElectionOfficialIn",
        "ElectionOfficialOut": "_civicinfo_11_ElectionOfficialOut",
        "DivisionSearchResultIn": "_civicinfo_12_DivisionSearchResultIn",
        "DivisionSearchResultOut": "_civicinfo_13_DivisionSearchResultOut",
        "SimpleAddressTypeIn": "_civicinfo_14_SimpleAddressTypeIn",
        "SimpleAddressTypeOut": "_civicinfo_15_SimpleAddressTypeOut",
        "ElectoralDistrictIn": "_civicinfo_16_ElectoralDistrictIn",
        "ElectoralDistrictOut": "_civicinfo_17_ElectoralDistrictOut",
        "MessageSetIn": "_civicinfo_18_MessageSetIn",
        "MessageSetOut": "_civicinfo_19_MessageSetOut",
        "AdministrativeBodyIn": "_civicinfo_20_AdministrativeBodyIn",
        "AdministrativeBodyOut": "_civicinfo_21_AdministrativeBodyOut",
        "CandidateIn": "_civicinfo_22_CandidateIn",
        "CandidateOut": "_civicinfo_23_CandidateOut",
        "RepresentativeInfoResponseIn": "_civicinfo_24_RepresentativeInfoResponseIn",
        "RepresentativeInfoResponseOut": "_civicinfo_25_RepresentativeInfoResponseOut",
        "VoterInfoResponseIn": "_civicinfo_26_VoterInfoResponseIn",
        "VoterInfoResponseOut": "_civicinfo_27_VoterInfoResponseOut",
        "GeographicDivisionIn": "_civicinfo_28_GeographicDivisionIn",
        "GeographicDivisionOut": "_civicinfo_29_GeographicDivisionOut",
        "SourceIn": "_civicinfo_30_SourceIn",
        "SourceOut": "_civicinfo_31_SourceOut",
        "PrecinctIn": "_civicinfo_32_PrecinctIn",
        "PrecinctOut": "_civicinfo_33_PrecinctOut",
        "GeocodingSummaryIn": "_civicinfo_34_GeocodingSummaryIn",
        "GeocodingSummaryOut": "_civicinfo_35_GeocodingSummaryOut",
        "ChannelIn": "_civicinfo_36_ChannelIn",
        "ChannelOut": "_civicinfo_37_ChannelOut",
        "ElectionIn": "_civicinfo_38_ElectionIn",
        "ElectionOut": "_civicinfo_39_ElectionOut",
        "ElectionsQueryResponseIn": "_civicinfo_40_ElectionsQueryResponseIn",
        "ElectionsQueryResponseOut": "_civicinfo_41_ElectionsQueryResponseOut",
        "ContestIn": "_civicinfo_42_ContestIn",
        "ContestOut": "_civicinfo_43_ContestOut",
        "OfficeIn": "_civicinfo_44_OfficeIn",
        "OfficeOut": "_civicinfo_45_OfficeOut",
        "DivisionSearchResponseIn": "_civicinfo_46_DivisionSearchResponseIn",
        "DivisionSearchResponseOut": "_civicinfo_47_DivisionSearchResponseOut",
        "AdministrationRegionIn": "_civicinfo_48_AdministrationRegionIn",
        "AdministrationRegionOut": "_civicinfo_49_AdministrationRegionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RepresentativeInfoDataIn"] = t.struct(
        {
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoDataIn"])
    types["RepresentativeInfoDataOut"] = t.struct(
        {
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoDataOut"])
    types["PollingLocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "address": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "longitude": t.number().optional(),
            "voterServices": t.string().optional(),
            "pollingHours": t.string().optional(),
            "notes": t.string().optional(),
            "latitude": t.number().optional(),
        }
    ).named(renames["PollingLocationIn"])
    types["PollingLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "address": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "startDate": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "longitude": t.number().optional(),
            "voterServices": t.string().optional(),
            "pollingHours": t.string().optional(),
            "notes": t.string().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollingLocationOut"])
    types["OfficialIn"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeIn"])).optional(),
            "photoUrl": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryIn"])
            ).optional(),
            "party": t.string().optional(),
            "phones": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
        }
    ).named(renames["OfficialIn"])
    types["OfficialOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeOut"])).optional(),
            "photoUrl": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryOut"])
            ).optional(),
            "party": t.string().optional(),
            "phones": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficialOut"])
    types["FeatureIdProtoIn"] = t.struct(
        {
            "temporaryData": t.proxy(renames["MessageSetIn"]).optional(),
            "cellId": t.string().optional(),
            "fprint": t.string().optional(),
        }
    ).named(renames["FeatureIdProtoIn"])
    types["FeatureIdProtoOut"] = t.struct(
        {
            "temporaryData": t.proxy(renames["MessageSetOut"]).optional(),
            "cellId": t.string().optional(),
            "fprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureIdProtoOut"])
    types["ElectionOfficialIn"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "emailAddress": t.string().optional(),
            "faxNumber": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ElectionOfficialIn"])
    types["ElectionOfficialOut"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "emailAddress": t.string().optional(),
            "faxNumber": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOfficialOut"])
    types["DivisionSearchResultIn"] = t.struct(
        {
            "ocdId": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DivisionSearchResultIn"])
    types["DivisionSearchResultOut"] = t.struct(
        {
            "ocdId": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DivisionSearchResultOut"])
    types["SimpleAddressTypeIn"] = t.struct(
        {
            "locationName": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
            "line1": t.string().optional(),
            "line3": t.string().optional(),
            "line2": t.string().optional(),
            "zip": t.string().optional(),
        }
    ).named(renames["SimpleAddressTypeIn"])
    types["SimpleAddressTypeOut"] = t.struct(
        {
            "locationName": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
            "line1": t.string().optional(),
            "line3": t.string().optional(),
            "line2": t.string().optional(),
            "zip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleAddressTypeOut"])
    types["ElectoralDistrictIn"] = t.struct(
        {
            "scope": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ElectoralDistrictIn"])
    types["ElectoralDistrictOut"] = t.struct(
        {
            "scope": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectoralDistrictOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["AdministrativeBodyIn"] = t.struct(
        {
            "voter_services": t.array(t.string()).optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialIn"])
            ).optional(),
            "ballotInfoUrl": t.string().optional(),
            "name": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "votingLocationFinderUrl": t.string().optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "correspondenceAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "electionRegistrationUrl": t.string().optional(),
        }
    ).named(renames["AdministrativeBodyIn"])
    types["AdministrativeBodyOut"] = t.struct(
        {
            "voter_services": t.array(t.string()).optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialOut"])
            ).optional(),
            "ballotInfoUrl": t.string().optional(),
            "name": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "votingLocationFinderUrl": t.string().optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "correspondenceAddress": t.proxy(
                renames["SimpleAddressTypeOut"]
            ).optional(),
            "electionRegistrationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrativeBodyOut"])
    types["CandidateIn"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "party": t.string().optional(),
            "email": t.string().optional(),
            "phone": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "orderOnBallot": t.string().optional(),
            "candidateUrl": t.string().optional(),
        }
    ).named(renames["CandidateIn"])
    types["CandidateOut"] = t.struct(
        {
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "party": t.string().optional(),
            "email": t.string().optional(),
            "phone": t.string().optional(),
            "name": t.string().optional(),
            "photoUrl": t.string().optional(),
            "orderOnBallot": t.string().optional(),
            "candidateUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandidateOut"])
    types["RepresentativeInfoResponseIn"] = t.struct(
        {
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
            "kind": t.string().optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoResponseIn"])
    types["RepresentativeInfoResponseOut"] = t.struct(
        {
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "kind": t.string().optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoResponseOut"])
    types["VoterInfoResponseIn"] = t.struct(
        {
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "precinctId": t.string(),
            "kind": t.string().optional(),
            "otherElections": t.array(t.proxy(renames["ElectionIn"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "mailOnly": t.boolean().optional(),
            "contests": t.array(t.proxy(renames["ContestIn"])).optional(),
            "election": t.proxy(renames["ElectionIn"]).optional(),
            "earlyVoteSites": t.array(t.proxy(renames["PollingLocationIn"])).optional(),
            "precincts": t.array(t.proxy(renames["PrecinctIn"])).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionIn"])).optional(),
        }
    ).named(renames["VoterInfoResponseIn"])
    types["VoterInfoResponseOut"] = t.struct(
        {
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "precinctId": t.string(),
            "kind": t.string().optional(),
            "otherElections": t.array(t.proxy(renames["ElectionOut"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "mailOnly": t.boolean().optional(),
            "contests": t.array(t.proxy(renames["ContestOut"])).optional(),
            "election": t.proxy(renames["ElectionOut"]).optional(),
            "earlyVoteSites": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "precincts": t.array(t.proxy(renames["PrecinctOut"])).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoterInfoResponseOut"])
    types["GeographicDivisionIn"] = t.struct(
        {
            "alsoKnownAs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "officeIndices": t.array(t.integer()).optional(),
        }
    ).named(renames["GeographicDivisionIn"])
    types["GeographicDivisionOut"] = t.struct(
        {
            "alsoKnownAs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "officeIndices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeographicDivisionOut"])
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
    types["PrecinctIn"] = t.struct(
        {
            "name": t.string(),
            "splitName": t.string().optional(),
            "number": t.string().optional(),
            "ward": t.string().optional(),
            "administrationRegionId": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "ocdId": t.array(t.string()).optional(),
            "id": t.string(),
            "mailOnly": t.boolean().optional(),
            "contestId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
        }
    ).named(renames["PrecinctIn"])
    types["PrecinctOut"] = t.struct(
        {
            "name": t.string(),
            "splitName": t.string().optional(),
            "number": t.string().optional(),
            "ward": t.string().optional(),
            "administrationRegionId": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "ocdId": t.array(t.string()).optional(),
            "id": t.string(),
            "mailOnly": t.boolean().optional(),
            "contestId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrecinctOut"])
    types["GeocodingSummaryIn"] = t.struct(
        {
            "featureId": t.proxy(renames["FeatureIdProtoIn"]).optional(),
            "positionPrecisionMeters": t.number().optional(),
            "addressUnderstood": t.boolean().optional(),
            "featureType": t.string().optional(),
            "queryString": t.string().optional(),
        }
    ).named(renames["GeocodingSummaryIn"])
    types["GeocodingSummaryOut"] = t.struct(
        {
            "featureId": t.proxy(renames["FeatureIdProtoOut"]).optional(),
            "positionPrecisionMeters": t.number().optional(),
            "addressUnderstood": t.boolean().optional(),
            "featureType": t.string().optional(),
            "queryString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeocodingSummaryOut"])
    types["ChannelIn"] = t.struct(
        {"type": t.string().optional(), "id": t.string().optional()}
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ElectionIn"] = t.struct(
        {
            "electionDay": t.string().optional(),
            "shapeLookupBehavior": t.string(),
            "name": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ElectionIn"])
    types["ElectionOut"] = t.struct(
        {
            "electionDay": t.string().optional(),
            "shapeLookupBehavior": t.string(),
            "name": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOut"])
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
    types["ContestIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "electorateSpecifications": t.string().optional(),
            "referendumPassageThreshold": t.string().optional(),
            "ballotPlacement": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateIn"])).optional(),
            "referendumTitle": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "district": t.proxy(renames["ElectoralDistrictIn"]).optional(),
            "ballotTitle": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "referendumBrief": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "office": t.string().optional(),
            "special": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "numberElected": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "type": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumText": t.string().optional(),
        }
    ).named(renames["ContestIn"])
    types["ContestOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "electorateSpecifications": t.string().optional(),
            "referendumPassageThreshold": t.string().optional(),
            "ballotPlacement": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateOut"])).optional(),
            "referendumTitle": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "district": t.proxy(renames["ElectoralDistrictOut"]).optional(),
            "ballotTitle": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "referendumBrief": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "office": t.string().optional(),
            "special": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "numberElected": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "type": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContestOut"])
    types["OfficeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "divisionId": t.string().optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "levels": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["OfficeIn"])
    types["OfficeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "divisionId": t.string().optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "levels": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficeOut"])
    types["DivisionSearchResponseIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(t.proxy(renames["DivisionSearchResultIn"])),
        }
    ).named(renames["DivisionSearchResponseIn"])
    types["DivisionSearchResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "results": t.array(t.proxy(renames["DivisionSearchResultOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DivisionSearchResponseOut"])
    types["AdministrationRegionIn"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyIn"]
            ).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "name": t.string().optional(),
            "local_jurisdiction": t.proxy(renames["AdministrationRegionIn"]).optional(),
        }
    ).named(renames["AdministrationRegionIn"])
    types["AdministrationRegionOut"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyOut"]
            ).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "name": t.string().optional(),
            "local_jurisdiction": t.proxy(
                renames["AdministrationRegionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrationRegionOut"])

    functions = {}
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
    functions["electionsElectionQuery"] = civicinfo.get(
        "civicinfo/v2/voterinfo",
        t.struct(
            {
                "returnAllAvailableData": t.boolean().optional(),
                "address": t.string().optional(),
                "electionId": t.string().optional(),
                "officialOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VoterInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["electionsVoterInfoQuery"] = civicinfo.get(
        "civicinfo/v2/voterinfo",
        t.struct(
            {
                "returnAllAvailableData": t.boolean().optional(),
                "address": t.string().optional(),
                "electionId": t.string().optional(),
                "officialOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VoterInfoResponseOut"]),
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
