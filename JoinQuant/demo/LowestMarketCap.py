# 导入函数库
from jqdata import *


# 初始化函数，设定基准等等
def initialize(context):
    run_daily(period, time='every_bar')
    # 代码：设定好要交易的股票数量stocksnum
    g.stock_num = 10;


def period(context):
    # 代码：找出市值排名最小的前stocksnum只股票作为要买入的股票
    q = query(valuation.code).order_by(valuation.market_cap).limit(1);
    code_list = get_fundamentals(q)['code']

    inexsitence_stocks = getInexsitenceStocks(context, code_list)
    for i in inexsitence_stocks:
        order_target(i, 0)

    for i in code_list:
        order_target(i, 100)


def getInexsitenceStocks(context, codes):
    long_positions = context.portfolio.long_positions
    inexsitence_stocks = []
    for code in long_positions:
        isExsit = False
        for c in codes:
            if c == code:
                isExsit = True
                break

        if isExsit == False:
            inexsitence_stocks.append(code)

    return inexsitence_stocks













