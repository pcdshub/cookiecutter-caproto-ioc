import textwrap

import caproto.server

from .{{cookiecutter.import_name}} import {{cookiecutter.import_name.capitalize() }}


def main():
    ioc_options, run_options = caproto.server.ioc_arg_parser(
        default_prefix='{{ cookiecutter.default_prefix }}',
        desc=textwrap.dedent({{cookiecutter.import_name.capitalize()}}.__doc__)
    )

    ioc = {{cookiecutter.import_name.capitalize()}}(**ioc_options)
    caproto.server.run(ioc.pvdb, **run_options)


if __name__ == '__main__':
    main()
