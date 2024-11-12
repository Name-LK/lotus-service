from confluent_kafka import Consumer, KafkaError, KafkaException
from src.shared.loggers import logger

class CustomConsumer:
    def __init__(self, config):
        self.consumer = Consumer(config)
        
    def subscribe(self, topics):
        try:
            self.consumer.subscribe(topics)
            logger.info(f"Subscribed to topics: {topics}")
        
        except KafkaException as e:
            logger.error(f"Failed to subscribe to topics {topics}: {e}")
            raise

    def poll(self, timeout):
        try:
            msg = self.consumer.poll(timeout)
            if msg is None:
                pass
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.warning(f"End of the partition reached {msg.topic()} [{msg.partition()}]")
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                logger.info(msg.value().decode('utf-8'))
        except KafkaException as e:
            logger.error(f"Polling error: {e}")
            raise
        
    def close(self):
        try:
            self.consumer.close()
            logger.info("Consumer closed")
        except KafkaException as e:
            logger.error(f"Failed to close consumer: {e}")
            raise