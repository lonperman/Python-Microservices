import pika

params = pika.URLParameters('amqps://wwwzopqg:6GpZUvY1WtpAoaF98SiYa5t4CB0f1UZA@clam.rmq.cloudamqp.com/wwwzopqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')