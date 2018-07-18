import os
import json
import click


@click.command()
@click.option('--base', default='https://schemas.datacubed.com', help='Base URL.')
@click.option('--path', default='schemas', help='Directory to scan.')
@click.option('--ext', default='.json', help='File extension to look for')
def gen_idx(base, path, ext):
    """
    Gets directory tree structure as json of files with specific extension
    """

    def path_to_dict(r_path):
        if os.path.isdir(r_path):
            return {
                k: v
                for k, v in ({
                    x: path_to_dict(os.path.join(r_path, x))
                    for x in os.listdir(r_path)
                }).items() if len(v)
            }
        else:
            if os.path.splitext(r_path)[1] == ext:
                return base + r_path[len(path):]
            else:
                return {}

    click.echo(
        json.dumps(
            path_to_dict(path)
        )
    )


if __name__ == '__main__':
    gen_idx()
