# text_formatter_tool.py
import json
import xml.dom.minidom
from html.parser import HTMLParser
from css_html_js_minify import process_single_html_file, process_single_css_file
import defusedxml.minidom

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("End tag  :", tag)
    def handle_data(self, data):
        print("Data     :", data)

def format(text, format, action):
    if format == 'json':
        if action == 'beautify':
            return json.dumps(json.loads(text), indent=4)
        elif action == 'minify':
            return json.dumps(json.loads(text), separators=(',', ':'))
        elif action == 'validate':
            try:
                json.loads(text)
                return 'Valid JSON'
            except json.JSONDecodeError:
                return 'Invalid JSON'
    elif format == 'xml':
        if action == 'beautify':
            return defusedxml.minidom.parseString(text).toprettyxml()
        elif action == 'minify':
            return defusedxml.minidom.parseString(text).toxml()
        elif action == 'validate':
            try:
                defusedxml.minidom.parseString(text)
                return 'Valid XML'
            except xml.parsers.expat.ExpatError:
                return 'Invalid XML'
    elif format == 'html':
        if action == 'beautify':
            return process_single_html_file(text, overwrite=False)
        elif action == 'minify':
            return process_single_html_file(text, overwrite=False, remove_comments=True, reduce_empty_attributes=True, remove_optional_attribute_quotes=False)
        elif action == 'validate':
            parser = MyHTMLParser()
            parser.feed(text)
            return 'HTML Parsed'
    elif format == 'css':
        if action == 'beautify':
            return process_single_css_file(text, overwrite=False)
        elif action == 'minify':
            return process_single_css_file(text, overwrite=False, remove_comments=True, reduce_empty_attributes=True, remove_optional_attribute_quotes=False)
    # Add more formats and actions as needed
