import argparse


def command_get(args):
    print(args)


def command_delete(args):
    print(args)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_get = subparsers.add_parser("get", help="get resource")
parser_delete = subparsers.add_parser("delete", help="delete resource")

parser_get.add_argument("resource")
parser_get.add_argument("resource_name", default=None, nargs="?")
parser_get.add_argument("--no-header", action="store_true")
parser_get.set_defaults(handler=command_get)

parser_delete.add_argument("resource")
parser_delete.add_argument("resource_name", default=None, nargs="?")
parser_delete.set_defaults(handler=command_delete)

args = parser.parse_args()

args.handler(args)

