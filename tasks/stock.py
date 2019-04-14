# -*- coding: utf-8 -*-
import json
from time import sleep
from pprint import pprint
from datetime import datetime, timedelta
from mrq.task import Task
from mrq.context import log, connections, run_task, get_current_job, get_current_worker
from mrq.basetasks.utils import JobAction


class Stock(Task):

    def run(self, params):
        current_stock = connections.mongodb_sharding.stock
        data_set = current_stock.find({"name": {"$in": params.keys()}})
        for material in params.keys():
            ndata = {
                "name": material,
                "quantity": params[material]
            }
            for data in data_set:
                if material == data["name"]:
                    ndata["quantity"] += data["quantity"]
            current_stock.update({"name":material}, update=ndata, upsery=True)

