## 【dataframe】选取数据
### 摘要
+ 选取行名、列名、值
+ 以标签label（行、列的名字）为索引选择数据—— x.loc[行标签,列标签]
+ 以位置position（第几行、第几列）为索引选择数据—— x.iloc[行位置,列位置]
+ 同时根据标签和位置选择数据——x.ix[行,列]
+ 选择连续的多行多列——切片
+ 选择不连续的某几行或某几列
+ 简便地获取行或列
+ 如何返回一个dataframe的单列或单行
+ 按条件选取数据——df[逻辑条件]
```
            open	close	high	low
2016-02-01	8.08	7.93	8.10	7.88
2016-02-02	7.93	8.05	8.12	7.92
2016-02-03	7.97	7.97	8.00	7.91
2016-02-04	8.00	8.05	8.09	8.00
```
### 获得row 行名
df.index:DatetimeIndex(['2016-02-01', '2016-02-02', '2016-02-03', '2016-02-04'], dtype='datetime64[ns]', freq=None, tz=None)
### 选择列名
df.columns:Index([u'open', u'close', u'high', u'low'], dtype='object')
### 选择值
df.values:array([[ 8.08,  7.93,  8.1 ,  7.88],
       [ 7.93,  8.05,  8.12,  7.92],
       [ 7.97,  7.97,  8.  ,  7.91],
       [ 8.  ,  8.05,  8.09,  8.  ]])

一句话总结，就index是单数，其他是复数，但是index和columns返回的是内置index类型，而values就随意咯
;index也能切片，column理论上也行


### 以标签（行、列的名字）为索引选择数据—— df.loc[行标签,列标签]
选择行标签为'2016-02-01'，列标签为'open'，的数据
df.loc['2016-02-01','open']:8.0800000000000001
### 以位置（第几行、第几列）为索引选择数据—— df.iloc[行位置,列位置]
 选择第1行第1列的数据
df.iloc[0,0]:8.0800000000000001
### 同时根据标签和位置选择数据——df.ix[行,列]
 选择第1行列为‘open’的数据
df.ix[0,'open']:8.080000000001


一句话总结，必定先行后列,loc是name，iloc是用num，ix是随便
### 选择连续的多行多列——切片
切片在.loc、.iloc、.ix三种方法中都可以应用

选择行从'2016-02-02'到'2016-02-04'，列从'open'到'high'的数据

选择从第2行到最后一行，列从第1列到第3列的数据(注意此时的列会多1，多了（行名）这一列)

df.loc['2016-02-02':'2016-02-04','open':'high']

df.iloc[1:,0:3]

df.ix['2016-02-02':'2016-02-04',:3]

备注：当以标签名选取不连续的某几行的时候在这个例子中如df.loc['2016-02-02','2016-02-04',:]这样写会出错，，是时间格式的原因，这样写就可以了df.ix[[pd.Timestamp('2016-02-02'), pd.Timestamp('2016-02-04')]]
### 选择不连续的某几行或某几列
df.loc[:,['open','high']]

df.iloc[:,[0,2]]

df.ix[:,['open',2]]
### 简便地获取行或列
直接用切片获取行，直接用标签名获取列。注意不要错乱。

df['2016-02-02':'2016-02-04']

df[0:3]

df[['open','high']]

df['open']

### 如何返回一个dataframe的单列或单行
如上此时返回的是一个series，而不是dataframe，有时单独只获取一行的时候也会返回一个series，如df.ix[0,:]。

df.ix[0,:]

若要返回dataframe，可用中括号把索引括上，如下。

df[['open']]

df.ix[[0],:]
### 按条件选取数据——df[逻辑条件]
逻辑条件支持&(与)、|(或)、~(非)等逻辑运算(这是py里的二进制操作符啊。。)

df[df['open']>=8]

多个条件之间运算时用括号括起
df[(df.index=='2016-02-02') | (df['open']>=8)]


选择df中不在[8.10,8]的数据
df[~df.isin([8.10,8])]

把df中open大于8的替换为123
df[df['open']>=8]=123


#【dataframe】转置、排序
## 转置——df.T
## 按行名或列名排序——df.sort_index
df.sort_index(axis=0,ascending=True)

