from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']


def load_data(file_path: str) -> pd.DataFrame:
    """加载并返回电影数据"""
    data = pd.read_csv(
        file_path,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )
    return data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """处理缺失值和异常值"""
    data['年份'] = data['年份'].fillna(data['上映时间'].str[0:4])
    return data


def plot_yearly_trend(ax: Axes, data: pd.DataFrame):
    """绘制每年电影数量变化折线图"""
    # 分组统计
    year_count = data.groupby('年份')['年份'].count()

    # 组装数据
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]
    y = [year_count.get(i, 0) for i in x]

    # 绘图
    ax.plot(x, y, color='g')
    ax.set_title('每年电影数量变化折线图', fontsize=15)
    ax.set_xlabel('年份', fontsize=15)
    ax.set_ylabel('电影数量', fontsize=15)
    ax.set_xticks(x[::8])
    ax.set_yticks([i for i in range(0, 31, 3)])
    ax.grid(linestyle='--', alpha=0.4)


def plot_language_count(ax: Axes, data: pd.DataFrame):
    """绘制不同语言电影数量柱状图"""
    # 分组统计
    language_count = data.groupby('语言')['语言'].count().sort_values(ascending=False)
    x_language = language_count.index.tolist()
    y_language_count = language_count.values.tolist()

    # 绘图
    ax.bar(x_language, y_language_count, color='g', width=0.8)
    ax.set_title('不同语言电影数量', fontsize=15)
    ax.set_xlabel('语言', fontsize=15)
    ax.set_ylabel('数量', fontsize=15)
    ax.grid(linestyle='--', alpha=0.4)
    ax.tick_params(axis='x', rotation=30, labelsize=10)


def plot_type_count(ax: Axes, data: pd.DataFrame):
    """绘制不同类型电影数量柱状图"""
    # 统计各类型电影数量
    type_count = {}
    for types in data['类型'].str.split(','):
        for t in types:
            if t in type_count:
                type_count[t] += 1
            else:
                type_count[t] = 1

    x_types = list(type_count.keys())
    y_values = list(type_count.values())

    # 绘图
    ax.bar(x_types, y_values, color='g', width=0.8)
    ax.set_title('不同类型电影数量', fontsize=15)
    ax.set_xlabel('类型', fontsize=15)
    ax.set_ylabel('电影数量', fontsize=15)
    ax.grid(linestyle='--', alpha=0.4)
    ax.tick_params(axis='x', rotation=30, labelsize=10)


def plot_rating_distribution(ax: Axes, data: pd.DataFrame):
    """绘制各个评分电影占比饼状图"""
    # 分组统计
    rate_count = data.groupby('评分')['评分'].count()

    # 合并小数据为"其他"
    total = rate_count.sum()
    large_score = rate_count.loc[rate_count >= total * 0.05]
    small_score = rate_count.loc[rate_count < total * 0.05]

    if small_score.shape[0] > 0:
        large_score['其他'] = small_score.sum()

    rates = large_score.index.tolist()
    values = large_score.values.tolist()

    # 绘图
    ax.pie(values, labels=rates, autopct='%1.1f%%', startangle=0, radius=1.1)
    ax.set_title('各个评分电影占比', fontsize=15)
    ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.15))


def main():
    """主函数：加载数据、清洗数据、绘制图表并保存"""
    # 加载与清洗数据
    data = load_data("data/movies.csv")
    data = clean_data(data)

    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.subplots_adjust(hspace=0.4, wspace=0.3)
    fig.suptitle("TMDB-Top300电影榜单数据统计", fontsize=20, x=0.5, y=0.96)

    # 获取四个子图
    ax1: Axes = axes[0][0]
    ax2: Axes = axes[0][1]
    ax3: Axes = axes[1][0]
    ax4: Axes = axes[1][1]

    # 绘制四个图表
    plot_yearly_trend(ax1, data)
    plot_language_count(ax2, data)
    plot_type_count(ax3, data)
    plot_rating_distribution(ax4, data)

    # 保存并展示图片
    plt.savefig("data/tmdb_top300_movies_data_statistics.png")
    plt.show()


if __name__ == '__main__':
    main()
