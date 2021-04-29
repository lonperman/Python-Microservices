import pika, json

params = pika.URLParameters('amqps://wwwzopqg:6GpZUvY1WtpAoaF98SiYa5t4CB0f1UZA@clam.rmq.cloudamqp.com/wwwzopqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)