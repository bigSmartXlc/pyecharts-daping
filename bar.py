import codecs
import csv

from pyecharts import options as opts
from pyecharts.charts import Bar


x_data=[]
y_data=[]
with codecs.open('bar.csv') as f:
    for row in csv.reader(f, skipinitialspace=True):
        x_data.append(row[0])
        y_data.append(row[1])
        

c = (
    Bar(
        # 初始化图表配置
         init_opts=opts.InitOpts(
            width='420px', # 图表画布宽度
            height='340px', # 图标画布长度
            chart_id = None, # 图表 ID，图表唯一标识，用于在多图表时区分
            renderer = 'canvas', # 渲染风格，可选 "canvas", "svg" 
            page_title = "Awesome-pyecharts", # 网页标题
            theme = "white", # 图表主题 white dark
            bg_color = None, # 图表背景颜色 可用颜色英文或者rgb(0,0,0)通道颜色配置
            js_host = "", # 远程 js host，如不设置默认为 https://assets.pyecharts.org/assets/
            # animation_opts = AnimationOpts() # 画图动画初始化配置，参考 `global_options.AnimationOpts
        )
    )
    .add_xaxis(x_data)
    .add_yaxis("数据", y_data)
    .set_global_opts(
        legend_opts=opts.LegendOpts(pos_right='10%'),# 图例配置
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts()),#x轴配置
        title_opts=opts.TitleOpts(title="Bar", subtitle="测试"),#图标标题配置
    )
    .render("bar.html")
)



