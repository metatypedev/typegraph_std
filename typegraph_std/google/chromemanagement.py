from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_chromemanagement() -> Import:
    chromemanagement = HTTPRuntime("https://chromemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromemanagement_1_ErrorResponse",
        "GoogleChromeManagementV1DeviceHardwareCountReportIn": "_chromemanagement_2_GoogleChromeManagementV1DeviceHardwareCountReportIn",
        "GoogleChromeManagementV1DeviceHardwareCountReportOut": "_chromemanagement_3_GoogleChromeManagementV1DeviceHardwareCountReportOut",
        "GoogleChromeManagementV1ListTelemetryEventsResponseIn": "_chromemanagement_4_GoogleChromeManagementV1ListTelemetryEventsResponseIn",
        "GoogleChromeManagementV1ListTelemetryEventsResponseOut": "_chromemanagement_5_GoogleChromeManagementV1ListTelemetryEventsResponseOut",
        "GoogleChromeManagementV1CountInstalledAppsResponseIn": "_chromemanagement_6_GoogleChromeManagementV1CountInstalledAppsResponseIn",
        "GoogleChromeManagementV1CountInstalledAppsResponseOut": "_chromemanagement_7_GoogleChromeManagementV1CountInstalledAppsResponseOut",
        "GoogleChromeManagementV1StorageStatusReportIn": "_chromemanagement_8_GoogleChromeManagementV1StorageStatusReportIn",
        "GoogleChromeManagementV1StorageStatusReportOut": "_chromemanagement_9_GoogleChromeManagementV1StorageStatusReportOut",
        "GoogleChromeManagementV1CpuTemperatureInfoIn": "_chromemanagement_10_GoogleChromeManagementV1CpuTemperatureInfoIn",
        "GoogleChromeManagementV1CpuTemperatureInfoOut": "_chromemanagement_11_GoogleChromeManagementV1CpuTemperatureInfoOut",
        "GoogleChromeManagementV1OsUpdateStatusIn": "_chromemanagement_12_GoogleChromeManagementV1OsUpdateStatusIn",
        "GoogleChromeManagementV1OsUpdateStatusOut": "_chromemanagement_13_GoogleChromeManagementV1OsUpdateStatusOut",
        "GoogleChromeManagementV1CpuInfoIn": "_chromemanagement_14_GoogleChromeManagementV1CpuInfoIn",
        "GoogleChromeManagementV1CpuInfoOut": "_chromemanagement_15_GoogleChromeManagementV1CpuInfoOut",
        "GoogleChromeManagementV1StorageInfoIn": "_chromemanagement_16_GoogleChromeManagementV1StorageInfoIn",
        "GoogleChromeManagementV1StorageInfoOut": "_chromemanagement_17_GoogleChromeManagementV1StorageInfoOut",
        "GoogleChromeManagementV1AndroidAppPermissionIn": "_chromemanagement_18_GoogleChromeManagementV1AndroidAppPermissionIn",
        "GoogleChromeManagementV1AndroidAppPermissionOut": "_chromemanagement_19_GoogleChromeManagementV1AndroidAppPermissionOut",
        "GoogleChromeManagementV1DiskInfoIn": "_chromemanagement_20_GoogleChromeManagementV1DiskInfoIn",
        "GoogleChromeManagementV1DiskInfoOut": "_chromemanagement_21_GoogleChromeManagementV1DiskInfoOut",
        "GoogleChromeManagementV1ChromeAppRequestIn": "_chromemanagement_22_GoogleChromeManagementV1ChromeAppRequestIn",
        "GoogleChromeManagementV1ChromeAppRequestOut": "_chromemanagement_23_GoogleChromeManagementV1ChromeAppRequestOut",
        "GoogleChromeManagementV1BatterySampleReportIn": "_chromemanagement_24_GoogleChromeManagementV1BatterySampleReportIn",
        "GoogleChromeManagementV1BatterySampleReportOut": "_chromemanagement_25_GoogleChromeManagementV1BatterySampleReportOut",
        "GoogleChromeManagementV1TelemetryUserInfoIn": "_chromemanagement_26_GoogleChromeManagementV1TelemetryUserInfoIn",
        "GoogleChromeManagementV1TelemetryUserInfoOut": "_chromemanagement_27_GoogleChromeManagementV1TelemetryUserInfoOut",
        "GoogleChromeManagementV1DisplayInfoIn": "_chromemanagement_28_GoogleChromeManagementV1DisplayInfoIn",
        "GoogleChromeManagementV1DisplayInfoOut": "_chromemanagement_29_GoogleChromeManagementV1DisplayInfoOut",
        "GoogleTypeDateIn": "_chromemanagement_30_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_chromemanagement_31_GoogleTypeDateOut",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseIn": "_chromemanagement_32_GoogleChromeManagementV1FindInstalledAppDevicesResponseIn",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseOut": "_chromemanagement_33_GoogleChromeManagementV1FindInstalledAppDevicesResponseOut",
        "GoogleChromeManagementV1NetworkStatusReportIn": "_chromemanagement_34_GoogleChromeManagementV1NetworkStatusReportIn",
        "GoogleChromeManagementV1NetworkStatusReportOut": "_chromemanagement_35_GoogleChromeManagementV1NetworkStatusReportOut",
        "GoogleChromeManagementV1TelemetryEventIn": "_chromemanagement_36_GoogleChromeManagementV1TelemetryEventIn",
        "GoogleChromeManagementV1TelemetryEventOut": "_chromemanagement_37_GoogleChromeManagementV1TelemetryEventOut",
        "GoogleChromeManagementV1BatteryInfoIn": "_chromemanagement_38_GoogleChromeManagementV1BatteryInfoIn",
        "GoogleChromeManagementV1BatteryInfoOut": "_chromemanagement_39_GoogleChromeManagementV1BatteryInfoOut",
        "GoogleChromeManagementV1UsbPeripheralReportIn": "_chromemanagement_40_GoogleChromeManagementV1UsbPeripheralReportIn",
        "GoogleChromeManagementV1UsbPeripheralReportOut": "_chromemanagement_41_GoogleChromeManagementV1UsbPeripheralReportOut",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn": "_chromemanagement_42_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut": "_chromemanagement_43_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut",
        "GoogleChromeManagementV1TouchScreenInfoIn": "_chromemanagement_44_GoogleChromeManagementV1TouchScreenInfoIn",
        "GoogleChromeManagementV1TouchScreenInfoOut": "_chromemanagement_45_GoogleChromeManagementV1TouchScreenInfoOut",
        "GoogleChromeManagementV1ChromeAppPermissionIn": "_chromemanagement_46_GoogleChromeManagementV1ChromeAppPermissionIn",
        "GoogleChromeManagementV1ChromeAppPermissionOut": "_chromemanagement_47_GoogleChromeManagementV1ChromeAppPermissionOut",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn": "_chromemanagement_48_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut": "_chromemanagement_49_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut",
        "GoogleChromeManagementV1MemoryStatusReportIn": "_chromemanagement_50_GoogleChromeManagementV1MemoryStatusReportIn",
        "GoogleChromeManagementV1MemoryStatusReportOut": "_chromemanagement_51_GoogleChromeManagementV1MemoryStatusReportOut",
        "GoogleChromeManagementV1DeviceIn": "_chromemanagement_52_GoogleChromeManagementV1DeviceIn",
        "GoogleChromeManagementV1DeviceOut": "_chromemanagement_53_GoogleChromeManagementV1DeviceOut",
        "GoogleChromeManagementV1GraphicsInfoIn": "_chromemanagement_54_GoogleChromeManagementV1GraphicsInfoIn",
        "GoogleChromeManagementV1GraphicsInfoOut": "_chromemanagement_55_GoogleChromeManagementV1GraphicsInfoOut",
        "GoogleRpcStatusIn": "_chromemanagement_56_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_chromemanagement_57_GoogleRpcStatusOut",
        "GoogleChromeManagementV1AudioStatusReportIn": "_chromemanagement_58_GoogleChromeManagementV1AudioStatusReportIn",
        "GoogleChromeManagementV1AudioStatusReportOut": "_chromemanagement_59_GoogleChromeManagementV1AudioStatusReportOut",
        "GoogleChromeManagementV1TelemetryDeviceInfoIn": "_chromemanagement_60_GoogleChromeManagementV1TelemetryDeviceInfoIn",
        "GoogleChromeManagementV1TelemetryDeviceInfoOut": "_chromemanagement_61_GoogleChromeManagementV1TelemetryDeviceInfoOut",
        "GoogleChromeManagementV1AppDetailsIn": "_chromemanagement_62_GoogleChromeManagementV1AppDetailsIn",
        "GoogleChromeManagementV1AppDetailsOut": "_chromemanagement_63_GoogleChromeManagementV1AppDetailsOut",
        "GoogleChromeManagementV1MemoryInfoIn": "_chromemanagement_64_GoogleChromeManagementV1MemoryInfoIn",
        "GoogleChromeManagementV1MemoryInfoOut": "_chromemanagement_65_GoogleChromeManagementV1MemoryInfoOut",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn": "_chromemanagement_66_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut": "_chromemanagement_67_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoIn": "_chromemanagement_68_GoogleChromeManagementV1TotalMemoryEncryptionInfoIn",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoOut": "_chromemanagement_69_GoogleChromeManagementV1TotalMemoryEncryptionInfoOut",
        "GoogleChromeManagementV1CpuStatusReportIn": "_chromemanagement_70_GoogleChromeManagementV1CpuStatusReportIn",
        "GoogleChromeManagementV1CpuStatusReportOut": "_chromemanagement_71_GoogleChromeManagementV1CpuStatusReportOut",
        "GoogleChromeManagementV1DeviceAueCountReportIn": "_chromemanagement_72_GoogleChromeManagementV1DeviceAueCountReportIn",
        "GoogleChromeManagementV1DeviceAueCountReportOut": "_chromemanagement_73_GoogleChromeManagementV1DeviceAueCountReportOut",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataIn": "_chromemanagement_74_GoogleChromeManagementV1HttpsLatencyRoutineDataIn",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataOut": "_chromemanagement_75_GoogleChromeManagementV1HttpsLatencyRoutineDataOut",
        "GoogleChromeManagementV1InstalledAppIn": "_chromemanagement_76_GoogleChromeManagementV1InstalledAppIn",
        "GoogleChromeManagementV1InstalledAppOut": "_chromemanagement_77_GoogleChromeManagementV1InstalledAppOut",
        "GoogleChromeManagementV1ThunderboltInfoIn": "_chromemanagement_78_GoogleChromeManagementV1ThunderboltInfoIn",
        "GoogleChromeManagementV1ThunderboltInfoOut": "_chromemanagement_79_GoogleChromeManagementV1ThunderboltInfoOut",
        "GoogleChromeManagementV1GraphicsAdapterInfoIn": "_chromemanagement_80_GoogleChromeManagementV1GraphicsAdapterInfoIn",
        "GoogleChromeManagementV1GraphicsAdapterInfoOut": "_chromemanagement_81_GoogleChromeManagementV1GraphicsAdapterInfoOut",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn": "_chromemanagement_82_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut": "_chromemanagement_83_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut",
        "GoogleChromeManagementV1TelemetryUserIn": "_chromemanagement_84_GoogleChromeManagementV1TelemetryUserIn",
        "GoogleChromeManagementV1TelemetryUserOut": "_chromemanagement_85_GoogleChromeManagementV1TelemetryUserOut",
        "GoogleChromeManagementV1ChromeAppSiteAccessIn": "_chromemanagement_86_GoogleChromeManagementV1ChromeAppSiteAccessIn",
        "GoogleChromeManagementV1ChromeAppSiteAccessOut": "_chromemanagement_87_GoogleChromeManagementV1ChromeAppSiteAccessOut",
        "GoogleChromeManagementV1PeripheralsReportIn": "_chromemanagement_88_GoogleChromeManagementV1PeripheralsReportIn",
        "GoogleChromeManagementV1PeripheralsReportOut": "_chromemanagement_89_GoogleChromeManagementV1PeripheralsReportOut",
        "GoogleChromeManagementV1TelemetryUserDeviceIn": "_chromemanagement_90_GoogleChromeManagementV1TelemetryUserDeviceIn",
        "GoogleChromeManagementV1TelemetryUserDeviceOut": "_chromemanagement_91_GoogleChromeManagementV1TelemetryUserDeviceOut",
        "GoogleChromeManagementV1DisplayDeviceIn": "_chromemanagement_92_GoogleChromeManagementV1DisplayDeviceIn",
        "GoogleChromeManagementV1DisplayDeviceOut": "_chromemanagement_93_GoogleChromeManagementV1DisplayDeviceOut",
        "GoogleChromeManagementV1NetworkDeviceIn": "_chromemanagement_94_GoogleChromeManagementV1NetworkDeviceIn",
        "GoogleChromeManagementV1NetworkDeviceOut": "_chromemanagement_95_GoogleChromeManagementV1NetworkDeviceOut",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseIn": "_chromemanagement_96_GoogleChromeManagementV1ListTelemetryDevicesResponseIn",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseOut": "_chromemanagement_97_GoogleChromeManagementV1ListTelemetryDevicesResponseOut",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn": "_chromemanagement_98_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut": "_chromemanagement_99_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut",
        "GoogleChromeManagementV1BatteryStatusReportIn": "_chromemanagement_100_GoogleChromeManagementV1BatteryStatusReportIn",
        "GoogleChromeManagementV1BatteryStatusReportOut": "_chromemanagement_101_GoogleChromeManagementV1BatteryStatusReportOut",
        "GoogleChromeManagementV1GraphicsStatusReportIn": "_chromemanagement_102_GoogleChromeManagementV1GraphicsStatusReportIn",
        "GoogleChromeManagementV1GraphicsStatusReportOut": "_chromemanagement_103_GoogleChromeManagementV1GraphicsStatusReportOut",
        "GoogleChromeManagementV1NetworkInfoIn": "_chromemanagement_104_GoogleChromeManagementV1NetworkInfoIn",
        "GoogleChromeManagementV1NetworkInfoOut": "_chromemanagement_105_GoogleChromeManagementV1NetworkInfoOut",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseIn": "_chromemanagement_106_GoogleChromeManagementV1CountChromeAppRequestsResponseIn",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseOut": "_chromemanagement_107_GoogleChromeManagementV1CountChromeAppRequestsResponseOut",
        "GoogleChromeManagementV1TouchScreenDeviceIn": "_chromemanagement_108_GoogleChromeManagementV1TouchScreenDeviceIn",
        "GoogleChromeManagementV1TouchScreenDeviceOut": "_chromemanagement_109_GoogleChromeManagementV1TouchScreenDeviceOut",
        "GoogleChromeManagementV1ChromeAppInfoIn": "_chromemanagement_110_GoogleChromeManagementV1ChromeAppInfoIn",
        "GoogleChromeManagementV1ChromeAppInfoOut": "_chromemanagement_111_GoogleChromeManagementV1ChromeAppInfoOut",
        "GoogleChromeManagementV1TelemetryDeviceIn": "_chromemanagement_112_GoogleChromeManagementV1TelemetryDeviceIn",
        "GoogleChromeManagementV1TelemetryDeviceOut": "_chromemanagement_113_GoogleChromeManagementV1TelemetryDeviceOut",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn": "_chromemanagement_114_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut": "_chromemanagement_115_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn": "_chromemanagement_116_GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut": "_chromemanagement_117_GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut",
        "GoogleChromeManagementV1NetworkDiagnosticsReportIn": "_chromemanagement_118_GoogleChromeManagementV1NetworkDiagnosticsReportIn",
        "GoogleChromeManagementV1NetworkDiagnosticsReportOut": "_chromemanagement_119_GoogleChromeManagementV1NetworkDiagnosticsReportOut",
        "GoogleChromeManagementV1AndroidAppInfoIn": "_chromemanagement_120_GoogleChromeManagementV1AndroidAppInfoIn",
        "GoogleChromeManagementV1AndroidAppInfoOut": "_chromemanagement_121_GoogleChromeManagementV1AndroidAppInfoOut",
        "GoogleChromeManagementV1CountChromeVersionsResponseIn": "_chromemanagement_122_GoogleChromeManagementV1CountChromeVersionsResponseIn",
        "GoogleChromeManagementV1CountChromeVersionsResponseOut": "_chromemanagement_123_GoogleChromeManagementV1CountChromeVersionsResponseOut",
        "GoogleChromeManagementV1ListTelemetryUsersResponseIn": "_chromemanagement_124_GoogleChromeManagementV1ListTelemetryUsersResponseIn",
        "GoogleChromeManagementV1ListTelemetryUsersResponseOut": "_chromemanagement_125_GoogleChromeManagementV1ListTelemetryUsersResponseOut",
        "GoogleChromeManagementV1StorageInfoDiskVolumeIn": "_chromemanagement_126_GoogleChromeManagementV1StorageInfoDiskVolumeIn",
        "GoogleChromeManagementV1StorageInfoDiskVolumeOut": "_chromemanagement_127_GoogleChromeManagementV1StorageInfoDiskVolumeOut",
        "GoogleChromeManagementV1BootPerformanceReportIn": "_chromemanagement_128_GoogleChromeManagementV1BootPerformanceReportIn",
        "GoogleChromeManagementV1BootPerformanceReportOut": "_chromemanagement_129_GoogleChromeManagementV1BootPerformanceReportOut",
        "GoogleChromeManagementV1BrowserVersionIn": "_chromemanagement_130_GoogleChromeManagementV1BrowserVersionIn",
        "GoogleChromeManagementV1BrowserVersionOut": "_chromemanagement_131_GoogleChromeManagementV1BrowserVersionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleChromeManagementV1CountInstalledAppsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseIn"])
    types["GoogleChromeManagementV1CountInstalledAppsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseOut"])
    types["GoogleChromeManagementV1StorageStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1StorageStatusReportIn"])
    types["GoogleChromeManagementV1StorageStatusReportOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "disk": t.array(
                t.proxy(renames["GoogleChromeManagementV1DiskInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageStatusReportOut"])
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
    types["GoogleChromeManagementV1OsUpdateStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusIn"])
    types["GoogleChromeManagementV1OsUpdateStatusOut"] = t.struct(
        {
            "lastRebootTime": t.string().optional(),
            "newRequestedPlatformVersion": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "updateState": t.string().optional(),
            "lastUpdateCheckTime": t.string().optional(),
            "newPlatformVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
    types["GoogleChromeManagementV1CpuInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuInfoIn"])
    types["GoogleChromeManagementV1CpuInfoOut"] = t.struct(
        {
            "keylockerSupported": t.boolean().optional(),
            "model": t.string().optional(),
            "architecture": t.string().optional(),
            "keylockerConfigured": t.boolean().optional(),
            "maxClockSpeed": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuInfoOut"])
    types["GoogleChromeManagementV1StorageInfoIn"] = t.struct(
        {
            "volume": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageInfoDiskVolumeIn"])
            ).optional(),
            "totalDiskBytes": t.string().optional(),
            "availableDiskBytes": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoIn"])
    types["GoogleChromeManagementV1StorageInfoOut"] = t.struct(
        {
            "volume": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageInfoDiskVolumeOut"])
            ).optional(),
            "totalDiskBytes": t.string().optional(),
            "availableDiskBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoOut"])
    types["GoogleChromeManagementV1AndroidAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionIn"])
    types["GoogleChromeManagementV1AndroidAppPermissionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionOut"])
    types["GoogleChromeManagementV1DiskInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DiskInfoIn"])
    types["GoogleChromeManagementV1DiskInfoOut"] = t.struct(
        {
            "health": t.string().optional(),
            "volumeIds": t.array(t.string()).optional(),
            "sizeBytes": t.string().optional(),
            "ioTimeThisSession": t.string().optional(),
            "readTimeThisSession": t.string().optional(),
            "manufacturer": t.string().optional(),
            "bytesWrittenThisSession": t.string().optional(),
            "type": t.string().optional(),
            "discardTimeThisSession": t.string().optional(),
            "serialNumber": t.string().optional(),
            "writeTimeThisSession": t.string().optional(),
            "model": t.string().optional(),
            "bytesReadThisSession": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DiskInfoOut"])
    types["GoogleChromeManagementV1ChromeAppRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
    types["GoogleChromeManagementV1ChromeAppRequestOut"] = t.struct(
        {
            "detailUri": t.string().optional(),
            "appDetails": t.string().optional(),
            "latestRequestTime": t.string().optional(),
            "requestCount": t.string().optional(),
            "iconUri": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
    types["GoogleChromeManagementV1BatterySampleReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatterySampleReportIn"])
    types["GoogleChromeManagementV1BatterySampleReportOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "dischargeRate": t.integer().optional(),
            "chargeRate": t.integer().optional(),
            "current": t.string().optional(),
            "status": t.string().optional(),
            "voltage": t.string().optional(),
            "remainingCapacity": t.string().optional(),
            "temperature": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatterySampleReportOut"])
    types["GoogleChromeManagementV1TelemetryUserInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryUserInfoIn"])
    types["GoogleChromeManagementV1TelemetryUserInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserInfoOut"])
    types["GoogleChromeManagementV1DisplayInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayInfoIn"])
    types["GoogleChromeManagementV1DisplayInfoOut"] = t.struct(
        {
            "isInternal": t.boolean().optional(),
            "resolutionWidth": t.integer().optional(),
            "displayName": t.string().optional(),
            "refreshRate": t.integer().optional(),
            "deviceId": t.string().optional(),
            "resolutionHeight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayInfoOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"])
    types["GoogleChromeManagementV1NetworkStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportIn"])
    types["GoogleChromeManagementV1NetworkStatusReportOut"] = t.struct(
        {
            "wifiLinkQuality": t.string().optional(),
            "connectionType": t.string().optional(),
            "lanIpAddress": t.string().optional(),
            "transmissionBitRateMbps": t.string().optional(),
            "gatewayIpAddress": t.string().optional(),
            "guid": t.string().optional(),
            "wifiPowerManagementEnabled": t.boolean().optional(),
            "transmissionPowerDbm": t.integer().optional(),
            "sampleFrequency": t.string().optional(),
            "encryptionOn": t.boolean().optional(),
            "reportTime": t.string().optional(),
            "receivingBitRateMbps": t.string().optional(),
            "signalStrengthDbm": t.integer().optional(),
            "connectionState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
    types["GoogleChromeManagementV1TelemetryEventIn"] = t.struct(
        {"eventType": t.string().optional(), "reportTime": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryEventIn"])
    types["GoogleChromeManagementV1TelemetryEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "audioSevereUnderrunEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"]
            ).optional(),
            "device": t.proxy(
                renames["GoogleChromeManagementV1TelemetryDeviceInfoOut"]
            ).optional(),
            "httpsLatencyChangeEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"]
            ).optional(),
            "usbPeripheralsEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut"]
            ).optional(),
            "name": t.string().optional(),
            "user": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUserInfoOut"]
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryEventOut"])
    types["GoogleChromeManagementV1BatteryInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryInfoIn"])
    types["GoogleChromeManagementV1BatteryInfoOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "designCapacity": t.string().optional(),
            "manufactureDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "designMinVoltage": t.integer().optional(),
            "technology": t.string().optional(),
            "manufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryInfoOut"])
    types["GoogleChromeManagementV1UsbPeripheralReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
    types["GoogleChromeManagementV1UsbPeripheralReportOut"] = t.struct(
        {
            "vid": t.integer().optional(),
            "firmwareVersion": t.string().optional(),
            "classId": t.integer().optional(),
            "subclassId": t.integer().optional(),
            "vendor": t.string().optional(),
            "pid": t.integer().optional(),
            "name": t.string().optional(),
            "categories": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"])
    types["GoogleChromeManagementV1TouchScreenInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TouchScreenInfoIn"])
    types["GoogleChromeManagementV1TouchScreenInfoOut"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TouchScreenDeviceOut"])
            ).optional(),
            "touchpadLibrary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TouchScreenInfoOut"])
    types["GoogleChromeManagementV1ChromeAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionIn"])
    types["GoogleChromeManagementV1ChromeAppPermissionOut"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "type": t.string().optional(),
            "accessUserData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
    types["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn"] = t.struct(
        {
            "httpsLatencyState": t.string().optional(),
            "httpsLatencyRoutineData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"]
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn"])
    types["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"] = t.struct(
        {
            "httpsLatencyState": t.string().optional(),
            "httpsLatencyRoutineData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"])
    types["GoogleChromeManagementV1MemoryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportIn"])
    types["GoogleChromeManagementV1MemoryStatusReportOut"] = t.struct(
        {
            "systemRamFreeBytes": t.string().optional(),
            "pageFaults": t.integer().optional(),
            "sampleFrequency": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
    types["GoogleChromeManagementV1DeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DeviceIn"])
    types["GoogleChromeManagementV1DeviceOut"] = t.struct(
        {
            "machine": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceOut"])
    types["GoogleChromeManagementV1GraphicsInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsInfoIn"])
    types["GoogleChromeManagementV1GraphicsInfoOut"] = t.struct(
        {
            "displayDevices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DisplayDeviceOut"])
            ).optional(),
            "touchScreenInfo": t.proxy(
                renames["GoogleChromeManagementV1TouchScreenInfoOut"]
            ).optional(),
            "adapterInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"]
            ).optional(),
            "eprivacySupported": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsInfoOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleChromeManagementV1AudioStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AudioStatusReportIn"])
    types["GoogleChromeManagementV1AudioStatusReportOut"] = t.struct(
        {
            "outputDevice": t.string().optional(),
            "inputDevice": t.string().optional(),
            "outputMute": t.boolean().optional(),
            "reportTime": t.string().optional(),
            "inputMute": t.boolean().optional(),
            "inputGain": t.integer().optional(),
            "outputVolume": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AudioStatusReportOut"])
    types["GoogleChromeManagementV1TelemetryDeviceInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceInfoIn"])
    types["GoogleChromeManagementV1TelemetryDeviceInfoOut"] = t.struct(
        {
            "orgUnitId": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceInfoOut"])
    types["GoogleChromeManagementV1AppDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AppDetailsIn"])
    types["GoogleChromeManagementV1AppDetailsOut"] = t.struct(
        {
            "chromeAppInfo": t.proxy(
                renames["GoogleChromeManagementV1ChromeAppInfoOut"]
            ).optional(),
            "isPaidApp": t.boolean().optional(),
            "privacyPolicyUri": t.string().optional(),
            "revisionId": t.string().optional(),
            "type": t.string().optional(),
            "latestPublishTime": t.string().optional(),
            "iconUri": t.string().optional(),
            "serviceError": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "name": t.string().optional(),
            "reviewNumber": t.string().optional(),
            "reviewRating": t.number().optional(),
            "firstPublishTime": t.string().optional(),
            "displayName": t.string().optional(),
            "homepageUri": t.string().optional(),
            "androidAppInfo": t.proxy(
                renames["GoogleChromeManagementV1AndroidAppInfoOut"]
            ).optional(),
            "publisher": t.string().optional(),
            "description": t.string().optional(),
            "detailUri": t.string().optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AppDetailsOut"])
    types["GoogleChromeManagementV1MemoryInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1MemoryInfoIn"])
    types["GoogleChromeManagementV1MemoryInfoOut"] = t.struct(
        {
            "totalRamBytes": t.string().optional(),
            "availableRamBytes": t.string().optional(),
            "totalMemoryEncryption": t.proxy(
                renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1MemoryInfoOut"])
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"
    ] = t.struct(
        {
            "recentlyEnrolledCount": t.string().optional(),
            "pendingBrowserUpdateCount": t.string().optional(),
            "noRecentActivityCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
    ] = t.struct(
        {
            "recentlyEnrolledCount": t.string().optional(),
            "pendingBrowserUpdateCount": t.string().optional(),
            "noRecentActivityCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
        ]
    )
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"] = t.struct(
        {
            "encryptionAlgorithm": t.string().optional(),
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionState": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"])
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"] = t.struct(
        {
            "encryptionAlgorithm": t.string().optional(),
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"])
    types["GoogleChromeManagementV1CpuStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuStatusReportIn"])
    types["GoogleChromeManagementV1CpuStatusReportOut"] = t.struct(
        {
            "sampleFrequency": t.string().optional(),
            "reportTime": t.string().optional(),
            "cpuTemperatureInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuTemperatureInfoOut"])
            ).optional(),
            "cpuUtilizationPct": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuStatusReportOut"])
    types["GoogleChromeManagementV1DeviceAueCountReportIn"] = t.struct(
        {
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "aueYear": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportIn"])
    types["GoogleChromeManagementV1DeviceAueCountReportOut"] = t.struct(
        {
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "aueYear": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportOut"])
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
    types["GoogleChromeManagementV1InstalledAppIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1InstalledAppIn"])
    types["GoogleChromeManagementV1InstalledAppOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "browserDeviceCount": t.string().optional(),
            "displayName": t.string().optional(),
            "homepageUri": t.string().optional(),
            "appInstallType": t.string().optional(),
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "osUserCount": t.string().optional(),
            "appSource": t.string().optional(),
            "appType": t.string().optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1InstalledAppOut"])
    types["GoogleChromeManagementV1ThunderboltInfoIn"] = t.struct(
        {"securityLevel": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoIn"])
    types["GoogleChromeManagementV1ThunderboltInfoOut"] = t.struct(
        {
            "securityLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
    types["GoogleChromeManagementV1GraphicsAdapterInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoIn"])
    types["GoogleChromeManagementV1GraphicsAdapterInfoOut"] = t.struct(
        {
            "adapter": t.string().optional(),
            "driverVersion": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"])
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"
    ] = t.struct(
        {
            "noRecentUserActivityCount": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
            "pendingUpdate": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut"
    ] = t.struct(
        {
            "noRecentUserActivityCount": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
            "pendingUpdate": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut"
        ]
    )
    types["GoogleChromeManagementV1TelemetryUserIn"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "customer": t.string().optional(),
            "name": t.string().optional(),
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceIn"])
            ).optional(),
            "orgUnitId": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserIn"])
    types["GoogleChromeManagementV1TelemetryUserOut"] = t.struct(
        {
            "userEmail": t.string().optional(),
            "customer": t.string().optional(),
            "name": t.string().optional(),
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceOut"])
            ).optional(),
            "orgUnitId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserOut"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessIn"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessOut"] = t.struct(
        {
            "hostMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
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
    types["GoogleChromeManagementV1DisplayDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayDeviceIn"])
    types["GoogleChromeManagementV1DisplayDeviceOut"] = t.struct(
        {
            "displayHeightMm": t.integer().optional(),
            "manufactureYear": t.integer().optional(),
            "displayName": t.string().optional(),
            "modelId": t.integer().optional(),
            "manufacturerId": t.string().optional(),
            "internal": t.boolean().optional(),
            "displayWidthMm": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayDeviceOut"])
    types["GoogleChromeManagementV1NetworkDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkDeviceIn"])
    types["GoogleChromeManagementV1NetworkDeviceOut"] = t.struct(
        {
            "macAddress": t.string().optional(),
            "mdn": t.string().optional(),
            "meid": t.string().optional(),
            "type": t.string().optional(),
            "iccid": t.string().optional(),
            "imei": t.string().optional(),
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
    types["GoogleChromeManagementV1BatteryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportIn"])
    types["GoogleChromeManagementV1BatteryStatusReportOut"] = t.struct(
        {
            "sample": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatterySampleReportOut"])
            ).optional(),
            "reportTime": t.string().optional(),
            "batteryHealth": t.string().optional(),
            "cycleCount": t.integer().optional(),
            "fullChargeCapacity": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
    types["GoogleChromeManagementV1GraphicsStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsStatusReportIn"])
    types["GoogleChromeManagementV1GraphicsStatusReportOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "displays": t.array(
                t.proxy(renames["GoogleChromeManagementV1DisplayInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsStatusReportOut"])
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
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
            ).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"])
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
            ).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"])
    types["GoogleChromeManagementV1TouchScreenDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceIn"])
    types["GoogleChromeManagementV1TouchScreenDeviceOut"] = t.struct(
        {
            "touchPointCount": t.integer().optional(),
            "stylusCapable": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceOut"])
    types["GoogleChromeManagementV1ChromeAppInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppInfoIn"])
    types["GoogleChromeManagementV1ChromeAppInfoOut"] = t.struct(
        {
            "kioskEnabled": t.boolean().optional(),
            "isKioskOnly": t.boolean().optional(),
            "isExtensionPolicySupported": t.boolean().optional(),
            "type": t.string().optional(),
            "isCwsHosted": t.boolean().optional(),
            "siteAccess": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
            ).optional(),
            "isTheme": t.boolean().optional(),
            "googleOwned": t.boolean().optional(),
            "minUserCount": t.integer().optional(),
            "permissions": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
            ).optional(),
            "supportEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppInfoOut"])
    types["GoogleChromeManagementV1TelemetryDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceIn"])
    types["GoogleChromeManagementV1TelemetryDeviceOut"] = t.struct(
        {
            "peripheralsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1PeripheralsReportOut"])
            ).optional(),
            "storageInfo": t.proxy(
                renames["GoogleChromeManagementV1StorageInfoOut"]
            ).optional(),
            "orgUnitId": t.string().optional(),
            "storageStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageStatusReportOut"])
            ).optional(),
            "name": t.string().optional(),
            "memoryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
            ).optional(),
            "customer": t.string().optional(),
            "deviceId": t.string().optional(),
            "graphicsInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsInfoOut"]
            ).optional(),
            "networkDiagnosticsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkDiagnosticsReportOut"])
            ).optional(),
            "cpuStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuStatusReportOut"])
            ).optional(),
            "audioStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1AudioStatusReportOut"])
            ).optional(),
            "batteryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
            ).optional(),
            "networkStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
            ).optional(),
            "bootPerformanceReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
            ).optional(),
            "memoryInfo": t.proxy(
                renames["GoogleChromeManagementV1MemoryInfoOut"]
            ).optional(),
            "thunderboltInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
            ).optional(),
            "cpuInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuInfoOut"])
            ).optional(),
            "osUpdateStatus": t.array(
                t.proxy(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
            ).optional(),
            "graphicsStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1GraphicsStatusReportOut"])
            ).optional(),
            "serialNumber": t.string().optional(),
            "batteryInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryInfoOut"])
            ).optional(),
            "networkInfo": t.proxy(
                renames["GoogleChromeManagementV1NetworkInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceOut"])
    types[
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn"
    ] = t.struct(
        {
            "cpuReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "memoryReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "storageReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
            ).optional(),
            "modelReports": t.array(
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
            "memoryReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "storageReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "modelReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut"]
    )
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
    types["GoogleChromeManagementV1NetworkDiagnosticsReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkDiagnosticsReportIn"])
    types["GoogleChromeManagementV1NetworkDiagnosticsReportOut"] = t.struct(
        {
            "httpsLatencyData": t.proxy(
                renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"]
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkDiagnosticsReportOut"])
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
            "storageFreeBytes": t.string().optional(),
            "volumeId": t.string().optional(),
            "storageTotalBytes": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeIn"])
    types["GoogleChromeManagementV1StorageInfoDiskVolumeOut"] = t.struct(
        {
            "storageFreeBytes": t.string().optional(),
            "volumeId": t.string().optional(),
            "storageTotalBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeOut"])
    types["GoogleChromeManagementV1BootPerformanceReportIn"] = t.struct(
        {
            "bootUpTime": t.string().optional(),
            "shutdownDuration": t.string().optional(),
            "shutdownTime": t.string().optional(),
            "shutdownReason": t.string().optional(),
            "reportTime": t.string().optional(),
            "bootUpDuration": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportIn"])
    types["GoogleChromeManagementV1BootPerformanceReportOut"] = t.struct(
        {
            "bootUpTime": t.string().optional(),
            "shutdownDuration": t.string().optional(),
            "shutdownTime": t.string().optional(),
            "shutdownReason": t.string().optional(),
            "reportTime": t.string().optional(),
            "bootUpDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
    types["GoogleChromeManagementV1BrowserVersionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BrowserVersionIn"])
    types["GoogleChromeManagementV1BrowserVersionOut"] = t.struct(
        {
            "deviceOsVersion": t.string().optional(),
            "system": t.string().optional(),
            "channel": t.string().optional(),
            "count": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BrowserVersionOut"])

    functions = {}
    functions["customersTelemetryUsersGet"] = chromemanagement.get(
        "v1/{parent}/telemetry/users",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryUsersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryDevicesGet"] = chromemanagement.get(
        "v1/{parent}/telemetry/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryEventsList"] = chromemanagement.get(
        "v1/{parent}/telemetry/events",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1ListTelemetryEventsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountChromeVersions"] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesThatNeedAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeBrowsersNeedingAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountChromeHardwareFleetDevices"] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesReachingAutoExpirationDate"
    ] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountInstalledApps"] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsFindInstalledAppDevices"] = chromemanagement.get(
        "v1/{customer}/reports:findInstalledAppDevices",
        t.struct(
            {
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "appType": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
                "appId": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersAppsCountChromeAppRequests"] = chromemanagement.get(
        "v1/{customer}/apps:countChromeAppRequests",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "pageToken": t.string().optional(),
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
    functions["customersAppsAndroidGet"] = chromemanagement.get(
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

    return Import(
        importer="chromemanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
