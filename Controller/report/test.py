from reportlab.pdfbase import pdfmetrics  # 注册字体
from reportlab.pdfbase.ttfonts import TTFont  # 字体类
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
from reportlab.lib import colors  # 颜色模块
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Drawing  # 绘图工具
from reportlab.lib.units import cm  # 单位：cm

import matplotlib.pyplot as plt
from Memory.detect import *
from Data.leanCloud import *
from Memory.detect import *

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))
pdfmetrics.registerFont(TTFont('Times', 'times.ttf'))


# 封装不同内容对应的函数
# 创建一个Graphs类，通过不同的静态方法提供不同的报告内容，包括：标题、普通段落、图片、表格和图表。函数中的相关数据目前绝大多数都是固定值，可以根据情况自行设置成相关参数。
# Graphs类的全部代码

class Graphs:
    # 绘制标题
    @staticmethod
    def draw_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Heading1']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 35  # 字体大小
        ct.leading = 50  # 行间距
        ct.textColor = colors.green  # 字体颜色
        ct.alignment = 1  # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

        # 绘制小标题

    @staticmethod
    def draw_little_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Normal']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 15  # 字体大小
        ct.leading = 30  # 行间距
        ct.textColor = colors.black  # 字体颜色
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

        # 绘制普通段落内容

    @staticmethod
    def draw_text(text: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 12
        ct.wordWrap = 'CJK'  # 设置自动换行
        ct.alignment = 0  # 左对齐
        ct.firstLineIndent = 32  # 第一行开头空格
        ct.leading = 25
        return Paragraph(text, ct)

    @staticmethod
    def draw_report_text(text):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'times'
        ct.fontSize = 10
        # ct.wordWrap = 'CJK'  # 设置自动换行
        ct.alignment = 0  # 左对齐
        # ct.firstLineIndent = 32  # 第一行开头空格
        ct.leading = 25
        return Paragraph(text, ct)

    # 绘制表格

    @staticmethod
    def draw_table(*args):
        # 列宽度
        col_width = 240
        style = [
            ('FONTNAME', (0, 0), (-1, -1), 'SimSun'),  # 字体
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
            ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
            # ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
            # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
            # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
            # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
            # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
        ]
        table = Table(args, colWidths=col_width, style=style)
        return table

        # 创建图表

    @staticmethod
    def draw_bar(bar_data: list, ax: list, items: list):
        drawing = Drawing(500, 250)
        bc = VerticalBarChart()
        bc.x = 45  # 整个图表的x坐标
        bc.y = 45  # 整个图表的y坐标
        bc.height = 200  # 图表的高度
        bc.width = 350  # 图表的宽度
        bc.data = bar_data
        bc.strokeColor = colors.black  # 顶部和右边轴线的颜色
        bc.valueAxis.valueMin = 5000  # 设置y坐标的最小值
        bc.valueAxis.valueMax = 26000  # 设置y坐标的最大值
        bc.valueAxis.valueStep = 2000  # 设置y坐标的步长
        bc.categoryAxis.labels.dx = 2
        bc.categoryAxis.labels.dy = -8
        bc.categoryAxis.labels.angle = 20
        bc.categoryAxis.categoryNames = ax

        # 图示
        leg = Legend()
        leg.fontName = 'SimSun'
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = 475  # 图例的x坐标
        leg.y = 240
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = items
        drawing.add(leg)
        drawing.add(bc)
        return drawing

        # 绘制图片

    @staticmethod
    def draw_img(path):
        img = Image(path)  # 读取指定路径下的图片
        img.drawWidth = 10 * cm  # 设置图片的宽度
        img.drawHeight = 8 * cm  # 设置图片的高度
        return img

    @staticmethod
    def createReport(reportResult, riskFunction ,filepath):
        content = list()

        # 添加标题
        content.append(Graphs.draw_title('《代码审计报告》'))

        # 添加小标题
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[风险函数统计结果]'))
        """
        获取风险函数库中的所有函数
        返回格式：[{'FunctionName': "xxx",
                  'RiskLevel': "xxx",
                  'Solution': "xxx"
        }]
        """
        # 添加风险函数表
        low = 0
        mid = 0
        high = 0
        most = 0

        HighriskDescription = [('高等风险函数', '解决方式')]
        MidriskDescription = [('中等风险函数', '解决方式')]
        LowriskDescription = [('低等风险函数', '解决方式')]

        for risk in riskFunction:
            if risk['RiskLevel'] == "低危险":
                low += 1
                temp = (risk['FunctionName'], risk['Solution'])
                LowriskDescription.append(temp)
            if risk['RiskLevel'] == "中等危险":
                mid += 1
                temp = (risk['FunctionName'], risk['Solution'])
                MidriskDescription.append(temp)
            if risk['RiskLevel'] == "很危险":
                high += 1
                temp = (risk['FunctionName'], risk['Solution'])
                HighriskDescription.append(temp)
            if risk['RiskLevel'] == "最危险":
                most += 1
        data = [
            ('风险等级', '风险数量'),
            ('高等风险函数', high),
            ('中等风险函数', mid),
            ('低等风险函数', low)
        ]
        content.append(Graphs.draw_table(*data))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[风险函数饼状图]'))
        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试
        labels = '低等', '中等', '高等'
        sizes = [low, mid, high]  # define size of each part
        colorsList = 'yellowgreen', 'lightskyblue', 'lightcoral'  # define color of each part on pie
        explode = 0, 0, 0.1  # define which one will be exploded
        plt.pie(sizes, explode=explode, labels=labels, colors=colorsList,
                autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
        plt.axis('equal')  # axis type
        plt.savefig(filepath.replace('.c', 'PieChart.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'PieChart.png')))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[各风险函数详细信息]'))
        content.append(Graphs.draw_table(*HighriskDescription))
        content.append(Graphs.draw_table(*MidriskDescription))
        content.append(Graphs.draw_table(*LowriskDescription))


        # 添加段落
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[CppCheck工具检测]'))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[CppCheck工具检测:STDOUT]'))
        content.append(Graphs.draw_text(reportResult[0]['cppcheckeroutput']))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[CppCheck工具检测:STDERROR]'))
        content.append(Graphs.draw_text(reportResult[0]['cppcheckeroutput']))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[内存泄露检测报告]'))
        content.append(Graphs.draw_title(''))
        errors = reportResult[1]['drmemory_error']
        # summarys = reportResult[1]['drmemory_summery']
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[内存泄露数据说明]'))
        for error in errors:
            content.append(Graphs.draw_text(error))
        content.append(Graphs.draw_title(''))
        # content.append(Graphs.draw_little_title('[内存泄露数据总结]'))
        # for summary in summarys:
        #     content.append(Graphs.draw_text(summary))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[ClangChecker评估报告]'))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[ClangChecker评估报告:STDOUT]'))
        content.append(Graphs.draw_text(reportResult[2]['clangcheckroutput']))
        content.append(Graphs.draw_little_title('[ClangChecker评估报告:STDERR]'))
        content.append(Graphs.draw_text(reportResult[2]['clangcheckererror']))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码质量评估报告]'))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码质量评估报告:STDOUT]'))
        content.append(Graphs.draw_text(reportResult[3]['clangevaluationoutput']))
        content.append(Graphs.draw_little_title('[代码质量评估报告:STDERR]'))
        content.append(Graphs.draw_text(reportResult[3]['clangevaluationerror']))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码综合评估报告]'))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码综合评估报告:STDOUT]'))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[关于代码综合评估的详细说明]'))
        content.append(Graphs.draw_text(reportResult[4]['copy_right']))
        content.append(Graphs.draw_text(reportResult[4]['detect_rules']))
        content.append(Graphs.draw_text(reportResult[4]['examing_file']))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码综合扫描结果]'))
        content.append(Graphs.draw_text(reportResult[4]['final_results']))
        content.append(Graphs.draw_text(reportResult[4]['hits']))
        content.append(Graphs.draw_text(reportResult[4]['detect_lines']))
        content.append(Graphs.draw_text(reportResult[4]['detect_real_lines']))
        content.append(Graphs.draw_text(reportResult[4]['Minimum_risk_level']))
        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[代码扫描结果分析]'))
        content.append(Graphs.draw_text(reportResult[4]['analysis_summary']))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[函数漏洞等级统计]'))
        content.append(Graphs.draw_title(''))

        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试 1
        labels = 'Low Risk', 'Moderate Risk', 'Significant Risk', 'High Risk', 'Critical Risk', 'Catastrophic Risk'
        sizes = reportResult[4]['levels']  # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']# define color of each part on pie
        explode = 0, 0, 0, 0, 0, 0.1  # define which one will be exploded
        plt.pie(sizes, explode=explode, labels=labels, colors=colorsList,
                autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
        plt.axis('equal')  # axis type
        plt.title('Quantity pieChart of each risk level')
        plt.savefig(filepath.replace('.c', 'PieChart1.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'PieChart1.png')))

        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试
        labels = ['Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+',
                  'Catastrophic Risk+']
        sizes = reportResult[4]['levels'] # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
                      '#00FFFF']  # define color of each part on pie
        plt.bar(labels, sizes, color=colorsList)
        plt.xlabel('Risk Levels')
        plt.ylabel('KSLOC')
        plt.title('Quantity histogram for each risk level')
        plt.savefig(filepath.replace('.c', 'Histogram1.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'Histogram1.png')))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[函数漏洞等级累计统计]'))
        content.append(Graphs.draw_title(''))
        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试 2
        labels = 'Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+', 'Catastrophic Risk+'
        sizes = reportResult[4]['levels_plus']  # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
                      '#00FFFF']  # define color of each part on pie
        explode = 0, 0, 0, 0, 0, 0.1  # define which one will be exploded
        plt.pie(sizes, explode=explode, labels=labels, colors=colorsList,
                autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
        plt.axis('equal')  # axis type
        plt.title('Cumulative quantity pieChart of each risk level')
        plt.savefig(filepath.replace('.c', 'PieChart2.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'PieChart2.png')))

        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试
        labels = ['Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+',
                  'Catastrophic Risk+']
        sizes = reportResult[4]['levels_plus']   # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
                      '#00FFFF']  # define color of each part on pie
        plt.bar(labels, sizes, color=colorsList)
        plt.xlabel('Risk Levels')
        plt.ylabel('KSLOC')
        plt.title('Cumulative quantity histogram for each risk level')
        plt.savefig(filepath.replace('.c', 'Histogram2.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'Histogram2.png')))

        content.append(Graphs.draw_title(''))
        content.append(Graphs.draw_little_title('[函数漏洞物理代码行频率统计]'))
        content.append(Graphs.draw_title(''))
        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试 3
        labels = 'Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+', 'Catastrophic Risk+'
        sizes = reportResult[4]['levels_plus_KSLOC']  # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
                      '#00FFFF']  # define color of each part on pie
        explode = 0, 0, 0, 0, 0, 0.1  # define which one will be exploded
        plt.pie(sizes, explode=explode, labels=labels, colors=colorsList,
                autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
        plt.axis('equal')  # axis type
        plt.title('Estimated defect density piecahrt for each risk level')
        plt.savefig(filepath.replace('.c', 'PieChart3.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'PieChart3.png')))

        # Clear previous plot state
        plt.clf()
        # 添加图片生成plt图标测试
        labels = ['Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+',
                  'Catastrophic Risk+']
        sizes = reportResult[4]['levels_plus_KSLOC']  # define size of each part
        colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
                      '#00FFFF']  # define color of each part on pie
        plt.bar(labels, sizes, color=colorsList)
        plt.xlabel('Risk Levels')
        plt.ylabel('KSLOC')
        plt.title('Estimated defect density histogram for each risk level')
        plt.savefig(filepath.replace('.c', 'Histogram3.png'))
        content.append(Graphs.draw_img(filepath.replace('.c', 'Histogram3.png')))

        # 生成pdf文件
        doc = SimpleDocTemplate(filepath.replace('.c', '.pdf'), pagesize=letter)
        doc.build(content)

def get_report(file_path):
    risk = detectRiskFunction(file_path)
    result = memory_merge(file_path)
    Graphs.createReport(result, risk, file_path)

if __name__ == '__main__':
    file_path = r'D:\work1\c_test_file\test\test.c'
    risk = detectRiskFunction(file_path)
    result = memory_merge(file_path)
    Graphs.createReport(result, risk, file_path)

    # # # 添加图片生成plt图标测试
    # #
    # # 添加图片生成plt图标测试 1
    # labels = 'Low Risk', 'Moderate Risk', 'Significant Risk', 'High Risk', 'Critical Risk', 'Catastrophic Risk'
    # sizes = ['88', '0', '0', '0', '0', '0']  # define size of each part
    # colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']  # define color of each part on pie
    # explode = 0, 0, 0, 0, 0, 0.1  # define which one will be exploded
    # plt.pie(sizes, explode=explode, labels=labels, colors=colorsList,
    #         autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
    # plt.axis('equal')  # axis type
    # plt.title('Quantity pieChart of each risk level')
    # plt.savefig('hello1.png')
    #
    # # Clear previous plot state
    # plt.clf()
    # labels = ['Low Risk+', 'Moderate Risk+', 'Significant Risk+', 'High Risk+', 'Critical Risk+',
    #           'Catastrophic Risk+']
    # # sizes = [1,2,3,4,5,6]  # define size of each part
    # sizes = ['88', '0', '0', '0', '0', '0']  # define size of each part
    #
    # colorsList = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
    #               '#00FFFF']  # define color of each part on pie
    #
    # plt.xlabel('Risk Levels')
    # plt.ylabel('KSLOC')
    # plt.title('Estimated defect density histogram for each risk level')
    #
    #
    #
    # plt.savefig('hello2.png')

#     # 创建内容对应的空列表
#     content = list()
#
#     # 添加标题
#     content.append(Graphs.draw_title('《代码审计报告》'))
#
#     # 添加段落文字
#     content.append(Graphs.draw_text(
#         '这里是段落文字添加'))
#
#     # 添加小标题
#     content.append(Graphs.draw_title(''))
#     content.append(Graphs.draw_little_title('[风险函数统计结果]'))
#
#     # 添加表格
#
#     data = [
#         ('风险等级', '风险数量'),
#         ('高等风险函数', '2'),
#         ('中等风险函数', '4'),
#         ('低等风险函数', '10')
#     ]
#     content.append(Graphs.draw_table(*data))
#
#     content.append(Graphs.draw_title(''))
#     content.append(Graphs.draw_little_title('[各风险函数详细信息]'))
#
#     data = [
#         ('风险等级', '风险数量'),
#         ('高等风险函数', '2'),
#         ('中等风险函数', '4'),
#         ('低等风险函数', '10')
#     ]
#     content.append(Graphs.draw_table(*data))
#
#     # 生成图表
#     content.append(Graphs.draw_title(''))
#     content.append(Graphs.draw_little_title('热门城市的就业情况'))
#     b_data = [(25400, 12900, 20100, 20300, 20300, 17400), (15800, 9700, 12982, 9283, 13900, 7623)]
#     ax_data = ['BeiJing', 'ChengDu', 'ShenZhen', 'ShangHai', 'HangZhou', 'NanJing']
#     leg_items = [(colors.red, '平均薪资'), (colors.green, '招聘量')]
#     content.append(Graphs.draw_bar(b_data, ax_data, leg_items))
#
#     # plt图标测试
#     labels = '高等', '中等', '低等'
#     sizes = 25, 30, 45  # define size of each part
#     colors = 'yellowgreen', 'lightskyblue', 'lightcoral'  # define color of each part on pie
#     explode = 0, 0, 0.1  # define which one will be exploded
#     plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=50)  # plot pie
#     plt.axis('equal')  # axis type
#     plt.savefig('PieChart',dpi=300)
#     # 添加图片
#     content.append(Graphs.draw_img('PieChart.png'))
#
#     # 生成pdf文件
#     doc = SimpleDocTemplate('report.pdf', pagesize=letter)
#     doc.build(content)
