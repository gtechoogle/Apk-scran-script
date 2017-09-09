import os

class AdbUtils:
    device_serio_number=[];
    def get_device_serio_number(self):
        command = "adb devices";
        out_info = os.popen(command);
        device_info = out_info.read().split('\n');
        for info in device_info:
            if (info.find("\tdevice") != -1):
                self.device_serio_number.append(info.split("\t")[0])
        # print (device_info);
        print (self.device_serio_number);
    def is_device_available(self):
        self.get_device_serio_number();
        if (len(test.device_serio_number) > 0):
            return True;
        return False;

if __name__ == '__main__':
    test = AdbUtils();
    if (test.is_device_available()):
        print ("device is plug")
    

    