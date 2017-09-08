import os;

class ApkLoader:
    temp_folder_name = 'apk_temp';
    def creat_temp_apk_folder(self):
        if (not os.path.exists(self.temp_folder_name)):
            print("Create apk temp folder")
            os.mkdir('apk_temp');
    def pull_data_apk(self):
        data_app_path = '/data/app'
        self.pull_apk(data_app_path);
    def pull_system_apk(self):
        data_app_path = '/system/app'
        self.pull_apk(data_app_path);
        data_priv_app_path = '/system/priv-app'
        self.pull_apk(data_priv_app_path);
    def pull_apk(self, path):
        os.system('adb pull ' + path + ' ' + self.temp_folder_name);
    
    
if __name__ == '__main__':
    test = ApkLoader();
    test.creat_temp_apk_folder();
    test.pull_data_apk();
    test.pull_system_apk();
