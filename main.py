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
        model_wave_length.append(line[0])

        if not is_init:
            is_init = True
            # 理論値 - 光の強さ一覧
            model_light_intensity = []
            for _ in range(len(line[1:])):
                model_light_intensity.append([])

        for i in range(len(line[1:])):
            model_light_intensity[i].append(line[i + 1])

# 実験値 - 波長一覧
experiment_wave_length = []
# 実験値 - 光の強さ一覧
experiment_light_intensity = []
with open('result.txt') as f:
    for line in f:
        # 読み込んだ行の末尾には改行文字があるので削除
        # 参考 : https://atmarkit.itmedia.co.jp/ait/articles/2104/13/news024.html
        # 参考 : https://note.nkmk.me/python-split-rsplit-splitlines-re/
        line = line.rstrip().split()
        experiment_wave_length.append(line[0])
        experiment_light_intensity.append(line[1])
#####################################

#####################################
# <ここからグラフ描画>

# 参考 : https://qiita.com/trami/items/b501abe7667e55ab2c9f
fig, ax = plt.subplots()

# 参考 : https://www.delftstack.com/ja/howto/matplotlib/how-to-hide-axis-text-ticks-and-or-tick-labels-in-matplotlib/#:~:text=%E6%80%A7%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82-,%E8%BB%B8%E3%81%AE%E3%83%A9%E3%83%99%E3%83%AB%E3%82%92%E5%90%AB%E3%82%80%E8%BB%B8%E3%82%92%E9%9D%9E%E8%A1%A8%E7%A4%BA%E3%81%AB,%E3%82%92%E9%9D%9E%E8%A1%A8%E7%A4%BA%E3%81%AB%E3%81%97%E3%81%BE%E3%81%99%E3%80%82
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

# グラフのタイトル
ax.set_title('fitting graph')
# x軸ラベル
plt.xlabel("wave_length")
# y軸ラベル
plt.ylabel("light_intensity")

# 実験値 - グラフ
ax.plot(np.array(experiment_wave_length), np.array(experiment_light_intensity), color="purple", label='experiment value')

COLORS = ['red', 'blue', 'green', 'yellow', 'black', 'pink', 'gold', 'violet', 'orange', 'magenta', 'cyan']
# 理論値 - グラフ
for i in range(len(model_light_intensity)):
    ax.plot(np.array(model_wave_length), np.array(model_light_intensity[i]), color=random.choice(COLORS), label='model value' + str(i + 1))

# レイアウトの設定
fig.tight_layout()

# 参考 : https://it-ojisan.tokyo/matplotlib-label/
plt.legend()

plt.show()
#####################################
