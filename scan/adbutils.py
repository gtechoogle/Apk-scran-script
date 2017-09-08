import os

class AdbUtils:
    def check_device(self):
        command = "adb devices";
        output_flow = os.popen(command);
        print (output_flow.read());

if __name__ == '__main__':
    test = AdbUtils();
    test.check_device();

    