+ axis= 0 为按行名排序；1 为按列名排序
+ ascending= True 为升序； False 为降序
## 按值排序——df.sort
df.sort(by=, ascending=True)

+ by 按哪一列的值排序，默认是按行标签排序
+ ascending= True 为升序； False 为降序

# [dataframe] 增删行或列
## 增加一列 column
    df['newColumn']=[1,2,3,4]
## 增加一行 row
    df.loc['newIndex',:]=[1,1,1,1,1]
## 删除行或列——df.drop
    df.drop(labels,axis=0，inplace=False)
+ labels 行或列的标签名，写在第一个可省略。
+ axis= 0 删除行；1 删除列
+ inplace= False 生成新dataframe；True 不生成新的dataframe，替换原本dataframe。默认是False。
+ 该操作默认返回的是另一个新的dataframe，以至于原来的没有变，如在下面第一个例子中删除的列，在第二个例子中还有。要替换原来的请调整inplace参数
    
    df.drop(['newColumn','close'],axis=1)
# [dataframe] 连接
## concat
    
    concat([df1,df2,...],axis=0)

+ axis= 0 纵向,可以省略；1 横向。
+ 使用前需导入过pandas模块
+ 使用时要注意连接的dataframe行列对齐
+ 可以同时拼接多个dataframe
+ 拼接是强制的，允许连接后存在同名的行或列，见纵向连接的第二个例子

    pd.concat([df1,df2],axis=1)
    
    pd.concat([df1,df3,df3],axis=0)
## 按索引链接——join    
    df1.join([df2,df3,...])
+ 含义为按照df1的索引，将df1，df2，df3...链接起来，返回一个链接后的dataframe。
+ df1，df2，df3...皆为dataframe 使用样例：
    ```
    q = query(
    valuation.pe_ratio,valuation.market_cap,valuation.code
    ).filter(
    valuation.code.in_(['000001.XSHE','000002.XSHE']))
    df1 = get_fundamentals(q, '2017-10-15')
    log.info(df1)
    # 调整股票代码为index
    df1.index=df1['code']
    log.info(df1)
    df2=get_all_securities(types=['stock'],date='2017-10-15')
    log.info(df2.head())
    log.info(df1.join([df2]))
    ```
# dataframe 组建
## 组建方法——pd.DataFrame
pd.DataFrame(data=None, index=None, columns=None)

+ data= 数据
+ index= 索引，即行名、行表头
+ columns= 列名、列表头
```
# 建立一个简单的dataframe
# 一个三行两列的数据
d= [[1,2],
    [3,4],
    [5,6]]
# 列名
v=['a','b']
#行名
h=['c','d','e']
收起代码 ↑    
# 将数据d，列名v，行名h组合成一个dataframe
df = pd.DataFrame(data=d,index=h,columns=v)
df
```
## 用字典型数据组建——pd.DataFrame
方法基本同上，因为字典型自带一个标签，所以就不用写列名了。例子如下：
```
# 建立一个简单的字典型数据
dic={'a':[1,3,5],'b':[2,4,6]}
dic
{'a': [1, 3, 5], 'b': [2, 4, 6]}
df = pd.DataFrame(data=dic,index=['c','d','e'])
df
```
## 简便地获得聚宽数据中的时间索引
有时建立一个dataframe时，为了和平台数据保持一致，需要使用相同的时间行索引，但时间数据操作复杂，而且涉及到节假日、非交易日等问题,直接建立比较困难，这里介绍一种简单的方法，快速获得跟平台数据一致的时间索引。

