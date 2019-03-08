# 在20180301买入一个股票，20180302卖出
# 根据某些条件执行止损，止盈
# 写一个判断当前年份是否闰年

def year(num):
    rest = num % 100
    if rest == 0:
        if num % 400 == 0:
            return True
    else:
        if num % 4 == 0:
            return True
    return False

# 初始化函数，设定基准等等
def initialize(context):
    run_daily(demo1, time='every_bar')

def demo1(context):
    date = context.current_dt.strftime('%Y-%m-%d')
    if date == '2018-03-01':
        order('000001.XSHE', 100)
        log.info('buying')
    if date == '2018-03-02':
        order('000001.XSHE',-100)
        log.info('selling')


# 导入函数库
from jqdata import *


# 初始化函数，设定基准等等
def initialize(context):
    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')

    run_daily(before_market_open, time='before_open', reference_security='000300.XSHG')
    # 开盘时运行
    run_daily(market_open, time='open', reference_security='000300.XSHG')
    # 收盘后运行
    run_daily(after_market_close, time='after_close', reference_security='000300.XSHG')


## 开盘前运行函数
def before_market_open(context):
    # 输出运行时间
    log.info('函数运行时间(before_market_open)：' + str(context.current_dt.time()))

    # 给微信发送消息（添加模拟交易，并绑定微信生效）
    # send_message('美好的一天~')

    # 要操作的股票：平安银行（g.为全局变量）
    g.security = '000001.XSHE'


## 开盘时运行函数
def market_open(context):
    log.info('函数运行时间(market_open):' + str(context.current_dt.time()))
    security = g.security
    # 获取股票的收盘价
    close_data = get_bars(security, count=5, unit='1d', fields=['close'])
    close_data_20 = get_bars(security, count=20, unit='1d', fields=['close'])
    # 取得过去五天的平均价格
    MA5 = close_data['close'].mean()
    MA20 = close_data_20['close'].mean()
    # 取得上一时间点价格
    current_price = close_data['close'][-1]
    # 取得当前的现金
    cash = context.portfolio.available_cash

    # 如果上一时间点价格高出五天平均价1%, 则全仓买入
    if current_price > 1.01 * MA5:
        # 记录这次买入
        log.info("价格高于均价 1%%, 买入 %s" % (security))
        # 用所有 cash 买入股票
        order_value(security, cash)
    # 如果上一时间点价格低于五天平均价, 则空仓卖出
    elif current_price < MA5 and context.portfolio.positions[security].closeable_amount > 0:
        # 记录这次卖出
        log.info("价格低于均价, 卖出 %s" % (security))
        # 卖出所有股票,使这只股票的最终持有量为0
        order_target(security, 0)
    elif current_price > 1.02 * MA20:
        log.info("price is higher than 20 %s" % (security))
        order_target(security, 0)


## 收盘后运行函数
def after_market_close(context):
    log.info(str('函数运行时间(after_market_close):' + str(context.current_dt.time())))
    # 得到当天所有成交记录
    trades = get_trades()
    for _trade in trades.values():
        log.info('成交记录：' + str(_trade))
    log.info('一天结束')
    log.info('##############################################################')
