from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudidentity() -> Import:
    cloudidentity = HTTPRuntime("https://cloudidentity.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudidentity_1_ErrorResponse",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn": "_cloudidentity_2_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut": "_cloudidentity_3_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn": "_cloudidentity_4_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut": "_cloudidentity_5_GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadataOut",
        "DynamicGroupQueryIn": "_cloudidentity_6_DynamicGroupQueryIn",
        "DynamicGroupQueryOut": "_cloudidentity_7_DynamicGroupQueryOut",
        "SamlSpConfigIn": "_cloudidentity_8_SamlSpConfigIn",
        "SamlSpConfigOut": "_cloudidentity_9_SamlSpConfigOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn": "_cloudidentity_10_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut": "_cloudidentity_11_GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut",
        "RsaPublicKeyInfoIn": "_cloudidentity_12_RsaPublicKeyInfoIn",
        "RsaPublicKeyInfoOut": "_cloudidentity_13_RsaPublicKeyInfoOut",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn": "_cloudidentity_14_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut": "_cloudidentity_15_GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut",
        "DeleteInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_16_DeleteInboundSamlSsoProfileOperationMetadataIn",
        "DeleteInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_17_DeleteInboundSamlSsoProfileOperationMetadataOut",
        "SecuritySettingsIn": "_cloudidentity_18_SecuritySettingsIn",
        "SecuritySettingsOut": "_cloudidentity_19_SecuritySettingsOut",
        "MembershipRelationIn": "_cloudidentity_20_MembershipRelationIn",
        "MembershipRelationOut": "_cloudidentity_21_MembershipRelationOut",
        "ListMembershipsResponseIn": "_cloudidentity_22_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_cloudidentity_23_ListMembershipsResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn": "_cloudidentity_24_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut": "_cloudidentity_25_GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut",
        "RestrictionEvaluationsIn": "_cloudidentity_26_RestrictionEvaluationsIn",
        "RestrictionEvaluationsOut": "_cloudidentity_27_RestrictionEvaluationsOut",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn": "_cloudidentity_28_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut": "_cloudidentity_29_GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut",
        "GoogleAppsCloudidentityDevicesV1ClientStateIn": "_cloudidentity_30_GoogleAppsCloudidentityDevicesV1ClientStateIn",
        "GoogleAppsCloudidentityDevicesV1ClientStateOut": "_cloudidentity_31_GoogleAppsCloudidentityDevicesV1ClientStateOut",
        "GroupRelationIn": "_cloudidentity_32_GroupRelationIn",
        "GroupRelationOut": "_cloudidentity_33_GroupRelationOut",
        "GetMembershipGraphMetadataIn": "_cloudidentity_34_GetMembershipGraphMetadataIn",
        "GetMembershipGraphMetadataOut": "_cloudidentity_35_GetMembershipGraphMetadataOut",
        "GetMembershipGraphResponseIn": "_cloudidentity_36_GetMembershipGraphResponseIn",
        "GetMembershipGraphResponseOut": "_cloudidentity_37_GetMembershipGraphResponseOut",
        "LookupGroupNameResponseIn": "_cloudidentity_38_LookupGroupNameResponseIn",
        "LookupGroupNameResponseOut": "_cloudidentity_39_LookupGroupNameResponseOut",
        "CreateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_40_CreateInboundSsoAssignmentOperationMetadataIn",
        "CreateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_41_CreateInboundSsoAssignmentOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn": "_cloudidentity_42_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut": "_cloudidentity_43_GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponseOut",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn": "_cloudidentity_44_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut": "_cloudidentity_45_GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut",
        "MembershipRoleIn": "_cloudidentity_46_MembershipRoleIn",
        "MembershipRoleOut": "_cloudidentity_47_MembershipRoleOut",
        "UserInvitationIn": "_cloudidentity_48_UserInvitationIn",
        "UserInvitationOut": "_cloudidentity_49_UserInvitationOut",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesIn": "_cloudidentity_50_GoogleAppsCloudidentityDevicesV1AndroidAttributesIn",
        "GoogleAppsCloudidentityDevicesV1AndroidAttributesOut": "_cloudidentity_51_GoogleAppsCloudidentityDevicesV1AndroidAttributesOut",
        "ListUserInvitationsResponseIn": "_cloudidentity_52_ListUserInvitationsResponseIn",
        "ListUserInvitationsResponseOut": "_cloudidentity_53_ListUserInvitationsResponseOut",
        "RestrictionEvaluationIn": "_cloudidentity_54_RestrictionEvaluationIn",
        "RestrictionEvaluationOut": "_cloudidentity_55_RestrictionEvaluationOut",
        "UpdateInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_56_UpdateInboundSsoAssignmentOperationMetadataIn",
        "UpdateInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_57_UpdateInboundSsoAssignmentOperationMetadataOut",
        "SignInBehaviorIn": "_cloudidentity_58_SignInBehaviorIn",
        "SignInBehaviorOut": "_cloudidentity_59_SignInBehaviorOut",
        "SearchTransitiveMembershipsResponseIn": "_cloudidentity_60_SearchTransitiveMembershipsResponseIn",
        "SearchTransitiveMembershipsResponseOut": "_cloudidentity_61_SearchTransitiveMembershipsResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn": "_cloudidentity_62_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut": "_cloudidentity_63_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponseOut",
        "DeleteIdpCredentialOperationMetadataIn": "_cloudidentity_64_DeleteIdpCredentialOperationMetadataIn",
        "DeleteIdpCredentialOperationMetadataOut": "_cloudidentity_65_DeleteIdpCredentialOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn": "_cloudidentity_66_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut": "_cloudidentity_67_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponseOut",
        "CreateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_68_CreateInboundSamlSsoProfileOperationMetadataIn",
        "CreateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_69_CreateInboundSamlSsoProfileOperationMetadataOut",
        "DeleteMembershipMetadataIn": "_cloudidentity_70_DeleteMembershipMetadataIn",
        "DeleteMembershipMetadataOut": "_cloudidentity_71_DeleteMembershipMetadataOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn": "_cloudidentity_72_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut": "_cloudidentity_73_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut",
        "SearchDirectGroupsResponseIn": "_cloudidentity_74_SearchDirectGroupsResponseIn",
        "SearchDirectGroupsResponseOut": "_cloudidentity_75_SearchDirectGroupsResponseOut",
        "GoogleAppsCloudidentityDevicesV1DeviceIn": "_cloudidentity_76_GoogleAppsCloudidentityDevicesV1DeviceIn",
        "GoogleAppsCloudidentityDevicesV1DeviceOut": "_cloudidentity_77_GoogleAppsCloudidentityDevicesV1DeviceOut",
        "TransitiveMembershipRoleIn": "_cloudidentity_78_TransitiveMembershipRoleIn",
        "TransitiveMembershipRoleOut": "_cloudidentity_79_TransitiveMembershipRoleOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn": "_cloudidentity_80_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut": "_cloudidentity_81_GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequestOut",
        "AddIdpCredentialRequestIn": "_cloudidentity_82_AddIdpCredentialRequestIn",
        "AddIdpCredentialRequestOut": "_cloudidentity_83_AddIdpCredentialRequestOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn": "_cloudidentity_84_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut": "_cloudidentity_85_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut",
        "OperationIn": "_cloudidentity_86_OperationIn",
        "OperationOut": "_cloudidentity_87_OperationOut",
        "GroupIn": "_cloudidentity_88_GroupIn",
        "GroupOut": "_cloudidentity_89_GroupOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn": "_cloudidentity_90_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut": "_cloudidentity_91_GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponseOut",
        "ListInboundSamlSsoProfilesResponseIn": "_cloudidentity_92_ListInboundSamlSsoProfilesResponseIn",
        "ListInboundSamlSsoProfilesResponseOut": "_cloudidentity_93_ListInboundSamlSsoProfilesResponseOut",
        "CancelUserInvitationRequestIn": "_cloudidentity_94_CancelUserInvitationRequestIn",
        "CancelUserInvitationRequestOut": "_cloudidentity_95_CancelUserInvitationRequestOut",
        "SearchGroupsResponseIn": "_cloudidentity_96_SearchGroupsResponseIn",
        "SearchGroupsResponseOut": "_cloudidentity_97_SearchGroupsResponseOut",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn": "_cloudidentity_98_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut": "_cloudidentity_99_GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut",
        "LookupMembershipNameResponseIn": "_cloudidentity_100_LookupMembershipNameResponseIn",
        "LookupMembershipNameResponseOut": "_cloudidentity_101_LookupMembershipNameResponseOut",
        "InboundSamlSsoProfileIn": "_cloudidentity_102_InboundSamlSsoProfileIn",
        "InboundSamlSsoProfileOut": "_cloudidentity_103_InboundSamlSsoProfileOut",
        "IsInvitableUserResponseIn": "_cloudidentity_104_IsInvitableUserResponseIn",
        "IsInvitableUserResponseOut": "_cloudidentity_105_IsInvitableUserResponseOut",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn": "_cloudidentity_106_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut": "_cloudidentity_107_GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut",
        "GoogleAppsCloudidentityDevicesV1DeviceUserIn": "_cloudidentity_108_GoogleAppsCloudidentityDevicesV1DeviceUserIn",
        "GoogleAppsCloudidentityDevicesV1DeviceUserOut": "_cloudidentity_109_GoogleAppsCloudidentityDevicesV1DeviceUserOut",
        "SamlIdpConfigIn": "_cloudidentity_110_SamlIdpConfigIn",
        "SamlIdpConfigOut": "_cloudidentity_111_SamlIdpConfigOut",
        "DynamicGroupStatusIn": "_cloudidentity_112_DynamicGroupStatusIn",
        "DynamicGroupStatusOut": "_cloudidentity_113_DynamicGroupStatusOut",
        "SendUserInvitationRequestIn": "_cloudidentity_114_SendUserInvitationRequestIn",
        "SendUserInvitationRequestOut": "_cloudidentity_115_SendUserInvitationRequestOut",
        "StatusIn": "_cloudidentity_116_StatusIn",
        "StatusOut": "_cloudidentity_117_StatusOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn": "_cloudidentity_118_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut": "_cloudidentity_119_GoogleAppsCloudidentityDevicesV1WipeDeviceRequestOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn": "_cloudidentity_120_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut": "_cloudidentity_121_GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut",
        "InboundSsoAssignmentIn": "_cloudidentity_122_InboundSsoAssignmentIn",
        "InboundSsoAssignmentOut": "_cloudidentity_123_InboundSsoAssignmentOut",
        "SamlSsoInfoIn": "_cloudidentity_124_SamlSsoInfoIn",
        "SamlSsoInfoOut": "_cloudidentity_125_SamlSsoInfoOut",
        "IdpCredentialIn": "_cloudidentity_126_IdpCredentialIn",
        "IdpCredentialOut": "_cloudidentity_127_IdpCredentialOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn": "_cloudidentity_128_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut": "_cloudidentity_129_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn": "_cloudidentity_130_GoogleAppsCloudidentityDevicesV1CustomAttributeValueIn",
        "GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut": "_cloudidentity_131_GoogleAppsCloudidentityDevicesV1CustomAttributeValueOut",
        "DeleteInboundSsoAssignmentOperationMetadataIn": "_cloudidentity_132_DeleteInboundSsoAssignmentOperationMetadataIn",
        "DeleteInboundSsoAssignmentOperationMetadataOut": "_cloudidentity_133_DeleteInboundSsoAssignmentOperationMetadataOut",
        "DeleteGroupMetadataIn": "_cloudidentity_134_DeleteGroupMetadataIn",
        "DeleteGroupMetadataOut": "_cloudidentity_135_DeleteGroupMetadataOut",
        "MembershipAdjacencyListIn": "_cloudidentity_136_MembershipAdjacencyListIn",
        "MembershipAdjacencyListOut": "_cloudidentity_137_MembershipAdjacencyListOut",
        "ModifyMembershipRolesResponseIn": "_cloudidentity_138_ModifyMembershipRolesResponseIn",
        "ModifyMembershipRolesResponseOut": "_cloudidentity_139_ModifyMembershipRolesResponseOut",
        "ListIdpCredentialsResponseIn": "_cloudidentity_140_ListIdpCredentialsResponseIn",
        "ListIdpCredentialsResponseOut": "_cloudidentity_141_ListIdpCredentialsResponseOut",
        "CheckTransitiveMembershipResponseIn": "_cloudidentity_142_CheckTransitiveMembershipResponseIn",
        "CheckTransitiveMembershipResponseOut": "_cloudidentity_143_CheckTransitiveMembershipResponseOut",
        "AddIdpCredentialOperationMetadataIn": "_cloudidentity_144_AddIdpCredentialOperationMetadataIn",
        "AddIdpCredentialOperationMetadataOut": "_cloudidentity_145_AddIdpCredentialOperationMetadataOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn": "_cloudidentity_146_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut": "_cloudidentity_147_GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut",
        "MembershipIn": "_cloudidentity_148_MembershipIn",
        "MembershipOut": "_cloudidentity_149_MembershipOut",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn": "_cloudidentity_150_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseIn",
        "GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut": "_cloudidentity_151_GoogleAppsCloudidentityDevicesV1WipeDeviceResponseOut",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn": "_cloudidentity_152_GoogleAppsCloudidentityDevicesV1ListDevicesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut": "_cloudidentity_153_GoogleAppsCloudidentityDevicesV1ListDevicesResponseOut",
        "ListInboundSsoAssignmentsResponseIn": "_cloudidentity_154_ListInboundSsoAssignmentsResponseIn",
        "ListInboundSsoAssignmentsResponseOut": "_cloudidentity_155_ListInboundSsoAssignmentsResponseOut",
        "CreateGroupMetadataIn": "_cloudidentity_156_CreateGroupMetadataIn",
        "CreateGroupMetadataOut": "_cloudidentity_157_CreateGroupMetadataOut",
        "MemberRestrictionIn": "_cloudidentity_158_MemberRestrictionIn",
        "MemberRestrictionOut": "_cloudidentity_159_MemberRestrictionOut",
        "UpdateInboundSamlSsoProfileOperationMetadataIn": "_cloudidentity_160_UpdateInboundSamlSsoProfileOperationMetadataIn",
        "UpdateInboundSamlSsoProfileOperationMetadataOut": "_cloudidentity_161_UpdateInboundSamlSsoProfileOperationMetadataOut",
        "MembershipRoleRestrictionEvaluationIn": "_cloudidentity_162_MembershipRoleRestrictionEvaluationIn",
        "MembershipRoleRestrictionEvaluationOut": "_cloudidentity_163_MembershipRoleRestrictionEvaluationOut",
        "EntityKeyIn": "_cloudidentity_164_EntityKeyIn",
        "EntityKeyOut": "_cloudidentity_165_EntityKeyOut",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn": "_cloudidentity_166_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn",
        "GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut": "_cloudidentity_167_GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn": "_cloudidentity_168_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut": "_cloudidentity_169_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponseOut",
        "ListGroupsResponseIn": "_cloudidentity_170_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_cloudidentity_171_ListGroupsResponseOut",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn": "_cloudidentity_172_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn",
        "GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut": "_cloudidentity_173_GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn": "_cloudidentity_174_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut": "_cloudidentity_175_GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut",
        "MemberRelationIn": "_cloudidentity_176_MemberRelationIn",
        "MemberRelationOut": "_cloudidentity_177_MemberRelationOut",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn": "_cloudidentity_178_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn",
        "GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut": "_cloudidentity_179_GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut",
        "DsaPublicKeyInfoIn": "_cloudidentity_180_DsaPublicKeyInfoIn",
        "DsaPublicKeyInfoOut": "_cloudidentity_181_DsaPublicKeyInfoOut",
        "UpdateMembershipMetadataIn": "_cloudidentity_182_UpdateMembershipMetadataIn",
        "UpdateMembershipMetadataOut": "_cloudidentity_183_UpdateMembershipMetadataOut",
        "CreateMembershipMetadataIn": "_cloudidentity_184_CreateMembershipMetadataIn",
        "CreateMembershipMetadataOut": "_cloudidentity_185_CreateMembershipMetadataOut",
        "UpdateMembershipRolesParamsIn": "_cloudidentity_186_UpdateMembershipRolesParamsIn",
        "UpdateMembershipRolesParamsOut": "_cloudidentity_187_UpdateMembershipRolesParamsOut",
        "ExpiryDetailIn": "_cloudidentity_188_ExpiryDetailIn",
        "ExpiryDetailOut": "_cloudidentity_189_ExpiryDetailOut",
        "UpdateGroupMetadataIn": "_cloudidentity_190_UpdateGroupMetadataIn",
        "UpdateGroupMetadataOut": "_cloudidentity_191_UpdateGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn": "_cloudidentity_192_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut": "_cloudidentity_193_GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut",
        "DynamicGroupMetadataIn": "_cloudidentity_194_DynamicGroupMetadataIn",
        "DynamicGroupMetadataOut": "_cloudidentity_195_DynamicGroupMetadataOut",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn": "_cloudidentity_196_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseIn",
        "GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut": "_cloudidentity_197_GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponseOut",
        "SearchTransitiveGroupsResponseIn": "_cloudidentity_198_SearchTransitiveGroupsResponseIn",
        "SearchTransitiveGroupsResponseOut": "_cloudidentity_199_SearchTransitiveGroupsResponseOut",
        "ModifyMembershipRolesRequestIn": "_cloudidentity_200_ModifyMembershipRolesRequestIn",
        "ModifyMembershipRolesRequestOut": "_cloudidentity_201_ModifyMembershipRolesRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceMetadataOut"])
    types["RsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["RsaPublicKeyInfoIn"]
    )
    types["RsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RsaPublicKeyInfoOut"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CreateDeviceMetadataOut"])
    types["DeleteInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataIn"])
    types["DeleteInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSamlSsoProfileOperationMetadataOut"])
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
    types["MembershipRelationIn"] = t.struct(
        {
            "description": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "membership": t.string().optional(),
            "displayName": t.string().optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MembershipRelationIn"])
    types["MembershipRelationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "group": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "membership": t.string().optional(),
            "displayName": t.string().optional(),
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRelationOut"])
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
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customer": t.string().optional(),
            "names": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseIn"])
    types[
        "GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customer": t.string().optional(),
            "names": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponseOut"]
    )
    types["GoogleAppsCloudidentityDevicesV1ClientStateIn"] = t.struct(
        {
            "assetTags": t.array(t.string()).optional(),
            "complianceState": t.string().optional(),
            "scoreReason": t.string().optional(),
            "customId": t.string().optional(),
            "healthScore": t.string().optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "managed": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
    types["GoogleAppsCloudidentityDevicesV1ClientStateOut"] = t.struct(
        {
            "assetTags": t.array(t.string()).optional(),
            "complianceState": t.string().optional(),
            "scoreReason": t.string().optional(),
            "customId": t.string().optional(),
            "ownerType": t.string().optional(),
            "healthScore": t.string().optional(),
            "keyValuePairs": t.struct({"_": t.string().optional()}).optional(),
            "managed": t.string().optional(),
            "name": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
    types["GroupRelationIn"] = t.struct(
        {
            "relationType": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyIn"]).optional(),
            "group": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "roles": t.array(t.proxy(renames["TransitiveMembershipRoleIn"])).optional(),
        }
    ).named(renames["GroupRelationIn"])
    types["GroupRelationOut"] = t.struct(
        {
            "relationType": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]).optional(),
            "group": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "roles": t.array(
                t.proxy(renames["TransitiveMembershipRoleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupRelationOut"])
    types["GetMembershipGraphMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetMembershipGraphMetadataIn"])
    types["GetMembershipGraphMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetMembershipGraphMetadataOut"])
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
    types["LookupGroupNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupGroupNameResponseIn"])
    types["LookupGroupNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupGroupNameResponseOut"])
    types["CreateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataIn"])
    types["CreateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSsoAssignmentOperationMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"] = t.struct(
        {
            "supportsWorkProfile": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesIn"])
    types["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"] = t.struct(
        {
            "supportsWorkProfile": t.boolean().optional(),
            "ownershipPrivilege": t.string().optional(),
            "enabledUnknownSources": t.boolean().optional(),
            "ownerProfileAccount": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"])
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
    types["RestrictionEvaluationIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestrictionEvaluationIn"]
    )
    types["RestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestrictionEvaluationOut"])
    types["UpdateInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataIn"])
    types["UpdateInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSsoAssignmentOperationMetadataOut"])
    types["SignInBehaviorIn"] = t.struct(
        {"redirectCondition": t.string().optional()}
    ).named(renames["SignInBehaviorIn"])
    types["SignInBehaviorOut"] = t.struct(
        {
            "redirectCondition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignInBehaviorOut"])
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
    types["CreateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataIn"])
    types["CreateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateInboundSamlSsoProfileOperationMetadataOut"])
    types["DeleteMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteMembershipMetadataIn"]
    )
    types["DeleteMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteMembershipMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeviceIn"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "serialNumber": t.string().optional(),
            "assetTag": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceOut"] = t.struct(
        {
            "securityPatchTime": t.string().optional(),
            "brand": t.string().optional(),
            "releaseVersion": t.string().optional(),
            "encryptionState": t.string().optional(),
            "deviceType": t.string().optional(),
            "osVersion": t.string().optional(),
            "deviceId": t.string().optional(),
            "imei": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "otherAccounts": t.array(t.string()).optional(),
            "bootloaderVersion": t.string().optional(),
            "wifiMacAddresses": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "compromisedState": t.string().optional(),
            "model": t.string().optional(),
            "basebandVersion": t.string().optional(),
            "enabledDeveloperOptions": t.boolean().optional(),
            "ownerType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "networkOperator": t.string().optional(),
            "kernelVersion": t.string().optional(),
            "meid": t.string().optional(),
            "assetTag": t.string().optional(),
            "androidSpecificAttributes": t.proxy(
                renames["GoogleAppsCloudidentityDevicesV1AndroidAttributesOut"]
            ).optional(),
            "name": t.string().optional(),
            "manufacturer": t.string().optional(),
            "enabledUsbDebugging": t.boolean().optional(),
            "buildNumber": t.string().optional(),
            "managementState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceOut"])
    types["TransitiveMembershipRoleIn"] = t.struct(
        {"role": t.string().optional()}
    ).named(renames["TransitiveMembershipRoleIn"])
    types["TransitiveMembershipRoleOut"] = t.struct(
        {
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransitiveMembershipRoleOut"])
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
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["GroupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "parent": t.string(),
            "groupKey": t.proxy(renames["EntityKeyIn"]),
            "displayName": t.string().optional(),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataIn"]
            ).optional(),
        }
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}),
            "parent": t.string(),
            "additionalGroupKeys": t.array(t.proxy(renames["EntityKeyOut"])).optional(),
            "name": t.string().optional(),
            "groupKey": t.proxy(renames["EntityKeyOut"]),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "dynamicGroupMetadata": t.proxy(
                renames["DynamicGroupMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["CancelUserInvitationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CancelUserInvitationRequestIn"])
    types["CancelUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelUserInvitationRequestOut"])
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
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadataOut"])
    types["LookupMembershipNameResponseIn"] = t.struct(
        {"name": t.string().optional()}
    ).named(renames["LookupMembershipNameResponseIn"])
    types["LookupMembershipNameResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupMembershipNameResponseOut"])
    types["InboundSamlSsoProfileIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
            "customer": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileIn"])
    types["InboundSamlSsoProfileOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "spConfig": t.proxy(renames["SamlSpConfigOut"]).optional(),
            "name": t.string().optional(),
            "customer": t.string().optional(),
            "idpConfig": t.proxy(renames["SamlIdpConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSamlSsoProfileOut"])
    types["IsInvitableUserResponseIn"] = t.struct(
        {"isInvitableUser": t.boolean().optional()}
    ).named(renames["IsInvitableUserResponseIn"])
    types["IsInvitableUserResponseOut"] = t.struct(
        {
            "isInvitableUser": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IsInvitableUserResponseOut"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserIn"] = t.struct(
        {
            "passwordState": t.string().optional(),
            "createTime": t.string().optional(),
            "compromisedState": t.string().optional(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserIn"])
    types["GoogleAppsCloudidentityDevicesV1DeviceUserOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "passwordState": t.string().optional(),
            "firstSyncTime": t.string().optional(),
            "userAgent": t.string().optional(),
            "managementState": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "compromisedState": t.string().optional(),
            "userEmail": t.string().optional(),
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1DeviceUserOut"])
    types["SamlIdpConfigIn"] = t.struct(
        {
            "logoutRedirectUri": t.string().optional(),
            "changePasswordUri": t.string().optional(),
            "entityId": t.string(),
            "singleSignOnServiceUri": t.string(),
        }
    ).named(renames["SamlIdpConfigIn"])
    types["SamlIdpConfigOut"] = t.struct(
        {
            "logoutRedirectUri": t.string().optional(),
            "changePasswordUri": t.string().optional(),
            "entityId": t.string(),
            "singleSignOnServiceUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlIdpConfigOut"])
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
    types["SendUserInvitationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SendUserInvitationRequestIn"]
    )
    types["SendUserInvitationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SendUserInvitationRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadataOut"])
    types["InboundSsoAssignmentIn"] = t.struct(
        {
            "customer": t.string().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
            "ssoMode": t.string().optional(),
            "targetGroup": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
            "rank": t.integer().optional(),
        }
    ).named(renames["InboundSsoAssignmentIn"])
    types["InboundSsoAssignmentOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "signInBehavior": t.proxy(renames["SignInBehaviorOut"]).optional(),
            "name": t.string().optional(),
            "ssoMode": t.string().optional(),
            "targetGroup": t.string().optional(),
            "targetOrgUnit": t.string().optional(),
            "samlSsoInfo": t.proxy(renames["SamlSsoInfoOut"]).optional(),
            "rank": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InboundSsoAssignmentOut"])
    types["SamlSsoInfoIn"] = t.struct({"inboundSamlSsoProfile": t.string()}).named(
        renames["SamlSsoInfoIn"]
    )
    types["SamlSsoInfoOut"] = t.struct(
        {
            "inboundSamlSsoProfile": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SamlSsoInfoOut"])
    types["IdpCredentialIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IdpCredentialIn"]
    )
    types["IdpCredentialOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "dsaKeyInfo": t.proxy(renames["DsaPublicKeyInfoOut"]).optional(),
            "rsaKeyInfo": t.proxy(renames["RsaPublicKeyInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdpCredentialOut"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceRequestOut"])
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
    types["DeleteInboundSsoAssignmentOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataIn"])
    types["DeleteInboundSsoAssignmentOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteInboundSsoAssignmentOperationMetadataOut"])
    types["DeleteGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteGroupMetadataIn"]
    )
    types["DeleteGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteGroupMetadataOut"])
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
    types["ModifyMembershipRolesResponseIn"] = t.struct(
        {"membership": t.proxy(renames["MembershipIn"]).optional()}
    ).named(renames["ModifyMembershipRolesResponseIn"])
    types["ModifyMembershipRolesResponseOut"] = t.struct(
        {
            "membership": t.proxy(renames["MembershipOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesResponseOut"])
    types["ListIdpCredentialsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "idpCredentials": t.array(t.proxy(renames["IdpCredentialIn"])).optional(),
        }
    ).named(renames["ListIdpCredentialsResponseIn"])
    types["ListIdpCredentialsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "idpCredentials": t.array(t.proxy(renames["IdpCredentialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIdpCredentialsResponseOut"])
    types["CheckTransitiveMembershipResponseIn"] = t.struct(
        {"hasMembership": t.boolean().optional()}
    ).named(renames["CheckTransitiveMembershipResponseIn"])
    types["CheckTransitiveMembershipResponseOut"] = t.struct(
        {
            "hasMembership": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckTransitiveMembershipResponseOut"])
    types["AddIdpCredentialOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AddIdpCredentialOperationMetadataIn"])
    types["AddIdpCredentialOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddIdpCredentialOperationMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequestOut"])
    types["MembershipIn"] = t.struct(
        {
            "roles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyIn"]),
        }
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "roles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "updateTime": t.string().optional(),
            "deliverySetting": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "preferredMemberKey": t.proxy(renames["EntityKeyOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
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
    types["CreateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateGroupMetadataIn"]
    )
    types["CreateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateGroupMetadataOut"])
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
    types["UpdateInboundSamlSsoProfileOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataIn"])
    types["UpdateInboundSamlSsoProfileOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateInboundSamlSsoProfileOperationMetadataOut"])
    types["MembershipRoleRestrictionEvaluationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["MembershipRoleRestrictionEvaluationIn"])
    types["MembershipRoleRestrictionEvaluationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipRoleRestrictionEvaluationOut"])
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
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"] = t.struct(
        {"customer": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestIn"])
    types["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"] = t.struct(
        {
            "customer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequestOut"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadataOut"])
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
    types["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn"] = t.struct(
        {
            "clientStates": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseIn"])
    types["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"] = t.struct(
        {
            "clientStates": t.array(
                t.proxy(renames["GoogleAppsCloudidentityDevicesV1ClientStateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCloudidentityDevicesV1ListClientStatesResponseOut"])
    types["DsaPublicKeyInfoIn"] = t.struct({"keySize": t.integer().optional()}).named(
        renames["DsaPublicKeyInfoIn"]
    )
    types["DsaPublicKeyInfoOut"] = t.struct(
        {
            "keySize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsaPublicKeyInfoOut"])
    types["UpdateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateMembershipMetadataIn"]
    )
    types["UpdateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateMembershipMetadataOut"])
    types["CreateMembershipMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateMembershipMetadataIn"]
    )
    types["CreateMembershipMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateMembershipMetadataOut"])
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
    types["ExpiryDetailIn"] = t.struct({"expireTime": t.string().optional()}).named(
        renames["ExpiryDetailIn"]
    )
    types["ExpiryDetailOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpiryDetailOut"])
    types["UpdateGroupMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateGroupMetadataIn"]
    )
    types["UpdateGroupMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateGroupMetadataOut"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataIn"])
    types["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadataOut"])
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
    types["ModifyMembershipRolesRequestIn"] = t.struct(
        {
            "removeRoles": t.array(t.string()).optional(),
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsIn"])
            ).optional(),
            "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestIn"])
    types["ModifyMembershipRolesRequestOut"] = t.struct(
        {
            "removeRoles": t.array(t.string()).optional(),
            "updateRolesParams": t.array(
                t.proxy(renames["UpdateMembershipRolesParamsOut"])
            ).optional(),
            "addRoles": t.array(t.proxy(renames["MembershipRoleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyMembershipRolesRequestOut"])

    functions = {}
    functions["devicesGet"] = cloudidentity.post(
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
    functions["devicesDelete"] = cloudidentity.post(
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
    functions["devicesList"] = cloudidentity.post(
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
    functions["devicesWipe"] = cloudidentity.post(
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
    functions["devicesCreate"] = cloudidentity.post(
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
    functions["devicesCancelWipe"] = cloudidentity.post(
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
    functions["inboundSsoAssignmentsCreate"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "customer": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "targetGroup": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "rank": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsDelete"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "customer": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "targetGroup": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "rank": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsGet"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "customer": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "targetGroup": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "rank": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsList"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "customer": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "targetGroup": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "rank": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSsoAssignmentsPatch"] = cloudidentity.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "customer": t.string().optional(),
                "signInBehavior": t.proxy(renames["SignInBehaviorIn"]).optional(),
                "ssoMode": t.string().optional(),
                "targetGroup": t.string().optional(),
                "targetOrgUnit": t.string().optional(),
                "samlSsoInfo": t.proxy(renames["SamlSsoInfoIn"]).optional(),
                "rank": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesList"] = cloudidentity.post(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "displayName": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesDelete"] = cloudidentity.post(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "displayName": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesGet"] = cloudidentity.post(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "displayName": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesPatch"] = cloudidentity.post(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "displayName": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesCreate"] = cloudidentity.post(
        "v1/inboundSamlSsoProfiles",
        t.struct(
            {
                "displayName": t.string().optional(),
                "spConfig": t.proxy(renames["SamlSpConfigIn"]).optional(),
                "customer": t.string().optional(),
                "idpConfig": t.proxy(renames["SamlIdpConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsGet"] = cloudidentity.get(
        "v1/{parent}/idpCredentials",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdpCredentialsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsAdd"] = cloudidentity.get(
        "v1/{parent}/idpCredentials",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdpCredentialsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsDelete"] = cloudidentity.get(
        "v1/{parent}/idpCredentials",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdpCredentialsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["inboundSamlSsoProfilesIdpCredentialsList"] = cloudidentity.get(
        "v1/{parent}/idpCredentials",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIdpCredentialsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsGet"] = cloudidentity.post(
        "v1/{name}:send",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsList"] = cloudidentity.post(
        "v1/{name}:send",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsCancel"] = cloudidentity.post(
        "v1/{name}:send",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsIsInvitableUser"] = cloudidentity.post(
        "v1/{name}:send",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersUserinvitationsSend"] = cloudidentity.post(
        "v1/{name}:send",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsSearch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGetSecuritySettings"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsLookup"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsUpdateSecuritySettings"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsPatch"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsDelete"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsCreate"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsList"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsGet"] = cloudidentity.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCheckTransitiveMembership"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsLookup"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGetMembershipGraph"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchDirectGroups"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveMemberships"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsCreate"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsGet"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsList"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsDelete"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsSearchTransitiveGroups"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["groupsMembershipsModifyMembershipRoles"] = cloudidentity.post(
        "v1/{name}:modifyMembershipRoles",
        t.struct(
            {
                "name": t.string(),
                "removeRoles": t.array(t.string()).optional(),
                "updateRolesParams": t.array(
                    t.proxy(renames["UpdateMembershipRolesParamsIn"])
                ).optional(),
                "addRoles": t.array(t.proxy(renames["MembershipRoleIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ModifyMembershipRolesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudidentity",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
