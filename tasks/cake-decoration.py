# -*- coding: utf-8 -*-
import json
from time import sleep
from pprint import pprint
from datetime import datetime, timedelta
from mrq.task import Task
from mrq.context import log, connections, run_task, get_current_job, get_current_worker,job
from mrq.basetasks.utils import JobAction


class Decoration(Task):
    def run(self, params):
        specification = {
            "pineapple": 1,
            "strawberry": 20,
            "banana": 2,
        }

    def run(self, params):
        stockdb = connections.mongodb_sharding.stock
        stocks = stockdb.find({"name": {"$in": self.specification.keys()}})
        is_enough = True

        for metarial in stocks:
            if metarial["quantity"] < self.specification[metarial["name"]]:
                is_enough = False

        if is_enough:
            micro_data = {"action": "decrease"}
            job.queue_jobs("tasks.stock.Stock", dict(self.specification, **micro_data), queue="low")
            job.queue_jobs("tasks.stock.Stock", {"decoration": 10, "action": "increase"}, queue="low")