```
h=get_price('000001.XSHE',start_date='2016-02-01',end_date='2016-02-03',frequency='daily').index
h
DatetimeIndex(['2016-02-01', '2016-02-02', '2016-02-03'], dtype='datetime64[ns]', freq=None, tz=None)
用获得的时间索引，组建dataframe

df = pd.DataFrame(data=dic,index=h)
```
# 【dataframe】缺失值处理
## 去掉缺失值——df.dropna
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
+ axis= 0 按行检查缺失；1 按列检查缺失。不写默认为0
+ how= 'any' 有一个缺失值就算缺失；'all' 行或列(根据axis参数)全缺失才算缺失。不写默认为'any'
+ thresh= x,x为一个整数,含义为行或列(根据axis参数)中非缺失数值个数大于等于x则不算缺失，即小于x则算缺失，会被去除。
+ subset= 标签名。选择要对哪个列或行（与axis中的相反）进行检查缺失，没写的则不检查。即限制检查范围。
```
# 参数全不设置则取默认值，即axis=0, how='any', thresh=None, subset=None, inplace=False
# 即去掉缺失值所在的行
df.dropna()
#  按列检查是否缺失，去掉缺失值所在的列
df.dropna(axis=1)
#  按列检查是否缺失，若列中全部缺失才去除。所以例子中没有去除
df.dropna(axis=1,how='all')
#  按列检查是否缺失，只保留非缺失值大于等于2个的。high列只有一个非缺失值，该列被去掉。
df.dropna(axis=1,thresh=2)
#  按行检查是否缺失，只检查high列和close列，去掉这两列中含有缺失值的行
df.dropna(axis=0,subset=['low','close'])
```
## 对缺失值进行填充——df.fillna
df.fillna(value=None,axis=None)

+ value= 替换缺失值的值。可以是单个值、字典、dataframe等，但不能是list。区别请看例子。
```
# 把缺失值替换成233
df.fillna(value=233)
# 用字典时：仅替换open列中的缺失值
df.fillna(value={'open':233})
# 用dataframe时：替换df中的缺失值，如果缺失则替换为gf中对应位置的值
df.fillna(value=gf)
```
## 判断数据是否为缺失——df.isnull
为什么要这样用这个方法判断是否为缺失？

因为nan不等于nan
# 【dataframe】常用统计函数
常用统计函数
+ describe 针对Series或个DataFrame列计算汇总统计
+ count 非na值的数量
+ min、max 计算最小值和最大值
+ idxmin、idxmax 计算能够获取到最大值和最小值得索引值
+ quantile 计算样本的分位数（0到1）  其实取的是50%分位数
+ sum 值的总和
+ mean 值得平均数
+ median 值得算术中位数（50%分位数）
+ mad 根据平均值计算平均绝对离差 离差也叫偏差—，某一子样值与平均值之差（绝对离差），即x-xˉ，相对离差即x-xˉ /xˉ * 100% 
+ var 样本值的方差
+ std 样本值的标准差
+ skew 样本值得偏度（三阶矩）
+ kurt 样本值得峰度（四阶矩）
+ cumsum 样本值得累计和
+ cummin，cummax 样本值得累计最大值和累计最小值
+ cumprod 样本值得累计积
+ diff 计算一阶差分
+ pct_change 计算百分数变化

# panel类型数据怎么处理
dataframe是一个二维的表，panel则是三维的“包”。
```
pa=get_price(['000001.XSHE','000002.XSHE','000004.XSHE'],start_date='2016-02-01',end_date='2016-02-04',fields=['open','high','low','close'])
pa
<class 'pandas.core.panel.Panel'>
Dimensions: 4 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: close to open
Major_axis axis: 2016-02-01 00:00:00 to 2016-02-04 00:00:00
Minor_axis axis: 000001.XSHE to 000004.XSHE
```
如上面获得的panel数据——pa，是一个“4 (items) x 4 (major_axis) x 3 (minor_axis)”三维的数据。有三个维度：

+ Items axis: close to open，即从收盘价close到开盘价open。
+ major_axis axis: 2016-02-01 00:00:00 to 2016-02-04 00:00:00 ，即时间维度。
+ Minor_axis axis: 000001.XSHE to 000004.XSHE，即个股维度。
## panel的取用方法¶
panel类型的的取用方法类似与dataframe，看下例子也就明白了。一般要做统计方面的工作，也是如下分解成dataframe进行操作，基本满足日常需求。

```
# 每天'000001.XSHE'的各个价格
pa[:,:,'000001.XSHE']
# 每天各个股票的收盘价
pa['close',:,:]
# '2016-02-01'各个股票的各个价格
pa[:,'2016-02-01',:]
```
 









    



    

    




