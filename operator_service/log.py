#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#

import logging
import logging.config
import os
from pathlib import Path

import coloredlogs
import yaml


def setup_logging(log_config_path=None, log_level=None):
    """Logging Setup"""
    if env_log_level := os.getenv("LOG_LEVEL", None):
        print(f"env var LOG_LEVEL detected = {env_log_level}")
        log_level = env_log_level

    if env_log_config_path := os.getenv("LOG_CFG", None):
        print(f"env var LOG_CFG detected = {env_log_config_path}")
        log_config_path = env_log_config_path

    if log_level:
        print(f"Using basic logging config, log level = {log_level}")
        logging_level = logging._nameToLevel.get(log_level)
        logging.basicConfig(level=logging_level)
        coloredlogs.install(level=logging_level)
    elif log_config_path:
        log_config_path = Path(log_config_path).expanduser().resolve()
        print(f"Using logging config file, {log_config_path}")
        with open(log_config_path, "rt") as f:
            log_config_dict = yaml.safe_load(f.read())
            logging.config.dictConfig(log_config_dict)
    else:
        print("Using default logging config, log level = INFO")
        logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
