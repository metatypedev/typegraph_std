from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_managedidentities() -> Import:
    managedidentities = HTTPRuntime("https://managedidentities.googleapis.com/")

    renames = {
        "ErrorResponse": "_managedidentities_1_ErrorResponse",
        "ListOperationsResponseIn": "_managedidentities_2_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_managedidentities_3_ListOperationsResponseOut",
        "AttachTrustRequestIn": "_managedidentities_4_AttachTrustRequestIn",
        "AttachTrustRequestOut": "_managedidentities_5_AttachTrustRequestOut",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataIn": "_managedidentities_6_GoogleCloudManagedidentitiesV1beta1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1beta1OpMetadataOut": "_managedidentities_7_GoogleCloudManagedidentitiesV1beta1OpMetadataOut",
        "UpdatePolicyIn": "_managedidentities_8_UpdatePolicyIn",
        "UpdatePolicyOut": "_managedidentities_9_UpdatePolicyOut",
        "OperationIn": "_managedidentities_10_OperationIn",
        "OperationOut": "_managedidentities_11_OperationOut",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataIn": "_managedidentities_12_GoogleCloudManagedidentitiesV1alpha1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1alpha1OpMetadataOut": "_managedidentities_13_GoogleCloudManagedidentitiesV1alpha1OpMetadataOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn": "_managedidentities_14_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut": "_managedidentities_15_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut",
        "TestIamPermissionsResponseIn": "_managedidentities_16_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_managedidentities_17_TestIamPermissionsResponseOut",
        "ReconfigureTrustRequestIn": "_managedidentities_18_ReconfigureTrustRequestIn",
        "ReconfigureTrustRequestOut": "_managedidentities_19_ReconfigureTrustRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn": "_managedidentities_20_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut": "_managedidentities_21_GoogleCloudSaasacceleratorManagementProvidersV1SloEligibilityOut",
        "WeeklyCycleIn": "_managedidentities_22_WeeklyCycleIn",
        "WeeklyCycleOut": "_managedidentities_23_WeeklyCycleOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn": "_managedidentities_24_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut": "_managedidentities_25_GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataOut",
        "CertificateIn": "_managedidentities_26_CertificateIn",
        "CertificateOut": "_managedidentities_27_CertificateOut",
        "ListLocationsResponseIn": "_managedidentities_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_managedidentities_29_ListLocationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn": "_managedidentities_30_GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut": "_managedidentities_31_GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut",
        "DomainJoinMachineRequestIn": "_managedidentities_32_DomainJoinMachineRequestIn",
        "DomainJoinMachineRequestOut": "_managedidentities_33_DomainJoinMachineRequestOut",
        "TrustIn": "_managedidentities_34_TrustIn",
        "TrustOut": "_managedidentities_35_TrustOut",
        "RestoreDomainRequestIn": "_managedidentities_36_RestoreDomainRequestIn",
        "RestoreDomainRequestOut": "_managedidentities_37_RestoreDomainRequestOut",
        "MaintenanceWindowIn": "_managedidentities_38_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_managedidentities_39_MaintenanceWindowOut",
        "DenyMaintenancePeriodIn": "_managedidentities_40_DenyMaintenancePeriodIn",
        "DenyMaintenancePeriodOut": "_managedidentities_41_DenyMaintenancePeriodOut",
        "ListBackupsResponseIn": "_managedidentities_42_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_managedidentities_43_ListBackupsResponseOut",
        "MaintenancePolicyIn": "_managedidentities_44_MaintenancePolicyIn",
        "MaintenancePolicyOut": "_managedidentities_45_MaintenancePolicyOut",
        "EmptyIn": "_managedidentities_46_EmptyIn",
        "EmptyOut": "_managedidentities_47_EmptyOut",
        "PolicyIn": "_managedidentities_48_PolicyIn",
        "PolicyOut": "_managedidentities_49_PolicyOut",
        "DomainIn": "_managedidentities_50_DomainIn",
        "DomainOut": "_managedidentities_51_DomainOut",
        "ResetAdminPasswordResponseIn": "_managedidentities_52_ResetAdminPasswordResponseIn",
        "ResetAdminPasswordResponseOut": "_managedidentities_53_ResetAdminPasswordResponseOut",
        "ValidateTrustRequestIn": "_managedidentities_54_ValidateTrustRequestIn",
        "ValidateTrustRequestOut": "_managedidentities_55_ValidateTrustRequestOut",
        "ExprIn": "_managedidentities_56_ExprIn",
        "ExprOut": "_managedidentities_57_ExprOut",
        "ExtendSchemaRequestIn": "_managedidentities_58_ExtendSchemaRequestIn",
        "ExtendSchemaRequestOut": "_managedidentities_59_ExtendSchemaRequestOut",
        "SqlIntegrationIn": "_managedidentities_60_SqlIntegrationIn",
        "SqlIntegrationOut": "_managedidentities_61_SqlIntegrationOut",
        "OperationMetadataIn": "_managedidentities_62_OperationMetadataIn",
        "OperationMetadataOut": "_managedidentities_63_OperationMetadataOut",
        "TimeOfDayIn": "_managedidentities_64_TimeOfDayIn",
        "TimeOfDayOut": "_managedidentities_65_TimeOfDayOut",
        "DomainJoinMachineResponseIn": "_managedidentities_66_DomainJoinMachineResponseIn",
        "DomainJoinMachineResponseOut": "_managedidentities_67_DomainJoinMachineResponseOut",
        "ScheduleIn": "_managedidentities_68_ScheduleIn",
        "ScheduleOut": "_managedidentities_69_ScheduleOut",
        "LDAPSSettingsIn": "_managedidentities_70_LDAPSSettingsIn",
        "LDAPSSettingsOut": "_managedidentities_71_LDAPSSettingsOut",
        "ListPeeringsResponseIn": "_managedidentities_72_ListPeeringsResponseIn",
        "ListPeeringsResponseOut": "_managedidentities_73_ListPeeringsResponseOut",
        "DailyCycleIn": "_managedidentities_74_DailyCycleIn",
        "DailyCycleOut": "_managedidentities_75_DailyCycleOut",
        "DetachTrustRequestIn": "_managedidentities_76_DetachTrustRequestIn",
        "DetachTrustRequestOut": "_managedidentities_77_DetachTrustRequestOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn": "_managedidentities_78_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut": "_managedidentities_79_GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut",
        "LocationIn": "_managedidentities_80_LocationIn",
        "LocationOut": "_managedidentities_81_LocationOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn": "_managedidentities_82_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut": "_managedidentities_83_GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut",
        "TestIamPermissionsRequestIn": "_managedidentities_84_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_managedidentities_85_TestIamPermissionsRequestOut",
        "DateIn": "_managedidentities_86_DateIn",
        "DateOut": "_managedidentities_87_DateOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn": "_managedidentities_88_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut": "_managedidentities_89_GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameterOut",
        "BindingIn": "_managedidentities_90_BindingIn",
        "BindingOut": "_managedidentities_91_BindingOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn": "_managedidentities_92_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut": "_managedidentities_93_GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut",
        "BackupIn": "_managedidentities_94_BackupIn",
        "BackupOut": "_managedidentities_95_BackupOut",
        "SetIamPolicyRequestIn": "_managedidentities_96_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_managedidentities_97_SetIamPolicyRequestOut",
        "GoogleCloudManagedidentitiesV1OpMetadataIn": "_managedidentities_98_GoogleCloudManagedidentitiesV1OpMetadataIn",
        "GoogleCloudManagedidentitiesV1OpMetadataOut": "_managedidentities_99_GoogleCloudManagedidentitiesV1OpMetadataOut",
        "StatusIn": "_managedidentities_100_StatusIn",
        "StatusOut": "_managedidentities_101_StatusOut",
        "ListDomainsResponseIn": "_managedidentities_102_ListDomainsResponseIn",
        "ListDomainsResponseOut": "_managedidentities_103_ListDomainsResponseOut",
        "ListSqlIntegrationsResponseIn": "_managedidentities_104_ListSqlIntegrationsResponseIn",
        "ListSqlIntegrationsResponseOut": "_managedidentities_105_ListSqlIntegrationsResponseOut",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn": "_managedidentities_106_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn",
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut": "_managedidentities_107_GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut",
        "CancelOperationRequestIn": "_managedidentities_108_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_managedidentities_109_CancelOperationRequestOut",
        "PeeringIn": "_managedidentities_110_PeeringIn",
        "PeeringOut": "_managedidentities_111_PeeringOut",
        "ResetAdminPasswordRequestIn": "_managedidentities_112_ResetAdminPasswordRequestIn",
        "ResetAdminPasswordRequestOut": "_managedidentities_113_ResetAdminPasswordRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AttachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["AttachTrustRequestIn"])
    types["AttachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTrustRequestOut"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1beta1OpMetadataOut"])
    types["UpdatePolicyIn"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodIn"])
            ).optional(),
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowIn"]).optional(),
        }
    ).named(renames["UpdatePolicyIn"])
    types["UpdatePolicyOut"] = t.struct(
        {
            "denyMaintenancePeriods": t.array(
                t.proxy(renames["DenyMaintenancePeriodOut"])
            ).optional(),
            "channel": t.string().optional(),
            "window": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdatePolicyOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1alpha1OpMetadataOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["WeeklyCycleIn"] = t.struct(
        {"schedule": t.array(t.proxy(renames["ScheduleIn"])).optional()}
    ).named(renames["WeeklyCycleIn"])
    types["WeeklyCycleOut"] = t.struct(
        {
            "schedule": t.array(t.proxy(renames["ScheduleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WeeklyCycleOut"])
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
    ] = t.struct(
        {
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
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
            "nodeId": t.string().optional(),
            "location": t.string().optional(),
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
    types["CertificateIn"] = t.struct(
        {
            "issuingCertificate": t.proxy(renames["CertificateIn"]).optional(),
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
        }
    ).named(renames["CertificateIn"])
    types["CertificateOut"] = t.struct(
        {
            "issuingCertificate": t.proxy(renames["CertificateOut"]).optional(),
            "thumbprint": t.string().optional(),
            "expireTime": t.string().optional(),
            "subject": t.string().optional(),
            "subjectAlternativeName": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateOut"])
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
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"] = t.struct(
        {
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceIn"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"] = t.struct(
        {
            "softwareVersions": t.struct({"_": t.string().optional()}).optional(),
            "slmInstanceTemplate": t.string().optional(),
            "consumerDefinedName": t.string().optional(),
            "maintenanceSchedules": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "producerMetadata": t.struct({"_": t.string().optional()}).optional(),
            "maintenancePolicyNames": t.struct({"_": t.string().optional()}).optional(),
            "sloMetadata": t.proxy(
                renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"]
            ).optional(),
            "state": t.string().optional(),
            "instanceType": t.string().optional(),
            "notificationParameters": t.struct({"_": t.string().optional()}).optional(),
            "tenantProjectId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "maintenanceSettings": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettingsOut"
                ]
            ).optional(),
            "provisionedResources": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResourceOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1InstanceOut"])
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
    types["TrustIn"] = t.struct(
        {
            "trustType": t.string(),
            "targetDnsIpAddresses": t.array(t.string()),
            "selectiveAuthentication": t.boolean().optional(),
            "targetDomainName": t.string(),
            "trustDirection": t.string(),
            "trustHandshakeSecret": t.string(),
        }
    ).named(renames["TrustIn"])
    types["TrustOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "trustType": t.string(),
            "lastTrustHeartbeatTime": t.string().optional(),
            "targetDnsIpAddresses": t.array(t.string()),
            "selectiveAuthentication": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "stateDescription": t.string().optional(),
            "targetDomainName": t.string(),
            "trustDirection": t.string(),
            "trustHandshakeSecret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrustOut"])
    types["RestoreDomainRequestIn"] = t.struct({"backupId": t.string()}).named(
        renames["RestoreDomainRequestIn"]
    )
    types["RestoreDomainRequestOut"] = t.struct(
        {"backupId": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreDomainRequestOut"])
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
    types["DenyMaintenancePeriodIn"] = t.struct(
        {
            "startDate": t.proxy(renames["DateIn"]).optional(),
            "time": t.proxy(renames["TimeOfDayIn"]).optional(),
            "endDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodIn"])
    types["DenyMaintenancePeriodOut"] = t.struct(
        {
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "time": t.proxy(renames["TimeOfDayOut"]).optional(),
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DenyMaintenancePeriodOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
    types["MaintenancePolicyIn"] = t.struct(
        {
            "updatePolicy": t.proxy(renames["UpdatePolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MaintenancePolicyIn"])
    types["MaintenancePolicyOut"] = t.struct(
        {
            "updatePolicy": t.proxy(renames["UpdatePolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenancePolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["DomainIn"] = t.struct(
        {
            "admin": t.string().optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservedIpRange": t.string(),
            "authorizedNetworks": t.array(t.string()).optional(),
            "name": t.string(),
            "locations": t.array(t.string()),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "admin": t.string().optional(),
            "auditLogsEnabled": t.boolean().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "reservedIpRange": t.string(),
            "trusts": t.array(t.proxy(renames["TrustOut"])).optional(),
            "authorizedNetworks": t.array(t.string()).optional(),
            "fqdn": t.string().optional(),
            "name": t.string(),
            "updateTime": t.string().optional(),
            "locations": t.array(t.string()),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["ResetAdminPasswordResponseIn"] = t.struct(
        {"password": t.string().optional()}
    ).named(renames["ResetAdminPasswordResponseIn"])
    types["ResetAdminPasswordResponseOut"] = t.struct(
        {
            "password": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResetAdminPasswordResponseOut"])
    types["ValidateTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["ValidateTrustRequestIn"])
    types["ValidateTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateTrustRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ExtendSchemaRequestIn"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "gcsPath": t.string().optional(),
            "description": t.string(),
        }
    ).named(renames["ExtendSchemaRequestIn"])
    types["ExtendSchemaRequestOut"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "gcsPath": t.string().optional(),
            "description": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtendSchemaRequestOut"])
    types["SqlIntegrationIn"] = t.struct(
        {"sqlInstance": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SqlIntegrationIn"])
    types["SqlIntegrationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "sqlInstance": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SqlIntegrationOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TimeOfDayIn"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["TimeOfDayIn"])
    types["TimeOfDayOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "seconds": t.integer().optional(),
            "minutes": t.integer().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeOfDayOut"])
    types["DomainJoinMachineResponseIn"] = t.struct(
        {"domainJoinBlob": t.string().optional()}
    ).named(renames["DomainJoinMachineResponseIn"])
    types["DomainJoinMachineResponseOut"] = t.struct(
        {
            "domainJoinBlob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainJoinMachineResponseOut"])
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
    types["LDAPSSettingsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "certificatePfx": t.string().optional(),
            "certificatePassword": t.string().optional(),
        }
    ).named(renames["LDAPSSettingsIn"])
    types["LDAPSSettingsOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "certificatePfx": t.string().optional(),
            "certificatePassword": t.string().optional(),
            "certificate": t.proxy(renames["CertificateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LDAPSSettingsOut"])
    types["ListPeeringsResponseIn"] = t.struct(
        {
            "peerings": t.array(t.proxy(renames["PeeringIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPeeringsResponseIn"])
    types["ListPeeringsResponseOut"] = t.struct(
        {
            "peerings": t.array(t.proxy(renames["PeeringOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPeeringsResponseOut"])
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
    types["DetachTrustRequestIn"] = t.struct(
        {"trust": t.proxy(renames["TrustIn"])}
    ).named(renames["DetachTrustRequestIn"])
    types["DetachTrustRequestOut"] = t.struct(
        {
            "trust": t.proxy(renames["TrustOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachTrustRequestOut"])
    types["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataIn"] = t.struct(
        {
            "nodes": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadataIn"
                    ]
                )
            ).optional(),
            "tier": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityIn"
                ]
            ).optional(),
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
            "tier": t.string().optional(),
            "perSliEligibility": t.proxy(
                renames[
                    "GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibilityOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudSaasacceleratorManagementProvidersV1SloMetadataOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["BackupIn"] = t.struct(
        {"labels": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "state": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["GoogleCloudManagedidentitiesV1OpMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataIn"])
    types["GoogleCloudManagedidentitiesV1OpMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudManagedidentitiesV1OpMetadataOut"])
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
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"
    ] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleIn"]
    )
    types[
        "GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"
    ] = t.struct(
        {
            "scheduleDeadlineTime": t.string().optional(),
            "startTime": t.string().optional(),
            "rolloutManagementPolicy": t.string().optional(),
            "endTime": t.string().optional(),
            "canReschedule": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceScheduleOut"]
    )
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
            "statusMessage": t.string().optional(),
            "domainResource": t.string(),
            "authorizedNetwork": t.string(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeringOut"])
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions[
        "projectsLocationsGlobalDomainsTestIamPermissions"
    ] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsList"] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsCreate"] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsReconfigureTrust"] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsGet"] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsDelete"] = managedidentities.get(
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
    functions["projectsLocationsGlobalDomainsRestore"] = managedidentities.get(
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
    functions[
        "projectsLocationsGlobalDomainsResetAdminPassword"
    ] = managedidentities.get(
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
        "projectsLocationsGlobalDomainsBackupsSetIamPolicy"
    ] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsTestIamPermissions"
    ] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsDelete"] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsPatch"] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsList"] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsGet"] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGlobalDomainsBackupsCreate"] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsGlobalDomainsBackupsGetIamPolicy"
    ] = managedidentities.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
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
        importer="managedidentities", renames=renames, types=types, functions=functions
    )
