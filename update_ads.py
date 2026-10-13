import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/50b964409b6e221e210634eca4b74c9d"></script>
<script data-cfasync="false" src="https://bauval.org/14/718034770aae2c225d19654bce959bf6"></script>
<script>
  atOptions = {
    'key' : '7d2682caba5dfd4da0bbc18b3e9f38c9',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/7d2682caba5dfd4da0bbc18b3e9f38c9"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-50b964409b6e221e210634eca4b74c9d"></div>
</div>'''

files = ['index.html', 'weapons.html', 'monsters.html', 'armor.html', 'quests.html', 'systems.html', 'collectibles.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '7d2682caba5dfd4da0bbc18b3e9f38c9' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-50b964409b6e221e210634eca4b74c9d' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
