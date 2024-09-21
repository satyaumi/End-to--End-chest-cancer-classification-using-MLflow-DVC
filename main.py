from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME ="Data Ingestion stage"



try:
        logger.info(f">>>>>>>>stage{STAGE_NAME} started <<<<<<<")
        obj =DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
        raise e
        
# logger.info('welcome to cnnClassifier')


STAGE_NAME ="prepare base model"
try:    
        logger.info(f"**********************")
        logger.info(f">>>>>>>>stage{STAGE_NAME} started <<<<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} completed <<<<<<<\n\nx======x")
except Exception as e:
        logger.exception(e)
        raise e