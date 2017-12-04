#!/usr/bin/env python3

import csv

page = '''
<header>
  <h2>Finalists</h2>
</header>
'''

map_url_ignore = len('http://miamibaywalk.poepublic.com')

with open('data/miamiddafinalists.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['finalist'] == 'no':
            continue

        page += '''
        <article class="finalist">
          <header>
            <h3 class="title">{title}</h3>
            <span class="author">by {submitter}</span>
          </header>

          {conditional_image}
          <p class="description">{description}</p>

          <div class="proposal-link"><a href="{map_url}">View proposal</a></div>
        </article>
        '''.format(
            title=row['updated_title'],
            submitter=row['updated_submitter_name'],
            description=row['updated_description'],
            map_url=row['map_url'][map_url_ignore:],
            conditional_image=('<img src="{}">'.format('/static/images/finalists/' + row['updated_image'] or row['image'])
                if (row['updated_image'] or row['image']) else '')
        )

print(page)
