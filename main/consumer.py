import pika, json

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
# django.setup()

# from products.models import Product

params = pika.URLParameters('amqps://wwwzopqg:6GpZUvY1WtpAoaF98SiYa5t4CB0f1UZA@clam.rmq.cloudamqp.com/wwwzopqg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

callback()