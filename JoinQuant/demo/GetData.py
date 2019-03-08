# 导入函数库
from jqdata import *
from sqlalchemy.sql.expression import or_


# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')
    # 过滤掉order系列API产生的比error级别低的log
    # log.set_level('order', 'error')

    ### 股票相关设定 ###

    ## 运行函数（reference_security为运行时间的参考标的；传入的标的只做种类区分，因此传入'000300.XSHG'或'510300.XSHG'是一样的）
    # 开盘前运行
    run_daily(before_market_open, time='before_open', reference_security='000300.XSHG')
    # set_universe(['000001.XSHE','000005.XSHE']) history对象里的股票列表，当列表为none时选
    # 开盘时运行
    # run_daily(market_open, time='open', reference_security='000300.XSHG')
    # 收盘后运行
    # run_daily(after_market_close, time='after_close', reference_security='000300.XSHG')


## 开盘前运行函数
def before_market_open(context):
    # 输出运行时间
    log.info('函数运行时间(before_market_open)：' + str(context.current_dt.time()))
    # stocks = get_index_stocks('000016.XSHG')
    # 获取指数成分股
    # for i in stocks:
    # log.info(i)
    # 获取一系列股票的相关数据
    # history_data = history(1,unit='1d',field="avg",security_list=['000002.XSHE'],df=True,skip_paused=False,fq='pre')
    # history_data = history(count = 1,unit='1d',field="avg",security_list=['000002.XSHE'],df=False,skip_paused=False,fq='pre')
    #  if df = False: log.info(history_data) 这是一个dist对象，value是array
    # arr = history_data['000002.XSHE']
    # for i in arr:
    # log.info(i)
    # 获取单个股票的多个数据
    # attributes =  attribute_history('000002.XSHE',3,unit='1d',fields=['open','close','high','low'],skip_paused=True,df=True,fq='pre')
    # attributes =  attribute_history('000002.XSHE',3,unit='1d',fields=['open','close','high','low'],skip_paused=True,df=False,fq='pre')

    # log.info(attributes)
    # # log.info(attributes.index)
    # log.info('--------')

    # 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
    # q = query(valuation).filter(valuation.code == '000001.XSHE')
    # df = get_fundamentals(q, '2015-10-15')
    # 打印出总市值
    # log.info(df[''market_cap''][0])
    # 获取多只股票在某一日期的市值, 利润
    # df = get_fundamentals(query(
    #     valuation, income
    # ).filter(
    #     # 这里不能使用 in 操作, 要使用in_()函数
    #     valuation.code.in_(['000001.XSHE', '600000.XSHG'])
    # ), date='2015-10-15')
    # 选出所有的总市值大于1000亿元, 市盈率小于10, 营业总收入大于200亿元的股票
    # df = get_fundamentals(query(
    #     valuation.code, valuation.market_cap, valuation.pe_ratio, income.total_operating_revenue
    # ).filter(
    #     valuation.market_cap > 1000,
    #     valuation.pe_ratio < 10,
    #     income.total_operating_revenue > 2e10
    # ).order_by(
    #     # 按市值降序排列
    #     valuation.market_cap.desc()
    # ).limit(
    #     # 最多返回100个
    #     100
    # ), date='2015-10-15')
    # 使用 or_ 函数: 查询总市值大于1000亿元 **或者** 市盈率小于10的股票
    # df = get_fundamentals(query(
    #     valuation.code
    # ).filter(
    #     or_(
    #         valuation.market_cap > 1000,
    #         valuation.pe_ratio < 10
    #     )
    # ))
    # q = query(
    #     income.statDate,
    #     income.code,
    #     income.basic_eps,
    #     balance.cash_equivalents,
    #     cash_flow.goods_sale_and_service_render_cash
    # ).filter(
    #     income.code == '000001.XSHE',
    # )

    # rets = [get_fundamentals(q, statDate='2014q'+str(i)) for i in range(1, 5)]

    # 查询平安银行2014年的年报
    # q = query(
    #     income.statDate,
    #     income.code,
    #     income.basic_eps,
    #     cash_flow.goods_sale_and_service_render_cash
    # ).filter(
    #     income.code == '000001.XSHE',
    # )

    # ret = get_fundamentals(q, statDate='2014')

    # log.info(ret)








