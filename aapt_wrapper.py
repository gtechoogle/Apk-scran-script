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
            if (item.find('package')):
                pkg_name = self.get_pkg_name(item);
            else:
                pkg_permission.append(self.get_permission(item))
        self.pkg_recorder[pkg_name] = pkg_permission;
        print(self.pkg_recorder);
    
    def get_pkg_name(self, data):
        return "test.app";
    def get_permission(self, data):
        return "adsffsdf";

def main():
    test_app = AaptWrapper();
    test_app.permission_dump("E:\\WorkSpace\\AndroidStudioProjects\\Fuliba\\app\\build\outputs\\apk\\app-debug.apk");


    

if __name__ == '__main__':
    main()
    