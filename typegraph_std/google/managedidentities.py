from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_managedidentities() -> Import:
    managedidentities = HTTPRuntime("https://managedidentities.googleapis.com/")

    renames = {
        "ErrorResponse": "_managedidentities_1_ErrorResponse",
        "MaintenancePolicyIn": "_managedidentities_2_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_managedidentities_3_MaintenancePolicyOut",
        "OperationMetadataIn": "_managedidentities_4_OperationMetadataIn",
        "OperationMetadataOut": "_managedidentities_5_OperationMetadataOut",
        "ExprIn": "_managedidentities_6_ExprIn",
        "ExprOut": "_managedidentities_7_ExprOut",
        "SqlIntegrationIn": "_managedidentities_8_SqlIntegrationIn",
        "SqlIntegrationOut": "_managedidentities_9_SqlIntegrationOut",
        "ListPeeringsResponseIn": "_managedidentities_10_ListPeeringsResponseIn",
        "ListPeeringsResponseOut": "_managedidentities_11_ListPeeringsResponseOut",
        "ResetAdminPasswordRequestIn": "_managedidentities_12_ResetAdminPasswordRequestIn",
        "ResetAdminPasswordRequestOut": "_managedidentities_13_ResetAdminPasswordRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_managedidentities_14_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_managedidentities_15_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "TestIamPermissionsRequestIn": "_managedidentities_16_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_managedidentities_17_TestIamPermissionsRequestOut",
        "PeeringIn": "_managedidentities_18_PeeringIn",
        "PeeringOut": "_managedidentities_19_PeeringOut",
        "CertificateIn": "_managedidentities_20_CertificateIn",
        "CertificateOut": "_managedidentities_21_CertificateOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_managedidentities_22_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_managedidentities_23_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "DomainJoinMachineResponseIn": "_managedidentities_24_DomainJoinMachineResponseIn",
        "DomainJoinMachineResponseOut": "_managedidentities_25_DomainJoinMachineResponseOut",
        "EnableMigrationRequestIn": "_managedidentities_26_EnableMigrationRequestIn",
        "EnableMigrationRequestOut": "_managedidentities_27_EnableMigrationRequestOut",
        "OperationIn": "_managedidentities_28_OperationIn",
        "OperationOut": "_managedidentities_29_OperationOut",
        "ReconfigureTrustRequestIn": "_managedidentities_30_ReconfigureTrustRequestIn",
        "ReconfigureTrustRequestOut": "_managedidentities_31_ReconfigureTrustRequestOut",
        "ScheduleIn": "_managedidentities_32_ScheduleIn",
        "ScheduleOut": "_managedidentities_33_ScheduleOut",
        "ValidateTrustRequestIn": "_managedidentities_34_ValidateTrustRequestIn",
        "ValidateTrustRequestOut": "_managedidentities_35_ValidateTrustRequestOut",
        "BindingIn": "_managedidentities_36_BindingIn",
        "BindingOut": "_managedidentities_37_BindingOut",
        "ListOperationsResponseIn": "_managedidentities_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_managedidentities_39_ListOperationsResponseOut",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataIn": "_managedidentities_40_GoogleCloudManagedidentitiesV1alpha1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataOut": "_managedidentities_41_GoogleCloudManagedidentitiesV1alpha1OpMetadataOut",
        "EmptyIn": "_managedidentities_42_EmptyIn",
        "EmptyOut": "_managedidentities_43_EmptyOut",
        "ListLocationsResponseIn": "_managedidentities_44_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_managedidentities_45_ListLocationsResponseOut",
        "OnPremDomainDetailsIn": "_managedidentities_46_OnPremDomainDetailsIn",
        "OnPremDomainDetailsOut": "_managedidentities_47_OnPremDomainDetailsOut",
        "ExtendSchemaRequestIn": "_managedidentities_48_ExtendSchemaRequestIn",
        "ExtendSchemaRequestOut": "_managedidentities_49_ExtendSchemaRequestOut",
        "TrustIn": "_managedidentities_50_TrustIn",
        "TrustOut": "_managedidentities_51_TrustOut",
        "ListSqlIntegrationsResponseIn": "_managedidentities_52_ListSqlIntegrationsResponseIn",
        "ListSqlIntegrationsResponseOut": "_managedidentities_53_ListSqlIntegrationsResponseOut",
        "WeeklyCycleIn": "_managedidentities_54_WeeklyCycleIn",
        "WeeklyCycleOut": "_managedidentities_55_WeeklyCycleOut",
        "DenyMaintenancePeriodIn": "_managedidentities_56_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_managedidentities_57_DenyMaintenancePeriodOut",
        "DomainJoinMachineRequestIn": "_managedidentities_58_DomainJoinMachineRequestIn",
        "DomainJoinMachineRequestOut": "_managedidentities_59_DomainJoinMachineRequestOut",
        "DomainIn": "_managedidentities_60_DomainIn",
        "DomainOut": "_managedidentities_61_DomainOut",
        "LocationIn": "_managedidentities_62_LocationIn",
        "LocationOut": "_managedidentities_63_LocationOut",
        "TimeOfDayIn": "_managedidentities_64_TimeOfDayIn",
        "TimeOfDayOut": "_managedidentities_65_TimeOfDayOut",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataIn": "_managedidentities_66_GoogleCloudManagedidentitiesV1beta1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataOut": "_managedidentities_67_GoogleCloudManagedidentitiesV1beta1OpMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_managedidentities_68_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_managedidentities_69_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "MaintenanceWindowIn": "_managedidentities_70_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_managedidentities_71_MaintenanceWindowOut",
        "DateIn": "_managedidentities_72_DateIn",
        "DateOut": "_managedidentities_73_DateOut",
        "DetachTrustRequestIn": "_managedidentities_74_DetachTrustRequestIn",
        "DetachTrustRequestOut": "_managedidentities_75_DetachTrustRequestOut",
        "DailyCycleIn": "_managedidentities_76_DailyCycleIn",
        "DailyCycleOut": "_managedidentities_77_DailyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_managedidentities_78_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_managedidentities_79_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "PolicyIn": "_managedidentities_80_PolicyIn",
        "PolicyOut": "_managedidentities_81_PolicyOut",
        "AttachTrustRequestIn": "_managedidentities_82_AttachTrustRequestIn",
        "AttachTrustRequestOut": "_managedidentities_83_AttachTrustRequestOut",
        "StatusIn": "_managedidentities_84_StatusIn",
        "StatusOut": "_managedidentities_85_StatusOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_managedidentities_86_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_managedidentities_87_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_managedidentities_88_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_managedidentities_89_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "ListDomainsResponseIn": "_managedidentities_90_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_managedidentities_91_ListDomainsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_managedidentities_92_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_managedidentities_93_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "ListBackupsResponseIn": "_managedidentities_94_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_managedidentities_95_ListBackupsResponseOut",
        "BackupIn": "_managedidentities_96_BackupIn",
        "BackupOut": "_managedidentities_97_BackupOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_managedidentities_98_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_managedidentities_99_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "ResetAdminPasswordResponseIn": "_managedidentities_100_ResetAdminPasswordResponseIn",
        "ResetAdminPasswordResponseOut": "_managedidentities_101_ResetAdminPasswordResponseOut",
        "TestIamPermissionsResponseIn": "_managedidentities_102_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_managedidentities_103_TestIamPermissionsResponseOut",
        "UpdatePolicyIn": "_managedidentities_104_UpdatePolicyIn",
        "UpdatePolicyOut": "_managedidentities_105_UpdatePolicyOut",
        "SetIamPolicyRequestIn": "_managedidentities_106_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_managedidentities_107_SetIamPolicyRequestOut",
        "CancelOperationRequestIn": "_managedidentities_108_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_managedidentities_109_CancelOperationRequestOut",
        "GoogleCloudManagedidentitiesV1OpMetadataIn": "_managedidentities_110_GoogleCloudManagedidentitiesV1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1OpMetadataOut": "_managedidentities_111_GoogleCloudManagedidentitiesV1OpMetadataOut",
        "DisableMigrationRequestIn": "_managedidentities_112_DisableMigrationRequestIn",
        "DisableMigrationRequestOut": "_managedidentities_113_DisableMigrationRequestOut",
        "LDAPSSettingsIn": "_managedidentities_114_LDAPSSettingsIn",
        "LDAPSSettingsOut": "_managedidentities_115_LDAPSSettingsOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_managedidentities_116_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_managedidentities_117_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "RestoreDomainRequestIn": "_managedidentities_118_RestoreDomainRequestIn",
        "RestoreDomainRequestOut": "_managedidentities_119_RestoreDomainRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SqlIntegrationIn"] = t.struct(
        {"sqlInstance": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SqlIntegrationIn"])
    types["SqlIntegrationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "sqlInstance": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIntegrationOut"])
    types["ListPeeringsResponseIn"] = t.struct(
        {
            "peerings": t.array(t.proxy(renames["PeeringIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListPeeringsResponseIn"])
    types["ListPeeringsResponseOut"] = t.struct(
        {
            "peerings": t.array(t.proxy(renames["PeeringOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPeeringsResponseOut"])
    types["ResetAdminPasswordRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetAdminPasswordRequestIn"]
    )
    types["ResetAdminPasswordRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAdminPasswordRequestOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"
    ] = t.struct(
        {
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut"]
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
    types["PeeringIn"] = t.struct(
        {
            "domainResource": t.string(),
            "authorizedNetwork": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PeeringIn"])
    types["PeeringOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "domainResource": t.string(),
            "name": t.string().optional(),
            "authorizedNetwork": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeringOut"])
    types["CertificateIn"] = t.struct(
        {
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "issuingCertificate": t.proxy(renames["CertificateIn"]).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "issuingCertificate": t.proxy(renames["CertificateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "startTime": t.string().optional(),
            "scheduleDeadlineTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
    types["DomainJoinMachineResponseIn"] = t.struct(
        {"domainJoinBlob": t.string().optional()}
    ).named(renames["DomainJoinMachineResponseIn"])
    types["DomainJoinMachineResponseOut"] = t.struct(
        {
            "domainJoinBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineResponseOut"])
    types["EnableMigrationRequestIn"] = t.struct(
        {"migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsIn"]))}
    ).named(renames["EnableMigrationRequestIn"])
    types["EnableMigrationRequestOut"] = t.struct(
        {
            "migratingDomains": t.array(t.proxy(renames["OnPremDomainDetailsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableMigrationRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ScheduleIn"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
            "day": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "day": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["ValidateTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["ValidateTrustRequestIn"])
    types["ValidateTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateTrustRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["OnPremDomainDetailsIn"] = t.struct(
        {"disableSidFiltering": t.boolean().optional(), "domainName": t.string()}
    ).named(renames["OnPremDomainDetailsIn"])
    types["OnPremDomainDetailsOut"] = t.struct(
        {
            "disableSidFiltering": t.boolean().optional(),
            "domainName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnPremDomainDetailsOut"])
    types["ExtendSchemaRequestIn"] = t.struct(
        {
            "description": t.string(),
            "gcsPath": t.string().optional(),
            "fileContents": t.string().optional(),
        }
    ).named(renames["ExtendSchemaRequestIn"])
    types["ExtendSchemaRequestOut"] = t.struct(
        {
            "description": t.string(),
            "gcsPath": t.string().optional(),
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendSchemaRequestOut"])
    types["TrustIn"] = t.struct(
        {
            "trustHandshakeSecret": t.string(),
            "trustDirection": t.string(),
            "trustType": t.string(),
            "targetDomainName": t.string(),
            "selectiveAuthentication": t.boolean().optional(),
            "targetDnsIpAddresses": t.array(t.string()),
        }
    ).named(renames["TrustIn"])
    types["TrustOut"] = t.struct(
        {
            "stateDescription": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "trustHandshakeSecret": t.string(),
            "trustDirection": t.string(),
            "lastTrustHeartbeatTime": t.string().optional(),
            "trustType": t.string(),
            "state": t.string().optional(),
            "targetDomainName": t.string(),
            "selectiveAuthentication": t.boolean().optional(),
            "targetDnsIpAddresses": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustOut"])
    types["ListSqlIntegrationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "sqlIntegrations": t.array(t.proxy(renames["SqlIntegrationIn"])).optional(),
        }
    ).named(renames["ListSqlIntegrationsResponseIn"])
    types["ListSqlIntegrationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "sqlIntegrations": t.array(
                t.proxy(renames["SqlIntegrationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSqlIntegrationsResponseOut"])
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["DomainJoinMachineRequestIn"] = t.struct(
        {
            "force": t.boolean().optional(),
            "vmIdToken": t.string(),
            "ouName": t.string().optional(),
        }
    ).named(renames["DomainJoinMachineRequestIn"])
    types["DomainJoinMachineRequestOut"] = t.struct(
        {
            "force": t.boolean().optional(),
            "vmIdToken": t.string(),
            "ouName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineRequestOut"])
    types["DomainIn"] = t.struct(
        {
            "authorizedNetworks": t.array(t.string()).optional(),
            "admin": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "reservedIpRange": t.string(),
            "name": t.string(),
            "locations": t.array(t.string()),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "authorizedNetworks": t.array(t.string()).optional(),
            "admin": t.string().optional(),
            "statusMessage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "reservedIpRange": t.string(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "fqdn": t.string().optional(),
            "updateTime": t.string().optional(),
            "locations": t.array(t.string()),
            "trusts": t.array(t.proxy(renames["TrustOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"])
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
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["DetachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["DetachTrustRequestIn"])
    types["DetachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachTrustRequestOut"])
    types["DailyCycleIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayIn"]).optional(),
        }
    ).named(renames["DailyCycleIn"])
    types["DailyCycleOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "startTime": t.proxy(renames["TimeOfDayOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DailyCycleOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "consumerDefinedName": t.string().optional(),
            "name": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "consumerDefinedName": t.string().optional(),
            "name": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "instanceType": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
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
    types["AttachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["AttachTrustRequestIn"])
    types["AttachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTrustRequestOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "isRollback": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
    ] = t.struct(
        {
            "exclude": t.boolean().optional(),
            "maintenancePolicies": t.struct({"_": t.string().optional()}).optional(),
            "isRollback": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"]
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
    types["ListDomainsResponseIn"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListDomainsResponseIn"])
    types["ListDomainsResponseOut"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainsResponseOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"
    ] = t.struct(
        {"resourceUrl": t.string().optional(), "resourceType": t.string().optional()}
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
    ] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"]
    )
    types["ListBackupsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["BackupIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "statusMessage": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["ResetAdminPasswordResponseIn"] = t.struct(
        {"password": t.string().optional()}
    ).named(renames["ResetAdminPasswordResponseIn"])
    types["ResetAdminPasswordResponseOut"] = t.struct(
        {
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetAdminPasswordResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "channel": t.string().optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["GoogleCloudManagedidentitiesV1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1OpMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataOut"])
    types["DisableMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DisableMigrationRequestIn"]
    )
    types["DisableMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableMigrationRequestOut"])
    types["LDAPSSettingsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "certificatePassword": t.string().optional(),
            "certificatePfx": t.string().optional(),
        }
    ).named(renames["LDAPSSettingsIn"])
    types["LDAPSSettingsOut"] = t.struct(
        {
            "certificate": t.proxy(renames["CertificateOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "certificatePassword": t.string().optional(),
            "state": t.string().optional(),
            "certificatePfx": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LDAPSSettingsOut"])
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
    types["RestoreDomainRequestIn"] = t.struct({"backupId": t.string()}).named(
        renames["RestoreDomainRequestIn"]
    )
    types["RestoreDomainRequestOut"] = t.struct(
        {"backupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreDomainRequestOut"])

    functions = {}
    functions["projectsLocationsGet"] = managedidentities.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsGlobalDomainsDisableMigration"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsUpdateLdapssettings"
    ] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDetachTrust"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsTestIamPermissions"
    ] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsSetIamPolicy"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsList"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsCreate"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsDomainJoinMachine"
    ] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsResetAdminPassword"
    ] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsDelete"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGet"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsExtendSchema"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsEnableMigration"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsReconfigureTrust"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsPatch"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsRestore"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsValidateTrust"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsAttachTrust"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGetIamPolicy"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsGetLdapssettings"] = managedidentities.get(
        "v1/{name}/ldapssettings",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LDAPSSettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsSqlIntegrationsGet"
    ] = managedidentities.get(
        "v1/{parent}/sqlIntegrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSqlIntegrationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsSqlIntegrationsList"
    ] = managedidentities.get(
        "v1/{parent}/sqlIntegrations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSqlIntegrationsResponseOut"]),
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
    functions[
        "projectsLocationsGlobalDomainsBackupsGetIamPolicy"
    ] = managedidentities.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
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
    functions["projectsLocationsGlobalDomainsBackupsDelete"] = managedidentities.get(
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
        "projectsLocationsGlobalDomainsBackupsSetIamPolicy"
    ] = managedidentities.get(
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
    functions["projectsLocationsGlobalPeeringsList"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsGetIamPolicy"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsDelete"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsGet"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsSetIamPolicy"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalPeeringsTestIamPermissions"
    ] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsPatch"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalPeeringsCreate"] = managedidentities.post(
        "v1/{parent}/peerings",
        t.struct(
            {
                "parent": t.string(),
                "peeringId": t.string(),
                "domainResource": t.string(),
                "authorizedNetwork": t.string(),
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
