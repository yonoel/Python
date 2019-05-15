# Publish/Subscribe
## What This Tutorial Focuses On
 In this part we'll do something completely different -- we'll deliver a message to multiple consumers. This pattern is known as "publish/subscribe".

 To illustrate the pattern, we're going to build a simple logging system. It will consist of two programs -- the first will emit log messages and the second will receive and print them.

 ## Exchanges
In previous parts of the tutorial we sent and received messages to and from a queue. Now it's time to introduce the full messaging model in Rabbit.

Let's quickly go over what we covered in the previous tutorials:

+ A producer is a user application that sends messages.
+ A queue is a buffer that stores messages.
+ A consumer is a user application that receives messages.

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.
生产者不要直接发送任何信息到队列里。事实上，生产者甚至不知道一个消息会被分发到一个队列。

Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.
替代来说，生产者仅发送消息到一个转换器。转换器一边接受来自生产者到信息，一边推送信息到队列。转换器要准确知道它对消息到处理，需要去哪个队列？还是多个队列？是否要忽视这条消息等等。。
There are a few exchange types available: direct, topic, headers and fanout. We'll focus on the last one -- the fanout. Let's create an exchange of that type, and call it logs:
```
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
```
fanout分发

### Listing exchanges
To list the exchanges on the server you can run the ever useful rabbitmqctl:

sudo rabbitmqctl list_exchanges
In this list there will be some amq.* exchanges and the default (unnamed) exchange. These are created by default, but it is unlikely you'll need to use them at the moment.

The default exchange
In previous parts of the tutorial we knew nothing about exchanges, but still were able to send messages to queues. That was possible because we were using a default exchange, which we identify by the empty string ("").

Recall how we published a message before:

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
The exchange parameter is the name of the exchange. The empty string denotes the default or nameless exchange: messages are routed to the queue with the name specified by routing_key, if it exists.

Now, we can publish to our named exchange instead:

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
## Temporary queues
Being able to name a queue was crucial for us -- we needed to point the workers to the same queue. Giving a queue a name is important when you want to share the queue between producers and consumers.

但是这种情况下的channel应该都是临时的
Firstly, whenever we connect to Rabbit we need a fresh, empty queue. To do it we could create a queue with a random name, or, even better - let the server choose a random queue name for us. We can do this by not supplying the queue parameter to queue_declare:

result = channel.queue_declare()

At this point result.method.queue contains a random queue name. For example it may look like amq.gen-JzTY20BRgKO-HjmUJj0wLg.

Secondly, once the consumer connection is closed, the queue should be deleted. There's an exclusive flag for that:

result = channel.queue_declare(exclusive=True)
## Bindings
We've already created a fanout exchange and a queue. Now we need to tell the exchange to send messages to our queue. That relationship between exchange and a queue is called a binding.

channel.queue_bind(exchange='logs',
                   queue=result.method.queue)

### Listing bindings
rabbitmqctl list_bindings

## End
The most important change is that we now want to publish messages to our logs exchange instead of the nameless one. We need to supply a routing_key when sending, but its value is ignored for fanout exchanges
不需要声明路由了