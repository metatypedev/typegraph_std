from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_managedidentities() -> Import:
    managedidentities = HTTPRuntime("https://managedidentities.googleapis.com/")

    renames = {
        "ErrorResponse": "_managedidentities_1_ErrorResponse",
        "DailyCycleIn": "_managedidentities_2_DailyCycleIn",
        "DailyCycleOut": "_managedidentities_3_DailyCycleOut",
        "LDAPSSettingsIn": "_managedidentities_4_LDAPSSettingsIn",
        "LDAPSSettingsOut": "_managedidentities_5_LDAPSSettingsOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_managedidentities_6_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_managedidentities_7_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "StatusIn": "_managedidentities_8_StatusIn",
        "StatusOut": "_managedidentities_9_StatusOut",
        "SqlIntegrationIn": "_managedidentities_10_SqlIntegrationIn",
        "SqlIntegrationOut": "_managedidentities_11_SqlIntegrationOut",
        "RestoreDomainRequestIn": "_managedidentities_12_RestoreDomainRequestIn",
        "RestoreDomainRequestOut": "_managedidentities_13_RestoreDomainRequestOut",
        "ScheduleIn": "_managedidentities_14_ScheduleIn",
        "ScheduleOut": "_managedidentities_15_ScheduleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_managedidentities_16_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_managedidentities_17_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "EmptyIn": "_managedidentities_18_EmptyIn",
        "EmptyOut": "_managedidentities_19_EmptyOut",
        "PeeringIn": "_managedidentities_20_PeeringIn",
        "PeeringOut": "_managedidentities_21_PeeringOut",
        "DisableMigrationRequestIn": "_managedidentities_22_DisableMigrationRequestIn",
        "DisableMigrationRequestOut": "_managedidentities_23_DisableMigrationRequestOut",
        "DomainJoinMachineResponseIn": "_managedidentities_24_DomainJoinMachineResponseIn",
        "DomainJoinMachineResponseOut": "_managedidentities_25_DomainJoinMachineResponseOut",
        "CancelOperationRequestIn": "_managedidentities_26_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_managedidentities_27_CancelOperationRequestOut",
        "OnPremDomainDetailsIn": "_managedidentities_28_OnPremDomainDetailsIn",
        "OnPremDomainDetailsOut": "_managedidentities_29_OnPremDomainDetailsOut",
        "EnableMigrationRequestIn": "_managedidentities_30_EnableMigrationRequestIn",
        "EnableMigrationRequestOut": "_managedidentities_31_EnableMigrationRequestOut",
        "CertificateIn": "_managedidentities_32_CertificateIn",
        "CertificateOut": "_managedidentities_33_CertificateOut",
        "LocationIn": "_managedidentities_34_LocationIn",
        "LocationOut": "_managedidentities_35_LocationOut",
        "DetachTrustRequestIn": "_managedidentities_36_DetachTrustRequestIn",
        "DetachTrustRequestOut": "_managedidentities_37_DetachTrustRequestOut",
        "UpdatePolicyIn": "_managedidentities_38_UpdatePolicyIn",
        "UpdatePolicyOut": "_managedidentities_39_UpdatePolicyOut",
        "OperationIn": "_managedidentities_40_OperationIn",
        "OperationOut": "_managedidentities_41_OperationOut",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataIn": "_managedidentities_42_GoogleCloudManagedidentitiesV1alpha1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataOut": "_managedidentities_43_GoogleCloudManagedidentitiesV1alpha1OpMetadataOut",
        "TestIamPermissionsResponseIn": "_managedidentities_44_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_managedidentities_45_TestIamPermissionsResponseOut",
        "GoogleCloudManagedidentitiesV1OpMetadataIn": "_managedidentities_46_GoogleCloudManagedidentitiesV1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1OpMetadataOut": "_managedidentities_47_GoogleCloudManagedidentitiesV1OpMetadataOut",
        "BackupIn": "_managedidentities_48_BackupIn",
        "BackupOut": "_managedidentities_49_BackupOut",
        "TestIamPermissionsRequestIn": "_managedidentities_50_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_managedidentities_51_TestIamPermissionsRequestOut",
        "ExprIn": "_managedidentities_52_ExprIn",
        "ExprOut": "_managedidentities_53_ExprOut",
        "WeeklyCycleIn": "_managedidentities_54_WeeklyCycleIn",
        "WeeklyCycleOut": "_managedidentities_55_WeeklyCycleOut",
        "AttachTrustRequestIn": "_managedidentities_56_AttachTrustRequestIn",
        "AttachTrustRequestOut": "_managedidentities_57_AttachTrustRequestOut",
        "SetIamPolicyRequestIn": "_managedidentities_58_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_managedidentities_59_SetIamPolicyRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_managedidentities_60_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_managedidentities_61_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "ListLocationsResponseIn": "_managedidentities_62_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_managedidentities_63_ListLocationsResponseOut",
        "DomainIn": "_managedidentities_64_DomainIn",
        "DomainOut": "_managedidentities_65_DomainOut",
        "TimeOfDayIn": "_managedidentities_66_TimeOfDayIn",
        "TimeOfDayOut": "_managedidentities_67_TimeOfDayOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_managedidentities_68_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_managedidentities_69_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "ListDomainsResponseIn": "_managedidentities_70_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_managedidentities_71_ListDomainsResponseOut",
        "ReconfigureTrustRequestIn": "_managedidentities_72_ReconfigureTrustRequestIn",
        "ReconfigureTrustRequestOut": "_managedidentities_73_ReconfigureTrustRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_managedidentities_74_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_managedidentities_75_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "ListPeeringsResponseIn": "_managedidentities_76_ListPeeringsResponseIn",
        "ListPeeringsResponseOut": "_managedidentities_77_ListPeeringsResponseOut",
        "ResetAdminPasswordResponseIn": "_managedidentities_78_ResetAdminPasswordResponseIn",
        "ResetAdminPasswordResponseOut": "_managedidentities_79_ResetAdminPasswordResponseOut",
        "ListSqlIntegrationsResponseIn": "_managedidentities_80_ListSqlIntegrationsResponseIn",
        "ListSqlIntegrationsResponseOut": "_managedidentities_81_ListSqlIntegrationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_managedidentities_82_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_managedidentities_83_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "ListBackupsResponseIn": "_managedidentities_84_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_managedidentities_85_ListBackupsResponseOut",
        "ExtendSchemaRequestIn": "_managedidentities_86_ExtendSchemaRequestIn",
        "ExtendSchemaRequestOut": "_managedidentities_87_ExtendSchemaRequestOut",
        "PolicyIn": "_managedidentities_88_PolicyIn",
        "PolicyOut": "_managedidentities_89_PolicyOut",
        "DateIn": "_managedidentities_90_DateIn",
        "DateOut": "_managedidentities_91_DateOut",
        "ValidateTrustRequestIn": "_managedidentities_92_ValidateTrustRequestIn",
        "ValidateTrustRequestOut": "_managedidentities_93_ValidateTrustRequestOut",
        "DenyMaintenancePeriodIn": "_managedidentities_94_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_managedidentities_95_DenyMaintenancePeriodOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_managedidentities_96_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_managedidentities_97_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_managedidentities_98_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_managedidentities_99_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "ResetAdminPasswordRequestIn": "_managedidentities_100_ResetAdminPasswordRequestIn",
        "ResetAdminPasswordRequestOut": "_managedidentities_101_ResetAdminPasswordRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_managedidentities_102_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_managedidentities_103_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "ListOperationsResponseIn": "_managedidentities_104_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_managedidentities_105_ListOperationsResponseOut",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataIn": "_managedidentities_106_GoogleCloudManagedidentitiesV1beta1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataOut": "_managedidentities_107_GoogleCloudManagedidentitiesV1beta1OpMetadataOut",
        "BindingIn": "_managedidentities_108_BindingIn",
        "BindingOut": "_managedidentities_109_BindingOut",
        "OperationMetadataIn": "_managedidentities_110_OperationMetadataIn",
        "OperationMetadataOut": "_managedidentities_111_OperationMetadataOut",
        "MaintenancePolicyIn": "_managedidentities_112_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_managedidentities_113_MaintenancePolicyOut",
        "MaintenanceWindowIn": "_managedidentities_114_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_managedidentities_115_MaintenanceWindowOut",
        "DomainJoinMachineRequestIn": "_managedidentities_116_DomainJoinMachineRequestIn",
        "DomainJoinMachineRequestOut": "_managedidentities_117_DomainJoinMachineRequestOut",
        "TrustIn": "_managedidentities_118_TrustIn",
        "TrustOut": "_managedidentities_119_TrustOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LDAPSSettingsIn"] = t.struct(
        {
            "certificatePfx": t.string().optional(),
            "name": t.string().optional(),
            "certificatePassword": t.string().optional(),
        }
    ).named(renames["LDAPSSettingsIn"])
    types["LDAPSSettingsOut"] = t.struct(
        {
            "certificatePfx": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "certificatePassword": t.string().optional(),
            "certificate": t.proxy(renames["CertificateOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LDAPSSettingsOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["SqlIntegrationIn"] = t.struct(
        {"name": t.string().optional(), "sqlInstance": t.string().optional()}
    ).named(renames["SqlIntegrationIn"])
    types["SqlIntegrationOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "sqlInstance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIntegrationOut"])
    types["RestoreDomainRequestIn"] = t.struct({"backupId": t.string()}).named(
        renames["RestoreDomainRequestIn"]
    )
    types["RestoreDomainRequestOut"] = t.struct(
        {"backupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreDomainRequestOut"])
    types["ScheduleIn"] = t.struct(
        {
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PeeringIn"] = t.struct(
        {
            "domainResource": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "authorizedNetwork": t.string(),
        }
    ).named(renames["PeeringIn"])
    types["PeeringOut"] = t.struct(
        {
            "domainResource": t.string(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "statusMessage": t.string().optional(),
            "state": t.string().optional(),
            "authorizedNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeringOut"])
    types["DisableMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DisableMigrationRequestIn"]
    )
    types["DisableMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableMigrationRequestOut"])
    types["DomainJoinMachineResponseIn"] = t.struct(
        {"domainJoinBlob": t.string().optional()}
    ).named(renames["DomainJoinMachineResponseIn"])
    types["DomainJoinMachineResponseOut"] = t.struct(
        {
            "domainJoinBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["EnableMigrationRequestIn"] = t.struct(
        {"migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsIn"]))}
    ).named(renames["EnableMigrationRequestIn"])
    types["EnableMigrationRequestOut"] = t.struct(
        {
            "migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableMigrationRequestOut"])
    types["CertificateIn"] = t.struct(
        {
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "issuingCertificate": t.proxy(renames["CertificateIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "issuingCertificate": t.proxy(renames["CertificateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DetachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["DetachTrustRequestIn"])
    types["DetachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachTrustRequestOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudManagedidentitiesV1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1OpMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataOut"])
    types["BackupIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "statusMessage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["AttachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["AttachTrustRequestIn"])
    types["AttachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTrustRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["DomainIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "auditLogsEnabled": t.boolean().optional(),
            "reservedIpRange": t.string(),
            "admin": t.string().optional(),
            "authorizedNetworks": t.array(t.string()).optional(),
            "locations": t.array(t.string()),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "auditLogsEnabled": t.boolean().optional(),
            "reservedIpRange": t.string(),
            "fqdn": t.string().optional(),
            "statusMessage": t.string().optional(),
            "admin": t.string().optional(),
            "authorizedNetworks": t.array(t.string()).optional(),
            "locations": t.array(t.string()),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "trusts": t.array(t.proxy(renames["TrustOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "location": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
    )
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
    types["ReconfigureTrustRequestIn"] = t.struct(
        {"targetDnsIpAddresses": t.array(t.string()), "targetDomainName": t.string()}
    ).named(renames["ReconfigureTrustRequestIn"])
    types["ReconfigureTrustRequestOut"] = t.struct(
        {
            "targetDnsIpAddresses": t.array(t.string()),
            "targetDomainName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReconfigureTrustRequestOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "startTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["ListPeeringsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "peerings": t.array(t.proxy(renames["PeeringIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPeeringsResponseIn"])
    types["ListPeeringsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "peerings": t.array(t.proxy(renames["PeeringOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPeeringsResponseOut"])
    types["ResetAdminPasswordResponseIn"] = t.struct(
        {"password": t.string().optional()}
    ).named(renames["ResetAdminPasswordResponseIn"])
    types["ResetAdminPasswordResponseOut"] = t.struct(
        {
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetAdminPasswordResponseOut"])
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
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
            "name": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "state": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "tenantProjectId": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "instanceType": t.string().optional(),
            "name": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "createTime": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["ExtendSchemaRequestIn"] = t.struct(
        {
            "description": t.string(),
            "fileContents": t.string().optional(),
            "gcsPath": t.string().optional(),
        }
    ).named(renames["ExtendSchemaRequestIn"])
    types["ExtendSchemaRequestOut"] = t.struct(
        {
            "description": t.string(),
            "fileContents": t.string().optional(),
            "gcsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendSchemaRequestOut"])
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
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ValidateTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["ValidateTrustRequestIn"])
    types["ValidateTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateTrustRequestOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "isRollback": t.boolean().optional(),
            "exclude": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "isRollback": t.boolean().optional(),
            "exclude": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
    )
    types["ResetAdminPasswordRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetAdminPasswordRequestIn"]
    )
    types["ResetAdminPasswordRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAdminPasswordRequestOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
                    ]
                )
            ).optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "tier": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"] = t.struct(
        {
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
                    ]
                )
            ).optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "tier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
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
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "weeklyCycle": t.proxy(renames["WeeklyCycleIn"]).optional(),
            "dailyCycle": t.proxy(renames["DailyCycleIn"]).optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "weeklyCycle": t.proxy(renames["WeeklyCycleOut"]).optional(),
            "dailyCycle": t.proxy(renames["DailyCycleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["DomainJoinMachineRequestIn"] = t.struct(
        {
            "vmIdToken": t.string(),
            "force": t.boolean().optional(),
            "ouName": t.string().optional(),
        }
    ).named(renames["DomainJoinMachineRequestIn"])
    types["DomainJoinMachineRequestOut"] = t.struct(
        {
            "vmIdToken": t.string(),
            "force": t.boolean().optional(),
            "ouName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineRequestOut"])
    types["TrustIn"] = t.struct(
        {
            "trustType": t.string(),
            "trustDirection": t.string(),
            "selectiveAuthentication": t.boolean().optional(),
            "targetDomainName": t.string(),
            "targetDnsIpAddresses": t.array(t.string()),
            "trustHandshakeSecret": t.string(),
        }
    ).named(renames["TrustIn"])
    types["TrustOut"] = t.struct(
        {
            "lastTrustHeartbeatTime": t.string().optional(),
            "state": t.string().optional(),
            "trustType": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "trustDirection": t.string(),
            "selectiveAuthentication": t.boolean().optional(),
            "stateDescription": t.string().optional(),
            "targetDomainName": t.string(),
            "targetDnsIpAddresses": t.array(t.string()),
            "trustHandshakeSecret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustOut"])

    functions = {}
    functions["projectsLocationsList"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsList"] = managedidentities.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsGet"] = managedidentities.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsDelete"] = managedidentities.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalOperationsCancel"] = managedidentities.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsTestIamPermissions"
    ] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGetIamPolicy"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGet"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsAttachTrust"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDetachTrust"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsSetIamPolicy"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDelete"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsValidateTrust"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsExtendSchema"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsList"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsPatch"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsRestore"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsEnableMigration"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsCreate"] = managedidentities.post(
        "v1/{parent}/domains",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string(),
                "auditLogsEnabled": t.boolean().optional(),
                "reservedIpRange": t.string(),
                "admin": t.string().optional(),
                "authorizedNetworks": t.array(t.string()).optional(),
                "locations": t.array(t.string()),
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
    functions["projectsLocationsGlobalDomainsBackupsCreate"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsPatch"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsTestIamPermissions"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsGetIamPolicy"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsSetIamPolicy"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsList"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsDelete"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsGet"] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
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

    return Import(
        importer="managedidentities",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
