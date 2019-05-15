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

channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')

当然如果你是分发的，这个key值自动忽略了。
### Direct exchange
直接转发
