from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_managedidentities():
    managedidentities = HTTPRuntime("https://managedidentities.googleapis.com/")

    renames = {
        "ErrorResponse": "_managedidentities_1_ErrorResponse",
        "LDAPSSettingsIn": "_managedidentities_2_LDAPSSettingsIn",
        "LDAPSSettingsOut": "_managedidentities_3_LDAPSSettingsOut",
        "ScheduleIn": "_managedidentities_4_ScheduleIn",
        "ScheduleOut": "_managedidentities_5_ScheduleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_managedidentities_6_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_managedidentities_7_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataIn": "_managedidentities_8_GoogleCloudManagedidentitiesV1alpha1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataOut": "_managedidentities_9_GoogleCloudManagedidentitiesV1alpha1OpMetadataOut",
        "DomainIn": "_managedidentities_10_DomainIn",
        "DomainOut": "_managedidentities_11_DomainOut",
        "RestoreDomainRequestIn": "_managedidentities_12_RestoreDomainRequestIn",
        "RestoreDomainRequestOut": "_managedidentities_13_RestoreDomainRequestOut",
        "LocationIn": "_managedidentities_14_LocationIn",
        "LocationOut": "_managedidentities_15_LocationOut",
        "GoogleCloudManagedidentitiesV1OpMetadataIn": "_managedidentities_16_GoogleCloudManagedidentitiesV1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1OpMetadataOut": "_managedidentities_17_GoogleCloudManagedidentitiesV1OpMetadataOut",
        "ValidateTrustRequestIn": "_managedidentities_18_ValidateTrustRequestIn",
        "ValidateTrustRequestOut": "_managedidentities_19_ValidateTrustRequestOut",
        "DailyCycleIn": "_managedidentities_20_DailyCycleIn",
        "DailyCycleOut": "_managedidentities_21_DailyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_managedidentities_22_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_managedidentities_23_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "AttachTrustRequestIn": "_managedidentities_24_AttachTrustRequestIn",
        "AttachTrustRequestOut": "_managedidentities_25_AttachTrustRequestOut",
        "TimeOfDayIn": "_managedidentities_26_TimeOfDayIn",
        "TimeOfDayOut": "_managedidentities_27_TimeOfDayOut",
        "CancelOperationRequestIn": "_managedidentities_28_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_managedidentities_29_CancelOperationRequestOut",
        "PeeringIn": "_managedidentities_30_PeeringIn",
        "PeeringOut": "_managedidentities_31_PeeringOut",
        "TrustIn": "_managedidentities_32_TrustIn",
        "TrustOut": "_managedidentities_33_TrustOut",
        "SqlIntegrationIn": "_managedidentities_34_SqlIntegrationIn",
        "SqlIntegrationOut": "_managedidentities_35_SqlIntegrationOut",
        "PolicyIn": "_managedidentities_36_PolicyIn",
        "PolicyOut": "_managedidentities_37_PolicyOut",
        "DateIn": "_managedidentities_38_DateIn",
        "DateOut": "_managedidentities_39_DateOut",
        "TestIamPermissionsResponseIn": "_managedidentities_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_managedidentities_41_TestIamPermissionsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_managedidentities_42_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_managedidentities_43_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "DisableMigrationRequestIn": "_managedidentities_44_DisableMigrationRequestIn",
        "DisableMigrationRequestOut": "_managedidentities_45_DisableMigrationRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_managedidentities_46_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_managedidentities_47_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "StatusIn": "_managedidentities_48_StatusIn",
        "StatusOut": "_managedidentities_49_StatusOut",
        "OnPremDomainDetailsIn": "_managedidentities_50_OnPremDomainDetailsIn",
        "OnPremDomainDetailsOut": "_managedidentities_51_OnPremDomainDetailsOut",
        "DetachTrustRequestIn": "_managedidentities_52_DetachTrustRequestIn",
        "DetachTrustRequestOut": "_managedidentities_53_DetachTrustRequestOut",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataIn": "_managedidentities_54_GoogleCloudManagedidentitiesV1beta1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataOut": "_managedidentities_55_GoogleCloudManagedidentitiesV1beta1OpMetadataOut",
        "CertificateIn": "_managedidentities_56_CertificateIn",
        "CertificateOut": "_managedidentities_57_CertificateOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_managedidentities_58_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_managedidentities_59_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "TestIamPermissionsRequestIn": "_managedidentities_60_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_managedidentities_61_TestIamPermissionsRequestOut",
        "ResetAdminPasswordResponseIn": "_managedidentities_62_ResetAdminPasswordResponseIn",
        "ResetAdminPasswordResponseOut": "_managedidentities_63_ResetAdminPasswordResponseOut",
        "OperationMetadataIn": "_managedidentities_64_OperationMetadataIn",
        "OperationMetadataOut": "_managedidentities_65_OperationMetadataOut",
        "ListBackupsResponseIn": "_managedidentities_66_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_managedidentities_67_ListBackupsResponseOut",
        "OperationIn": "_managedidentities_68_OperationIn",
        "OperationOut": "_managedidentities_69_OperationOut",
        "ListLocationsResponseIn": "_managedidentities_70_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_managedidentities_71_ListLocationsResponseOut",
        "BackupIn": "_managedidentities_72_BackupIn",
        "BackupOut": "_managedidentities_73_BackupOut",
        "DomainJoinMachineRequestIn": "_managedidentities_74_DomainJoinMachineRequestIn",
        "DomainJoinMachineRequestOut": "_managedidentities_75_DomainJoinMachineRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_managedidentities_76_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_managedidentities_77_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "BindingIn": "_managedidentities_78_BindingIn",
        "BindingOut": "_managedidentities_79_BindingOut",
        "ExtendSchemaRequestIn": "_managedidentities_80_ExtendSchemaRequestIn",
        "ExtendSchemaRequestOut": "_managedidentities_81_ExtendSchemaRequestOut",
        "ReconfigureTrustRequestIn": "_managedidentities_82_ReconfigureTrustRequestIn",
        "ReconfigureTrustRequestOut": "_managedidentities_83_ReconfigureTrustRequestOut",
        "UpdatePolicyIn": "_managedidentities_84_UpdatePolicyIn",
        "UpdatePolicyOut": "_managedidentities_85_UpdatePolicyOut",
        "EnableMigrationRequestIn": "_managedidentities_86_EnableMigrationRequestIn",
        "EnableMigrationRequestOut": "_managedidentities_87_EnableMigrationRequestOut",
        "ListSqlIntegrationsResponseIn": "_managedidentities_88_ListSqlIntegrationsResponseIn",
        "ListSqlIntegrationsResponseOut": "_managedidentities_89_ListSqlIntegrationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_managedidentities_90_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_managedidentities_91_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_managedidentities_92_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_managedidentities_93_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "ListPeeringsResponseIn": "_managedidentities_94_ListPeeringsResponseIn",
        "ListPeeringsResponseOut": "_managedidentities_95_ListPeeringsResponseOut",
        "ListOperationsResponseIn": "_managedidentities_96_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_managedidentities_97_ListOperationsResponseOut",
        "ListDomainsResponseIn": "_managedidentities_98_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_managedidentities_99_ListDomainsResponseOut",
        "EmptyIn": "_managedidentities_100_EmptyIn",
        "EmptyOut": "_managedidentities_101_EmptyOut",
        "DomainJoinMachineResponseIn": "_managedidentities_102_DomainJoinMachineResponseIn",
        "DomainJoinMachineResponseOut": "_managedidentities_103_DomainJoinMachineResponseOut",
        "ExprIn": "_managedidentities_104_ExprIn",
        "ExprOut": "_managedidentities_105_ExprOut",
        "MaintenancePolicyIn": "_managedidentities_106_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_managedidentities_107_MaintenancePolicyOut",
        "SetIamPolicyRequestIn": "_managedidentities_108_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_managedidentities_109_SetIamPolicyRequestOut",
        "DenyMaintenancePeriodIn": "_managedidentities_110_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_managedidentities_111_DenyMaintenancePeriodOut",
        "WeeklyCycleIn": "_managedidentities_112_WeeklyCycleIn",
        "WeeklyCycleOut": "_managedidentities_113_WeeklyCycleOut",
        "MaintenanceWindowIn": "_managedidentities_114_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_managedidentities_115_MaintenanceWindowOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_managedidentities_116_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_managedidentities_117_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "ResetAdminPasswordRequestIn": "_managedidentities_118_ResetAdminPasswordRequestIn",
        "ResetAdminPasswordRequestOut": "_managedidentities_119_ResetAdminPasswordRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LDAPSSettingsIn"] = t.struct(
        {
            "certificatePassword": t.string().optional(),
            "certificatePfx": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LDAPSSettingsIn"])
    types["LDAPSSettingsOut"] = t.struct(
        {
            "certificatePassword": t.string().optional(),
            "state": t.string().optional(),
            "certificatePfx": t.string().optional(),
            "certificate": t.proxy(renames["CertificateOut"]).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LDAPSSettingsOut"])
    types["ScheduleIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "day": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
                    ]
                )
            ).optional(),
            "tier": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
                    ]
                )
            ).optional(),
            "tier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"])
    types["DomainIn"] = t.struct(
        {
            "authorizedNetworks": t.array(t.string()).optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservedIpRange": t.string(),
            "name": t.string(),
            "locations": t.array(t.string()),
            "admin": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "authorizedNetworks": t.array(t.string()).optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "fqdn": t.string().optional(),
            "reservedIpRange": t.string(),
            "trusts": t.array(t.proxy(renames["TrustOut"])).optional(),
            "name": t.string(),
            "locations": t.array(t.string()),
            "updateTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "admin": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["RestoreDomainRequestIn"] = t.struct({"backupId": t.string()}).named(
        renames["RestoreDomainRequestIn"]
    )
    types["RestoreDomainRequestOut"] = t.struct(
        {"backupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreDomainRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GoogleCloudManagedidentitiesV1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1OpMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataOut"])
    types["ValidateTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["ValidateTrustRequestIn"])
    types["ValidateTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateTrustRequestOut"])
    types["DailyCycleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["DailyCycleIn"])
    types["DailyCycleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyCycleOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn"
    ] = t.struct({"values": t.array(t.string()).optional()}).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn"
        ]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut"
    ] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut"
        ]
    )
    types["AttachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["AttachTrustRequestIn"])
    types["AttachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTrustRequestOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "seconds": t.integer().optional(),
            "nanos": t.integer().optional(),
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PeeringIn"] = t.struct(
        {
            "domainResource": t.string(),
            "authorizedNetwork": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PeeringIn"])
    types["PeeringOut"] = t.struct(
        {
            "domainResource": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "authorizedNetwork": t.string(),
            "statusMessage": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeringOut"])
    types["TrustIn"] = t.struct(
        {
            "targetDnsIpAddresses": t.array(t.string()),
            "trustDirection": t.string(),
            "selectiveAuthentication": t.boolean().optional(),
            "trustType": t.string(),
            "trustHandshakeSecret": t.string(),
            "targetDomainName": t.string(),
        }
    ).named(renames["TrustIn"])
    types["TrustOut"] = t.struct(
        {
            "targetDnsIpAddresses": t.array(t.string()),
            "lastTrustHeartbeatTime": t.string().optional(),
            "createTime": t.string().optional(),
            "trustDirection": t.string(),
            "updateTime": t.string().optional(),
            "selectiveAuthentication": t.boolean().optional(),
            "trustType": t.string(),
            "stateDescription": t.string().optional(),
            "state": t.string().optional(),
            "trustHandshakeSecret": t.string(),
            "targetDomainName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustOut"])
    types["SqlIntegrationIn"] = t.struct(
        {"sqlInstance": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SqlIntegrationIn"])
    types["SqlIntegrationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "sqlInstance": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIntegrationOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"] = t.struct(
        {"reason": t.string().optional(), "eligible": t.boolean().optional()}
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"
    ] = t.struct(
        {
            "reason": t.string().optional(),
            "eligible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut"]
    )
    types["DisableMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DisableMigrationRequestIn"]
    )
    types["DisableMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableMigrationRequestOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"
    ] = t.struct(
        {"resourceType": t.string().optional(), "resourceUrl": t.string().optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
    ] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"]
    )
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
    types["OnPremDomainDetailsIn"] = t.struct(
        {"domainName": t.string(), "disableSidFiltering": t.boolean().optional()}
    ).named(renames["OnPremDomainDetailsIn"])
    types["OnPremDomainDetailsOut"] = t.struct(
        {
            "domainName": t.string(),
            "disableSidFiltering": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremDomainDetailsOut"])
    types["DetachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["DetachTrustRequestIn"])
    types["DetachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachTrustRequestOut"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"])
    types["CertificateIn"] = t.struct(
        {
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "issuingCertificate": t.proxy(renames["CertificateIn"]).optional(),
            "subject": t.string().optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "issuingCertificate": t.proxy(renames["CertificateOut"]).optional(),
            "subject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ResetAdminPasswordResponseIn"] = t.struct(
        {"password": t.string().optional()}
    ).named(renames["ResetAdminPasswordResponseIn"])
    types["ResetAdminPasswordResponseOut"] = t.struct(
        {
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetAdminPasswordResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["BackupIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["DomainJoinMachineRequestIn"] = t.struct(
        {
            "ouName": t.string().optional(),
            "force": t.boolean().optional(),
            "vmIdToken": t.string(),
        }
    ).named(renames["DomainJoinMachineRequestIn"])
    types["DomainJoinMachineRequestOut"] = t.struct(
        {
            "ouName": t.string().optional(),
            "force": t.boolean().optional(),
            "vmIdToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineRequestOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "isRollback": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
    )
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ExtendSchemaRequestIn"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "description": t.string(),
            "fileContents": t.string().optional(),
        }
    ).named(renames["ExtendSchemaRequestIn"])
    types["ExtendSchemaRequestOut"] = t.struct(
        {
            "gcsPath": t.string().optional(),
            "description": t.string(),
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendSchemaRequestOut"])
    types["ReconfigureTrustRequestIn"] = t.struct(
        {"targetDomainName": t.string(), "targetDnsIpAddresses": t.array(t.string())}
    ).named(renames["ReconfigureTrustRequestIn"])
    types["ReconfigureTrustRequestOut"] = t.struct(
        {
            "targetDomainName": t.string(),
            "targetDnsIpAddresses": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReconfigureTrustRequestOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "channel": t.string().optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["EnableMigrationRequestIn"] = t.struct(
        {"migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsIn"]))}
    ).named(renames["EnableMigrationRequestIn"])
    types["EnableMigrationRequestOut"] = t.struct(
        {
            "migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableMigrationRequestOut"])
    types["ListSqlIntegrationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sqlIntegrations": t.array(t.proxy(renames["SqlIntegrationIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListSqlIntegrationsResponseIn"])
    types["ListSqlIntegrationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sqlIntegrations": t.array(
                t.proxy(renames["SqlIntegrationOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSqlIntegrationsResponseOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "nodeId": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
    ] = t.struct(
        {"eligibilities": t.struct({"_": t.string().optional()}).optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
    ] = t.struct(
        {
            "eligibilities": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
        ]
    )
    types["ListPeeringsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "peerings": t.array(t.proxy(renames["PeeringIn"])).optional(),
        }
    ).named(renames["ListPeeringsResponseIn"])
    types["ListPeeringsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "peerings": t.array(t.proxy(renames["PeeringOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPeeringsResponseOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["ListDomainsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
        }
    ).named(renames["ListDomainsResponseIn"])
    types["ListDomainsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DomainJoinMachineResponseIn"] = t.struct(
        {"domainJoinBlob": t.string().optional()}
    ).named(renames["DomainJoinMachineResponseIn"])
    types["DomainJoinMachineResponseOut"] = t.struct(
        {
            "domainJoinBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "dailyCycle": t.proxy(renames["DailyCycleIn"]).optional(),
            "weeklyCycle": t.proxy(renames["WeeklyCycleIn"]).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "dailyCycle": t.proxy(renames["DailyCycleOut"]).optional(),
            "weeklyCycle": t.proxy(renames["WeeklyCycleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "slmInstanceTemplate": t.string().optional(),
            "instanceType": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "slmInstanceTemplate": t.string().optional(),
            "createTime": t.string().optional(),
            "instanceType": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "tenantProjectId": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["ResetAdminPasswordRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetAdminPasswordRequestIn"]
    )
    types["ResetAdminPasswordRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAdminPasswordRequestOut"])

    functions = {}
    functions["projectsLocationsGet"] = managedidentities.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = managedidentities.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsDelete"] = managedidentities.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsGet"] = managedidentities.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsCancel"] = managedidentities.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsList"] = managedidentities.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsList"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsPatch"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsCreate"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsDelete"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsGetIamPolicy"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPeeringsTestIamPermissions"
    ] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsGet"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsSetIamPolicy"] = managedidentities.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsTestIamPermissions"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsExtendSchema"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsReconfigureTrust"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsList"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDelete"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsSetIamPolicy"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsGetLdapssettings"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsResetAdminPassword"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsEnableMigration"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsPatch"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsRestore"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsDisableMigration"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsCreate"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsDomainJoinMachine"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsValidateTrust"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDetachTrust"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGetIamPolicy"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsUpdateLdapssettings"
    ] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGet"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsAttachTrust"] = managedidentities.post(
        "v1/{name}:attachTrust",
        t.struct(
            {
                "name": t.string(),
                "trust": t.proxy(renames["TrustIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsSqlIntegrationsList"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SqlIntegrationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsSqlIntegrationsGet"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SqlIntegrationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsGetIamPolicy"
    ] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsList"] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsSetIamPolicy"
    ] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsPatch"] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsDelete"] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsGet"] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsTestIamPermissions"
    ] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsCreate"] = managedidentities.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "parent": t.string(),
                "backupId": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="managedidentities",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
