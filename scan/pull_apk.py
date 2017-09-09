import os;

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
        self.creat_temp_apk_folder();
        for path in self.apk_path:
            self.pull_apk(path)
    
if __name__ == '__main__':
    test = ApkLoader();
    test.pull_apks();