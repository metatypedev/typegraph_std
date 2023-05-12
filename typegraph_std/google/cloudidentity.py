from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudidentity() -> Import:
    cloudidentity = HTTPRuntime("https://cloudidentity.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudidentity_1_ErrorResponse",
        "RestrictionEvaluationIn": "_cloudidentity_2_RestrictionEvaluationIn",
        "RestrictionEvaluationOut": "_cloudidentity_3_RestrictionEvaluationOut",
        "CreateMembershipMetadataIn": "_cloudidentity_4_CreateMembershipMetadataIn",
        "CreateMembershipMetadataOut": "_cloudidentity_5_CreateMembershipMetadataOut",
        "ListInboundSamlSsoProfilesResponseIn": "_cloudidentity_6_ListInboundSamlSsoProfilesResponseIn",
        "ListInboundSamlSsoProfilesResponseOut": "_cloudidentity_7_ListInboundSamlSsoProfilesResponseOut",
        "SecuritySettingsIn": "_cloudidentity_8_SecuritySettingsIn",
        "SecuritySettingsOut": "_cloudidentity_9_SecuritySettingsOut",
        "CancelUserInvitationRequestIn": "_cloudidentity_10_CancelUserInvitationRequestIn",
        "CancelUserInvitationRequestOut": "_cloudidentity_11_CancelUserInvitationRequestOut",
        "MemberRelationIn": "_cloudidentity_12_MemberRelationIn",
        "MemberRelationOut": "_cloudidentity_13_MemberRelationOut",
        "InboundSamlSsoProfileIn": "_cloudidentity_14_InboundSamlSsoProfileIn",
        "InboundSamlSsoProfileOut": "_cloudidentity_15_InboundSamlSsoProfileOut",
        "StatusIn": "_cloudidentity_16_StatusIn",
        "StatusOut": "_cloudidentity_17_StatusOut",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn": "_cloudidentity_18_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut": "_cloudidentity_19_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut",
        "SearchTransitiveGroupsResponseIn": "_cloudidentity_20_SearchTransitiveGroupsResponseIn",
        "SearchTransitiveGroupsResponseOut": "_cloudidentity_21_SearchTransitiveGroupsResponseOut",
        "DynamicGroupMetadataIn": "_cloudidentity_22_DynamicGroupMetadataIn",
        "DynamicGroupMetadataOut": "_cloudidentity_23_DynamicGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn": "_cloudidentity_24_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut": "_cloudidentity_25_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn": "_cloudidentity_26_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut": "_cloudidentity_27_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn": "_cloudidentity_28_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut": "_cloudidentity_29_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut",
        "MembershipIn": "_cloudidentity_30_MembershipIn",
        "MembershipOut": "_cloudidentity_31_MembershipOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn": "_cloudidentity_32_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut": "_cloudidentity_33_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn": "_cloudidentity_34_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut": "_cloudidentity_35_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut",
        "CreateGroupMetadataIn": "_cloudidentity_36_CreateGroupMetadataIn",
        "CreateGroupMetadataOut": "_cloudidentity_37_CreateGroupMetadataOut",
        "MembershipRoleRestrictionEvaluationIn": "_cloudidentity_38_MembershipRoleRestrictionEvaluationIn",
        "MembershipRoleRestrictionEvaluationOut": "_cloudidentity_39_MembershipRoleRestrictionEvaluationOut",
        "UpdateMembershipMetadataIn": "_cloudidentity_40_UpdateMembershipMetadataIn",
        "UpdateMembershipMetadataOut": "_cloudidentity_41_UpdateMembershipMetadataOut",
        "DynamicGroupStatusIn": "_cloudidentity_42_DynamicGroupStatusIn",
        "DynamicGroupStatusOut": "_cloudidentity_43_DynamicGroupStatusOut",
        "UpdateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_44_UpdateInboundSamlSsoProfileOperationMetadataIn",
        "UpdateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_45_UpdateInboundSamlSsoProfileOperationMetadataOut",
        "UserInvitationIn": "_cloudidentity_46_UserInvitationIn",
        "UserInvitationOut": "_cloudidentity_47_UserInvitationOut",
        "MemberRestrictionIn": "_cloudidentity_48_MemberRestrictionIn",
        "MemberRestrictionOut": "_cloudidentity_49_MemberRestrictionOut",
        "CreateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_50_CreateInboundSamlSsoProfileOperationMetadataIn",
        "CreateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_51_CreateInboundSamlSsoProfileOperationMetadataOut",
        "LookupMembershipNameResponseIn": "_cloudidentity_52_LookupMembershipNameResponseIn",
        "LookupMembershipNameResponseOut": "_cloudidentity_53_LookupMembershipNameResponseOut",
        "UpdateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_54_UpdateInboundSsoAssignmentOperationMetadataIn",
        "UpdateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_55_UpdateInboundSsoAssignmentOperationMetadataOut",
        "ListIdpCredentialsResponseIn": "_cloudidentity_56_ListIdpCredentialsResponseIn",
        "ListIdpCredentialsResponseOut": "_cloudidentity_57_ListIdpCredentialsResponseOut",
        "TransitiveMembershipRoleIn": "_cloudidentity_58_TransitiveMembershipRoleIn",
        "TransitiveMembershipRoleOut": "_cloudidentity_59_TransitiveMembershipRoleOut",
        "GroupRelationIn": "_cloudidentity_60_GroupRelationIn",
        "GroupRelationOut": "_cloudidentity_61_GroupRelationOut",
        "GoogleAppsCloudidentityDevicesV1DeviceIn": "_cloudidentity_62_GoogleAppsCloudidentityDevicesV1DeviceIn",
        "GoogleAppsCloudidentityDevicesV1DeviceOut": "_cloudidentity_63_GoogleAppsCloudidentityDevicesV1DeviceOut",
        "RsaPublicKeyInfoIn": "_cloudidentity_64_RsaPublicKeyInfoIn",
        "RsaPublicKeyInfoOut": "_cloudidentity_65_RsaPublicKeyInfoOut",
        "SearchGroupsResponseIn": "_cloudidentity_66_SearchGroupsResponseIn",
        "SearchGroupsResponseOut": "_cloudidentity_67_SearchGroupsResponseOut",
        "ModifyMembershipRolesRequestIn": "_cloudidentity_68_ModifyMembershipRolesRequestIn",
        "ModifyMembershipRolesRequestOut": "_cloudidentity_69_ModifyMembershipRolesRequestOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn": "_cloudidentity_70_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut": "_cloudidentity_71_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn": "_cloudidentity_72_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut": "_cloudidentity_73_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut",
        "ModifyMembershipRolesResponseIn": "_cloudidentity_74_ModifyMembershipRolesResponseIn",
        "ModifyMembershipRolesResponseOut": "_cloudidentity_75_ModifyMembershipRolesResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn": "_cloudidentity_76_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut": "_cloudidentity_77_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut",
        "SendUserInvitationRequestIn": "_cloudidentity_78_SendUserInvitationRequestIn",
        "SendUserInvitationRequestOut": "_cloudidentity_79_SendUserInvitationRequestOut",
        "LookupGroupNameResponseIn": "_cloudidentity_80_LookupGroupNameResponseIn",
        "LookupGroupNameResponseOut": "_cloudidentity_81_LookupGroupNameResponseOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn": "_cloudidentity_82_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut": "_cloudidentity_83_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn": "_cloudidentity_84_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut": "_cloudidentity_85_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn": "_cloudidentity_86_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut": "_cloudidentity_87_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut",
        "UpdateGroupMetadataIn": "_cloudidentity_88_UpdateGroupMetadataIn",
        "UpdateGroupMetadataOut": "_cloudidentity_89_UpdateGroupMetadataOut",
        "UpdateMembershipRolesParamsIn": "_cloudidentity_90_UpdateMembershipRolesParamsIn",
        "UpdateMembershipRolesParamsOut": "_cloudidentity_91_UpdateMembershipRolesParamsOut",
        "DeleteGroupMetadataIn": "_cloudidentity_92_DeleteGroupMetadataIn",
        "DeleteGroupMetadataOut": "_cloudidentity_93_DeleteGroupMetadataOut",
        "ExpiryDetailIn": "_cloudidentity_94_ExpiryDetailIn",
        "ExpiryDetailOut": "_cloudidentity_95_ExpiryDetailOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn": "_cloudidentity_96_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut": "_cloudidentity_97_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn": "_cloudidentity_98_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut": "_cloudidentity_99_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut",
        "ListInboundSsoAssignmentsResponseIn": "_cloudidentity_100_ListInboundSsoAssignmentsResponseIn",
        "ListInboundSsoAssignmentsResponseOut": "_cloudidentity_101_ListInboundSsoAssignmentsResponseOut",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesIn": "_cloudidentity_102_GoogleAppsCloudidentityDevicesV1AndroidAttributesIn",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesOut": "_cloudidentity_103_GoogleAppsCloudidentityDevicesV1AndroidAttributesOut",
        "SearchDirectGroupsResponseIn": "_cloudidentity_104_SearchDirectGroupsResponseIn",
        "SearchDirectGroupsResponseOut": "_cloudidentity_105_SearchDirectGroupsResponseOut",
        "DsaPublicKeyInfoIn": "_cloudidentity_106_DsaPublicKeyInfoIn",
        "DsaPublicKeyInfoOut": "_cloudidentity_107_DsaPublicKeyInfoOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn": "_cloudidentity_108_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut": "_cloudidentity_109_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut",
        "AddIdpCredentialRequestIn": "_cloudidentity_110_AddIdpCredentialRequestIn",
        "AddIdpCredentialRequestOut": "_cloudidentity_111_AddIdpCredentialRequestOut",
        "RestrictionEvaluationsIn": "_cloudidentity_112_RestrictionEvaluationsIn",
        "RestrictionEvaluationsOut": "_cloudidentity_113_RestrictionEvaluationsOut",
        "SearchTransitiveMembershipsResponseIn": "_cloudidentity_114_SearchTransitiveMembershipsResponseIn",
        "SearchTransitiveMembershipsResponseOut": "_cloudidentity_115_SearchTransitiveMembershipsResponseOut",
        "IsInvitableUserResponseIn": "_cloudidentity_116_IsInvitableUserResponseIn",
        "IsInvitableUserResponseOut": "_cloudidentity_117_IsInvitableUserResponseOut",
        "SamlIdpConfigIn": "_cloudidentity_118_SamlIdpConfigIn",
        "SamlIdpConfigOut": "_cloudidentity_119_SamlIdpConfigOut",
        "GroupIn": "_cloudidentity_120_GroupIn",
        "GroupOut": "_cloudidentity_121_GroupOut",
        "OperationIn": "_cloudidentity_122_OperationIn",
        "OperationOut": "_cloudidentity_123_OperationOut",
        "CheckTransitiveMembershipResponseIn": "_cloudidentity_124_CheckTransitiveMembershipResponseIn",
        "CheckTransitiveMembershipResponseOut": "_cloudidentity_125_CheckTransitiveMembershipResponseOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn": "_cloudidentity_126_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut": "_cloudidentity_127_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut",
        "DeleteIdpCredentialOperationMetadataIn": "_cloudidentity_128_DeleteIdpCredentialOperationMetadataIn",
        "DeleteIdpCredentialOperationMetadataOut": "_cloudidentity_129_DeleteIdpCredentialOperationMetadataOut",
        "ListMembershipsResponseIn": "_cloudidentity_130_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_cloudidentity_131_ListMembershipsResponseOut",
        "DynamicGroupQueryIn": "_cloudidentity_132_DynamicGroupQueryIn",
        "DynamicGroupQueryOut": "_cloudidentity_133_DynamicGroupQueryOut",
        "SignInBehaviorIn": "_cloudidentity_134_SignInBehaviorIn",
        "SignInBehaviorOut": "_cloudidentity_135_SignInBehaviorOut",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn": "_cloudidentity_136_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut": "_cloudidentity_137_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut",
        "ListUserInvitationsResponseIn": "_cloudidentity_138_ListUserInvitationsResponseIn",
        "ListUserInvitationsResponseOut": "_cloudidentity_139_ListUserInvitationsResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn": "_cloudidentity_140_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut": "_cloudidentity_141_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn": "_cloudidentity_142_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut": "_cloudidentity_143_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut",
        "GetMembershipGraphMetadataIn": "_cloudidentity_144_GetMembershipGraphMetadataIn",
        "GetMembershipGraphMetadataOut": "_cloudidentity_145_GetMembershipGraphMetadataOut",
        "AddIdpCredentialOperationMetadataIn": "_cloudidentity_146_AddIdpCredentialOperationMetadataIn",
        "AddIdpCredentialOperationMetadataOut": "_cloudidentity_147_AddIdpCredentialOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn": "_cloudidentity_148_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut": "_cloudidentity_149_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut",
        "MembershipRoleIn": "_cloudidentity_150_MembershipRoleIn",
        "MembershipRoleOut": "_cloudidentity_151_MembershipRoleOut",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn": "_cloudidentity_152_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut": "_cloudidentity_153_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn": "_cloudidentity_154_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut": "_cloudidentity_155_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut",
        "IdpCredentialIn": "_cloudidentity_156_IdpCredentialIn",
        "IdpCredentialOut": "_cloudidentity_157_IdpCredentialOut",
        "GoogleAppsCloudidentityDevicesV1DeviceUserIn": "_cloudidentity_158_GoogleAppsCloudidentityDevicesV1DeviceUserIn",
        "GoogleAppsCloudidentityDevicesV1DeviceUserOut": "_cloudidentity_159_GoogleAppsCloudidentityDevicesV1DeviceUserOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn": "_cloudidentity_160_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut": "_cloudidentity_161_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn": "_cloudidentity_162_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut": "_cloudidentity_163_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut",
        "DeleteMembershipMetadataIn": "_cloudidentity_164_DeleteMembershipMetadataIn",
        "DeleteMembershipMetadataOut": "_cloudidentity_165_DeleteMembershipMetadataOut",
        "DeleteInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_166_DeleteInboundSsoAssignmentOperationMetadataIn",
        "DeleteInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_167_DeleteInboundSsoAssignmentOperationMetadataOut",
        "EntityKeyIn": "_cloudidentity_168_EntityKeyIn",
        "EntityKeyOut": "_cloudidentity_169_EntityKeyOut",
        "SamlSsoInfoIn": "_cloudidentity_170_SamlSsoInfoIn",
        "SamlSsoInfoOut": "_cloudidentity_171_SamlSsoInfoOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn": "_cloudidentity_172_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut": "_cloudidentity_173_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut",
        "SamlSpConfigIn": "_cloudidentity_174_SamlSpConfigIn",
        "SamlSpConfigOut": "_cloudidentity_175_SamlSpConfigOut",
        "MembershipAdjacencyListIn": "_cloudidentity_176_MembershipAdjacencyListIn",
        "MembershipAdjacencyListOut": "_cloudidentity_177_MembershipAdjacencyListOut",
        "GetMembershipGraphResponseIn": "_cloudidentity_178_GetMembershipGraphResponseIn",
        "GetMembershipGraphResponseOut": "_cloudidentity_179_GetMembershipGraphResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn": "_cloudidentity_180_GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut": "_cloudidentity_181_GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut",
        "GoogleAppsCloudidentityDevicesV1ClientStateIn": "_cloudidentity_182_GoogleAppsCloudidentityDevicesV1ClientStateIn",
        "GoogleAppsCloudidentityDevicesV1ClientStateOut": "_cloudidentity_183_GoogleAppsCloudidentityDevicesV1ClientStateOut",
        "CreateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_184_CreateInboundSsoAssignmentOperationMetadataIn",
        "CreateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_185_CreateInboundSsoAssignmentOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn": "_cloudidentity_186_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut": "_cloudidentity_187_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut",
        "ListGroupsResponseIn": "_cloudidentity_188_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_cloudidentity_189_ListGroupsResponseOut",
        "DeleteInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_190_DeleteInboundSamlSsoProfileOperationMetadataIn",
        "DeleteInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_191_DeleteInboundSamlSsoProfileOperationMetadataOut",
        "InboundSsoAssignmentIn": "_cloudidentity_192_InboundSsoAssignmentIn",
        "InboundSsoAssignmentOut": "_cloudidentity_193_InboundSsoAssignmentOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn": "_cloudidentity_194_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut": "_cloudidentity_195_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut",
        "MembershipRelationIn": "_cloudidentity_196_MembershipRelationIn",
        "MembershipRelationOut": "_cloudidentity_197_MembershipRelationOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn": "_cloudidentity_198_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut": "_cloudidentity_199_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn": "_cloudidentity_200_GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut": "_cloudidentity_201_GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RestrictionEvaluationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestrictionEvaluationIn"]
    )
    types["RestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionEvaluationOut"])
    types["CreateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateMembershipMetadataIn"]
    )
    types["CreateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateMembershipMetadataOut"])
    types["ListInboundSamlSsoProfilesResponseIn"] = t.struct(
        {
            "inboundSamlSsoProfiles": t.array(
                t.proxy(renames["InboundSamlSsoProfileIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInboundSamlSsoProfilesResponseIn"])
    types["ListInboundSamlSsoProfilesResponseOut"] = t.struct(
        {
            "inboundSamlSsoProfiles": t.array(
                t.proxy(renames["InboundSamlSsoProfileOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInboundSamlSsoProfilesResponseOut"])
    types["SecuritySettingsIn"] = t.struct(
        {"memberRestriction": t.proxy(renames["MemberRestrictionIn"]).optional()}
    ).named(renames["SecuritySettingsIn"])
    types["SecuritySettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "memberRestriction": t.proxy(renames["MemberRestrictionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecuritySettingsOut"])
    types["CancelUserInvitationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelUserInvitationRequestIn"])
    types["CancelUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelUserInvitationRequestOut"])
    types["MemberRelationIn"] = t.struct(
        {
            "member": t.string().optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyIn"])).optional(),
            "relationType": t.string().optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
        }
    ).named(renames["MemberRelationIn"])
    types["MemberRelationOut"] = t.struct(
        {
            "member": t.string().optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "relationType": t.string().optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberRelationOut"])
    types["InboundSamlSsoProfileIn"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
            "customer": t.string().optional(),
            "displayName": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileIn"])
    types["InboundSamlSsoProfileOut"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigOut"]).optional(),
            "customer": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"])
    types["SearchTransitiveGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["GroupRelationIn"])).optional(),
        }
    ).named(renames["SearchTransitiveGroupsResponseIn"])
    types["SearchTransitiveGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["GroupRelationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTransitiveGroupsResponseOut"])
    types["DynamicGroupMetadataIn"] = t.struct(
        {"queries": t.array(t.proxy(renames["DynamicGroupQueryIn"])).optional()}
    ).named(renames["DynamicGroupMetadataIn"])
    types["DynamicGroupMetadataOut"] = t.struct(
        {
            "status": t.proxy(renames["DynamicGroupStatusOut"]).optional(),
            "queries": t.array(t.proxy(renames["DynamicGroupQueryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"])
    types["MembershipIn"] = t.struct(
        {
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyIn"]),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyOut"]),
            "deliverySetting": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut"])
    types["CreateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateGroupMetadataIn"]
    )
    types["CreateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateGroupMetadataOut"])
    types["MembershipRoleRestrictionEvaluationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipRoleRestrictionEvaluationIn"])
    types["MembershipRoleRestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleRestrictionEvaluationOut"])
    types["UpdateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateMembershipMetadataIn"]
    )
    types["UpdateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateMembershipMetadataOut"])
    types["DynamicGroupStatusIn"] = t.struct(
        {"statusTime": t.string().optional(), "status": t.string().optional()}
    ).named(renames["DynamicGroupStatusIn"])
    types["DynamicGroupStatusOut"] = t.struct(
        {
            "statusTime": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupStatusOut"])
    types["UpdateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataIn"])
    types["UpdateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataOut"])
    types["UserInvitationIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserInvitationIn"])
    types["UserInvitationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInvitationOut"])
    types["MemberRestrictionIn"] = t.struct(
        {
            "query": t.string().optional(),
            "evaluation": t.proxy(renames["RestrictionEvaluationIn"]).optional(),
        }
    ).named(renames["MemberRestrictionIn"])
    types["MemberRestrictionOut"] = t.struct(
        {
            "query": t.string().optional(),
            "evaluation": t.proxy(renames["RestrictionEvaluationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberRestrictionOut"])
    types["CreateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataIn"])
    types["CreateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataOut"])
    types["LookupMembershipNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupMembershipNameResponseIn"])
    types["LookupMembershipNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupMembershipNameResponseOut"])
    types["UpdateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataIn"])
    types["UpdateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataOut"])
    types["ListIdpCredentialsResponseIn"] = t.struct(
        {
            "idpCredentials": t.array(t.proxy(renames["IdpCredentialIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListIdpCredentialsResponseIn"])
    types["ListIdpCredentialsResponseOut"] = t.struct(
        {
            "idpCredentials": t.array(t.proxy(renames["IdpCredentialOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIdpCredentialsResponseOut"])
    types["TransitiveMembershipRoleIn"] = t.struct(
        {"role": t.string().optional()}
    ).named(renames["TransitiveMembershipRoleIn"])
    types["TransitiveMembershipRoleOut"] = t.struct(
        {
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitiveMembershipRoleOut"])
    types["GroupRelationIn"] = t.struct(
        {
            "relationType": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "group": t.string().optional(),
            "displayName": t.string().optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
        }
    ).named(renames["GroupRelationIn"])
    types["GroupRelationOut"] = t.struct(
        {
            "relationType": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "group": t.string().optional(),
            "displayName": t.string().optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupRelationOut"])
    types["GoogleAppsCloudidentityDevicesV1DeviceIn"] = t.struct(
        {
            "assetTag": t.string().optional(),
            "serialNumber": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "deviceId": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceOut"] = t.struct(
        {
            "bootloaderVersion": t.string().optional(),
            "ownerType": t.string().optional(),
            "brand": t.string().optional(),
            "encryptionState": t.string().optional(),
            "deviceType": t.string().optional(),
            "manufacturer": t.string().optional(),
            "compromisedState": t.string().optional(),
            "model": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "assetTag": t.string().optional(),
            "osVersion": t.string().optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "androidSpecificAttributes": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"]
            ).optional(),
            "otherAccounts": t.array(t.string()).optional(),
            "enabledDeveloperOptions": t.boolean().optional(),
            "enabledUsbDebugging": t.boolean().optional(),
            "serialNumber": t.string().optional(),
            "securityPatchTime": t.string().optional(),
            "buildNumber": t.string().optional(),
            "networkOperator": t.string().optional(),
            "basebandVersion": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "createTime": t.string().optional(),
            "deviceId": t.string().optional(),
            "name": t.string().optional(),
            "managementState": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "releaseVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
    types["RsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["RsaPublicKeyInfoIn"]
    )
    types["RsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaPublicKeyInfoOut"])
    types["SearchGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["SearchGroupsResponseIn"])
    types["SearchGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGroupsResponseOut"])
    types["ModifyMembershipRolesRequestIn"] = t.struct(
        {
            "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "removeRoles": t.array(t.string()).optional(),
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsIn"])
            ).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestIn"])
    types["ModifyMembershipRolesRequestOut"] = t.struct(
        {
            "addRoles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "removeRoles": t.array(t.string()).optional(),
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"])
    types["ModifyMembershipRolesResponseIn"] = t.struct(
        {"membership": t.proxy(renames["MembershipIn"]).optional()}
    ).named(renames["ModifyMembershipRolesResponseIn"])
    types["ModifyMembershipRolesResponseOut"] = t.struct(
        {
            "membership": t.proxy(renames["MembershipOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"])
    types["SendUserInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendUserInvitationRequestIn"]
    )
    types["SendUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendUserInvitationRequestOut"])
    types["LookupGroupNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupGroupNameResponseIn"])
    types["LookupGroupNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupGroupNameResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn"] = t.struct(
        {
            "device": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut"] = t.struct(
        {
            "device": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut"])
    types["UpdateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateGroupMetadataIn"]
    )
    types["UpdateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateGroupMetadataOut"])
    types["UpdateMembershipRolesParamsIn"] = t.struct(
        {
            "membershipRole": t.proxy(renames["MembershipRoleIn"]).optional(),
            "fieldMask": t.string().optional(),
        }
    ).named(renames["UpdateMembershipRolesParamsIn"])
    types["UpdateMembershipRolesParamsOut"] = t.struct(
        {
            "membershipRole": t.proxy(renames["MembershipRoleOut"]).optional(),
            "fieldMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMembershipRolesParamsOut"])
    types["DeleteGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteGroupMetadataIn"]
    )
    types["DeleteGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteGroupMetadataOut"])
    types["ExpiryDetailIn"] = t.struct({"expireTime": t.string().optional()}).named(
        renames["ExpiryDetailIn"]
    )
    types["ExpiryDetailOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpiryDetailOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"])
    types["ListInboundSsoAssignmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inboundSsoAssignments": t.array(
                t.proxy(renames["InboundSsoAssignmentIn"])
            ).optional(),
        }
    ).named(renames["ListInboundSsoAssignmentsResponseIn"])
    types["ListInboundSsoAssignmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inboundSsoAssignments": t.array(
                t.proxy(renames["InboundSsoAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInboundSsoAssignmentsResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"] = t.struct(
        {
            "enabledUnknownSources": t.boolean().optional(),
            "supportsWorkProfile": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"] = t.struct(
        {
            "enabledUnknownSources": t.boolean().optional(),
            "supportsWorkProfile": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"])
    types["SearchDirectGroupsResponseIn"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MembershipRelationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchDirectGroupsResponseIn"])
    types["SearchDirectGroupsResponseOut"] = t.struct(
        {
            "memberships": t.array(
                t.proxy(renames["MembershipRelationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDirectGroupsResponseOut"])
    types["DsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["DsaPublicKeyInfoIn"]
    )
    types["DsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsaPublicKeyInfoOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn"] = t.struct(
        {
            "device": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut"] = t.struct(
        {
            "device": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut"])
    types["AddIdpCredentialRequestIn"] = t.struct(
        {"pemData": t.string().optional()}
    ).named(renames["AddIdpCredentialRequestIn"])
    types["AddIdpCredentialRequestOut"] = t.struct(
        {
            "pemData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddIdpCredentialRequestOut"])
    types["RestrictionEvaluationsIn"] = t.struct(
        {
            "memberRestrictionEvaluation": t.proxy(
                renames["MembershipRoleRestrictionEvaluationIn"]
            ).optional()
        }
    ).named(renames["RestrictionEvaluationsIn"])
    types["RestrictionEvaluationsOut"] = t.struct(
        {
            "memberRestrictionEvaluation": t.proxy(
                renames["MembershipRoleRestrictionEvaluationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionEvaluationsOut"])
    types["SearchTransitiveMembershipsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MemberRelationIn"])).optional(),
        }
    ).named(renames["SearchTransitiveMembershipsResponseIn"])
    types["SearchTransitiveMembershipsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MemberRelationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTransitiveMembershipsResponseOut"])
    types["IsInvitableUserResponseIn"] = t.struct(
        {"isInvitableUser": t.boolean().optional()}
    ).named(renames["IsInvitableUserResponseIn"])
    types["IsInvitableUserResponseOut"] = t.struct(
        {
            "isInvitableUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IsInvitableUserResponseOut"])
    types["SamlIdpConfigIn"] = t.struct(
        {
            "entityId": t.string(),
            "changePasswordUri": t.string().optional(),
            "singleSignOnServiceUri": t.string(),
            "logoutRedirectUri": t.string().optional(),
        }
    ).named(renames["SamlIdpConfigIn"])
    types["SamlIdpConfigOut"] = t.struct(
        {
            "entityId": t.string(),
            "changePasswordUri": t.string().optional(),
            "singleSignOnServiceUri": t.string(),
            "logoutRedirectUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlIdpConfigOut"])
    types["GroupIn"] = t.struct(
        {
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]),
            "parent": t.string(),
            "labels": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataOut"]
            ).optional(),
            "name": t.string().optional(),
            "additionalGroupKeys": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]),
            "createTime": t.string().optional(),
            "parent": t.string(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["CheckTransitiveMembershipResponseIn"] = t.struct(
        {"hasMembership": t.boolean().optional()}
    ).named(renames["CheckTransitiveMembershipResponseIn"])
    types["CheckTransitiveMembershipResponseOut"] = t.struct(
        {
            "hasMembership": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckTransitiveMembershipResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"])
    types["DeleteIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataIn"])
    types["DeleteIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["DynamicGroupQueryIn"] = t.struct(
        {"query": t.string().optional(), "resourceType": t.string().optional()}
    ).named(renames["DynamicGroupQueryIn"])
    types["DynamicGroupQueryOut"] = t.struct(
        {
            "query": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupQueryOut"])
    types["SignInBehaviorIn"] = t.struct(
        {"redirectCondition": t.string().optional()}
    ).named(renames["SignInBehaviorIn"])
    types["SignInBehaviorOut"] = t.struct(
        {
            "redirectCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignInBehaviorOut"])
    types["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "customer": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"])
    types[
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"]
    )
    types["ListUserInvitationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userInvitations": t.array(t.proxy(renames["UserInvitationIn"])).optional(),
        }
    ).named(renames["ListUserInvitationsResponseIn"])
    types["ListUserInvitationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "userInvitations": t.array(
                t.proxy(renames["UserInvitationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserInvitationsResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deviceUsers": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deviceUsers": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"])
    types["GetMembershipGraphMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMembershipGraphMetadataIn"])
    types["GetMembershipGraphMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetMembershipGraphMetadataOut"])
    types["AddIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AddIdpCredentialOperationMetadataIn"])
    types["AddIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddIdpCredentialOperationMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn"] = t.struct(
        {"customer": t.string().optional(), "removeResetLock": t.boolean().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "removeResetLock": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut"])
    types["MembershipRoleIn"] = t.struct(
        {
            "expiryDetail": t.proxy(renames["ExpiryDetailIn"]).optional(),
            "name": t.string().optional(),
            "restrictionEvaluations": t.proxy(
                renames["RestrictionEvaluationsIn"]
            ).optional(),
        }
    ).named(renames["MembershipRoleIn"])
    types["MembershipRoleOut"] = t.struct(
        {
            "expiryDetail": t.proxy(renames["ExpiryDetailOut"]).optional(),
            "name": t.string().optional(),
            "restrictionEvaluations": t.proxy(
                renames["RestrictionEvaluationsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleOut"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"])
    types["IdpCredentialIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdpCredentialIn"]
    )
    types["IdpCredentialOut"] = t.struct(
        {
            "dsaKeyInfo": t.proxy(renames["DsaPublicKeyInfoOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "rsaKeyInfo": t.proxy(renames["RsaPublicKeyInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpCredentialOut"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserIn"] = t.struct(
        {
            "compromisedState": t.string().optional(),
            "userEmail": t.string().optional(),
            "passwordState": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserOut"] = t.struct(
        {
            "compromisedState": t.string().optional(),
            "languageCode": t.string().optional(),
            "userEmail": t.string().optional(),
            "managementState": t.string().optional(),
            "userAgent": t.string().optional(),
            "name": t.string().optional(),
            "passwordState": t.string().optional(),
            "createTime": t.string().optional(),
            "firstSyncTime": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientStates": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "clientStates": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"])
    types["DeleteMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMembershipMetadataIn"]
    )
    types["DeleteMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMembershipMetadataOut"])
    types["DeleteInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataIn"])
    types["DeleteInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataOut"])
    types["EntityKeyIn"] = t.struct(
        {"id": t.string().optional(), "namespace": t.string().optional()}
    ).named(renames["EntityKeyIn"])
    types["EntityKeyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "namespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityKeyOut"])
    types["SamlSsoInfoIn"] = t.struct({"inboundSamlSsoProfile": t.string()}).named(
        renames["SamlSsoInfoIn"]
    )
    types["SamlSsoInfoOut"] = t.struct(
        {
            "inboundSamlSsoProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSsoInfoOut"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"])
    types["SamlSpConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SamlSpConfigIn"]
    )
    types["SamlSpConfigOut"] = t.struct(
        {
            "assertionConsumerServiceUri": t.string().optional(),
            "entityId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSpConfigOut"])
    types["MembershipAdjacencyListIn"] = t.struct(
        {
            "group": t.string().optional(),
            "edges": t.array(t.proxy(renames["MembershipIn"])).optional(),
        }
    ).named(renames["MembershipAdjacencyListIn"])
    types["MembershipAdjacencyListOut"] = t.struct(
        {
            "group": t.string().optional(),
            "edges": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipAdjacencyListOut"])
    types["GetMembershipGraphResponseIn"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
            "adjacencyList": t.array(
                t.proxy(renames["MembershipAdjacencyListIn"])
            ).optional(),
        }
    ).named(renames["GetMembershipGraphResponseIn"])
    types["GetMembershipGraphResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "adjacencyList": t.array(
                t.proxy(renames["MembershipAdjacencyListOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetMembershipGraphResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateIn"] = t.struct(
        {
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "healthScore": t.string().optional(),
            "complianceState": t.string().optional(),
            "managed": t.string().optional(),
            "customId": t.string().optional(),
            "assetTags": t.array(t.string()).optional(),
            "scoreReason": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateOut"] = t.struct(
        {
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "ownerType": t.string().optional(),
            "healthScore": t.string().optional(),
            "complianceState": t.string().optional(),
            "managed": t.string().optional(),
            "customId": t.string().optional(),
            "assetTags": t.array(t.string()).optional(),
            "scoreReason": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
    types["CreateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataIn"])
    types["CreateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["DeleteInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataIn"])
    types["DeleteInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataOut"])
    types["InboundSsoAssignmentIn"] = t.struct(
        {
            "ssoMode": t.string().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
            "rank": t.integer().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
            "targetGroup": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
        }
    ).named(renames["InboundSsoAssignmentIn"])
    types["InboundSsoAssignmentOut"] = t.struct(
        {
            "ssoMode": t.string().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorOut"]).optional(),
            "rank": t.integer().optional(),
            "name": t.string().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoOut"]).optional(),
            "targetGroup": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSsoAssignmentOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"]
            ).optional()
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut"] = t.struct(
        {
            "deviceUser": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut"])
    types["MembershipRelationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "membership": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
        }
    ).named(renames["MembershipRelationIn"])
    types["MembershipRelationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "membership": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRelationOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"])
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"] = t.struct(
        {
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"])

    functions = {}
    functions["inboundSamlSsoProfilesCreate"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "displayName": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesList"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "displayName": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesDelete"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "displayName": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesGet"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "displayName": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesPatch"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "displayName": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsList"] = cloudidentity.post(
        "v1/{parent}/idpCredentials:add",
        t.struct(
            {
                "parent": t.string(),
                "pemData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsDelete"] = cloudidentity.post(
        "v1/{parent}/idpCredentials:add",
        t.struct(
            {
                "parent": t.string(),
                "pemData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsGet"] = cloudidentity.post(
        "v1/{parent}/idpCredentials:add",
        t.struct(
            {
                "parent": t.string(),
                "pemData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsAdd"] = cloudidentity.post(
        "v1/{parent}/idpCredentials:add",
        t.struct(
            {
                "parent": t.string(),
                "pemData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsPatch"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "ssoMode": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsGet"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "ssoMode": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsDelete"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "ssoMode": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsList"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "ssoMode": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsCreate"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "ssoMode": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsCancel"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsGet"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsIsInvitableUser"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsSend"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsList"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCreate"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDelete"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesWipe"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCancelWipe"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesList"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "customer": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersList"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersCancelWipe"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersWipe"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersLookup"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersBlock"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersGet"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersDelete"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersApprove"] = cloudidentity.post(
        "v1/{name}:approve",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesList"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesPatch"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsLookup"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGetSecuritySettings"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsPatch"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGet"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsCreate"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdateSecuritySettings"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsSearch"] = cloudidentity.get(
        "v1/groups:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "query": t.string(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchGroupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGet"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGetMembershipGraph"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsModifyMembershipRoles"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsList"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsDelete"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCheckTransitiveMembership"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchDirectGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCreate"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsLookup"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveMemberships"] = cloudidentity.get(
        "v1/{parent}/memberships:searchTransitiveMemberships",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTransitiveMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudidentity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
