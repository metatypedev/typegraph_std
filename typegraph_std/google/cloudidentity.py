from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudidentity() -> Import:
    cloudidentity = HTTPRuntime("https://cloudidentity.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudidentity_1_ErrorResponse",
        "MembershipAdjacencyListIn": "_cloudidentity_2_MembershipAdjacencyListIn",
        "MembershipAdjacencyListOut": "_cloudidentity_3_MembershipAdjacencyListOut",
        "DeleteGroupMetadataIn": "_cloudidentity_4_DeleteGroupMetadataIn",
        "DeleteGroupMetadataOut": "_cloudidentity_5_DeleteGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn": "_cloudidentity_6_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut": "_cloudidentity_7_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn": "_cloudidentity_8_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut": "_cloudidentity_9_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut",
        "ModifyMembershipRolesRequestIn": "_cloudidentity_10_ModifyMembershipRolesRequestIn",
        "ModifyMembershipRolesRequestOut": "_cloudidentity_11_ModifyMembershipRolesRequestOut",
        "SamlSpConfigIn": "_cloudidentity_12_SamlSpConfigIn",
        "SamlSpConfigOut": "_cloudidentity_13_SamlSpConfigOut",
        "SearchTransitiveMembershipsResponseIn": "_cloudidentity_14_SearchTransitiveMembershipsResponseIn",
        "SearchTransitiveMembershipsResponseOut": "_cloudidentity_15_SearchTransitiveMembershipsResponseOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn": "_cloudidentity_16_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut": "_cloudidentity_17_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut",
        "IdpCredentialIn": "_cloudidentity_18_IdpCredentialIn",
        "IdpCredentialOut": "_cloudidentity_19_IdpCredentialOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn": "_cloudidentity_20_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut": "_cloudidentity_21_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut",
        "UpdateMembershipRolesParamsIn": "_cloudidentity_22_UpdateMembershipRolesParamsIn",
        "UpdateMembershipRolesParamsOut": "_cloudidentity_23_UpdateMembershipRolesParamsOut",
        "UpdateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_24_UpdateInboundSsoAssignmentOperationMetadataIn",
        "UpdateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_25_UpdateInboundSsoAssignmentOperationMetadataOut",
        "AddIdpCredentialOperationMetadataIn": "_cloudidentity_26_AddIdpCredentialOperationMetadataIn",
        "AddIdpCredentialOperationMetadataOut": "_cloudidentity_27_AddIdpCredentialOperationMetadataOut",
        "InboundSsoAssignmentIn": "_cloudidentity_28_InboundSsoAssignmentIn",
        "InboundSsoAssignmentOut": "_cloudidentity_29_InboundSsoAssignmentOut",
        "MembershipRoleRestrictionEvaluationIn": "_cloudidentity_30_MembershipRoleRestrictionEvaluationIn",
        "MembershipRoleRestrictionEvaluationOut": "_cloudidentity_31_MembershipRoleRestrictionEvaluationOut",
        "ModifyMembershipRolesResponseIn": "_cloudidentity_32_ModifyMembershipRolesResponseIn",
        "ModifyMembershipRolesResponseOut": "_cloudidentity_33_ModifyMembershipRolesResponseOut",
        "CreateGroupMetadataIn": "_cloudidentity_34_CreateGroupMetadataIn",
        "CreateGroupMetadataOut": "_cloudidentity_35_CreateGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn": "_cloudidentity_36_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut": "_cloudidentity_37_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut",
        "LookupGroupNameResponseIn": "_cloudidentity_38_LookupGroupNameResponseIn",
        "LookupGroupNameResponseOut": "_cloudidentity_39_LookupGroupNameResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn": "_cloudidentity_40_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut": "_cloudidentity_41_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn": "_cloudidentity_42_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut": "_cloudidentity_43_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn": "_cloudidentity_44_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut": "_cloudidentity_45_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn": "_cloudidentity_46_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut": "_cloudidentity_47_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn": "_cloudidentity_48_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut": "_cloudidentity_49_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut",
        "MembershipIn": "_cloudidentity_50_MembershipIn",
        "MembershipOut": "_cloudidentity_51_MembershipOut",
        "MemberRestrictionIn": "_cloudidentity_52_MemberRestrictionIn",
        "MemberRestrictionOut": "_cloudidentity_53_MemberRestrictionOut",
        "GoogleAppsCloudidentityDevicesV1DeviceIn": "_cloudidentity_54_GoogleAppsCloudidentityDevicesV1DeviceIn",
        "GoogleAppsCloudidentityDevicesV1DeviceOut": "_cloudidentity_55_GoogleAppsCloudidentityDevicesV1DeviceOut",
        "RestrictionEvaluationsIn": "_cloudidentity_56_RestrictionEvaluationsIn",
        "RestrictionEvaluationsOut": "_cloudidentity_57_RestrictionEvaluationsOut",
        "ListMembershipsResponseIn": "_cloudidentity_58_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_cloudidentity_59_ListMembershipsResponseOut",
        "RestrictionEvaluationIn": "_cloudidentity_60_RestrictionEvaluationIn",
        "RestrictionEvaluationOut": "_cloudidentity_61_RestrictionEvaluationOut",
        "TransitiveMembershipRoleIn": "_cloudidentity_62_TransitiveMembershipRoleIn",
        "TransitiveMembershipRoleOut": "_cloudidentity_63_TransitiveMembershipRoleOut",
        "InboundSamlSsoProfileIn": "_cloudidentity_64_InboundSamlSsoProfileIn",
        "InboundSamlSsoProfileOut": "_cloudidentity_65_InboundSamlSsoProfileOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn": "_cloudidentity_66_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut": "_cloudidentity_67_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn": "_cloudidentity_68_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut": "_cloudidentity_69_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn": "_cloudidentity_70_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut": "_cloudidentity_71_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesIn": "_cloudidentity_72_GoogleAppsCloudidentityDevicesV1AndroidAttributesIn",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesOut": "_cloudidentity_73_GoogleAppsCloudidentityDevicesV1AndroidAttributesOut",
        "GetMembershipGraphResponseIn": "_cloudidentity_74_GetMembershipGraphResponseIn",
        "GetMembershipGraphResponseOut": "_cloudidentity_75_GetMembershipGraphResponseOut",
        "DsaPublicKeyInfoIn": "_cloudidentity_76_DsaPublicKeyInfoIn",
        "DsaPublicKeyInfoOut": "_cloudidentity_77_DsaPublicKeyInfoOut",
        "DynamicGroupStatusIn": "_cloudidentity_78_DynamicGroupStatusIn",
        "DynamicGroupStatusOut": "_cloudidentity_79_DynamicGroupStatusOut",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn": "_cloudidentity_80_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut": "_cloudidentity_81_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut",
        "CreateMembershipMetadataIn": "_cloudidentity_82_CreateMembershipMetadataIn",
        "CreateMembershipMetadataOut": "_cloudidentity_83_CreateMembershipMetadataOut",
        "SamlIdpConfigIn": "_cloudidentity_84_SamlIdpConfigIn",
        "SamlIdpConfigOut": "_cloudidentity_85_SamlIdpConfigOut",
        "SamlSsoInfoIn": "_cloudidentity_86_SamlSsoInfoIn",
        "SamlSsoInfoOut": "_cloudidentity_87_SamlSsoInfoOut",
        "DynamicGroupMetadataIn": "_cloudidentity_88_DynamicGroupMetadataIn",
        "DynamicGroupMetadataOut": "_cloudidentity_89_DynamicGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn": "_cloudidentity_90_GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut": "_cloudidentity_91_GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn": "_cloudidentity_92_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut": "_cloudidentity_93_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut",
        "ListInboundSamlSsoProfilesResponseIn": "_cloudidentity_94_ListInboundSamlSsoProfilesResponseIn",
        "ListInboundSamlSsoProfilesResponseOut": "_cloudidentity_95_ListInboundSamlSsoProfilesResponseOut",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn": "_cloudidentity_96_GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut": "_cloudidentity_97_GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut",
        "LookupMembershipNameResponseIn": "_cloudidentity_98_LookupMembershipNameResponseIn",
        "LookupMembershipNameResponseOut": "_cloudidentity_99_LookupMembershipNameResponseOut",
        "EntityKeyIn": "_cloudidentity_100_EntityKeyIn",
        "EntityKeyOut": "_cloudidentity_101_EntityKeyOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn": "_cloudidentity_102_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut": "_cloudidentity_103_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn": "_cloudidentity_104_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut": "_cloudidentity_105_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut",
        "DeleteInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_106_DeleteInboundSamlSsoProfileOperationMetadataIn",
        "DeleteInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_107_DeleteInboundSamlSsoProfileOperationMetadataOut",
        "SearchTransitiveGroupsResponseIn": "_cloudidentity_108_SearchTransitiveGroupsResponseIn",
        "SearchTransitiveGroupsResponseOut": "_cloudidentity_109_SearchTransitiveGroupsResponseOut",
        "UpdateGroupMetadataIn": "_cloudidentity_110_UpdateGroupMetadataIn",
        "UpdateGroupMetadataOut": "_cloudidentity_111_UpdateGroupMetadataOut",
        "MemberRelationIn": "_cloudidentity_112_MemberRelationIn",
        "MemberRelationOut": "_cloudidentity_113_MemberRelationOut",
        "CreateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_114_CreateInboundSamlSsoProfileOperationMetadataIn",
        "CreateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_115_CreateInboundSamlSsoProfileOperationMetadataOut",
        "RsaPublicKeyInfoIn": "_cloudidentity_116_RsaPublicKeyInfoIn",
        "RsaPublicKeyInfoOut": "_cloudidentity_117_RsaPublicKeyInfoOut",
        "SearchDirectGroupsResponseIn": "_cloudidentity_118_SearchDirectGroupsResponseIn",
        "SearchDirectGroupsResponseOut": "_cloudidentity_119_SearchDirectGroupsResponseOut",
        "UpdateMembershipMetadataIn": "_cloudidentity_120_UpdateMembershipMetadataIn",
        "UpdateMembershipMetadataOut": "_cloudidentity_121_UpdateMembershipMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn": "_cloudidentity_122_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut": "_cloudidentity_123_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn": "_cloudidentity_124_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut": "_cloudidentity_125_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut",
        "UpdateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_126_UpdateInboundSamlSsoProfileOperationMetadataIn",
        "UpdateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_127_UpdateInboundSamlSsoProfileOperationMetadataOut",
        "SearchGroupsResponseIn": "_cloudidentity_128_SearchGroupsResponseIn",
        "SearchGroupsResponseOut": "_cloudidentity_129_SearchGroupsResponseOut",
        "UserInvitationIn": "_cloudidentity_130_UserInvitationIn",
        "UserInvitationOut": "_cloudidentity_131_UserInvitationOut",
        "GetMembershipGraphMetadataIn": "_cloudidentity_132_GetMembershipGraphMetadataIn",
        "GetMembershipGraphMetadataOut": "_cloudidentity_133_GetMembershipGraphMetadataOut",
        "SignInBehaviorIn": "_cloudidentity_134_SignInBehaviorIn",
        "SignInBehaviorOut": "_cloudidentity_135_SignInBehaviorOut",
        "ListGroupsResponseIn": "_cloudidentity_136_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_cloudidentity_137_ListGroupsResponseOut",
        "ListInboundSsoAssignmentsResponseIn": "_cloudidentity_138_ListInboundSsoAssignmentsResponseIn",
        "ListInboundSsoAssignmentsResponseOut": "_cloudidentity_139_ListInboundSsoAssignmentsResponseOut",
        "GroupIn": "_cloudidentity_140_GroupIn",
        "GroupOut": "_cloudidentity_141_GroupOut",
        "DynamicGroupQueryIn": "_cloudidentity_142_DynamicGroupQueryIn",
        "DynamicGroupQueryOut": "_cloudidentity_143_DynamicGroupQueryOut",
        "MembershipRelationIn": "_cloudidentity_144_MembershipRelationIn",
        "MembershipRelationOut": "_cloudidentity_145_MembershipRelationOut",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn": "_cloudidentity_146_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut": "_cloudidentity_147_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut",
        "MembershipRoleIn": "_cloudidentity_148_MembershipRoleIn",
        "MembershipRoleOut": "_cloudidentity_149_MembershipRoleOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn": "_cloudidentity_150_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut": "_cloudidentity_151_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn": "_cloudidentity_152_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut": "_cloudidentity_153_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut",
        "DeleteInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_154_DeleteInboundSsoAssignmentOperationMetadataIn",
        "DeleteInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_155_DeleteInboundSsoAssignmentOperationMetadataOut",
        "ListUserInvitationsResponseIn": "_cloudidentity_156_ListUserInvitationsResponseIn",
        "ListUserInvitationsResponseOut": "_cloudidentity_157_ListUserInvitationsResponseOut",
        "IsInvitableUserResponseIn": "_cloudidentity_158_IsInvitableUserResponseIn",
        "IsInvitableUserResponseOut": "_cloudidentity_159_IsInvitableUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1ClientStateIn": "_cloudidentity_160_GoogleAppsCloudidentityDevicesV1ClientStateIn",
        "GoogleAppsCloudidentityDevicesV1ClientStateOut": "_cloudidentity_161_GoogleAppsCloudidentityDevicesV1ClientStateOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn": "_cloudidentity_162_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut": "_cloudidentity_163_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut",
        "AddIdpCredentialRequestIn": "_cloudidentity_164_AddIdpCredentialRequestIn",
        "AddIdpCredentialRequestOut": "_cloudidentity_165_AddIdpCredentialRequestOut",
        "DeleteMembershipMetadataIn": "_cloudidentity_166_DeleteMembershipMetadataIn",
        "DeleteMembershipMetadataOut": "_cloudidentity_167_DeleteMembershipMetadataOut",
        "GroupRelationIn": "_cloudidentity_168_GroupRelationIn",
        "GroupRelationOut": "_cloudidentity_169_GroupRelationOut",
        "StatusIn": "_cloudidentity_170_StatusIn",
        "StatusOut": "_cloudidentity_171_StatusOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn": "_cloudidentity_172_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut": "_cloudidentity_173_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut",
        "SecuritySettingsIn": "_cloudidentity_174_SecuritySettingsIn",
        "SecuritySettingsOut": "_cloudidentity_175_SecuritySettingsOut",
        "DeleteIdpCredentialOperationMetadataIn": "_cloudidentity_176_DeleteIdpCredentialOperationMetadataIn",
        "DeleteIdpCredentialOperationMetadataOut": "_cloudidentity_177_DeleteIdpCredentialOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn": "_cloudidentity_178_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut": "_cloudidentity_179_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut",
        "ListIdpCredentialsResponseIn": "_cloudidentity_180_ListIdpCredentialsResponseIn",
        "ListIdpCredentialsResponseOut": "_cloudidentity_181_ListIdpCredentialsResponseOut",
        "SendUserInvitationRequestIn": "_cloudidentity_182_SendUserInvitationRequestIn",
        "SendUserInvitationRequestOut": "_cloudidentity_183_SendUserInvitationRequestOut",
        "CancelUserInvitationRequestIn": "_cloudidentity_184_CancelUserInvitationRequestIn",
        "CancelUserInvitationRequestOut": "_cloudidentity_185_CancelUserInvitationRequestOut",
        "GoogleAppsCloudidentityDevicesV1DeviceUserIn": "_cloudidentity_186_GoogleAppsCloudidentityDevicesV1DeviceUserIn",
        "GoogleAppsCloudidentityDevicesV1DeviceUserOut": "_cloudidentity_187_GoogleAppsCloudidentityDevicesV1DeviceUserOut",
        "CheckTransitiveMembershipResponseIn": "_cloudidentity_188_CheckTransitiveMembershipResponseIn",
        "CheckTransitiveMembershipResponseOut": "_cloudidentity_189_CheckTransitiveMembershipResponseOut",
        "CreateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_190_CreateInboundSsoAssignmentOperationMetadataIn",
        "CreateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_191_CreateInboundSsoAssignmentOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn": "_cloudidentity_192_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut": "_cloudidentity_193_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn": "_cloudidentity_194_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut": "_cloudidentity_195_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut",
        "ExpiryDetailIn": "_cloudidentity_196_ExpiryDetailIn",
        "ExpiryDetailOut": "_cloudidentity_197_ExpiryDetailOut",
        "OperationIn": "_cloudidentity_198_OperationIn",
        "OperationOut": "_cloudidentity_199_OperationOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn": "_cloudidentity_200_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut": "_cloudidentity_201_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DeleteGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteGroupMetadataIn"]
    )
    types["DeleteGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteGroupMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"])
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
    types["SearchTransitiveMembershipsResponseIn"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MemberRelationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchTransitiveMembershipsResponseIn"])
    types["SearchTransitiveMembershipsResponseOut"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MemberRelationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTransitiveMembershipsResponseOut"])
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
    types["IdpCredentialIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdpCredentialIn"]
    )
    types["IdpCredentialOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "rsaKeyInfo": t.proxy(renames["RsaPublicKeyInfoOut"]).optional(),
            "dsaKeyInfo": t.proxy(renames["DsaPublicKeyInfoOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpCredentialOut"])
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
    types["UpdateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataIn"])
    types["UpdateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataOut"])
    types["AddIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AddIdpCredentialOperationMetadataIn"])
    types["AddIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddIdpCredentialOperationMetadataOut"])
    types["InboundSsoAssignmentIn"] = t.struct(
        {
            "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
            "ssoMode": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "rank": t.integer().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
            "targetGroup": t.string().optional(),
        }
    ).named(renames["InboundSsoAssignmentIn"])
    types["InboundSsoAssignmentOut"] = t.struct(
        {
            "signInBehavior": t.proxy(renames["SignInBehaviorOut"]).optional(),
            "ssoMode": t.string().optional(),
            "customer": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "rank": t.integer().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoOut"]).optional(),
            "name": t.string().optional(),
            "targetGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSsoAssignmentOut"])
    types["MembershipRoleRestrictionEvaluationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipRoleRestrictionEvaluationIn"])
    types["MembershipRoleRestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleRestrictionEvaluationOut"])
    types["ModifyMembershipRolesResponseIn"] = t.struct(
        {"membership": t.proxy(renames["MembershipIn"]).optional()}
    ).named(renames["ModifyMembershipRolesResponseIn"])
    types["ModifyMembershipRolesResponseOut"] = t.struct(
        {
            "membership": t.proxy(renames["MembershipOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesResponseOut"])
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
    types["LookupGroupNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupGroupNameResponseIn"])
    types["LookupGroupNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupGroupNameResponseOut"])
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
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"])
    types["MembershipIn"] = t.struct(
        {
            "preferredMemberKey": t.proxy(renames["EntityKeyIn"]),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "deliverySetting": t.string().optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyOut"]),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeviceIn"] = t.struct(
        {
            "wifiMacAddresses": t.array(t.string()).optional(),
            "lastSyncTime": t.string().optional(),
            "assetTag": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceId": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceOut"] = t.struct(
        {
            "model": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "manufacturer": t.string().optional(),
            "releaseVersion": t.string().optional(),
            "compromisedState": t.string().optional(),
            "createTime": t.string().optional(),
            "buildNumber": t.string().optional(),
            "ownerType": t.string().optional(),
            "brand": t.string().optional(),
            "imei": t.string().optional(),
            "otherAccounts": t.array(t.string()).optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "enabledDeveloperOptions": t.boolean().optional(),
            "enabledUsbDebugging": t.boolean().optional(),
            "lastSyncTime": t.string().optional(),
            "networkOperator": t.string().optional(),
            "basebandVersion": t.string().optional(),
            "managementState": t.string().optional(),
            "encryptionState": t.string().optional(),
            "securityPatchTime": t.string().optional(),
            "androidSpecificAttributes": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"]
            ).optional(),
            "deviceType": t.string().optional(),
            "meid": t.string().optional(),
            "assetTag": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
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
    types["RestrictionEvaluationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestrictionEvaluationIn"]
    )
    types["RestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionEvaluationOut"])
    types["TransitiveMembershipRoleIn"] = t.struct(
        {"role": t.string().optional()}
    ).named(renames["TransitiveMembershipRoleIn"])
    types["TransitiveMembershipRoleOut"] = t.struct(
        {
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitiveMembershipRoleOut"])
    types["InboundSamlSsoProfileIn"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
            "customer": t.string().optional(),
        }
    ).named(renames["InboundSamlSsoProfileIn"])
    types["InboundSamlSsoProfileOut"] = t.struct(
        {
            "spConfig": t.proxy(renames["SamlSpConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigOut"]).optional(),
            "customer": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"] = t.struct(
        {
            "ownerProfileAccount": t.boolean().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
            "supportsWorkProfile": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"] = t.struct(
        {
            "ownerProfileAccount": t.boolean().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
            "supportsWorkProfile": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"])
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
    types["DsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["DsaPublicKeyInfoIn"]
    )
    types["DsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsaPublicKeyInfoOut"])
    types["DynamicGroupStatusIn"] = t.struct(
        {"status": t.string().optional(), "statusTime": t.string().optional()}
    ).named(renames["DynamicGroupStatusIn"])
    types["DynamicGroupStatusOut"] = t.struct(
        {
            "status": t.string().optional(),
            "statusTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupStatusOut"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"])
    types["CreateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateMembershipMetadataIn"]
    )
    types["CreateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateMembershipMetadataOut"])
    types["SamlIdpConfigIn"] = t.struct(
        {
            "singleSignOnServiceUri": t.string(),
            "logoutRedirectUri": t.string().optional(),
            "changePasswordUri": t.string().optional(),
            "entityId": t.string(),
        }
    ).named(renames["SamlIdpConfigIn"])
    types["SamlIdpConfigOut"] = t.struct(
        {
            "singleSignOnServiceUri": t.string(),
            "logoutRedirectUri": t.string().optional(),
            "changePasswordUri": t.string().optional(),
            "entityId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlIdpConfigOut"])
    types["SamlSsoInfoIn"] = t.struct({"inboundSamlSsoProfile": t.string()}).named(
        renames["SamlSsoInfoIn"]
    )
    types["SamlSsoInfoOut"] = t.struct(
        {
            "inboundSamlSsoProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSsoInfoOut"])
    types["DynamicGroupMetadataIn"] = t.struct(
        {"queries": t.array(t.proxy(renames["DynamicGroupQueryIn"])).optional()}
    ).named(renames["DynamicGroupMetadataIn"])
    types["DynamicGroupMetadataOut"] = t.struct(
        {
            "queries": t.array(t.proxy(renames["DynamicGroupQueryOut"])).optional(),
            "status": t.proxy(renames["DynamicGroupStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicGroupMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn"])
    types["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"] = t.struct(
        {
            "numberValue": t.number().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut"])
    types["LookupMembershipNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupMembershipNameResponseIn"])
    types["LookupMembershipNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupMembershipNameResponseOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"])
    types["DeleteInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataIn"])
    types["DeleteInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataOut"])
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
    types["UpdateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateGroupMetadataIn"]
    )
    types["UpdateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateGroupMetadataOut"])
    types["MemberRelationIn"] = t.struct(
        {
            "relationType": t.string().optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyIn"])).optional(),
            "member": t.string().optional(),
        }
    ).named(renames["MemberRelationIn"])
    types["MemberRelationOut"] = t.struct(
        {
            "relationType": t.string().optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "preferredMemberKey": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "member": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemberRelationOut"])
    types["CreateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataIn"])
    types["CreateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataOut"])
    types["RsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["RsaPublicKeyInfoIn"]
    )
    types["RsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaPublicKeyInfoOut"])
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
    types["UpdateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateMembershipMetadataIn"]
    )
    types["UpdateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateMembershipMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"])
    types["UpdateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataIn"])
    types["UpdateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataOut"])
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
    types["UserInvitationIn"] = t.struct(
        {
            "state": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserInvitationIn"])
    types["UserInvitationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "mailsSentCount": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInvitationOut"])
    types["GetMembershipGraphMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMembershipGraphMetadataIn"])
    types["GetMembershipGraphMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetMembershipGraphMetadataOut"])
    types["SignInBehaviorIn"] = t.struct(
        {"redirectCondition": t.string().optional()}
    ).named(renames["SignInBehaviorIn"])
    types["SignInBehaviorOut"] = t.struct(
        {
            "redirectCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignInBehaviorOut"])
    types["ListGroupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupIn"])).optional(),
        }
    ).named(renames["ListGroupsResponseIn"])
    types["ListGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["ListInboundSsoAssignmentsResponseIn"] = t.struct(
        {
            "inboundSsoAssignments": t.array(
                t.proxy(renames["InboundSsoAssignmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInboundSsoAssignmentsResponseIn"])
    types["ListInboundSsoAssignmentsResponseOut"] = t.struct(
        {
            "inboundSsoAssignments": t.array(
                t.proxy(renames["InboundSsoAssignmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInboundSsoAssignmentsResponseOut"])
    types["GroupIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string(),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataIn"]
            ).optional(),
            "description": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]),
            "labels": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string(),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataOut"]
            ).optional(),
            "description": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]),
            "updateTime": t.string().optional(),
            "additionalGroupKeys": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["MembershipRelationIn"] = t.struct(
        {
            "membership": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "group": t.string().optional(),
        }
    ).named(renames["MembershipRelationIn"])
    types["MembershipRelationOut"] = t.struct(
        {
            "membership": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRelationOut"])
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
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"])
    types["DeleteInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataIn"])
    types["DeleteInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataOut"])
    types["ListUserInvitationsResponseIn"] = t.struct(
        {
            "userInvitations": t.array(t.proxy(renames["UserInvitationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUserInvitationsResponseIn"])
    types["ListUserInvitationsResponseOut"] = t.struct(
        {
            "userInvitations": t.array(
                t.proxy(renames["UserInvitationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUserInvitationsResponseOut"])
    types["IsInvitableUserResponseIn"] = t.struct(
        {"isInvitableUser": t.boolean().optional()}
    ).named(renames["IsInvitableUserResponseIn"])
    types["IsInvitableUserResponseOut"] = t.struct(
        {
            "isInvitableUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IsInvitableUserResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateIn"] = t.struct(
        {
            "customId": t.string().optional(),
            "healthScore": t.string().optional(),
            "etag": t.string().optional(),
            "managed": t.string().optional(),
            "complianceState": t.string().optional(),
            "assetTags": t.array(t.string()).optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "scoreReason": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateOut"] = t.struct(
        {
            "customId": t.string().optional(),
            "healthScore": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "etag": t.string().optional(),
            "managed": t.string().optional(),
            "ownerType": t.string().optional(),
            "complianceState": t.string().optional(),
            "assetTags": t.array(t.string()).optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "scoreReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut"])
    types["AddIdpCredentialRequestIn"] = t.struct(
        {"pemData": t.string().optional()}
    ).named(renames["AddIdpCredentialRequestIn"])
    types["AddIdpCredentialRequestOut"] = t.struct(
        {
            "pemData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddIdpCredentialRequestOut"])
    types["DeleteMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMembershipMetadataIn"]
    )
    types["DeleteMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMembershipMetadataOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["DeleteIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataIn"])
    types["DeleteIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteIdpCredentialOperationMetadataOut"])
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
    types["SendUserInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendUserInvitationRequestIn"]
    )
    types["SendUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendUserInvitationRequestOut"])
    types["CancelUserInvitationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelUserInvitationRequestIn"])
    types["CancelUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelUserInvitationRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "compromisedState": t.string().optional(),
            "passwordState": t.string().optional(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "compromisedState": t.string().optional(),
            "name": t.string().optional(),
            "firstSyncTime": t.string().optional(),
            "passwordState": t.string().optional(),
            "languageCode": t.string().optional(),
            "managementState": t.string().optional(),
            "userEmail": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
    types["CheckTransitiveMembershipResponseIn"] = t.struct(
        {"hasMembership": t.boolean().optional()}
    ).named(renames["CheckTransitiveMembershipResponseIn"])
    types["CheckTransitiveMembershipResponseOut"] = t.struct(
        {
            "hasMembership": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckTransitiveMembershipResponseOut"])
    types["CreateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataIn"])
    types["CreateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"])
    types["ExpiryDetailIn"] = t.struct({"expireTime": t.string().optional()}).named(
        renames["ExpiryDetailIn"]
    )
    types["ExpiryDetailOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpiryDetailOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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

    functions = {}
    functions["devicesGet"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCreate"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesCancelWipe"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDelete"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesList"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesWipe"] = cloudidentity.post(
        "v1/{name}:wipe",
        t.struct(
            {
                "name": t.string(),
                "customer": t.string().optional(),
                "removeResetLock": t.boolean().optional(),
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
    functions["devicesDeviceUsersClientStatesGet"] = cloudidentity.get(
        "v1/{parent}/clientStates",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "customer": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesPatch"] = cloudidentity.get(
        "v1/{parent}/clientStates",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "customer": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesDeviceUsersClientStatesList"] = cloudidentity.get(
        "v1/{parent}/clientStates",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "customer": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsDelete"] = cloudidentity.post(
        "v1/inboundSsoAssignments",
        t.struct(
            {
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
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
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
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
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
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
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
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
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "customer": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "rank": t.integer().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "targetGroup": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesGet"] = cloudidentity.get(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInboundSamlSsoProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesCreate"] = cloudidentity.get(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInboundSamlSsoProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesDelete"] = cloudidentity.get(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInboundSamlSsoProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesPatch"] = cloudidentity.get(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInboundSamlSsoProfilesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesList"] = cloudidentity.get(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListInboundSamlSsoProfilesResponseOut"]),
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
    functions["inboundSamlSsoProfilesIdpCredentialsAdd"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["inboundSamlSsoProfilesIdpCredentialsDelete"] = cloudidentity.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsLookup"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsPatch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsCreate"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdateSecuritySettings"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsSearch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGetSecuritySettings"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecuritySettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGetMembershipGraph"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCreate"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsList"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveMemberships"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsDelete"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchDirectGroups"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsModifyMembershipRoles"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGet"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCheckTransitiveMembership"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsLookup"] = cloudidentity.get(
        "v1/{parent}/memberships:lookup",
        t.struct(
            {
                "memberKey.namespace": t.string().optional(),
                "memberKey.id": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LookupMembershipNameResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsCancel"] = cloudidentity.get(
        "v1/{name}:isInvitableUser",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IsInvitableUserResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsGet"] = cloudidentity.get(
        "v1/{name}:isInvitableUser",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IsInvitableUserResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsSend"] = cloudidentity.get(
        "v1/{name}:isInvitableUser",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IsInvitableUserResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsList"] = cloudidentity.get(
        "v1/{name}:isInvitableUser",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IsInvitableUserResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsIsInvitableUser"] = cloudidentity.get(
        "v1/{name}:isInvitableUser",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["IsInvitableUserResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudidentity", renames=renames, types=types, functions=functions
    )
