# Publish/Subscribe

## What This Tutorial Focuses On

 In this part we'll do something completely different -- we'll deliver a message to multiple consumers. This pattern is known as "publish/subscribe".

 To illustrate the pattern, we're going to build a simple logging system. It will consist of two programs -- the first will emit log messages and the second will receive and print them.

In our logging system every running copy of the receiver program will get the messages. That way we'll be able to run one receiver and direct the logs to disk; and at the same time we'll be able to run another receiver and see the logs on the screen.

Essentially, published log messages are going to be broadcast to all the receiver

## Exchanges

之前都是指定一个queue来分发任务，现在介绍一下rabbitmq的数据模型

Let's quickly go over what we covered in the previous tutorials:

+ A producer is a user application that sends messages.
+ A queue is a buffer that stores messages.
+ A consumer is a user application that receives messages.

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.
生产者永不直接发消息到队列，实际上，生产者甚至不知道，消息会不会分发给队列。
Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.
生产者其实是把消息发给了交换机，交换机负责消息的接收和发送。
There are a few exchange types available: direct, topic, headers and fanout. We'll focus on the last one -- the fanout. Let's create an exchange of that type, and call it logs:
交换机有以下不同的类型direct，topic，headers，fanout。

### Listing exchanges

To list the exchanges on the server you can run the ever useful rabbitmqctl:

sudo rabbitmqctl list_exchanges

In this list there will be some amq.* exchanges and the default (unnamed) exchange. These are created by default, but it is unlikely you'll need to use them at the moment.

### The default exchange

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

因为是交换机默认是fanout，所以需要我们指明哪一条临时queue
Firstly, whenever we connect to Rabbit we need a fresh, empty queue. To do it we could create a queue with a random name, or, even better - let the server choose a random queue name for us. We can do this by not supplying the queue parameter to queue_declare:

result = channel.queue_declare()

At this point result.method.queue contains a random queue name. For example it may look like amq.gen-JzTY20BRgKO-HjmUJj0wLg

secondly, once the consumer connection is closed, the queue should be deleted. There's an exclusive flag for that:

result = channel.queue_declare(exclusive=True)

You can learn more about the exclusive flag and other queue properties in the guide on queues.

## Bindings

We've already created a fanout exchange and a queue. Now we need to tell the exchange to send messages to our queue. That relationship between exchange and a queue is called a binding.
队列和交换机之间的关系叫做绑定。

channel.queue_bind(exchange='logs',
                   queue=result.method.queue)

From now on the logs exchange will append messages to our queue.

### Listing bindings

You can list existing bindings using, you guessed it,

rabbitmqctl list_bindings

## End

见 emit_log.py (source),receive_logs.py (source)














