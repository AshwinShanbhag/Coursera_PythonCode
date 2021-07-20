import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Ashwin</name>
    <phone type="intl">
    +91 9945118177
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
