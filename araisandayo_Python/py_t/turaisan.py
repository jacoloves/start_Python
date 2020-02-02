# while True:
#     try:
#         x = int(input("数字を入れてください："))
#         break
#     except ValueError:
#         print("あらら！これは有効な数字ではありません。どうぞもう一度...")

import sys

class test:
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("データが整数に変換できません。")
# except:
#     print("予期せぬエラー:", sys.exc_info()[0])
#     raise

    def testsan(site):
        for site in sys.argv[1:]:
            try:
                f = open(arg, 'r')
            except IOError:
                print('cannot open', arg)
            else:
                print(arg, 'has', len(f.readline()), 'lines')
                f.close()
