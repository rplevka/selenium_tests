from fauxfactory import gen_string
import random

def test_foo(selenium):
    selenium.get('https://www.sme.sk/search?q={0}&period=190'.format(gen_string('alpha'), 3))
    aas = selenium.find_elements_by_tag_name('a')
    index = random.choice(range(0, len(aas)-1))
    selenium.get(aas[index].get_attribute("href"))
