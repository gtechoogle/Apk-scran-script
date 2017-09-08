import os;

def look_for_apk_file():
    if (os.path.exists('apk_temp')):
        os.listdir('apk_temp');

file_list=[]
def test(dir):
    for fpathe,dirs,fs in os.walk('apk_temp'):
        for f in fs:
            file_list.append((os.path.join(fpathe,f)))


if __name__ == '__main__':
    test(r'apk_temp\\app');
    print(file_list)