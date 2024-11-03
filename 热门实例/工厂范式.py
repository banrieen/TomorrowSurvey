""" Python 编程范式-》工厂模式-工厂方法
"""
import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath,mode="r",encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    def __init__(self, filepath):
        self.etree = etree.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.etree

def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sqlite_factory = connect_to('cookBook/data/person.sq3')
    print()
    xml_factory = connect_to('cookBook/data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall('//*[@id="collapsible3"]/div[1]/div[1]/span[2]')
    # liars = xml_data.findall(".//{}[{}='{}']").format('peson','lastname','liars')
    print('Found: {}'.format(len(liars)))
    print(liars)

    json_factory = connect_to('cookBook/data/person.json')
    json_data = json_factory.parsed_data
    print('Found: {}'.format(len(json_data)))
    print(json_data)

if __name__ == "__main__":
    main()