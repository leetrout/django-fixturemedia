from fixture_media.management.commands._utils import file_patt

JSON = """
{
    "thing": {
        "foo1": "bar/baz/bing/bang.foo"
        "foo2": "bar//baz//bing//bang.foo"
        "foo3": "bar\\baz\\bing\\bang.foo"
    }
}
"""

assert len(file_patt.findall(JSON)) == 3
