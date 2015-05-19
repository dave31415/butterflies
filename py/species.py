from pyquery import PyQuery as pq
from collections import defaultdict
from params import root_dir


def get_species_from_html():
    """
    Gets the species list from the html file from here
    http://www.ucl.ac.uk/taxome/tabd/php/taxonomysearch.php
    """
    root = pq(filename="%s/data/species.html" % root_dir)
    selects = root.find("select")
    assert len(selects) == 5
    data = defaultdict(list)
    for select in selects:
        name = select.name
        for option in select.findall("option"):
            text = option.text
            if text.startswith('--') or len(text) < 2:
                pass
            else:
                data[name].append(text)
    for k, v in data.iteritems():
        print "%s: %s values" % (k, len(v))

    return data