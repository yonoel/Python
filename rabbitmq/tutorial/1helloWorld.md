## Introduction
## Hello World!
(using the Pika Python client)
### sending
Our first program send.py will send a single message to the queue. The first thing we need to do is to establish a connection with RabbitMQ server.

```
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```
Next, before sending we need to make sure the recipient queue exists. If we send a message to non-existing location, RabbitMQ will just drop the message. Let's create a hello queue to which the message will be delivered:
```
channel.queue_declare(queue='hello')
```
In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange. But let's not get dragged down by the details ‒ you can read more about exchanges in the third part of this tutorial. All we need to know now is how to use a default exchange identified by an empty string. This exchange is special ‒ it allows us to specify exactly to which queue the message should go. The queue name needs to be specified in the routing_key parameter:
```
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
```
finally we should close connection
### Receiving
Our second program receive.py will receive messages from the queue and print them on the screen.

Again, first we need to connect to RabbitMQ server. The code responsible for connecting to Rabbit is the same as previously.

Again, first we need to connect to RabbitMQ server. The code responsible for connecting to Rabbit is the same as previously.
```
channel.queue_declare(queue='hello')
```
You may ask why we declare the queue again ‒ we have already declared it in our previous code. We could avoid that if we were sure that the queue already exists. For example if send.py program was run before. But we're not yet sure which program to run first. In such cases it's a good practice to repeat declaring the queue in both programs.
```
Listing queues
    You may wish to see what queues RabbitMQ has and how many messages are in them. You can do it (as a privileged user) using the rabbitmqctl tool:

    sudo rabbitmqctl list_queues
    rabbitmqctl.bat list_queues

```
Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. Whenever we receive a message, this callback function is called by the Pika library. In our case this function will print on the screen the contents of the message.

```
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
```
Next, we need to tell RabbitMQ that this particular callback function should receive messages from our hello queue:
```
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)
```
And finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary.
```
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```
