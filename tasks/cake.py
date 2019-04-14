# -*- coding: utf-8 -*-
import json
from time import sleep
from pprint import pprint
from datetime import datetime, timedelta
from mrq.task import Task
from mrq.context import log, connections, run_task, get_current_job, get_current_worker
from mrq.basetasks.utils import JobAction


class Cake(Task):

    def run(self, params):
        return
