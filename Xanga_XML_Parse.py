import re
import xml.etree.ElementTree as ET


tree1 = ET.parse(file1_pathname)
root1 = tree1.getroot()

tree2 = ET.parse(file2_pathname)
root2 = tree2.getroot()

# print(root.tag, root.attrib)
# print(len(root))

with open('Xanga_blog.txt', 'w') as f:
    for root in [root1, root2]:
        for x in range(len(root)):
            f.write('Date: ')
            f.write(root[x][2].text[5:17])
            f.write('\n\n')

            f.write('Title: ')
            f.write(root[x][0].text)
            f.write('\n\n')

            content = root[x][3].text
            content = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', '', content)
            f.write('Content: ')
            f.write(content)
            f.write('\n\n')

            f.write('***')
            f.write('\n\n')
