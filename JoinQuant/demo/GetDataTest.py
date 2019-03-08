# 导入函数库
from jqdata import *


# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')
    g.container = []
    # 过滤掉order系列API产生的比error级别低的log
    # log.set_level('order', 'error')

    ### 股票相关设定 ###
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5),
                   type='stock')

    ## 运行函数（reference_security为运行时间的参考标的；传入的标的只做种类区分，因此传入'000300.XSHG'或'510300.XSHG'是一样的）
    # 开盘前运行
    run_daily(before_market_open, time='before_open', reference_security='000300.XSHG')
    # 开盘时运行


## 开盘前运行函数
def before_market_open(context):
    # 输出运行时间
    log.info('函数运行时间(before_market_open)：' + str(context.current_dt.time()))

    # 要操作的股票：平安银行（g.为全局变量）
    g.security = '000001.XSHE'
    container = g.container
    df = attribute_history(security=g.security
                           , count=5
                           , unit="1d"
                           , fields="high"
                           , skip_paused=True
                           , df=True
                           , fq='pre')

    # container.append(df['high'][0])
    # sum = 0;å
    # index = 0;
    # for i in container[::-1]:
    #     sum += i
    #     index += 1
    #     if index == 5:break

    # log.info(sum / index)
    # log.info(df['high'].mean())
    q = query(valuation.code).order_by(valuation.market_cap.desc()).limit(5)
    log.info(get_fundamentals(q))






