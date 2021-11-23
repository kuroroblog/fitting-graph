import random
import numpy as np
import matplotlib.pyplot as plt

#####################################
# <ここからデータ呼び出し>
# 理論値 - 波長一覧
model_wave_length = []
is_init = False
with open('model.txt') as f:
    for line in f:
        # 読み込んだ行の末尾には改行文字があるので削除
        # 参考 : https://atmarkit.itmedia.co.jp/ait/articles/2104/13/news024.html
        # 参考 : https://note.nkmk.me/python-split-rsplit-splitlines-re/
        line = line.rstrip().split()
        model_wave_length.append(float(line[0]))

        if not is_init:
            is_init = True
            # 理論値 - 光の強さ一覧
            model_light_intensity = []
            # 理論値 - 傾き
            model_tilt = []
            for _ in range(len(line[1:])):
                model_light_intensity.append([])
                model_tilt.append([])

        for i in range(len(line[1:])):
            model_light_intensity[i].append(float(line[i + 1]))
            tilt = float(line[i + 1]) / float(line[0])
            model_tilt[i].append(tilt)

# 実験値 - 波長一覧
experiment_wave_length = []
# 実験値 - 光の強さ一覧
experiment_light_intensity = []
# 実験値 - 傾き
experiment_tilt = []
with open('result.txt') as f:
    for line in f:
        # 読み込んだ行の末尾には改行文字があるので削除
        # 参考 : https://atmarkit.itmedia.co.jp/ait/articles/2104/13/news024.html
        # 参考 : https://note.nkmk.me/python-split-rsplit-splitlines-re/
        line = line.rstrip().split()
        experiment_wave_length.append(float(line[0]))
        experiment_light_intensity.append(float(line[1]))
        experiment_tilt.append(float(line[1]) / float(line[0]))
#####################################

#####################################
# <ここからグラフ描画>

# グラフ1 ##################

# 参考 : https://qiita.com/trami/items/b501abe7667e55ab2c9f
plt.subplot(2, 1, 1)

# 参考 : https://tech-market.org/matplotlib-delete-ticks/
plt.xticks([])
plt.yticks([])

# グラフのタイトル
plt.title('fitting graph1')
# x軸ラベル
plt.xlabel("wave_length")
# y軸ラベル
plt.ylabel("light_intensity")

# 実験値 - グラフ
plt.plot(np.array(experiment_wave_length), np.array(experiment_light_intensity), color="purple", label='experiment value')

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']
# 理論値 - グラフ
for i in range(len(model_light_intensity)):
    plt.plot(np.array(model_wave_length), np.array(model_light_intensity[i]), color=random.choice(COLORS), label='model value' + str(i + 1))

# 参考 : https://it-ojisan.tokyo/matplotlib-label/
plt.legend()

#########################

# グラフ2 ##################

# 参考 : https://qiita.com/trami/items/b501abe7667e55ab2c9f
plt.subplot(2, 1, 2)

# 参考 : https://tech-market.org/matplotlib-delete-ticks/
plt.xticks([])
plt.yticks([])

# グラフのタイトル
plt.title('fitting graph2')
# x軸ラベル
plt.xlabel("wave_length")
# y軸ラベル
plt.ylabel("tilt")

# 実験値 - グラフ
plt.plot(np.array(experiment_wave_length), np.array(experiment_tilt), color="purple", label='experiment value')

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']
# 理論値 - グラフ
for i in range(len(model_tilt)):
    plt.plot(np.array(model_wave_length), np.array(model_tilt[i]), color=random.choice(COLORS), label='model value' + str(i + 1))

# 参考 : https://it-ojisan.tokyo/matplotlib-label/
plt.legend()

# 参考 : https://rhinohattan.com/matplotlib%E3%81%AEsubplots%E3%81%A7%E3%82%B0%E3%83%A9%E3%83%95%E3%81%8C%E9%87%8D%E3%81%AA%E3%82%8B/
plt.tight_layout()

plt.show()
#########################

#####################################
