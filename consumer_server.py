import asyncio
from confluent_kafka import Consumer

BROKER_URL = "PLAINTEXT://localhost:9092"

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': BROKER_URL,
        'group.id': '0',
    })
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume()
        
        for message in messages:
            print(message.value())
            
        await asyncio.sleep(1.0)
                
def run_consumer():
    asyncio.run(consume('police.calls'))
        
if __name__ == '__main__':
    run_consumer()