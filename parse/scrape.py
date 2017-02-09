import sys
from lxml import etree

def scrape_api(path):
    with open(path, 'r') as f:
        tree = etree.parse(f)
        
        keywords = (
            ('commands', tree.xpath("//command")),
            ('events', tree.xpath("//event")),
            ('enums', tree.xpath("//enum"))
        )
        return {name: ["_".join([v.xpath('ancestor::class')[0].attrib['name'], v.attrib['name']]) for v in val] for name, val in keywords}

def scrape_notepad(path):
    with open(path, 'r') as f:
        tree = etree.parse(f)
        
        keywords = (
            ('commands', tree.xpath("//Keywords[@name='Keywords2']/text()")[0]),
            ('events', tree.xpath("//Keywords[@name='Keywords3']/text()")[0]),
            ('enums', tree.xpath("//Keywords[@name='Keywords4']/text()")[0])
        )
        return {name: val.split(' ') for name, val in keywords}

def main():
    if len(sys.argv) < 2:
        print('usage: python scrape.py gecko.xml userDefineLang_BGScript.xml > ../grammars/bgscript.cson')
        exit(1)
    
    # scrape gecko.xml
    api = scrape_api(sys.argv[1])
    
    # scrape notepad++ lang (if present)
    if len(sys.argv) == 3:
        np = scrape_notepad(sys.argv[2])
        for k in api:
            api[k] += np[k]
    
    # ensure unique values, also concat
    for k in api:
        api[k] = "|".join([v for i, v in enumerate(api[k]) if v not in api[k][:i]])
    
    # apply to template
    with open('template.cson', 'r') as f:
        print(f.read().format(**api))

if __name__ == "__main__":
    main()
