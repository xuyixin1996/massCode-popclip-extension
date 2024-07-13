from masscode import create_snippet
import unittest

text = """@click.command()
@click.option('--hash-type',
              type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
def digest(hash_type):
    click.echo(hash_type)
"""


class TestMasscode(unittest.TestCase):
    def test_create_snippet(self):
        create_snippet(text)


if __name__ == "__main__":
    unittest.main()
