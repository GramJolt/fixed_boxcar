import setting
import csv
import matplotlib.pyplot as plt
import shutil

def create_log(population_data, gen, population_size, sort_value):

    #フォルダの中身をコピー
    shutil.copy('./mklog.py', setting.curdir + '/' + setting.filename)
    shutil.copy('./classes.py', setting.curdir + '/' + setting.filename)
    shutil.copy('./run.py', setting.curdir + '/' + setting.filename)
    shutil.copy('./setting.py', setting.curdir + '/' + setting.filename)
    shutil.copy('requirements.txt', setting.curdir + '/' + setting.filename)


    #全個体の評価値ログファイルの作成
    with open('{}{}'.format(setting.curdir + '/', setting.filename + '/' + setting.filename2 ),'a') as f:
        writer = csv.writer(f, lineterminator='\n')#delimiter = ',')
        for ind_i in range(population_size):
            info = [gen, ind_i, population_data[ind_i].max_dist]
            writer.writerow(info)

    #評価値の推移グラフ作成
    with open('{}{}'.format(setting.curdir + '/', setting.filename + '/' + setting.filename2 ),'r') as f:
        reader = csv.reader(f)
        l = []
        for row in reader:
            l.append(round(float(row[2]),3))
        fig = plt.figure()

        if(sort_value == 0): #ソートなし
            plt.plot(l)
            fig.savefig(setting.curdir + '/' + setting.filename + '/' + setting.filename3)

        elif(sort_value == 1): #全個体まとめてソート
            l.sort()
            plt.plot(l)
            fig.savefig(setting.curdir + '/' + setting.filename + '/' + setting.filename3)

        elif(sort_value == 2): #世代ごとにソート
            l2 = []
            for i in range(int(len(l) / population_size)):
                tmp = []
                for j in range(population_size):
                    tmp.append(l[i*population_size + j])
                tmp.sort()
                l2+=(tmp)
                plt.plot(l2)

        if(setting.SHOW_GRAPH == True):
            plt.show()

        fig.savefig(setting.curdir + '/' + setting.filename + '/' + setting.filename3)
