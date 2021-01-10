Android terminal commands:

1. ADB reboot-bootloader and reboot recovery commands:
This command will let you can reboot your device in the bootloader. If due to some malware your device is stuck or if your device is not rebooting then you can connect your device to the computer and run this command to reboot. To run the command just type adb reboot-bootloader in the command line and to boot the device in recovery just type adb reboot recovery.

2. Fastboot device command:
Fastboot is a diagnostic and engineering protocol that you can boot your Android device into. ADB does not work in the bootloader. If you have to boot into Android and the debugging tools are not active to communicate then you can use the fastboot command. Type fastboot devices in the prompt and you get the serial number.

3. Fastboot unlock command:
Fastboot flashing unlock command unlocks your bootloader. This command is not supported in many phones that support fastboot but you can check if your phone supports it. Just type fastboot flashing unlock in the command prompt and hit enter.

4. ADB sideload command:
You can download the update zip file in your phone instead of waiting for the update to be pushed into the phone. To do that just download the update to your computer and connect your device to the computer. Now reboot into recovery on your phone and using the volume buttons choose to apply update from ADB. then open command line and type ADB sideload Full-Path-to-the-file.zip and hit enter.



adb shell dumpsys batterystats						- collects battery data from your device

adb cd <directory>							- change the directory or folder

adb shell ls								- list directory contents

adb shell ls -a								- do not hide entries starting with

adb shell ls -i								- print index number of each file

adb shell ls -s								- print size of each file, in blocks

adb shell ls -n								- list numeric UIDs and GIDs

adb shell ls -R								- list subdirectories recursively

rm [options] <files or directory>					- removes files or directories

mkdir [options] <directory name>					- make a directory or create a folder

touch [options] <file>							- create an empty file or change file timestamps

cp [options] <source> <destination>					- copy files and directories

mv [options] <source> <destination>					- move or rename files

ping [options] <destination>						- Test the connection & latency between two network connections

netcfg [<interface> {dhcp|up|down}]					- manage and configure network connections via profiles.

ip [options] object							- show, manipulate routing, devices, policy routing, and tunnels.

--object := { link | addr | addrlabel | route | rule | neigh | ntable |tunnel | tuntap | maddr | mroute | mrule | monitor | xfrm |netns | l2tp }

--options := { -V[ersion] | -s[tatistics] | -d[etails] | -r[esolve] |-f[amily] { inet | inet6 | ipx | dnet | link } |-l[oops] { maximum-addr-flush-attempts } |-o[neline] | -t[imestamp] | -b[atch] [filename] |-rc[vbuf] [size]}



logcat									- prints log data on the screen

adb shell netstat							- list tcp connectivity

adb shell pwd								- print current working directory location

adb shell dumpstate							- dumps state

adb shell ps								- print process status

dumpsys [options]							- dumps system data

dumpstate								- dumps state

screencap <filename>							- takes a screenshot of the device’s display

screenrecord [options] <filename>					- records screen. Requires: Android 4.4 (API level 19) or higher

top [options]								- displays top CPU processes

getprop [options]							- get property via the android property service

setprop <key> <value>							- this command is used to set property service

fastboot oem unlock							- unlocks bootloader on the devic

fastboot oem lock							- used to relock the bootloader on the device

fastboot oem device-info						- prints bootloader lock/unlock status

fastboot flash recovery <file-name.img>					- flashes recovery image to the device

fastboot boot <file-name.img>						- boot the image file without installing or flashing on the 											device. Can be used to boot recovery image without 											flashing on the device

fastboot flash <file.zip>						- flashes flashable zip file from fastboot or bootloader mode

fastboot getvar cid							- displays CID (Carrier ID) of the device



adb root								- restarts the adbd daemon with root permissions

pip install monkey:
monkey -p com.package.name -c android.intent.category.LAUNCHER 1  	- run an Android package

am start -a android.intent.action.VIEW -d				- open browser

am start -t image/* -a android.intent.action.VIEW			- open gallery

am force-stop app.package.name						- force app to stop.

backup -all								- To backup all the device and app data. When executed, it will 										trigger the backup, ask you to accept the action on the 										Android device and then creates “backup.adb” file in the
										current directory.



Syntax: adb devices
- prints a list of all attached devices with USB Debugging enabled. In response, it returns the serial number and state of the device.

Syntax: adb forward <local> <remote>
- forwards the socket connections. It required USB Debugging enabled on the device.

Syntax: adb kill-server
- terminates the adb server process. Sometimes you might want to terminate the adb server and restart it to resolve the problems.

Syntax: adb connect <host>[:<port>]
- allows using adb over Wi-Fi. This requires the host and the device connected to the same Wi-Fi network.

Syntax: adb usb
- Restarts ADB in USB mode.

Syntax: adb install [option] <path to .apk>
- Pushes an Android application (.apk) from host to an emulator or the device.

Syntax: adb uninstall [option] <PACKAGE>
- Uninstalls or removes the package from the emulator or Android device.

Syntax: adb shell pm list packages [options] <FILTER>
- Prints all packages installed on the device/emulator.

Syntax: adb shell pm path <PACKAGE>
- Prints the path to the APK of the given package.

Syntax: adb shell pm clear <PACKAGE>
- deletes all the data associated with the package (clears app data and cache).

Syntax: adb pull <remote> [local]
- Downloads or pulls a specified file from an emulator/device to your computer (host).

Syntax: adb push <local> <remote>
- upload or push or copy a file from the host (computer) to an emulator or the device.