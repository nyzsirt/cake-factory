import argparse
import sys, os
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../'
sys.path.append(BASEPATH)
from mrq.context import connections, log, setup_context, job
import simplejson as json

parser = argparse.ArgumentParser(description='Start and Manipulate Kasirga Job.')
subparsers = parser.add_subparsers(help='<sub-command> help', dest='operation')

product_parser = subparsers.add_parser('order', help='Start')
product_parser.add_argument('--product', dest='product', action='store', required=False, help='')
product_parser.add_argument('--quantity', dest='quantity', action='store', required=False, help='')


stock_parser = subparsers.add_parser('stock', help='Cancel Kasirga Job')
stock_parser.add_argument('--goods', dest='goods', action='store', required=True, help='JSON type parameters')


def order(arguments):
    prm = {
        "product": arguments.product,
        "quantity": arguments.product,
    }
    all_ids = job.queue_jobs("tasks.stock.Stock", prm, queue="low")
    return all_ids


def stock(arguments):
    goods = json.loads(arguments.goods)
    all_ids = job.queue_jobs("tasks.stock.Stock", goods, queue="low")
    return all_ids


if __name__ == '__main__':
    args = parser.parse_args()
    if args.operation == 'order':
        setup_context(file_path=BASEPATH + '/config/config.py', config_type='run')
        order(args)
    elif args.operation == 'stock':
        setup_context(file_path=BASEPATH + '/config/config.py', config_type='run')
        stock(args)
