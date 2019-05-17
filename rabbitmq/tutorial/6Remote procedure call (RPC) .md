# Remote procedure call (RPC)

## What This Tutorial Focuses On

## Client interface

To illustrate how an RPC service could be used we're going to create a simple client class. It's going to expose a method named call which sends an RPC request and blocks until the answer is received:

fibonacci_rpc = FibonacciRpcClient()
result = fibonacci_rpc.call(4)
print("fib(4) is %r" % result)

## Callback queue

In general doing RPC over RabbitMQ is easy. A client sends a request message and a server replies with a response message. In order to receive a response the client needs to send a 'callback' queue address with the request. Let's try it:

result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            ),
                      body=request)

## Message properties

The AMQP 0-9-1 protocol predefines a set of 14 properties that go with a message. Most of the properties are rarely used, with the exception of the following:

+ delivery_mode: Marks a message as persistent (with a value of 2) or transient (any other value). You may remember this property from the second tutorial.
+ content_type: Used to describe the mime-type of the encoding. For example for the often used JSON encoding it is a good practice to set this property to: application/json.
+ reply_to: Commonly used to name a callback queue.
+ correlation_id: Useful to correlate RPC responses with requests.

## Correlation id

In the method presented above we suggest creating a callback queue for every RPC request. That's pretty inefficient, but fortunately there is a better way - let's create a single callback queue per client.
之前是对每一个请求创造了一个回调的队列，这样非常无效，浪费太多。所以我们创造单一的队列处理每一个请求。

That raises a new issue, having received a response in that queue it's not clear to which request the response belongs. That's when the correlation_id property is used. We're going to set it to a unique value for every request. Later, when we receive a message in the callback queue we'll look at this property, and based on that we'll be able to match a response with a request. If we see an unknown correlation_id value, we may safely discard the message - it doesn't belong to our requests.
这就导致了一个问题，队列不清楚响应属于哪个请求。这就是统计id属性有用的地方，我们为每一个请求设置
一个唯一的值。

You may ask, why should we ignore unknown messages in the callback queue, rather than failing with an error? It's due to a possibility of a race condition on the server side. Although unlikely, it is possible that the RPC server will die just after sending us the answer, but before sending an acknowledgment message for the request. If that happens, the restarted RPC server will process the request again. That's why on the client we must handle the duplicate responses gracefully, and the RPC should ideally be idempotent.

因为如果对一个不可知的请求发送回报，服务器可能死亡，如果这个发生了，需要重启远程服务。

## Summary

Our RPC will work like this:

+ When the Client starts up, it creates an anonymous exclusive callback queue.
+ For an RPC request, the Client sends a message with two properties: reply_to, which is set to the callback queue and correlation_id, which is set to a unique value for every request.
+ The request is sent to an rpc_queue queue.
+ The RPC worker (aka: server) is waiting for requests on that queue. When a request appears, it does the job and sends a message with the result back to the Client, using the queue from the reply_to field.
+ The client waits for data on the callback queue. When a message appears, it checks the correlation_id property. If it matches the value from the request it returns the response to the application.







