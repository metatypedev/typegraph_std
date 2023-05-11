from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_civicinfo() -> Import:
    civicinfo = HTTPRuntime("https://civicinfo.googleapis.com/")

    renames = {
        "ErrorResponse": "_civicinfo_1_ErrorResponse",
        "FeatureIdProtoIn": "_civicinfo_2_FeatureIdProtoIn",
        "FeatureIdProtoOut": "_civicinfo_3_FeatureIdProtoOut",
        "GeocodingSummaryIn": "_civicinfo_4_GeocodingSummaryIn",
        "GeocodingSummaryOut": "_civicinfo_5_GeocodingSummaryOut",
        "GeographicDivisionIn": "_civicinfo_6_GeographicDivisionIn",
        "GeographicDivisionOut": "_civicinfo_7_GeographicDivisionOut",
        "ElectoralDistrictIn": "_civicinfo_8_ElectoralDistrictIn",
        "ElectoralDistrictOut": "_civicinfo_9_ElectoralDistrictOut",
        "AdministrationRegionIn": "_civicinfo_10_AdministrationRegionIn",
        "AdministrationRegionOut": "_civicinfo_11_AdministrationRegionOut",
        "CandidateIn": "_civicinfo_12_CandidateIn",
        "CandidateOut": "_civicinfo_13_CandidateOut",
        "ElectionOfficialIn": "_civicinfo_14_ElectionOfficialIn",
        "ElectionOfficialOut": "_civicinfo_15_ElectionOfficialOut",
        "RepresentativeInfoDataIn": "_civicinfo_16_RepresentativeInfoDataIn",
        "RepresentativeInfoDataOut": "_civicinfo_17_RepresentativeInfoDataOut",
        "DivisionSearchResponseIn": "_civicinfo_18_DivisionSearchResponseIn",
        "DivisionSearchResponseOut": "_civicinfo_19_DivisionSearchResponseOut",
        "OfficeIn": "_civicinfo_20_OfficeIn",
        "OfficeOut": "_civicinfo_21_OfficeOut",
        "RepresentativeInfoResponseIn": "_civicinfo_22_RepresentativeInfoResponseIn",
        "RepresentativeInfoResponseOut": "_civicinfo_23_RepresentativeInfoResponseOut",
        "ContestIn": "_civicinfo_24_ContestIn",
        "ContestOut": "_civicinfo_25_ContestOut",
        "ElectionIn": "_civicinfo_26_ElectionIn",
        "ElectionOut": "_civicinfo_27_ElectionOut",
        "MessageSetIn": "_civicinfo_28_MessageSetIn",
        "MessageSetOut": "_civicinfo_29_MessageSetOut",
        "PrecinctIn": "_civicinfo_30_PrecinctIn",
        "PrecinctOut": "_civicinfo_31_PrecinctOut",
        "ElectionsQueryResponseIn": "_civicinfo_32_ElectionsQueryResponseIn",
        "ElectionsQueryResponseOut": "_civicinfo_33_ElectionsQueryResponseOut",
        "OfficialIn": "_civicinfo_34_OfficialIn",
        "OfficialOut": "_civicinfo_35_OfficialOut",
        "SimpleAddressTypeIn": "_civicinfo_36_SimpleAddressTypeIn",
        "SimpleAddressTypeOut": "_civicinfo_37_SimpleAddressTypeOut",
        "DivisionSearchResultIn": "_civicinfo_38_DivisionSearchResultIn",
        "DivisionSearchResultOut": "_civicinfo_39_DivisionSearchResultOut",
        "ChannelIn": "_civicinfo_40_ChannelIn",
        "ChannelOut": "_civicinfo_41_ChannelOut",
        "AdministrativeBodyIn": "_civicinfo_42_AdministrativeBodyIn",
        "AdministrativeBodyOut": "_civicinfo_43_AdministrativeBodyOut",
        "VoterInfoResponseIn": "_civicinfo_44_VoterInfoResponseIn",
        "VoterInfoResponseOut": "_civicinfo_45_VoterInfoResponseOut",
        "PollingLocationIn": "_civicinfo_46_PollingLocationIn",
        "PollingLocationOut": "_civicinfo_47_PollingLocationOut",
        "SourceIn": "_civicinfo_48_SourceIn",
        "SourceOut": "_civicinfo_49_SourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FeatureIdProtoIn"] = t.struct(
        {
            "fprint": t.string().optional(),
            "cellId": t.string().optional(),
            "temporaryData": t.proxy(renames["MessageSetIn"]).optional(),
        }
    ).named(renames["FeatureIdProtoIn"])
    types["FeatureIdProtoOut"] = t.struct(
        {
            "fprint": t.string().optional(),
            "cellId": t.string().optional(),
            "temporaryData": t.proxy(renames["MessageSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureIdProtoOut"])
    types["GeocodingSummaryIn"] = t.struct(
        {
            "featureType": t.string().optional(),
            "queryString": t.string().optional(),
            "positionPrecisionMeters": t.number().optional(),
            "addressUnderstood": t.boolean().optional(),
            "featureId": t.proxy(renames["FeatureIdProtoIn"]).optional(),
        }
    ).named(renames["GeocodingSummaryIn"])
    types["GeocodingSummaryOut"] = t.struct(
        {
            "featureType": t.string().optional(),
            "queryString": t.string().optional(),
            "positionPrecisionMeters": t.number().optional(),
            "addressUnderstood": t.boolean().optional(),
            "featureId": t.proxy(renames["FeatureIdProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeocodingSummaryOut"])
    types["GeographicDivisionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "officeIndices": t.array(t.integer()).optional(),
            "alsoKnownAs": t.array(t.string()).optional(),
        }
    ).named(renames["GeographicDivisionIn"])
    types["GeographicDivisionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "officeIndices": t.array(t.integer()).optional(),
            "alsoKnownAs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeographicDivisionOut"])
    types["ElectoralDistrictIn"] = t.struct(
        {
            "id": t.string().optional(),
            "scope": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ElectoralDistrictIn"])
    types["ElectoralDistrictOut"] = t.struct(
        {
            "id": t.string().optional(),
            "scope": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectoralDistrictOut"])
    types["AdministrationRegionIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "name": t.string().optional(),
            "local_jurisdiction": t.proxy(renames["AdministrationRegionIn"]).optional(),
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyIn"]
            ).optional(),
        }
    ).named(renames["AdministrationRegionIn"])
    types["AdministrationRegionOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "name": t.string().optional(),
            "local_jurisdiction": t.proxy(
                renames["AdministrationRegionOut"]
            ).optional(),
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrationRegionOut"])
    types["CandidateIn"] = t.struct(
        {
            "email": t.string().optional(),
            "name": t.string().optional(),
            "phone": t.string().optional(),
            "photoUrl": t.string().optional(),
            "orderOnBallot": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "candidateUrl": t.string().optional(),
            "party": t.string().optional(),
        }
    ).named(renames["CandidateIn"])
    types["CandidateOut"] = t.struct(
        {
            "email": t.string().optional(),
            "name": t.string().optional(),
            "phone": t.string().optional(),
            "photoUrl": t.string().optional(),
            "orderOnBallot": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "candidateUrl": t.string().optional(),
            "party": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandidateOut"])
    types["ElectionOfficialIn"] = t.struct(
        {
            "faxNumber": t.string().optional(),
            "officePhoneNumber": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "emailAddress": t.string().optional(),
        }
    ).named(renames["ElectionOfficialIn"])
    types["ElectionOfficialOut"] = t.struct(
        {
            "faxNumber": t.string().optional(),
            "officePhoneNumber": t.string().optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "emailAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOfficialOut"])
    types["RepresentativeInfoDataIn"] = t.struct(
        {
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RepresentativeInfoDataIn"])
    types["RepresentativeInfoDataOut"] = t.struct(
        {
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoDataOut"])
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
    types["OfficeIn"] = t.struct(
        {
            "divisionId": t.string().optional(),
            "name": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "levels": t.array(t.string()).optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["OfficeIn"])
    types["OfficeOut"] = t.struct(
        {
            "divisionId": t.string().optional(),
            "name": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "levels": t.array(t.string()).optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficeOut"])
    types["RepresentativeInfoResponseIn"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoResponseIn"])
    types["RepresentativeInfoResponseOut"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoResponseOut"])
    types["ContestIn"] = t.struct(
        {
            "ballotTitle": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumText": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "type": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateIn"])).optional(),
            "referendumBrief": t.string().optional(),
            "special": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "ballotPlacement": t.string().optional(),
            "district": t.proxy(renames["ElectoralDistrictIn"]).optional(),
            "primaryParties": t.array(t.string()).optional(),
            "referendumPassageThreshold": t.string().optional(),
            "office": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "electorateSpecifications": t.string().optional(),
        }
    ).named(renames["ContestIn"])
    types["ContestOut"] = t.struct(
        {
            "ballotTitle": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumText": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "numberVotingFor": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "type": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateOut"])).optional(),
            "referendumBrief": t.string().optional(),
            "special": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "ballotPlacement": t.string().optional(),
            "district": t.proxy(renames["ElectoralDistrictOut"]).optional(),
            "primaryParties": t.array(t.string()).optional(),
            "referendumPassageThreshold": t.string().optional(),
            "office": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "electorateSpecifications": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContestOut"])
    types["ElectionIn"] = t.struct(
        {
            "shapeLookupBehavior": t.string(),
            "name": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "id": t.string().optional(),
            "electionDay": t.string().optional(),
        }
    ).named(renames["ElectionIn"])
    types["ElectionOut"] = t.struct(
        {
            "shapeLookupBehavior": t.string(),
            "name": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "id": t.string().optional(),
            "electionDay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["PrecinctIn"] = t.struct(
        {
            "number": t.string().optional(),
            "name": t.string(),
            "administrationRegionId": t.string().optional(),
            "ward": t.string().optional(),
            "id": t.string(),
            "datasetId": t.string(),
            "contestId": t.array(t.string()).optional(),
            "mailOnly": t.boolean().optional(),
            "splitName": t.string().optional(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "ocdId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
        }
    ).named(renames["PrecinctIn"])
    types["PrecinctOut"] = t.struct(
        {
            "number": t.string().optional(),
            "name": t.string(),
            "administrationRegionId": t.string().optional(),
            "ward": t.string().optional(),
            "id": t.string(),
            "datasetId": t.string(),
            "contestId": t.array(t.string()).optional(),
            "mailOnly": t.boolean().optional(),
            "splitName": t.string().optional(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "ocdId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrecinctOut"])
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
    types["OfficialIn"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryIn"])
            ).optional(),
            "phones": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "photoUrl": t.string().optional(),
            "emails": t.array(t.string()).optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeIn"])).optional(),
        }
    ).named(renames["OfficialIn"])
    types["OfficialOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryOut"])
            ).optional(),
            "phones": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "photoUrl": t.string().optional(),
            "emails": t.array(t.string()).optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficialOut"])
    types["SimpleAddressTypeIn"] = t.struct(
        {
            "line1": t.string().optional(),
            "zip": t.string().optional(),
            "line3": t.string().optional(),
            "state": t.string().optional(),
            "locationName": t.string().optional(),
            "city": t.string().optional(),
            "line2": t.string().optional(),
        }
    ).named(renames["SimpleAddressTypeIn"])
    types["SimpleAddressTypeOut"] = t.struct(
        {
            "line1": t.string().optional(),
            "zip": t.string().optional(),
            "line3": t.string().optional(),
            "state": t.string().optional(),
            "locationName": t.string().optional(),
            "city": t.string().optional(),
            "line2": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleAddressTypeOut"])
    types["DivisionSearchResultIn"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "ocdId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DivisionSearchResultIn"])
    types["DivisionSearchResultOut"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "ocdId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DivisionSearchResultOut"])
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
    types["AdministrativeBodyIn"] = t.struct(
        {
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialIn"])
            ).optional(),
            "name": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "correspondenceAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "hoursOfOperation": t.string().optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
        }
    ).named(renames["AdministrativeBodyIn"])
    types["AdministrativeBodyOut"] = t.struct(
        {
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialOut"])
            ).optional(),
            "name": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "electionNoticeUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "correspondenceAddress": t.proxy(
                renames["SimpleAddressTypeOut"]
            ).optional(),
            "hoursOfOperation": t.string().optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrativeBodyOut"])
    types["VoterInfoResponseIn"] = t.struct(
        {
            "precincts": t.array(t.proxy(renames["PrecinctIn"])).optional(),
            "precinctId": t.string(),
            "contests": t.array(t.proxy(renames["ContestIn"])).optional(),
            "kind": t.string().optional(),
            "earlyVoteSites": t.array(t.proxy(renames["PollingLocationIn"])).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "election": t.proxy(renames["ElectionIn"]).optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionIn"])).optional(),
            "mailOnly": t.boolean().optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionIn"])).optional(),
        }
    ).named(renames["VoterInfoResponseIn"])
    types["VoterInfoResponseOut"] = t.struct(
        {
            "precincts": t.array(t.proxy(renames["PrecinctOut"])).optional(),
            "precinctId": t.string(),
            "contests": t.array(t.proxy(renames["ContestOut"])).optional(),
            "kind": t.string().optional(),
            "earlyVoteSites": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "election": t.proxy(renames["ElectionOut"]).optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionOut"])).optional(),
            "mailOnly": t.boolean().optional(),
            "state": t.array(t.proxy(renames["AdministrationRegionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoterInfoResponseOut"])
    types["PollingLocationIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "address": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "latitude": t.number().optional(),
            "startDate": t.string().optional(),
            "notes": t.string().optional(),
            "voterServices": t.string().optional(),
            "pollingHours": t.string().optional(),
            "longitude": t.number().optional(),
            "name": t.string().optional(),
            "endDate": t.string().optional(),
        }
    ).named(renames["PollingLocationIn"])
    types["PollingLocationOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "address": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "latitude": t.number().optional(),
            "startDate": t.string().optional(),
            "notes": t.string().optional(),
            "voterServices": t.string().optional(),
            "pollingHours": t.string().optional(),
            "longitude": t.number().optional(),
            "name": t.string().optional(),
            "endDate": t.string().optional(),
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

    functions = {}
    functions["representativesRepresentativeInfoByDivision"] = civicinfo.get(
        "civicinfo/v2/representatives",
        t.struct(
            {
                "address": t.string().optional(),
                "includeOffices": t.boolean().optional(),
                "roles": t.string().optional(),
                "levels": t.string().optional(),
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
                "address": t.string().optional(),
                "includeOffices": t.boolean().optional(),
                "roles": t.string().optional(),
                "levels": t.string().optional(),
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
                "officialOnly": t.boolean().optional(),
                "returnAllAvailableData": t.boolean().optional(),
                "electionId": t.string().optional(),
                "address": t.string().optional(),
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
                "officialOnly": t.boolean().optional(),
                "returnAllAvailableData": t.boolean().optional(),
                "electionId": t.string().optional(),
                "address": t.string().optional(),
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
        importer="civicinfo", renames=renames, types=types, functions=functions
    )
