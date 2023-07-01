from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudidentity():
    cloudidentity = HTTPRuntime("https://cloudidentity.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudidentity_1_ErrorResponse",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn": "_cloudidentity_2_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut": "_cloudidentity_3_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn": "_cloudidentity_4_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut": "_cloudidentity_5_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut",
        "MemberRelationIn": "_cloudidentity_6_MemberRelationIn",
        "MemberRelationOut": "_cloudidentity_7_MemberRelationOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn": "_cloudidentity_8_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut": "_cloudidentity_9_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn": "_cloudidentity_10_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut": "_cloudidentity_11_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut",
        "GetMembershipGraphResponseIn": "_cloudidentity_12_GetMembershipGraphResponseIn",
        "GetMembershipGraphResponseOut": "_cloudidentity_13_GetMembershipGraphResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn": "_cloudidentity_14_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut": "_cloudidentity_15_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut",
        "AddIdpCredentialRequestIn": "_cloudidentity_16_AddIdpCredentialRequestIn",
        "AddIdpCredentialRequestOut": "_cloudidentity_17_AddIdpCredentialRequestOut",
        "ModifyMembershipRolesRequestIn": "_cloudidentity_18_ModifyMembershipRolesRequestIn",
        "ModifyMembershipRolesRequestOut": "_cloudidentity_19_ModifyMembershipRolesRequestOut",
        "TransitiveMembershipRoleIn": "_cloudidentity_20_TransitiveMembershipRoleIn",
        "TransitiveMembershipRoleOut": "_cloudidentity_21_TransitiveMembershipRoleOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn": "_cloudidentity_22_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut": "_cloudidentity_23_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn": "_cloudidentity_24_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut": "_cloudidentity_25_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut",
        "ListInboundSamlSsoProfilesResponseIn": "_cloudidentity_26_ListInboundSamlSsoProfilesResponseIn",
        "ListInboundSamlSsoProfilesResponseOut": "_cloudidentity_27_ListInboundSamlSsoProfilesResponseOut",
        "GoogleAppsCloudidentityDevicesV1DeviceUserIn": "_cloudidentity_28_GoogleAppsCloudidentityDevicesV1DeviceUserIn",
        "GoogleAppsCloudidentityDevicesV1DeviceUserOut": "_cloudidentity_29_GoogleAppsCloudidentityDevicesV1DeviceUserOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn": "_cloudidentity_30_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut": "_cloudidentity_31_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut",
        "MembershipRelationIn": "_cloudidentity_32_MembershipRelationIn",
        "MembershipRelationOut": "_cloudidentity_33_MembershipRelationOut",
        "IdpCredentialIn": "_cloudidentity_34_IdpCredentialIn",
        "IdpCredentialOut": "_cloudidentity_35_IdpCredentialOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn": "_cloudidentity_36_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut": "_cloudidentity_37_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut",
        "CheckTransitiveMembershipResponseIn": "_cloudidentity_38_CheckTransitiveMembershipResponseIn",
        "CheckTransitiveMembershipResponseOut": "_cloudidentity_39_CheckTransitiveMembershipResponseOut",
        "SamlIdpConfigIn": "_cloudidentity_40_SamlIdpConfigIn",
        "SamlIdpConfigOut": "_cloudidentity_41_SamlIdpConfigOut",
        "OperationIn": "_cloudidentity_42_OperationIn",
        "OperationOut": "_cloudidentity_43_OperationOut",
        "ModifyMembershipRolesResponseIn": "_cloudidentity_44_ModifyMembershipRolesResponseIn",
        "ModifyMembershipRolesResponseOut": "_cloudidentity_45_ModifyMembershipRolesResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn": "_cloudidentity_46_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut": "_cloudidentity_47_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut",
        "DynamicGroupQueryIn": "_cloudidentity_48_DynamicGroupQueryIn",
        "DynamicGroupQueryOut": "_cloudidentity_49_DynamicGroupQueryOut",
        "MemberRestrictionIn": "_cloudidentity_50_MemberRestrictionIn",
        "MemberRestrictionOut": "_cloudidentity_51_MemberRestrictionOut",
        "SearchTransitiveMembershipsResponseIn": "_cloudidentity_52_SearchTransitiveMembershipsResponseIn",
        "SearchTransitiveMembershipsResponseOut": "_cloudidentity_53_SearchTransitiveMembershipsResponseOut",
        "RestrictionEvaluationIn": "_cloudidentity_54_RestrictionEvaluationIn",
        "RestrictionEvaluationOut": "_cloudidentity_55_RestrictionEvaluationOut",
        "RestrictionEvaluationsIn": "_cloudidentity_56_RestrictionEvaluationsIn",
        "RestrictionEvaluationsOut": "_cloudidentity_57_RestrictionEvaluationsOut",
        "IsInvitableUserResponseIn": "_cloudidentity_58_IsInvitableUserResponseIn",
        "IsInvitableUserResponseOut": "_cloudidentity_59_IsInvitableUserResponseOut",
        "CreateGroupMetadataIn": "_cloudidentity_60_CreateGroupMetadataIn",
        "CreateGroupMetadataOut": "_cloudidentity_61_CreateGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn": "_cloudidentity_62_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut": "_cloudidentity_63_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut",
        "DeleteIdpCredentialOperationMetadataIn": "_cloudidentity_64_DeleteIdpCredentialOperationMetadataIn",
        "DeleteIdpCredentialOperationMetadataOut": "_cloudidentity_65_DeleteIdpCredentialOperationMetadataOut",
        "SearchGroupsResponseIn": "_cloudidentity_66_SearchGroupsResponseIn",
        "SearchGroupsResponseOut": "_cloudidentity_67_SearchGroupsResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn": "_cloudidentity_68_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut": "_cloudidentity_69_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn": "_cloudidentity_70_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut": "_cloudidentity_71_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut",
        "EntityKeyIn": "_cloudidentity_72_EntityKeyIn",
        "EntityKeyOut": "_cloudidentity_73_EntityKeyOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn": "_cloudidentity_74_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut": "_cloudidentity_75_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn": "_cloudidentity_76_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut": "_cloudidentity_77_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut",
        "GoogleAppsCloudidentityDevicesV1DeviceIn": "_cloudidentity_78_GoogleAppsCloudidentityDevicesV1DeviceIn",
        "GoogleAppsCloudidentityDevicesV1DeviceOut": "_cloudidentity_79_GoogleAppsCloudidentityDevicesV1DeviceOut",
        "SendUserInvitationRequestIn": "_cloudidentity_80_SendUserInvitationRequestIn",
        "SendUserInvitationRequestOut": "_cloudidentity_81_SendUserInvitationRequestOut",
        "ListUserInvitationsResponseIn": "_cloudidentity_82_ListUserInvitationsResponseIn",
        "ListUserInvitationsResponseOut": "_cloudidentity_83_ListUserInvitationsResponseOut",
        "GoogleAppsCloudidentityDevicesV1ClientStateIn": "_cloudidentity_84_GoogleAppsCloudidentityDevicesV1ClientStateIn",
        "GoogleAppsCloudidentityDevicesV1ClientStateOut": "_cloudidentity_85_GoogleAppsCloudidentityDevicesV1ClientStateOut",
        "MembershipRoleIn": "_cloudidentity_86_MembershipRoleIn",
        "MembershipRoleOut": "_cloudidentity_87_MembershipRoleOut",
        "SamlSsoInfoIn": "_cloudidentity_88_SamlSsoInfoIn",
        "SamlSsoInfoOut": "_cloudidentity_89_SamlSsoInfoOut",
        "ExpiryDetailIn": "_cloudidentity_90_ExpiryDetailIn",
        "ExpiryDetailOut": "_cloudidentity_91_ExpiryDetailOut",
        "DsaPublicKeyInfoIn": "_cloudidentity_92_DsaPublicKeyInfoIn",
        "DsaPublicKeyInfoOut": "_cloudidentity_93_DsaPublicKeyInfoOut",
        "DeleteMembershipMetadataIn": "_cloudidentity_94_DeleteMembershipMetadataIn",
        "DeleteMembershipMetadataOut": "_cloudidentity_95_DeleteMembershipMetadataOut",
        "DeleteInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_96_DeleteInboundSamlSsoProfileOperationMetadataIn",
        "DeleteInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_97_DeleteInboundSamlSsoProfileOperationMetadataOut",
        "ListMembershipsResponseIn": "_cloudidentity_98_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_cloudidentity_99_ListMembershipsResponseOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn": "_cloudidentity_100_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut": "_cloudidentity_101_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut",
        "GroupRelationIn": "_cloudidentity_102_GroupRelationIn",
        "GroupRelationOut": "_cloudidentity_103_GroupRelationOut",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn": "_cloudidentity_104_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut": "_cloudidentity_105_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut",
        "UpdateGroupMetadataIn": "_cloudidentity_106_UpdateGroupMetadataIn",
        "UpdateGroupMetadataOut": "_cloudidentity_107_UpdateGroupMetadataOut",
        "MembershipIn": "_cloudidentity_108_MembershipIn",
        "MembershipOut": "_cloudidentity_109_MembershipOut",
        "SecuritySettingsIn": "_cloudidentity_110_SecuritySettingsIn",
        "SecuritySettingsOut": "_cloudidentity_111_SecuritySettingsOut",
        "UpdateMembershipMetadataIn": "_cloudidentity_112_UpdateMembershipMetadataIn",
        "UpdateMembershipMetadataOut": "_cloudidentity_113_UpdateMembershipMetadataOut",
        "SamlSpConfigIn": "_cloudidentity_114_SamlSpConfigIn",
        "SamlSpConfigOut": "_cloudidentity_115_SamlSpConfigOut",
        "ListGroupsResponseIn": "_cloudidentity_116_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_cloudidentity_117_ListGroupsResponseOut",
        "InboundSsoAssignmentIn": "_cloudidentity_118_InboundSsoAssignmentIn",
        "InboundSsoAssignmentOut": "_cloudidentity_119_InboundSsoAssignmentOut",
        "CreateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_120_CreateInboundSsoAssignmentOperationMetadataIn",
        "CreateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_121_CreateInboundSsoAssignmentOperationMetadataOut",
        "MembershipAdjacencyListIn": "_cloudidentity_122_MembershipAdjacencyListIn",
        "MembershipAdjacencyListOut": "_cloudidentity_123_MembershipAdjacencyListOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn": "_cloudidentity_124_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut": "_cloudidentity_125_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn": "_cloudidentity_126_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut": "_cloudidentity_127_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn": "_cloudidentity_128_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut": "_cloudidentity_129_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut",
        "UserInvitationIn": "_cloudidentity_130_UserInvitationIn",
        "UserInvitationOut": "_cloudidentity_131_UserInvitationOut",
        "RsaPublicKeyInfoIn": "_cloudidentity_132_RsaPublicKeyInfoIn",
        "RsaPublicKeyInfoOut": "_cloudidentity_133_RsaPublicKeyInfoOut",
        "LookupGroupNameResponseIn": "_cloudidentity_134_LookupGroupNameResponseIn",
        "LookupGroupNameResponseOut": "_cloudidentity_135_LookupGroupNameResponseOut",
        "GroupIn": "_cloudidentity_136_GroupIn",
        "GroupOut": "_cloudidentity_137_GroupOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn": "_cloudidentity_138_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut": "_cloudidentity_139_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut",
        "SearchTransitiveGroupsResponseIn": "_cloudidentity_140_SearchTransitiveGroupsResponseIn",
        "SearchTransitiveGroupsResponseOut": "_cloudidentity_141_SearchTransitiveGroupsResponseOut",
        "CreateMembershipMetadataIn": "_cloudidentity_142_CreateMembershipMetadataIn",
        "CreateMembershipMetadataOut": "_cloudidentity_143_CreateMembershipMetadataOut",
        "SignInBehaviorIn": "_cloudidentity_144_SignInBehaviorIn",
        "SignInBehaviorOut": "_cloudidentity_145_SignInBehaviorOut",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn": "_cloudidentity_146_GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut": "_cloudidentity_147_GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut",
        "LookupMembershipNameResponseIn": "_cloudidentity_148_LookupMembershipNameResponseIn",
        "LookupMembershipNameResponseOut": "_cloudidentity_149_LookupMembershipNameResponseOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn": "_cloudidentity_150_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut": "_cloudidentity_151_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut",
        "DeleteGroupMetadataIn": "_cloudidentity_152_DeleteGroupMetadataIn",
        "DeleteGroupMetadataOut": "_cloudidentity_153_DeleteGroupMetadataOut",
        "CreateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_154_CreateInboundSamlSsoProfileOperationMetadataIn",
        "CreateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_155_CreateInboundSamlSsoProfileOperationMetadataOut",
        "UpdateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_156_UpdateInboundSamlSsoProfileOperationMetadataIn",
        "UpdateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_157_UpdateInboundSamlSsoProfileOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn": "_cloudidentity_158_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut": "_cloudidentity_159_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut",
        "ListIdpCredentialsResponseIn": "_cloudidentity_160_ListIdpCredentialsResponseIn",
        "ListIdpCredentialsResponseOut": "_cloudidentity_161_ListIdpCredentialsResponseOut",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesIn": "_cloudidentity_162_GoogleAppsCloudidentityDevicesV1AndroidAttributesIn",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesOut": "_cloudidentity_163_GoogleAppsCloudidentityDevicesV1AndroidAttributesOut",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn": "_cloudidentity_164_GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut": "_cloudidentity_165_GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut",
        "SearchDirectGroupsResponseIn": "_cloudidentity_166_SearchDirectGroupsResponseIn",
        "SearchDirectGroupsResponseOut": "_cloudidentity_167_SearchDirectGroupsResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn": "_cloudidentity_168_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut": "_cloudidentity_169_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut",
        "DynamicGroupStatusIn": "_cloudidentity_170_DynamicGroupStatusIn",
        "DynamicGroupStatusOut": "_cloudidentity_171_DynamicGroupStatusOut",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn": "_cloudidentity_172_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut": "_cloudidentity_173_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut",
        "AddIdpCredentialOperationMetadataIn": "_cloudidentity_174_AddIdpCredentialOperationMetadataIn",
        "AddIdpCredentialOperationMetadataOut": "_cloudidentity_175_AddIdpCredentialOperationMetadataOut",
        "UpdateMembershipRolesParamsIn": "_cloudidentity_176_UpdateMembershipRolesParamsIn",
        "UpdateMembershipRolesParamsOut": "_cloudidentity_177_UpdateMembershipRolesParamsOut",
        "DeleteInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_178_DeleteInboundSsoAssignmentOperationMetadataIn",
        "DeleteInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_179_DeleteInboundSsoAssignmentOperationMetadataOut",
        "CancelUserInvitationRequestIn": "_cloudidentity_180_CancelUserInvitationRequestIn",
        "CancelUserInvitationRequestOut": "_cloudidentity_181_CancelUserInvitationRequestOut",
        "UpdateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_182_UpdateInboundSsoAssignmentOperationMetadataIn",
        "UpdateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_183_UpdateInboundSsoAssignmentOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn": "_cloudidentity_184_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut": "_cloudidentity_185_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut",
        "ListInboundSsoAssignmentsResponseIn": "_cloudidentity_186_ListInboundSsoAssignmentsResponseIn",
        "ListInboundSsoAssignmentsResponseOut": "_cloudidentity_187_ListInboundSsoAssignmentsResponseOut",
        "GetMembershipGraphMetadataIn": "_cloudidentity_188_GetMembershipGraphMetadataIn",
        "GetMembershipGraphMetadataOut": "_cloudidentity_189_GetMembershipGraphMetadataOut",
        "StatusIn": "_cloudidentity_190_StatusIn",
        "StatusOut": "_cloudidentity_191_StatusOut",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn": "_cloudidentity_192_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut": "_cloudidentity_193_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut",
        "InboundSamlSsoProfileIn": "_cloudidentity_194_InboundSamlSsoProfileIn",
        "InboundSamlSsoProfileOut": "_cloudidentity_195_InboundSamlSsoProfileOut",
        "MembershipRoleRestrictionEvaluationIn": "_cloudidentity_196_MembershipRoleRestrictionEvaluationIn",
        "MembershipRoleRestrictionEvaluationOut": "_cloudidentity_197_MembershipRoleRestrictionEvaluationOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn": "_cloudidentity_198_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut": "_cloudidentity_199_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut",
        "DynamicGroupMetadataIn": "_cloudidentity_200_DynamicGroupMetadataIn",
        "DynamicGroupMetadataOut": "_cloudidentity_201_DynamicGroupMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"])
    types["MemberRelationIn"] = t.struct(
        {
            "member": t.string().optional(),
            "relationType": t.string().optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyIn"])).optional(),
        }
    ).named(renames["MemberRelationIn"])
    types["MemberRelationOut"] = t.struct(
        {
            "member": t.string().optional(),
            "relationType": t.string().optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberRelationOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"])
    types["GetMembershipGraphResponseIn"] = t.struct(
        {
            "adjacencyList": t.array(
                t.proxy(renames["MembershipAdjacencyListIn"])
            ).optional(),
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["GetMembershipGraphResponseIn"])
    types["GetMembershipGraphResponseOut"] = t.struct(
        {
            "adjacencyList": t.array(
                t.proxy(renames["MembershipAdjacencyListOut"])
            ).optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetMembershipGraphResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn"] = t.struct(
        {
            "deviceUsers": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut"] = t.struct(
        {
            "deviceUsers": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut"])
    types["AddIdpCredentialRequestIn"] = t.struct(
        {"pemData": t.string().optional()}
    ).named(renames["AddIdpCredentialRequestIn"])
    types["AddIdpCredentialRequestOut"] = t.struct(
        {
            "pemData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddIdpCredentialRequestOut"])
    types["ModifyMembershipRolesRequestIn"] = t.struct(
        {
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsIn"])
            ).optional(),
            "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "removeRoles": t.array(t.string()).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestIn"])
    types["ModifyMembershipRolesRequestOut"] = t.struct(
        {
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsOut"])
            ).optional(),
            "addRoles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "removeRoles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestOut"])
    types["TransitiveMembershipRoleIn"] = t.struct(
        {"role": t.string().optional()}
    ).named(renames["TransitiveMembershipRoleIn"])
    types["TransitiveMembershipRoleOut"] = t.struct(
        {
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitiveMembershipRoleOut"])
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
    types["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "customer": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"])
    types[
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"
    ] = t.struct(
        {
            "names": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"]
    )
    types["ListInboundSamlSsoProfilesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inboundSamlSsoProfiles": t.array(
                t.proxy(renames["InboundSamlSsoProfileIn"])
            ).optional(),
        }
    ).named(renames["ListInboundSamlSsoProfilesResponseIn"])
    types["ListInboundSamlSsoProfilesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "inboundSamlSsoProfiles": t.array(
                t.proxy(renames["InboundSamlSsoProfileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInboundSamlSsoProfilesResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "userEmail": t.string().optional(),
            "compromisedState": t.string().optional(),
            "passwordState": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "languageCode": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "managementState": t.string().optional(),
            "userEmail": t.string().optional(),
            "userAgent": t.string().optional(),
            "name": t.string().optional(),
            "compromisedState": t.string().optional(),
            "firstSyncTime": t.string().optional(),
            "passwordState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
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
    types["MembershipRelationIn"] = t.struct(
        {
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "group": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "displayName": t.string().optional(),
            "membership": t.string().optional(),
        }
    ).named(renames["MembershipRelationIn"])
    types["MembershipRelationOut"] = t.struct(
        {
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "group": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "displayName": t.string().optional(),
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRelationOut"])
    types["IdpCredentialIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdpCredentialIn"]
    )
    types["IdpCredentialOut"] = t.struct(
        {
            "dsaKeyInfo": t.proxy(renames["DsaPublicKeyInfoOut"]).optional(),
            "rsaKeyInfo": t.proxy(renames["RsaPublicKeyInfoOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpCredentialOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"])
    types["CheckTransitiveMembershipResponseIn"] = t.struct(
        {"hasMembership": t.boolean().optional()}
    ).named(renames["CheckTransitiveMembershipResponseIn"])
    types["CheckTransitiveMembershipResponseOut"] = t.struct(
        {
            "hasMembership": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckTransitiveMembershipResponseOut"])
    types["SamlIdpConfigIn"] = t.struct(
        {
            "singleSignOnServiceUri": t.string(),
            "changePasswordUri": t.string().optional(),
            "logoutRedirectUri": t.string().optional(),
            "entityId": t.string(),
        }
    ).named(renames["SamlIdpConfigIn"])
    types["SamlIdpConfigOut"] = t.struct(
        {
            "singleSignOnServiceUri": t.string(),
            "changePasswordUri": t.string().optional(),
            "logoutRedirectUri": t.string().optional(),
            "entityId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlIdpConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ModifyMembershipRolesResponseIn"] = t.struct(
        {"membership": t.proxy(renames["MembershipIn"]).optional()}
    ).named(renames["ModifyMembershipRolesResponseIn"])
    types["ModifyMembershipRolesResponseOut"] = t.struct(
        {
            "membership": t.proxy(renames["MembershipOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesResponseOut"])
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
    types["DynamicGroupQueryIn"] = t.struct(
        {"resourceType": t.string().optional(), "query": t.string().optional()}
    ).named(renames["DynamicGroupQueryIn"])
    types["DynamicGroupQueryOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupQueryOut"])
    types["MemberRestrictionIn"] = t.struct(
        {
            "evaluation": t.proxy(renames["RestrictionEvaluationIn"]).optional(),
            "query": t.string().optional(),
        }
    ).named(renames["MemberRestrictionIn"])
    types["MemberRestrictionOut"] = t.struct(
        {
            "evaluation": t.proxy(renames["RestrictionEvaluationOut"]).optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberRestrictionOut"])
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
    types["RestrictionEvaluationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestrictionEvaluationIn"]
    )
    types["RestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionEvaluationOut"])
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
    types["IsInvitableUserResponseIn"] = t.struct(
        {"isInvitableUser": t.boolean().optional()}
    ).named(renames["IsInvitableUserResponseIn"])
    types["IsInvitableUserResponseOut"] = t.struct(
        {
            "isInvitableUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IsInvitableUserResponseOut"])
    types["CreateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateGroupMetadataIn"]
    )
    types["CreateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateGroupMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"])
    types["DeleteIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataIn"])
    types["DeleteIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataOut"])
    types["SearchGroupsResponseIn"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchGroupsResponseIn"])
    types["SearchGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchGroupsResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"])
    types["EntityKeyIn"] = t.struct(
        {"namespace": t.string().optional(), "id": t.string().optional()}
    ).named(renames["EntityKeyIn"])
    types["EntityKeyOut"] = t.struct(
        {
            "namespace": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityKeyOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeviceIn"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "deviceId": t.string().optional(),
            "assetTag": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "serialNumber": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceOut"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "androidSpecificAttributes": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"]
            ).optional(),
            "enabledDeveloperOptions": t.boolean().optional(),
            "createTime": t.string().optional(),
            "model": t.string().optional(),
            "enabledUsbDebugging": t.boolean().optional(),
            "name": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "releaseVersion": t.string().optional(),
            "deviceId": t.string().optional(),
            "buildNumber": t.string().optional(),
            "osVersion": t.string().optional(),
            "assetTag": t.string().optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "encryptionState": t.string().optional(),
            "manufacturer": t.string().optional(),
            "deviceType": t.string().optional(),
            "brand": t.string().optional(),
            "networkOperator": t.string().optional(),
            "otherAccounts": t.array(t.string()).optional(),
            "bootloaderVersion": t.string().optional(),
            "managementState": t.string().optional(),
            "compromisedState": t.string().optional(),
            "basebandVersion": t.string().optional(),
            "securityPatchTime": t.string().optional(),
            "ownerType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
    types["SendUserInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendUserInvitationRequestIn"]
    )
    types["SendUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendUserInvitationRequestOut"])
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
    types["GoogleAppsCloudidentityDevicesV1ClientStateIn"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "customId": t.string().optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "assetTags": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "healthScore": t.string().optional(),
            "scoreReason": t.string().optional(),
            "managed": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateOut"] = t.struct(
        {
            "complianceState": t.string().optional(),
            "customId": t.string().optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "assetTags": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "healthScore": t.string().optional(),
            "scoreReason": t.string().optional(),
            "ownerType": t.string().optional(),
            "createTime": t.string().optional(),
            "managed": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
    types["MembershipRoleIn"] = t.struct(
        {
            "restrictionEvaluations": t.proxy(
                renames["RestrictionEvaluationsIn"]
            ).optional(),
            "expiryDetail": t.proxy(renames["ExpiryDetailIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MembershipRoleIn"])
    types["MembershipRoleOut"] = t.struct(
        {
            "restrictionEvaluations": t.proxy(
                renames["RestrictionEvaluationsOut"]
            ).optional(),
            "expiryDetail": t.proxy(renames["ExpiryDetailOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleOut"])
    types["SamlSsoInfoIn"] = t.struct({"inboundSamlSsoProfile": t.string()}).named(
        renames["SamlSsoInfoIn"]
    )
    types["SamlSsoInfoOut"] = t.struct(
        {
            "inboundSamlSsoProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSsoInfoOut"])
    types["ExpiryDetailIn"] = t.struct({"expireTime": t.string().optional()}).named(
        renames["ExpiryDetailIn"]
    )
    types["ExpiryDetailOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpiryDetailOut"])
    types["DsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["DsaPublicKeyInfoIn"]
    )
    types["DsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsaPublicKeyInfoOut"])
    types["DeleteMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMembershipMetadataIn"]
    )
    types["DeleteMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMembershipMetadataOut"])
    types["DeleteInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataIn"])
    types["DeleteInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"])
    types["GroupRelationIn"] = t.struct(
        {
            "relationType": t.string().optional(),
            "displayName": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GroupRelationIn"])
    types["GroupRelationOut"] = t.struct(
        {
            "relationType": t.string().optional(),
            "displayName": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupRelationOut"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"])
    types["UpdateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateGroupMetadataIn"]
    )
    types["UpdateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateGroupMetadataOut"])
    types["MembershipIn"] = t.struct(
        {
            "preferredMemberKey": t.proxy(renames["EntityKeyIn"]),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyOut"]),
            "deliverySetting": t.string().optional(),
            "name": t.string().optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["SecuritySettingsIn"] = t.struct(
        {"memberRestriction": t.proxy(renames["MemberRestrictionIn"]).optional()}
    ).named(renames["SecuritySettingsIn"])
    types["SecuritySettingsOut"] = t.struct(
        {
            "memberRestriction": t.proxy(renames["MemberRestrictionOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecuritySettingsOut"])
    types["UpdateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateMembershipMetadataIn"]
    )
    types["UpdateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateMembershipMetadataOut"])
    types["SamlSpConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SamlSpConfigIn"]
    )
    types["SamlSpConfigOut"] = t.struct(
        {
            "entityId": t.string().optional(),
            "assertionConsumerServiceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSpConfigOut"])
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
    types["InboundSsoAssignmentIn"] = t.struct(
        {
            "rank": t.integer().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
            "targetGroup": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "ssoMode": t.string().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
        }
    ).named(renames["InboundSsoAssignmentIn"])
    types["InboundSsoAssignmentOut"] = t.struct(
        {
            "rank": t.integer().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorOut"]).optional(),
            "name": t.string().optional(),
            "targetGroup": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "ssoMode": t.string().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSsoAssignmentOut"])
    types["CreateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataIn"])
    types["CreateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"])
    types["UserInvitationIn"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["UserInvitationIn"])
    types["UserInvitationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInvitationOut"])
    types["RsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["RsaPublicKeyInfoIn"]
    )
    types["RsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaPublicKeyInfoOut"])
    types["LookupGroupNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupGroupNameResponseIn"])
    types["LookupGroupNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupGroupNameResponseOut"])
    types["GroupIn"] = t.struct(
        {
            "groupKey": t.proxy(renames["EntityKeyIn"]),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataIn"]
            ).optional(),
            "parent": t.string(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "description": t.string().optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataOut"]
            ).optional(),
            "parent": t.string(),
            "additionalGroupKeys": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["SearchTransitiveGroupsResponseIn"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["GroupRelationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchTransitiveGroupsResponseIn"])
    types["SearchTransitiveGroupsResponseOut"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["GroupRelationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTransitiveGroupsResponseOut"])
    types["CreateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateMembershipMetadataIn"]
    )
    types["CreateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateMembershipMetadataOut"])
    types["SignInBehaviorIn"] = t.struct(
        {"redirectCondition": t.string().optional()}
    ).named(renames["SignInBehaviorIn"])
    types["SignInBehaviorOut"] = t.struct(
        {
            "redirectCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignInBehaviorOut"])
    types["GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"])
    types["LookupMembershipNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupMembershipNameResponseIn"])
    types["LookupMembershipNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupMembershipNameResponseOut"])
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
    types["DeleteGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteGroupMetadataIn"]
    )
    types["DeleteGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteGroupMetadataOut"])
    types["CreateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataIn"])
    types["CreateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataOut"])
    types["UpdateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataIn"])
    types["UpdateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"] = t.struct(
        {
            "ownershipPrivilege": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "verifiedBoot": t.boolean().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ctsProfileMatch": t.boolean().optional(),
            "supportsWorkProfile": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
            "hasPotentiallyHarmfulApps": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"] = t.struct(
        {
            "ownershipPrivilege": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "verifiedBoot": t.boolean().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ctsProfileMatch": t.boolean().optional(),
            "supportsWorkProfile": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
            "hasPotentiallyHarmfulApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"])
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"])
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "numberValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"])
    types["SearchDirectGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipRelationIn"])).optional(),
        }
    ).named(renames["SearchDirectGroupsResponseIn"])
    types["SearchDirectGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(
                t.proxy(renames["MembershipRelationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDirectGroupsResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"])
    types["AddIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AddIdpCredentialOperationMetadataIn"])
    types["AddIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddIdpCredentialOperationMetadataOut"])
    types["UpdateMembershipRolesParamsIn"] = t.struct(
        {
            "fieldMask": t.string().optional(),
            "membershipRole": t.proxy(renames["MembershipRoleIn"]).optional(),
        }
    ).named(renames["UpdateMembershipRolesParamsIn"])
    types["UpdateMembershipRolesParamsOut"] = t.struct(
        {
            "fieldMask": t.string().optional(),
            "membershipRole": t.proxy(renames["MembershipRoleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMembershipRolesParamsOut"])
    types["DeleteInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataIn"])
    types["DeleteInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataOut"])
    types["CancelUserInvitationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelUserInvitationRequestIn"])
    types["CancelUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelUserInvitationRequestOut"])
    types["UpdateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataIn"])
    types["UpdateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"])
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
    types["GetMembershipGraphMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMembershipGraphMetadataIn"])
    types["GetMembershipGraphMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetMembershipGraphMetadataOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"])
    types["InboundSamlSsoProfileIn"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "customer": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileIn"])
    types["InboundSamlSsoProfileOut"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigOut"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "customer": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileOut"])
    types["MembershipRoleRestrictionEvaluationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipRoleRestrictionEvaluationIn"])
    types["MembershipRoleRestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleRestrictionEvaluationOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn"] = t.struct(
        {"removeResetLock": t.boolean().optional(), "customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut"] = t.struct(
        {
            "removeResetLock": t.boolean().optional(),
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut"])
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

    functions = {}
    functions["groupsUpdateSecuritySettings"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsSearch"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsCreate"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGetSecuritySettings"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsPatch"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGet"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsLookup"] = cloudidentity.get(
        "v1/groups:lookup",
        t.struct(
            {
                "groupKey.id": t.string().optional(),
                "groupKey.namespace": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupGroupNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCreate"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsLookup"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchDirectGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGet"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsDelete"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsList"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGetMembershipGraph"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveMemberships"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsModifyMembershipRoles"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCheckTransitiveMembership"] = cloudidentity.get(
        "v1/{parent}/memberships:checkTransitiveMembership",
        t.struct(
            {
                "query": t.string(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckTransitiveMembershipResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesList"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSamlSsoProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesCreate"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSamlSsoProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesPatch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSamlSsoProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesDelete"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSamlSsoProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSamlSsoProfileOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsGet"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsAdd"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsList"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsDelete"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesWipe"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGet"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCancelWipe"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCreate"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDelete"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesList"] = cloudidentity.get(
        "v1/devices",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "view": t.string().optional(),
                "customer": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersWipe"] = cloudidentity.post(
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
    functions["devicesDeviceUsersList"] = cloudidentity.post(
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
        "v1/{name}:cancelWipe",
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
    functions["devicesDeviceUsersClientStatesGet"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "customer": t.string().optional(),
                "complianceState": t.string().optional(),
                "customId": t.string().optional(),
                "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
                "assetTags": t.array(t.string()).optional(),
                "etag": t.string().optional(),
                "healthScore": t.string().optional(),
                "scoreReason": t.string().optional(),
                "managed": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesList"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "customer": t.string().optional(),
                "complianceState": t.string().optional(),
                "customId": t.string().optional(),
                "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
                "assetTags": t.array(t.string()).optional(),
                "etag": t.string().optional(),
                "healthScore": t.string().optional(),
                "scoreReason": t.string().optional(),
                "managed": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesPatch"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "customer": t.string().optional(),
                "complianceState": t.string().optional(),
                "customId": t.string().optional(),
                "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
                "assetTags": t.array(t.string()).optional(),
                "etag": t.string().optional(),
                "healthScore": t.string().optional(),
                "scoreReason": t.string().optional(),
                "managed": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsList"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSsoAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsDelete"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSsoAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsPatch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSsoAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsCreate"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSsoAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["InboundSsoAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsIsInvitableUser"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsCancel"] = cloudidentity.get(
        "v1/{parent}/userinvitations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListUserInvitationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudidentity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
