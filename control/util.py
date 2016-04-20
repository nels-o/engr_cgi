import copy, re
import mistune
from mistune import Renderer, InlineGrammar, InlineLexer

class CustomRenderer(Renderer):
    
    def wiki_link(self, alt, link):
        return '<a href="%s">%s</a>' % (link, alt)


class WikiLinkInlineLexer(InlineLexer):
    def enable_wiki_link(self):
        # add wiki_link rules
        self.rules.wiki_link = re.compile(
            r'\[\['                   # [[
            r'([\s\S]+?\|[\s\S]+?)'   # Page 2|Page 2
            r'\]\](?!\])'             # ]]
        )

        # Add wiki_link parser to default rules
        # you can insert it some place you like
        # but place matters, maybe 3 is not good
        self.default_rules.insert(3, 'wiki_link')

    def output_wiki_link(self, m):
        text = m.group(1)
        alt, link = text.split('|')
        # you can create an custom render
        # you can also return the html if you like
        return self.renderer.wiki_link(alt, link)

def parse_wheel_name(name):
    parts = name.split('-')
    result = {
            "package": "",
            "version": "",
            "build": "",
            "python": "",
            "abi": "",
            "platform": ""
            }
    if len(parts) == 6:
        # Build Tag is specified
        result["package"] = parts[0].replace('_', ' ')
        result["version"] = parts[1]
        result["build"] = parts[2]
        result["python"] = parts[3]
        result["abi"] = parts[4]
        result["platform"] = parts[5].split('.')[0]
    elif len(parts) == 5:
        result["package"] = parts[0].replace('_', ' ')
        result["version"] = parts[1]
        result["python"] = parts[2]
        result["abi"] = parts[3]
        result["platform"] = parts[4].split('.')[0]
    else:
        # Malformed wheel name.
        return None
    return result

def inspect_routes(app):
    for route in app.routes:
        if 'mountpoint' in route.config:
            prefix = route.config['mountpoint']['prefix']
            subapp = route.config['mountpoint']['target']

            for prefixes, route in inspect_routes(subapp):
                yield [prefix] + prefixes, route
        else:
            yield [], route