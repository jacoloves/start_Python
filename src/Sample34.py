my_list=[('納豆',78),('ヨーグルト',90),('コーヒー',120),('コーラ',120),('鯖缶',100)]
my_list.sort(key=lambda tpl:tpl[1])
print(my_list)