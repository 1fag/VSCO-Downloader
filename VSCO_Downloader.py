import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from os import makedirs, listdir
from os.path import isdir, isfile
from time import sleep


def save_vsco_elements(elements, path):
    files = listdir(path)
    for y, x in enumerate(elements):
        print('Downloading File ' + str(y + 1) + ' of ' + str(len(elements)))
        img_resize = x['src'].find('?')
        if img_resize == -1:
            img_url = 'http:' + x['src']
        else:
            img_url = 'http:' + x['src'][:img_resize]
        r = requests.get(img_url, allow_redirects=True)
        if path[-1] != '/':
            path += '/'
        filename = r.url[r.url.rfind('/') + 1:]
        if filename in files:
            print('Found all new files.\n')
            return True
        print(r.url)
        print(path + r.url[r.url.rfind('/') + 1:])
        if not isfile(path + r.url[r.url.rfind('/') + 1:]):
            open(path + filename, 'wb').write(r.content)
    return False

    print('Done.\n')


def update_users():
    usernames = listdir('Users')
    for user in usernames:
        get_media('https://vsco.co/' + user + '/images/1', user)

    print('\n-' * 30)
    print('All profiles updated successfully')
    print('Total profiles updated: ' + str(len(usernames)))
    print('-' * 30)
    sleep(2)

def get_media(profile_url, username):
    print('-' * 30)
    print('Downloading media for user: ' + username)
    next_page = int(profile_url[profile_url.rfind('/') + 1:]) + 1

    print('Initializing HTML session...')
    session = HTMLSession()

    print('Establishing connection with VSCO servers...')
    site = session.get(profile_url, allow_redirects=True)
    print('Rendering JavaScript...')
    site.html.render()
    print('Parsing HTML...')
    page = bs(site.html.html, 'html5lib')

    print('Searching for Images...')
    images = page.findAll('img', {'class': 'css-1nb43sd disableSave-mobile'})
    print('Searching for Videos...')
    videos = page.findAll('source', {'type': 'video/mp4'})
    if next_page == 2:
        print('Searching for Profile Pic...')
        profile_pic = page.findAll('img', {'class': 'css-147a4kv'})

    # Check if User Exists
    if images == [] and videos == []:
        if next_page - 1 > 1:
            session.close()
            return True
        else:
            session.close()
            return False

    # Create Dirs
    if next_page == 2:
        print('Making new directories...')
        if not isdir('Users/' + username + '/ProfilePics'):
            makedirs('Users/' + username + '/ProfilePics')
        if not isdir('Users/' + username + '/Images'):
            makedirs('Users/' + username + '/Images')
        if not isdir('Users/' + username + '/Videos'):
            makedirs('Users/' + username + '/Videos')


    # Download Profile Pic
    if next_page == 2:
        print('\nDownloading Profile Pic:')
        save_vsco_elements(profile_pic, 'Users/' + username + '/ProfilePics')
        
    # Download Images
    print('Downloading Images:')
    if save_vsco_elements(images, 'Users/' + username + '/Images'):
        return True

    # Download Videos
    print('Videos')
    if save_vsco_elements(videos, 'Users/' + username + '/Videos'):
        return True

    # Check for additional pages of media
    print('Attempting to download page ' + str(next_page) + '...')
    session.close()
    return get_media('https://vsco.co/' + username + '/images/' + str(next_page), username)


# --------------------------------------------------------------------
username = str(input('Type VSCO Username: '))
if username == 'update':
    update_users()
else:
    media = get_media('https://vsco.co/' + username + '/images/1', username)

    if not media:
        print('Error: Username not found. Try Again!')
    else:
        print('\n' + '-' * 30)
        print('Media downloaded for user: ' + username)
        print(str(len(listdir('Users/' + username + '/Images'))) + ' image(s) downloaded')
        print(str(len(listdir('Users/' + username + '/Videos'))) + ' video(s) downloaded')
        print(str(len(listdir('Users/' + username + '/ProfilePics'))) + ' profile pic downloaded')
        print('\n' + '-' * 30)
        sleep(2)















