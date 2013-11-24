#!/usr/bin/env python
from fixture_media.management.commands._utils import file_patt, file_patt_prefixed

JSON = """
{
    "thing": {
        "foo1": "bar/baz/bing/bang.foo"
        "foo2": "bar//baz//bing//bang.foo"
        "foo3": "bar\\baz\\bing\\bang.foo"
        "foo1": "media://pbar/baz/bing/bang.foo"
        "foo2": "media://pbar//baz//bing//bang.foo"
        "foo3": "media://pbar\\baz\\bing\\bang.foo"
    }
}
"""

assert file_patt.findall(JSON) == ['bar/baz/bing/bang.foo', 'bar//baz//bing//bang.foo', 'bar\\baz\\bing\\bang.foo', 'pbar/baz/bing/bang.foo', 'pbar//baz//bing//bang.foo', 'pbar\\baz\\bing\\bang.foo']

assert file_patt_prefixed.findall(JSON) == ['pbar/baz/bing/bang.foo', 'pbar//baz//bing//bang.foo', 'pbar\\baz\\bing\\bang.foo']
