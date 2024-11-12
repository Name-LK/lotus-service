from confluent_kafka import Producer
from src.shared.loggers import logger

class CustomProducer:
    def __init__(self, config):
        self.producer = Producer(config)
        
    def delivery_callback(self, err, msg):
        if err is not None:
            logger.error(f"Message sent failure: {err}")
        else:
            logger.success(f"Message delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}")
    
    def message(self):
        msg = input('Type a message to send _ ')
        return msg
        
    def producing(self, topic):
        while True:
            self.producer.produce(topic, value=self.message(), callback=self.delivery_callback)
            logger.warning(f"Producing to topic: {topic}")
            self.producer.flush()