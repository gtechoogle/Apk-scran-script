import os;
from adbutils import AdbUtils;

class ApkLoader:
    temp_folder_name = 'apk_temp';
    apk_path = ['/data/app','/system/app','/system/priv-app','vendor/app','vendor/priv-app']
    def creat_temp_apk_folder(self):
        if (not os.path.exists(self.temp_folder_name)):
            print("Create apk temp folder")
            os.mkdir(self.temp_folder_name);
    def pull_apk(self, path):
        os.system('adb pull ' + path + ' ' + self.temp_folder_name);
    def pull_apks(self):
        device_checker = AdbUtils();
        if (device_checker.is_device_available()):
            self.creat_temp_apk_folder();
            for path in self.apk_path:
                self.pull_apk(path)
        else:
            print("Please check your device connection");
    
if __name__ == '__main__':
    test = ApkLoader();
    test.pull_apks();