import codecs
import csv
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Grid,Pie,Scatter,Map
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import webbrowser
import os

# js颜色分配
js_function = """
                function(params) {
                    var colorList = ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'];
                    return colorList[params.dataIndex%9];
                }
                """
                
# 饼图
pie_data=[]
a = (
    Pie(
        init_opts=opts.InitOpts(
            width='420px', # 图表画布宽度
            height='360px', # 图标画布长度
        )
    )
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_colors(['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pie",title_textstyle_opts=opts.TextStyleOpts(color='#fff')),
        legend_opts=opts.LegendOpts(is_show=False)
        )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("daping/echarts/echart_4.html")
)

# 地图
data_city = [('十堰',1),('神农架',2),('襄阳',3),('随州',4),('荆门',5),('宜昌',6),('恩施',8),('荆州',9),('潜江',10),('天门',11),('仙桃',12),('孝感',13),('武汉',14),('黄冈',14),('鄂州',14),('黄石',14),('咸宁',14),]
name_map = {
'十堰市':'十堰','神农架林区':'神农架','襄阳市':'襄阳','随州市':'随州','荆门市':'荆门','宜昌市':'宜昌','恩施土家族苗族自治州':'恩施','荆州市':'荆州','潜江市':'潜江','天门市':'天门','仙桃市':'仙桃','孝感市':'孝感','武汉市':'武汉','黄冈市':'黄冈','鄂州市':'鄂州','黄石市':'黄石','咸宁市':'咸宁'
}

b = (
    Map(
         init_opts=opts.InitOpts(
            height="700px"
         )
    )
    .add(
        data_pair=data_city,
        series_name='',
        maptype="湖北",
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=True),
        name_map=name_map
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title='湖北',title_textstyle_opts=opts.TextStyleOpts(color='#fff')
            ),
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=15,
            is_piecewise=True
        )
    )
    .render("daping/echarts/echart_3.html")
)

# 柱状图

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
            height='360px', # 图标画布长度
        )
    )
    .add_xaxis(x_data)#x轴数据
    .add_yaxis("数据", y_data,
        itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode(js_function)# 图形的颜色 见部分配置通用参数详解
            # color="rgb(5,101,123)"
        ))#y轴数据
     .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False)
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),# 图例配置
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(),boundary_gap=['1%','1%']),#x轴配置
        title_opts=opts.TitleOpts(title="Bar", subtitle="测试",title_textstyle_opts=opts.TextStyleOpts(color='#fff')),#图标标题配置
    )
    .render('daping/echarts/echart_1.html')
)

# 折线图
week_name_list = []
high_temperature = []
with codecs.open('daping/data/line.csv') as f:
    for row in csv.reader(f, skipinitialspace=True):
        if(row[0]!='date'):
            week_name_list.append(row[0])
            high_temperature.append(row[1])
d=(
     Line(
         # 初始化图表配置
         init_opts=opts.InitOpts(
            width='400px', # 图表画布宽度
            height='360px', # 图标画布长度
        )
     )
    .add_xaxis(xaxis_data=week_name_list)
    .add_yaxis(
        series_name="最高气温",
        y_axis=high_temperature,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
            ]
        )
    )
    .set_series_opts(
        linestyle_opts=opts.LineStyleOpts(
            color='#ea7ccc'
        )
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),# 图例配置
        title_opts=opts.TitleOpts(title="折线", subtitle="纯属虚构",title_textstyle_opts=opts.TextStyleOpts(color='#fff')),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts()),#x轴配置
    )
    .render("daping/echarts/echart_2.html")
)

# 散点图
data = [
    [10.0, 8.04],
    [8.0, 6.95],
    [13.0, 7.58],
    [9.0, 8.81],
    [11.0, 8.33],
    [14.0, 9.96],
    [6.0, 7.24],
    [4.0, 4.26],
    [12.0, 10.84],
    [7.0, 4.82],
    [5.0, 5.68],
]
data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]
e=(
    Scatter(
         init_opts=opts.InitOpts(
            width='400px', # 图表画布宽度
            height='360px', # 图标画布长度
         ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name='散点',
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False,color='#fff'),
        itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode(js_function)# 图形的颜色 见部分配置通用参数详解
            # color="rgb(5,101,123)"
        ),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),# 图例配置
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
        title_opts=opts.TitleOpts(title="散点",title_textstyle_opts=opts.TextStyleOpts(color='#fff')),
    )
    .render("daping/echarts/echart_5.html")
)
filename = 'file:///'+os.getcwd()+'/' + 'daping/index.html'
webbrowser.open_new_tab(filename)



