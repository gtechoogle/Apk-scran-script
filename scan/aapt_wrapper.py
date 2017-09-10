import os;

class AaptWrapper:
    pkg_recorder={};
    def permission_dump(self, apk_path):
        command = 'aapt dump permissions ' + apk_path;
        print(command)
        stream = os.popen(command);
        self.record(stream.read());
        stream.close();
    def record(self, content):
        values = content.split('\n');
        pkg_permission = [];
        for item in values:
            if (item.find('package') != -1):
                pkg_name = self.get_pkg_name(item);
            else:
                permission = self.get_used_permission(item);
                if (permission != None):
                    pkg_permission.append(permission)
        self.pkg_recorder[pkg_name] = pkg_permission;    
    def get_pkg_name(self, data):
        pkg_name=data.split(' ')[1];
        return pkg_name;
    def get_used_permission(self, data):
        if (data.find('uses-permission') != -1):
            temp = data.split("'");
            return temp[1];
        return None;
    def get_internet_permission_pkg(self):
        pkg_internet=[];
        for key in self.pkg_recorder:
            permissions = self.pkg_recorder[key];
            if 'android.permission.INTERNET' in permissions:
                pkg_internet.append(key);
        return pkg_internet;

def get_files():
    file_list = [];
    for fpathe,dirs,fs in os.walk('apk_temp'):
        for f in fs:
            file_list.append((os.path.join(fpathe,f)))
    return file_list;

if __name__ == '__main__':
    temp_list=get_files();
    apk_file_path=[];
    for file in temp_list:
        if (file.endswith('.apk')):
            apk_file_path.append(file);
    print (apk_file_path);    
    test_app = AaptWrapper();
    for path in apk_file_path:
        test_app.permission_dump(path);
    print (test_app.get_internet_permission_pkg());