from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_chromemanagement():
    chromemanagement = HTTPRuntime("https://chromemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromemanagement_1_ErrorResponse",
        "GoogleChromeManagementV1AndroidAppInfoIn": "_chromemanagement_2_GoogleChromeManagementV1AndroidAppInfoIn",
        "GoogleChromeManagementV1AndroidAppInfoOut": "_chromemanagement_3_GoogleChromeManagementV1AndroidAppInfoOut",
        "GoogleChromeManagementV1CpuStatusReportIn": "_chromemanagement_4_GoogleChromeManagementV1CpuStatusReportIn",
        "GoogleChromeManagementV1CpuStatusReportOut": "_chromemanagement_5_GoogleChromeManagementV1CpuStatusReportOut",
        "GoogleChromeManagementV1NetworkDeviceIn": "_chromemanagement_6_GoogleChromeManagementV1NetworkDeviceIn",
        "GoogleChromeManagementV1NetworkDeviceOut": "_chromemanagement_7_GoogleChromeManagementV1NetworkDeviceOut",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseIn": "_chromemanagement_8_GoogleChromeManagementV1ListTelemetryDevicesResponseIn",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseOut": "_chromemanagement_9_GoogleChromeManagementV1ListTelemetryDevicesResponseOut",
        "GoogleChromeManagementV1MemoryInfoIn": "_chromemanagement_10_GoogleChromeManagementV1MemoryInfoIn",
        "GoogleChromeManagementV1MemoryInfoOut": "_chromemanagement_11_GoogleChromeManagementV1MemoryInfoOut",
        "GoogleChromeManagementV1ChromeAppPermissionIn": "_chromemanagement_12_GoogleChromeManagementV1ChromeAppPermissionIn",
        "GoogleChromeManagementV1ChromeAppPermissionOut": "_chromemanagement_13_GoogleChromeManagementV1ChromeAppPermissionOut",
        "GoogleChromeManagementV1NetworkDiagnosticsReportIn": "_chromemanagement_14_GoogleChromeManagementV1NetworkDiagnosticsReportIn",
        "GoogleChromeManagementV1NetworkDiagnosticsReportOut": "_chromemanagement_15_GoogleChromeManagementV1NetworkDiagnosticsReportOut",
        "GoogleChromeManagementV1DisplayDeviceIn": "_chromemanagement_16_GoogleChromeManagementV1DisplayDeviceIn",
        "GoogleChromeManagementV1DisplayDeviceOut": "_chromemanagement_17_GoogleChromeManagementV1DisplayDeviceOut",
        "GoogleChromeManagementV1BatterySampleReportIn": "_chromemanagement_18_GoogleChromeManagementV1BatterySampleReportIn",
        "GoogleChromeManagementV1BatterySampleReportOut": "_chromemanagement_19_GoogleChromeManagementV1BatterySampleReportOut",
        "GoogleChromeManagementV1BootPerformanceReportIn": "_chromemanagement_20_GoogleChromeManagementV1BootPerformanceReportIn",
        "GoogleChromeManagementV1BootPerformanceReportOut": "_chromemanagement_21_GoogleChromeManagementV1BootPerformanceReportOut",
        "GoogleChromeManagementV1BrowserVersionIn": "_chromemanagement_22_GoogleChromeManagementV1BrowserVersionIn",
        "GoogleChromeManagementV1BrowserVersionOut": "_chromemanagement_23_GoogleChromeManagementV1BrowserVersionOut",
        "GoogleChromeManagementV1ChromeAppRequestIn": "_chromemanagement_24_GoogleChromeManagementV1ChromeAppRequestIn",
        "GoogleChromeManagementV1ChromeAppRequestOut": "_chromemanagement_25_GoogleChromeManagementV1ChromeAppRequestOut",
        "GoogleChromeManagementV1ChromeAppSiteAccessIn": "_chromemanagement_26_GoogleChromeManagementV1ChromeAppSiteAccessIn",
        "GoogleChromeManagementV1ChromeAppSiteAccessOut": "_chromemanagement_27_GoogleChromeManagementV1ChromeAppSiteAccessOut",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn": "_chromemanagement_28_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut": "_chromemanagement_29_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut",
        "GoogleChromeManagementV1ChromeAppInfoIn": "_chromemanagement_30_GoogleChromeManagementV1ChromeAppInfoIn",
        "GoogleChromeManagementV1ChromeAppInfoOut": "_chromemanagement_31_GoogleChromeManagementV1ChromeAppInfoOut",
        "GoogleChromeManagementV1GraphicsStatusReportIn": "_chromemanagement_32_GoogleChromeManagementV1GraphicsStatusReportIn",
        "GoogleChromeManagementV1GraphicsStatusReportOut": "_chromemanagement_33_GoogleChromeManagementV1GraphicsStatusReportOut",
        "GoogleChromeManagementV1AndroidAppPermissionIn": "_chromemanagement_34_GoogleChromeManagementV1AndroidAppPermissionIn",
        "GoogleChromeManagementV1AndroidAppPermissionOut": "_chromemanagement_35_GoogleChromeManagementV1AndroidAppPermissionOut",
        "GoogleChromeManagementV1InstalledAppIn": "_chromemanagement_36_GoogleChromeManagementV1InstalledAppIn",
        "GoogleChromeManagementV1InstalledAppOut": "_chromemanagement_37_GoogleChromeManagementV1InstalledAppOut",
        "GoogleChromeManagementV1UsbPeripheralReportIn": "_chromemanagement_38_GoogleChromeManagementV1UsbPeripheralReportIn",
        "GoogleChromeManagementV1UsbPeripheralReportOut": "_chromemanagement_39_GoogleChromeManagementV1UsbPeripheralReportOut",
        "GoogleChromeManagementV1TelemetryUserIn": "_chromemanagement_40_GoogleChromeManagementV1TelemetryUserIn",
        "GoogleChromeManagementV1TelemetryUserOut": "_chromemanagement_41_GoogleChromeManagementV1TelemetryUserOut",
        "GoogleTypeDateIn": "_chromemanagement_42_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_chromemanagement_43_GoogleTypeDateOut",
        "GoogleChromeManagementV1AppDetailsIn": "_chromemanagement_44_GoogleChromeManagementV1AppDetailsIn",
        "GoogleChromeManagementV1AppDetailsOut": "_chromemanagement_45_GoogleChromeManagementV1AppDetailsOut",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn": "_chromemanagement_46_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut": "_chromemanagement_47_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn": "_chromemanagement_48_GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut": "_chromemanagement_49_GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn": "_chromemanagement_50_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut": "_chromemanagement_51_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut",
        "GoogleChromeManagementV1NetworkStatusReportIn": "_chromemanagement_52_GoogleChromeManagementV1NetworkStatusReportIn",
        "GoogleChromeManagementV1NetworkStatusReportOut": "_chromemanagement_53_GoogleChromeManagementV1NetworkStatusReportOut",
        "GoogleRpcStatusIn": "_chromemanagement_54_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_chromemanagement_55_GoogleRpcStatusOut",
        "GoogleChromeManagementV1TelemetryDeviceInfoIn": "_chromemanagement_56_GoogleChromeManagementV1TelemetryDeviceInfoIn",
        "GoogleChromeManagementV1TelemetryDeviceInfoOut": "_chromemanagement_57_GoogleChromeManagementV1TelemetryDeviceInfoOut",
        "GoogleChromeManagementV1CountInstalledAppsResponseIn": "_chromemanagement_58_GoogleChromeManagementV1CountInstalledAppsResponseIn",
        "GoogleChromeManagementV1CountInstalledAppsResponseOut": "_chromemanagement_59_GoogleChromeManagementV1CountInstalledAppsResponseOut",
        "GoogleChromeManagementV1ThunderboltInfoIn": "_chromemanagement_60_GoogleChromeManagementV1ThunderboltInfoIn",
        "GoogleChromeManagementV1ThunderboltInfoOut": "_chromemanagement_61_GoogleChromeManagementV1ThunderboltInfoOut",
        "GoogleChromeManagementV1DisplayInfoIn": "_chromemanagement_62_GoogleChromeManagementV1DisplayInfoIn",
        "GoogleChromeManagementV1DisplayInfoOut": "_chromemanagement_63_GoogleChromeManagementV1DisplayInfoOut",
        "GoogleChromeManagementV1TelemetryDeviceIn": "_chromemanagement_64_GoogleChromeManagementV1TelemetryDeviceIn",
        "GoogleChromeManagementV1TelemetryDeviceOut": "_chromemanagement_65_GoogleChromeManagementV1TelemetryDeviceOut",
        "GoogleChromeManagementV1TelemetryUserDeviceIn": "_chromemanagement_66_GoogleChromeManagementV1TelemetryUserDeviceIn",
        "GoogleChromeManagementV1TelemetryUserDeviceOut": "_chromemanagement_67_GoogleChromeManagementV1TelemetryUserDeviceOut",
        "GoogleChromeManagementV1NetworkInfoIn": "_chromemanagement_68_GoogleChromeManagementV1NetworkInfoIn",
        "GoogleChromeManagementV1NetworkInfoOut": "_chromemanagement_69_GoogleChromeManagementV1NetworkInfoOut",
        "GoogleChromeManagementV1DeviceHardwareCountReportIn": "_chromemanagement_70_GoogleChromeManagementV1DeviceHardwareCountReportIn",
        "GoogleChromeManagementV1DeviceHardwareCountReportOut": "_chromemanagement_71_GoogleChromeManagementV1DeviceHardwareCountReportOut",
        "GoogleChromeManagementV1CpuTemperatureInfoIn": "_chromemanagement_72_GoogleChromeManagementV1CpuTemperatureInfoIn",
        "GoogleChromeManagementV1CpuTemperatureInfoOut": "_chromemanagement_73_GoogleChromeManagementV1CpuTemperatureInfoOut",
        "GoogleChromeManagementV1HeartbeatStatusReportIn": "_chromemanagement_74_GoogleChromeManagementV1HeartbeatStatusReportIn",
        "GoogleChromeManagementV1HeartbeatStatusReportOut": "_chromemanagement_75_GoogleChromeManagementV1HeartbeatStatusReportOut",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn": "_chromemanagement_76_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut": "_chromemanagement_77_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut",
        "GoogleChromeManagementV1GraphicsAdapterInfoIn": "_chromemanagement_78_GoogleChromeManagementV1GraphicsAdapterInfoIn",
        "GoogleChromeManagementV1GraphicsAdapterInfoOut": "_chromemanagement_79_GoogleChromeManagementV1GraphicsAdapterInfoOut",
        "GoogleChromeManagementV1DiskInfoIn": "_chromemanagement_80_GoogleChromeManagementV1DiskInfoIn",
        "GoogleChromeManagementV1DiskInfoOut": "_chromemanagement_81_GoogleChromeManagementV1DiskInfoOut",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseIn": "_chromemanagement_82_GoogleChromeManagementV1CountChromeAppRequestsResponseIn",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseOut": "_chromemanagement_83_GoogleChromeManagementV1CountChromeAppRequestsResponseOut",
        "GoogleChromeManagementV1BatteryStatusReportIn": "_chromemanagement_84_GoogleChromeManagementV1BatteryStatusReportIn",
        "GoogleChromeManagementV1BatteryStatusReportOut": "_chromemanagement_85_GoogleChromeManagementV1BatteryStatusReportOut",
        "GoogleChromeManagementV1DeviceAueCountReportIn": "_chromemanagement_86_GoogleChromeManagementV1DeviceAueCountReportIn",
        "GoogleChromeManagementV1DeviceAueCountReportOut": "_chromemanagement_87_GoogleChromeManagementV1DeviceAueCountReportOut",
        "GoogleChromeManagementV1KioskAppStatusReportIn": "_chromemanagement_88_GoogleChromeManagementV1KioskAppStatusReportIn",
        "GoogleChromeManagementV1KioskAppStatusReportOut": "_chromemanagement_89_GoogleChromeManagementV1KioskAppStatusReportOut",
        "GoogleChromeManagementV1BatteryInfoIn": "_chromemanagement_90_GoogleChromeManagementV1BatteryInfoIn",
        "GoogleChromeManagementV1BatteryInfoOut": "_chromemanagement_91_GoogleChromeManagementV1BatteryInfoOut",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseIn": "_chromemanagement_92_GoogleChromeManagementV1FindInstalledAppDevicesResponseIn",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseOut": "_chromemanagement_93_GoogleChromeManagementV1FindInstalledAppDevicesResponseOut",
        "GoogleChromeManagementV1ListTelemetryEventsResponseIn": "_chromemanagement_94_GoogleChromeManagementV1ListTelemetryEventsResponseIn",
        "GoogleChromeManagementV1ListTelemetryEventsResponseOut": "_chromemanagement_95_GoogleChromeManagementV1ListTelemetryEventsResponseOut",
        "GoogleChromeManagementV1TelemetryEventIn": "_chromemanagement_96_GoogleChromeManagementV1TelemetryEventIn",
        "GoogleChromeManagementV1TelemetryEventOut": "_chromemanagement_97_GoogleChromeManagementV1TelemetryEventOut",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn": "_chromemanagement_98_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut": "_chromemanagement_99_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut",
        "GoogleChromeManagementV1DeviceIn": "_chromemanagement_100_GoogleChromeManagementV1DeviceIn",
        "GoogleChromeManagementV1DeviceOut": "_chromemanagement_101_GoogleChromeManagementV1DeviceOut",
        "GoogleChromeManagementV1TelemetryUserInfoIn": "_chromemanagement_102_GoogleChromeManagementV1TelemetryUserInfoIn",
        "GoogleChromeManagementV1TelemetryUserInfoOut": "_chromemanagement_103_GoogleChromeManagementV1TelemetryUserInfoOut",
        "GoogleChromeManagementV1StorageInfoIn": "_chromemanagement_104_GoogleChromeManagementV1StorageInfoIn",
        "GoogleChromeManagementV1StorageInfoOut": "_chromemanagement_105_GoogleChromeManagementV1StorageInfoOut",
        "GoogleChromeManagementV1ListTelemetryUsersResponseIn": "_chromemanagement_106_GoogleChromeManagementV1ListTelemetryUsersResponseIn",
        "GoogleChromeManagementV1ListTelemetryUsersResponseOut": "_chromemanagement_107_GoogleChromeManagementV1ListTelemetryUsersResponseOut",
        "GoogleChromeManagementV1StorageInfoDiskVolumeIn": "_chromemanagement_108_GoogleChromeManagementV1StorageInfoDiskVolumeIn",
        "GoogleChromeManagementV1StorageInfoDiskVolumeOut": "_chromemanagement_109_GoogleChromeManagementV1StorageInfoDiskVolumeOut",
        "GoogleChromeManagementV1MemoryStatusReportIn": "_chromemanagement_110_GoogleChromeManagementV1MemoryStatusReportIn",
        "GoogleChromeManagementV1MemoryStatusReportOut": "_chromemanagement_111_GoogleChromeManagementV1MemoryStatusReportOut",
        "GoogleChromeManagementV1TouchScreenDeviceIn": "_chromemanagement_112_GoogleChromeManagementV1TouchScreenDeviceIn",
        "GoogleChromeManagementV1TouchScreenDeviceOut": "_chromemanagement_113_GoogleChromeManagementV1TouchScreenDeviceOut",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn": "_chromemanagement_114_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut": "_chromemanagement_115_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut",
        "GoogleChromeManagementV1TouchScreenInfoIn": "_chromemanagement_116_GoogleChromeManagementV1TouchScreenInfoIn",
        "GoogleChromeManagementV1TouchScreenInfoOut": "_chromemanagement_117_GoogleChromeManagementV1TouchScreenInfoOut",
        "GoogleChromeManagementV1AudioStatusReportIn": "_chromemanagement_118_GoogleChromeManagementV1AudioStatusReportIn",
        "GoogleChromeManagementV1AudioStatusReportOut": "_chromemanagement_119_GoogleChromeManagementV1AudioStatusReportOut",
        "GoogleChromeManagementV1CpuInfoIn": "_chromemanagement_120_GoogleChromeManagementV1CpuInfoIn",
        "GoogleChromeManagementV1CpuInfoOut": "_chromemanagement_121_GoogleChromeManagementV1CpuInfoOut",
        "GoogleChromeManagementV1CountChromeVersionsResponseIn": "_chromemanagement_122_GoogleChromeManagementV1CountChromeVersionsResponseIn",
        "GoogleChromeManagementV1CountChromeVersionsResponseOut": "_chromemanagement_123_GoogleChromeManagementV1CountChromeVersionsResponseOut",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataIn": "_chromemanagement_124_GoogleChromeManagementV1HttpsLatencyRoutineDataIn",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataOut": "_chromemanagement_125_GoogleChromeManagementV1HttpsLatencyRoutineDataOut",
        "GoogleChromeManagementV1PeripheralsReportIn": "_chromemanagement_126_GoogleChromeManagementV1PeripheralsReportIn",
        "GoogleChromeManagementV1PeripheralsReportOut": "_chromemanagement_127_GoogleChromeManagementV1PeripheralsReportOut",
        "GoogleChromeManagementV1GraphicsInfoIn": "_chromemanagement_128_GoogleChromeManagementV1GraphicsInfoIn",
        "GoogleChromeManagementV1GraphicsInfoOut": "_chromemanagement_129_GoogleChromeManagementV1GraphicsInfoOut",
        "GoogleChromeManagementV1StorageStatusReportIn": "_chromemanagement_130_GoogleChromeManagementV1StorageStatusReportIn",
        "GoogleChromeManagementV1StorageStatusReportOut": "_chromemanagement_131_GoogleChromeManagementV1StorageStatusReportOut",
        "GoogleChromeManagementV1OsUpdateStatusIn": "_chromemanagement_132_GoogleChromeManagementV1OsUpdateStatusIn",
        "GoogleChromeManagementV1OsUpdateStatusOut": "_chromemanagement_133_GoogleChromeManagementV1OsUpdateStatusOut",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoIn": "_chromemanagement_134_GoogleChromeManagementV1TotalMemoryEncryptionInfoIn",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoOut": "_chromemanagement_135_GoogleChromeManagementV1TotalMemoryEncryptionInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleChromeManagementV1AndroidAppInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AndroidAppInfoIn"])
    types["GoogleChromeManagementV1AndroidAppInfoOut"] = t.struct(
        {
            "permissions": t.array(
                t.proxy(renames["GoogleChromeManagementV1AndroidAppPermissionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AndroidAppInfoOut"])
    types["GoogleChromeManagementV1CpuStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuStatusReportIn"])
    types["GoogleChromeManagementV1CpuStatusReportOut"] = t.struct(
        {
            "cpuUtilizationPct": t.integer().optional(),
            "sampleFrequency": t.string().optional(),
            "reportTime": t.string().optional(),
            "cpuTemperatureInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuTemperatureInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuStatusReportOut"])
    types["GoogleChromeManagementV1NetworkDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkDeviceIn"])
    types["GoogleChromeManagementV1NetworkDeviceOut"] = t.struct(
        {
            "macAddress": t.string().optional(),
            "type": t.string().optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "mdn": t.string().optional(),
            "iccid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkDeviceOut"])
    types["GoogleChromeManagementV1ListTelemetryDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"])
    types["GoogleChromeManagementV1MemoryInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1MemoryInfoIn"])
    types["GoogleChromeManagementV1MemoryInfoOut"] = t.struct(
        {
            "availableRamBytes": t.string().optional(),
            "totalMemoryEncryption": t.proxy(
                renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"]
            ).optional(),
            "totalRamBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1MemoryInfoOut"])
    types["GoogleChromeManagementV1ChromeAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionIn"])
    types["GoogleChromeManagementV1ChromeAppPermissionOut"] = t.struct(
        {
            "accessUserData": t.boolean().optional(),
            "type": t.string().optional(),
            "documentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
    types["GoogleChromeManagementV1NetworkDiagnosticsReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkDiagnosticsReportIn"])
    types["GoogleChromeManagementV1NetworkDiagnosticsReportOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "httpsLatencyData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkDiagnosticsReportOut"])
    types["GoogleChromeManagementV1DisplayDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayDeviceIn"])
    types["GoogleChromeManagementV1DisplayDeviceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "modelId": t.integer().optional(),
            "manufactureYear": t.integer().optional(),
            "internal": t.boolean().optional(),
            "displayWidthMm": t.integer().optional(),
            "manufacturerId": t.string().optional(),
            "displayHeightMm": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayDeviceOut"])
    types["GoogleChromeManagementV1BatterySampleReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatterySampleReportIn"])
    types["GoogleChromeManagementV1BatterySampleReportOut"] = t.struct(
        {
            "remainingCapacity": t.string().optional(),
            "temperature": t.integer().optional(),
            "current": t.string().optional(),
            "dischargeRate": t.integer().optional(),
            "status": t.string().optional(),
            "reportTime": t.string().optional(),
            "chargeRate": t.integer().optional(),
            "voltage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatterySampleReportOut"])
    types["GoogleChromeManagementV1BootPerformanceReportIn"] = t.struct(
        {
            "shutdownReason": t.string().optional(),
            "shutdownDuration": t.string().optional(),
            "bootUpDuration": t.string().optional(),
            "shutdownTime": t.string().optional(),
            "bootUpTime": t.string().optional(),
            "reportTime": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportIn"])
    types["GoogleChromeManagementV1BootPerformanceReportOut"] = t.struct(
        {
            "shutdownReason": t.string().optional(),
            "shutdownDuration": t.string().optional(),
            "bootUpDuration": t.string().optional(),
            "shutdownTime": t.string().optional(),
            "bootUpTime": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
    types["GoogleChromeManagementV1BrowserVersionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BrowserVersionIn"])
    types["GoogleChromeManagementV1BrowserVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "count": t.string().optional(),
            "channel": t.string().optional(),
            "deviceOsVersion": t.string().optional(),
            "system": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BrowserVersionOut"])
    types["GoogleChromeManagementV1ChromeAppRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
    types["GoogleChromeManagementV1ChromeAppRequestOut"] = t.struct(
        {
            "iconUri": t.string().optional(),
            "requestCount": t.string().optional(),
            "latestRequestTime": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
            "appDetails": t.string().optional(),
            "detailUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessIn"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessOut"] = t.struct(
        {
            "hostMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"
    ] = t.struct(
        {
            "noRecentUserActivityCount": t.string().optional(),
            "pendingUpdate": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut"
    ] = t.struct(
        {
            "noRecentUserActivityCount": t.string().optional(),
            "pendingUpdate": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut"
        ]
    )
    types["GoogleChromeManagementV1ChromeAppInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppInfoIn"])
    types["GoogleChromeManagementV1ChromeAppInfoOut"] = t.struct(
        {
            "googleOwned": t.boolean().optional(),
            "supportEnabled": t.boolean().optional(),
            "siteAccess": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
            ).optional(),
            "permissions": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
            ).optional(),
            "isCwsHosted": t.boolean().optional(),
            "isTheme": t.boolean().optional(),
            "kioskEnabled": t.boolean().optional(),
            "isExtensionPolicySupported": t.boolean().optional(),
            "type": t.string().optional(),
            "minUserCount": t.integer().optional(),
            "isKioskOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppInfoOut"])
    types["GoogleChromeManagementV1GraphicsStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsStatusReportIn"])
    types["GoogleChromeManagementV1GraphicsStatusReportOut"] = t.struct(
        {
            "displays": t.array(
                t.proxy(renames["GoogleChromeManagementV1DisplayInfoOut"])
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsStatusReportOut"])
    types["GoogleChromeManagementV1AndroidAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionIn"])
    types["GoogleChromeManagementV1AndroidAppPermissionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionOut"])
    types["GoogleChromeManagementV1InstalledAppIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1InstalledAppIn"])
    types["GoogleChromeManagementV1InstalledAppOut"] = t.struct(
        {
            "browserDeviceCount": t.string().optional(),
            "osUserCount": t.string().optional(),
            "appType": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "appSource": t.string().optional(),
            "homepageUri": t.string().optional(),
            "appId": t.string().optional(),
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "appInstallType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1InstalledAppOut"])
    types["GoogleChromeManagementV1UsbPeripheralReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
    types["GoogleChromeManagementV1UsbPeripheralReportOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "pid": t.integer().optional(),
            "classId": t.integer().optional(),
            "subclassId": t.integer().optional(),
            "vid": t.integer().optional(),
            "name": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
    types["GoogleChromeManagementV1TelemetryUserIn"] = t.struct(
        {
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceIn"])
            ).optional(),
            "name": t.string().optional(),
            "customer": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "userId": t.string().optional(),
            "userEmail": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserIn"])
    types["GoogleChromeManagementV1TelemetryUserOut"] = t.struct(
        {
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceOut"])
            ).optional(),
            "name": t.string().optional(),
            "customer": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "userId": t.string().optional(),
            "userEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleChromeManagementV1AppDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AppDetailsIn"])
    types["GoogleChromeManagementV1AppDetailsOut"] = t.struct(
        {
            "chromeAppInfo": t.proxy(
                renames["GoogleChromeManagementV1ChromeAppInfoOut"]
            ).optional(),
            "detailUri": t.string().optional(),
            "revisionId": t.string().optional(),
            "description": t.string().optional(),
            "iconUri": t.string().optional(),
            "firstPublishTime": t.string().optional(),
            "reviewNumber": t.string().optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "reviewRating": t.number().optional(),
            "isPaidApp": t.boolean().optional(),
            "serviceError": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "publisher": t.string().optional(),
            "latestPublishTime": t.string().optional(),
            "androidAppInfo": t.proxy(
                renames["GoogleChromeManagementV1AndroidAppInfoOut"]
            ).optional(),
            "homepageUri": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "privacyPolicyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AppDetailsOut"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"])
    types["GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn"] = t.struct(
        {
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
            ).optional()
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn"])
    types["GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut"] = t.struct(
        {
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut"])
    types[
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn"
    ] = t.struct(
        {
            "cpuReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "storageReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "modelReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "memoryReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut"
    ] = t.struct(
        {
            "cpuReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "storageReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "modelReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "memoryReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut"]
    )
    types["GoogleChromeManagementV1NetworkStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportIn"])
    types["GoogleChromeManagementV1NetworkStatusReportOut"] = t.struct(
        {
            "wifiPowerManagementEnabled": t.boolean().optional(),
            "transmissionBitRateMbps": t.string().optional(),
            "guid": t.string().optional(),
            "wifiLinkQuality": t.string().optional(),
            "transmissionPowerDbm": t.integer().optional(),
            "reportTime": t.string().optional(),
            "sampleFrequency": t.string().optional(),
            "encryptionOn": t.boolean().optional(),
            "lanIpAddress": t.string().optional(),
            "receivingBitRateMbps": t.string().optional(),
            "connectionState": t.string().optional(),
            "gatewayIpAddress": t.string().optional(),
            "connectionType": t.string().optional(),
            "signalStrengthDbm": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleChromeManagementV1TelemetryDeviceInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceInfoIn"])
    types["GoogleChromeManagementV1TelemetryDeviceInfoOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceInfoOut"])
    types["GoogleChromeManagementV1CountInstalledAppsResponseIn"] = t.struct(
        {
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseIn"])
    types["GoogleChromeManagementV1CountInstalledAppsResponseOut"] = t.struct(
        {
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseOut"])
    types["GoogleChromeManagementV1ThunderboltInfoIn"] = t.struct(
        {"securityLevel": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoIn"])
    types["GoogleChromeManagementV1ThunderboltInfoOut"] = t.struct(
        {
            "securityLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
    types["GoogleChromeManagementV1DisplayInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayInfoIn"])
    types["GoogleChromeManagementV1DisplayInfoOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "displayName": t.string().optional(),
            "resolutionHeight": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "isInternal": t.boolean().optional(),
            "resolutionWidth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayInfoOut"])
    types["GoogleChromeManagementV1TelemetryDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceIn"])
    types["GoogleChromeManagementV1TelemetryDeviceOut"] = t.struct(
        {
            "storageStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageStatusReportOut"])
            ).optional(),
            "thunderboltInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
            ).optional(),
            "memoryInfo": t.proxy(
                renames["GoogleChromeManagementV1MemoryInfoOut"]
            ).optional(),
            "customer": t.string().optional(),
            "graphicsInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsInfoOut"]
            ).optional(),
            "batteryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
            ).optional(),
            "cpuInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuInfoOut"])
            ).optional(),
            "heartbeatStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1HeartbeatStatusReportOut"])
            ).optional(),
            "networkInfo": t.proxy(
                renames["GoogleChromeManagementV1NetworkInfoOut"]
            ).optional(),
            "name": t.string().optional(),
            "deviceId": t.string().optional(),
            "osUpdateStatus": t.array(
                t.proxy(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
            ).optional(),
            "graphicsStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1GraphicsStatusReportOut"])
            ).optional(),
            "storageInfo": t.proxy(
                renames["GoogleChromeManagementV1StorageInfoOut"]
            ).optional(),
            "bootPerformanceReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
            ).optional(),
            "memoryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
            ).optional(),
            "serialNumber": t.string().optional(),
            "batteryInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryInfoOut"])
            ).optional(),
            "orgUnitId": t.string().optional(),
            "networkStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
            ).optional(),
            "cpuStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuStatusReportOut"])
            ).optional(),
            "peripheralsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1PeripheralsReportOut"])
            ).optional(),
            "kioskAppStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1KioskAppStatusReportOut"])
            ).optional(),
            "networkDiagnosticsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkDiagnosticsReportOut"])
            ).optional(),
            "audioStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1AudioStatusReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceOut"])
    types["GoogleChromeManagementV1TelemetryUserDeviceIn"] = t.struct(
        {"deviceId": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryUserDeviceIn"])
    types["GoogleChromeManagementV1TelemetryUserDeviceOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "audioStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1AudioStatusReportOut"])
            ).optional(),
            "peripheralsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1PeripheralsReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserDeviceOut"])
    types["GoogleChromeManagementV1NetworkInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkInfoIn"])
    types["GoogleChromeManagementV1NetworkInfoOut"] = t.struct(
        {
            "networkDevices": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkDeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkInfoOut"])
    types["GoogleChromeManagementV1DeviceHardwareCountReportIn"] = t.struct(
        {"bucket": t.string().optional(), "count": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
    types["GoogleChromeManagementV1DeviceHardwareCountReportOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
    types["GoogleChromeManagementV1CpuTemperatureInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuTemperatureInfoIn"])
    types["GoogleChromeManagementV1CpuTemperatureInfoOut"] = t.struct(
        {
            "label": t.string().optional(),
            "temperatureCelsius": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuTemperatureInfoOut"])
    types["GoogleChromeManagementV1HeartbeatStatusReportIn"] = t.struct(
        {"state": t.string().optional(), "reportTime": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1HeartbeatStatusReportIn"])
    types["GoogleChromeManagementV1HeartbeatStatusReportOut"] = t.struct(
        {
            "state": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1HeartbeatStatusReportOut"])
    types[
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn"
    ] = t.struct(
        {
            "deviceAueCountReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceAueCountReportIn"])
            ).optional()
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn"
        ]
    )
    types[
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
    ] = t.struct(
        {
            "deviceAueCountReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceAueCountReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
        ]
    )
    types["GoogleChromeManagementV1GraphicsAdapterInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoIn"])
    types["GoogleChromeManagementV1GraphicsAdapterInfoOut"] = t.struct(
        {
            "driverVersion": t.string().optional(),
            "deviceId": t.string().optional(),
            "adapter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"])
    types["GoogleChromeManagementV1DiskInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DiskInfoIn"])
    types["GoogleChromeManagementV1DiskInfoOut"] = t.struct(
        {
            "writeTimeThisSession": t.string().optional(),
            "discardTimeThisSession": t.string().optional(),
            "model": t.string().optional(),
            "volumeIds": t.array(t.string()).optional(),
            "ioTimeThisSession": t.string().optional(),
            "bytesReadThisSession": t.string().optional(),
            "manufacturer": t.string().optional(),
            "health": t.string().optional(),
            "type": t.string().optional(),
            "serialNumber": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "readTimeThisSession": t.string().optional(),
            "bytesWrittenThisSession": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DiskInfoOut"])
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"] = t.struct(
        {
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"])
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"] = t.struct(
        {
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"])
    types["GoogleChromeManagementV1BatteryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportIn"])
    types["GoogleChromeManagementV1BatteryStatusReportOut"] = t.struct(
        {
            "cycleCount": t.integer().optional(),
            "batteryHealth": t.string().optional(),
            "serialNumber": t.string().optional(),
            "fullChargeCapacity": t.string().optional(),
            "reportTime": t.string().optional(),
            "sample": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatterySampleReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
    types["GoogleChromeManagementV1DeviceAueCountReportIn"] = t.struct(
        {
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "aueYear": t.string().optional(),
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportIn"])
    types["GoogleChromeManagementV1DeviceAueCountReportOut"] = t.struct(
        {
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "aueYear": t.string().optional(),
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportOut"])
    types["GoogleChromeManagementV1KioskAppStatusReportIn"] = t.struct(
        {
            "appVersion": t.string().optional(),
            "appId": t.string().optional(),
            "reportTime": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1KioskAppStatusReportIn"])
    types["GoogleChromeManagementV1KioskAppStatusReportOut"] = t.struct(
        {
            "appVersion": t.string().optional(),
            "appId": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1KioskAppStatusReportOut"])
    types["GoogleChromeManagementV1BatteryInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryInfoIn"])
    types["GoogleChromeManagementV1BatteryInfoOut"] = t.struct(
        {
            "manufactureDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "manufacturer": t.string().optional(),
            "designMinVoltage": t.integer().optional(),
            "serialNumber": t.string().optional(),
            "technology": t.string().optional(),
            "designCapacity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryInfoOut"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"])
    types["GoogleChromeManagementV1ListTelemetryEventsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "telemetryEvents": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryEventIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryEventsResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryEventsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "telemetryEvents": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryEventOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryEventsResponseOut"])
    types["GoogleChromeManagementV1TelemetryEventIn"] = t.struct(
        {"reportTime": t.string().optional(), "eventType": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryEventIn"])
    types["GoogleChromeManagementV1TelemetryEventOut"] = t.struct(
        {
            "name": t.string().optional(),
            "reportTime": t.string().optional(),
            "device": t.proxy(
                renames["GoogleChromeManagementV1TelemetryDeviceInfoOut"]
            ).optional(),
            "httpsLatencyChangeEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"]
            ).optional(),
            "user": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUserInfoOut"]
            ).optional(),
            "usbPeripheralsEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut"]
            ).optional(),
            "audioSevereUnderrunEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"]
            ).optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryEventOut"])
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"
    ] = t.struct(
        {
            "pendingBrowserUpdateCount": t.string().optional(),
            "noRecentActivityCount": t.string().optional(),
            "recentlyEnrolledCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
    ] = t.struct(
        {
            "pendingBrowserUpdateCount": t.string().optional(),
            "noRecentActivityCount": t.string().optional(),
            "recentlyEnrolledCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
        ]
    )
    types["GoogleChromeManagementV1DeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DeviceIn"])
    types["GoogleChromeManagementV1DeviceOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "machine": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceOut"])
    types["GoogleChromeManagementV1TelemetryUserInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryUserInfoIn"])
    types["GoogleChromeManagementV1TelemetryUserInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserInfoOut"])
    types["GoogleChromeManagementV1StorageInfoIn"] = t.struct(
        {
            "availableDiskBytes": t.string().optional(),
            "totalDiskBytes": t.string().optional(),
            "volume": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageInfoDiskVolumeIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoIn"])
    types["GoogleChromeManagementV1StorageInfoOut"] = t.struct(
        {
            "availableDiskBytes": t.string().optional(),
            "totalDiskBytes": t.string().optional(),
            "volume": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageInfoDiskVolumeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoOut"])
    types["GoogleChromeManagementV1ListTelemetryUsersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "telemetryUsers": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryUsersResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryUsersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "telemetryUsers": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryUsersResponseOut"])
    types["GoogleChromeManagementV1StorageInfoDiskVolumeIn"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "storageTotalBytes": t.string().optional(),
            "storageFreeBytes": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeIn"])
    types["GoogleChromeManagementV1StorageInfoDiskVolumeOut"] = t.struct(
        {
            "volumeId": t.string().optional(),
            "storageTotalBytes": t.string().optional(),
            "storageFreeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeOut"])
    types["GoogleChromeManagementV1MemoryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportIn"])
    types["GoogleChromeManagementV1MemoryStatusReportOut"] = t.struct(
        {
            "pageFaults": t.integer().optional(),
            "systemRamFreeBytes": t.string().optional(),
            "sampleFrequency": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
    types["GoogleChromeManagementV1TouchScreenDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceIn"])
    types["GoogleChromeManagementV1TouchScreenDeviceOut"] = t.struct(
        {
            "stylusCapable": t.boolean().optional(),
            "touchPointCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceOut"])
    types["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn"] = t.struct(
        {
            "httpsLatencyRoutineData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"]
            ).optional(),
            "httpsLatencyState": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn"])
    types["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"] = t.struct(
        {
            "httpsLatencyRoutineData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"]
            ).optional(),
            "httpsLatencyState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"])
    types["GoogleChromeManagementV1TouchScreenInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TouchScreenInfoIn"])
    types["GoogleChromeManagementV1TouchScreenInfoOut"] = t.struct(
        {
            "touchpadLibrary": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TouchScreenDeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TouchScreenInfoOut"])
    types["GoogleChromeManagementV1AudioStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AudioStatusReportIn"])
    types["GoogleChromeManagementV1AudioStatusReportOut"] = t.struct(
        {
            "outputMute": t.boolean().optional(),
            "inputMute": t.boolean().optional(),
            "outputDevice": t.string().optional(),
            "outputVolume": t.integer().optional(),
            "reportTime": t.string().optional(),
            "inputGain": t.integer().optional(),
            "inputDevice": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AudioStatusReportOut"])
    types["GoogleChromeManagementV1CpuInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuInfoIn"])
    types["GoogleChromeManagementV1CpuInfoOut"] = t.struct(
        {
            "maxClockSpeed": t.integer().optional(),
            "keylockerSupported": t.boolean().optional(),
            "keylockerConfigured": t.boolean().optional(),
            "model": t.string().optional(),
            "architecture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuInfoOut"])
    types["GoogleChromeManagementV1CountChromeVersionsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "browserVersions": t.array(
                t.proxy(renames["GoogleChromeManagementV1BrowserVersionIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeVersionsResponseIn"])
    types["GoogleChromeManagementV1CountChromeVersionsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "browserVersions": t.array(
                t.proxy(renames["GoogleChromeManagementV1BrowserVersionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeVersionsResponseOut"])
    types["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"])
    types["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"] = t.struct(
        {
            "problem": t.string().optional(),
            "latency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"])
    types["GoogleChromeManagementV1PeripheralsReportIn"] = t.struct(
        {
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
            ).optional()
        }
    ).named(renames["GoogleChromeManagementV1PeripheralsReportIn"])
    types["GoogleChromeManagementV1PeripheralsReportOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1PeripheralsReportOut"])
    types["GoogleChromeManagementV1GraphicsInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsInfoIn"])
    types["GoogleChromeManagementV1GraphicsInfoOut"] = t.struct(
        {
            "touchScreenInfo": t.proxy(
                renames["GoogleChromeManagementV1TouchScreenInfoOut"]
            ).optional(),
            "eprivacySupported": t.boolean().optional(),
            "displayDevices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DisplayDeviceOut"])
            ).optional(),
            "adapterInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsInfoOut"])
    types["GoogleChromeManagementV1StorageStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1StorageStatusReportIn"])
    types["GoogleChromeManagementV1StorageStatusReportOut"] = t.struct(
        {
            "disk": t.array(
                t.proxy(renames["GoogleChromeManagementV1DiskInfoOut"])
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageStatusReportOut"])
    types["GoogleChromeManagementV1OsUpdateStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusIn"])
    types["GoogleChromeManagementV1OsUpdateStatusOut"] = t.struct(
        {
            "lastRebootTime": t.string().optional(),
            "updateState": t.string().optional(),
            "newPlatformVersion": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "lastUpdateCheckTime": t.string().optional(),
            "newRequestedPlatformVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"] = t.struct(
        {
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionState": t.string().optional(),
            "encryptionAlgorithm": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"])
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"] = t.struct(
        {
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionState": t.string().optional(),
            "encryptionAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"])

    functions = {}
    functions["customersTelemetryDevicesGet"] = chromemanagement.get(
        "v1/{parent}/telemetry/devices",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryDevicesList"] = chromemanagement.get(
        "v1/{parent}/telemetry/devices",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryUsersGet"] = chromemanagement.get(
        "v1/{parent}/telemetry/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryUsersList"] = chromemanagement.get(
        "v1/{parent}/telemetry/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryEventsList"] = chromemanagement.get(
        "v1/{parent}/telemetry/events",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersAppsCountChromeAppRequests"] = chromemanagement.get(
        "v1/{customer}/apps:countChromeAppRequests",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "customer": t.string(),
                "pageToken": t.string().optional(),
                "orgUnitId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersAppsWebGet"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersAppsChromeGet"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersAppsAndroidGet"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1AppDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsFindInstalledAppDevices"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountInstalledApps"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountChromeVersions"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesThatNeedAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountChromeHardwareFleetDevices"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeBrowsersNeedingAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesReachingAutoExpirationDate"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeDevicesReachingAutoExpirationDate",
        t.struct(
            {
                "orgUnitId": t.string().optional(),
                "maxAueDate": t.string().optional(),
                "minAueDate": t.string().optional(),
                "customer": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chromemanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
