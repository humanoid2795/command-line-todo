import argparse
import task


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    parser_insert = subparsers.add_parser('insert', help='Insert Command')
    parser_insert.add_argument('--name', '-n', required=True, help='Task name')
    parser_insert.add_argument('--description', '-d', help='Task Description')
    parser_insert.add_argument('--limit', '-l', help='Task time limit.')

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('--name', '-n', required=True, help='Task name')

    parser_update = subparsers.add_parser('update')
    parser_update.add_argument('--name', '-n', required=True, help='Task name')
    parser_update.add_argument('--description', '-d', help="Task Description")
    parser_update.add_argument('--limit', '-l', help='Task time limit.')

    _parser_show = subparsers.add_parser('show', help='Show Todo')

    argument_parser = parser.parse_args()
    if argument_parser.subparser_name == 'insert':
        task.Task.insert(
            name=argument_parser.name,
            description=argument_parser.description,
            limit=argument_parser.limit,
        )
    elif argument_parser.subparser_name == 'delete':
        task.Task.delete(name=argument_parser.name)
    elif argument_parser.subparser_name == 'update':
        task.Task.update(
            name=argument_parser.name,
            description=argument_parser.description,
            limit=argument_parser.limit,
        )
    elif argument_parser.subparser_name == 'show':
        task.Task.show()
    else:
        pass


if __name__ == '__main__':
    main()
