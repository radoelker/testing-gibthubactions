import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    print(" [*] Processing message...")
    time.sleep(2)  # Simulate work
    print(" [✓] Done processing")
    
    # Acknowledge AFTER successful processing
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Remove auto_ack=True, handle acknowledgment manually
channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
