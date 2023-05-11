from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_chromemanagement() -> Import:
    chromemanagement = HTTPRuntime("https://chromemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_chromemanagement_1_ErrorResponse",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseIn": "_chromemanagement_2_GoogleChromeManagementV1FindInstalledAppDevicesResponseIn",
        "GoogleChromeManagementV1FindInstalledAppDevicesResponseOut": "_chromemanagement_3_GoogleChromeManagementV1FindInstalledAppDevicesResponseOut",
        "GoogleChromeManagementV1InstalledAppIn": "_chromemanagement_4_GoogleChromeManagementV1InstalledAppIn",
        "GoogleChromeManagementV1InstalledAppOut": "_chromemanagement_5_GoogleChromeManagementV1InstalledAppOut",
        "GoogleChromeManagementV1BootPerformanceReportIn": "_chromemanagement_6_GoogleChromeManagementV1BootPerformanceReportIn",
        "GoogleChromeManagementV1BootPerformanceReportOut": "_chromemanagement_7_GoogleChromeManagementV1BootPerformanceReportOut",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn": "_chromemanagement_8_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn",
        "GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut": "_chromemanagement_9_GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut",
        "GoogleChromeManagementV1CountInstalledAppsResponseIn": "_chromemanagement_10_GoogleChromeManagementV1CountInstalledAppsResponseIn",
        "GoogleChromeManagementV1CountInstalledAppsResponseOut": "_chromemanagement_11_GoogleChromeManagementV1CountInstalledAppsResponseOut",
        "GoogleChromeManagementV1GraphicsAdapterInfoIn": "_chromemanagement_12_GoogleChromeManagementV1GraphicsAdapterInfoIn",
        "GoogleChromeManagementV1GraphicsAdapterInfoOut": "_chromemanagement_13_GoogleChromeManagementV1GraphicsAdapterInfoOut",
        "GoogleChromeManagementV1DiskInfoIn": "_chromemanagement_14_GoogleChromeManagementV1DiskInfoIn",
        "GoogleChromeManagementV1DiskInfoOut": "_chromemanagement_15_GoogleChromeManagementV1DiskInfoOut",
        "GoogleChromeManagementV1DisplayInfoIn": "_chromemanagement_16_GoogleChromeManagementV1DisplayInfoIn",
        "GoogleChromeManagementV1DisplayInfoOut": "_chromemanagement_17_GoogleChromeManagementV1DisplayInfoOut",
        "GoogleChromeManagementV1ChromeAppSiteAccessIn": "_chromemanagement_18_GoogleChromeManagementV1ChromeAppSiteAccessIn",
        "GoogleChromeManagementV1ChromeAppSiteAccessOut": "_chromemanagement_19_GoogleChromeManagementV1ChromeAppSiteAccessOut",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseIn": "_chromemanagement_20_GoogleChromeManagementV1ListTelemetryDevicesResponseIn",
        "GoogleChromeManagementV1ListTelemetryDevicesResponseOut": "_chromemanagement_21_GoogleChromeManagementV1ListTelemetryDevicesResponseOut",
        "GoogleChromeManagementV1NetworkDiagnosticsReportIn": "_chromemanagement_22_GoogleChromeManagementV1NetworkDiagnosticsReportIn",
        "GoogleChromeManagementV1NetworkDiagnosticsReportOut": "_chromemanagement_23_GoogleChromeManagementV1NetworkDiagnosticsReportOut",
        "GoogleChromeManagementV1DisplayDeviceIn": "_chromemanagement_24_GoogleChromeManagementV1DisplayDeviceIn",
        "GoogleChromeManagementV1DisplayDeviceOut": "_chromemanagement_25_GoogleChromeManagementV1DisplayDeviceOut",
        "GoogleChromeManagementV1PeripheralsReportIn": "_chromemanagement_26_GoogleChromeManagementV1PeripheralsReportIn",
        "GoogleChromeManagementV1PeripheralsReportOut": "_chromemanagement_27_GoogleChromeManagementV1PeripheralsReportOut",
        "GoogleChromeManagementV1ListTelemetryEventsResponseIn": "_chromemanagement_28_GoogleChromeManagementV1ListTelemetryEventsResponseIn",
        "GoogleChromeManagementV1ListTelemetryEventsResponseOut": "_chromemanagement_29_GoogleChromeManagementV1ListTelemetryEventsResponseOut",
        "GoogleChromeManagementV1TelemetryUserInfoIn": "_chromemanagement_30_GoogleChromeManagementV1TelemetryUserInfoIn",
        "GoogleChromeManagementV1TelemetryUserInfoOut": "_chromemanagement_31_GoogleChromeManagementV1TelemetryUserInfoOut",
        "GoogleChromeManagementV1DeviceAueCountReportIn": "_chromemanagement_32_GoogleChromeManagementV1DeviceAueCountReportIn",
        "GoogleChromeManagementV1DeviceAueCountReportOut": "_chromemanagement_33_GoogleChromeManagementV1DeviceAueCountReportOut",
        "GoogleChromeManagementV1MemoryStatusReportIn": "_chromemanagement_34_GoogleChromeManagementV1MemoryStatusReportIn",
        "GoogleChromeManagementV1MemoryStatusReportOut": "_chromemanagement_35_GoogleChromeManagementV1MemoryStatusReportOut",
        "GoogleChromeManagementV1BatteryStatusReportIn": "_chromemanagement_36_GoogleChromeManagementV1BatteryStatusReportIn",
        "GoogleChromeManagementV1BatteryStatusReportOut": "_chromemanagement_37_GoogleChromeManagementV1BatteryStatusReportOut",
        "GoogleChromeManagementV1TelemetryEventIn": "_chromemanagement_38_GoogleChromeManagementV1TelemetryEventIn",
        "GoogleChromeManagementV1TelemetryEventOut": "_chromemanagement_39_GoogleChromeManagementV1TelemetryEventOut",
        "GoogleChromeManagementV1AndroidAppPermissionIn": "_chromemanagement_40_GoogleChromeManagementV1AndroidAppPermissionIn",
        "GoogleChromeManagementV1AndroidAppPermissionOut": "_chromemanagement_41_GoogleChromeManagementV1AndroidAppPermissionOut",
        "GoogleChromeManagementV1DeviceHardwareCountReportIn": "_chromemanagement_42_GoogleChromeManagementV1DeviceHardwareCountReportIn",
        "GoogleChromeManagementV1DeviceHardwareCountReportOut": "_chromemanagement_43_GoogleChromeManagementV1DeviceHardwareCountReportOut",
        "GoogleChromeManagementV1CountChromeVersionsResponseIn": "_chromemanagement_44_GoogleChromeManagementV1CountChromeVersionsResponseIn",
        "GoogleChromeManagementV1CountChromeVersionsResponseOut": "_chromemanagement_45_GoogleChromeManagementV1CountChromeVersionsResponseOut",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataIn": "_chromemanagement_46_GoogleChromeManagementV1HttpsLatencyRoutineDataIn",
        "GoogleChromeManagementV1HttpsLatencyRoutineDataOut": "_chromemanagement_47_GoogleChromeManagementV1HttpsLatencyRoutineDataOut",
        "GoogleRpcStatusIn": "_chromemanagement_48_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_chromemanagement_49_GoogleRpcStatusOut",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn": "_chromemanagement_50_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut": "_chromemanagement_51_GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut",
        "GoogleChromeManagementV1ChromeAppRequestIn": "_chromemanagement_52_GoogleChromeManagementV1ChromeAppRequestIn",
        "GoogleChromeManagementV1ChromeAppRequestOut": "_chromemanagement_53_GoogleChromeManagementV1ChromeAppRequestOut",
        "GoogleChromeManagementV1BatterySampleReportIn": "_chromemanagement_54_GoogleChromeManagementV1BatterySampleReportIn",
        "GoogleChromeManagementV1BatterySampleReportOut": "_chromemanagement_55_GoogleChromeManagementV1BatterySampleReportOut",
        "GoogleChromeManagementV1AudioStatusReportIn": "_chromemanagement_56_GoogleChromeManagementV1AudioStatusReportIn",
        "GoogleChromeManagementV1AudioStatusReportOut": "_chromemanagement_57_GoogleChromeManagementV1AudioStatusReportOut",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn": "_chromemanagement_58_GoogleChromeManagementV1TelemetryUsbPeripheralsEventIn",
        "GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut": "_chromemanagement_59_GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut",
        "GoogleChromeManagementV1MemoryInfoIn": "_chromemanagement_60_GoogleChromeManagementV1MemoryInfoIn",
        "GoogleChromeManagementV1MemoryInfoOut": "_chromemanagement_61_GoogleChromeManagementV1MemoryInfoOut",
        "GoogleChromeManagementV1TouchScreenDeviceIn": "_chromemanagement_62_GoogleChromeManagementV1TouchScreenDeviceIn",
        "GoogleChromeManagementV1TouchScreenDeviceOut": "_chromemanagement_63_GoogleChromeManagementV1TouchScreenDeviceOut",
        "GoogleChromeManagementV1ListTelemetryUsersResponseIn": "_chromemanagement_64_GoogleChromeManagementV1ListTelemetryUsersResponseIn",
        "GoogleChromeManagementV1ListTelemetryUsersResponseOut": "_chromemanagement_65_GoogleChromeManagementV1ListTelemetryUsersResponseOut",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn": "_chromemanagement_66_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut": "_chromemanagement_67_GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut",
        "GoogleChromeManagementV1ChromeAppInfoIn": "_chromemanagement_68_GoogleChromeManagementV1ChromeAppInfoIn",
        "GoogleChromeManagementV1ChromeAppInfoOut": "_chromemanagement_69_GoogleChromeManagementV1ChromeAppInfoOut",
        "GoogleChromeManagementV1StorageInfoDiskVolumeIn": "_chromemanagement_70_GoogleChromeManagementV1StorageInfoDiskVolumeIn",
        "GoogleChromeManagementV1StorageInfoDiskVolumeOut": "_chromemanagement_71_GoogleChromeManagementV1StorageInfoDiskVolumeOut",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn": "_chromemanagement_72_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseIn",
        "GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut": "_chromemanagement_73_GoogleChromeManagementV1CountChromeDevicesReachingAutoExpirationDateResponseOut",
        "GoogleChromeManagementV1DeviceIn": "_chromemanagement_74_GoogleChromeManagementV1DeviceIn",
        "GoogleChromeManagementV1DeviceOut": "_chromemanagement_75_GoogleChromeManagementV1DeviceOut",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoIn": "_chromemanagement_76_GoogleChromeManagementV1TotalMemoryEncryptionInfoIn",
        "GoogleChromeManagementV1TotalMemoryEncryptionInfoOut": "_chromemanagement_77_GoogleChromeManagementV1TotalMemoryEncryptionInfoOut",
        "GoogleChromeManagementV1AppDetailsIn": "_chromemanagement_78_GoogleChromeManagementV1AppDetailsIn",
        "GoogleChromeManagementV1AppDetailsOut": "_chromemanagement_79_GoogleChromeManagementV1AppDetailsOut",
        "GoogleChromeManagementV1TelemetryUserDeviceIn": "_chromemanagement_80_GoogleChromeManagementV1TelemetryUserDeviceIn",
        "GoogleChromeManagementV1TelemetryUserDeviceOut": "_chromemanagement_81_GoogleChromeManagementV1TelemetryUserDeviceOut",
        "GoogleChromeManagementV1NetworkDeviceIn": "_chromemanagement_82_GoogleChromeManagementV1NetworkDeviceIn",
        "GoogleChromeManagementV1NetworkDeviceOut": "_chromemanagement_83_GoogleChromeManagementV1NetworkDeviceOut",
        "GoogleChromeManagementV1CpuInfoIn": "_chromemanagement_84_GoogleChromeManagementV1CpuInfoIn",
        "GoogleChromeManagementV1CpuInfoOut": "_chromemanagement_85_GoogleChromeManagementV1CpuInfoOut",
        "GoogleChromeManagementV1CpuTemperatureInfoIn": "_chromemanagement_86_GoogleChromeManagementV1CpuTemperatureInfoIn",
        "GoogleChromeManagementV1CpuTemperatureInfoOut": "_chromemanagement_87_GoogleChromeManagementV1CpuTemperatureInfoOut",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseIn": "_chromemanagement_88_GoogleChromeManagementV1CountChromeAppRequestsResponseIn",
        "GoogleChromeManagementV1CountChromeAppRequestsResponseOut": "_chromemanagement_89_GoogleChromeManagementV1CountChromeAppRequestsResponseOut",
        "GoogleChromeManagementV1GraphicsStatusReportIn": "_chromemanagement_90_GoogleChromeManagementV1GraphicsStatusReportIn",
        "GoogleChromeManagementV1GraphicsStatusReportOut": "_chromemanagement_91_GoogleChromeManagementV1GraphicsStatusReportOut",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn": "_chromemanagement_92_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventIn",
        "GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut": "_chromemanagement_93_GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut",
        "GoogleChromeManagementV1StorageStatusReportIn": "_chromemanagement_94_GoogleChromeManagementV1StorageStatusReportIn",
        "GoogleChromeManagementV1StorageStatusReportOut": "_chromemanagement_95_GoogleChromeManagementV1StorageStatusReportOut",
        "GoogleChromeManagementV1TelemetryDeviceInfoIn": "_chromemanagement_96_GoogleChromeManagementV1TelemetryDeviceInfoIn",
        "GoogleChromeManagementV1TelemetryDeviceInfoOut": "_chromemanagement_97_GoogleChromeManagementV1TelemetryDeviceInfoOut",
        "GoogleChromeManagementV1ChromeAppPermissionIn": "_chromemanagement_98_GoogleChromeManagementV1ChromeAppPermissionIn",
        "GoogleChromeManagementV1ChromeAppPermissionOut": "_chromemanagement_99_GoogleChromeManagementV1ChromeAppPermissionOut",
        "GoogleChromeManagementV1UsbPeripheralReportIn": "_chromemanagement_100_GoogleChromeManagementV1UsbPeripheralReportIn",
        "GoogleChromeManagementV1UsbPeripheralReportOut": "_chromemanagement_101_GoogleChromeManagementV1UsbPeripheralReportOut",
        "GoogleChromeManagementV1CpuStatusReportIn": "_chromemanagement_102_GoogleChromeManagementV1CpuStatusReportIn",
        "GoogleChromeManagementV1CpuStatusReportOut": "_chromemanagement_103_GoogleChromeManagementV1CpuStatusReportOut",
        "GoogleChromeManagementV1TouchScreenInfoIn": "_chromemanagement_104_GoogleChromeManagementV1TouchScreenInfoIn",
        "GoogleChromeManagementV1TouchScreenInfoOut": "_chromemanagement_105_GoogleChromeManagementV1TouchScreenInfoOut",
        "GoogleChromeManagementV1TelemetryDeviceIn": "_chromemanagement_106_GoogleChromeManagementV1TelemetryDeviceIn",
        "GoogleChromeManagementV1TelemetryDeviceOut": "_chromemanagement_107_GoogleChromeManagementV1TelemetryDeviceOut",
        "GoogleChromeManagementV1NetworkInfoIn": "_chromemanagement_108_GoogleChromeManagementV1NetworkInfoIn",
        "GoogleChromeManagementV1NetworkInfoOut": "_chromemanagement_109_GoogleChromeManagementV1NetworkInfoOut",
        "GoogleChromeManagementV1GraphicsInfoIn": "_chromemanagement_110_GoogleChromeManagementV1GraphicsInfoIn",
        "GoogleChromeManagementV1GraphicsInfoOut": "_chromemanagement_111_GoogleChromeManagementV1GraphicsInfoOut",
        "GoogleChromeManagementV1NetworkStatusReportIn": "_chromemanagement_112_GoogleChromeManagementV1NetworkStatusReportIn",
        "GoogleChromeManagementV1NetworkStatusReportOut": "_chromemanagement_113_GoogleChromeManagementV1NetworkStatusReportOut",
        "GoogleChromeManagementV1ThunderboltInfoIn": "_chromemanagement_114_GoogleChromeManagementV1ThunderboltInfoIn",
        "GoogleChromeManagementV1ThunderboltInfoOut": "_chromemanagement_115_GoogleChromeManagementV1ThunderboltInfoOut",
        "GoogleChromeManagementV1StorageInfoIn": "_chromemanagement_116_GoogleChromeManagementV1StorageInfoIn",
        "GoogleChromeManagementV1StorageInfoOut": "_chromemanagement_117_GoogleChromeManagementV1StorageInfoOut",
        "GoogleChromeManagementV1TelemetryUserIn": "_chromemanagement_118_GoogleChromeManagementV1TelemetryUserIn",
        "GoogleChromeManagementV1TelemetryUserOut": "_chromemanagement_119_GoogleChromeManagementV1TelemetryUserOut",
        "GoogleTypeDateIn": "_chromemanagement_120_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_chromemanagement_121_GoogleTypeDateOut",
        "GoogleChromeManagementV1AndroidAppInfoIn": "_chromemanagement_122_GoogleChromeManagementV1AndroidAppInfoIn",
        "GoogleChromeManagementV1AndroidAppInfoOut": "_chromemanagement_123_GoogleChromeManagementV1AndroidAppInfoOut",
        "GoogleChromeManagementV1BatteryInfoIn": "_chromemanagement_124_GoogleChromeManagementV1BatteryInfoIn",
        "GoogleChromeManagementV1BatteryInfoOut": "_chromemanagement_125_GoogleChromeManagementV1BatteryInfoOut",
        "GoogleChromeManagementV1BrowserVersionIn": "_chromemanagement_126_GoogleChromeManagementV1BrowserVersionIn",
        "GoogleChromeManagementV1BrowserVersionOut": "_chromemanagement_127_GoogleChromeManagementV1BrowserVersionOut",
        "GoogleChromeManagementV1OsUpdateStatusIn": "_chromemanagement_128_GoogleChromeManagementV1OsUpdateStatusIn",
        "GoogleChromeManagementV1OsUpdateStatusOut": "_chromemanagement_129_GoogleChromeManagementV1OsUpdateStatusOut",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn": "_chromemanagement_130_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseIn",
        "GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut": "_chromemanagement_131_GoogleChromeManagementV1CountChromeHardwareFleetDevicesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseIn"])
    types["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1FindInstalledAppDevicesResponseOut"])
    types["GoogleChromeManagementV1InstalledAppIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1InstalledAppIn"])
    types["GoogleChromeManagementV1InstalledAppOut"] = t.struct(
        {
            "appSource": t.string().optional(),
            "disabled": t.boolean().optional(),
            "description": t.string().optional(),
            "homepageUri": t.string().optional(),
            "osUserCount": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
            "browserDeviceCount": t.string().optional(),
            "appInstallType": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "appType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1InstalledAppOut"])
    types["GoogleChromeManagementV1BootPerformanceReportIn"] = t.struct(
        {
            "shutdownDuration": t.string().optional(),
            "bootUpDuration": t.string().optional(),
            "bootUpTime": t.string().optional(),
            "reportTime": t.string().optional(),
            "shutdownReason": t.string().optional(),
            "shutdownTime": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportIn"])
    types["GoogleChromeManagementV1BootPerformanceReportOut"] = t.struct(
        {
            "shutdownDuration": t.string().optional(),
            "bootUpDuration": t.string().optional(),
            "bootUpTime": t.string().optional(),
            "reportTime": t.string().optional(),
            "shutdownReason": t.string().optional(),
            "shutdownTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventIn"])
    types["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"])
    types["GoogleChromeManagementV1CountInstalledAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppIn"])
            ).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseIn"])
    types["GoogleChromeManagementV1CountInstalledAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "installedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1InstalledAppOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountInstalledAppsResponseOut"])
    types["GoogleChromeManagementV1GraphicsAdapterInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoIn"])
    types["GoogleChromeManagementV1GraphicsAdapterInfoOut"] = t.struct(
        {
            "driverVersion": t.string().optional(),
            "adapter": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"])
    types["GoogleChromeManagementV1DiskInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DiskInfoIn"])
    types["GoogleChromeManagementV1DiskInfoOut"] = t.struct(
        {
            "readTimeThisSession": t.string().optional(),
            "discardTimeThisSession": t.string().optional(),
            "type": t.string().optional(),
            "writeTimeThisSession": t.string().optional(),
            "bytesReadThisSession": t.string().optional(),
            "ioTimeThisSession": t.string().optional(),
            "manufacturer": t.string().optional(),
            "serialNumber": t.string().optional(),
            "bytesWrittenThisSession": t.string().optional(),
            "health": t.string().optional(),
            "volumeIds": t.array(t.string()).optional(),
            "model": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DiskInfoOut"])
    types["GoogleChromeManagementV1DisplayInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayInfoIn"])
    types["GoogleChromeManagementV1DisplayInfoOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "refreshRate": t.integer().optional(),
            "resolutionWidth": t.integer().optional(),
            "displayName": t.string().optional(),
            "isInternal": t.boolean().optional(),
            "resolutionHeight": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayInfoOut"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessIn"])
    types["GoogleChromeManagementV1ChromeAppSiteAccessOut"] = t.struct(
        {
            "hostMatch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
    types["GoogleChromeManagementV1ListTelemetryDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryDevicesResponseOut"])
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
    types["GoogleChromeManagementV1DisplayDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DisplayDeviceIn"])
    types["GoogleChromeManagementV1DisplayDeviceOut"] = t.struct(
        {
            "internal": t.boolean().optional(),
            "modelId": t.integer().optional(),
            "displayWidthMm": t.integer().optional(),
            "displayName": t.string().optional(),
            "manufactureYear": t.integer().optional(),
            "manufacturerId": t.string().optional(),
            "displayHeightMm": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DisplayDeviceOut"])
    types["GoogleChromeManagementV1PeripheralsReportIn"] = t.struct(
        {
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
            ).optional()
        }
    ).named(renames["GoogleChromeManagementV1PeripheralsReportIn"])
    types["GoogleChromeManagementV1PeripheralsReportOut"] = t.struct(
        {
            "usbPeripheralReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1PeripheralsReportOut"])
    types["GoogleChromeManagementV1ListTelemetryEventsResponseIn"] = t.struct(
        {
            "telemetryEvents": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryEventIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryEventsResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryEventsResponseOut"] = t.struct(
        {
            "telemetryEvents": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryEventOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryEventsResponseOut"])
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
    types["GoogleChromeManagementV1DeviceAueCountReportIn"] = t.struct(
        {
            "aueYear": t.string().optional(),
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportIn"])
    types["GoogleChromeManagementV1DeviceAueCountReportOut"] = t.struct(
        {
            "aueYear": t.string().optional(),
            "aueMonth": t.string().optional(),
            "count": t.string().optional(),
            "expired": t.boolean().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceAueCountReportOut"])
    types["GoogleChromeManagementV1MemoryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportIn"])
    types["GoogleChromeManagementV1MemoryStatusReportOut"] = t.struct(
        {
            "pageFaults": t.integer().optional(),
            "sampleFrequency": t.string().optional(),
            "systemRamFreeBytes": t.string().optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
    types["GoogleChromeManagementV1BatteryStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportIn"])
    types["GoogleChromeManagementV1BatteryStatusReportOut"] = t.struct(
        {
            "cycleCount": t.integer().optional(),
            "serialNumber": t.string().optional(),
            "reportTime": t.string().optional(),
            "fullChargeCapacity": t.string().optional(),
            "sample": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatterySampleReportOut"])
            ).optional(),
            "batteryHealth": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
    types["GoogleChromeManagementV1TelemetryEventIn"] = t.struct(
        {"reportTime": t.string().optional(), "eventType": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryEventIn"])
    types["GoogleChromeManagementV1TelemetryEventOut"] = t.struct(
        {
            "reportTime": t.string().optional(),
            "name": t.string().optional(),
            "usbPeripheralsEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUsbPeripheralsEventOut"]
            ).optional(),
            "eventType": t.string().optional(),
            "device": t.proxy(
                renames["GoogleChromeManagementV1TelemetryDeviceInfoOut"]
            ).optional(),
            "audioSevereUnderrunEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryAudioSevereUnderrunEventOut"]
            ).optional(),
            "httpsLatencyChangeEvent": t.proxy(
                renames["GoogleChromeManagementV1TelemetryHttpsLatencyChangeEventOut"]
            ).optional(),
            "user": t.proxy(
                renames["GoogleChromeManagementV1TelemetryUserInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryEventOut"])
    types["GoogleChromeManagementV1AndroidAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionIn"])
    types["GoogleChromeManagementV1AndroidAppPermissionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AndroidAppPermissionOut"])
    types["GoogleChromeManagementV1DeviceHardwareCountReportIn"] = t.struct(
        {"count": t.string().optional(), "bucket": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1DeviceHardwareCountReportIn"])
    types["GoogleChromeManagementV1DeviceHardwareCountReportOut"] = t.struct(
        {
            "count": t.string().optional(),
            "bucket": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
    types["GoogleChromeManagementV1CountChromeVersionsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "browserVersions": t.array(
                t.proxy(renames["GoogleChromeManagementV1BrowserVersionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeVersionsResponseIn"])
    types["GoogleChromeManagementV1CountChromeVersionsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "browserVersions": t.array(
                t.proxy(renames["GoogleChromeManagementV1BrowserVersionOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeVersionsResponseOut"])
    types["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1HttpsLatencyRoutineDataIn"])
    types["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"] = t.struct(
        {
            "latency": t.string().optional(),
            "problem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1HttpsLatencyRoutineDataOut"])
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
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"
    ] = t.struct(
        {
            "noRecentActivityCount": t.string().optional(),
            "pendingBrowserUpdateCount": t.string().optional(),
            "recentlyEnrolledCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
    ] = t.struct(
        {
            "noRecentActivityCount": t.string().optional(),
            "pendingBrowserUpdateCount": t.string().optional(),
            "recentlyEnrolledCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
        ]
    )
    types["GoogleChromeManagementV1ChromeAppRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
    types["GoogleChromeManagementV1ChromeAppRequestOut"] = t.struct(
        {
            "appDetails": t.string().optional(),
            "iconUri": t.string().optional(),
            "displayName": t.string().optional(),
            "appId": t.string().optional(),
            "requestCount": t.string().optional(),
            "detailUri": t.string().optional(),
            "latestRequestTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
    types["GoogleChromeManagementV1BatterySampleReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatterySampleReportIn"])
    types["GoogleChromeManagementV1BatterySampleReportOut"] = t.struct(
        {
            "remainingCapacity": t.string().optional(),
            "chargeRate": t.integer().optional(),
            "reportTime": t.string().optional(),
            "temperature": t.integer().optional(),
            "dischargeRate": t.integer().optional(),
            "voltage": t.string().optional(),
            "status": t.string().optional(),
            "current": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatterySampleReportOut"])
    types["GoogleChromeManagementV1AudioStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AudioStatusReportIn"])
    types["GoogleChromeManagementV1AudioStatusReportOut"] = t.struct(
        {
            "outputDevice": t.string().optional(),
            "outputMute": t.boolean().optional(),
            "inputDevice": t.string().optional(),
            "outputVolume": t.integer().optional(),
            "inputMute": t.boolean().optional(),
            "reportTime": t.string().optional(),
            "inputGain": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AudioStatusReportOut"])
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
    types["GoogleChromeManagementV1TouchScreenDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceIn"])
    types["GoogleChromeManagementV1TouchScreenDeviceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "touchPointCount": t.integer().optional(),
            "stylusCapable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TouchScreenDeviceOut"])
    types["GoogleChromeManagementV1ListTelemetryUsersResponseIn"] = t.struct(
        {
            "telemetryUsers": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryUsersResponseIn"])
    types["GoogleChromeManagementV1ListTelemetryUsersResponseOut"] = t.struct(
        {
            "telemetryUsers": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ListTelemetryUsersResponseOut"])
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"
    ] = t.struct(
        {
            "pendingUpdate": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
            "noRecentUserActivityCount": t.string().optional(),
        }
    ).named(
        renames["GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseIn"]
    )
    types[
        "GoogleChromeManagementV1CountChromeDevicesThatNeedAttentionResponseOut"
    ] = t.struct(
        {
            "pendingUpdate": t.string().optional(),
            "osVersionNotCompliantCount": t.string().optional(),
            "noRecentPolicySyncCount": t.string().optional(),
            "unsupportedPolicyCount": t.string().optional(),
            "noRecentUserActivityCount": t.string().optional(),
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
            "minUserCount": t.integer().optional(),
            "isTheme": t.boolean().optional(),
            "supportEnabled": t.boolean().optional(),
            "isExtensionPolicySupported": t.boolean().optional(),
            "isCwsHosted": t.boolean().optional(),
            "type": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
            ).optional(),
            "siteAccess": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppSiteAccessOut"])
            ).optional(),
            "isKioskOnly": t.boolean().optional(),
            "kioskEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppInfoOut"])
    types["GoogleChromeManagementV1StorageInfoDiskVolumeIn"] = t.struct(
        {
            "storageTotalBytes": t.string().optional(),
            "storageFreeBytes": t.string().optional(),
            "volumeId": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeIn"])
    types["GoogleChromeManagementV1StorageInfoDiskVolumeOut"] = t.struct(
        {
            "storageTotalBytes": t.string().optional(),
            "storageFreeBytes": t.string().optional(),
            "volumeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1StorageInfoDiskVolumeOut"])
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
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"] = t.struct(
        {
            "encryptionState": t.string().optional(),
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionAlgorithm": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoIn"])
    types["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"] = t.struct(
        {
            "encryptionState": t.string().optional(),
            "maxKeys": t.string().optional(),
            "keyLength": t.string().optional(),
            "encryptionAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TotalMemoryEncryptionInfoOut"])
    types["GoogleChromeManagementV1AppDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1AppDetailsIn"])
    types["GoogleChromeManagementV1AppDetailsOut"] = t.struct(
        {
            "latestPublishTime": t.string().optional(),
            "firstPublishTime": t.string().optional(),
            "reviewNumber": t.string().optional(),
            "revisionId": t.string().optional(),
            "reviewRating": t.number().optional(),
            "privacyPolicyUri": t.string().optional(),
            "appId": t.string().optional(),
            "detailUri": t.string().optional(),
            "name": t.string().optional(),
            "homepageUri": t.string().optional(),
            "androidAppInfo": t.proxy(
                renames["GoogleChromeManagementV1AndroidAppInfoOut"]
            ).optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "iconUri": t.string().optional(),
            "chromeAppInfo": t.proxy(
                renames["GoogleChromeManagementV1ChromeAppInfoOut"]
            ).optional(),
            "publisher": t.string().optional(),
            "description": t.string().optional(),
            "serviceError": t.proxy(renames["GoogleRpcStatusOut"]).optional(),
            "isPaidApp": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1AppDetailsOut"])
    types["GoogleChromeManagementV1TelemetryUserDeviceIn"] = t.struct(
        {"deviceId": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryUserDeviceIn"])
    types["GoogleChromeManagementV1TelemetryUserDeviceOut"] = t.struct(
        {
            "peripheralsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1PeripheralsReportOut"])
            ).optional(),
            "deviceId": t.string().optional(),
            "audioStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1AudioStatusReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserDeviceOut"])
    types["GoogleChromeManagementV1NetworkDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkDeviceIn"])
    types["GoogleChromeManagementV1NetworkDeviceOut"] = t.struct(
        {
            "iccid": t.string().optional(),
            "imei": t.string().optional(),
            "type": t.string().optional(),
            "macAddress": t.string().optional(),
            "meid": t.string().optional(),
            "mdn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkDeviceOut"])
    types["GoogleChromeManagementV1CpuInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuInfoIn"])
    types["GoogleChromeManagementV1CpuInfoOut"] = t.struct(
        {
            "model": t.string().optional(),
            "keylockerSupported": t.boolean().optional(),
            "architecture": t.string().optional(),
            "keylockerConfigured": t.boolean().optional(),
            "maxClockSpeed": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuInfoOut"])
    types["GoogleChromeManagementV1CpuTemperatureInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuTemperatureInfoIn"])
    types["GoogleChromeManagementV1CpuTemperatureInfoOut"] = t.struct(
        {
            "temperatureCelsius": t.integer().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuTemperatureInfoOut"])
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseIn"])
    types["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "requestedApps": t.array(
                t.proxy(renames["GoogleChromeManagementV1ChromeAppRequestOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CountChromeAppRequestsResponseOut"])
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
    types["GoogleChromeManagementV1ChromeAppPermissionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionIn"])
    types["GoogleChromeManagementV1ChromeAppPermissionOut"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "accessUserData": t.boolean().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ChromeAppPermissionOut"])
    types["GoogleChromeManagementV1UsbPeripheralReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportIn"])
    types["GoogleChromeManagementV1UsbPeripheralReportOut"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "subclassId": t.integer().optional(),
            "name": t.string().optional(),
            "vid": t.integer().optional(),
            "pid": t.integer().optional(),
            "categories": t.array(t.string()).optional(),
            "vendor": t.string().optional(),
            "classId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1UsbPeripheralReportOut"])
    types["GoogleChromeManagementV1CpuStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1CpuStatusReportIn"])
    types["GoogleChromeManagementV1CpuStatusReportOut"] = t.struct(
        {
            "sampleFrequency": t.string().optional(),
            "cpuUtilizationPct": t.integer().optional(),
            "cpuTemperatureInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuTemperatureInfoOut"])
            ).optional(),
            "reportTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1CpuStatusReportOut"])
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
    types["GoogleChromeManagementV1TelemetryDeviceIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceIn"])
    types["GoogleChromeManagementV1TelemetryDeviceOut"] = t.struct(
        {
            "audioStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1AudioStatusReportOut"])
            ).optional(),
            "cpuStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuStatusReportOut"])
            ).optional(),
            "peripheralsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1PeripheralsReportOut"])
            ).optional(),
            "batteryInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryInfoOut"])
            ).optional(),
            "networkInfo": t.proxy(
                renames["GoogleChromeManagementV1NetworkInfoOut"]
            ).optional(),
            "storageStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1StorageStatusReportOut"])
            ).optional(),
            "osUpdateStatus": t.array(
                t.proxy(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
            ).optional(),
            "memoryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1MemoryStatusReportOut"])
            ).optional(),
            "name": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "bootPerformanceReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BootPerformanceReportOut"])
            ).optional(),
            "thunderboltInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
            ).optional(),
            "networkDiagnosticsReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkDiagnosticsReportOut"])
            ).optional(),
            "batteryStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1BatteryStatusReportOut"])
            ).optional(),
            "cpuInfo": t.array(
                t.proxy(renames["GoogleChromeManagementV1CpuInfoOut"])
            ).optional(),
            "storageInfo": t.proxy(
                renames["GoogleChromeManagementV1StorageInfoOut"]
            ).optional(),
            "networkStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
            ).optional(),
            "graphicsStatusReport": t.array(
                t.proxy(renames["GoogleChromeManagementV1GraphicsStatusReportOut"])
            ).optional(),
            "deviceId": t.string().optional(),
            "serialNumber": t.string().optional(),
            "graphicsInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsInfoOut"]
            ).optional(),
            "customer": t.string().optional(),
            "memoryInfo": t.proxy(
                renames["GoogleChromeManagementV1MemoryInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryDeviceOut"])
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
    types["GoogleChromeManagementV1GraphicsInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1GraphicsInfoIn"])
    types["GoogleChromeManagementV1GraphicsInfoOut"] = t.struct(
        {
            "touchScreenInfo": t.proxy(
                renames["GoogleChromeManagementV1TouchScreenInfoOut"]
            ).optional(),
            "displayDevices": t.array(
                t.proxy(renames["GoogleChromeManagementV1DisplayDeviceOut"])
            ).optional(),
            "adapterInfo": t.proxy(
                renames["GoogleChromeManagementV1GraphicsAdapterInfoOut"]
            ).optional(),
            "eprivacySupported": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1GraphicsInfoOut"])
    types["GoogleChromeManagementV1NetworkStatusReportIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportIn"])
    types["GoogleChromeManagementV1NetworkStatusReportOut"] = t.struct(
        {
            "transmissionPowerDbm": t.integer().optional(),
            "gatewayIpAddress": t.string().optional(),
            "receivingBitRateMbps": t.string().optional(),
            "connectionState": t.string().optional(),
            "encryptionOn": t.boolean().optional(),
            "reportTime": t.string().optional(),
            "lanIpAddress": t.string().optional(),
            "signalStrengthDbm": t.integer().optional(),
            "wifiPowerManagementEnabled": t.boolean().optional(),
            "wifiLinkQuality": t.string().optional(),
            "connectionType": t.string().optional(),
            "sampleFrequency": t.string().optional(),
            "transmissionBitRateMbps": t.string().optional(),
            "guid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1NetworkStatusReportOut"])
    types["GoogleChromeManagementV1ThunderboltInfoIn"] = t.struct(
        {"securityLevel": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoIn"])
    types["GoogleChromeManagementV1ThunderboltInfoOut"] = t.struct(
        {
            "securityLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1ThunderboltInfoOut"])
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
    types["GoogleChromeManagementV1TelemetryUserIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceIn"])
            ).optional(),
            "userEmail": t.string().optional(),
            "customer": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserIn"])
    types["GoogleChromeManagementV1TelemetryUserOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "userDevice": t.array(
                t.proxy(renames["GoogleChromeManagementV1TelemetryUserDeviceOut"])
            ).optional(),
            "userEmail": t.string().optional(),
            "customer": t.string().optional(),
            "orgUnitId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1TelemetryUserOut"])
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
    types["GoogleChromeManagementV1BatteryInfoIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BatteryInfoIn"])
    types["GoogleChromeManagementV1BatteryInfoOut"] = t.struct(
        {
            "designCapacity": t.string().optional(),
            "manufactureDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "serialNumber": t.string().optional(),
            "designMinVoltage": t.integer().optional(),
            "manufacturer": t.string().optional(),
            "technology": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BatteryInfoOut"])
    types["GoogleChromeManagementV1BrowserVersionIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1BrowserVersionIn"])
    types["GoogleChromeManagementV1BrowserVersionOut"] = t.struct(
        {
            "system": t.string().optional(),
            "channel": t.string().optional(),
            "count": t.string().optional(),
            "version": t.string().optional(),
            "deviceOsVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1BrowserVersionOut"])
    types["GoogleChromeManagementV1OsUpdateStatusIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusIn"])
    types["GoogleChromeManagementV1OsUpdateStatusOut"] = t.struct(
        {
            "newRequestedPlatformVersion": t.string().optional(),
            "newPlatformVersion": t.string().optional(),
            "updateState": t.string().optional(),
            "lastRebootTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "lastUpdateCheckTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleChromeManagementV1OsUpdateStatusOut"])
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
            "memoryReports": t.array(
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
            "storageReports": t.array(
                t.proxy(renames["GoogleChromeManagementV1DeviceHardwareCountReportOut"])
            ).optional(),
            "memoryReports": t.array(
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

    functions = {}
    functions["customersReportsCountChromeHardwareFleetDevices"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountInstalledApps"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsFindInstalledAppDevices"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersReportsCountChromeVersions"] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesReachingAutoExpirationDate"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeDevicesThatNeedAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "customersReportsCountChromeBrowsersNeedingAttention"
    ] = chromemanagement.get(
        "v1/{customer}/reports:countChromeBrowsersNeedingAttention",
        t.struct(
            {
                "customer": t.string(),
                "orgUnitId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames[
                "GoogleChromeManagementV1CountChromeBrowsersNeedingAttentionResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryDevicesList"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryDevicesGet"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1TelemetryDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryUsersList"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1TelemetryUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryUsersGet"] = chromemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleChromeManagementV1TelemetryUserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersTelemetryEventsList"] = chromemanagement.get(
        "v1/{parent}/telemetry/events",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "customer": t.string(),
                "orderBy": t.string().optional(),
                "orgUnitId": t.string().optional(),
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

    return Import(
        importer="chromemanagement", renames=renames, types=types, functions=functions
    )
