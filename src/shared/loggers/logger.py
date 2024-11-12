import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger: 
    def info(self, message):
        logging.info(message)
    
    def warning(self, message):
        logging.warning(message)
    
    def error(self, message):
        logging.error(message)

    def success(self, message):
        logging.info(message)

    def log(self, name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                if result is not None:
                    size = result.shape[0]
                    logging.info(f"{name} size: {size} rows")
                logging.info(
                    f"{func.__name__} executed in {execution_time:.2f} seconds"
                )

                return result
            
            return wrapper

        return decorator
    

if __name__ == '__main__':
    logger = Logger()
    
    logger.warning('WARNING TEST')
    logger.info('INFO TEST')
    logger.error('ERROR TEST')
    logger.success('SUCCESS TEST')
    logger.log('LOG')