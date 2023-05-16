from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_civicinfo() -> Import:
    civicinfo = HTTPRuntime("https://civicinfo.googleapis.com/")

    renames = {
        "ErrorResponse": "_civicinfo_1_ErrorResponse",
        "ChannelIn": "_civicinfo_2_ChannelIn",
        "ChannelOut": "_civicinfo_3_ChannelOut",
        "SourceIn": "_civicinfo_4_SourceIn",
        "SourceOut": "_civicinfo_5_SourceOut",
        "FeatureIdProtoIn": "_civicinfo_6_FeatureIdProtoIn",
        "FeatureIdProtoOut": "_civicinfo_7_FeatureIdProtoOut",
        "DivisionSearchResultIn": "_civicinfo_8_DivisionSearchResultIn",
        "DivisionSearchResultOut": "_civicinfo_9_DivisionSearchResultOut",
        "ElectionsQueryResponseIn": "_civicinfo_10_ElectionsQueryResponseIn",
        "ElectionsQueryResponseOut": "_civicinfo_11_ElectionsQueryResponseOut",
        "AdministrationRegionIn": "_civicinfo_12_AdministrationRegionIn",
        "AdministrationRegionOut": "_civicinfo_13_AdministrationRegionOut",
        "GeocodingSummaryIn": "_civicinfo_14_GeocodingSummaryIn",
        "GeocodingSummaryOut": "_civicinfo_15_GeocodingSummaryOut",
        "ElectionIn": "_civicinfo_16_ElectionIn",
        "ElectionOut": "_civicinfo_17_ElectionOut",
        "PrecinctIn": "_civicinfo_18_PrecinctIn",
        "PrecinctOut": "_civicinfo_19_PrecinctOut",
        "DivisionSearchResponseIn": "_civicinfo_20_DivisionSearchResponseIn",
        "DivisionSearchResponseOut": "_civicinfo_21_DivisionSearchResponseOut",
        "CandidateIn": "_civicinfo_22_CandidateIn",
        "CandidateOut": "_civicinfo_23_CandidateOut",
        "AdministrativeBodyIn": "_civicinfo_24_AdministrativeBodyIn",
        "AdministrativeBodyOut": "_civicinfo_25_AdministrativeBodyOut",
        "OfficeIn": "_civicinfo_26_OfficeIn",
        "OfficeOut": "_civicinfo_27_OfficeOut",
        "ContestIn": "_civicinfo_28_ContestIn",
        "ContestOut": "_civicinfo_29_ContestOut",
        "RepresentativeInfoDataIn": "_civicinfo_30_RepresentativeInfoDataIn",
        "RepresentativeInfoDataOut": "_civicinfo_31_RepresentativeInfoDataOut",
        "RepresentativeInfoResponseIn": "_civicinfo_32_RepresentativeInfoResponseIn",
        "RepresentativeInfoResponseOut": "_civicinfo_33_RepresentativeInfoResponseOut",
        "VoterInfoResponseIn": "_civicinfo_34_VoterInfoResponseIn",
        "VoterInfoResponseOut": "_civicinfo_35_VoterInfoResponseOut",
        "SimpleAddressTypeIn": "_civicinfo_36_SimpleAddressTypeIn",
        "SimpleAddressTypeOut": "_civicinfo_37_SimpleAddressTypeOut",
        "OfficialIn": "_civicinfo_38_OfficialIn",
        "OfficialOut": "_civicinfo_39_OfficialOut",
        "MessageSetIn": "_civicinfo_40_MessageSetIn",
        "MessageSetOut": "_civicinfo_41_MessageSetOut",
        "ElectoralDistrictIn": "_civicinfo_42_ElectoralDistrictIn",
        "ElectoralDistrictOut": "_civicinfo_43_ElectoralDistrictOut",
        "ElectionOfficialIn": "_civicinfo_44_ElectionOfficialIn",
        "ElectionOfficialOut": "_civicinfo_45_ElectionOfficialOut",
        "PollingLocationIn": "_civicinfo_46_PollingLocationIn",
        "PollingLocationOut": "_civicinfo_47_PollingLocationOut",
        "GeographicDivisionIn": "_civicinfo_48_GeographicDivisionIn",
        "GeographicDivisionOut": "_civicinfo_49_GeographicDivisionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SourceIn"] = t.struct(
        {"official": t.boolean().optional(), "name": t.string().optional()}
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "official": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["FeatureIdProtoIn"] = t.struct(
        {
            "cellId": t.string().optional(),
            "temporaryData": t.proxy(renames["MessageSetIn"]).optional(),
            "fprint": t.string().optional(),
        }
    ).named(renames["FeatureIdProtoIn"])
    types["FeatureIdProtoOut"] = t.struct(
        {
            "cellId": t.string().optional(),
            "temporaryData": t.proxy(renames["MessageSetOut"]).optional(),
            "fprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureIdProtoOut"])
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
    types["AdministrationRegionIn"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyIn"]
            ).optional(),
            "local_jurisdiction": t.proxy(renames["AdministrationRegionIn"]).optional(),
            "name": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
        }
    ).named(renames["AdministrationRegionIn"])
    types["AdministrationRegionOut"] = t.struct(
        {
            "electionAdministrationBody": t.proxy(
                renames["AdministrativeBodyOut"]
            ).optional(),
            "local_jurisdiction": t.proxy(
                renames["AdministrationRegionOut"]
            ).optional(),
            "name": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrationRegionOut"])
    types["GeocodingSummaryIn"] = t.struct(
        {
            "featureType": t.string().optional(),
            "addressUnderstood": t.boolean().optional(),
            "queryString": t.string().optional(),
            "positionPrecisionMeters": t.number().optional(),
            "featureId": t.proxy(renames["FeatureIdProtoIn"]).optional(),
        }
    ).named(renames["GeocodingSummaryIn"])
    types["GeocodingSummaryOut"] = t.struct(
        {
            "featureType": t.string().optional(),
            "addressUnderstood": t.boolean().optional(),
            "queryString": t.string().optional(),
            "positionPrecisionMeters": t.number().optional(),
            "featureId": t.proxy(renames["FeatureIdProtoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GeocodingSummaryOut"])
    types["ElectionIn"] = t.struct(
        {
            "shapeLookupBehavior": t.string(),
            "id": t.string().optional(),
            "electionDay": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ElectionIn"])
    types["ElectionOut"] = t.struct(
        {
            "shapeLookupBehavior": t.string(),
            "id": t.string().optional(),
            "electionDay": t.string().optional(),
            "ocdDivisionId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOut"])
    types["PrecinctIn"] = t.struct(
        {
            "ocdId": t.array(t.string()).optional(),
            "administrationRegionId": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "id": t.string(),
            "contestId": t.array(t.string()).optional(),
            "number": t.string().optional(),
            "splitName": t.string().optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "name": t.string(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "ward": t.string().optional(),
            "mailOnly": t.boolean().optional(),
        }
    ).named(renames["PrecinctIn"])
    types["PrecinctOut"] = t.struct(
        {
            "ocdId": t.array(t.string()).optional(),
            "administrationRegionId": t.string().optional(),
            "electoralDistrictId": t.array(t.string()).optional(),
            "id": t.string(),
            "contestId": t.array(t.string()).optional(),
            "number": t.string().optional(),
            "splitName": t.string().optional(),
            "pollingLocationId": t.array(t.string()).optional(),
            "spatialBoundaryId": t.array(t.string()).optional(),
            "datasetId": t.string(),
            "name": t.string(),
            "earlyVoteSiteId": t.array(t.string()).optional(),
            "ward": t.string().optional(),
            "mailOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrecinctOut"])
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
    types["CandidateIn"] = t.struct(
        {
            "candidateUrl": t.string().optional(),
            "photoUrl": t.string().optional(),
            "phone": t.string().optional(),
            "email": t.string().optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "orderOnBallot": t.string().optional(),
        }
    ).named(renames["CandidateIn"])
    types["CandidateOut"] = t.struct(
        {
            "candidateUrl": t.string().optional(),
            "photoUrl": t.string().optional(),
            "phone": t.string().optional(),
            "email": t.string().optional(),
            "party": t.string().optional(),
            "name": t.string().optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "orderOnBallot": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CandidateOut"])
    types["AdministrativeBodyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialIn"])
            ).optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "correspondenceAddress": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "electionNoticeUrl": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "electionNoticeText": t.string().optional(),
        }
    ).named(renames["AdministrativeBodyIn"])
    types["AdministrativeBodyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "voter_services": t.array(t.string()).optional(),
            "electionRulesUrl": t.string().optional(),
            "electionInfoUrl": t.string().optional(),
            "physicalAddress": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "votingLocationFinderUrl": t.string().optional(),
            "electionOfficials": t.array(
                t.proxy(renames["ElectionOfficialOut"])
            ).optional(),
            "electionRegistrationConfirmationUrl": t.string().optional(),
            "electionRegistrationUrl": t.string().optional(),
            "ballotInfoUrl": t.string().optional(),
            "correspondenceAddress": t.proxy(
                renames["SimpleAddressTypeOut"]
            ).optional(),
            "electionNoticeUrl": t.string().optional(),
            "absenteeVotingInfoUrl": t.string().optional(),
            "hoursOfOperation": t.string().optional(),
            "electionNoticeText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministrativeBodyOut"])
    types["OfficeIn"] = t.struct(
        {
            "divisionId": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "levels": t.array(t.string()).optional(),
        }
    ).named(renames["OfficeIn"])
    types["OfficeOut"] = t.struct(
        {
            "divisionId": t.string().optional(),
            "roles": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "officialIndices": t.array(t.integer()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "levels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficeOut"])
    types["ContestIn"] = t.struct(
        {
            "office": t.string().optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumBrief": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumText": t.string().optional(),
            "special": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "ballotTitle": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "referendumPassageThreshold": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "electorateSpecifications": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "ballotPlacement": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateIn"])).optional(),
            "district": t.proxy(renames["ElectoralDistrictIn"]).optional(),
            "numberVotingFor": t.string().optional(),
        }
    ).named(renames["ContestIn"])
    types["ContestOut"] = t.struct(
        {
            "office": t.string().optional(),
            "referendumSubtitle": t.string().optional(),
            "referendumBrief": t.string().optional(),
            "numberElected": t.string().optional(),
            "referendumText": t.string().optional(),
            "special": t.string().optional(),
            "referendumConStatement": t.string().optional(),
            "primaryParties": t.array(t.string()).optional(),
            "ballotTitle": t.string().optional(),
            "referendumBallotResponses": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "referendumPassageThreshold": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "electorateSpecifications": t.string().optional(),
            "level": t.array(t.string()).optional(),
            "roles": t.array(t.string()).optional(),
            "ballotPlacement": t.string().optional(),
            "referendumEffectOfAbstain": t.string().optional(),
            "referendumTitle": t.string().optional(),
            "referendumUrl": t.string().optional(),
            "referendumProStatement": t.string().optional(),
            "candidates": t.array(t.proxy(renames["CandidateOut"])).optional(),
            "district": t.proxy(renames["ElectoralDistrictOut"]).optional(),
            "numberVotingFor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContestOut"])
    types["RepresentativeInfoDataIn"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoDataIn"])
    types["RepresentativeInfoDataOut"] = t.struct(
        {
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoDataOut"])
    types["RepresentativeInfoResponseIn"] = t.struct(
        {
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeIn"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "kind": t.string().optional(),
            "officials": t.array(t.proxy(renames["OfficialIn"])).optional(),
        }
    ).named(renames["RepresentativeInfoResponseIn"])
    types["RepresentativeInfoResponseOut"] = t.struct(
        {
            "divisions": t.struct({"_": t.string().optional()}).optional(),
            "offices": t.array(t.proxy(renames["OfficeOut"])).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "kind": t.string().optional(),
            "officials": t.array(t.proxy(renames["OfficialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepresentativeInfoResponseOut"])
    types["VoterInfoResponseIn"] = t.struct(
        {
            "precincts": t.array(t.proxy(renames["PrecinctIn"])).optional(),
            "election": t.proxy(renames["ElectionIn"]).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionIn"])).optional(),
            "kind": t.string().optional(),
            "precinctId": t.string(),
            "state": t.array(t.proxy(renames["AdministrationRegionIn"])).optional(),
            "mailOnly": t.boolean().optional(),
            "contests": t.array(t.proxy(renames["ContestIn"])).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationIn"])
            ).optional(),
            "earlyVoteSites": t.array(t.proxy(renames["PollingLocationIn"])).optional(),
        }
    ).named(renames["VoterInfoResponseIn"])
    types["VoterInfoResponseOut"] = t.struct(
        {
            "precincts": t.array(t.proxy(renames["PrecinctOut"])).optional(),
            "election": t.proxy(renames["ElectionOut"]).optional(),
            "normalizedInput": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "otherElections": t.array(t.proxy(renames["ElectionOut"])).optional(),
            "kind": t.string().optional(),
            "precinctId": t.string(),
            "state": t.array(t.proxy(renames["AdministrationRegionOut"])).optional(),
            "mailOnly": t.boolean().optional(),
            "contests": t.array(t.proxy(renames["ContestOut"])).optional(),
            "dropOffLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "pollingLocations": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "earlyVoteSites": t.array(
                t.proxy(renames["PollingLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VoterInfoResponseOut"])
    types["SimpleAddressTypeIn"] = t.struct(
        {
            "locationName": t.string().optional(),
            "zip": t.string().optional(),
            "line2": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
            "line3": t.string().optional(),
            "line1": t.string().optional(),
        }
    ).named(renames["SimpleAddressTypeIn"])
    types["SimpleAddressTypeOut"] = t.struct(
        {
            "locationName": t.string().optional(),
            "zip": t.string().optional(),
            "line2": t.string().optional(),
            "state": t.string().optional(),
            "city": t.string().optional(),
            "line3": t.string().optional(),
            "line1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SimpleAddressTypeOut"])
    types["OfficialIn"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelIn"])).optional(),
            "name": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryIn"])
            ).optional(),
            "phones": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "photoUrl": t.string().optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeIn"])).optional(),
        }
    ).named(renames["OfficialIn"])
    types["OfficialOut"] = t.struct(
        {
            "urls": t.array(t.string()).optional(),
            "emails": t.array(t.string()).optional(),
            "channels": t.array(t.proxy(renames["ChannelOut"])).optional(),
            "name": t.string().optional(),
            "geocodingSummaries": t.array(
                t.proxy(renames["GeocodingSummaryOut"])
            ).optional(),
            "phones": t.array(t.string()).optional(),
            "party": t.string().optional(),
            "photoUrl": t.string().optional(),
            "address": t.array(t.proxy(renames["SimpleAddressTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OfficialOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["ElectoralDistrictIn"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "scope": t.string().optional(),
        }
    ).named(renames["ElectoralDistrictIn"])
    types["ElectoralDistrictOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "scope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectoralDistrictOut"])
    types["ElectionOfficialIn"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "faxNumber": t.string().optional(),
            "name": t.string().optional(),
            "emailAddress": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ElectionOfficialIn"])
    types["ElectionOfficialOut"] = t.struct(
        {
            "officePhoneNumber": t.string().optional(),
            "faxNumber": t.string().optional(),
            "name": t.string().optional(),
            "emailAddress": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ElectionOfficialOut"])
    types["PollingLocationIn"] = t.struct(
        {
            "latitude": t.number().optional(),
            "pollingHours": t.string().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "startDate": t.string().optional(),
            "voterServices": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceIn"])).optional(),
            "longitude": t.number().optional(),
            "address": t.proxy(renames["SimpleAddressTypeIn"]).optional(),
        }
    ).named(renames["PollingLocationIn"])
    types["PollingLocationOut"] = t.struct(
        {
            "latitude": t.number().optional(),
            "pollingHours": t.string().optional(),
            "name": t.string().optional(),
            "notes": t.string().optional(),
            "startDate": t.string().optional(),
            "voterServices": t.string().optional(),
            "endDate": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "longitude": t.number().optional(),
            "address": t.proxy(renames["SimpleAddressTypeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PollingLocationOut"])
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

    functions = {}
    functions["divisionsSearch"] = civicinfo.get(
        "civicinfo/v2/divisions",
        t.struct({"query": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DivisionSearchResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["electionsElectionQuery"] = civicinfo.get(
        "civicinfo/v2/voterinfo",
        t.struct(
            {
                "officialOnly": t.boolean().optional(),
                "address": t.string().optional(),
                "returnAllAvailableData": t.boolean().optional(),
                "electionId": t.string().optional(),
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
                "address": t.string().optional(),
                "returnAllAvailableData": t.boolean().optional(),
                "electionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VoterInfoResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["representativesRepresentativeInfoByAddress"] = civicinfo.get(
        "civicinfo/v2/representatives/{ocdId}",
        t.struct(
            {
                "roles": t.string().optional(),
                "levels": t.string().optional(),
                "ocdId": t.string().optional(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepresentativeInfoDataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["representativesRepresentativeInfoByDivision"] = civicinfo.get(
        "civicinfo/v2/representatives/{ocdId}",
        t.struct(
            {
                "roles": t.string().optional(),
                "levels": t.string().optional(),
                "ocdId": t.string().optional(),
                "recursive": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RepresentativeInfoDataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="civicinfo",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
