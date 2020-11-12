# -*- coding: UTF-8 -*-
import os
import csv

cur_path = os.getcwd()
skips = ["/.git/", "/.gradle/", "/.idea/", "/build/generated/", "/build/intermediates/", "/build/kotlin/",
         "/build/outputs/", "/build/tmp/"]
fileSuffix = [".java", ".kt", ".gradle", ".xml", ".pro", ".txt", ".cfg"]


def get_all_files(path):
    lists = []
    dirs = os.listdir(path)
    for dir in dirs:
        if skip_file(path + '/' + dir):
            break
        if os.path.isdir(path+'/'+dir):
            for f in get_all_files(path+'/'+dir):
                if validate_file(f):
                    lists.append(f)
        else:
            if validate_file(dir):
                lists.append(path+'/'+dir)

    return lists


# 是否跳过目录或文件
def skip_file(path):
    for s in skips:
        if path.__contains__(s):
            return True
    return False


def validate_file(path):
    for s in fileSuffix:
        if path.__contains__(s):
            return True
    return False


def read_csv(path):
    lists = []
    csv_file = open(path, 'r')
    reader = csv.DictReader(csv_file)
    for line in reader:
        lists.append(line)
    return lists


def update_androidx(line):
    lists = read_csv('androidx-class-mapping.csv')
    for item in lists:
        if line.__contains__(item['Support Library class']):
            line = line.replace(item['Support Library class'], item['Android X class'])
            break
    return line


if __name__ == '__main__':
    need_replace = False
    content = ''
    files = get_all_files('/Users/liepu/weimai/test')
    for file in files:
        for line in iter(open(file)):
            if line.__contains__('android.support') or line.__contains__('android.arch') or \
                    line.__contains__('android.databinding') or line.__contains__('android.test'):
                content += update_androidx(line)
                need_replace = True
            else:
                content += line
        if need_replace:
            print(file)
            fo = open(file, 'w')
            fo.write(content)
            fo.close()

    print(len(files))
    read_csv('androidx-class-mapping.csv')
