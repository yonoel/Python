# Routing

## What This Tutorial Focuses On

In the previous tutorial we built a simple logging system. We were able to broadcast log messages to many receivers.

In this tutorial we're going to add a feature to it - we're going to make it possible to subscribe only to a subset of the messages. For example, we will be able to direct only critical error messages to the log file (to save disk space), while still being able to print all of the log messages on the console.

### Bindings

In previous examples we were already creating bindings. You may recall code like:

channel.queue_bind(exchange=exchange_name,
                   queue=queue_name)

A binding is a relationship between an exchange and a queue. This can be simply read as: the queue is interested in messages from this exchange.
一个绑定意味一个一个交换机和队列的联系。

Bindings can take an extra routing_key parameter. To avoid the confusion with a basic_publish parameter we're going to call it a binding key. This is how we could create a binding with a key:
绑定可以有一个额外的路由key参数，我们可以根据这个key创造绑定

channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')

The meaning of a binding key depends on the exchange type. The fanout exchanges, which we used previously, simply ignored its value.
这意味着绑定依赖于交换机的类型，当然如果你是分发的，这个key值自动忽略了。

### Direct exchange

We want to extend that to allow filtering messages based on their severity. For example we may want the script which is writing log messages to the disk to only receive critical errors, and not waste disk space on warning or info log messages.

We were using a fanout exchange, which doesn't give us too much flexibility - it's only capable of mindless broadcasting.

We will use a direct exchange instead. The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.

交换机负责了分发什么数据给什么queue，虽然集中管理了交换，但是万一名字不对咋办？这个key其实类似了queue的name，但是queue的name唯一，key可以同时指向几个quue。

## Multiple bindings

It is perfectly legal to bind multiple queues with the same binding key. In our example we could add a binding between X and Q1 with binding key black. In that case, the direct exchange will behave like fanout and will broadcast the message to all the matching queues. A message with routing key black will be delivered to both Q1 and Q2.

## Emitting logs

Like always we need to create an exchange first:

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
And we're ready to send a message:

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

## Subscribing

Receiving messages will work just like in the previous tutorial, with one exception - we're going to create a new binding for each severity we're interested in.

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
