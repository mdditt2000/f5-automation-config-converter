import json
import argparse
from deepdiff import DeepDiff
from pprint import pprint
import sys
import os
from bs4 import BeautifulSoup
import re
import fileinput

class Diff:
    def get_arguments(self):
        parser = argparse.ArgumentParser(description='Diff between 2 AS3 json files: data/as3_from_bigip.json and data/as3_from_charon.json')
        parser.add_argument("--version", type=str, help="Append version to the diff result file.")

        return parser.parse_args()



    def diff(self, version):
        with open('/ansible/data/as3_from_bigip.json') as f:
            data1 = json.load(f)

        with open('/ansible/data/as3_from_charon.json') as f:
            data2 = json.load(f)

        print(json.dumps(data1, sort_keys=True, indent=2))

        print("---------------------------------------------------------")

        print(json.dumps(data2, sort_keys=True, indent=2))

        print("---------------------------------------------------------")

        with open('/ansible/data/as3_from_bigip_sorted.json', 'w') as f:
            json.dump(data1, f, sort_keys=True, indent=2)

        with open('/ansible/data/as3_from_charon_sorted.json', 'w') as f:
            json.dump(data2, f, sort_keys=True, indent=2)

        print("---------------------------------------------------------")

        # https://zepworks.com/deepdiff
        ddiff = DeepDiff(data1, data2, ignore_order=True)

        pprint(ddiff.pretty(), width=1000)
        original_stdout = sys.stdout

        filename = 'diff_' + str(version)

        # Replace /n with <br>
        def replace_newline_with_br(s, soup):
            lines = s.split('\n')
            div = soup.new_tag('div')
            div.append(lines[0])
            for l in lines[1:]:
                div.append(soup.new_tag('br'))
                div.append(l)
            soup.append(div)

        soup = BeautifulSoup("", 'html.parser')
        replace_newline_with_br(ddiff.pretty(), soup)

        # Save in HTML
        with open('/ansible/data/' + filename + '.html', 'w') as f:
            sys.stdout = f 
            print(soup.prettify())
            sys.stdout = original_stdout

        # Get it sorted out
        html = open('/ansible/data/' + filename + '.html','r')
        txt = open('/ansible/data/' + filename + '_sorted.html','w')
        for line in html:
            if not re.search('<br/>',line):
                if not re.search('<div>',line):
                    if not re.search('</div>',line):
                        line = line.replace('Item root', '')
                        line = line.replace('Value of root', '')
                        line = line.replace('Type of root', '')
                        line = line.replace('][', '] [')
                        if line.startswith(' ['):
                            txt.write(line)

        html.close()
        txt.close()

        # Sort it
        os.system('sort /ansible/data/' + filename + '_sorted.html -o /ansible/data/' + filename + '_sorted.html')

        for line in fileinput.input(['/ansible/data/' + filename + '_sorted.html'], inplace=True):
            sys.stdout.write('<br/>{l}'.format(l=line))

        # Delete old sorted jons file used for the diff
        os.remove("/ansible/data/as3_from_bigip_sorted.json")
        os.remove("/ansible/data/as3_from_charon_sorted.json")

    def main(self):
        args = self.get_arguments()
        print(args)
        self.diff(args.version)

if __name__ == "__main__":

    diff = Diff()
    diff.main()
