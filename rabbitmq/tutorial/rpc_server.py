import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)
    print('done and reply_to is %r'%props.reply_to)

    ch.basic_publish(exchange='', routing_key=props.reply_to, properties=pika.BasicProperties(
        correlation_id=props.correlation_id), body=str(response))
    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue',on_message_callback=on_request)

print(" awaiting RPC requests ")
channel.start_consuming()
