# utils/logger.py

import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def log_fitness(step, fitness):
    logger.info(f"Step {step}: Fitness = {fitness:.4f}")
