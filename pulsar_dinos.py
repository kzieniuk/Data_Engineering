from pulsar import Client, Message
from dinosaurs import Dinos, get_dino

pulsar_service_url = "pulsar://localhost:6650"

client = Client(pulsar_service_url)

topic_name = "random_dinosaur_queue"

producer = client.create_producer(topic_name)

for _ in range(1001):
    dino_data = get_dino(Dinos())
    message_data = f"Random Dinosaur Data: {dino_data}"
    producer.send(Message(message_data.encode("utf-8")))


producer.close()
client.close()
